---

copyright:
years: 2019
lastupdated: "2020-2-25"

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

Este servicio escucha la palabra Watson. Cuando se detecta, el servicio captura un clip de audio y lo envía a una instancia de Speech to Text.  Las palabras de detención se eliminan (opcionalmente), y el texto transcrito se envía a {{site.data.keyword.event_streams}}.

## Antes de empezar

Asegúrese de que el sistema cumple estos requisitos:

* Debe registrarse y anular su registro realizando los pasos de la [Preparación de un dispositivo periférico](adding_devices.md).
* Se instala una tarjeta de sonido USB y un micrófono en Raspberry Pi. 

Este servicio requiere una instancia de {{site.data.keyword.event_streams}} y, también, IBM Speech to Text para que se ejecute correctamente. Para obtener instrucciones sobre cómo desplegar una instancia de secuencias de sucesos, consulte [Ejemplo de porcentaje de carga de CPU de host (cpu2evtstreams)](../using_edge_services/cpu_load_example.md).  

Asegúrese de que están establecidas las variables de entorno de {{site.data.keyword.event_streams}} necesarias:

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

El tema de secuencias de sucesos que utiliza este ejemplo es `myeventstreams`, de forma predeterminada, pero puede utilizar cualquier tema estableciendo la variable de entorno siguiente:

```
export EVTSTREAMS_TOPIC=<su-nombre-tema>
```
{: codeblock}

## Despliegue de una instancia de IBM Speech to Text
{: #deploy_watson}

Si una instancia está desplegada actualmente, obtenga la información de acceso y establezca las variables de entorno, o siga estos pasos:

1. Vaya hasta IBM Cloud.
2. Pulse **Crear recurso**.
3. Especifique `Speech to Text` en el recuadro de búsqueda.
4. Seleccione el recuadro `Speech to Text`.
5. Seleccione una región, seleccione un plan de precios, especifique un nombre de servicio y pulse **Crear** para suministrar la instancia.
6. Después de completar el suministro, pulse la instancia y anote el URL y la clave de la API de las credenciales y expórtelos como la variable de entorno siguiente:

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>     export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Vaya a la sección Cómo empezar para obtener instrucciones sobre cómo probar el servicio Speech to Text.

## Registro del dispositivo periférico
{: #watson_reg}

Para ejecutar el ejemplo de servicio watsons2text en el nodo periférico, debe registrar el nodo periférico con el patrón de despliegue `IBM/pattern-ibm.watsons2text-arm`. Realice los pasos de la sección [Utilización del servicio Watson Speech to Text a IBM Event Streams con patrón de despliegue](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) del archivo léame.

## Información adicional

El código fuente de ejemplo `processtect` también está disponible en el repositorio Horizon GitHub como ejemplo para el desarrollo de {{site.data.keyword.edge_notm}}. Este código fuente incluye el código para los cuatro servicios que se ejecutan en los nodos periféricos para este ejemplo. 

Estos servicios son:

* El servicio [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) escucha y detecta la palabra activa Watson y, después, registra un clip de audio y lo publica en el intermediario mqtt.
* El servicio [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) recibe un clip de audio, lo envía al servicio IBM Speech to Text y publica el texto descifrado en el intermediario mqtt.
* El servicio [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) se ejecuta como un servidor WSGI, toma un objeto JSON como, por ejemplo, {"text": "how are you today"}, elimina las palabras de detención comunes y devuelve {"result": "how you today"}.
* El servicio [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) publica datos en {{site.data.keyword.event_streams}} cuando recibe algo sobre el tema mqtt al que está suscrito.
* El [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) es responsable de toda la comunicación entre contenedores.

## Qué hacer a continuación

* Para obtener instrucciones sobre cómo crear y publicar su propia versión del servicio periférico de asistente de voz fuera de línea, consulte [Servicio periférico de asistente de voz fuera de línea](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service). Siga los pasos del directorio `watson_speech2text` del repositorio de ejemplos de Open Horizon.

* Consulte el [repositorio de ejemplos de Open Horizon](https://github.com/open-horizon/examples).
