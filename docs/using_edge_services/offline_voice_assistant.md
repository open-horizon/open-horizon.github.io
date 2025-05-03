---
copyright: Contributors to the Open Horizon project
years: 2019 - 2025
title: Offline voice assistant
description: Documentation for Offline voice assistant
lastupdated: 2025-05-03
nav_order: 4
parent: Edge service examples
grand_parent: Using edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Offline voice assistant
{: #offline-voice-assistant}

Every minute, the Offline voice assistant records a five second audio clip, converts the audio clip to text locally on the edge device, and directs the host machine to execute the command and speak the output. 

## Before you begin
{: #before_beginning}

Ensure that your system meets these requirements:

* You must register and unregister by performing the steps in [Preparing an edge device](../installing/adding_devices.md).
* A USB sound card and microphone is installed on your Raspberry Pi. 

## Registering your edge device
{: #reg_edge_device}

To run the `processtext` service example on your edge node, you must register your edge node with the `IBM/pattern-ibm.processtext` deployment pattern. 

Perform the steps in the Using the Offline Voice Assistant Example Edge Service with Deployment Pattern [Using the Offline Voice Assistant Example Edge Service with Deployment Pattern ](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern){:target="_blank"}{: .externalLink} section of the readme file.

## Additional information
{: #additional_info}

The `processtext` example source code is also available in the Horizon GitHub repository as an example for I{{site.data.keyword.edge_notm}} development. This source includes  code for all of the services that run on the edge nodes for this example. 

These [Open Horizon examples ](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio){:target="_blank"}{: .externalLink} services include:

* The [voice2audio ](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio){:target="_blank"}{: .externalLink} service records the five-second audio clip and publishes it to the mqtt broker.
* The [audio2text ](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text){:target="_blank"}{: .externalLink} service uses the audio clip and converts it to text offline using pocket sphinx.
* The [processtext ](https://github.com/open-horizon/examples/tree/master/edge/services/processtext){:target="_blank"}{: .externalLink} service uses the text and attempts to execute the recorded command.
* The [text2speech ](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech){:target="_blank"}{: .externalLink} service plays the output of the command through a speaker.
* The [mqtt_broker ](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker){:target="_blank"}{: .externalLink} manages all inter-container communication.

## What to do next
{: #what_next}

For instructions for building and publishing your own version of Watson speech to text, see the `processtext` directory steps in the [Open Horizon examples ](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service){:target="_blank"}{: .externalLink} repository. 
