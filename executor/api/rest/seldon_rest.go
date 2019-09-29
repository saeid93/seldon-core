package rest

import (
	"github.com/go-logr/logr"
	"github.com/gogo/protobuf/proto"
	"github.com/golang/protobuf/jsonpb"
	"github.com/gorilla/mux"
	"github.com/prometheus/common/log"
	api "github.com/seldonio/seldon-core/executor/api/grpc"
	"github.com/seldonio/seldon-core/executor/api/machinelearning/v1alpha2"
	"github.com/seldonio/seldon-core/executor/predictor"
	"io/ioutil"
	"net/http"
	logf "sigs.k8s.io/controller-runtime/pkg/runtime/log"
)

type SeldonRestApi struct {
	Router *mux.Router
	predictor *v1alpha2.PredictorSpec
	Log logr.Logger
}



func NewSeldonRestApi(predictor *v1alpha2.PredictorSpec) *SeldonRestApi {
	return &SeldonRestApi{
		mux.NewRouter(),
		predictor,
		logf.Log.WithName("SeldonRestApi"),
	}
}

func respondWithJSON(w http.ResponseWriter, code int, payload proto.Message) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(code)

	ma := jsonpb.Marshaler{}
	ma.Marshal(w, payload)
}

// Extract a SeldonMessage proto from the REST request
func (r *SeldonRestApi) getSeldonMessage(req *http.Request) (*api.SeldonMessage, error) {
	var sm api.SeldonMessage
	bodyBytes, err := ioutil.ReadAll(req.Body)
	if err != nil {
		return nil, err
	}
	value := string(bodyBytes)
	if err := jsonpb.UnmarshalString(value, &sm); err != nil {
		return nil, err
	}
	return &sm, nil
}

func (r *SeldonRestApi) Initialise() {
	s := r.Router.PathPrefix("/api/v0.1").Methods("POST").HeadersRegexp("Content-Type", "application/json").Subrouter()
	s.HandleFunc("/predictions", r.predictions)
}


func (r *SeldonRestApi) predictions(w http.ResponseWriter, req *http.Request) {
	r.Log.Info("Prediction called")

	sm, err := r.getSeldonMessage(req)
	if err != nil {
		log.Error("Failed to parse request:",err)
	}

	seldonPredictorProcess := predictor.NewPredictorProcess(r.predictor)

	smResp, respCode, err := seldonPredictorProcess.Execute(r.predictor.Graph,sm)

	if err != nil {
		if smResp != nil && respCode != nil {
			respondWithJSON(w, *respCode, smResp)
		} else if respCode != nil {
			respFailed := api.SeldonMessage{Status:&api.Status{Code: int32(*respCode), Info: err.Error()}}
			respondWithJSON(w, *respCode, &respFailed)
		} else {
			respFailed := api.SeldonMessage{Status:&api.Status{Code: 500, Info: err.Error()}}
			respondWithJSON(w, 500, &respFailed)
		}
	} else {
		respondWithJSON(w,200, smResp)
	}

}