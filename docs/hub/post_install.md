---

copyright:
years: 2020 - 2024
lastupdated: "2024-10-15"
title: "Post-installation"

parent: Install Open Horizon
nav_order: 3
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Post installation configuration

## Prerequisites

- [**jq** ](https://stedolan.github.io/jq/download/){:target="_blank"}{: .externalLink}
- [**git** ](https://git-scm.com/downloads){:target="_blank"}{: .externalLink}
- [**docker** ](https://docs.docker.com/get-docker/){:target="_blank"}{: .externalLink} version 1.13 or greater
- **make**

## Installation verification

1. Complete the steps in [Install {{site.data.keyword.ieam}}](online_installation.md)

## Post installation configuration
{: #postconfig}

At the end of a successful installation, credentials and secrets will be shown once on the screen.  Administrators, please capture this information and save it for future use.  There is no way to recover this.

For future users, prepare a file named `agent-install.cfg` and populate it with the following contents, substituting `${HZN_LISTEN_IP}` and `${HZN_TRANSPORT}` with their values.  This further assumes you are using the default port numbers.

```text
HZN_EXCHANGE_URL=${HZN_TRANSPORT}://${HZN_LISTEN_IP}:3090/v1
HZN_FSS_CSSURL=${HZN_TRANSPORT}://${HZN_LISTEN_IP}:9443/
HZN_AGBOT_URL=${HZN_TRANSPORT}://${HZN_LISTEN_IP}:3111
HZN_SDO_SVC_URL=${HZN_TRANSPORT}://${HZN_LISTEN_IP}:9008/api
HZN_FDO_SVC_URL=${HZN_TRANSPORT}://${HZN_LISTEN_IP}:9008/api
```

## What's Next

Follow the process on the [Gather edge node files](gather_files.md) page to prepare installation media for your edge nodes.
