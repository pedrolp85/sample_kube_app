#!/bin/bash
set -ex

kubectl create -f mysql_secret.yml
kubectl apply -f db_storage.yml
#kubectl apply -f init-db_storage.yml
kubectl create -f mysql_deployment.yml
kubectl create -f mysql_service.yml