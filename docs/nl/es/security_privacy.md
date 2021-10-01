---

copyright:
years: 2021
lastupdated: "2021-02-20"
 
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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), basado en [Open Horizon](https://github.com/open-horizon), utiliza distintas tecnologías de seguridad para garantizar su seguridad contra los ataques y proteger la privacidad. {{site.data.keyword.ieam}} se basa en procesos de agente autónomo distribuidos geográficamente para la gestión de software periférico. Como resultado, tanto el centro de gestión de {{site.data.keyword.ieam}} y los agentes representan destinos potenciales para las brechas de seguridad. Este documento explica cómo {{site.data.keyword.ieam}} mitiga o elimina amenazas.
{:shortdesc}

## Centro de gestión
El centro de gestión de {{site.data.keyword.ieam}} se despliega en una plataforma de OpenShift Container; por lo tanto, hereda todas las ventajas inherentes del mecanismo de seguridad. Todo el tráfico de red de centro de gestión de {{site.data.keyword.ieam}} atraviesa un punto de entrada protegido por TLS. La comunicación de red de centro de gestión entre los componentes de centro de gestión de {{site.data.keyword.ieam}} realiza sin TLS.

## Plano de control seguro
{: #dc_pane}

Los agentes distribuidos y de centro de gestión de {{site.data.keyword.ieam}} se comunican a través del plano de control para desplegar las cargas de trabajo y los modelos en los nodos periféricos. A diferencia de las típicas plataformas de Internet de las Cosas (IoT) centralizadas y los sistemas de control basados en la nube, el plano de control de {{site.data.keyword.ieam}} está principalmente descentralizado. Cada actor del sistema tiene un ámbito limitado de autoridad para que cada actor tenga solo el nivel mínimo de autorización necesario para completar sus tareas. Ningún actor único puede certificar el control en todo el sistema. Además, un único actor no puede obtener acceso a todos los nodos periféricos del sistema comprometiendo cualquier nodo periférico, host o componente de software único.

El plano de control lo implementan tres diferentes entidades de software:
* Agentes de {{site.data.keyword.horizon}} abiertos
* Agbots de {{site.data.keyword.horizon}} abiertos
* {{site.data.keyword.horizon_exchange}} abierto

Los agente y agbots de {{site.data.keyword.horizon}} abiertos son los actores principales del plano de control. {{site.data.keyword.horizon_exchange}} facilita el descubrimiento y la comunicación segura entre los agentes y los agbots. Juntos, proporcionan protección a nivel de mensaje utilizando un algoritmo que se denomina secreto-perfecto-adelante.

De forma predeterminada, los agentes y los agbots se comunican con Exchange a través de TLS 1.3. Pero el propio TLS no proporciona suficiente seguridad. {{site.data.keyword.ieam}} cifra cada mensaje de control que fluye entre agentes y agbots antes de que se envíe a través de la red. Cada agente y agbot genera un par de claves RSA de 2048 bits y publica su clave pública en Exchange. La clave privada se almacena en el almacenamiento protegido por root de cada actor. Otros actores del sistema utilizan la clave pública del receptor de mensajes para cifrar una clave simétrica que se utiliza para cifrar mensajes de plano de control. Esto garantiza que solo el destinatario deseado pueda descifrar la clave simétrica; por lo tanto, el propio mensaje. El uso del secreto-perfecto-adelante en el plano de control proporciona seguridad adicional, como la prevención de ataques de hombre en el medio, que TLS no impide.

### Agentes
{: #agents}

Los agentes de {{site.data.keyword.horizon_open}} superan en número a todos los demás agentes de {{site.data.keyword.ieam}}. Un agente se ejecuta en cada uno de los nodos periféricos gestionados. Cada agente tiene autorización para gestionar solo ese nodo periférico. Un agente comprometido no tiene autorización para afectar a otros nodos periféricos ni a ningún otro componente del sistema. Cada nodo tiene credenciales exclusivas que se almacenan en su propio almacenamiento protegido por root. {{site.data.keyword.horizon_exchange}} garantiza que un nodo solo pueda acceder a sus propios recursos. Cuando se registra un nodo mediante el mandato `hzn register`, se puede proporcionar una señal de autenticación. Sin embargo, lo mejor es permitir que el agente genere su propia señal para que ninguna persona tenga conocimiento de las credenciales del nodo, lo que reduce el potencial para comprometer el nodo periférico.

El agente está protegido de los ataques de red porque no tiene puertos de escucha en la red de host. Toda la comunicación entre el agente y el centro de gestión la lleva a cabo el agente que sondea el centro de gestión. Además, se recomienda encarecidamente a los usuarios que protejan los nodos periféricos con un cortafuegos de red que impida la intrusión en el host del nodo. A pesar de estas protecciones, si el sistema operativo de host del agente o el propio proceso de agente se piratean o se comprometen de algún otro modo, solo ese nodo periférico está comprometido. El resto de componentes del sistema {{site.data.keyword.ieam}} no se ven afectados.

El agente es responsable de descargar y iniciar cargas de trabajo contenerizadas. Para asegurarse de que la seguridad de la imagen de contenedor descargada y su configuración no se vea comprometida, el agente verifica la firma digital de imagen de contenedor y la firma digital de configuración de despliegue. Cuando un contenedor se almacena en un registro de contenedor, el registro proporciona una firma digital para la imagen (por ejemplo, un hash SHA256). El registro de contenedor gestiona las claves que se utilizan para crear la firma. Cuando un servicio de {{site.data.keyword.ieam}} se publica utilizando el mandato `hzn exchange service publish`, obtiene la firma de imagen y la almacena con el servicio publicado en {{site.data.keyword.horizon_exchange}}. La firma digital de la imagen se pasa al agente sobre el plano de control seguro, lo que permite que el agente verifique la firma de imagen de contenedor con la imagen descargada. Si la firma de imagen no coincide con la imagen, el agente no inicia el contenedor. El proceso es similar para la configuración del contenedor, con una excepción. El mandato `hzn exchange service publish` firma la configuración de contenedor y almacena la firma en {{site.data.keyword.horizon_exchange}}. En este caso, el usuario (que publica el servicio) debe proporcionar el par de claves RSA que se utiliza para crear la firma. El mandato `hzn key create` se puede utilizar para generar claves para este fin si el usuario aún no tiene ninguna clave. La clave pública se almacena en Exchange con la firma de la configuración de contenedor y se pasa al agente a través del plano de control seguro. A continuación, el agente puede utilizar la clave pública para verificar la configuración de contenedor. Si prefiere utilizar un par de claves diferente para cada configuración de contenedor, la clave privada utilizada para firmar esta configuración de contenedor se puede descartar ahora, porque ya no se necesita. Consulte [Desarrollo de servicios periféricos](../developing/developing_edge_services.md) para obtener más detalles sobre la publicación de una carga de trabajo.

Cuando un modelo se despliega en un nodo periférico, el agente descarga el modelo y verifica la firma del modelo para asegurarse de que no se ha manipulado en tránsito. La firma y la clave de verificación se crean cuando el modelo se publica en el concentrador de gestión. El agente almacena el modelo en el almacenamiento protegido raíz del host. Se proporciona una credencial a cada servicio cuando el agente lo inicia. El servicio utiliza esa credencial para identificarse y habilitar el acceso a los modelos a los que se le permite al servicio acceder. Cada objeto de modelo de {{site.data.keyword.ieam}} indica la lista de servicios, que pueden acceder al modelo. Cada servicio obtiene una nueva credencial cada vez que {{site.data.keyword.ieam}} lo reinicia. {{site.data.keyword.ieam}} no cifra el objeto de modelo. Dado que {{site.data.keyword.ieam}} trata el objeto de modelo como un paquete de bits, una implementación de servicio puede cifrar el modelo si es necesario. Para obtener más información sobre cómo utilizar MMS, consulte [Detalles de gestión de modelos](../developing/model_management_details.md).

### Agbots
{: #agbots}

El centro de gestión de {{site.data.keyword.ieam}} contiene varias instancias de un agbot, que son responsables de iniciar el despliegue de las cargas de trabajo en todos los nodos periféricos registrados en el centro de gestión. Los agbots examinan periódicamente todas las políticas de despliegue y los patrones que se han publicado en Exchange, asegurándose de que los servicios de esos patrones y políticas se despliegan en todos los nodos periféricos correctos. Cuando un agbot inicia una solicitud de despliegue, envía la solicitud a través del plano de control seguro. La solicitud de despliegue contiene todo lo que el agente necesita para verificar la carga de trabajo y su configuración, si el agente decide aceptar la solicitud. Consulte [Agentes](security_privacy.md#agents) para obtener detalles de seguridad sobre lo que hace el agente. El agbot también indica a MMS dónde y cuándo desplegar modelos. Consulte [Agentes](security_privacy.md#agents) para obtener detalles de seguridad sobre cómo se gestionan los modelos.

Un agbot comprometido puede intentar proponer despliegues de carga de trabajo maliciosos, pero el despliegue propuesto debe cumplir los requisitos de seguridad indicados en la sección de agente. Aunque el agbot inicia el despliegue de carga de trabajo, no tiene autorización para crear cargas de trabajo y configuraciones de contenedor y, por lo tanto, no puede proponer sus propias cargas de trabajo maliciosas.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}} es un servidor de API REST centralizado, replicado y con equilibrio de carga. Funciona como una base de datos compartida de metadatos para usuarios, organizaciones, nodos periféricos, servicios publicados, políticas y patrones. También permite que los agentes distribuidos y los agbots desplieguen cargas de trabajo contenerizadas proporcionando el almacenamiento para el plano de control seguro, hasta que se puedan recuperar los mensajes. {{site.data.keyword.horizon_exchange}} no puede leer los mensajes de control porque no posee la clave RSA privada para descifrar el mensaje. Así, un {{site.data.keyword.horizon_exchange}} comprometido es incapaz de espiar el tráfico del plano de control. Para obtener más información sobre el rol de Exchange, consulte [Visión general de {{site.data.keyword.edge}}](../getting_started/overview_ieam.md).

## Servicios de modalidad privilegiada
{: #priv_services}
En una máquina de host, algunas tareas solo puede realizarlas una cuenta con acceso root. El equivalente para los contenedores es la modalidad privilegiada. Aunque los contenedores generalmente no necesitan la modalidad privilegiada en el host, hay algunos casos de uso en los que es necesaria. En {{site.data.keyword.ieam}}, puede especificar que un servicio de aplicación debe desplegarse con la ejecución de proceso privilegiada habilitada. De forma predeterminada, está inhabilitada. Debe habilitarla explícitamente en la [configuración de despliegue](https://open-horizon.github.io/anax/deployment_string.html) del archivo de Definición de servicio correspondiente para cada Servicio que deba ejecutarse con esta modalidad. Asimismo, cualquier nodo en el que desee desplegar dicho servicio también deberá permitir explícitamente contenedores de modalidad privilegiada. Esto garantiza que los propietarios de los nodos tengan algún control sobre qué servicios se ejecutan en sus nodos periféricos. Para ver un ejemplo sobre cómo habilitar la política de modalidad privilegiada en un nodo periférico, consulte la [política de nodo privilegiada](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Si la definición de servicio o una de sus dependencias requiere la modalidad privilegiada, la política de nodo también debe permitir la modalidad privilegiada o ninguno de los servicios se desplegará en el nodo. Para ver un análisis detallado de la modalidad privilegiada, consulte [¿Qué es la modalidad privilegiada y la necesito en mi caso?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).

## Ataque de denegación de servicio
{: #denial}

El centro de gestión de {{site.data.keyword.ieam}} es un servicio centralizado. Los servicios centralizados de entornos típicos basados en la nube son generalmente vulnerables a los ataques de denegación de servicio. El agente necesita una conexión sólo cuando se registra por primera vez en el hub o cuando está negociando el despliegue de una carga de trabajo. En todas las demás ocasiones, el agente sigue funcionando normalmente incluso cuando se desconecta del centro de gestión de {{site.data.keyword.ieam}}.  Esto garantiza que el agente de {{site.data.keyword.ieam}} permanece activo en el nodo periférico incluso si el centro de gestión está bajo ataque.

## Sistema de gestión de modelos
{: #malware}

{{site.data.keyword.ieam}} no realiza una exploración de malware o virus en los datos cargados en el MMS. Asegúrese de que los datos cargados se hayan explorado antes de cargarse en el MMS.

## Datos en reposo
{: #drest}

{{site.data.keyword.ieam}} no cifra los datos en reposo. El cifrado de datos en reposo debe implementarse con un programa de utilidad que sea adecuado para el sistema operativo de host en el que se ejecuta el agente o el centro de gestión de {{site.data.keyword.ieam}}.

## Estándares de seguridad
{: #standards}

En {{site.data.keyword.ieam}} se utilizan los siguientes estándares de seguridad:
* Se utiliza TLS 1.2 (HTTPS) para el cifrado de datos en tránsito hacia y desde el centro de gestión.
* Se utiliza el cifrado AES de 256 bits para los datos en tránsito, específicamente los mensajes que fluyen a través del plano de control seguro.
* Se utilizan pares de claves RSA de 2048 bits para los datos en tránsito, concretamente la clave simétrica AES 256 que fluye a través del plano de control seguro.
* Claves RSA proporcionadas por un usuario para firmar configuraciones de despliegue de contenedor al utilizar el mandato **hzn exchange service publish**.
* Par de claves RSA tal como las ha generado el mandato **hzn key create**, si el usuario elige utilizar este mandato. El tamaño de bit de esta clave es 4096 de forma predeterminada, pero el usuario lo puede cambiar.

## Resumen
{: #summary}

{{site.data.keyword.edge_notm}} utiliza hashes, firmas criptográficas y cifrado para garantizar la seguridad frente al acceso no deseado. Al ser principalmente descentralizado, {{site.data.keyword.ieam}} evita exponerse a la mayoría de ataques que normalmente se encuentran en los entornos de computación periférica. Al restringir el ámbito de autoridad de los roles de participante, {{site.data.keyword.ieam}} contiene el daño potencial de un host comprometido o componente de software comprometido en esa parte del sistema. Incluso los ataques externos a gran escala en los servicios centralizados de los servicios de {{site.data.keyword.horizon}} que se utilizan en {{site.data.keyword.ieam}} tienen un impacto mínimo en la ejecución de las cargas de trabajo en la periferia.
