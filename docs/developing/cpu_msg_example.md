---

copyright:
yyears: 2020 - 2022
lastupdated: "2022-03-17"
title: CPU to Apache Kafka service
description: This example collects CPU load percentage information to send to Apache Kafka. Use this example to help you develop your own edge applications that send data to cloud services.

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU to {{site.data.keyword.message_hub_notm}} service
{: #cpu_msg_ex}

This example collects CPU load percentage information to send to {{site.data.keyword.message_hub_notm}}. Use this example to help you develop your own edge applications that send data to cloud services.
{:shortdesc}

## Before you begin
{: #cpu_msg_begin}

Complete the prerequisite steps in [Preparing to create an edge service](service_containers.md). As a result, these environment variables should be set, these commands should be installed, and these files should exist:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## Procedure
{: #cpu_msg_procedure}

This example is part of the [{{site.data.keyword.horizon_open}} ](https://github.com/open-horizon/){:target="_blank"}{: .externalLink} open source project. Follow the steps in [Building and Publishing Your Own Version of the CPU To IBM Event Streams Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service){:target="_blank"}{: .externalLink} and then return here.

## What you learned in this example

### Required services

The cpu2evtstreams edge service is an example of a service that depends on two other edge services (**cpu** and **gps**) to accomplish its task. You can see the details for these dependencies within the **requiredServices** section of the **horizon/service.definition.json** file:

```json
    "requiredServices": [
        {
            "url": "ibm.cpu",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        }
    ],
```
{: codeblock}

### Configuration variables
{: #cpu_msg_config_var}

The **cpu2evtstreams** service requires some configuration before it can run. Edge services can declare configuration variables, stating their type and providing default values. You can see these configuration variables in **horizon/service.definition.json**, in the **userInput** section:

```json  
    "userInput": [
        {
            "name": "EVTSTREAMS_API_KEY",
            "label": "The API key to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",
            "label": "The comma-separated list of URLs to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",
            "label": "The base64-encoded self-signed certificate to use when sending messages to your ICP instance of IBM Event Streams. Not needed for IBM Cloud Event Streams.",
            "type": "string",
            "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",
            "label": "The topic to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",
            "label": "the number of samples to read before calculating the average",
            "type": "int",
            "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",
            "label": "the number of seconds between samples",
            "type": "int",
            "defaultValue": "2"
        },
        {
            "name": "MOCK",
            "label": "mock the CPU sampling",
            "type": "boolean",
            "defaultValue": "false"
        },
        {
            "name": "PUBLISH",
            "label": "publish the CPU samples to IBM Event Streams",
            "type": "boolean",
            "defaultValue": "true"
        },
        {
            "name": "VERBOSE",
            "label": "log everything that happens",
            "type": "string",
            "defaultValue": "1"
        }
    ],
```
{: codeblock}

User input configuration variables like these are required to have values when the edge service is started on the edge node. The values can come from any of these sources (in this precedence order):

1. A user input file specified with the **hzn register -f** flag
2. The **userInput** section of the edge node resource in the exchange
3. The **userInput** section of the pattern or deployment policy resource in the exchange
4. The default value specified in the service definition resource in the exchange

When you registered your edge device for this service, you provided a **userinput.json** file that specified some of the configuration variables that did not have default values.

### Development tips
{: #cpu_msg_dev_tips}

It can be useful to incorporate configuration variables into your service that help test and debug the service. For example, this service's metadata (**service.definition.json**) and code (**service.sh**) use these configuration variables:

* **VERBOSE** increases the amount of information that is logged while it runs
* **PUBLISH** controls whether the code attempts to send messages to {{site.data.keyword.message_hub_notm}}
* **MOCK** controls whether **service.sh** attempts to call the REST APIs of its dependencies (the **cpu** and **gps** services) or create mock data itself instead.

The ability to mock the services that you depend on is optional, but can be helpful to develop and test components in isolation from required services. This approach can also enable development of a service on a device type in which the hardware sensors or actuators are not present.

The ability to turn off interaction with cloud services can be convenient during development and testing to avoid unnecessary charges and to facilitate testing in a synthetic devops environment.

## What to do next
{: #cpu_msg_what_next}

* Try the other edge service examples at [Developing edge services with {{site.data.keyword.edge_notm}}](developing.md).
