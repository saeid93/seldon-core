import os
import time
import logging
import pytest
from subprocess import run
from seldon_e2e_utils import (
    wait_for_status,
    wait_for_rollout,
    wait_for_shutdown,
    rest_request_ambassador,
    get_deployment_names,
    initial_rest_request,
    assert_model,
    assert_model_during_op,
    retry_run,
    API_AMBASSADOR,
    API_ISTIO_GATEWAY,
)


def to_resources_path(file_name):
    return os.path.join("..", "resources", file_name)


with_api_gateways = pytest.mark.parametrize(
    "api_gateway", [API_AMBASSADOR, API_ISTIO_GATEWAY], ids=["ambas", "istio"]
)


@pytest.mark.flaky
@with_api_gateways
class TestRollingHttp(object):
    # Test updating a model with a new resource request but same image
    def test_rolling_update3(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace)
        logging.warning("Initial request")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph4.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
            time.sleep(1)
        assert i == 49
        logging.warning("Success for test_rolling_update3")
        run(f"kubectl delete -f ../resources/graph1.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph4.json -n {namespace}", shell=True)

    # Test updating a model with a multi deployment new model
    def test_rolling_update4(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace)
        logging.warning("Initial request")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph5.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
            time.sleep(1)
        assert i == 49
        logging.warning("Success for test_rolling_update4")
        run(f"kubectl delete -f ../resources/graph1.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph5.json -n {namespace}", shell=True)

    # Test updating a model to a multi predictor model
    def test_rolling_update5(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace)
        logging.warning("Initial request")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph6.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert (res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            )
            if (not r.status_code == 200) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            ):
                break
            time.sleep(1)
        assert i < 100
        logging.warning("Success for test_rolling_update5")
        run(f"kubectl delete -f ../resources/graph1.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph6.json -n {namespace}", shell=True)

    # Test updating a model with a new image version as the only change
    def test_rolling_update6(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1svc.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace, expected_deployments=2)
        logging.warning("Initial request")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph2svc.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(100):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert (res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            )
            if (not r.status_code == 200) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            ):
                break
            time.sleep(1)
        assert i < 100
        logging.warning("Success for test_rolling_update6")
        run(f"kubectl delete -f ../resources/graph1svc.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph2svc.json -n {namespace}", shell=True)

    # test changing the image version and the name of its container
    def test_rolling_update7(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1svc.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace, expected_deployments=2)
        logging.warning("Initial request")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph3svc.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(100):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert (res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            )
            if (not r.status_code == 200) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            ):
                break
            time.sleep(1)
        assert i < 100
        logging.warning("Success for test_rolling_update7")
        run(f"kubectl delete -f ../resources/graph1svc.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph3svc.json -n {namespace}", shell=True)

    # Test updating a model with a new resource request but same image
    def test_rolling_update8(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1svc.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace, expected_deployments=2)
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph4svc.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
            time.sleep(1)
        assert i == 49
        logging.warning("Success for test_rolling_update8")
        run(f"kubectl delete -f ../resources/graph1svc.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph4svc.json -n {namespace}", shell=True)

    # Test updating a model with a multi deployment new model
    def test_rolling_update9(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1svc.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace, expected_deployments=2)
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph5svc.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
            time.sleep(1)
        assert i == 49
        logging.warning("Success for test_rolling_update9")
        run(f"kubectl delete -f ../resources/graph1svc.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph5svc.json -n {namespace}", shell=True)

    # Test updating a model to a multi predictor model
    def test_rolling_update10(self, namespace, api_gateway):
        if api_gateway == API_ISTIO_GATEWAY:
            retry_run(
                f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}"
            )
        retry_run(f"kubectl apply -f ../resources/graph1svc.json -n {namespace}")
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace, expected_deployments=2)
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        retry_run(f"kubectl apply -f ../resources/graph6svc.json -n {namespace}")
        r = initial_rest_request("mymodel", namespace, endpoint=api_gateway)
        assert r.status_code == 200
        assert r.json()["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]
        i = 0
        for i in range(50):
            r = rest_request_ambassador("mymodel", namespace, api_gateway)
            assert r.status_code == 200
            res = r.json()
            assert (res["data"]["tensor"]["values"] == [1.0, 2.0, 3.0, 4.0]) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            )
            if (not r.status_code == 200) or (
                res["data"]["tensor"]["values"] == [5.0, 6.0, 7.0, 8.0]
            ):
                break
            time.sleep(1)
        assert i < 100
        logging.warning("Success for test_rolling_update10")
        run(f"kubectl delete -f ../resources/graph1svc.json -n {namespace}", shell=True)
        run(f"kubectl delete -f ../resources/graph6svc.json -n {namespace}", shell=True)


@pytest.mark.flaky
@with_api_gateways
@pytest.mark.parametrize(
    "from_deployment,to_deployment",
    [
        ("graph1.json", "graph2.json"),  # New image version
        ("graph1.json", "graph3.json"),  # New image version and new name of container
        ("graph1.json", "graph4.json"),  # New resource request but same image
        ("graph1.json", "graph8.json"),  # From v1alpha2 to v1
        ("graph7.json", "graph8.json"),  # From v1alpha3 to v1
    ],
)
def test_rolling_update_deployment(
    namespace, api_gateway, from_deployment, to_deployment
):
    if api_gateway == API_ISTIO_GATEWAY:
        retry_run(f"kubectl create -f ../resources/seldon-gateway.yaml -n {namespace}")

    from_file_path = to_resources_path(from_deployment)
    retry_run(f"kubectl apply -f {from_file_path} -n {namespace}")
    wait_for_status("mymodel", namespace)
    wait_for_rollout("mymodel", namespace)
    assert_model("mymodel", namespace, initial=True, endpoint=api_gateway)

    old_deployment_name = get_deployment_names("mymodel", namespace)[0]
    to_file_path = to_resources_path(to_deployment)

    def _update_model():
        retry_run(f"kubectl apply -f {to_file_path} -n {namespace}")
        wait_for_shutdown(old_deployment_name, namespace)
        wait_for_status("mymodel", namespace)
        wait_for_rollout("mymodel", namespace)

    assert_model_during_op(_update_model, "mymodel", namespace, endpoint=api_gateway)

    delete_cmd = f"kubectl delete --ignore-not-found -n {namespace}"
    run(f"{delete_cmd} -f {from_file_path}", shell=True)
    run(f"{delete_cmd} -f {to_file_path}", shell=True)
