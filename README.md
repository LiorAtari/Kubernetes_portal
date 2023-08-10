# Kubernetes cluster web portal

This web portal provides information on all of the services running on your Kubernetes cluster.
This information includes - 
1. The IP and port number of the every service in every namespace
2. An HTML link to open that service in a new tab.

## Deployment steps
To deploy the portal, you can choose to manually install or use ArgoCD.

### ArgoCD deployment

To deploy on ArgoCD, Open the UI and create a new app with the following fields:  
```
Application Name: cluster-portal  
Project Name: default  
SYNC POLICY: Which ever you like  
AUTO-CREATE NAMESPACE: Check  
Repository URL: https://github.com/LiorAtari/Kubernetes_portal.git  
Path: ./YAML  
Cluster URL: <Your cluster URL>  
Namespace: "cluster-portal
```

### Manual deployment on Kubernetes
To deploy the portal directly on your cluster, run the following commands:
```
git clone https://github.com/LiorAtari/Kubernetes_portal.git
cd Kubernetes_portal
kubectl create namespace cluster-portal
kubectl apply -f ./YAML
```
