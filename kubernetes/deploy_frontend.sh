#!/bin/bash
set -ex

kubectl create -f react_deployment.yml
kubectl create -f react_service.yml