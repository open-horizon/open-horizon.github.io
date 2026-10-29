---
copyright: Contributors to the Open Horizon project
years: 2020 - 2025
title: Hello world using model management
description: Documentation for Hello world using model management
lastupdated: 2025-05-03
parent: Model Management Service
grand_parent: Developing edge services
---

# Hello world using model management

This example helps you learn how to develop an Open Horizon service that uses the model management system (MMS). You can use this system to deploy and update the learning machine models that are used by edge services that run on your edge nodes.

## Before you begin

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure

This example is part of the [Open Horizon ](https://github.com/open-horizon/) open-source project. Follow the steps in [Creating Your Own Hello MMS Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md) and then return here.

## What to do next

* Try the other edge service examples at [Developing an edge service for devices](developing.md).

## Further reading

* [Model management system](../developing/model_management_details.md)
