---

copyright:
years: 2020 - 2024
lastupdated: "2024-10-15"
title: "Installing Open Horizon"

parent: Install Open Horizon
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Installing {{site.data.keyword.ieam}} Overview
{: #hub_install_overview}

The [Open Horizon](https://open-horizon.github.io/docs/) [All-in-One (AIO) script](https://open-horizon.github.io/quick-start/) is a tool for installing, restarting, upgrading, and removing all [Open Horizon components](https://open-horizon.github.io/docs/getting_started/overview_oh/).  This includes the Management Hub, the anax Agent, the CLI, and [example services and deployment policies](https://open-horizon.github.io/docs/developing/examples/).  Please note that Open Horizon does not include [a container or model registry](https://open-horizon.github.io/docs/developing/container_registry/), nor an automation solution like Ansible Automation Platform.

Once Open Horizon's Management Hub is running, and at least one Agent is registered with that Hub, you will be able to automatically deploy containerized applications and ML models to the Agent's host.  This is activated by publishing, at minimum, [a Service Definition file](https://open-horizon.github.io/docs/developing/developing_details/#service_definition) describing [a microservice or distributed application](https://open-horizon.github.io/docs/developing/developing_details/#services_deploy_patterns), and [a Deployment Policy](https://open-horizon.github.io/docs/anax/docs/deployment_policy/#deployment-policy) describing the circumstances under which a service can be matched to an edge node.  Once those exist, the act of publishing a deployment policy, or registering a node, will cause services and policies to be evaluated by the AgreementBot looking for potential matches.  If matches are found, proposed, and accepted by all parties, the deployment process begins.

## Installation summary
{: #sum}

* This content describes the steps to deploy the following components.
  * {{site.data.keyword.edge_notm}} Exchange API.
  * {{site.data.keyword.edge_notm}} Agreement Bot (AgBot).
  * {{site.data.keyword.edge_notm}} Cloud Sync Service (CSS).
  * {{site.data.keyword.edge_notm}} FIDO Device Onboard (FDO).
  * {{site.data.keyword.edge_notm}} Secrets Manager.

### Environment Variables
{: #prereq}

You may want to persist configuration variables in a file (example: `mycreds.env`) or in your `.bashrc` or equivalent file.  Exporting the values in the current session will work for this installation only and will not make them available to future sessions.

Ensure that you are running with elevated privileges before setting variables and installing the Hub: `sudo -i`

```shell
export MONGO_IMAGE_TAG=4.0.6
export CSS_IMAGE_TAG=1.10.1-1577
export HZN_LISTEN_IP=132.177.125.232 # <-- use your IP address, not this one
```

NOTE: If you'd like to use TLS 1.3 (https) for secure services, and you're not using macOS, set the following variables.

```shell
export HZN_TRANSPORT=https
export VAULT_DISABLE_TLS=false
```

### Installation

IMPORTANT: At the end of a successful installation, credentials and secrets will be shown once on the screen.  Administrators, please capture this information and save it for future use.  There is no way to recover this.

Here is the one-liner to download and run the install script to install ONLY the Hub, not the Agent and the Examples:

```shell
curl -sSL https://raw.githubusercontent.com/open-horizon/devops/master/mgmt-hub/deploy-mgmt-hub.sh | bash -s -- -A -R -E
```

```text
Flags:
  -c <config-file>   A config file with lines in the form variable=value that set any of the environment variables supported by this script. Takes precedence over the same variables passed in through the environment.
  -A    Do not install the horizon agent package. (It will still install the horizon-cli package.) Without this flag, it will install and register the horizon agent (as well as all of the management hub services).
  -R    Skip registering the edge node. If -A is not specified, it will install the horizon agent.
  -E    Skip loading the horizon example services, policies, and patterns.
  -S    Stop the management hub services and agent (instead of starting them). This flag is necessary instead of you simply running 'docker-compose down' because docker-compose.yml contains environment variables that must be set.
  -P    Purge (delete) the persistent volumes and images of the Horizon services and uninstall the Horizon agent. Can only be used with -S.
  -s    Start the management hub services and agent, without installing software or creating configuration. Intended to be run to restart the services and agent at some point after you have stopped them using -S. (If you want to change the configuration, run this script without any flags.)
  -u    Update any container whose specified version is not currently running.
  -r <container>   Have docker-compose restart the specified container.
  -v    Verbose output.
  -h    Show this usage.
  ```

### Followup

To ensure that the user on the host can see Docker containers, run the following command:

```shell
sudo usermod -aG docker $USER
```

## What's Next

Follow the steps in [post installation](post_install.md) to continue setting up your new management hub.
