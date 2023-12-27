# GET STARTED

## Resources

* [Using Cloud Functions with Spanner](https://cloud.google.com/spanner/docs/use-cloud-functions?hl=en&skip_cache=true) 
* [Getting started with Spanner using Python](https://cloud.google.com/spanner/docs/getting-started/python)

## Install `gcloud-cli`

1. `cd GCLOUD_DIRECTORY`
1. `curl -X GET https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-458.0.1-darwin-arm.tar.gz --output google-cloud-cli-458.0.1-darwin-arm.tar.gz`
1. `tar xzf google-cloud-cli-458.0.1-darwin-arm.tar.gz`
1. `./google-cloud-sdk/install.sh`
1. `./google-cloud-sdk/bin/gcloud init`
1. `gcloud auth application-default login`

## Setup things

1. `pip -m venv env`
1. `source env/bin/activate`
1. `(env) ~ pip install -r requirements.txt`
1. `(env) ~ gcloud config set project MY_PROJECT_ID`
1. [Enable Spanner API (via link)](https://console.cloud.google.com/apis/enableflow?apiid=spanner.googleapis.com&_ga=2.103414144.1619621355.1703657989-499465908.1684214670&_gac=1.79913701.1702108251.CjwKCAiAmsurBhBvEiwA6e-WPLDPmVeNyXLtZgcbr9Z-FGHtdxuNBqstoCbQbdJKTk1xYhD7sYlqWxoCKOMQAvD_BwE&project=hallta-on-gcp) 
