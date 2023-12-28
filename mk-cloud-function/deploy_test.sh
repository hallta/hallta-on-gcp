#!/bin/bash

gcloud functions deploy spanner_read_data --runtime python312 --trigger-http