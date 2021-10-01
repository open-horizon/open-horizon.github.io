---

copyright:
years: 2019
lastupdated: "2019-07-05"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Detalles de desarrollo
{: #developing}

El contenido siguiente proporciona más detalles sobre las prácticas de desarrollo de software y los conceptos
para el desarrollo de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).{:shortdesc}

## Introducción
{: #developing_intro}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) se basa en el software de código abierto [Open Horizon - EdgeX Project Group ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). 

Con {{site.data.keyword.ieam}} puede desarrollar cualquier contenedor de servicios que desee para las máquinas periféricas. A continuación, puede firmar y publicar criptográficamente el código. Por
último, puede especificar políticas en un {{site.data.keyword.edge_deploy_pattern}} para controlar
la instalación, supervisión y actualización de software. Después de completar estas tareas, puede ver los {{site.data.keyword.horizon_agents}} y los {{site.data.keyword.horizon_agbots}} que establecen acuerdos de formación para colaborar en la gestión del ciclo de vida de software. A continuación, estos componentes gestionan los detalles del ciclo de vida del software en los {{site.data.keyword.edge_nodes}} de forma totalmente autónoma según el patrón de despliegue registrado para cada nodo periférico. {{site.data.keyword.ieam}}
también puede utilizar políticas para determinar dónde y cuándo desplegar de forma autónoma
servicios y modelos de aprendizaje automático. Las políticas son una alternativa a los patrones de despliegue.

El proceso de desarrollo de software de {{site.data.keyword.ieam}} se centra en el mantenimiento
de la seguridad e integridad del sistema, al tiempo que simplifica enormemente el esfuerzo necesario para
la gestión de software activa en los nodos periféricos. {{site.data.keyword.ieam}}
también puede utilizar políticas para determinar dónde y cuándo desplegar de forma autónoma
servicios y modelos de aprendizaje automático. Las políticas son una alternativa a los patrones de despliegue. Puede crear procedimientos de publicación de {{site.data.keyword.ieam}} en el conducto de integración y despliegue continuos. Cuando
los agentes autónomos distribuidos descubren cambios publicados en el software o en una política, como en la
política de {{site.data.keyword.edge_deploy_pattern}} o de despliegue, los agentes autónomos actúan
de forma independiente para actualizar el software o aplicar sus políticas en toda la flota de
máquinas perimetrales, dondequiera que se encuentren.

## Patrones de servicios y despliegue
{: #services_deploy_patterns}

{{site.data.keyword.edge_services}} son los bloques de creación de los patrones de despliegue. Cada servicio puede contener uno o más contenedores de Docker. A su vez, cada contenedor de Docker puede contener uno o varios procesos de larga ejecución. Estos procesos pueden estar escritos en casi cualquier lenguaje de programación y utilizar cualquier biblioteca o programa de utilidad. Sin embargo los procesos deben estar desarrollados para un contenedor de Docker y se deben en el contexto de éste. Esta flexibilidad significa que casi no hay restricciones sobre el código que {{site.data.keyword.ieam}} puede gestionar para usted. Cuando se ejecuta un contenedor, el contenedor queda restringido a un recinto de seguridad protegido. Este recinto de seguridad restringe el acceso a dispositivos de hardware, a algunos servicios de sistema operativo, al sistema de archivos de host y a las redes de máquinas periféricas de host. Para obtener información sobre las restricciones de recinto de seguridad, consulte [Recinto de seguridad](#sandbox).

El código de ejemplo `cpu2evtstreams` consta de un contenedor de Docker que utiliza otros dos servicios periféricos locales. Estos servicios periféricos locales se conectan a través de las redes virtuales de Docker privadas locales mediante las API REST HTTP. Estos servicios se denominan `cpu` y `gps`. El agente despliega cada servicio en una red privada independiente junto con cada servicio que ha declarado una dependencia del servicio. Se crea una red para `cpu2evtstreams` y `cpu` y se crea otra red para `cpu2evtstreams` y `gps`. Si hay un cuarto servicio en este patrón de despliegue que también está compartiendo el servicio `cpu`, se crea otra red privada solo para el `cpu` y el cuarto servicio. En {{site.data.keyword.ieam}} esta estrategia de red restringe el acceso para los servicios solo a los otros servicios que se listan en `requiredServices` cuando se publicaron los otros servicios. En el diagrama siguiente se muestra el patrón de despliegue `cpu2evtstreams` cuando el patrón se ejecuta en un nodo periférico:

<img src="../../images/edge/07_What_is_an_edge_node.svg" width="70%" alt="Servicios en un patrón">

Nota: La configuración de IBM Event Streams sólo es necesaria para algunos ejemplos.

Las dos redes virtuales permiten al contenedor de servicio `cpu2evtstreams` acceder a las API REST proporcionadas por los contenedores de servicio `cpu` y `gps`. Estos dos contenedores gestionan el acceso a los servicios del sistema operativo y a los dispositivos de hardware. Aunque se utilizan las API REST, existen muchas otras formas posibles de comunicación que puede utilizar para permitir que los servicios compartan datos y control.

A menudo, el patrón de codificación más eficaz para los nodos periféricos implica desplegar varios servicios pequeños que se pueden configurar y desplegar independientemente. Por ejemplo, los patrones de Internet de las cosas tienen a menudo servicios de nivel bajo que necesitan acceder al hardware del nodo periférico, como por ejemplo sensores o mecanismos de acceso. Estos servicios proporcionan acceso compartido a este hardware para que los utilicen otros servicios.

Este patrón es útil cuando el hardware requiere un acceso exclusivo para proporcionar una función útil. El servicio de nivel bajo puede gestionar correctamente este acceso. El rol de los contenedores de servicio `cpu` y `gps` es similar en principio al del software de controlador de dispositivos del sistema operativo del host, pero a un nivel superior. La segmentación del código en servicios pequeños independientes, algunos especializados en el acceso a hardware de nivel bajo, permite separar claramente las preocupaciones. Cada componente puede evolucionar y ser actualizado independientemente en el campo. Las aplicaciones de terceros también se pueden desplegar de forma segura junto con la pila de software incorporada tradicional propietaria, permitiendo de forma selectiva el acceso a hardware determinado u otros servicios.

Por ejemplo, un patrón de despliegue de controlador industrial puede estar compuesto por un servicio de nivel bajo para supervisar los sensores de uso de energía y otros servicios de bajo nivel. Estos otros servicios de nivel bajo se pueden utilizar para permitir el control de los métodos de acceso para alimentar los dispositivos que se supervisan. El patrón de despliegue puede tener también otro contenedor de servicio de nivel superior que consume los servicios del sensor y el método de acceso. Este servicio de nivel superior puede utilizar los servicios para alertar a los operadores o para apagar automáticamente los dispositivos cuando se detecten lecturas de consumo de energía anómalas. Este patrón de despliegue también puede incluir un servicio de historial que registra y archiva los datos del sensor y el método de acceso y posiblemente el análisis completo de los datos. Otro componente útil de un patrón de despliegue de este tipo pueden ser un servicio de ubicación GPS.

Cada contenedor de servicio individual se puede actualizar de forma independiente con este diseño. Cada servicio individual también se puede volver a configurar y componer en otros patrones de despliegue útiles sin ningún cambio de código. Si es necesario, se puede añadir al patrón un servicio de análisis de terceros. A este servicio de terceros se le puede dar acceso sólo a un conjunto concreto de API de sólo lectura, que impide el servicio interactuar con los métodos de acceso en la plataforma.

De forma alternativa, todas las tareas de este ejemplo de controlador industrial se pueden ejecutar dentro de un único contenedor de servicio. Esta alternativa no es normalmente el mejor enfoque, ya que una colección de servicios independientes e interconectados de menor tamaño hace que las actualizaciones de software sean más rápidas y más flexibles. Las colecciones de servicios más pequeños también pueden ser más robustas en el campo. Para obtener más información sobre cómo diseñar los patrones de despliegue, consulte [Prácticas de desarrollo nativos de Edge](best_practices.md).

## Recinto de seguridad
{: #sandbox}

El recinto de seguridad en el que se ejecutan los patrones de despliegue restringe el acceso a las API que proporcionan los contenedores de servicio. Únicamente se permite el acceso a los otros servicios que declaran explícitamente dependencias de sus servicios. Otros procesos del host no acceden normalmente a estos servicios. De forma similar, otros hosts remotos no tienen acceso normalmente a ninguno de estos servicios a menos que el servicio publique explícitamente un puerto en la interfaz de red externa del host.

## Servicios que utilizan otros servicios
{: #using_services}

Los servicios periféricos suelen utilizar varias interfaces de API que proporcionan otros servicios periféricos para adquirir datos de ellos o para proporcionarles mandatos de control. Estas interfaces de API son normalmente API REST de HTTP, como las proporcionadas por los servicios `cpu` y `gps` de nivel bajo en el ejemplo `cpu2evtstreams`. Sin embargo, esas interfaces realmente pueden ser cualquier cosa que desee, como por ejemplo memoria compartida, TCP o UDP y puede estar cifradas o no. Dado que estas comunicaciones normalmente se llevan a cabo dentro de un único periférico, sin que los mensajes salgan nunca de este host, a menudo el cifrado es innecesario.

Como alternativa a las API REST puede utilizar una interfaz de publicación y suscripción como por ejemplo, la interfaz que proporciona MQTT. Cuando un servicio sólo proporciona datos de forma intermitente, una interfaz de publicación y suscripción suele ser más algo más sencillo que sondear repetidamente una API REST, ya que las API REST pueden agotar el tiempo de espera. Por ejemplo, considere un servicio que supervisa un botón de hardware y proporciona una API para otros servicios para detectar si se ha pulsado el botón. Si se utiliza una API REST, el emisor de la llamada no puede llamar a la API REST y esperar una respuesta que se produciría cuando se pulsara el botón. Si pasara mucho tiempo sin que se pulsara el botón, la API REST agotaría el tiempo de espera. En lugar de ello, el proveedor de API tendría que responder con prontitud para evitar un error. El emisor de la llamada debe llamar repetidamente y con frecuencia a la API para asegurarse de que no se pierde una breve pulsación del botón. Una mejor solución es que el emisor de la llamada se suscriba a un tema adecuado en un servicio de publicación y suscripción y bloquee. Entonces, el emisor de la llamada puede esperar a que se publique algo, lo que puede ocurrir en un futuro lejano. El proveedor de API
puede cuidarse de supervisar el hardware del botón y a continuación, publicar sólo los cambios de estado en ese tema, como por ejemplo `button pressed`, o `button released`.

MQTT es una de las herramientas de publicación y suscripción más populares que se pueden utilizar. Puede desplegar un intermediario MQTT como un servicio periférico y hacer que los servicios de publicador y suscriptor lo requieran. MQTT también se utiliza con frecuencia como un servicio de nube. IBM Watson IoT Platform por ejemplo, utiliza MQTT para comunicarse con dispositivos IoT. Para obtener más información, consulte [IBM Watson IoT Platform ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/watson-iot-platform). Algunos de los ejemplos de proyecto de {{site.data.keyword.horizon_open}} utilizan MQTT. Para obtener más información, consulte [Ejemplos de {{site.data.keyword.horizon_open}}](https://github.com/open-horizon/examples).

Otra herramienta de publicación y suscripción popular es Apache Kafka, que también se utiliza frecuentemente como un servicio de nube. {{site.data.keyword.message_hub_notm}}, que el ejemplo `cpu2evtstreams` utiliza para enviar datos a {{site.data.keyword.cloud_notm}}, también está basado en Kafka. Para obtener más información, consulte [{{site.data.keyword.message_hub_notm}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/event-streams).

Cualquier contenedor de servicios periféricos puede proporcionar o consumir otros servicios periféricos locales en el mismo host y servicios periféricos proporcionados en los hosts cercanos en la LAN local. Los contenedores pueden comunicarse con sistemas centralizados en un centro de datos corporativo o de proveedor de nube remoto. Como creador de servicios, puede determinar con quién y cómo se comunican sus servicios.

Le será útil volver a consultar el ejemplo `cpu2evtstreams` para ver cómo el código de ejemplo utiliza los otros dos servicios locales. Por ejemplo, cómo el código de ejemplo especifica dependencias sobre los dos servicios locales, declara y utiliza variables de configuración y se comunica con Kafka. Para obtener más información, consulte [Ejemplo de `cpu2evtstreams`](cpu_msg_example.md).

## Definición de servicios
{: #service_definition}

Nota: Consulte [Convenciones utilizadas en este documento](../../getting_started/document_conventions.md)
para obtener más información sobre la sintaxis de mandato.

En cada proyecto de {{site.data.keyword.ieam}} tiene un archivo `horizon/service.definition.json`. Este archivo define el servicio periférico por dos razones. Una de estas razones es permitirle simular la ejecución del servicio mediante la herramienta `hzn dev`, similar a cómo se ejecuta en {{site.data.keyword.horizon_agent}}. Esta simulación es útil para elaborar cualesquiera instrucciones de despliegue especiales que necesite, como por ejemplo enlaces de puerto y acceso de dispositivos de hardware. La simulación también es útil para verificar las comunicaciones entre contenedores de servicios en las redes privadas virtuales de Docker que el agente crea para usted. La otra razón de ser de este archivo es permitirle publicar el servicio en {{site.data.keyword.horizon_exchange}}. En los ejemplos proporcionados, el archivo `horizon/service.definition.json` se le proporciona dentro del repositorio GitHub de ejemplo o se genera mediante el mandato `hzn dev service new`.

Abra el archivo `horizon/service.definition.json` que contiene los metadatos {{site.data.keyword.horizon}} para una de las implementaciones de servicio de ejemplo, por ejemplo, [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Cada servicio que se publica en {{site.data.keyword.horizon}} necesita tener un `url` que lo identifique de forma exclusiva dentro de su organización. Este campo no es un URL. En lugar de esto, el campo `url` forma un identificador exclusivo global, cuando se combina con el nombre de la organización, y unos campos `version` y `arch` de la implementación específicos. Puede editar el archivo `Horizon/service.definition.json` para proporcionar los valores adecuados para `url` y `version`. Para el valor de `version`, utilice un valor de estilo de mantenimiento de versiones semánticas. Utilice los nuevos valores cuando envíe, firme y publique los contenedores de servicio. También puede editar el archivo `horizon/hzn.json` y las herramientas sustituyen los valores de variable que se encuentran allí, en lugar de cualesquiera referencias de variable utilizadas en el archivo `horizon/service.definition.json`.

La sección `requiredServices` del archivo `horizon/service.definition.json` detalla cualesquiera dependencias de servicio, como por ejemplo los demás servicios periféricos que este contenedor utiliza. La herramienta `hzn dev dependency fetch` le permite agregar dependencias a esta lista, por lo que no es necesario editar manualmente la lista. Después de añadir dependencias, cuando el agente ejecuta el contenedor, los demás `requiredServices` también se ejecutan automáticamente (por ejemplo, cuando se utiliza `hzn dev service start` o cuando se registra un nodo con un patrón de despliegue que contiene este servicio). Para obtener más información sobre los servicios necesarios, consulte [cpu2evtstreams](cpu_msg_example.md).

En la sección `userInput` se declaran las variables de configuración que el servicio puede consumir para configurarse a sí mismo para un despliegue concreto. Aquí se proporcionan nombres de variable, tipos de datos y valores predeterminados y también se puede proporcionar una descripción legible para cada uno de ellos. Cuando se utiliza `hzn dev service start` o cuando se registra un nodo periférico con un patrón de despliegue que contiene este servicio, debe proporcionar un archivo `userinput.json` para definir valores para las variables que no tienen valores predeterminados. Para obtener más información acerca de las variables de configuración `userInput` y los archivos `userinput.json`, consulte [cpu2evtstreams](cpu_msg_example.md).

El archivo `horizon/service.definition.json` también contiene una sección `deployment`, hacia el final del archivo. Los campos de esta sección nombran cada imagen de contenedor de Docker que implementa el servicio lógico. El nombre de cada registro que se utiliza aquí en la matriz de `services` es el nombre que utilizan otros contenedores para identificar el contenedor en la red privada virtual compartida. Si este contenedor proporciona una API REST para que la consuman otros contenedores, puede acceder a esta API REST dentro del contenedor de consumo utilizando `curl http://<name>/<your-rest-api-uri>`. El campo `image` para cada nombre proporciona una referencia a la imagen de contenedor Docker correspondiente como, por ejemplo, en DockerHub o algún registro de contenedor privado. Otros campos de la sección `deployment` se pueden utilizar para cambiar la manera en la que el agente indica a Docker que ejecute el contenedor. Para
obtener más información, consulte [{{site.data.keyword.horizon}} Deployment Strings ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/anax/blob/master/doc/deployment_string.md).

## Interacción con {{site.data.keyword.horizon_exchange}}
{: #horizon_exchange}

Cuando crea y publica los programas de ejemplo, interactúa con
{{site.data.keyword.horizon_exchange}} para publicar los servicios, las políticas y
los patrones de despliegue. También puede utilizar {{site.data.keyword.horizon_exchange}} para registrar los nodos periféricos para ejecutar un patrón de despliegue concreto. {{site.data.keyword.horizon_exchange}} actúa como un repositorio para la información compartida, que le permite comunicarse indirectamente con otros componentes de {{site.data.keyword.ieam}}. Como desarrollador, tiene que entender cómo trabajar con {{site.data.keyword.horizon_exchange}}.

Este diagrama muestra los agentes que se deben ejecutar dentro de cada nodo periférico, y los agbots que se deben configurar para cada patrón de despliegue, normalmente, en la nube o en un centro de datos corporativo centralizado.

Los desarrolladores de {{site.data.keyword.ieam}} utilizan generalmente el mandato `hzn` para interactuar con {{site.data.keyword.horizon_exchange}}. Específicamente, el mandato `hzn exchange` se utiliza para todas las interacciones con {{site.data.keyword.horizon_exchange}}. Puede escribir `hzn exchange -- help` para ver todos los submandatos que pueden seguir a `hzn exchange` en la línea de mandatos. A continuación, puede utilizar `hzn exchange <submandato> --help` para obtener más detalles sobre el `<submandato>` de su elección.

Los mandatos siguientes son útiles para interrogar al {{site.data.keyword.horizon_exchange}}:

* Comprobar que las credenciales de usuario funcionan en {{site.data.keyword.horizon_exchange}}: `hzn exchange user list`
* Comprobar la versión de software de {{site.data.keyword.horizon_exchange}}: `hzn exchange version`
* Comprobar el estado actual de {{site.data.keyword.horizon_exchange}}: `hzn exchange status`
* Listar todos los nodos periféricos que se crean bajo la organización: `hzn exchange node list`
* Recuperar los detalles de un nodo periférico específico: `hzn exchange node list <node-id>`
  Sustituya `<node-id>` por el valor del ID del nodo periférico.
* Listar todos los servicios publicados bajo la organización: `hzn exchange service list`
* Listar todos los servicios públicos publicados bajo cualquier organización: `hzn exchange service list '<org>/*'`
* Recuperar los detalles de un servicio publicado en particular: `hzn exchange service list <org/service>`
* Listar todos los patrones de despliegue publicados bajo la organización: `hzn exchange pattern list`
* Listar todos los patrones de despliegue públicos publicados bajo cualquier organización: `hzn exchange pattern list '<org>/*'`
* Listar todos los detalles para un servicio publicado particular: `hzn exchange pattern list <org/pattern>`

## Agentes y agbots
{: #agents_agbots}

Es importante entender los roles de los agentes y los agbots y la forma exacta en que se comunican. Este conocimiento puede ser útil para diagnosticar y arreglar problemas cuando algo sale mal.

Los agentes y los agbots nunca se comunican directamente entre sí. El agente para cada nodo periférico debe
establecer un buzón para sí mismo en el {{site.data.keyword.horizon_switch}} y crear un recurso de nodo en
{{site.data.keyword.horizon_exchange}}. A continuación, cuando desea ejecutar un patrón de despliegue determinado, se registra a sí mismo para este patrón en {{site.data.keyword.horizon_exchange}}.

Los agbots supervisan los patrones y buscan continuamente en {{site.data.keyword.horizon_exchange}} para encontrar nodos periféricos que se registran para el patrón. Cuando un nodo periférico nuevo se registra para utilizar un patrón, un agbot contacta con el agente local en dicho nodo periférico correspondiente. El agbot contacta a través del {{site.data.keyword.horizon_switch}}. Ahora,
todo el agbot puede saber sobre el agente es su clave pública. El agbot no conoce la dirección IP del nodo periférico ni cualquier otra cosa sobre él que no sea el hecho de que está registrado para el patrón de despliegue específico. El agbot se comunica con el agente, a través de {{site.data.keyword.horizon_switch}}, para proponer que colaboren para gestionar el ciclo de vida del software de este patrón de despliegue en este nodo periférico.

El agente para cada nodo periférico supervisa el {{site.data.keyword.horizon_switch}} para ver si hay algún mensaje en el buzón. Cuando el agente recibe una propuesta de un agbot, evalúa esta propuesta basándose en las políticas que ha establecido el propietario del nodo periférico cuando se configuró el nodo periférico y elige si va a aceptar la propuesta o rechazarla.

Cuando se acepta una propuesta de patrón de despliegue, el agente procede a extraer los contenedores de servicio apropiados del registro de Docker adecuado, verificar las firmas de servicio, configurar el servicio y ejecutar el servicio.

Todas las comunicaciones entre los agentes y los agbots que pasan por el {{site.data.keyword.horizon_switch}} están cifradas por los dos participantes. A pesar de que estos mensajes se almacenan en el {{site.data.keyword.horizon_switch}}central, el {{site.data.keyword.horizon_switch}} no es capaz de descifrar y escuchar secretamente esas conversaciones.

## Despliegue de actualizaciones de software de servicio
{: #deploy_edge_updates}

Después de desplegar el software en su flota de nodos periféricos querrá actualizar el código. Las actualizaciones de software se pueden llevar a cabo con {{site.data.keyword.ieam}}. Normalmente, no es necesario que haga nada en los nodos periféricos para actualizar el software que se ejecuta en los nodos periféricos. En cuanto firma y publica una actualización, los agbots y los agentes que se ejecutan en cada nodo de borde se coordinan para desplegar la versión más reciente del patrón de despliegue en cada nodo periférico que está registrado para el patrón de despliegue actualizado. Una de las ventajas clave de {{site.data.keyword.ieam}} es la sencillez con la que facilita un conducto de actualización de software hasta llegar a los nodos periféricos.

Para publicar una nueva versión de software, siga estos pasos: 

* Edite el código de servicio tal como desee para esta actualización.
* Edite el número de versión semántico del código.
* Vuelva a crear los contenedores de servicio.
* Envíe los contenedores de servicio actualizados al registro de Docker adecuado.
* Firme y vuelva a publicar los servicios actualizados en {{site.data.keyword.horizon_exchange}}.
* Vuelva a publicar el patrón de despliegue en {{site.data.keyword.horizon_exchange}}. Utilice el mismo nombre y haga referencia a los nuevos números de versión de servicio.

Los agbots de {{site.data.keyword.horizon}} detectan rápidamente los cambios de patrón de despliegue. Los agbots contactan con cada agente cuyo nodo periférico está registrado para ejecutar el patrón de despliegue. El agbot y el agente se coordinan para descargar los contenedores nuevos, detener y eliminar los contenedores antiguos e iniciar los contenedores nuevos.

Este proceso hace que cada uno de los nodos periféricos que están registrados ejecute rápidamente el patrón de despliegue actualizado para ejecutar la versión de contenedor de servicio nueva, independientemente de dónde esté ubicado geográficamente el nodo periférico.

## Qué hacer a continuación
{: #developing_what_next}

Para obtener más información acerca del desarrollo del código de nodo periférico, consulte la documentación siguiente:

[Prácticas de desarrollo nativas de Edge](best_practices.md)

Revise los principios importantes y los procedimientos recomendados para desarrollar servicios periféricos para el desarrollo de software de {{site.data.keyword.ieam}}.

[Utilización de {{site.data.keyword.cloud_registry}}](container_registry.md)

Con {{site.data.keyword.ieam}}, puede colocar contenedores de servicio en el registro de contenedor seguro privado de IBM en lugar de en el Docker Hub público. Por ejemplo, si tiene una imagen de software que incluye activos que no son apropiados para incluir en un registro público, puede utilizar un registro de contenedor de Docker privado, como el {{site.data.keyword.cloud_registry}} en el que el acceso está estrechamente controlado.

[Las API](../installing/edge_rest_apis.md)

{{site.data.keyword.ieam}} proporciona API RESTful para que los componentes puedan colaborar y para permitir que los desarrolladores y los usuarios de la organización controlen los componentes.
