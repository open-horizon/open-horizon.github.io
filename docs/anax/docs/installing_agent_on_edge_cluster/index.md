# Installing the agent on an edge cluster

After you have installed and configured your edge cluster, you can install the Open Horizon agent on it. The agent enables the edge cluster to register with the management hub and receive workload deployments. You can install the Open Horizon agent on OpenShift Container Platform, K3s, or MicroK8s. K3s and MicroK8s are small and lightweight Kubernetes cluster solutions.

**Note**: These instructions assume that the management hub is configured to listen on an external IP using SSL transport. For more information about setting up an All-in-1 management hub, see [here](https://open-horizon.github.io/docs/anax/docs/installing_agent_on_edge_cluster/all-in-1-setup.md).
