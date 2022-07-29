set -ex

kubectl create -f configmap_file.yml
kubectl create -f fastapi_deployment.yml
kubectl create -f fastapi_service.yml