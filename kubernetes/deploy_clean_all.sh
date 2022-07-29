#!/bin/bash


kubectl delete deploy fastapi-deployment react-deployment mysql-deployment
kubectl delete service mysql-service fastapi-service react-service

kubectl delete pvc mysql-pv-claim

kubectl delete configmap example-config
kubectl delete secret mysql-secret

kubectl delete pvc mysql-initdb-pv-claim