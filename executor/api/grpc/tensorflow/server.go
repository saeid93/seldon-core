package tensorflow

import (
	"context"
	"github.com/go-logr/logr"
	"github.com/golang/protobuf/proto"
	"github.com/pkg/errors"
	"github.com/seldonio/seldon-core/executor/api/client"
	"github.com/seldonio/seldon-core/executor/api/grpc"
	"github.com/seldonio/seldon-core/executor/api/payload"
	"github.com/seldonio/seldon-core/executor/predictor"
	"github.com/seldonio/seldon-core/executor/proto/tensorflow/serving"
	"github.com/seldonio/seldon-core/operator/apis/machinelearning/v1"
	"net/url"
	logf "sigs.k8s.io/controller-runtime/pkg/runtime/log"
)

type GrpcTensorflowServer struct {
	Client    client.SeldonApiClient
	predictor *v1.PredictorSpec
	Log       logr.Logger
	ServerUrl *url.URL
	Namespace string
}

func NewGrpcTensorflowServer(predictor *v1.PredictorSpec, client client.SeldonApiClient, serverUrl *url.URL, namespace string) *GrpcTensorflowServer {
	return &GrpcTensorflowServer{
		Client:    client,
		predictor: predictor,
		Log:       logf.Log.WithName("SeldonGrpcApi"),
		ServerUrl: serverUrl,
		Namespace: namespace,
	}
}

func (g *GrpcTensorflowServer) execute(ctx context.Context, req proto.Message) (payload.SeldonPayload, error) {
	seldonPredictorProcess := predictor.NewPredictorProcess(ctx, g.Client, logf.Log.WithName("GrpcClassify"), grpc.GetEventId(ctx), g.ServerUrl, g.Namespace)
	reqPayload := payload.ProtoPayload{Msg: req}
	return seldonPredictorProcess.Execute(g.predictor.Graph, &reqPayload)
}

func (g *GrpcTensorflowServer) Classify(ctx context.Context, req *serving.ClassificationRequest) (*serving.ClassificationResponse, error) {
	resPayload, err := g.execute(ctx, req)
	if err != nil {
		return nil, err
	}
	return resPayload.GetPayload().(*serving.ClassificationResponse), nil
}

func (g *GrpcTensorflowServer) Regress(ctx context.Context, req *serving.RegressionRequest) (*serving.RegressionResponse, error) {
	resPayload, err := g.execute(ctx, req)
	if err != nil {
		return nil, err
	}
	return resPayload.GetPayload().(*serving.RegressionResponse), nil
}

func (g *GrpcTensorflowServer) Predict(ctx context.Context, req *serving.PredictRequest) (*serving.PredictResponse, error) {
	resPayload, err := g.execute(ctx, req)
	if err != nil {
		return nil, err
	}
	return resPayload.GetPayload().(*serving.PredictResponse), nil
}

// MultiInference API for multi-headed models.
func (g *GrpcTensorflowServer) MultiInference(ctx context.Context, req *serving.MultiInferenceRequest) (*serving.MultiInferenceResponse, error) {
	resPayload, err := g.execute(ctx, req)
	if err != nil {
		return nil, err
	}
	return resPayload.GetPayload().(*serving.MultiInferenceResponse), nil
}

// GetModelMetadata - provides access to metadata for loaded models.
func (g *GrpcTensorflowServer) GetModelMetadata(context.Context, *serving.GetModelMetadataRequest) (*serving.GetModelMetadataResponse, error) {
	return nil, errors.Errorf("not implemented")
}
