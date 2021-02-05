# Simple Microservice Demo


A simple microservice demo hosted on gcp.


## Quick Start

1. Create GCP project (and add billing)

    ```bash
    gcloud project create <PROJECT>
    PROJECT_ID="<your-project-id>"
    gcloud config set project ${PROJECT_ID}
    ```

2. Setup Billing and enable the apis we will be using

    ```bash
    gcloud beta billing accounts list
    gcloud beta billing projects link ${PROJECT_ID} \
                --billing-account ${BILLING_ACCOUNT}

    gcloud services enable 
        deploymentmanager.googleapis.com
        --project ${PROJECT_ID}
    ```

3. create the infrastructure

    ```bash
    gcloud deployment-manager deployments update simple-ms-deployment --config gcp-manifests/deployment.yaml --preview
    ```

## Local Cluster Development

1. Launch Minikube

    ```bash
    skaffold dev
    ```

2. expose front end

    ```bash
    minikube service frontend-external
    ```
