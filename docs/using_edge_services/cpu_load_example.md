---

copyright:
years: 2020 - 2023
lastupdated: "2023-02-19"
title: "CPU usage to IBM Event Streams"

parent: Edge service examples
grand_parent: Using edge services
nav_order: 2
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU usage to {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

Host CPU load percentage is an example of a deployment pattern that consumes CPU load percentage data and makes them available through IBM Event Streams.

This edge service repeatedly queries the edge device CPU load and sends the resulting data to [IBM Event Streams ](https://www.ibm.com/cloud/event-streams){:target="_blank"}{: .externalLink}. This edge service can run on any edge node because it does not require specialized sensor hardware.

Before performing this task, register and unregister by performing the steps in [Install the Horizon agent on your edge device](../installing/registration.md)

To gain experience with a more realistic scenario, this cpu2evtstreams example illustrates more aspects of a typical edge service, including:

* Querying dynamic edge device data
* Analyzing edge device data (for example, `cpu2evtstreams` calculates a window average of the CPU load)
* Sending processed data to a central data ingest service
* Automates the acquisition of event stream credentials to securely authenticate data transfer

## Before you begin
{: #deploy_instance}

Before deploying the cpu2evtstreams edge service you need an instance of {{site.data.keyword.message_hub_notm}} running in the cloud to receive its data. Every member of your organization can share one {{site.data.keyword.message_hub_notm}} instance. If the instance is deployed, obtain the access information and set the
environment variables.

### Deploying {{site.data.keyword.message_hub_notm}} in {{site.data.keyword.cloud_notm}}
{: #deploy_in_cloud}

1. Navigate to the {{site.data.keyword.cloud_notm}}.
2. Click **Create resource**.
3. Enter `Event Streams` in the search box.
4. Select the **Event Streams** tile.
5. In **Event Streams**, enter a service name, select a region, select a pricing plan, and click **Create** to provision the instance.
6. After provisioning is complete, click the instance.
7. To create a topic, click the + icon, then name the instance `cpu2evtstreams`.
8. You can either create credentials in your terminal or obtain them if they are already created. To create credentials, click **Service credentials > New credential**. Create a file called `event-streams.cfg` with your new credentials formatted similar to the following codeblock. Although these credentials only need to be created once, save this file for future use by yourself or other team members that might need {{site.data.keyword.event_streams}} access.

   ```bash
   EVTSTREAMS_API_KEY="<the value of api_key>"
   EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}

   For example, from the view credentials pane:

   ```bash
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. After you have created `event-streams.cfg`, set these environment variables in your shell:

   ```bash
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### Testing {{site.data.keyword.message_hub_notm}} in {{site.data.keyword.cloud_notm}}
{: #testing}

1. Install `kafkacat` (https://github.com/edenhill/kcat#install).

2. On a terminal, enter the following to subscribe to the `cpu2evtstreams` topic:

   ```bash
   kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
   ```
   {: codeblock}

3. On a second terminal, publish test content to the `cpu2evtstreams` topic to display it on the original console. For example:

   ```bash
   echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
   ```
   {: codeblock}

## Registering your edge device
{: #reg_device}

To run the cpu2evtstreams service example on your edge node, you must register your edge node with the `IBM/pattern-ibm.cpu2evtstreams` deployment pattern. Perform the steps in the **first** section in [Horizon CPU To {{site.data.keyword.message_hub_notm}} ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md){:target="_blank"}{: .externalLink}.

## Additional information
{: #add_info}

The CPU example source code is available in the [{{site.data.keyword.horizon_open}} examples repository ](https://github.com/open-horizon/examples){:target="_blank"}{: .externalLink} as an example for {{site.data.keyword.edge_notm}} edge service development. This source includes
the code for all three of the services that run on the edge node for this example:

* The cpu service that provides the CPU load percentage data as a REST service on a local private Docker network. For more information, see [Horizon CPU Percent Service ](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent){:target="_blank"}{: .externalLink}.
* The gps service that provides location information from GPS hardware (if available) or a location that is estimated from the edge nodes IP address. The location data is provided as a REST service on a local private Docker network. For more information, see [Horizon GPS Service ](https://github.com/open-horizon/examples/tree/master/edge/services/gps){:target="_blank"}{: .externalLink}.
* The cpu2evtstreams service that uses the REST APIs that are provided by the other two services. This service sends the combined data to an {{site.data.keyword.message_hub_notm}} kafka broker in the cloud. For more information about the service, see [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md){:target="_blank"}{: .externalLink}.
* For more information about the {{site.data.keyword.message_hub_notm}}, see [Event Streams - Overview ](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams){:target="_blank"}{: .externalLink}.

## What to do next
{: #cpu_next}

If you want to deploy your own software to an edge node, you must create your own edge services, and associated deployment pattern or deployment policy. For more information, see [Developing an edge service for devices](../developing/developing.md).
