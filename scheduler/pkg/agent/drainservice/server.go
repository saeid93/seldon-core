package drainservice

import (
	"context"
	"fmt"
	"net/http"
	"strconv"
	"sync"

	"github.com/gorilla/mux"
	log "github.com/sirupsen/logrus"
)

const (
	terminateEndpoint = "/terminate"
)

type DrainerService struct {
	server      *http.Server
	port        uint
	logger      log.FieldLogger
	serverReady bool
	// mutex to guard changes to `serverReady`
	muServerReady sync.RWMutex
	triggered     bool
	// mutex to guard changes to `triggered`
	muTriggered sync.Mutex
	// wait group to block consumers of the DrainerService until a call to /terminate has occurred.
	// this is effectively triggering downstream logic in agent
	triggeredWg *sync.WaitGroup
	// wait group to block until the logic of draining models (rescheduling) has finished.
	// this is effectively including agent and scheduler related logic.
	// at this state we should be confident that this server replica (agent) can go down gracefully.
	drainingFinishedWg *sync.WaitGroup
}

func NewDrainerService(logger log.FieldLogger, port uint) *DrainerService {
	triggeredWg := sync.WaitGroup{}
	triggeredWg.Add(1)
	schedulerWg := sync.WaitGroup{}
	schedulerWg.Add(1)
	return &DrainerService{
		port:               port,
		logger:             logger,
		serverReady:        false,
		triggered:          false,
		drainingFinishedWg: &schedulerWg,
		triggeredWg:        &triggeredWg,
	}
}

func (drainer *DrainerService) SetState(state interface{}) {
}

func (drainer *DrainerService) Start() error {
	rtr := mux.NewRouter()
	rtr.HandleFunc(terminateEndpoint, drainer.terminate).Methods("GET")

	drainer.server = &http.Server{
		Addr: ":" + strconv.Itoa(int(drainer.port)), Handler: rtr,
	}
	drainer.logger.Infof("Starting drainer HTTP server on port %d", drainer.port)
	go func() {
		drainer.muServerReady.Lock()
		drainer.serverReady = true
		drainer.muServerReady.Unlock()
		err := drainer.server.ListenAndServe()
		drainer.logger.WithError(err).Info("HTTP drainer service stopped")
		drainer.muServerReady.Lock()
		drainer.serverReady = false
		drainer.muServerReady.Unlock()
	}()
	return nil
}

func (drainer *DrainerService) Ready() bool {
	drainer.muServerReady.RLock()
	defer drainer.muServerReady.RUnlock()
	return drainer.serverReady
}

func (drainer *DrainerService) Stop() error {
	// Shutdown is graceful
	drainer.muServerReady.Lock()
	defer drainer.muServerReady.Unlock()
	err := drainer.server.Shutdown(context.Background())
	drainer.serverReady = false
	return err
}

func (drainer *DrainerService) Name() string {
	return "Agent drainer service"
}

func (drainer *DrainerService) WaitOnTrigger() {
	drainer.triggeredWg.Wait()
}

func (drainer *DrainerService) SetSchedulerDone() {
	drainer.drainingFinishedWg.Done()
}

func (drainer *DrainerService) terminate(w http.ResponseWriter, _ *http.Request) {
	// this is the crux of this service:
	// once someone (e.g. kubelet) calls `\terminate` we trigger downstream logic to drain this particular agent/server
	// the drain logic is defined in pkg/agent/server.go `drainServerReplicaImpl`
	// the flow is:
	// 1. call \terminate (this is atomic)
	// 2. agent (drainOnRequest) is unblocked
	// 3. agent sends an AgentDrain grpc message to scheduler and waits for a reply
	// 4. scheduler reschedules models to a different server and waits for them to be Available
	// 5. grpc message returns to agent
	// 6. agent unblocks logic here
	// 7. \terminate returns
	drainer.muTriggered.Lock()
	defer drainer.muTriggered.Unlock()
	if !drainer.triggered {
		drainer.triggered = true
		drainer.triggeredWg.Done()
	}
	drainer.drainingFinishedWg.Wait()
	fmt.Fprintf(w, "ok\n")
}