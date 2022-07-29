#!/bin/bash

set -ex

IMAGE_NAME="plopezpe/kube-app-backend"

REGISTRY="quay.io"

docker build -t ${REGISTRY}/${IMAGE_NAME}:latest .
docker push ${REGISTRY}/${IMAGE_NAME}