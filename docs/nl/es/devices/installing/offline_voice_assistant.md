---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Asistente de voz fuera de línea
{: #offline-voice-assistant}

Cada minuto, el asistente de voz fuera de línea registra un clip de audio de cinco segundos, convierte el clip de audio a texto localmente en el dispositivo periférico e indica a la máquina host que ejecute el mandato y pronuncie la salida. 

## Antes de empezar
{: #before_beginning}

Asegúrese de que el sistema cumple estos requisitos:

* Debe registrarse y anular su registro realizando los pasos de la [Preparación de un dispositivo periférico](adding_devices.md).
* Se instala una tarjeta de sonido USB y un micrófono en Raspberry Pi. 

## Registro del dispositivo periférico
{: #reg_edge_device}

Para ejecutar el ejemplo de servicio `processtext` en el nodo periférico, debe registrar el nodo periférico con el patrón de despliegue `IBM/pattern-ibm.processtext`. 

Realice los pasos de la sección Utilización del servicio periférico de ejemplo de asistente de voz fuera de línea con el patrón de despliegue [Utilización del servicio periférico de ejemplo de asistente de voz fuera de línea con el patrón de despliegue ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) del archivo léame.

## Información adicional
{: #additional_info}

El código fuente de ejemplo `processtext` también está disponible en el repositorio
Horizon GitHub como ejemplo para el desarrollo de {{site.data.keyword.edge_devices_notm}}. Este código fuente incluye código para todos los servicios que se ejecutan en los nodos periféricos para este ejemplo. 

Estos servicios de [Ejemplos de Open Horizon![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) incluyen:

* El servicio
[voice2audio ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) registra el clip de audio de cinco segundos y lo publica
en el intermediario mqtt. 
* El servicio [audio2text ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) utiliza el clip de audio y lo convierte a texto fuera de línea mediante pocketsphinx.
* El servicio [processtext ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) utiliza el texto e intenta ejecutar el mandato registrado.
* El servicio [text2speech ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) reproduce la salida del mandato a través de un altavoz.
* El [mqtt_broker ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) gestiona toda la comunicación entre contenedores.

## Qué hacer a continuación
{: #what_next}

Para obtener instrucciones para construir y publicar su propia versión de Watson Speech To Text, consulte los pasos del directorio `processtext` en el [repositorio de ejemplos de Open Horizon ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service). 
