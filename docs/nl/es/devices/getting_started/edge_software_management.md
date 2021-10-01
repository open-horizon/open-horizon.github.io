---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Gestión de software periférico
{: #edge_software_mgmt}

{{site.data.keyword.edge_devices_notm}} se basa en procesos autónomos distribuidos geográficamente para gestionar el ciclo de vida de software de todos los nodos periféricos.
{:shortdesc}

Los procesos autónomos que manejan la gestión de software de nodo periférico utilizan los servicios de {{site.data.keyword.horizon_exchange}} y el {{site.data.keyword.horizon_switch}} para buscarse en Internet sin revelar sus direcciones. Después de encontrarse el uno al otro, el proceso utiliza {{site.data.keyword.horizon_exchange}} y el {{site.data.keyword.horizon_switch}} para negociar relaciones y, a continuación, colaborar para gestionar el software de nodo periférico. Para obtener más información, consulte [Descubrimiento y negociación](discovery_negotiation.md).

El software de {{site.data.keyword.horizon}} en cualquier host puede actuar como un agente de nodo periférico o un agbot o ambos.

## Agbot (bot de acuerdo)

Las instancias de Agbot se crean centralmente para gestionar cada patrón de despliegue de software para {{site.data.keyword.edge_devices_notm}} que se publica en {{site.data.keyword.horizon_exchange}}. Usted, o uno de sus desarrolladores, también puede ejecutar procesos de agbot en cualquier máquina que pueda acceder al {{site.data.keyword.horizon_exchange}} y al {{site.data.keyword.horizon_switch}}.

Cuando se inicia un agbot y se configura para gestionar un patrón de despliegue de software específico, el agbot se registra con {{site.data.keyword.horizon_exchange}} y empieza a sondear en busca de nodos periféricos registrados para ejecutar el mismo patrón de despliegue. Cuando se descubre un nodo periférico, el agbot envía una solicitud al agente local en dicho nodo periférico para colaborar en la gestión del software.

Cuando se negocia un acuerdo, el agbot envía al agente la información siguiente:

* Los detalles de la política que están incluidos en el patrón de despliegue.
* La lista de servicios y versiones de {{site.data.keyword.horizon}} que están incluidos en el patrón de despliegue.
* Cualquier dependencia entre estos servicios.
* La capacidad de compartir los servicios. Un servicio se puede establecer como `exclusive`, `singleton` o `multiple`.
* Detalles sobre cada contenedor para cada servicio. Estos detalles incluyen la información siguiente: 
  * El registro de Docker en el que está registrado el contenedor, como por ejemplo el registro de DockerHub público o un registro privado.
  * Las credenciales de registro para registros privados.
  * Los detalles del entorno de shell para la configuración y la personalización.
  * Los hash firmados criptográficamente del contenedor y su configuración.

El agbot continúa supervisando el patrón de despliegue de software en {{site.data.keyword.horizon_exchange}} en busca de cualquier cambio, por ejemplo si se publican nuevas versiones de los servicios de {{site.data.keyword.horizon}} para el patrón. Si se detectan cambios, de nuevo el agbot envía solicitudes a cada nodo periférico que está registrado para el patrón para que colabore en la gestión de la transición a la versión de software nueva.

El agbot también comprueba periódicamente cada uno de los nodos periféricos que están registrados para el patrón de despliegue para asegurarse de que se imponen las políticas para el patrón. Si no se está imponiendo una política, el agbot puede detener el acuerdo negociado. Por ejemplo, si el nodo periférico deja de enviar datos o de proporcionar pulsaciones durante un tiempo prolongado, el agbot puede cancelar el acuerdo.  

### Agente de nodo periférico

Se crea un agente de nodo periférico cuando el paquete de software {{site.data.keyword.horizon}} se instala en una máquina periférica. Para obtener más información sobre la instalación, consulte [Instalación de software de {{site.data.keyword.horizon}}](../installing/adding_devices.md).

Cuando más tarde registre el nodo periférico con {{site.data.keyword.horizon_exchange}}, debe proporcionar la información siguiente:

* El URL de {{site.data.keyword.horizon_exchange}}.
* El nombre de nodo periférico y la señal de acceso para el nodo periférico.
* El patrón de despliegue de software que se va a ejecutar en el nodo periférico. Debe proporcionar tanto la organización como el nombre de patrón para identificar el patrón.

Para obtener más información sobre el registro, consulte [Registro de la máquina periférica](../installing/registration.md).

Una vez registrado el nodo periférico, el agente local sondea el {{site.data.keyword.horizon_switch}} en busca de solicitudes de colaboración de procesos de agbot remotos. Cuando un agbot descubre el agente por su patrón de despliegue configurado, el agbot envía una solicitud al agente de nodo periférico para negociar la colaboración en la gestión del ciclo de vida del software para el nodo periférico. Cuando se alcanza un acuerdo, el agbot envía información al nodo periférico.

El agente extrae los contenedores de Docker especificados de los registros adecuados. A continuación, el agente verifica los hash de contenedor y las firmas criptográficas. El agente inicia después los contenedores por orden inverso de dependencia con las configuraciones de entorno especificadas. Cuando los contenedores se están ejecutando, el agente local supervisa los contenedores. Si cualquier contenedor deja de ejecutarse inesperadamente, el agente vuelve a iniciar el contenedor para intentar mantener intacto el patrón de despliegue en el nodo periférico.

### Dependencias de servicio de {{site.data.keyword.horizon}}

Aunque el agente {{site.data.keyword.horizon}} trabaja para iniciar y gestionar los contenedores en el patrón de despliegue asignado, las dependencias entre los servicios deben gestionarse en el código de contenedor de servicios. Aunque los contenedores se inician por orden inverso de dependencia, {{site.data.keyword.horizon}} no puede garantizar que los proveedores de servicios están totalmente iniciados y listos para proporcionar servicio antes de que se inicien los consumidores de servicio. Los consumidores deben manejar estratégicamente el posible inicio lento de los servicios de los que dependen. Puesto que los servicios que proporcionan contenedores pueden fallar y quedar inhabilitados, los consumidores de servicio también deben manejar la ausencia de los servicios que consumen. 

El agente local detecta cuándo un servicio se detiene de manera anómala e inicia el servicio con el mismo nombre de red, en la misma red privada de Docker. Se produce un breve tiempo de inactividad durante el proceso de reinicio. El servicio de consumo debe manejar también el breve tiempo de inactividad o el servicio de consumo también puede fallar.

El agente tiene una tolerancia limitada para las anomalías. Si un contenedor se cuelga repetida y rápidamente, el agente puede renunciar a reiniciar los servicios que fallan perpetuamente, y puede cancelar el acuerdo.

### Red de Docker de {{site.data.keyword.horizon}}

{{site.data.keyword.horizon}} utiliza las características de red de Docker para aislar los contenedores de Docker que proporcionan servicios. Este aislamiento garantiza que solo los consumidores autorizados pueden acceder a los contenedores. Cada contenedor se inicia por orden inverso de dependencias, los productores primero y luego los consumidores en una red virtual Docker privada. Siempre que se inicia un contenedor de consumo de servicio, el contenedor se conecta a la red privada para el contenedor de productores correspondiente. Los contenedores de productores sólo son accesibles para los consumidores cuyas dependencias del productor son conocidas por {{site.data.keyword.horizon}}. Debido a la forma en que se implementan las redes de Docker, todos los contenedores son accesibles desde los shells de host. 

Si tiene que obtener la dirección IP de cualquier contenedor, puede utilizar el mandato `docker inspect <containerID>` para obtener la `IPAddress` asignada. Puede alcanzar cualquier contenedor desde los shells de host.

## Seguridad y privacidad

Aunque los agentes de nodo periférico y los agbots de patrón de despliegue se pueden descubrir uno a otro, los componentes mantienen la privacidad completa hasta que se negocia formalmente un acuerdo de colaboración. Las identidades de agente y agbot y toda la comunicación están cifradas. Las colaboraciones de gestión de software también están cifradas. Todo el software gestionado está firmado criptográficamente. Para obtener más información acerca de los aspectos de privacidad y seguridad de {{site.data.keyword.edge_devices_notm}}, consulte [Seguridad y privacidad](../user_management/security_privacy.md).
