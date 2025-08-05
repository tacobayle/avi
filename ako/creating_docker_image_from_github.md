git clone https://github.com/vmware/load-balancer-and-ingress-services-for-kubernetes.git
cd load-balancer-and-ingress-services-for-kubernetes

# Pull the docker images needed for building AKO
docker pull golang:bullseye
docker pull photon:4.0
docker tag golang:bullseye golang:latest
docker tag photon:4.0 photon:latest

# Check the docker images
sudo docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
photon              4.0                 9e9d04e011c5        8 days ago          42.2MB
photon              latest              9e9d04e011c5        8 days ago          42.2MB
golang              bullseye            050e12fb60cc        12 days ago         769MB
golang              latest              050e12fb60cc        12 days ago         769MB


sudo apt install nodejs

# Make AKO images
make docker
<SNIP>
[+] Building 173.9s (15/15) FINISHED

# I am also building gateway api image. You do not have to.
make ako-gateway-api-docker
<SNIP>
[+] Building 159.8s (14/14) FINISHED

# Check the images
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
ako-gateway-api     latest              10473a26bd1c        About a minute ago   132MB
ako                 latest              b9edd4241284        14 minutes ago       134MB


# Tagging the docker images
sudo docker tag ako tacobayle/ako-main:1.13.1
sudo docker tag ako-gateway-api tacobayle/ako-gateway-api:1.13.1

# Pushing the docker images
docker login 
sudo docker push tacobayle/ako-main:1.13.1
sudo docker push tacobayle/ako-gateway-api:1.13.1

# Creating the helm charts.
# Change the version and appVersion: to 1.13.1
cd helm
vi ako/Chart.yaml

helm package ako
Successfully packaged chart and saved it to: /root/load-balancer-and-ingress-services-for-kubernetes/helm/ako-1.13.1.tgz

# Push helm charts
helm registry login harbor.sfo.rainpole.io:443
helm push /root/load-balancer-and-ingress-services-for-kubernetes/helm/ako-1.13.1.tgz oci://harbor.sfo.rainpole.io:443/ako
Pushed: harbor.sfo.rainpole.io:443/ako/ako:1.13.1
Digest: sha256:3adcef2e13d748c1b227b868e07522df14c72e8bc2a2b1ab229989ec73721c45