Use a custom AKO image:
- upload the ako image and install the image on each k8s nodes:

```tanzu cluster kubeconfig get tkg-cluster-workload-1 --admin```

```kubectl config use-context tkg-cluster-workload-1-admin@tkg-cluster-workload-1```

```kubectl get nodes -o json | jq -r .items[].status.addresses[1].address # will list the IP addresses of the K8s nodes```

For each node, do

```scp -i /home/ubuntu/.ssh/cloudKey ./ako_1.9.1-5466-sctp.tar.gz capv@$ip:./ako_1.9.1-5466-sctp.tar.gz```

```sudo ctr -n=k8s.io image import ako_1.9.1-5466-sctp.tar.gz```

```
sudo crictl images
IMAGE                                                                                         TAG                    IMAGE ID            SIZE
docker.io/tacobayle/sctp_server                                                               latest                 6a6ff9efa8b25       215MB
projects.registry.vmware.com/tkg/antrea-advanced-debian                                       <none>                 14124acaf3c32       307MB
projects.registry.vmware.com/tkg/pause                                                        3.6                    30ac17a4f1edb       715kB
projects.registry.vmware.com/tkg/csi/csi-livenessprobe                                        <none>                 577ae8c1ee037       5MB
projects.registry.vmware.com/tkg/csi/csi-node-driver-registrar                                <none>                 1c028e25720a1       5.39MB
10.79.172.11:5000/avi-buildops/ako                                                            1.9.1-5466             265287ac15ad3       116MB
projects.registry.vmware.com/tkg/coredns                                                      v1.8.6_vmware.7        28e1d58a25905       46.9MB
projects.registry.vmware.com/tkg/kube-apiserver                                               v1.23.8_vmware.2       4c4e1c719aecf       136MB
projects.registry.vmware.com/tkg/csi/vsphere-block-csi-driver                                 <none>                 52e4357f40ff8       108MB
projects.registry.vmware.com/tkg/metrics-server                                               <none>                 e044ef92e6c48       29MB
projects.registry.vmware.com/tkg/secretgen-controller                                         <none>                 8c14a70635c99       21.1MB
projects.registry.vmware.com/tkg/etcd                                                         v3.5.4_vmware.6        8f4c1a3d12882       130MB
projects.registry.vmware.com/tkg/kube-controller-manager                                      v1.23.8_vmware.2       f51fc8bf26310       126MB
projects.registry.vmware.com/tkg/kube-proxy                                                   v1.23.8_vmware.2       9dcaa674553fb       114MB
projects.registry.vmware.com/tkg/kube-scheduler                                               v1.23.8_vmware.2       f4d8e95ef5a2c       54.8MB
projects.registry.vmware.com/tkg/tanzu_core/capabilities/capabilities-controller-manager-tf   v0.25.0-23-g6288c751   ef46fa32cc0c8       11.9MB
capv@tkg-cluster-workload-1-md-0-788b5cdfb7-g2llk:~$
```


```git clone https://github.com/vmware/load-balancer-and-ingress-services-for-kubernetes```

```cd load-balancer-and-ingress-services-for-kubernetes/helm```


edit ako/Chart.yaml like the following:

```apiVersion: v2
name: ako
description: A Helm chart for Kubernetes

# A chart can be either an 'application' or a 'library' chart.
#
# Application charts are a collection of templates that can be packaged into versioned archives
# to be deployed.
#
# Library charts provide useful utilities or functions for the chart developer. They're included as
# a dependency of application charts to inject those utilities and functions into the rendering
# pipeline. Library charts do not define any templates and therefore cannot be deployed.
type: application

# This is the chart version. This version number should be incremented each time you make changes
# to the chart and its templates, including the app version.
version: 0.1.0

# This is the version number of the application being deployed. This version number should be
# incremented each time you make changes to the application.
appVersion: 1.9.1-5466
```

edit values.yml like the following:

```
# Default values for ako.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
repository: 10.79.172.11:5000/avi-buildops/ako
pullPolicy: IfNotPresent

### This section outlines the generic AKO settings
AKOSettings:
primaryInstance: true # Defines AKO instance is primary or not. Value `true` indicates that AKO instance is primary. In a multiple AKO deployment in a cluster, only one AKO instance should be primary. Default value: true.
enableEvents: "true" # Enables/disables Event broadcasting via AKO
logLevel: "WARN" # enum: INFO|DEBUG|WARN|ERROR
fullSyncFrequency: "1800" # This frequency controls how often AKO polls the Avi controller to update itself with cloud configurations.
apiServerPort: 8080 # Internal port for AKO's API server for the liveness probe of the AKO pod default=8080
deleteConfig: "false" # Has to be set to true in configmap if user wants to delete AKO created objects from AVI
disableStaticRouteSync: "false" # If the POD networks are reachable from the Avi SE, set this knob to true.
clusterName: "my-cluster" # A unique identifier for the kubernetes cluster, that helps distinguish the objects for this cluster in the avi controller. // MUST-EDIT
cniPlugin: "" # Set the string if your CNI is calico or openshift. enum: calico|canal|flannel|openshift|antrea|ncp
enableEVH: false # This enables the Enhanced Virtual Hosting Model in Avi Controller for the Virtual Services
layer7Only: false # If this flag is switched on, then AKO will only do layer 7 loadbalancing.
# NamespaceSelector contains label key and value used for namespacemigration
# Same label has to be present on namespace/s which needs migration/sync to AKO
namespaceSelector:
```

deploy AKO

```helm install ./ako --generate-name --namespace=avi-system -f ~/yaml/ako-values-workload1.yml``` 
  