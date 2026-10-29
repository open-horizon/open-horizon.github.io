# Setting variables to use a remote image registry

Set `USE_EDGE_CLUSTER_REGISTRY` environment variable to `false` to instruct `agent-install.sh` script to use remote image registry. The following environment variables need to be set if use remote image registry:

```
export USE_EDGE_CLUSTER_REGISTRY=false
export EDGE_CLUSTER_REGISTRY_USERNAME=<remote-image-registry-username>
export EDGE_CLUSTER_REGISTRY_TOKEN=<remote-image-registry-password>
export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<remote-image-registry-host>/<repository-name>/amd64_anax_k8s
```

Or for s390x architecture:

```
export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<remote-image-registry-host>/<repository-name>/s390x_anax_k8s
```

## What's next

- [Installing the agent on Red Hat OpenShift Container Platform Kubernetes edge cluster](https://open-horizon.github.io/docs/anax/docs/installing_ocp_edge_cluster_agent/index.md)
- [Installing the agent on K3s and MicroK8s edge clusters](https://open-horizon.github.io/docs/anax/docs/installing_k3s_microk8s_agent/index.md)
