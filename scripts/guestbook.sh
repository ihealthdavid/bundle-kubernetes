#!/bin/bash

# This script sets up the guestbook example application on Kubernetes as
# deployed by Juju.

set -o errexit
set -o xtrace

# Set the kubernetes master environment variable for the script.
KM="export KUBERNETES_MASTER=http://0.0.0.0"
# Run the script that deploys the guestbook application.
juju run --unit kubernetes-master/0 "${KM}; scripts/guestbook.sh --debug"
# Open TCP port 8000 on the kubernetes minions.
juju run --service kubernetes "open-port 8000"
# Expose the public addresses of the kubernetes minions.
juju expose kubernetes

set +x

echo "Go http://kubernetes-ip-address:8000 to use the guestbook application."
