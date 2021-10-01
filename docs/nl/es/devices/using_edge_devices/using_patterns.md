---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilización de patrones
{: #using_patterns}

Normalmente, los patrones de despliegue de servicio se pueden publicar en el hub de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) después de que un desarrollador haya publicado un servicio periférico en Horizon Exchange.

La CLI de hzn proporciona funciones para listar y gestionar patrones en {{site.data.keyword.horizon_exchange}}, incluidos los mandatos para listar, publicar, verificar, actualizar y eliminar patrones de despliegue de servicio. También proporciona una forma de listar y eliminar claves criptográficas asociadas con un patrón de despliegue específico.

Para obtener una lista completa de mandatos de CLI y detalles adicionales:

```
hzn exchange pattern -h
```
{: codeblock}

## Ejemplo

Inicie la sesión y cree (o actualice) un recurso de patrón en {{site.data.keyword.horizon_exchange}}:

```
hzn exchange pattern publish --json-file=JSON-FILE [<distintivos>]
```
{: codeblock}

## Utilización de patrones de despliegue

La utilización de un patrón de despliegue es una manera simple y directa de desplegar un servicio en el nodo periférico. Especifique el servicio de nivel superior, o varios servicios de nivel superior, que se deban desplegar en el nodo periférico y {{site.data.keyword.ieam}} maneja el resto, incluido el despliegue de los servicios dependientes que pueda tener el servicio de nivel superior.

Después de crear y añadir un servicio a {{site.data.keyword.ieam}} Exchange, debe crear un archivo `pattern.json`, similar a:

```
{
  "name": "pattern-ibm.cpu2evtstreams-arm",
  "label": "Patrón de servicio periférico ibm.cpu2evtstreams para arm",
  "description": "Patrón para ibm.cpu2evtstreams para arm",
  "public": true,
  "services": [
    {
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceOrgid": "IBM",
      "serviceArch": "arm",
      "serviceVersions": [
        {
          "version": "1.4.3",
          "priority": {
            "priority_value": 1,
            "retries": 1,
            "retry_durations": 1800,
            "verified_durations": 45
          }
        },
        {
          "version": "1.4.2",
          "priority": {
            "priority_value": 2,
            "retries": 1,
            "retry_durations": 3600
          }
        }
      ]
    }
  ],
  "userInput": [
    {
      "serviceOrgid": "IBM",
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "inputs": [
        {
          "name": "EVTSTREAMS_API_KEY",
          "value": "$EVTSTREAMS_API_KEY"
        },
        {
          "name": "EVTSTREAMS_BROKER_URL",
          "value": "$EVTSTREAMS_BROKER_URL"
        },
        {
          "name": "EVTSTREAMS_CERT_ENCODED",
          "value": "$EVTSTREAMS_CERT_ENCODED"
        }
      ]
    }
  ]
}
```
{: codeblock}

Este código es un ejemplo de un archivo `pattern.json` para el servicio
`ibm.cpu2evtstreams` para dispositivos `arm`. Como se muestra aquí, no es necesario especificar `cpu_percent` y `gps` (servicios dependientes de `cpu2evtstreams`). El archivo `service_definition.json` se encarga de esta tarea, de modo que un nodo periférico registrado satisfactoriamente ejecuta esas cargas de trabajo de forma automática.

El archivo `pattern.json` le permite personalizar los valores de retrotracción en la sección `serviceVersions`. Puede especificar varias versiones anteriores del servicio y dar a cada versión una prioridad para que el nodo periférico se retrotraiga si hay un error con la nueva versión. Además de asignar una prioridad a cada versión de retrotracción, puede especificar cosas como el número y la duración de los reintentos antes de volver a una versión de prioridad inferior del servicio especificado. 

También puede establecer las variables de configuración que el servicio pueda necesitar para funcionar correctamente de forma centralizada al publicar el patrón de despliegue, incluyéndolas en la sección `userInput` cerca de la parte inferior. Cuando el servicio `ibm.cpu2evtstreams` se publica, pasa con él las credenciales necesarias para publicar datos en IBM Event Streams, lo que se puede realizar con:

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

Con el patrón publicado, puede registrar un dispositivo arm en él:

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

Este mandato despliega `ibm.cpu2evtstreams` y los servicios dependientes al nodo.

Nota: Un archivo `userInput.json` no se pasa en el mandato `hzn register` anterior, como lo haría si se estuvieran siguiendo los pasos del ejemplo de repositorio [Utilización de la CPU en el servicio periférico de IBM Event Streams con patrón de despliegue ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern). Dado que las entradas de usuario se han pasado con el patrón en sí, cualquier nodo periférico que se registre automáticamente tiene acceso a esas variables de entorno.

Todas las cargas de trabajo de `ibm.cpu2evtstreams` se pueden detener anulando el registro:

```
hzn unregister -fD
```
{: codeblock}
