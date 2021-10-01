---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Ejemplos de patrón de despliegue
{: #deploy_pattern_ex}

Para ayudarle a empezar con los patrones de despliegue de {{site.data.keyword.edge_devices_notm}}, puede cargar programas de ejemplo como patrones de despliegue.
{:shortdesc}

Intente registrar cada uno de estos patrones de despliegue de ejemplo creados previamente para obtener más información sobre cómo utilizar los patrones de despliegue.

Para registrar un nodo periférico para cualquiera de los ejemplos de patrón de despliegue siguientes, primero debe eliminar cualquier registro de patrón de despliegue existente para el nodo periférico. Ejecute los mandatos siguientes en el nodo periférico para eliminar cualquier registro de patrón de despliegue:
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

Salida de ejemplo:
```
"unconfigured"
```
{: codeblock}

Si la salida del mandato muestra `"unconfiguring"` en lugar de `"unconfigured"`, espere unos minutos y vuelva a ejecutar el mandato. Normalmente el mandato solo tarda unos segundos en completarse. Vuelva a intentar el mandato hasta que la salida muestre `"unconfigured"`.

## Ejemplos
{: #pattern_examples}

* [Hello, world ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld)
  Un ejemplo `"Hello, world."` mínimo para presentarle los patrones de despliegue {{site.data.keyword.edge_devices_notm}}.

* [Porcentaje de carga de CPU de host](cpu_load_example.md)
  Un patrón de despliegue de ejemplo que consume datos de porcentaje de carga de CPU y los hace disponibles a través de {{site.data.keyword.message_hub_notm}}.

* [Radio definida por software](software_defined_radio_ex.md)
  Un ejemplo completo que consume audio de estación de radio, extrae voz y convierte en texto la voz extraída. El ejemplo completa el análisis de emoción sobre el texto y hace que los datos y los resultados estén disponibles a través de una interfaz de usuario en la que puede ver los detalles de los datos para cada nodo periférico. Utilice este ejemplo para obtener más información sobre el proceso periférico.
