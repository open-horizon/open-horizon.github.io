# Installing a microk8s cluster

This content provides a summary of how to install MicroK8s, a lightweight and small Kubernetes cluster, on Ubuntu. (For more information, see the MicroK8s documentation.)

**Note**: This type of edge cluster is meant for development and test because a single worker node Kubernetes cluster does not provide scalability or high availability.

## Procedure

1. Install MicroK8s:

```
sudo snap install microk8s --classic --channel=stable
```

1. If you are not running as root, add your user to the MicroK8s group:

```
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
su - $USER
```

1. Enable dns and storage modules in MicroK8s:

```
microk8s.enable dns
microk8s.enable hostpath-storage
```

**Note**: MicroK8s uses 8.8.8.8 and 8.8.4.4 as upstream name servers by default. If these name servers cannot resolve the management hub hostname, you must change the name servers that MicroK8s is using:

a. Retrieve the list of upstream name servers in `/etc/resolv.conf` or `/run/system/resolve/resolv.conf`

b. Edit coredns configmap in the kube-system namespace. Set the upstream nameservers in the forward section:

```
microk8s.kubectl edit -n kube-system cm/coredns
```

1. Check the status:

```
microk8s.status --wait-ready
```

1. The MicroK8s kubectl command is called microk8s.kubectl to prevent conflicts with an already install kubectl command. Assuming that kubectl is not installed, add this alias for microk8s.kubectl:

```
echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
source ~/.bash_aliases
```

1. Choose the image registry types: remote image registry or edge cluster local registry. Image registry is the place that will hold the agent image and agent cronjob image.
1. [Setting variables to use a remote image registry](https://open-horizon.github.io/docs/installing/setting_remote_image_registry/index.md)
1. [Setup edge cluster local image registry for MicroK8s](https://open-horizon.github.io/docs/installing/setup_microk8s_image_registry/index.md)
