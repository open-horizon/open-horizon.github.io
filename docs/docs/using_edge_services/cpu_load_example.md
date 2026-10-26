---
copyright: Contributors to the Open Horizon project
years: 2020 - 2026
title: CPU usage to IBM Event Streams
description: Documentation for CPU usage to Apache Kafka
lastupdated: 2025-05-03
nav_order: 2
parent: Edge service examples
grand_parent: Using edge services
---

# CPU usage to Apache Kafka

Host CPU load percentage is an example of a deployment pattern that consumes CPU load percentage data and makes them available through IBM Event Streams.

This edge service repeatedly queries the edge device CPU load and sends the resulting data to [IBM Event Streams ](https://www.ibm.com/cloud/event-streams). This edge service can run on any edge node because it does not require specialized sensor hardware.

Before performing this task, register and unregister by performing the steps in [Install the Horizon agent on your edge device](../installing/registration.md)

To gain experience with a more realistic scenario, this cpu2evtstreams example illustrates more aspects of a typical edge service, including:

* Querying dynamic edge device data
* Analyzing edge device data (for example, `cpu2evtstreams` calculates a window average of the CPU load)
* Sending processed data to a central data ingest service
* Automates the acquisition of event stream credentials to securely authenticate data transfer

## Before you begin

Before deploying the cpu2evtstreams edge service you need an instance of Apache Kafka running in the cloud to receive its data. Every member of your organization can share one Apache Kafka instance. If the instance is deployed, obtain the access information and set the
environment variables.

### Deploying Apache Kafka in IBM Cloud

1. Navigate to the IBM Cloud.
2. Click **Create resource**.
3. Enter `Event Streams` in the search box.
4. Select the **Event Streams** tile.
5. In **Event Streams**, enter a service name, select a region, select a pricing plan, and click **Create** to provision the instance.
6. After provisioning is complete, click the instance.
7. To create a topic, click the + icon, then name the instance `cpu2evtstreams`.
8. You can either create credentials in your terminal or obtain them if they are already created. To create credentials, click **Service credentials > New credential**. Create a file called `event-streams.cfg` with your new credentials formatted similar to the following codeblock. Although these credentials only need to be created once, save this file for future use by yourself or other team members that might need Apache Kafka access.

   ```bash
   EVTSTREAMS_API_KEY="<the value of api_key>"
   EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```

   For example, from the view credentials pane:

   ```bash
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```

9. After you have created `event-streams.cfg`, set these environment variables in your shell:

   ```bash
   eval export $(cat event-streams.cfg)
   ```

### Testing Apache Kafka in IBM Cloud

1. Install [kafkacat ](https://github.com/edenhill/kcat#install).

2. On a terminal, enter the following to subscribe to the `cpu2evtstreams` topic:

   ```bash
   kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
   ```

3. On a second terminal, publish test content to the `cpu2evtstreams` topic to display it on the original console. For example:

   ```bash
   echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
   ```

## Registering your edge device

To run the cpu2evtstreams service example on your edge node, you must register your edge node with the `IBM/pattern-ibm.cpu2evtstreams` deployment pattern. Perform the steps in the **first** section in [Horizon CPU To Apache Kafka ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md).

## Additional information

The CPU example source code is available in the [Open Horizon examples repository ](https://github.com/open-horizon/examples) as an example for Open Horizon edge service development. This source includes
the code for all three of the services that run on the edge node for this example:

* The cpu service that provides the CPU load percentage data as a REST service on a local private Docker&reg; network. For more information, see [Horizon CPU Percent Service ](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent).
* The gps service that provides location information from GPS hardware (if available) or a location that is estimated from the edge nodes IP address. The location data is provided as a REST service on a local private Docker&reg; network. For more information, see [Horizon GPS Service ](https://github.com/open-horizon/examples/tree/master/edge/services/gps).
* The cpu2evtstreams service that uses the REST APIs that are provided by the other two services. This service sends the combined data to an Apache Kafka kafka broker in the cloud. For more information about the service, see [Horizon CPU To Apache Kafka Service ](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md).
* For more information about the Apache Kafka, see [Event Streams - Overview ](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams).

## What to do next

If you want to deploy your own software to an edge node, you must create your own edge services, and associated deployment pattern or deployment policy. For more information, see [Developing an edge service for devices](../developing/developing.md).
