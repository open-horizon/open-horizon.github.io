---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preguntas frecuentes
{: #faqs}

Las siguientes son las respuestas a algunas preguntas más frecuentes (FAQs) sobre {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

  * [¿Hay alguna forma de crear un entorno autónomo para fines de desarrollo?](#one_click)
  * [¿El software {{site.data.keyword.ieam}} es de código abierto?](#open_sourced)
  * [¿Cómo puedo utilizar {{site.data.keyword.ieam}} para desarrollar y desplegar servicios periférico?](#dev_dep)
  * [¿Qué plataformas de hardware de nodo periférico admite {{site.data.keyword.ieam}}?](#hw_plat)
  * [¿Puedo ejecutar cualquier distribución de {{site.data.keyword.linux_notm}} en mis nodos periféricos con {{site.data.keyword.ieam}}?](#lin_dist)
  * [¿Qué lenguajes de programación y entornos admite {{site.data.keyword.ieam}}?](#pro_env)
  * [¿Existe documentación detallada para las API REST proporcionadas por los componentes en {{site.data.keyword.ieam}}?](#rest_doc)
  * [¿{{site.data.keyword.ieam}} utiliza Kubernetes?](#use_kube)
  * [¿{{site.data.keyword.ieam}} utiliza MQTT?](#use_mqtt)
  * [¿Cuánto tiempo transcurre normalmente después de registrar un nodo periférico hasta que se establecen los acuerdos y los contenedores correspondientes empiezan a ejecutarse?](#agree_run)
  * [¿Se puede eliminar el software de {{site.data.keyword.horizon}} y todo el resto de software o datos relacionados con {{site.data.keyword.ieam}} de un host de nodo periférico?](#sw_rem)
  * [¿Hay un panel de control para visualizar los acuerdos y servicios que están activos en un nodo periférico?](#db_node)
  * [¿Qué sucede si una descarga de imagen de contenedor se interrumpe debido a un corte de red?](#image_download)
  * [¿Por qué es seguro {{site.data.keyword.ieam}}?](#ieam_secure)
  * [¿Cómo gestiono la IA en el borde con modelos frente a la IA en la nube?](#ai_cloud)

## ¿Hay alguna forma de crear un entorno autónomo para fines de desarrollo?
{: #one_click}

Puede instalar el centro de gestión de código abierto (sin la consola de gestión de {{site.data.keyword.ieam}}) con el instalador "todo en uno" ("all-in-one") para desarrolladores. El instalador todo en uno crea un centro de gestión completo pero mínimo, no adecuado para el uso en producción. También configura un nodo periférico de ejemplo. Esta herramienta permite que los desarrolladores de componentes de código abierto comiencen a desarrollar rápidamente sin tener que configurar un centro de gestión de {{site.data.keyword.ieam}} de producción completo. Para obtener información sobre el instalador todo en uno, consulte [Open Horizon - Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub).

## ¿El software de {{site.data.keyword.ieam}} es de código abierto?
{: #open_sourced}

{{site.data.keyword.ieam}} es un producto de IBM. Pero los componentes principales utilizan mucho el proyecto de código abierto de [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). Muchos de los programas de muestra y de ejemplo que están disponibles en el proyecto {{site.data.keyword.horizon}} funcionan con {{site.data.keyword.ieam}}. Para obtener más información sobre el proyecto, consulte [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## ¿Cómo puedo desarrollar y desplegar servicios periféricos con {{site.data.keyword.ieam}}?
{: #dev_dep}

Consulte [Utilización de servicios periféricos](../using_edge_services/using_edge_services.md).

## ¿Qué plataformas de hardware de nodo periférico admite {{site.data.keyword.ieam}}?
{: #hw_plat}

{{site.data.keyword.ieam}} admite diferentes arquitecturas de hardware a través del paquete binario {{site.data.keyword.linux_notm}} de Debian para {{site.data.keyword.horizon}} o mediante contenedores de Docker. Para obtener más información, consulte [Instalación del software de {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## ¿Puedo ejecutar cualquier distribución de {{site.data.keyword.linux_notm}} en mis nodos periféricos con {{site.data.keyword.ieam}}?
{: #lin_dist}

Sí y no.

Puede desarrollar software periférico que utilice cualquier distribución de {{site.data.keyword.linux_notm}} como imagen base de los contenedores de Docker (si utiliza la sentencia Dockerfile `FROM`) si esa base funciona en el kernel de {{site.data.keyword.linux_notm}} de host en los nodos periféricos. Esto significa que puede utilizar para los contenedores cualquier distribución que Docker pueda ejecutar en los hosts periféricos.

Sin embargo, el sistema operativo de host de nodo periférico debe poder ejecutar una versión reciente de Docker y poder ejecutar el software {{site.data.keyword.horizon}}. Actualmente, el software {{site.data.keyword.horizon}} solo se proporciona como paquetes Debian y RPM para nodos periféricos que ejecutan {{site.data.keyword.linux_notm}}. Para las máquinas Apple Macintosh, se proporciona una versión de contenedor Docker. El equipo de desarrollo de {{site.data.keyword.horizon}} utiliza principalmente Apple Macintosh, o las distribuciones de {{site.data.keyword.linux_notm}} Ubuntu o Raspbian.

Además, se ha probado la instalación de paquete RPM en los nodos periféricos configurados con Red Hat Enterprise Linux (RHEL) Versión 8.2.

## ¿Qué lenguajes de programación y entornos admite {{site.data.keyword.ieam}}?
{: #pro_env}

{{site.data.keyword.ieam}} admite casi cualquier lenguaje de programación y biblioteca de software que pueda configurar para ejecutarlos en un contenedor de Docker adecuado de los nodos periféricos.

Si su software requiere acceso a hardware o a servicios de sistema operativo específicos, es posible que tenga que especificar argumentos equivalentes a `docker run` para dar soporte a dicho acceso. Puede especificar argumentos soportados dentro de la sección `deployment` del archivo de definición del contenedor de Docker.

## ¿Existe documentación detallada para las API REST proporcionadas por los componentes de {{site.data.keyword.ieam}}?
{: #rest_doc}

Sí. Para obtener más información, consulte las [API de {{site.data.keyword.ieam}}](../api/edge_rest_apis.md). 

## ¿{{site.data.keyword.ieam}} utiliza Kubernetes?
{: #use_kube}

Sí. {{site.data.keyword.ieam}} utiliza servicios Kubernetes de [{{site.data.keyword.open_shift_cp}}](https://docs.openshift.com/container-platform/4.6/welcome/index.md).

## ¿{{site.data.keyword.ieam}} utiliza MQTT?
{: #use_mqtt}

{{site.data.keyword.ieam}} no utiliza Message Queuing Telemetry Transport (MQTT) para soportar sus propias funciones internas; sin embargo, los programas que despliega en los nodos periféricos pueden utilizar MQTT para sus propios fines. Hay programas de ejemplo disponibles que utilizan MQTT y otras tecnologías (por ejemplo, {{site.data.keyword.message_hub_notm}}, basado en Apache Kafka) para transportar datos hacia los nodos periféricos y desde dichos nodos.

## ¿Cuánto tiempo transcurre normalmente después de registrar el nodo periférico hasta que se establecen los acuerdos y los contenedores correspondientes empiezan a ejecutarse?
{: #agree_run}

Normalmente, solo son necesarios unos segundos después del registro para el agente y un agbot remoto para finalizar un acuerdo para desplegar software. Después de eso, el agente de {{site.data.keyword.horizon}} descarga (`docker pull`) los contenedores en el nodo periférico, verifica las firmas criptográficas con {{site.data.keyword.horizon_exchange}} y los ejecuta. En función de los tamaños de los contenedores y del tiempo que tarden en iniciarse y estar funcionales, pueden transcurrir sólo unos pocos segundos o muchos minutos antes de que el nodo periférico esté completamente operativo.

Después de haber registrado un nodo periférico, puede ejecutar el mandato `hzn node list` para ver el estado de {{site.data.keyword.horizon}} en el nodo periférico. Cuando el mandato `hzn node list` muestra que el estado es `configurado`, los agbots de {{site.data.keyword.horizon}} pueden descubrir el nodo periférico y empezar a establecer acuerdos.

Para observar las fases del proceso de negociación del acuerdo, puede utilizar el mandato `hzn agreement list` .

Una vez finalizada una lista de acuerdos, puede utilizar el mandato `docker ps` para ver los contenedores en ejecución. También puede emitir `docker inspect <container>` para ver información más detallada acerca del despliegue de cualquier `<container>` específico.

## ¿Se pueden eliminar el software de {{site.data.keyword.horizon}} y todo el resto de software o datos relacionados con {{site.data.keyword.ieam}} de un host de nodo periférico?
{: #sw_rem}

Sí. Si el nodo periférico está registrado, anule el registro del nodo periférico ejecutando: 
```
hzn unregister -f -r
```
{: codeblock}

Cuando se ha eliminado el registro del nodo periférico, puede eliminar el software {{site.data.keyword.horizon}} instalado, por ejemplo para la ejecución de sistemas basados en Debian:
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## ¿Hay un panel de control para visualizar los acuerdos y servicios que están activos en un nodo periférico?
{: #db_node}

Puede utilizar la interfaz de usuario web de {{site.data.keyword.ieam}} para observar los nodos y servicios periféricos.

Además, puede utilizar el mandato `hzn` para obtener información sobre los acuerdos y servicios activos utilizando la API REST de agente de {{site.data.keyword.horizon}} local en el nodo periférico. Ejecute los mandatos siguientes para utilizar la API para recuperar la información relacionada:

```
hzn node list hzn agreement list docker ps
```
{: codeblock}

## ¿Qué sucede si una descarga de imagen de contenedor se interrumpe debido a un corte de red?
{: #image_download}

La API de Docker se utiliza para descargar imágenes de contenedor. Si la API de Docker termina la descarga, devuelve un error al agente. A su vez, el agente cancela el intento de despliegue actual. Cuando el Agbot detecta la cancelación, inicia un nuevo intento de despliegue con el agente. Durante el siguiente intento de despliegue, la API de Docker reanuda la descarga desde el lugar donde se ha dejado. Este proceso continúa hasta que la imagen se ha descargado por completo y el despliegue puede continuar. La API de enlace de Docker es responsable de la extracción de imagen y, en caso de anomalía, se cancela el acuerdo.

## ¿Por qué es seguro {{site.data.keyword.ieam}}?
{: #ieam_secure}

* {{site.data.keyword.ieam}} automatiza y utiliza la autenticación de clave pública-privada firmada criptográficamente de los dispositivos periféricos mientras se comunica con el centro de gestión de {{site.data.keyword.ieam}} durante el suministro. La comunicación siempre la inicia y la controla el nodo periférico. 
* El sistema tiene credenciales de nodo y servicio.
* Verificación y autenticidad de software utilizando la verificación de hash.

Consulte [Seguridad en la periferia](https://www.ibm.com/cloud/blog/security-at-the-edge).

## ¿Cómo gestiono la IA en el borde con modelos frente a la IA en la nube?
{: #ai_cloud}

Normalmente, la IA en la periferia le permite realizar la inferencia de máquina inmediata con latencia subsecundaria, lo que permite la respuesta en tiempo real basándose en el caso de uso y el hardware (por ejemplo, RaspberryPi, Intel x86 y Nvidia Jetson Nano). El sistema de gestión de modelos de {{site.data.keyword.ieam}} le permite desplegar modelos de IA actualizados sin tiempo de inactividad de servicio.

Consulte [Modelos desplegados en la periferia](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
