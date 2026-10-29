# Setup edge cluster local image registry for MicroK8s

**Note**: Skip this section if using remote image registry. Enable the container registry and configure Docker to tolerate the insecure registry.

## Procedure

1. Enable the container registry:

```
microk8s.enable registry
export REGISTRY_ENDPOINT=localhost:32000
export REGISTRY_IP_ENDPOINT=$(kubectl get service registry -n container-registry | grep registry | awk '{print $3;}'):5000
```

1. Install Docker (if not already installed, `docker --version` to check):

```
curl -fsSL get.docker.com | sh
```

1. Install jq (if not already installed):

```
apt-get -y install jq
```

1. Define this registry as insecure to Docker. Create or add to `/etc/docker/daemon.json`:

```
echo "{
    \"insecure-registries\": [ \"$REGISTRY_ENDPOINT\", \"$REGISTRY_IP_ENDPOINT\" ]
}" >> /etc/docker/daemon.json
```

1. Restart Docker to pick up the change:

```
systemctl restart docker
```

## What's next

- [Installing the agent on K3s and MicroK8s edge clusters](https://open-horizon.github.io/docs/anax/docs/installing_k3s_microk8s_agent/index.md)
