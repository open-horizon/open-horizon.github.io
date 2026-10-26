---
copyright: Contributors to the Open Horizon project
years: 2021 - 2026
title: Prerequisites for installing management hub only
description: Documentation for Install Open Horizon
lastupdated: 2026-08-19
nav_order: 1
parent: Installing the management hub only
---

## Prerequisites for installing the management hub only

* Ensure that you know the public or network facing IP address for the local network that other machines will use to connect to the Management Hub. We will set that IP address as `HZN_LISTEN_IP`. If you do not set this in advance, other machines will not be able to connect to the hub.
* Open Horizon uses Mongo 6. If you want to run Open Horizon using only open source tools, you must set a variable to override the version of Mongo. Set the `MONGO_IMAGE_TAG` environment variable to 4.0.6.
* If you are using Podman or any container engine that is not Docker, you must set the `DOCKER_ENGINE` variable appropriately. For example, if you are using Podman, run this command: 
  ```shell
  export DOCKER_ENGINE=podman
  ```

