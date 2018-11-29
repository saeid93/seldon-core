import pytest
from model_microservice import get_rest_microservice, SeldonModelGRPC
import json
import numpy as np
from proto import prediction_pb2
from google.protobuf import json_format

class UserObject(object):
    def __init__(self,metrics_ok=True,ret_nparray=False):
        self.metrics_ok = metrics_ok
        self.ret_nparray = ret_nparray
        self.nparray = np.array([1,2,3])
        
    def predict(self,X,features_names):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        if self.ret_nparray:
            return self.nparray
        else:
            print("Predict called - will run identity function")
            print(X)
            return X

    def tags(self):
        return {"mytag":1}

    def metrics(self):
        if self.metrics_ok:
            return [{"type":"COUNTER","key":"mycounter","value":1}]
        else:
            return [{"type":"BAD","key":"mycounter","value":1}]



def test_model_ok():
    user_object = UserObject()
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    rv = client.get('/predict?json={"data":{"ndarray":[]}}')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 200
    assert j["meta"]["tags"] == {"mytag":1}
    assert j["meta"]["metrics"] == user_object.metrics()

def test_model_ok_with_names():
    user_object = UserObject()
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    rv = client.get('/predict?json={"data":{"names":["a","b"],"ndarray":[[1,2]]}}')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 200
    assert j["meta"]["tags"] == {"mytag":1}
    assert j["meta"]["metrics"] == user_object.metrics()

def test_model_bin_data():
    user_object = UserObject()
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    rv = client.get('/predict?json={"binData":"123"}')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 200
    assert "binData" in j
    assert j["meta"]["tags"] == {"mytag":1}
    assert j["meta"]["metrics"] == user_object.metrics()


def test_model_bin_data_nparray():
    user_object = UserObject(ret_nparray=True)        
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    rv = client.get('/predict?json={"binData":"123"}')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 200
    assert j["data"]["ndarray"] == [1, 2, 3]
    assert j["meta"]["tags"] == {"mytag":1}
    assert j["meta"]["metrics"] == user_object.metrics()
    

def test_model_no_json():
    user_object = UserObject()
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    uo = UserObject()
    rv = client.get('/predict?')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 400

def test_model_bad_metrics():
    user_object = UserObject(metrics_ok=False)
    app = get_rest_microservice(user_object,debug=True)
    client = app.test_client()
    rv = client.get('/predict?json={"data":{"ndarray":[]}}')
    j = json.loads(rv.data)
    print(j)
    assert rv.status_code == 400



def test_proto_ok():
    user_object = UserObject()    
    app = SeldonModelGRPC(user_object)
    arr = np.array([1,2])
    datadef = prediction_pb2.DefaultData(
        tensor = prediction_pb2.Tensor(
            shape = (2,1),
            values = arr
        )
    )
    request = prediction_pb2.SeldonMessage(data = datadef)
    resp = app.Predict(request,None)
    jStr = json_format.MessageToJson(resp)
    j = json.loads(jStr)
    print(j)
    assert j["meta"]["tags"] == {"mytag":1}
    # add default type
    j["meta"]["metrics"][0]["type"] = "COUNTER"
    assert j["meta"]["metrics"] == user_object.metrics()
    assert j["data"]["tensor"]["shape"] == [2,1]
    assert j["data"]["tensor"]["values"] == [1,2]


def test_proto_bin_data():
    user_object = UserObject()    
    app = SeldonModelGRPC(user_object)
    binData = b"\0\1"
    request = prediction_pb2.SeldonMessage(binData = binData)
    resp = app.Predict(request,None)
    assert resp.binData == binData

def test_proto_bin_data_nparray():
    user_object = UserObject(ret_nparray=True)    
    app = SeldonModelGRPC(user_object)
    binData = b"\0\1"
    request = prediction_pb2.SeldonMessage(binData = binData)
    resp = app.Predict(request,None)
    jStr = json_format.MessageToJson(resp)
    j = json.loads(jStr)
    print(j)
    assert j["data"]["tensor"]["values"] == list(user_object.nparray.flatten())

    

    
