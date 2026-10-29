# Installing the agent on K3s and MicroK8s edge clusters

This content describes how to install the Open Horizon agent on [K3s](https://k3s.io/) or [microk8s](https://microk8s.io/) , lightweight and small Kubernetes clusters:

## Prerequisites

- The architecture of the cluster must be one of the following:
- AMD64 (x86_64)
- ARM64 (AArch64)
- ppc64le
- s390x
- Operating system must be modern Linux variant with 64-bit and systemd support

**Note**: Open Horizon cluster agent installation requires cluster admin access on the edge cluster. Additionally, the "jq" command-line JSON processor must be installed prior to running the agent install script.

## Procedure

1. Log in to your edge cluster as **root**.
1. If you don't already have your authorization information, get it now. For details about how to get the authorization information, see [Authentication overview](https://open-horizon.github.io/docs/anax/docs/authentication_overview/index.md).

```
export HZN_ORG_ID=<your-exchange-organization>
export HZN_EXCHANGE_USER_AUTH=<authentication string>
export HZN_EXCHANGE_URL= # example http://open-horizon.lfedge.iol.unh.edu:3090/v1
export HZN_FSS_CSSURL= # example http://open-horizon.lfedge.iol.unh.edu:9443/
```

1. Copy the **agent-install.sh** script to your new edge cluster.

1. The **agent-install.sh** script will store the Open Horizon agent in the edge cluster image registry. Set the full image path (minus the tag) that should be used. For example:

1. On k3s:

   ```
   REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```

1. On microk8s:

   ```
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
   ```

**Note**: The Open Horizon agent image is stored in the local edge cluster registry because the edge cluster Kubernetes needs ongoing access to it, in case it needs to restart it or move it to another pod.

1. Instruct **agent-install.sh** to use the default storage class:

1. On k3s:

   ```
   export EDGE_CLUSTER_STORAGE_CLASS=local-path
   ```

1. On microk8s:

   ```
   export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
   ```

1. Run **agent-install.sh** to get the necessary files from CSS (Cloud Sync Service), install and configure the Horizon agent, and register your edge cluster with policy:

```
./agent-install.sh -D cluster -i 'css:'
```

**Notes**: * To see all of the available flags, run: **./agent-install.sh -h** * If an error occurs causing **agent-install.sh** to not complete successfully, correct the error that is displayed, and run **agent-install.sh** again. If that does not work, run **agent-uninstall.sh** (see [Removing agent from edge cluster](https://open-horizon.github.io/docs/anax/docs/removing_agent_from_cluster/index.md)) before running **agent-install.sh** again.

1. Verify that the agent pod is running:

```
kubectl get namespaces
kubectl -n openhorizon-agent get pods
```

1. Usually, when an edge cluster is registered for policy, but does not have any user-specified node policy, none of the deployment policies deploy edge services to it. This is expected. Proceed to [Deploying services to your edge cluster](https://open-horizon.github.io/docs/anax/docs/deploying_services_cluster/index.md) to set node policy so that an edge service will be deployed to this edge cluster.

## What's next

- [Deploying services to your edge cluster](https://open-horizon.github.io/docs/anax/docs/deploying_services_cluster/index.md)
- [Removing the agent from an edge cluster](https://open-horizon.github.io/docs/anax/docs/removing_agent_from_cluster/index.md)
