---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Servicio de CPU a {{site.data.keyword.message_hub_notm}}
{: #cpu_msg_ex}

En este ejemplo se recopila información de porcentaje de carga de CPU para enviar a {{site.data.keyword.message_hub_notm}}. Utilice este ejemplo para ayudarle a desarrollar sus propias aplicaciones periféricas que envían datos a servicios en la nube.
{:shortdesc}

## Antes de empezar
{: #cpu_msg_begin}

Complete los pasos de requisito previo en [Preparación para crear un servicio periférico](service_containers.md). Como resultado, estas variables de entorno se deben establecer, estos mandatos deben estar instalados y estos archivos deben existir.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedimiento
{: #cpu_msg_procedure}

Este ejemplo forma parte del proyecto de código abierto de [{{site.data.keyword.horizon_open}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/). Siga los pasos de [Creación y publicación de su propia versión del servicio de CPU a IBM Event Streams Edge ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service) y, después, vuelva aquí.

## Lo que ha aprendido en este ejemplo

### Servicios solicitados

El servicio periférico cpu2evtstreams es un ejemplo de un servicio que depende de los otros dos servicios periféricos (**cpu** y **gps**) para llevar a cabo su tarea. Puede ver los detalles para estas dependencias en la sección **requiredServices** del archivo **horizon/service.definition.json**:

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

### Variables de configuración
{: #cpu_msg_config_var}

Para poder ejecutar **cpu2evtstreams** es necesario realizar alguna configuración adicional. Los servicios periféricos pueden declarar variables de configuración, indicando su tipo y proporcionando valores predeterminados. Puede ver estas variables de configuración en **horizon/service.definition.json**, en la sección **userInput**:

```json  
    "userInput": [
        {
            "name": "EVTSTREAMS_API_KEY",
            "label": "La clave API que se va a utilizar al enviar mensajes a la instancia de IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",
            "label": "La lista de URLs separadas por comas que se van a utilizar al enviar mensajes a la instancia de IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",
            "label": "El certificado firmado automáticamente, codificado en base64 que se va a utilizar al enviar mensajes a la instancia de ICP de IBM Event Streams. No es necesario para IBM Cloud Event Streams.",
            "type": "string",
            "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",
            "label": "El tema que se va a utilizar al enviar mensajes a la instancia de IBM Event Streams",
            "type": "string",
            "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",
            "label": "El número de ejemplos que se van a leer antes de calcular el promedio",
            "type": "int",
            "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",
            "label": "El número de segundos entre los ejemplos",
            "type": "int",
            "defaultValue": "2"
        },
        {
            "name": "MOCK",
            "label": "Simular el muestreo de CPU",
            "type": "boolean",
            "defaultValue": "false"
        },
        {
            "name": "PUBLISH",
            "label": "Publicar los ejemplos de CPU en IBM Event Streams",
            "type": "boolean",
            "defaultValue": "true"
        },
        {
            "name": "VERBOSE",
            "label": "Registrar todo lo que ocurre",
            "type": "string",
            "defaultValue": "1"
        }
    ],
```

Es necesarios que las variables de configuración de entrada de usuario como estas tengan valores cuando se inicia el servicio periférico en el nodo periférico. Los valores pueden proceder de cualquiera de estas fuentes (en este orden de prioridad):

1. Un archivo de entrada de usuario especificado con el distintivo **hzn register -f**
2. La sección **userInput** del recurso del nodo periférico en Exchange
3. La sección **userInput** del recurso de política de patrón o de despliegue en
el intercambio
4. El valor predeterminado especificado en el recurso de definición de servicio en Exchange

Cuando ha registrado el dispositivo periférico para este servicio, ha proporcionado un archivo **userinput.json** que ha especificado algunas de las variables de configuración que no tenían valores predeterminados.

### Sugerencias de desarrollo
{: #cpu_msg_dev_tips}

Puede ser útil incorporar variables de configuración al servicio que ayudan a probar
y depurar el servicio. Por ejemplo, los metadatos de este servicio (**service.definition.json**) y este código (**service.sh**) utilizan estas variables de configuración:

* **VERBOSE** aumenta la cantidad de información que se registra mientras se ejecuta
* **PUBLISH** controla si el código intenta enviar mensajes a {{site.data.keyword.message_hub_notm}}
* **MOCK** controla si **service.sh** intenta llamar a las API REST de sus dependencias (los servicios **cpu** y **gps**) o crear datos simulados en su lugar.

La capacidad de simular los servicios de los que depende es opcional, pero puede ser útil para desarrollar y probar componentes en aislamiento a partir de los servicios necesarios. Este enfoque también puede habilitar el desarrollo de un servicio en un tipo de dispositivo en el cual no están presentes los mecanismos de acceso o los sensores de hardware.

La capacidad de desactivar la interacción con los servicios de nube puede ser útil durante el desarrollo
y las pruebas para evitar cargos innecesarios y para facilitar las pruebas en un entorno de DevOps sintético.

## Qué hacer a continuación
{: #cpu_msg_what_next}

* Pruebe los otros ejemplos de servicio periférico en [Desarrollo de servicios periféricos con {{site.data.keyword.edge_devices_notm}}](developing.md).
