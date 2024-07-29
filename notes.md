to deploy to aws we need to switch kubectl context
better idea is to have a runner that does this
deployment done with kubectl apply -f infra/k8s

aws eks update-kubeconfig --region eu-central-1 --name silas-deployment

kubectl config get-contexts
kubectl config set current-context minikube