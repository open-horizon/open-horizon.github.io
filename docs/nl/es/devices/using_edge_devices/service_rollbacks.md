---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Actualización de un servicio periférico con retrotracción
{: #service_rollback}

Los servicios en nodos periférico suelen realizar funciones críticas, de modo que cuando se implanta una
nueva versión de un servicio periférico en muchos nodos periféricos, es importante supervisar el éxito del
despliegue y, si falla en cualquier nodo periférico, devolver el nodo a la versión anterior del servicio periférico. {{site.data.keyword.edge_notm}}
puede hacerlo automáticamente. En los patrones o las políticas de despliegue, puede definir qué versión o versiones
de servicio anteriores se deben utilizar cuando falla una nueva versión de servicio.

El contenido siguiente proporciona detalles adicionales sobre cómo implantar una nueva versión de un
servicio periférico existente y las mejores prácticas de desarrollo de software para actualizar los
valores de retrotracción en las políticas de despliegue o patrón.

## Creación de una nueva definición de servicio periférico
{: #creating_edge_service_definition}

Tal como se explica en los apartados [Desarrollo de servicios periféricos con {{site.data.keyword.edge_notm}}](../developing/developing.md) y [Detalles de desarrollo](../developing/developing_details.md), los pasos principales para publicar una nueva versión de un servicio periférico son:

- Edite el código de servicio periférico según sea necesario para la nueva versión.
- Edite el número de versión semántico del código en la variable de versión de servicio en el archivo de configuración **hzn.json**.
- Vuelva a crear los contenedores de servicio.
- Firme y publique la nueva versión de servicio periférico en Horizon Exchange.

## Actualización de valores de retrotracción en la política de despliegue o patrón
{: #updating_rollback_settings}

Un servicio periférico nuevo especifica el número de versión en el campo
`version` de la definición de servicio.

Los patrones o las políticas de despliegue determinan qué servicios se despliegan en determinados
nodos periféricos. Para utilizar las prestaciones de retrotracción de servicio periférico,
debe añadir la referencia para el número de versión de servicio nuevo a la sección
**serviceVersions** en los archivos de configuración de política de despliegue o patrón.

Cuando un servicio periférico se despliega en nodo periférico como resultado de un patrón o
una política, el agente despliega la versión de servicio con el valor de prioridad superior.

Por ejemplo:

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
      {
        "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
      {
        "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

Se proporcionan variables adicionales en la sección de prioridad. La propiedad `priority_value` establece el orden de qué versión de servicio
se debe probar en primer lugar, en la práctica un número inferior significa una prioridad más alta. El
valor de variable `retries` define el número de veces que Horizon intentará iniciar esta
versión de servicio en el marco de tiempo especificado por `retry_durations` antes de
retrotraer a la siguiente versión de prioridad máxima. La variable `retry_durations` define el intervalo de tiempo específico en segundos. Por
ejemplo, es posible que tres anomalías de servicio en el transcurso de un mes no justifiquen
la retrotracción del servicio a una versión anterior, pero 3 anomalías en 5 minutos pueden ser una indicación de
que hay algo incorrecto en la nueva versión de servicio.

A continuación, vuelva a publicar el patrón de despliegue o actualice la política de despliegue con
los cambios de sección **serviceVersion** en Horizon Exchange.

Observe que también puede verificar la compatibilidad de las actualizaciones de valores de
patrón o política de despliegue con el mandato `deploycheck` de la CLI. Para ver
más detalles, emita: 

```bash
hzn deploycheck -h
```
{: codeblock}

Los agbots de {{site.data.keyword.ieam}} detectan rápidamente los cambios de
patrón de despliegue o de política de despliegue. A continuación, los agbots llegan a cada agente
cuyo nodo periférico esté registrado para ejecutar el patrón de despliegue o sea compatible con
la política de despliegue actualizada. El agbot y el agente se coordinan para descargar los contenedores nuevos, detener y eliminar los contenedores antiguos e iniciar los contenedores nuevos.

Como resultado, los nodos periféricos que están registrados para ejecutar el patrón de despliegue actualizado o
son compatibles con la política de despliegue ejecutan rápidamente la nueva versión de servicio periférico
con el valor de prioridad superior, independientemente de dónde esté ubicado geográficamente el nodo periférico.

## Visualización del progreso de la nueva versión de servicio se está implantando
{: #viewing_rollback_progress}

Consulte repetidamente los acuerdos de dispositivo hasta que se rellenen los campos
`agreement_finalized_time` y `agreement_execution_start_time`: 

```bash
hzn agreement list
```
{: codeblock}

Observe que el acuerdo listado muestra la versión asociada al servicio
y los valores de fecha y hora aparecen en las variables (por ejemplo, "agreement_creation_time": "",)

Además, el campo de versión se llena con la versión de servicio nueva (y operativa) con el
valor de prioridad superior:

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

Para obtener detalles adicionales, puede inspeccionar los registros de sucesos del nodo actual
con el mandato de CLI:

```bash
hzn eventlog list
```
{: codeblock}

Por último, también puede utilizar la
[consola de gestión](../getting_started/accessing_ui.md) para modificar
los valores de las versiones de despliegue de retrotracción. Puede hacerlo al crear una
nueva política de despliegue o visualizando y editando los detalles de política existentes,
incluidos los valores de retrotracciones. Tenga en cuenta que el término "marco de tiempo" en
la sección de retrotracción de la interfaz de usuario es equivalente a "retry_durations" en la CLI.
