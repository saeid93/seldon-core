package controllers

import (
	machinelearningv1 "github.com/seldonio/seldon-core/operator/apis/machinelearning.seldon.io/v1"
	"github.com/seldonio/seldon-core/operator/constants"
	v1 "k8s.io/api/core/v1"
)

const (
	MLServerSklearnImplementation = "mlserver.models.SKLearnModel"
	MLServerXgboostImplementation = "mlserver.models.XGBoostModel"
)

func getMLServerEnvVars(pu *machinelearningv1.PredictiveUnit) []v1.EnvVar {
	httpPort := getMLServerPort(pu, machinelearningv1.REST)
	grpcPort := getMLServerPort(pu, machinelearningv1.GRPC)

	return []v1.EnvVar{
		{
			Name:  "MLSERVER_HTTP_PORT",
			Value: string(httpPort),
		},
		{
			Name:  "MLSERVER_GRPC_PORT",
			Value: string(grpcPort),
		},
		{
			Name:  "MLSERVER_MODEL_IMPLEMENTATION",
			Value: getMLServerModelImplementation(pu),
		},
		{
			Name:  "MLSERVER_MODEL_URI",
			Value: DefaultModelLocalMountPath,
		},
	}
}

func getMLServerPort(pu *machinelearningv1.PredictiveUnit, endpointType machinelearningv1.EndpointType) int32 {
	if pu.Endpoint.Type == endpointType {
		return pu.Endpoint.ServicePort
	}

	// TODO: Error if something else
	switch endpointType {
	case machinelearningv1.REST:
		return constants.MLServerDefaultHttpPort
	case machinelearningv1.GRPC:
		return constants.MLServerDefaultGrpcPort
	}

	return 0
}

func getMLServerModelImplementation(pu *machinelearningv1.PredictiveUnit) string {
	switch *pu.Implementation {
	case machinelearningv1.PrepackSklearnName:
		return MLServerSklearnImplementation
	case machinelearningv1.PrepackXgboostName:
		return MLServerXgboostImplementation
	}

	// TODO: Error if something else
	return ""
}
