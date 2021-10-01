---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Seguridad y privacidad
{: #security_privacy}

{{site.data.keyword.edge_devices_notm}}, basado en {{site.data.keyword.horizon}}, es tan seguro como se puede ser contra ataques y privacidad y protege la privacidad de los participantes. {{site.data.keyword.edge_devices_notm}} se basa en procesos de agente autónomos y procesos de bot de acuerdo (agbot) distribuidos geográficamente para la gestión de software periférico y para mantener el anonimato.
{:shortdesc}

Para mantener el anonimato, los procesos de agente y agbot solo comparten sus claves públicas durante todo el proceso de descubrimiento y negociación de {{site.data.keyword.edge_devices_notm}}. De forma predeterminada, todas las partes de {{site.data.keyword.edge_devices_notm}} tratan a cada una de las partes como una entidad no de confianza. Las partes comparten información y solo colaboran cuando se establece la confianza, se han completado las negociaciones entre las partes y se ha establecido un acuerdo formal.

## Plano de control distribuido
{: #dc_pane}

A diferencia de las típicas plataformas centralizadas de Internet de las Cosas (IoT) y los sistemas de control basados en nube, el plano de control de {{site.data.keyword.edge_devices_notm}} está descentralizado en su mayor parte. Cada rol dentro del sistema tiene un ámbito de autorización limitado por lo que cada rol tiene sólo solo nivel mínimo de autoridad que se necesita para completar las tareas asociadas. Ninguna autoridad puede certificar el control de todo el sistema. Un usuario o rol no puede obtener acceso a todos los nodos del sistema comprometiendo un único host o componente de software.

El plano de control lo implementan tres diferentes entidades de software:
* Agentes de {{site.data.keyword.horizon}}
* Agbots de {{site.data.keyword.horizon}}
* {{site.data.keyword.horizon_exchange}}

Los agentes y los agbots de {{site.data.keyword.horizon}} son las entidades principales y actúan de manera autónoma para gestionar los nodos periféricos. {{site.data.keyword.horizon_exchange}} facilita el descubrimiento, la negociación y las
comunicaciones seguras entre los agentes y los agbots.

### Agentes
{: #agents}

Los agentes de {{site.data.keyword.horizon}} superan en número a todos los demás agentes de {{site.data.keyword.edge_devices_notm}}. Un agente se ejecuta en cada uno de los nodos periféricos gestionados. Cada agente tiene autorización para gestionar solo ese nodo periférico único. El agente publicita su clave pública en {{site.data.keyword.horizon_exchange}} y negocia con procesos de agbot remotos para gestionar el software del nodo local. El agente sólo espera recibir comunicaciones de los agbots que son responsables de los patrones de despliegue dentro de la organización del agente.

Un agente comprometido no tiene ninguna autoridad para afectar a ningún otro nodo periférico, ni a ningún otro componente del sistema. Si el sistema operativo de host o el proceso de agente en un nodo periférico está pirateado o comprometido de algún otro modo, sólo queda comprometido ese nodo periférico. El resto de componentes del sistema {{site.data.keyword.edge_devices_notm}} no se ven afectados.

El agente de nodo periférico puede ser el componente más potente de un nodo periférico, pero es el
componente menos capaz de comprometer la seguridad del sistema
{{site.data.keyword.edge_devices_notm}} general. El agente es responsable de descargar software en un nodo periférico, verificar el software y después ejecutar y enlazar el software con otro software y hardware en el nodo periférico. Sin embargo, dentro de la seguridad global de todo el sistema para {{site.data.keyword.edge_devices_notm}}, el agente no tiene autoridad más allá del nodo periférico en el que se ejecuta el agente.

### Agbots
{: #agbots}

Los procesos de agbot de {{site.data.keyword.horizon}} se pueden ejecutar en cualquier parte. De forma predeterminada, los procesos se ejecutan automáticamente. Las instancias de agbot son los segundos actores más comunes en {{site.data.keyword.horizon}}. Cada agbot es responsable únicamente de los patrones de despliegue que se asignan a ese agbot. Los patrones de despliegue están formados principalmente por políticas y un manifiesto de servicio de software. Una sola instancia de agbot puede gestionar varios patrones de despliegue para una organización.

Los desarrolladores publican patrones de despliegue en el contexto de una organización de usuario de {{site.data.keyword.edge_devices_notm}}. Los agbots sirven patrones de despliegue a agentes de {{site.data.keyword.horizon}}. Cuando un nodo periférico borde se registra con {{site.data.keyword.horizon_exchange}}, se asigna al nodo periférico un patrón de despliegue para la organización. El agente en ese nodo periférico acepta ofertas solo de los agbots que presentan ese patrón de despliegue específico de esa organización específica. El agbot es un vehículo de entrega para patrones de despliegue, pero el propio patrón de despliegue debe ser aceptable para las políticas que el propietario del nodo periférico establece en el nodo periférico. El patrón de despliegue debe pasar la validación de la firma o el agente no aceptará el patrón.

Un agbot comprometido puede intentar proponer acuerdos malintencionados con nodos periféricos e intentar desplegar un patrón de despliegue malicioso en nodos periféricos. Sin embargo, los agentes de nodo de borde aceptan acuerdos solo para los patrones de despliegue que los agentes han solicitado a través del registro y que son aceptables para las políticas que se establecen en el nodo periférico. El agente también utiliza su clave pública para validar la firma criptográfica del patrón antes de que acepte el patrón.

A pesar de que los procesos de agbot organizan la instalación de software y las actualizaciones de mantenimiento, el agbot no tiene autoridad para obligar a ningún nodo periférico ni a ningún agente a aceptar el software que el agbot está ofreciendo. El agente de cada nodo periférico individual decide qué software se debe aceptar o rechazar. El agente toma esta decisión según las claves públicas que tiene instaladas y las políticas establecidas por el propietario del nodo periférico cuando el propietario ha registrado el nodo periférico con {{site.data.keyword.horizon_exchange}}.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} es un servicio centralizado, pero geográficamente replicado y con equilibrio de carga que habilita a los agentes distribuidos y a los agbots para reunirse y negociar acuerdos. Para obtener más información, consulte [Visión general de {{site.data.keyword.edge}}](../../getting_started/overview_ieam.md).

{{site.data.keyword.horizon_exchange}} funciona también como base de datos compartida de metadatos para usuarios, organizaciones, nodos periféricos y todos los servicios, las políticas y los patrones de despliegue publicados.

Los desarrolladores publican los metadatos JSON acerca de las implementaciones de servicio de software, las políticas
y los patrones de despliegue que crean en {{site.data.keyword.horizon_exchange}}. Esta información se somete a un algoritmo hash y está firmada criptográficamente por el desarrollador. Los propietarios de nodos periféricos tienen que instalar claves públicas para el software durante el registro del nodo periférico para que el agente local pueda utilizar las claves para validar las firmas.

{{site.data.keyword.horizon_exchange}} comprometido puede ofrecer maliciosamente información falsa a los procesos de agente y agbot, pero cualquier impacto es mínimo debido a los mecanismos de verificación que se crean en el sistema. {{site.data.keyword.horizon_exchange}} no posee las credenciales necesarias para firmar los metadatos maliciosamente. {{site.data.keyword.horizon_exchange}} comprometido no puede suplantar maliciosamente a ningún usuario u organización. {{site.data.keyword.horizon_exchange}}
actúa como almacén para los artefactos publicados por los desarrolladores y por los propietarios de
nodos periféricos, para utilizarlos en la habilitación de los agbots durante los procesos de descubrimiento y negociación.

{{site.data.keyword.horizon_exchange}} también media y protege todas las comunicaciones
entre los agentes y los agbots. Implementa un mecanismo de buzón en el que los participantes pueden dejar
mensajes que van dirigidos a otros participantes. Para recibir mensajes, los participantes deben sondear el
conmutador de Horizon para ver si los buzones contienen mensajes.

Además, tanto los agentes como los agbots comparten sus claves públicas con
{{site.data.keyword.horizon_exchange}} para habilitar las comunicaciones seguras y privadas. Cuando cualquier participante tiene que comunicarse con otro, ese remitente utiliza la clave pública del destinatario deseado para identificar al destinatario. El remitente utiliza esa clave pública para cifrar un mensaje para el destinatario. A continuación, el destinatario puede cifrar su respuesta mediante la clave pública del remitente.

Este enfoque asegura que Horizon Exchange no pueda realizar escuchas no autorizadas
en los mensajes porque carece de las claves compartidas necesarias para descifrar los mensajes. Sólo los
destinatarios deseados pueden descifrar los mensajes. Un Horizon Exchange corrompido no tiene visibilidad
en las comunicaciones de cualquier participante y no puede insertar comunicaciones maliciosas
en las conversaciones entre participantes.

## Ataque de denegación de servicio
{: #denial}

{{site.data.keyword.horizon}} se basa en servicios centralizados. Los servicios
centralizados en sistemas típicos de Internet de las cosas son generalmente vulnerables a
los ataques de denegación de servicio. Para {{site.data.keyword.edge_devices_notm}},
estos servicios centralizados sólo se utilizan para tareas de descubrimiento, negociación y actualización. Los procesos de agente y agbot distribuidos y autónomos solo utilizan los servicios centralizados cuando los procesos deben completar tareas de descubrimiento, negociación y actualización. De lo contrario, cuando se forman acuerdos, el sistema puede seguir funcionando normalmente incluso cuando esos servicios centralizados están fuera de línea. Este comportamiento garantiza que {{site.data.keyword.edge_devices_notm}} permanece activo si hay ataques en los servicios centralizados.

## Criptografía asimétrica
{: #asym_crypt}

La mayor parte de la criptografía en {{site.data.keyword.edge_devices_notm}} se basa en la criptografía de clave asimétrica. Con
esta forma de criptografía, el usuario y los desarrolladores deben generar un par de claves utilizando
los mandatos `hzn key` y utilizar la clave privada para firmar criptográficamente cualquier
software o servicio que desee publicar. Debe instalar la clave pública en los nodos periféricos en los que se debe ejecutar el software o el servicio para que se pueda verificar la firma criptográfica del software o servicio.

Los agentes y los agbots firman criptográficamente sus mensajes entre sí mediante sus claves privadas y utilizan la clave pública de su homólogo para verificar los mensajes que reciben. Los agentes y los agbots también cifran sus mensajes con la clave pública de la otra parte para asegurarse de que sólo el destinatario deseado puede descifrar el mensaje.

Si la clave privada y las credenciales de un agente, agbot o usuario se ven comprometidas, solo quedan expuestos los artefactos que están bajo el control de esa entidad. 

## Resumen
{: #summary}

Mediante el uso de algoritmos hash, firmas criptográficas y cifrado, {{site.data.keyword.edge_devices_notm}} protege la mayoría de partes de la plataforma contra el acceso no deseado. Al estar principalmente descentralizado, {{site.data.keyword.edge_devices_notm}} evita quedar expuesto a la mayoría de ataques que se producen normalmente en plataformas más tradicionales de Internet de las cosas. Al restringir el ámbito de la autoridad y la influencia de los roles de participante, {{site.data.keyword.edge_devices_notm}} contiene el daño potencial de un host comprometido o de un componente de software comprometido a esa parte del sistema. Incluso los ataques externos a gran escala sobre los servicios centralizados de los servicios de {{site.data.keyword.horizon}} que se utilizan en {{site.data.keyword.edge_devices_notm}} tienen un impacto mínimo sobre los participantes que ya están de acuerdo. Los participantes que están bajo un acuerdo vigente siguen funcionando normalmente durante cualquier interrupción.
