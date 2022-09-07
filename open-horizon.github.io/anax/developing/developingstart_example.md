---

copyright:
years: 2020 - 2022
lastupdated: "2022-06-14"
title: Creating your own hello world edge service
description: ""
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Creating your own hello world edge service
{: #dev_start_ex}

The following example uses a simple `Hello World` service to help you learn more about developing for {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). With this example, you develop a single edge service that supports three hardware architectures and uses the {{site.data.keyword.horizon}} development tools.
{:shortdesc}

## Before you begin
{: #dev_start_ex_begin}

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedure
{: #dev_start_ex_procedure}

This example is part of the [{{site.data.keyword.horizon_open}} ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink} open-source project. Follow the steps in [Building and Publishing Your Own Hello World Example Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw){:target="_blank"}{: .externalLink} and then return here.

## What to do next
{: #dev_start_ex_what_next}

- Try the other edge service examples at [Developing an edge service with {{site.data.keyword.edge_notm}}](developing.md).
