---
copyright:
years: 2021 - 2023
lastupdated: "2023-02-14"
title: Hello world with a secret
description: This example teaches you how to develop an Open Horizon service that uses secrets. Secrets ensure that login credentials and other sensitive information are kept secure.

parent: Secrets Manager
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Before you begin
{: #secrets_begin}

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedure
{: #secrets_procedure}

This example is part of the [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) open-source project. Follow the steps in [Creating Your Own Hello Secret Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)) and then return here.

## What to do next
{: #secrets_what_next}

* Try the other edge service examples at [Developing an edge service for devices](developing.md).

## Further reading

* [Using Secrets](../developing/secrets_details.md)
