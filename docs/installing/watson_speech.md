---

copyright:
years: 2020 - 2023
lastupdated: "2023-02-18"
title: "Watson speech to text"

parent: Edge service examples
grand_parent: Using edge services
nav_order: 5
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson speech to text
{: #watson-speech}

This service listens for the word Watson. When it is detected, the service captures an audio clip and sends it to an instance of Speech to Text.  Stop words are removed (optionally), and the transcribed text is sent to {{site.data.keyword.event_streams}}.

## Before you begin

Ensure that your system meets these requirements:

* You must register and unregister by performing the steps in [Preparing an edge device](adding_devices.md).
* A USB sound card and microphone is installed on your Raspberry Pi.

This service requires both an instance of {{site.data.keyword.event_streams}} and IBM Speech to Text to run correctly. For instructions about how to deploy an instance of event streams, see [Host CPU load percentage example (cpu2evtstreams)](../using_edge_services/cpu_load_example.md).

Ensure the necessary {{site.data.keyword.event_streams}} environment variables are set:

```bash
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

The event streams topic this sample uses is `myeventstreams` by default, but you can use any topic by setting the following environment variable:

```bash
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## Deploying an instance of IBM Speech to Text
{: #deploy_watson}

If an instance is deployed currently, obtain the access information and set the environment variables, or follow these steps:

1. Navigate to the IBM Cloud.
2. Click **Create resource**.
3. Enter `Speech to Text` in the search box.
4. Select the `Speech to Text` tile.
5. Select a region, select a pricing plan, enter a service name, and click **Create** to provision the instance.
6. After provisioning is complete, click the instance and note the credentials API Key and URL and export them as the following environment variable:

    ```bash
    export STT_IAM_APIKEY=<speech-to-text-api-key>
    export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Go to the Getting Started section for instructions of how to test the Speech to Text service.

## Registering your edge device
{: #watson_reg}

To run the watsons2text service example on your edge node, you must register your edge node with the `IBM/pattern-ibm.watsons2text-arm` deployment pattern. Perform the steps in the [Using Watson Speech to Text to IBM Event Streams Service with Deployment Pattern ](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern){:target="_blank"}{: .externalLink} section of the readme file.

## Additional information

The `processtect` example source code is also available in the Horizon GitHub repository as an example for {{site.data.keyword.edge_notm}}development. This source includes the code for all of the four services that run on the edge nodes for this example.

These services include:

* The [hotworddetect ](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection){:target="_blank"}{: .externalLink} service listens and detects the hot word Watson, and then records an audio clip and published it to the mqtt broker.
* The [watsons2text ](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text){:target="_blank"}{: .externalLink} service receives an audio clip and sends it to the IBM Speech to Text service and publishes the deciphered text to the mqtt broker.
* The [stopwordremoval ](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) {:target="_blank"}{: .externalLink}service runs as a WSGI server takes a JSON object, such as {"text": "how are you today"} and removes common stop words and returns {"result": "how you today"}.
* The [mqtt2kafka ](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka){:target="_blank"}{: .externalLink} service publishes data to {{site.data.keyword.event_streams}} when it receives something on the mqtt topic where it is subscribed.
* The [mqtt_broker ](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker){:target="_blank"}{: .externalLink} is responsible for all inter-container communication.

## What to do next

* For instructions about building and publishing your own version of the Offline Voice Assistant Edge Service, see [Offline Voice Assistant Edge Service ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service){:target="_blank"}{: .externalLink}. Follow the steps in the `watson_speech2text` directory of the Open Horizon examples repository.

* See the [Open Horizon examples repository ](https://github.com/open-horizon/examples){:target="_blank"}{: .externalLink}.
