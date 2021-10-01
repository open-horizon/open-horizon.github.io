---

copyright:
  years: 2020
lastupdated: "2020-04-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Casos de uso de política de despliegue
{: #developing_edge_services}

En esta sección se pone de relieve un escenario real en el que se describen los tipos de política.

<img src="../OH/docs/images/edge/04_Defining_an_edge_policy.svg" style="margin: 3%" alt="Defining an edge policy">

Considere un cliente que ha instalado cámaras de cajero automático para detectar robos (el cliente también tiene otros tipos de nodos periféricos). El cliente utiliza una combinación de cajeros automáticos de acceso peatonal (still) y motorizado (motion). En este caso, hay dos servicios de terceros disponibles. Cada servicio puede detectar actividad sospechosa en los cajeros automáticos, pero las pruebas de cliente han determinado que el servicio atm1 detecta de forma más fiable la actividad sospechosa en los cajeros automáticos de acceso peatonal (still) y el servicio atm2 detecta de forma más fiable la actividad sospechosa en los cajeros automáticos de acceso motorizado (motion).

Esta es la forma en que se expresa la política para conseguir el despliegue de modelo y de servicio deseado:

* Establecer propiedades en la política de nodo en todos los cajeros automáticos de acceso peatonal (walk-up): propiedades: `camera-type: still`, `atm-type: walk-up`
* Establecer propiedades en la política de nodo en todos los cajeros automáticos de acceso motorizado (drive-thru): propiedades: `camera-type: motion`, `atm-type: drive-thru`
* Opcionalmente, establecer restricciones en la política de servicios establecida por los desarrolladores de terceros de atm1 y atm2: restricciones: `(Optional)`
* Establecer restricciones en la política de despliegue establecida por el cliente para el servicio atm1: restricciones: `camera-type == still`
* Establecer restricciones en la política de despliegue establecida por el cliente para el servicio atm2: restricciones: `camera-type == motion`

Nota: el mandato `hzn` utiliza a veces el término política de negocio al hacer referencia a la política de despliegue.

La política de nodo (establecida por el técnico que configura los cajeros) indica los hechos acerca de cada nodo; por ejemplo, si el cajero tiene una cámara y el tipo de ubicación en la que se encuentra el cajero. Para el técnico resulta fácil determinar y especificar esta información.

La política de servicio es una declaración sobre lo que el servicio necesita para funcionar correctamente (en este caso, una cámara). El desarrollador de servicios de terceros conoce esta información, a pesar de que no sabe qué cliente la está utilizando. Si el cliente tiene otros cajeros que no tienen cámaras, estos servicios no se despliegan en esos cajeros debido a esta restricción.

La política de despliegue está definida por el director de tecnologías de la información del cliente (o quien sea que gestione el entramado periférico). Esto define el despliegue de servicio global para el negocio. En este caso, el director de tecnologías de la información expresa el resultado deseado del despliegue de servicio, que atm1 se debe utilizar para los cajeros de acceso peatonal y atm2 se debe utilizar para los cajeros de acceso motorizado.

## Política de nodo
{: #node_policy}

La política se puede conectar a un nodo. El propietario del nodo puede proporcionar esto en el momento del registro y se puede cambiar en cualquier momento directamente en el nodo o de forma centralizada por parte de un administrador de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Cuando la política de nodo se cambia de forma centralizada, se refleja en el nodo la próxima vez que el centro de gestión registra un latido de aquel. Cuando la política de nodo se cambia directamente en el nodo, los cambios se reflejan inmediatamente en el centro de gestión para que el despliegue de modelo y servicio se pueda volver a evaluar inmediatamente. De forma predeterminada, un nodo tiene algunas [propiedades incorporadas](#node_builtins) que reflejan la memoria, la arquitectura y el número de las CPU. También puede contener propiedades arbitrarias; por ejemplo el modelo de producto, dispositivos conectados, configuración de software o cualquier otra cosa que el propietario del nodo considere relevante. Las restricciones de política de nodo se pueden utilizar para restringir qué servicios se permite ejecutar en este nodo.Cada nodo sólo tiene una política que contiene todas las propiedades y restricciones asignadas a ese nodo.

## Política de servicio
{: #service_policy}

Nota: la política de servicio es una función opcional.

Al igual que los nodos, los servicios pueden expresar la política y tener también algunas [propiedades incorporadas](#service_builtins). Esta política se aplica a un servicio publicado en Exchange y la crea el desarrollador de servicios. Las propiedades de política de servicio pueden indicar las características del código de servicio que los autores de políticas de nodo pueden encontrar relevantes. Las restricciones de política de servicio se pueden utilizar para restringir dónde y en qué tipo de dispositivos se puede ejecutar este servicio. Por ejemplo, el desarrollador de servicios puede afirmar que este servicio requiere una configuración de hardware en particular, como por ejemplo restricciones de CPU/GPU, restricciones de memoria, sensores específicos, mecanismos de acceso u otros dispositivos periféricos. Por lo general, las propiedades y las restricciones permanecen estáticas durante la vida del servicio porque describen aspectos de la implementación del servicio. En los casos de uso de ejemplo esperados, un cambio en uno de estos casos suele coincidir con cambios de código que necesitan una versión de servicio nueva. Las políticas de despliegue se utilizan para capturar los aspectos más dinámicos del despliegue de servicio que surgen de los requisitos del negocio.

## Política de despliegue
{: #deployment_policy}

La política de despliegue controla el despliegue del servicio. Al igual que los otros tipos de políticas, contiene un conjunto de propiedades y restricciones, pero también contiene otras cosas. Por ejemplo, identifica explícitamente un servicio que se va a desplegar y también puede contener valores de variables de configuración, versiones de retrotracción de servicio e información de configuración de estado de nodo. El enfoque de política de despliegue para los valores de configuración es potente porque esta operación se puede realizar de forma centralizada, sin necesidad de conectarse directamente al nodo periférico.

Los administradores pueden crear una política de despliegue y {{site.data.keyword.ieam}} utiliza esa política para ubicar todos los dispositivos que coinciden con las restricciones definidas y despliega el servicio especificado en esos dispositivos mediante las variables de servicio configuradas en la política. Las versiones de retrotracción de servicio indican a {{site.data.keyword.ieam}} qué versiones de servicio se deben desplegar si no se despliega una versión más alta del servicio. La configuración de estado del nodo indica cómo {{site.data.keyword.ieam}} debe medir el estado (pulsaciones y la comunicación con el centro de gestión) de un nodo antes de determinar si el nodo está fuera de la política.

Debido a que las políticas de despliegue capturan las restricciones y las propiedades de servicio de tipo de negocio que son más dinámicas, se espera que cambien más a menudo que la política de servicio. Su ciclo de vida es independiente del servicio al que hacen referencia, lo que otorga al administrador de políticas la posibilidad de declarar una versión de servicio específica o un rango de versiones. {{site.data.keyword.ieam}} fusiona entonces la política de servicio y la política de despliegue y a continuación, intenta encontrar nodos cuya política sea compatible con eso.

## Política de modelo
{: #model_policy}

Los servicios basados en el aprendizaje automático (ML) requieren que los tipos de modelo específicos funcionen correctamente y los clientes de {{site.data.keyword.ieam}} deben poder colocar modelos específicos en los mismos nodos, o en un subconjunto de ellos, en los que se han colocado dichos servicios. La finalidad de la política de modelo es reducir aún más el conjunto de nodos en los que se despliega un servicio determinado, lo que permite que un subconjunto de esos nodos reciba un objeto de modelo específico a través de [Hello world utilizando la gestión de modelos](../developing/model_management_system.md).

## Caso de uso de política ampliado
{: #extended_policy_use_case}

En el ejemplo de los cajeros, el cliente trabaja con cajeros de acceso peatonal en ubicaciones rurales que se utilizan con poca frecuencia. El cliente no desea que los cajeros rurales estén continuamente en funcionamiento y no desea activar el cajero cada vez que perciba un objeto cercano. Por lo tanto, el desarrollador de servicios añade un modelo ML al servicio atm1 que activa el cajero automático si éste identifica a una persona que se acerca. Con el fin de desplegar específicamente el modelo de aprendizaje automático en los cajeros rurales, configuran la política:

* Política de nodo en los cajeros automáticos rurales de acceso peatonal: propiedades: `camera-type: still`, `atm-type: walk-up`, `location: rural`
* Opcionalmente, las restricciones de política de servicio establecidas por los desarrolladores de terceros para atm1 siguen siendo las mismas: restricciones: `(Optional)`
* La política de despliegue establecida por el cliente para el servicio atm1 sigue siendo la misma: restricciones: `camera-type == still
* Los desarrolladores de terceros establecen en el objeto MMS las restricciones de política de modelo para el servicio atm1:

```
"destinationPolicy": {
  "constraints": [ "location == rural"  ],   "services": [        { "orgID": "$HZN_ORG_ID",          "serviceName": "atm1",          "arch": "$ARCH",            "version": "$VERSION"        }
  ]
}
```
{: codeblock}

Dentro del objeto MMS, la política de modelo declara un servicio (o lista de servicios) que puede acceder al objeto (en este caso, atm1) y declara las propiedades y las restricciones que permiten a {{site.data.keyword.ieam}} restringir aún más la ubicación adecuada del objeto en los cajeros automáticos en las ubicaciones rurales. Otros servicios que se ejecutan en el cajero no podrán acceder el objeto.

## Propiedades
{: #properties}

Las propiedades son esencialmente sentencias de hechos que se expresan como pares de nombre=valor. Las propiedades también se escriben, lo que proporciona una forma de construir expresiones potentes. En las tablas siguientes se muestran los tipos de valor de propiedad soportados por {{site.data.keyword.ieam}} y las propiedades de política de servicio y nodo incorporadas. Los propietarios de nodos, los desarrolladores de servicios y los administradores de políticas de despliegue pueden definir propiedades individuales para satisfacer sus necesidades. No es necesario definir las propiedades en un repositorio central, las propiedades se establecen y se hace referencia a ellas (en expresiones de restricción) según se necesita.

|Tipos de valores de propiedad aceptados|
|-----------------------------|
|versión - expresión decimal con punto que admite 1, 2 o 3 partes; por ejemplo, 1.2, 2.0.12, etc.|
|serie *|
|lista de series (series separadas por comas)|
|entero|
|booleano|
|flotante|
{: caption="Tabla 1. Tipos de valor de propiedad aceptados"}

*Los valores de serie que contienen espacios deben estar entrecomillados.

Las propiedades incorporadas proporcionan nombres bien definidos para las propiedades comunes, de modo que todas las restricciones puedan hacer referencia a ellas de la misma forma. Por ejemplo, si un servicio necesita un número `x` de CPU para poder ejecutarse de forma adecuada o eficaz, puede utilizar la propiedad `openhorizon.cpu` en su restricción. La mayoría de estas propiedades no se pueden establecer, pero en lugar de esto se leen del sistema subyacente y se ignoran los valores establecidos por un usuario.

### Propiedades incorporadas de nodo
{: #node_builtins}

|Nombre|Tipo|Descripción|Tipo de política|
|----|----|-----------|-----------|
|openhorizon.cpu|Entero|El número de CPU|Nodo|
|openhorizon.memory|Entero|La cantidad de memoria en MBs|Nodo|
|openhorizon.arch|Serie|Arquitectura de hardware de nodo (por ejemplo, amd64, armv6, etc.)|Nodo|
|openhorizon.hardwareId|Serie|El número de serie de hardware de nodo si está disponible a través de la API de linux; de lo contrario, es un número aleatorio de cifrado seguro que no cambia durante la vida del registro de nodo|Nodo|
|openhorizon.allowPrivileged|Booleano|Permitir que los contenedores utilicen la prestación privilegiada, como que se ejecuten con privilegios o que tengan la red del host conectada al contenedor.|Nodo|
{: caption="Tabla 2. Propiedades incorporadas de nodo"}

### Propiedades incorporadas de servicio
{: #service_builtins}

|Nombre|Tipo|Descripción|Tipo de política|
|----|----|-----------|-----------|
|openhorizon.service.url|Serie|El nombre exclusivo del servicio|Servicio|
|openhorizon.service.org|Serie|La organización de varios arrendatarios en la que se define el servicio*|Servicio|
|openhorizon.service.version|Versión|La versión de un servicio que utiliza la misma sintaxis de versión semántica (por ejemplo, 1.0.0)|Servicio|
{: caption="Tabla 3. Propiedades incorporadas de servicio"}

*En una restricción, si se especifica service.url, pero se omite service.org, org toma de forma predeterminada el valor de la política de nodo o de despliegue que define la restricción.

## Restricciones
{: #constraints}

En {{site.data.keyword.ieam}}, las políticas de nodo, servicio y despliegue pueden definir restricciones. Las restricciones se expresan como un predicado en un formato de texto simple y hacen referencia a las propiedades y a sus valores, o a un rango de valores posibles correspondientes. Las restricciones también pueden contener operadores booleanos tales como AND (& &), OR (||) entre expresiones de propiedad y valor para formar cláusulas más largas. Por ejemplo, `openhorizon.arch == amd64 && OS == Mojave`. Finalmente, se puede utilizar el paréntesis para crear la prioridad de evaluación dentro de una única expresión.

|Tipo de valor de propiedad|Operadores soportados|
|-------------------|-------------------|
|entero|==, <, >, <=, >=, =, !=|
|serie *|==, !=, =|
|Lista de series|in|
|Booleano|==, =|
|versión|==, =, in**|
{: caption="Tabla 4. Restricciones"}

*Para tipos de serie, una serie entrecomillada, dentro de la cual hay una lista de series separadas por coma, proporcione una lista de valores aceptables; por ejemplo, `hello == "beautiful, world"` será true (verdadero) si hello es "beautiful" o "world".

** Para un rango de versiones, utilice `in` en lugar de `==` .

## Caso de uso de política aún más ampliado
{: #extended_policy_use_case_more}

Para ilustrar la potencia de la naturaleza bidireccional de la política, tenga en cuenta el ejemplo del mundo real de esta sección y añada algunas restricciones al nodo. En nuestro ejemplo, algunos de los cajeros automáticos rurales de acceso peatonal se encuentran en una ubicación cerca del agua que crea un resplandor que el servicio atm1 existente utilizado por los otros cajeros automáticos de acceso peatonal no pueden manejar. Esto requiere un tercer servicio que pueda manejar el resplandor mejor para esos cajeros automáticos y la política se configura de la siguiente manera:

* Política de nodo en los cajeros de acceso peatonal situados frente al agua: propiedades: `camera-type: still`, `atm-type: walk-up`; restricciones: `feature == glare-correction`
* De manera optativa, la política de servicio establecida por los desarrolladores de terceros para atm3: restricciones: `(Opcional)`
* Política de despliegue establecida por el cliente para el servicio atm3: restricciones: `camera-type == still`; propiedades: `feature: glare-correction`  

De nuevo, la política de nodo indica los hechos acerca del nodo; sin embargo, en este caso, el técnico que configura los cajeros situados frente al agua especificó la restricción de que el servicio que se vaya a desplegar en este nodo debe tener la función de corrección de resplandor.

La política de servicio para atm3 tiene la misma restricción que las otras, lo que requiere una cámara en el cajero.

Dado que el cliente sabe que el servicio atm3 maneja mejor el resplandor, el cliente establece esta restricción en la política de despliegue asociada con atm3, la cual satisface la propiedad establecida en el nodo y hace que este servicio se despliegue en los cajeros situados frente al agua.

## Mandatos de política
{: #policy_commands}

|Mandato|Descripción|
|-------|-----------|
|`hzn policy list`|La política de este nodo periférico.|
|`hzn policy new`|Una plantilla de política de nodo vacía que se puede cumplimentar.|
|`hzn policy update --input-file=ARCHIVO-DE-ENTRADA`|Actualizar la política del nodo. Las propiedades incorporadas del nodo se añaden automáticamente si la política de entrada no las contiene.|
|`hzn policy remove [<flags>]`|Eliminar la política del nodo.|
|`hzn exchange node listpolicy [<flags>] <node>`|Visualizar la política de nodo de Horizon Exchange.|
|`hzn exchange node addpolicy --json-file=JSON-FILE [<flags>] <node>`|Añadir o sustituir la política de nodo en Horizon Exchange.|
|`hzn exchange node updatepolicy --json-file=JSON-FILE [<flags>] <node>`|Actualizar un atributo de la política para este nodo en Horizon Exchange.|
|`hzn exchange node removepolicy [<flags>] <node>`|Eliminar la política de nodo en Horizon Exchange.|
|`hzn exchange service listpolicy [<flags>] <service>`|Visualizar la política de servicio de Horizon Exchange.|
|`hzn exchange service newpolicy`|Visualizar una plantilla de política de servicio vacía que se puede cumplimentar|
|`hzn exchange service addpolicy --json-file=JSON-FILE [<flags>] <service>`|Añadir o sustituir la política de servicio en Horizon Exchange.|
|`hzn exchange service removepolicy [<flags>] <service>`|Eliminar la política de servicio en Horizon Exchange.|
|`hzn exchange deployment listpolicy [<flags>] [<policy>]`|Visualizar las políticas de negocio de Horizon Exchange.|
|`hzn exchange deployment new`|Visualizar una plantilla de política de despliegue vacía que se puede cumplimentar|
|`hzn exchange deployment addpolicy --json-file=JSON-FILE [<flags>] <policy>`|Añadir o sustituir una política de despliegue en Horizon Exchange. Utilice `hzn exchange deployment new` para una plantilla de política de despliegue vacía.|
|`hzn exchange deployment updatepolicy --json-file=JSON-FILE [<flags>] <policy>`|Actualizar un atributo de una política de despliegue existente en Horizon Exchange. Los atributos que reciben soporte son los atributos de nivel superior en la definición de política tal como se muestra en el mandato `hzn exchange deployment new`.|
|`hzn exchange deployment removepolicy [<flags>] <policy>`|Eliminar la política de despliegue de la Horizon Exchange.|
|`hzn dev service new [<flags>]`|Crear un proyecto de servicio nuevo. Este mandato generará todos los archivos de metadatos de servicio IEC, incluida la plantilla de política de servicio.|
|`hzn deploycheck policy [<flags>]`|Comprobar la compatibilidad de políticas entre una política de nodo, de servicio y de despliegue. También puede utilizar `hzn deploycheck all` para comprobar que las configuraciones de variable de servicio son correctas.|
{: caption="Tabla 5. Herramientas de desarrollo de política"}

Consulte [Exploración del mandato hzn](../cli/exploring_hzn.md) para obtener más información sobre el uso del mandato `hzn`.
