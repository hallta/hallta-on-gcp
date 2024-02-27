#!/bin/bash

gcloud functions deploy hello_world --runtime python312 --trigger-http

# https://us-central1-hallta-on-gcp.cloudfunctions.net/hello_world