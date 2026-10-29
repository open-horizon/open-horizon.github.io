# Installing a K3s cluster

This content provides a summary of how to install K3s, a lightweight and small Kubernetes cluster, on [Ubuntu](https://ubuntu.com/download/server). For more information, see [the K3s documentation](https://docs.k3s.io/) .

**Note**: If installed, uninstall kubectl before completing the following steps.

## Procedure

1. Either login as root or elevate to root with `sudo -i`
1. The full hostname of your machine must contain at least two dots. Check the full hostname:

```
hostname
```

If you need to update it (for example, from `k3s` to `k.3.s`), use the following pattern:

```
hostnamectl hostname k.3.s
```

1. Install K3s:

```
curl -sfL https://get.k3s.io | sh -
```

1. Choose the image registry types: remote image registry or edge cluster local registry. Image registry is the place that will hold the agent image and agent cronjob image.
1. [Setting variables to use a remote image registry](https://open-horizon.github.io/docs/installing/setting_remote_image_registry/index.md)
1. [Setup edge cluster local image registry for K3s](https://open-horizon.github.io/docs/installing/setup_k3s_image_registry/index.md)
