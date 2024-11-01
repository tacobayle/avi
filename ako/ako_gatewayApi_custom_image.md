```
root@ubuntuguest:/home/ubuntu/compose# tar -xvf gateway-t1lr.tar.gz
gateway-t1lr/
gateway-t1lr/ako-gateway-api-t1lr.tar.gz
gateway-t1lr/ako/
gateway-t1lr/ako/crds/
gateway-t1lr/ako/crds/ako.vmware.com_multiclusteringresses.yaml
gateway-t1lr/ako/crds/networking.x-k8s.io_gatewayclasses.yaml
gateway-t1lr/ako/crds/ako.vmware.com_ssorules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_clustersets.yaml
gateway-t1lr/ako/crds/ako_vmware.com_l7rules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_httprules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_aviinfrasettings.yaml
gateway-t1lr/ako/crds/networking.x-k8s.io_gateways.yaml
gateway-t1lr/ako/crds/ako.vmware.com_serviceimports.yaml
gateway-t1lr/ako/crds/ako.vmware.com_hostrules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_l4rules.yaml
gateway-t1lr/ako/Chart.yaml
gateway-t1lr/ako/templates/
gateway-t1lr/ako/templates/psppolicy.yaml
gateway-t1lr/ako/templates/gatewayclass.yaml
gateway-t1lr/ako/templates/clusterrole.yaml
gateway-t1lr/ako/templates/ingressclass.yaml
gateway-t1lr/ako/templates/secret.yaml
gateway-t1lr/ako/templates/_helpers.tpl
gateway-t1lr/ako/templates/configmap.yaml
gateway-t1lr/ako/templates/clusterrolebinding.yaml
gateway-t1lr/ako/templates/statefulset.yaml
gateway-t1lr/ako/templates/serviceaccount.yaml
gateway-t1lr/ako/templates/NOTES.txt
gateway-t1lr/ako/values.yaml
root@ubuntuguest:/home/ubuntu/compose#


cd gateway-t1lr/
docker load < ako-gateway-api-t1lr.tar.gz
df9b9ec6ef4b: Loading layer [==================================================>]   42.8MB/42.8MB
b21860d0c618: Loading layer [==================================================>]  18.37MB/18.37MB
031657f267bd: Loading layer [==================================================>]  70.74MB/70.74MB
Loaded image: ako-gateway-api:t1lr-support

root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr# docker tag ako-gateway-api:t1lr-support tacobayle/ako-gateway-api:1.12.1
root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr#
root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr#
root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr# docker login
Authenticating with existing credentials...
WARNING! Your password will be stored unencrypted in /root/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

Login Succeeded
root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr#

root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr# docker push tacobayle/ako-gateway-api:1.12.1
The push refers to repository [docker.io/tacobayle/ako-gateway-api]
031657f267bd: Pushed
b21860d0c618: Pushed
df9b9ec6ef4b: Pushed
1.12.1: digest: sha256:d4e507b4f27a97ab83628ea858fa22f869f97541dd478d40bbfaf96bd0721dc9 size: 953
root@ubuntuguest:/home/ubuntu/compose/gateway-t1lr#

ubuntu@nic-vsphere-nsx-avi-gw:~$ cd ~/avi/ 
ubuntu@nic-vsphere-nsx-avi-gw:~$
ubuntu@nic-vsphere-nsx-avi-gw:~$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi$ tar -xvf gateway-t1lr.tar.gz
gateway-t1lr/
gateway-t1lr/ako-gateway-api-t1lr.tar.gz
gateway-t1lr/ako/
gateway-t1lr/ako/crds/
gateway-t1lr/ako/crds/ako.vmware.com_multiclusteringresses.yaml
gateway-t1lr/ako/crds/networking.x-k8s.io_gatewayclasses.yaml
gateway-t1lr/ako/crds/ako.vmware.com_ssorules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_clustersets.yaml
gateway-t1lr/ako/crds/ako_vmware.com_l7rules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_httprules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_aviinfrasettings.yaml
gateway-t1lr/ako/crds/networking.x-k8s.io_gateways.yaml
gateway-t1lr/ako/crds/ako.vmware.com_serviceimports.yaml
gateway-t1lr/ako/crds/ako.vmware.com_hostrules.yaml
gateway-t1lr/ako/crds/ako.vmware.com_l4rules.yaml
gateway-t1lr/ako/Chart.yaml
gateway-t1lr/ako/templates/
gateway-t1lr/ako/templates/psppolicy.yaml
gateway-t1lr/ako/templates/gatewayclass.yaml
gateway-t1lr/ako/templates/clusterrole.yaml
gateway-t1lr/ako/templates/ingressclass.yaml
gateway-t1lr/ako/templates/secret.yaml
gateway-t1lr/ako/templates/_helpers.tpl
gateway-t1lr/ako/templates/configmap.yaml
gateway-t1lr/ako/templates/clusterrolebinding.yaml
gateway-t1lr/ako/templates/statefulset.yaml
gateway-t1lr/ako/templates/serviceaccount.yaml
gateway-t1lr/ako/templates/NOTES.txt
gateway-t1lr/ako/values.yaml
ubuntu@nic-vsphere-nsx-avi-gw:~/avi$ cd gateway-t1lr/ako/
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr/ako$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr/ako$

ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr/ako$ more Chart.yaml
apiVersion: v2
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
appVersion: 1.12.1
ubuntu@nic-vsphere-nsx-avi-gw:~/tmp/load-balancer-and-ingress-services-for-kubernetes/helm/ako$







ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr/ako$ more /home/ubuntu/tkc/ako_ns2-cluster-1-tenant_values.yml
# Default values for ako.
# This is a YAML-formatted file.
# Declare variables to be passed into your templates.

replicaCount: 1

image:
  repository: projects.registry.vmware.com/ako/ako
  pullPolicy: IfNotPresent

GatewayAPI:
  image:
    repository: tacobayle/ako-gateway-api
    pullPolicy: IfNotPresent

### This section outlines the generic AKO settings
AKOSettings:
  primaryInstance: true # Defines AKO instance is primary or not. Value `true` indicates that AKO instance is primary. In a multiple AKO deployment in a cluster, only one AKO instance should be primary. Defaul
t value: true.
  enableEvents: 'true' # Enables/disables Event broadcasting via AKO
  logLevel:  "WARN" # enum: INFO|DEBUG|WARN|ERROR
  fullSyncFrequency: '1800' # This frequency controls how often AKO polls the Avi controller to update itself with cloud configurations.
  apiServerPort: 8080 # Internal port for AKO's API server for the liveness probe of the AKO pod default=8080
  deleteConfig: 'false' # Has to be set to true in configmap if user wants to delete AKO created objects from AVI
  disableStaticRouteSync: true  # If the POD networks are reachable from the Avi SE, set this knob to true.
  clusterName: ns2-cluster-1-tenant # A unique identifier for the kubernetes cluster, that helps distinguish the objects for this cluster in the avi controller. // MUST-EDIT
  cniPlugin: antrea  # Set the string if your CNI is calico or openshift or ovn-kubernetes. For Cilium CNI, set the string as cilium only when using Cluster Scope mode for IPAM and leave it empty if using Kube
rnetes Host Scope mode for IPAM. enum: calico|canal|flannel|openshift|antrea|ncp|ovn-kubernetes|cilium
  enableEVH: false # This enables the Enhanced Virtual Hosting Model in Avi Controller for the Virtual Services
  layer7Only: true # If this flag is switched on, then AKO will only do layer 7 loadbalancing.
  # NamespaceSelector contains label key and value used for namespacemigration
  # Same label has to be present on namespace/s which needs migration/sync to AKO
  namespaceSelector:
    labelKey: ''
    labelValue: ''
  servicesAPI: false # Flag that enables AKO in services API mode: https://kubernetes-sigs.github.io/service-apis/. Currently implemented only for L4. This flag uses the upstream GA APIs which are not backward
 compatible
                     # with the advancedL4 APIs which uses a fork and a version of v1alpha1pre1
  vipPerNamespace: 'false' # Enabling this flag would tell AKO to create Parent VS per Namespace in EVH mode
  istioEnabled: false # This flag needs to be enabled when AKO is be to brought up in an Istio environment
  # This is the list of system namespaces from which AKO will not listen any Kubernetes or Openshift object event.
  blockedNamespaceList: []
  # blockedNamespaceList:
  #   - kube-system
  #   - kube-public
  ipFamily: '' # This flag can take values V4 or V6 (default V4). This is for the backend pools to use ipv6 or ipv4. For frontside VS, use v6cidr
  useDefaultSecretsOnly: 'false' # If this flag is set to true, AKO will only handle default secrets from the namespace where AKO is installed.
                                 # This flag is applicable only to Openshift clusters.

### This section outlines the network settings for virtualservices.
NetworkSettings:
  ## This list of network and cidrs are used in pool placement network for vcenter cloud.
  ## Node Network details are not needed when in nodeport mode / static routes are disabled / non vcenter clouds.
  #nodeNetworkList: []
  nodeNetworkList: []
  #     cidrs:
  #       - 10.0.0.1/24
  #       - 11.0.0.1/24
  enableRHI: false # This is a cluster wide setting for BGP peering.
  nsxtT1LR: /infra/tier-1s/t1_50240fb5-82cc-448a-8065-d6a8e369daa1_rtr # T1 Logical Segment mapping for backend network. Only applies to NSX-T cloud.
  bgpPeerLabels: [] # Select BGP peers using bgpPeerLabels, for selective VsVip advertisement.
  # bgpPeerLabels:
  #   - peer1
  #   - peer2
  #
  #
  #vipNetworkList: [] # Network information of the VIP network. Multiple networks allowed only for AWS Cloud.
  vipNetworkList:
     - networkName: "vcf-ako-net-domain-c9:1eef2ad0-5bc9-4de4-a573-ffe2785e1db8-ns2"
       cidr: 100.100.134.0/24
  #  - networkName: net1
  #    cidr: 100.1.1.0/24
  #    v6cidr: 2002::1234:abcd:ffff:c0a8:101/64 # Setting this will enable the VS networks to use ipv6

### This section outlines all the knobs  used to control Layer 7 loadbalancing settings in AKO.
L7Settings:
  defaultIngController: 'true'
  noPGForSNI: false # Switching this knob to true, will get rid of poolgroups from SNI VSes. Do not use this flag, if you don't want http caching. This will be deprecated once the controller support caching on
 PGs.
  serviceType: NodePort # enum NodePort|ClusterIP|NodePortLocal
  shardVSSize: SMALL # Use this to control the layer 7 VS numbers. This applies to both secure/insecure VSes but does not apply for passthrough. ENUMs: LARGE, MEDIUM, SMALL, DEDICATED
  passthroughShardSize: SMALL   # Control the passthrough virtualservice numbers using this ENUM. ENUMs: LARGE, MEDIUM, SMALL
  enableMCI: 'false' # Enabling this flag would tell AKO to start processing multi-cluster ingress objects.

### This section outlines all the knobs  used to control Layer 4 loadbalancing settings in AKO.
L4Settings:
  defaultDomain: '' # If multiple sub-domains are configured in the cloud, use this knob to set the default sub-domain to use for L4 VSes.
  autoFQDN: default   # ENUM: default(<svc>.<ns>.<subdomain>), flat (<svc>-<ns>.<subdomain>), "disabled" If the value is disabled then the FQDN generation is disabled.

### This section outlines settings on the Avi controller that affects AKO's functionality.
ControllerSettings:
  serviceEngineGroupName: Default-Group # Name of the ServiceEngine Group.
  controllerVersion: 30.2.2  # The controller API version
  cloudName: dc1_nsx # The configured cloud name on the Avi controller.
  controllerHost: 172.16.31.18  # IP address or Hostname of Avi Controller
  tenantName: ns2   # Name of the tenant where all the AKO objects will be created in AVI.

featureGates:
  GatewayAPI: true

nodePortSelector: # Only applicable if serviceType is NodePort
  key: ''
  value: ''

resources:
  limits:
    cpu: 350m
    memory: 400Mi
  requests:
    cpu: 200m
    memory: 300Mi

securityContext: {}

podSecurityContext: {}

rbac:
  # Creates the pod security policy if set to true
  pspEnable: false


avicredentials:
  username: 'admin'
  password: '$password'
  authtoken:
  certificateAuthorityData:


persistentVolumeClaim: ''
mountPath: /log
logFile: avi.log

ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr/ako$ cd ..
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$ helm install ./ako --generate-name -f /home/ubuntu/tkc/ako_ns2-cluster-1-tenant_values.yml --namespace=avi-system
NAME: ako-1730447759
LAST DEPLOYED: Fri Nov  1 07:56:00 2024
NAMESPACE: avi-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$ k get pod -A
NAMESPACE                      NAME                                                                 READY   STATUS    RESTARTS      AGE
avi-system                     ako-0                                                                2/2     Running   0             5m55s
default                        web-front1-7cdddf9d8-tzqtd                                           1/1     Running   0             59m
default                        web-front1-7cdddf9d8-vn7g6                                           1/1     Running   0             59m
default                        web-front2-67c5b69974-8g85x                                          1/1     Running   0             59m
default                        web-front2-67c5b69974-qrt8g                                          1/1     Running   0             59m
default                        web-front3-5d566d6d8-97hwb                                           1/1     Running   0             59m
default                        web-front3-5d566d6d8-t5r89                                           1/1     Running   0             59m
kube-system                    antrea-agent-qxkn5                                                   2/2     Running   0             81m
kube-system                    antrea-agent-sd6cf                                                   2/2     Running   0             78m
kube-system                    antrea-controller-59bfb878d-vxmkk                                    1/1     Running   0             81m
kube-system                    coredns-7f6d9b9f99-9fvzp                                             1/1     Running   0             89m
kube-system                    coredns-7f6d9b9f99-p9mdc                                             1/1     Running   0             89m
kube-system                    docker-registry-ns2-cluster-1-tenant-gzbn9-9mxsr                     1/1     Running   0             89m
kube-system                    docker-registry-ns2-cluster-1-tenant-node-pool-2-7bbjn-mq7js-xfmxz   1/1     Running   0             78m
kube-system                    etcd-ns2-cluster-1-tenant-gzbn9-9mxsr                                1/1     Running   0             89m
kube-system                    kube-apiserver-ns2-cluster-1-tenant-gzbn9-9mxsr                      1/1     Running   0             89m
kube-system                    kube-controller-manager-ns2-cluster-1-tenant-gzbn9-9mxsr             1/1     Running   0             89m
kube-system                    kube-proxy-64nsw                                                     1/1     Running   0             78m
kube-system                    kube-proxy-fbh65                                                     1/1     Running   0             89m
kube-system                    kube-scheduler-ns2-cluster-1-tenant-gzbn9-9mxsr                      1/1     Running   0             89m
kube-system                    metrics-server-76b87696d8-5vmf9                                      1/1     Running   0             81m
kube-system                    snapshot-controller-6c78fb9567-46jwj                                 1/1     Running   0             82m
secretgen-controller           secretgen-controller-6cbbbdb547-f6dzk                                1/1     Running   0             81m
tkg-system                     kapp-controller-b768df767-d2tsw                                      2/2     Running   0             82m
tkg-system                     tanzu-capabilities-controller-manager-686c77c8f-xjk95                1/1     Running   0             81m
vmware-system-auth             guest-cluster-auth-svc-4wb2m                                         1/1     Running   0             81m
vmware-system-cloud-provider   guest-cluster-cloud-provider-565ccd495d-n72rv                        1/1     Running   0             82m
vmware-system-csi              vsphere-csi-controller-dd99d7b4-p42dk                                7/7     Running   0             82m
vmware-system-csi              vsphere-csi-node-drg5s                                               3/3     Running   3 (81m ago)   82m
vmware-system-csi              vsphere-csi-node-v77wt                                               3/3     Running   0             78m
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$
ubuntu@nic-vsphere-nsx-avi-gw:~/avi/gateway-t1lr$

```

