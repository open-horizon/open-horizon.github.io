---
copyright:
years: 2021 - 2023
lastupdated: "2023-02-17"
layout: page
title: "Quick Start"
description: "A guide to get you using Open Horizon in minutes."

nav_order: 2
has_children: true
has_toc: false
---

### Overview

Open Horizon is a middleware solution designed to manage the deployment and service software lifecycle of containerized applications. It also supports an optional separation of concerns between a service and related machine learning assets by providing a separate [model sync service](/docs/developing/model_management_details.md#model_management_details).  These solutions enable autonomous management of large fleets of edge compute nodes in various connected states.

Open Horizon allows you to install individual tools like the Management Hub control plane, the CLI for remote management using the command-line, or the anax Agent.  If you would like all three installed on a single machine, use the all-in-one installation provided below.

### All-in-one installation instructions

To install a simple, developer-friendly version of [all the services on one device](docs/mgmt-hub/docs/index.md), run the following one-liner as `root` on an x86_64 machine running Ubuntu 18.04 (see [all supported environments](docs/installing/adding_devices.md#suparch-horizon)):

```bash
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash
```

### anax Agent installation instructions

If you've been provided with credentials by an administrator and just need to install the Agent and CLI on your machine, use these steps:

1. Log into your device and set the environment variables given to you, replacing the `<placeholders>` with real values applicable to you:

   ```bash
   export HZN_ORG_ID=<your exchange organization id>
   export HZN_DEVICE_TOKEN=<specify a string value for a token>
   export HZN_DEVICE_ID=<specify a string value to uniquely identify this device>
   export HZN_EXCHANGE_USER_AUTH=<user id>:<password>
   export HZN_EXCHANGE_URL=<management hub protocol and IP address>:3090/v1
   export HZN_FSS_CSSURL=<management hub protocol and IP address>:9443/
   export HZN_AGBOT_URL=<management hub protocol and IP address>:3111
   export HZN_SDO_SVC_URL=<management hub protocol and IP address>:9008/api
   ```

1. Download and run the `agent-install.sh` script to get the necessary files from CSS (Cloud Sync Service), install and configure the Agent, and register your edge device to run the helloworld sample edge service:

   ```bash
   sudo -s -E curl -sSL https://github.com/open-horizon/anax/releases/latest/download/agent-install.sh | bash -s -- -i css: -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```

1. If the CSS on the Hub has not been populated with an Agent for your environment and/or default configuration, you may need to manually create that configuration and then use a slightly different installation technique:

   A. Create a file named `agent-install.cfg` and populate it with the following, replacing the `<placeholders>` with real values applicable to you:

   ```text
   HZN_EXCHANGE_URL=<management hub protocol and IP address>:3090/v1
   HZN_FSS_CSSURL=<management hub protocol and IP address>:9443/
   HZN_AGBOT_URL=<management hub protocol and IP address>:3111
   HZN_SDO_SVC_URL=<management hub protocol and IP address>:9008/api
   ```
  
   B. Download and run the `agent-install.sh` script to install and configure the Agent and register your edge device to run the helloworld sample edge service:

   ```bash
   curl -sSL https://github.com/open-horizon/anax/releases/latest/download/agent-install.sh | bash -s -- -i anax: -k ./agent-install.cfg -c css: -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```

Alternatively, see the [detailed installation instructions](docs/installing/registration.md#registration) for other methods of installing the Agent.

### Common requests

👩‍💻 How to [install Open Horizon](common-requests/install.md)

💻 How to [use Open Horizon](common-requests/use.md)

💾 How to [contribute to the Open Horizon project](common-requests/contribute.md)

🐞 How to [report an issue to Open Horizon](common-requests/report-an-issue.md)

📚 How to [get support for Open Horizon](common-requests/get-technical-support.md)

### Learn more

[Developer Learning Path](docs/getting_started/developer_learning_path.md) page.

From the [Getting Started Overview](docs/getting_started/overview_oh.md) page.

From the [Open-Horizon Project Playlist](https://www.youtube.com/playlist?list=PLgohd895XSUddtseFy4HxCqTqqlYfW8Ix) on YouTube.
