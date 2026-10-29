# Installing an OpenShift Container Platform cluster

1. Install OpenShift Container Platform by following the installation instructions in the [OpenShift Container Platform Documentation](https://docs.openshift.com/container-platform/4.6/welcome/index.html). For information about the required cluster architecture, see [Installing the agent on OpenShift Container Platform Kubernetes edge cluster](https://open-horizon.github.io/docs/anax/docs/installing_ocp_edge_cluster_agent/index.md).
1. Install the Kubernetes CLI (**kubectl**), OpenShift client CLI (**oc**) and Docker on the admin host where you administer your OpenShift Container Platform edge cluster. This is the same host where you run the agent installation script. For more information, see [Installing cloudctl, kubectl, and oc](https://open-horizon.github.io/docs/cli/cloudctl_oc_cli/index.md).
1. Choose the image registry types: remote image registry or edge cluster local registry. Image registry is the place that will hold the agent image and agent cronjob image.
1. [Setting variables to use a remote image registry](https://open-horizon.github.io/docs/installing/setting_remote_image_registry/index.md)
1. [Setup edge cluster local image registry for K3s](https://open-horizon.github.io/docs/installing/setup_k3s_image_registry/index.md)
