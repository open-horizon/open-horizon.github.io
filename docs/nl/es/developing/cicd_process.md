---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Proceso CI-CD para servicios periféricos
{: #edge_native_practices}

Para el uso efectivo de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) es esencial un conjunto de servicios periféricos en evolución y un proceso de Continuous Integration and Continuous Deployment (CI/CD) sólido es un componente crítico. 

Utilice este contenido para diseñar los bloques de creación disponibles para crear un proceso CI/CD propio. A continuación, obtenga más información sobre este proceso en el repositorio [`open-horizon/examples`](https://github.com/open-horizon/examples).

## Variables de configuración
{: #config_variables}

Como desarrollador de servicio periféricos, tenga en cuenta el tamaño de contenedor de servicios en desarrollo. Basándose en dicha información, es posible que tenga que dividir las características de servicio en contenedores independientes. En esta situación, las variables de configuración que se utilizan para realizar pruebas pueden ayudar a simular los datos que proceden de un contenedor aún no desarrollado. En el [archivo de definición de servicio cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json), puede ver variables de entrada como **PUBLISH** y **MOCK**. Si examina el código `service.sh`, verá que utiliza estas variables de configuración y otras para controlar el comportamiento. **PUBLISH** controla si el código intenta enviar mensajes a IBM Event Streams. **MOCK** controla si service.sh intenta ponerse en contacto con las API REST y sus servicios dependientes (cpu y gps) o si `service.sh` crea datos falsos.

En el momento del despliegue de servicio, puede alterar temporalmente los valores predeterminados de variables de configuración especificándolos en la definición de nodo o en el mandato `hzn register`.

## Compilación cruzada
{: #cross_compiling}

Puede utilizar Docker si desea crear un servicio contenerizado para varias arquitecturas desde una única máquina amd64. De forma similar, puede desarrollar servicios periféricos con lenguajes de programación compilados que soporten la compilación cruzada, por ejemplo Go. Por ejemplo, si está escribiendo código en su Mac (un dispositivo de arquitectura amd64) para un dispositivo arm (un Raspberry Pi), es posible que tenga que crear un contenedor Docker que especifique parámetros como GOARCH para destinarlos a arm. Esta configuración puede evitar errores de despliegue. Consulte [Servicio gps open-horizon](https://github.com/open-horizon/examples/tree/master/edge/services/gps).

## Pruebas
{: #testing}

Las pruebas frecuentes y automatizadas son una parte importante del proceso de desarrollo. Para facilitar las pruebas, puede utilizar el mandato `hzn dev service start` para ejecutar el servicio en un entorno de agente de Horizon simulado. Este enfoque también es útil en entornos de DevOps donde puede ser problemático instalar y registrar el agente de Horizon completo. Este método automatiza las pruebas de servicio en el repositorio `open-horizon examples` con el destino **make test**. Consulte [make test target](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30).


Ejecute **make test** para crear y ejecutar el servicio que utiliza **hzn dev service start**. Después de que se esté ejecutando, [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) supervisa los registros de servicio y localiza los datos que indican que el servicio se está ejecutando correctamente.

## Prueba del despliegue
{: #testing_deployment}

Cuando se está desarrollando una nueva versión de servicio, el acceso a una prueba completa del mundo real es ideal. Para ello, puede desplegar el servicio en nodos periféricos; sin embargo, debido a que se trata de una prueba, es aconsejable no desplegar inicialmente el servicio en todos los nodos periféricos.

Para ello, cree una política de despliegue o un patrón que sólo haga referencia a la nueva versión de servicio. A continuación, registre los nodos de prueba con esta nueva política o patrón. Si se utiliza una política, una de las opciones es establecer una propiedad en un nodo periférico. Por ejemplo, "name": "mode", "value": "testing"), y añadir esa restricción a la política de despliegue ("mode == testing"). Esto le permite estar seguro de que sólo los nodos que se reservan para las pruebas reciben la nueva versión del servicio. 

**Nota**: También puede crear una política de despliegue o un patrón desde la consola de gestión. Consulte [Utilización de la consola de gestión](../console/accessing_ui.md).

## Despliegue de producción
{: #production_deployment}

Después de mover la nueva versión del servicio de una prueba a un entorno de producción, se pueden producir problemas que no se han encontrado durante las pruebas. Los valores de retrotracción de patrón o política de despliegue son útiles para resolver estos problemas. En una sección `serviceVersions` de patrón o de política de despliegue, puede especificar varias versiones anteriores del servicio. Dé a cada versión una prioridad para que el nodo periférico se retrotraiga si hay un error con la nueva versión. Además de asignar una prioridad a cada versión de
retrotracción, puede especificar cosas como el número y la duración de los reintentos
antes de volver a una versión de prioridad inferior del servicio especificado. Para ver la sintaxis específica, consulte [este ejemplo de política de despliegue](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json).

## Visualización de los nodos periféricos
{: #viewing_edge_nodes}

Después de desplegar una nueva versión del servicio en los nodos, es importante poder supervisar fácilmente el estado de los nodos periféricos. Utilice la {{site.data.keyword.gui}} de {{site.data.keyword.ieam}} para esta tarea. Por ejemplo, cuando se encuentra en el proceso [Despliegue de prueba](#testing_deployment) o [Despliegue de producción](#production_deployment), puede buscar rápidamente nodos que utilicen la política de despliegue o nodos con errores.

## Migración de servicios
{: #migrating_services}

En algún momento, puede que necesite mover servicios, patrones o políticas de una instancia de {{site.data.keyword.ieam}} a otra. De forma similar, es posible que tenga que mover servicios de una organización de intercambio a otra. Esto puede suceder si ha instalado una nueva instancia de {{site.data.keyword.ieam}} en un entorno de host distinto. De forma alternativa, es posible que tenga que mover servicios si tiene dos instancias {{site.data.keyword.ieam}}, una dedicada al desarrollo y otra para producción. Para facilitar este proceso, puede utilizar el [script `loadResources`](https://github.com/open-horizon/examples/blob/master/tools/loadResources) en el repositorio de ejemplos de open-horizon.

## Pruebas de solicitud de extracción automatizada con Travis
{: #testing_with_travis}

Puede automatizar las pruebas siempre que se abra una solicitud de extracción (PR) en el repositorio de GitHub utilizando [Travis CI](https://travis-ci.com). 

Continúe leyendo este contenido para saber cómo optimizar Travis y las técnicas en el repositorio de GitHub de ejemplos de open-horizon.

En el repositorio de ejemplos, Travis CI se utiliza para crear, probar y publicar ejemplos. En el [archivo `.travis.yml`](https://github.com/open-horizon/examples/blob/master/.travis.yml), se configura un entorno virtual para que se ejecute como una máquina Linux amd64 sin hzn, Docker y [qemu](https://github.com/multiarch/qemu-user-static) para construir en varias arquitecturas.

En este escenario, también se instala kafkacat para permitir que cpu2evtstreams envíe datos a IBM Event Streams. De forma similar a la utilización de la línea de mandatos, Travis puede utilizar variables de entorno como `EVTSTREAMS_TOPIC` y `HZN_DEVICE_ID` para utilizarlas con los servicios periféricos de ejemplo. HZN_EXCHANGE_URL se establece para que apunte al intercambio por etapas para publicar los servicios modificados.

A continuación, el script [travis-find](https://github.com/open-horizon/examples/blob/master/tools/travis-find) se utiliza para identificar servicios que la solicitud de extracción abierta ha modificado.

Si se ha modificado un ejemplo, se ejecuta el destino `test-all-arches` en el **makefile** de ese servicio. Con los contenedores qemu de las arquitecturas soportadas en ejecución, las construcciones de arquitectura cruzada se ejecutan con este destino **makefile** estableciendo la variable de entorno `ARCH` inmediatamente antes de la construcción y la prueba. 

El mandato `hzn dev service start` ejecuta el servicio periférico y el archivo [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) supervisa los registros de servicio para determinar si el servicio funciona correctamente.

Consulte [helloworld Makefile](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24) para ver el destino de archivo make `test-all-arches` dedicado.

El siguiente escenario muestra una prueba global más completa. Si uno de los ejemplos modificados incluye `cpu2evtstreams`, se puede supervisar una instancia de IBM Event Streams en segundo plano y se puede comprobar para HZN_DEVICE_ID. Puede pasar la prueba y añadirse a una lista de todos los servicios que pasan, solo si encuentra el ID de nodo **travis-test** en los datos leídos del tema cpu2evtstreams. Esto requiere una clave de API de IBM Event Streams y un URL de intermediario que estén establecidos como variables de entorno secretas.

Una vez que se ha fusionado la PR, se repite este proceso y se utiliza la lista de servicios que pasan para identificar qué servicios se pueden publicar en el intercambio. Las variables de entorno secretas de Travis que se utilizan en este ejemplo incluyen todo lo que se necesita para enviar, firmar y publicar servicios en el intercambio. Esto incluye las credenciales de Docker, HZN_EXCHANGE_USER_AUTH y un par de claves de firma criptográfica que se pueden obtener con el mandato `hzn key create`. A fin de guardar las claves de firma como variables de entorno seguras, éstas deben estar codificadas en base64.

Se utiliza la lista de servicios que han pasado la prueba funcional para identificar qué servicios se deben publicar con el destino `Makefile` de publicación dedicado. Consulte [helloworld sample](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45).

Dado que los servicios se han construido y probado, este destino publica el servicio, la política de servicio, el patrón y la política de despliegue en todas las arquitecturas para el intercambio.

**Nota**:  También puede realizar muchas de estas tareas desde la consola de gestión. Consulte
[Utilización de la consola de gestión](../console/accessing_ui.md).

