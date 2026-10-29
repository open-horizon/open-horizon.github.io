# Watson speech to text

This service listens for the word Watson. When it is detected, the service captures an audio clip and sends it to an instance of Speech to Text. Stop words are removed (optionally), and the transcribed text is sent to Apache Kafka.

## Before you begin

Ensure that your system meets these requirements:

- You must register and unregister by performing the steps in [Preparing an edge device](https://open-horizon.github.io/docs/installing/adding_devices/index.md).
- A USB sound card and microphone is installed on your Raspberry Pi.

This service requires both an instance of Apache Kafka and IBM Speech to Text to run correctly. For instructions about how to deploy an instance of event streams, see [Host CPU load percentage example (cpu2evtstreams)](https://open-horizon.github.io/docs/using_edge_services/cpu_load_example/index.md).

Ensure the necessary Apache Kafka environment variables are set:

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```

The event streams topic this sample uses is `myeventstreams` by default, but you can use any topic by setting the following environment variable:

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```

## Deploying an instance of IBM Speech to Text

If an instance is deployed currently, obtain the access information and set the environment variables, or follow these steps:

1. Navigate to the IBM Cloud.
1. Click **Create resource**.
1. Enter `Speech to Text` in the search box.
1. Select the `Speech to Text` tile.
1. Select a region, select a pricing plan, enter a service name, and click **Create** to provision the instance.
1. After provisioning is complete, click the instance and note the credentials API Key and URL and export them as the following environment variable:

```
export STT_IAM_APIKEY=<speech-to-text-api-key>
export STT_URL=<speech-to-text-url>
```

1. Go to the Getting Started section for instructions of how to test the Speech to Text service.

## Registering your edge device

To run the watsons2text service example on your edge node, you must register your edge node with the `IBM/pattern-ibm.watsons2text-arm` deployment pattern. Perform the steps in the [Using Watson Speech to Text to IBM Event Streams Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) section of the readme file.

## Additional information

The `processtect` example source code is also available in the Horizon GitHub repository as an example for Open Horizondevelopment. This source includes the code for all of the four services that run on the edge nodes for this example.

These services include:

- The [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) service listens and detects the hot word Watson, and then records an audio clip and published it to the mqtt broker.
- The [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) service receives an audio clip and sends it to the IBM Speech to Text service and publishes the deciphered text to the mqtt broker.
- The [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) service runs as a WSGI server takes a JSON object, such as {"text": "how are you today"} and removes common stop words and returns {"result": "how you today"}.
- The [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) service publishes data to Apache Kafka when it receives something on the mqtt topic where it is subscribed.
- The [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) is responsible for all inter-container communication.

## What to do next

- For instructions about building and publishing your own version of the Offline Voice Assistant Edge Service, see [Offline Voice Assistant Edge Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service) . Follow the steps in the `watson_speech2text` directory of the Open Horizon examples repository.
- See the [Open Horizon examples repository](https://github.com/open-horizon/examples) .
