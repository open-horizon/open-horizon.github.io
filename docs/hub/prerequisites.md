---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Prerequisites
description: Documentation for Install {{site.data.keyword.ieam}}
lastupdated: 2025-05-03
nav_order: 1
parent: Install Open Horizon
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Install {{site.data.keyword.ieam}}
{: #hub_install_overview}

You must install and configure a [management hub](../hub/overview.md) before you start the {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) node tasks.

## Installation summary
{: #sum}

* This content describes the steps to deploy the following components.
  * {{site.data.keyword.edge_notm}} Exchange API.
  * {{site.data.keyword.edge_notm}} Agreement Bot (AgBot).
  * {{site.data.keyword.edge_notm}} Cloud Sync Service (CSS).
  * {{site.data.keyword.edge_notm}} FIDO Device Onboard (FDO).
  * {{site.data.keyword.edge_notm}} Secrets Manager.

**Note:** Upgrade from previous versions of {{site.data.keyword.edge_notm}} is not supported.

## Prerequisites
{: #prereq}

Ensure you are using a Debian-based {{site.data.keyword.linux}} distribution such as Ubuntu 20.04 or 22.04 LTS and running on an x86-based micro-architecture. The installation can run on the bare hardware or in a VM.  The Hub **cannot** run on arm64-based hardware.

For installation, you will need to become root, ex. `sudo -i`

Ensure that you know the public or network facing IP address for the local network that other machines will use to connect to the Management Hub. We will set that IP address as `HZN_LISTEN_IP`. If you do not set this in advance, other machines will not be able to connect to the hub.

## What's Next

Continue setting up your new management hub by performing the steps in [Install {{site.data.keyword.ieam}}](online_installation.md).
