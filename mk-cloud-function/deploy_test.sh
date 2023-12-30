#!/bin/bash

gcloud functions deploy spanner_read_data --runtime python312 --trigger-http

# https://us-central1-hallta-on-gcp.cloudfunctions.net/spanner_read_data