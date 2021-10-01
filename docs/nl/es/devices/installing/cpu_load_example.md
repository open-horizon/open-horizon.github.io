---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Uso de CPU en {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

El porcentaje de carga de CPU de host es un patrón de despliegue de ejemplo que consume los datos de porcentaje de CPU y los hace disponibles a través de IBM Event Streams.

Este servicio periférico consulta repetidamente la carga de CPU de dispositivo periférico y envía los datos
resultantes a [IBM Event Streams
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/event-streams). Este
servicio periférico se puede ejecutar en cualquier nodo periférico porque no necesita hardware de
sensor especializado.

Antes de realizar esta tarea, registre y anule el registro realizando los pasos de [Instalar el agente Horizon en el dispositivo periférico y registrarlo con el ejemplo hello world](registration.md)

Para obtener experiencia con un escenario más realista, este ejemplo de cpu2evtstreams ilustra más aspectos
de un servicio periférico típico, incluyendo:

* Consulta de datos de dispositivo periférico dinámico
* Análisis de datos de dispositivo periférico (por ejemplo, `cpu2evtstreams` calcula una ventana promedio de la carga de CPU)
* Envío de datos procesados a un servicio de ingesta de datos central
* Automatiza la adquisición de credenciales de secuencia de sucesos para autenticar la transferencia de datos de forma segura

## Antes de empezar
{: #deploy_instance}

Antes de desplegar el servicio periférico cpu2evtstreams necesita una instancia de {{site.data.keyword.message_hub_notm}} que se ejecuta en la nube para recibir sus datos. Cada miembro de la organización puede compartir una instancia de {{site.data.keyword.message_hub_notm}}. Si la instancia está desplegada,
obtenga la información de acceso y establezca las variables de entorno.

### Despliegue de {{site.data.keyword.message_hub_notm}} en {{site.data.keyword.cloud_notm}}
{: #deploy_in_cloud}

1. Vaya a {{site.data.keyword.cloud_notm}}.

2. Pulse **Crear recurso**.

3. Especifique `Event Streams` en el cuadro de búsqueda.

4. Seleccione el recuadro **Event Streams**.

5. En **Event Streams** especifique un nombre de servicio, seleccione una ubicación, seleccione un plan de precios y pulse
**Crear** para disponer la instancia.

6. Una vez dispuesta, pulse la instancia.

7. Para crear un tema, pulse el icono + y, a continuación, póngale el nombre
`cpu2evtstreams` a la instancia.

8. Puede crear credenciales en el terminal u obtenerlas si ya se han creado. Para crear credenciales, pulse **Credenciales de servicio > Credenciales nuevas**. Cree
un archivo denominado `event-streams.cfg` con las nuevas credenciales formateadas de forma similar al
siguiente bloque de código. Aunque estas credenciales solo se deben crear una vez, guarde este archivo para que lo utilicen usted u otros miembros del equipo que puedan necesitar acceso de {{site.data.keyword.event_streams}}.

   ```
   EVTSTREAMS_API_KEY="<el valor de api_key>"
    EVTSTREAMS_BROKER_URL="<todos los valores kafka_brokers_sasl en una sola serie, separados por comas>"
   ```
   {: codeblock}
        
   Por ejemplo, en el panel de credenciales de la vista:

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. Después de crear `event-streams.cfg`, establezca estas variables de entorno en el shell:

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### Prueba de {{site.data.keyword.message_hub_notm}} en {{site.data.keyword.cloud_notm}}
{: #testing}

1. Instale `kafkacat`
(https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/).

2. En un terminal, especifique lo siguiente para suscribirse al tema `cpu2evtstreams`:

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. En un segundo terminal, publique contenido de prueba en el tema `cpu2evtstreams` para visualizarlo en la consola original. Por ejemplo:

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## Registro del dispositivo periférico
{: #reg_device}

Para ejecutar el ejemplo de servicio cpu2evtstreams en el nodo periférico, debe registrar el nodo periférico con el patrón de despliegue `IBM/pattern-ibm.cpu2evtstreams`. Siga los pasos de la **primera** sección de [Horizon CPU To {{site.data.keyword.message_hub_notm}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md).

## Información adicional
{: #add_info}

El código fuente de ejemplo de CPU está disponible en el [Repositorio de ejemplos de {{site.data.keyword.horizon_open}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples) como un ejemplo para el desarrollo del servicio periférico {{site.data.keyword.edge_devices_notm}}. Este código fuente incluye el código para los tres servicios que se ejecuta en el nodo periférico para este ejemplo:

  * El servicio cpu que proporciona los datos de porcentaje de carga de CPU como un servicio REST en una red de Docker privada local. Para obtener más información, consulte [Horizon CPU Percent Service ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent).
  * El servicio gps que proporciona información de ubicación del hardware de GPS (si está disponible) o una ubicación estimada a partir de la dirección IP de los nodos periféricos. Los datos de ubicación se proporcionan como un servicio REST en una red Docker privada local. Para obtener más información, consulte [Horizon GPS Service ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/gps).
  * El servicio cpu2evtstreams que utiliza las API REST que proporcionan los otros dos servicios. Este servicio envía los datos combinados a un intermediario Kafka de {{site.data.keyword.message_hub_notm}} en la nube. Para obtener más información acerca del servicio, consulte [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md).
  * Para obtener más información sobre {{site.data.keyword.message_hub_notm}}, consulte [Event Streams - Visión general ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams).

## Qué hacer a continuación
{: #cpu_next}

Si desea desplegar su propio software en un nodo periférico, debe crear sus propios servicios periféricos y el patrón de despliegue asociado o la política de despliegue. Para obtener más información, consulte [Desarrollo de servicios periféricos con {{site.data.keyword.edge_devices_notm}}](../developing/developing.md).
