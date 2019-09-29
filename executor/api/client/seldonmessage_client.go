package client

import (
	"bytes"
	"github.com/go-logr/logr"
	"github.com/golang/protobuf/jsonpb"
	api "github.com/seldonio/seldon-core/executor/api/grpc"
	"io/ioutil"
	"net"
	"net/http"
	"net/url"
	logf "sigs.k8s.io/controller-runtime/pkg/runtime/log"
	"strconv"
)

const (
	ContentTypeJSON = "application/json"
)

type SeldonMessageClient struct {
	Log logr.Logger
}

func NewSeldonMessageClient() *SeldonMessageClient {
	return &SeldonMessageClient{
		logf.Log.WithName("SeldonMessageClient"),
	}
}

func (smc *SeldonMessageClient) PostHttp(url *url.URL, msg *api.SeldonMessage) (*api.SeldonMessage, *int, error) {
	smc.Log.Info("Calling HTTP","URL",url)

	// Marshall message into JSON
	ma := jsonpb.Marshaler{}
	msgStr, err := ma.MarshalToString(msg)
	if err != nil {
		return nil, nil, err
	}

	// Call URL
	response, err := http.Post(url.String(), ContentTypeJSON, bytes.NewBufferString(msgStr))
	if err != nil {
		return nil, nil, err
	}

	if response.StatusCode != 200 {
		smc.Log.Info("httpPost failed","response code", response.StatusCode)
	}

	//Read response
	b, err := ioutil.ReadAll(response.Body)
	if err != nil {
		return nil, nil, err
	}
	if err = response.Body.Close(); err != nil {
		return nil, nil, err
	}

	// Return SeldonMessage
	var sm api.SeldonMessage
	value := string(b)
	if err := jsonpb.UnmarshalString(value, &sm); err != nil {
		return nil, nil, err
	}
	return &sm, &response.StatusCode, nil
}


func (smc *SeldonMessageClient) Predict(host string, port int32, msg *api.SeldonMessage) (*api.SeldonMessage, *int, error) {
	smc.Log.Info("Predict","port",port)
	url := url.URL{
	Scheme: "http",
	Host:   net.JoinHostPort(host,strconv.Itoa(int(port))),
	Path:   "/predict",
	}
	return smc.PostHttp(&url,msg)
}

