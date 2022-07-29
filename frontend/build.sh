#!/bin/bash

set -ex

IMAGE_NAME="plopezpe/kube-app-frontend"

REGISTRY="quay.io"

docker build -t ${REGISTRY}/${IMAGE_NAME}:latest .
docker push ${REGISTRY}/${IMAGE_NAME}