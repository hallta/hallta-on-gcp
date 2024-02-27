#!/bin/bash

PROJECT_ID="hallta-on-gcp"
REGION="us-central1"
REPO_NAME="example-repo"

#gcloud config set project hallta-on-gcp

#gcloud artifacts repositories create ${REPO_NAME} \
#  --project=${PROJECT_ID} \
#  --repository-format=docker \
#  --location=${REGION} \
#  --description="Cloud Function Quickstart Cloud SQL sample app"

gcloud builds submit \
  --tag ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO_NAME}/function-sql .