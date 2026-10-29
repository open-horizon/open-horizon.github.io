---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Creating your own hello world edge service
description: Documentation for Creating your own hello world edge service
lastupdated: 2025-05-03
nav_order: 3
parent: Edge services for devices
grand_parent: Developing edge services
---

# Creating your own hello world edge service

The following example uses a simple `Hello World` service to help you learn more about developing for Open Horizon (Open Horizon). With this example, you develop a single edge service that supports three hardware architectures and uses the Horizon development tools.

## Before you begin

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure

This example is part of the [Open Horizon ](https://github.com/open-horizon/) open-source project. Follow the steps in [Building and Publishing Your Own Hello World Example Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) and then return here.

## What to do next

- Try the other edge service examples at [Developing an edge service with Open Horizon](developing.md).
