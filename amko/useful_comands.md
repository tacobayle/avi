```bash
kubectl delete secret gslb-config-secret -n avi-system
kubectl create secret generic gslb-config-secret --from-file gslb-members -n avi-system
kubectl --kubeconfig gslb-members config get-contexts -n avi-system
```



```bash
helm list -n avi-system
helm uninstall amko-1679996918 -n avi-system

helm uninstall $(helm list -n avi-system | grep amko | cut -d$'\t' -f1) -n avi-system
helm install  ako/amko  --generate-name --version 1.7.1 -f values.yaml  --namespace=avi-system
kubectl logs amko-0 -n avi-system -c amko
```


```bash
sudo systemd-resolve --flush-caches
```
