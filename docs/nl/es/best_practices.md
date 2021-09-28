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

# Procedimientos recomendados de desarrollo nativo de Edge
{: #edge_native_practices}

Creará cargas de trabajo que funcionarán en la periferia, en centros de cálculo existentes más allá de los confines normales de su centro de datos de TI o entorno de nube. Esto significa que debe tener en cuenta las condiciones exclusivas de esos entornos. Esto se conoce como el modelo de programación nativo de Edge.

## Procedimientos recomendados para desarrollar servicios periféricos
{: #best_practices}

Los métodos recomendados y las directrices siguientes le ayudan a diseñar y desarrollar servicios periféricos para utilizarlos con {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}).
{:shortdesc}

La automatización de la ejecución de servicios en la periferia es diferente de la automatización de servicios en la nube de las formas siguientes:

* El número de nodos periféricos puede ser mucho mayor.
* Las redes con nodos periféricos pueden no ser fiables y ser mucho más lentas. Los nodos periféricos están a menudo detrás de cortafuegos, por lo que las conexiones normalmente no se pueden iniciar desde la nube hasta los nodos periféricos.
* Los nodos Edge están restringidos a los recursos.
* Una fuerza motriz detrás de las cargas de trabajo que funcionan en la periferia es la capacidad de reducir la latencia y optimizar el ancho de banda de la red. Esto convierte en un factor importante la colocación de cargas de trabajo en relación con dónde se generan los datos. 
* Por regla general, los nodos periféricos están en ubicaciones remotas y no son configurados por el personal de operaciones. Una vez que se ha configurado un nodo periférico, es posible que el personal no esté disponible para administrar el nodo.
* Los nodos periféricos también son normalmente entornos menos de confianza que los servidores de nube.

Estas diferencias requieren técnicas diferentes para desplegar y gestionar software en los nodos periféricos. {{site.data.keyword.edge_abbr}} está diseñado para la gestión de nodos periféricos. Al crear servicios, siga las directrices siguientes para asegurarse de que los servicios se han diseñado para trabajar con nodos periféricos.

## Directrices para el desarrollo de servicios
{: #service_guidelines}


* **Modelo de programación nativo de Cloud:** el modelo de programación nativo de Edge hereda muchos principios del modelo de programación nativo de Cloud, incluido lo siguiente:

  * Repartir las cargas de trabajo en componentes y en contenedores, construir las aplicaciones alrededor de un conjunto de microservicios, cada uno empaquetado en grupos relacionados lógicamente, pero equilibrar esa agrupación para reconocer dónde pueden funcionar mejor los diferentes contenedores en niveles o nodos periféricos diferentes.
  * Exponer las API a los microservicios que permiten a otros componentes de la aplicación encontrar los servicios de los que dependen.
  * Diseñar un acoplamiento dinámico entre los microservicios para que puedan funcionar de forma independiente entre sí y para evitar supuestos con estado que impongan afinidades entre servicios que de otro modo socavarían el escalado elástico, la migración tras error y la recuperación.
  * Ejercer la integración continua y el despliegue continuo (CI/CD) junto con las prácticas de desarrollo de Agile dentro de un marco de DevOps.
  * Tenga en cuenta los recursos siguientes para obtener más información sobre las prácticas de programación nativas de Cloud:
    * [10 KEY ATTRIBUTES OF CLOUD-NATIVE APPLICATIONS](https://thenewstack.io/10-key-attributes-of-cloud-native-applications/)
    * [Cloud Native Programming](https://researcher.watson.ibm.com/researcher/view_group.php?id=9957)
    *	[Understanding cloud-native applications](https://www.redhat.com/en/topics/cloud-native-apps)

* **Disponibilidad de servicio:** si el contenedor de servicios requiere y utiliza otros contenedores de servicios, el servicio debe ser tolerante cuando estos servicios están ausentes en algunas situaciones. Por ejemplo, cuando los contenedores se inician inicialmente, e incluso cuando se inician desde el final del gráfico de dependencias, al moverse en dirección ascendente, algunos servicios se pueden iniciar más rápidamente que otros. En esta situación, los contenedores de servicios deben reintentar mientras esperan a que las dependencias sean plenamente funcionales. De forma similar, si un contenedor de servicios dependiente se actualiza automáticamente, se reinicia. Es recomendable que los servicios sean siempre tolerantes con las interrupciones en los servicios de los que dependen.
* **Portabilidad:** el mundo de Edge Computing abarca varios niveles del sistema, incluidos los dispositivos periféricos, los clústeres periféricos y las ubicaciones periféricas de red o de metro. Dónde se coloque la carga de trabajo periférica contenerizada dependerá de una combinación de factores, incluidos la dependencia correspondiente de ciertos recursos, como por ejemplo datos de sensor y sensor y los métodos de acceso, los requisitos de latencia final y la capacidad de cálculo disponible. Debe diseñar la carga de trabajo para tolerar que se coloque en diferentes niveles del sistema según las necesidades del contexto en el que se utilizará la aplicación.
* **Orquestación de contenedores:** más allá del punto anterior sobre la portabilidad de varios niveles; normalmente los dispositivos periféricos funcionan con el tiempo de ejecución de Docker nativo, sin orquestación de contenedores local. Los clústeres periféricos y los periféricos de red/metro se configurarán con Kubernetes para orquestar la carga de trabajo frente a las demandas de recursos en competición compartidas. Debe implementar el contenedor para evitar cualquier dependencia explícita de Docker o Kubernetes para permitir su portabilidad a diferentes niveles del mundo de Edge Computing distribuido. 
* **Externalizar parámetros de configuración:** utilice el soporte incorporado proporcionado por {{site.data.keyword.ieam}} para externalizar las variables de configuración y las dependencias de recurso para que éstas se puedan proporcionar y actualizar a valores que sean específicos del nodo en el que se despliega el contenedor.
* **Secretos seguros:** los servicios periféricos a menudo requieren la integración con servicios locales o basados en la nube, que requieren credenciales de autenticación. Explote el [gestor de secretos](secrets_details.md) para desplegar de forma segura información confidencial en los nodos periféricos.
* **Consideraciones sobre el tamaño:** los contenedores de servicios deben ser lo más pequeños posible para que los servicios se puedan desplegar en redes potencialmente lentas o en dispositivos periféricos pequeños. Para ayudarle a desarrollar contenedores de servicios más pequeños, utilice las técnicas siguientes:

  * Utilice lenguajes de programación que pueden ayudarle a crear servicios más pequeños:
    * Los mejores: go, rust, c, sh
    * Correctos: c++, python, bash
    * A tener en cuenta: nodejs, Java y lenguajes basados en JVM, como por ejemplo scala
  * Utilice técnicas que pueden ayudarle a construir imágenes de Docker más pequeñas:
    * Utilice Alpine como la imagen base de {{site.data.keyword.linux_notm}}.
    * Para instalar paquetes en una imagen basada en Alpine, utilice el mandato `apk -- no-cache -- update add` para evitar almacenar la memoria caché de paquete, que no es necesaria para el tiempo de ejecución.
    * Suprima los archivos de la misma capa de Dockerfile (mandato) donde se añaden los archivos. Si utiliza una línea de mandatos Dockerfile separada para suprimir los archivos de la imagen, puede aumentar el tamaño de la imagen del contenedor. Por ejemplo, puede utilizar `&&` para agrupar los mandatos para descargar, utilizar y, a continuación, suprimir archivos, todo dentro de un único mandato de Dockerfile `RUN` .
    * No incluya herramientas de compilación en la imagen de Docker de tiempo de ejecución. Como procedimiento recomendado, utilice una [compilación de varias etapas Docker](https://docs.docker.com/develop/develop-images/multistage-build/) para crear artefactos de tiempo de ejecución. A continuación, copie de forma selectiva los artefactos de tiempo de ejecución necesarios como, por ejemplo, los componentes ejecutables, en la imagen Docker del tiempo de ejecución.
* **Conservar los servicios autocontenidos** puesto que un servicio debe enviarse a través de una red a nodos periféricos y se inicia automáticamente, el contenedor de servicios debe incluir todos aquello de lo que depende el servicio. Debe empaquetar estos activos, como por ejemplo todos los certificados necesarios, en el contenedor. No cuente con la disponibilidad de los administradores para completar tareas para añadir activos necesarios al nodo periférico para que un servicio se ejecute satisfactoriamente.
* **Privacidad de datos:** cada vez que se mueven datos privados y confidenciales alrededor de la red, se aumenta la vulnerabilidad de esos datos a los ataques y a la exposición. Edge Computing ofrece, como una de sus principales ventajas, la oportunidad de conservar esos datos allí donde se crean. Respeta esa oportunidad en su contenedor protegiéndolo. Lo ideal es no pasar esos datos a otros servicios. Si es absolutamente necesario pasar datos a otros servicios o niveles del sistema, intente eliminar la información de identificación personal (PII), la información personal sobre la salud (PHI) o la información personal financiera (PFI) a través de técnicas de ofuscación o eliminación de la identificación o cifrándola con una clave cuya propiedad esté enteramente dentro de los confines de su servicio. 
* **Diseñar y configurar para la automatización:** los nodos periféricos, y los servicios que se ejecutan en los nodos, deben estar tan cerca de las operaciones cero como sea posible. {{site.data.keyword.ieam}} automatiza el despliegue la y gestión de servicios, pero los servicios deben estar estructurados para permitir que {{site.data.keyword.ieam}} pueda automatizar estos procesos sin intervención humana. Para facilitar el diseño de automatización, siga las directrices siguientes:
  * Limite el número de variables de entrada de usuario para un servicio. Cualquier variable UserInput sin valores predeterminados en la definición de servicio requiere que los valores se especifiquen para cada nodo periférico. Limite el número de variables o evite los servicios que utilizan variables, siempre que sea posible.  
  * Si un servicio requiere muchos valores configurables, utilice un archivo de configuración para definir las variables. Incluya una versión predeterminada del archivo de configuración dentro del contenedor de servicios. A continuación, utilice el sistema de gestión de modelos {{site.data.keyword.ieam}} para permitir al administrador proporcionar su propio archivo de configuración y actualizarlo con el paso del tiempo.
  * **Optimizar los servicios de plataforma estándar:** muchas de las necesidades de su aplicación se pueden cubrir mediante servicios de plataforma preimplementados. En lugar de crear estas prestaciones desde cero en su aplicación, considere la posibilidad de utilizar lo que ya está creado y disponible. Una fuente de tales servicios de plataforma es IBM Cloud Pak, que cubre un amplio abanico de prestaciones, muchas de las cuales se han construido siguiendo procedimientos de programación nativos de Cloud, como por ejemplo:
    * **Gestión de datos:** tenga en cuenta IBM Cloud Pak for Data para sus requisitos de base de datos de almacenamiento de objetos y bloques SQL y no SQL, servicios de inteligencia artificial y aprendizaje automático y necesidades de lago de datos. 
    * **Seguridad:** tome en consideración IBM CloudPak for Security para sus necesidades de cifrado, exploración de código y detección de intrusiones.
    * **Aplicaciones:** tome en consideración IBM Cloud Pak for Applications para sus necesidades de aplicación web, sin servidor y marco de aplicaciones.
