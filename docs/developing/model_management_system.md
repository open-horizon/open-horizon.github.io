---

copyright:
years: 2020 - 2022
lastupdated: "2022-03-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello world using model management
{: #model_management_system}

This example helps you learn how to develop an {{site.data.keyword.edge_service}} that uses the model management system (MMS). You can use this system to deploy and update the learning machine models that are used by edge services that run on your edge nodes.
{:shortdesc}

## Before you begin
{: #mms_begin}

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedure
{: #mms_procedure}

This example is part of the [{{site.data.keyword.horizon_open}} ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink} open-source project. Follow the steps in [Creating Your Own Hello MMS Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md){:target="_blank"}{: .externalLink}) and then return here.

## What to do next
{: #mms_what_next}

* Try the other edge service examples at [Developing an edge service for devices](developing.md).

## Further reading

* [Model management system](../developing/model_management_details.md)
