export CLUSTER_NAME = "simple-microservice-demo-k8"


@test "Verify if cluster: ${CLUSTER_NAME} was created " {
    run gcloud container clusters describe "${CLUSTER_NAME}" \
        --region ${REGION} --format="value(name)"
    [[ "$status" -eq 0 ]]
    [[ "$output" =~ "${CLUSTER_NAME}" ]]
}