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

# Visión general del funcionamiento de {{site.data.keyword.edge_devices_notm}}
{: #overview}

{{site.data.keyword.edge_devices_notm}} se ha diseñado específicamente para la gestión de nodos periféricos, para minimizar los riesgos de despliegue y para gestionar el ciclo de vida del software de servicio en nodos periféricos de forma totalmente autónoma.
{:shortdesc}

## Arquitectura de {{site.data.keyword.edge_devices_notm}}
{: #iec4d_arch}

Otras soluciones de Edge Computing normalmente se centran en una de las estrategias de arquitectura siguientes:

* Una autorizada centralizada potente para imponer la conformidad de software de nodos periféricos.
* Pasar la responsabilidad de la conformidad de software a los propietarios de los nodos periféricos, que deben supervisar las actualizaciones de software y ocuparse manualmente de conseguir la conformidad de sus propios nodos periféricos.

La primera se centra en la autoridad, creando un único punto de anomalía y un objetivo que los atacantes pueden explotar para controlar toda la flota de nodos periféricos. La última solución puede hacer que haya grandes porcentajes de nodos periféricos que no tengan las actualizaciones de software más recientes instaladas. Si no todos los nodos periféricos tienen la versión más reciente o todos los arreglos disponibles, los nodos periféricos pueden ser vulnerables a los atacantes. Ambos enfoques suelen basarse también en la autoridad central como base para el establecimiento de la confianza.

<p align="center">
<img src="../../images/edge/overview_illustration.svg" width="70%" alt="Ilustración del alcance global de Edge Computing.">
</p>

En contraste con estos enfoques de solución, {{site.data.keyword.edge_devices_notm}} está descentralizado. {{site.data.keyword.edge_devices_notm}} gestiona la conformidad de software de servicio automáticamente en nodos periféricos sin ninguna intervención manual. En cada nodo periférico se ejecutan procesos de agente totalmente autónomos controlados por las políticas que se especifican durante el registro de la máquina con {{site.data.keyword.edge_devices_notm}}. Los procesos de agbot (bot de acuerdo) descentralizados y totalmente autónomos se ejecutan en una ubicación central, pero se pueden ejecutar en cualquier parte incluidos los nodos periféricos. Al igual que los procesos de agente, los agbots se rigen por políticas. Los agentes y los agbots manejan las mayor parte de la gestión del ciclo de vida del software de servicio periférico para los nodos periféricos e imponen la conformidad del software en los nodos periféricos.

Para mayor eficiencia, {{site.data.keyword.edge_devices_notm}} incluye dos servicios centralizados, Exchange y el panel de conmutación. Estos servicios no tienen autoridad central sobre los procesos autónomos de agente y agbot. En lugar de esto, estos servicios proporcionan servicios simples de descubrimiento y compartición de metadatos (Exchange) y un servicio de buzón privado para dar soporte a comunicaciones de igual a igual (el panel de conmutación). Estos servicios dan soporte al trabajo totalmente autónomo de los agentes y los agbots.

Por último, la consola {{site.data.keyword.edge_devices_notm}} ayuda a los administradores a establecer la política y supervisar el estado de los nodos periféricos.

Cada uno de los cinco tipos de componentes de {{site.data.keyword.edge_devices_notm}} (agentes, agbots, Exchange, panel de conmutación y consola) tiene un área restringida de responsabilidad. Cada componente no tiene autorización ni credenciales para actuar fuera de su respectiva área de responsabilidad. Al dividir la responsabilidad y determinar el ámbito de la autoridad y las credenciales, {{site.data.keyword.edge_devices_notm}} ofrece una gestión de riesgos para el despliegue de nodo periférico.

## Descubrimiento y negociación
{: #discovery_negotiation}

{{site.data.keyword.edge_devices_notm}}, que se basa en el proyecto [1 de {{site.data.keyword.horizon_open}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/), está descentralizado y distribuido principalmente. Los procesos de agente y bot de acuerdo (agbot) autónomos colaboran en la gestión de software de todos los nodos periféricos registrados.

Un proceso de agente autónomo se ejecuta en cada nodo periférico Horizon para imponer las políticas establecidas por el propietario del dispositivo periférico.

Los agbots autónomos supervisan los patrones de despliegue y las políticas en Exchange y buscan los agentes de nodo periférico que todavía no están en conformidad. Los agbots proponen acuerdos a los nodos periféricos para llevarlos a la conformidad. Cuando un agbot y un agente llegan a un acuerdo, cooperan para gestionar el ciclo de vida del software de los servicios periféricos en el nodo periférico.

Los agbots y los agentes utilizan los servicios centralizados siguientes para buscarse el uno al otro, establecer la confianza y comunicarse de forma segura en {{site.data.keyword.edge_devices_notm}}:

* {{site.data.keyword.horizon_exchange}}, que facilita el descubrimiento.
* {{site.data.keyword.horizon_switch}}, que habilita las comunicaciones de igual a igual seguras y privadas entre los agbots y los agentes.

<img src="../../images/edge/distributed.svg" width="90%" alt="Servicios centralizados y descentralizados">

### {{site.data.keyword.horizon_exchange}}
{: #iec4d_exchange}

{{site.data.keyword.horizon_exchange}} permite a los propietarios de dispositivos periféricos registrar nodos periféricos para la gestión del ciclo de vida de software. Cuando se registra un nodo periférico con {{site.data.keyword.horizon_exchange}} para {{site.data.keyword.edge_devices_notm}}, se especifica el patrón de despliegue o la política para el nodo periférico. (En su núcleo, un patrón de despliegue es simplemente un conjunto predefinido y con nombre de políticas para gestionar nodos periféricos.) Los patrones y las políticas se deben diseñar, desarrollar, probar, firmar y publicar en {{site.data.keyword.horizon_exchange}}.

Cada nodo periférico se registra con un ID exclusivo y una señal de seguridad. Los nodos se pueden registrar para utilizar un patrón o políticas proporcionados por su propia organización, o un patrón que proporciona otra organización.

Cuando se publica un patrón o una política en {{site.data.keyword.horizon_exchange}}, los agbots tratan de descubrir los nodos periféricos afectados por el patrón o la política nuevos o actualizados. Cuando se encuentra un nodo periférico registrado, un agbot negocia con el agente del nodo periférico.

Si bien {{site.data.keyword.horizon_exchange}} permite que los agbots encuentren los nodos periféricos que están registrados para utilizar patrones o políticas, {{site.data.keyword.horizon_exchange}} no está directamente implicado en el proceso de gestión de software del nodo periférico. Los agbots y los agentes manejan el proceso de gestión de software. {{site.data.keyword.horizon_exchange}} no tiene autoridad sobre el nodo periférico y no inicia ningún contacto con los agentes de nodo periférico.

### {{site.data.keyword.horizon_switch}}
{: #horizon_switch}

Cuando un agbot descubre un nodo periférico que se ve afectado por un patrón o una política nuevos o actualizados, el agbot utiliza el panel de conmutación de {{site.data.keyword.horizon}} para enviar un mensaje privado al agente en dicho nodo. Este mensaje es una propuesta de acuerdo para colaborar en la gestión del ciclo de vida de software del nodo periférico. Cuando el agente recibe el mensaje del agbot en su buzón privado en {{site.data.keyword.horizon_switch}}, descifra y evalúa la propuesta. Si está dentro de su propia política de nodo, el nodo envía un mensaje de aceptación al agbot. De lo contrario, el nodo rechaza la propuesta. Cuando el agbot recibe una aceptación del acuerdo en su buzón privado en {{site.data.keyword.horizon_switch}}, la negociación se ha completado.

Tanto los agentes como los agbots publican claves públicas en {{site.data.keyword.horizon_switch}} para permitir una comunicación segura y privada que utiliza un secreto-perfecto-adelante. Con este cifrado, el {{site.data.keyword.horizon_switch}} sirve solo de gestor de buzones. No es capaz de descifrar los mensajes.

Nota: puesto que toda la comunicación se ha mediado a través del
{{site.data.keyword.horizon_switch}}, las direcciones IP de los nodos periféricos no se revelan a ningún
agbot hasta que el agente de cada nodo periférico elige revelar esta información. El agente revela esta información cuando el agente y el agbot negocian con éxito un acuerdo.

## Gestión del ciclo de vida del software periférico
{: #edge_lifecycle}

Después de que el agbot y el agente lleguen a un acuerdo para un patrón concreto o un conjunto de políticas, colaboran para gestionar el ciclo de vida del software del patrón o de la política en el nodo periférico. El agbot supervisa el patrón o la política ya que evoluciona con el paso del tiempo y supervisa el nodo periférico para su conformidad. El agente descarga de forma local el software en el nodo periférico, verifica la firma para el software y, si se verifica, ejecuta y supervisa el software. Si es necesario, el agente actualiza el software y detiene el software cuando procede.

El agente extrae las imágenes del contenedor Docker del servicio periférico especificado de los registros apropiados y verifica las firmas de la imagen del contenedor. A continuación, el agente inicia los contenedores en orden de dependencia inversa con la configuración que se especifica en el patrón o la política. Cuando los contenedores se están ejecutando, el agente local supervisa los contenedores. Si algún contenedor deja de ejecutar inesperadamente, el agente vuelve a iniciar el contenedor para intentar mantener el patrón o la política en conformidad en el nodo periférico.

El agente tiene una tolerancia limitada para las anomalías. Si un contenedor se cuelga repetida y rápidamente, el agente deja de intentar reiniciar los servicios que fallan todo el rato y cancela el acuerdo.

### Dependencias de servicio de {{site.data.keyword.horizon}}
{: #service_dependencies}

Un servicio periférico puede especificar en sus dependencias de metadatos en otros servicios periféricos que utiliza. Cuando un servicio periférico se despliega en un nodo periférico como resultado de un patrón o de una política, el agente también desplegará todos los servicios periféricos que requiere (en orden de dependencia inversa). Se admite cualquier número de niveles de dependencias de servicio.

### Red de Docker de {{site.data.keyword.horizon}}
{: #docker_networking}

{{site.data.keyword.horizon}} utiliza las características de red de Docker para aislar los contenedores Docker, de forma que solo los servicios que los requieren se pueden conectar a los mismos. Cuando se inicia un contenedor de servicios que depende de otro servicio, el contenedor de servicios se conecta a la red privada del contenedor de servicios dependiente. Esto facilita la ejecución de servicios periféricos creados por organizaciones distintas, ya que cada servicio periférico solo puede acceder are otros servicios que aparecen listados en sus metadatos.
