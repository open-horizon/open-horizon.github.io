# Quick Start

Open Horizon manages the deployment and service software lifecycle of containerized applications. It also supports an optional separation of concerns between a service and related machine learning assets through a model sync service. These capabilities enable autonomous management of large fleets of edge compute nodes in various connected states.

You can install individual tools such as the Management Hub control plane, the CLI, or the anax agent. If you want all three on a single machine, use the all-in-one installation below.

## All-in-one installation

To install a developer-friendly version of all services on one device, run the following as `root` on a machine that meets the [system requirements](https://open-horizon.github.io/docs/hub/requirements/index.md):

```
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash
```

## Agent installation

If an administrator has provided credentials and you only need the agent and CLI on your machine:

1. Log into your device and set the environment variables you were given, replacing the placeholders with real values:

```
export HZN_ORG_ID=<your exchange organization id>
export HZN_DEVICE_TOKEN=<specify a string value for a token>
export HZN_DEVICE_ID=<specify a string value to uniquely identify this device>
export HZN_EXCHANGE_USER_AUTH=<user id>:<password>
export HZN_EXCHANGE_URL=<management hub protocol and IP address>:3090/v1
export HZN_FSS_CSSURL=<management hub protocol and IP address>:9443/
export HZN_AGBOT_URL=<management hub protocol and IP address>:3111
export HZN_SDO_SVC_URL=<management hub protocol and IP address>:9008/api
```

1. Download and run `agent-install.sh` to fetch files from CSS, install and configure the agent, and register your edge device to run the helloworld sample edge service:

```
sudo -s -E curl -sSL https://github.com/open-horizon/anax/releases/latest/download/agent-install.sh | bash -s -- -i css: -p IBM/pattern-ibm.helloworld -w '*' -T 120
```

## What's next

- Read the [overview](https://open-horizon.github.io/docs/getting_started/overview_oh/index.md) of Open Horizon architecture and components.
- Explore [installing](https://open-horizon.github.io/docs/installing/installing_edge_nodes/index.md) options for edge devices and clusters.
- Start [developing](https://open-horizon.github.io/docs/developing/index.md) edge services.
