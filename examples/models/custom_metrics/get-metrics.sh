
kubectl run --quiet=true -it --rm curl --image=tutum/curl --restart=Never -- \
    curl -s seldon-core-analytics-prometheus-seldon.seldon-system/api/v1/query?query=mycounter_total