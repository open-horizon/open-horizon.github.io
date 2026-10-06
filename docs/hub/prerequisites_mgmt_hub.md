---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Prerequisites for installing management hub only
description: Documentation for Install {{site.data.keyword.ieam}}
lastupdated: 2026-08-19
nav_order: 1
parent: Installing the management hub only
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

## Prerequisites for installing the management hub only
{: #prereq}

* Ensure that you know the public or network facing IP address for the local network that other machines will use to connect to the Management Hub. We will set that IP address as `HZN_LISTEN_IP`. If you do not set this in advance, other machines will not be able to connect to the hub.
* {{site.data.keyword.edge_notm}} uses Mongo 6. If you want to run {{site.data.keyword.edge_notm}} using only open source tools, you must set a variable to override the version of Mongo. Set the `MONGO_IMAGE_TAG` environment variable to 4.0.6.
* If you are using Podman or any container engine that is not Docker, you must set the `DOCKER_ENGINE` variable appropriately. For example, if you are using Podman, run this command: 
  ```shell
  export DOCKER_ENGINE=podman
  ```

