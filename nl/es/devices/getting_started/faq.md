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

Obtenga respuestas a algunas de las preguntas más frecuentes (FAQs) sobre {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

  * [¿El software {{site.data.keyword.edge_devices_notm}} es de código abierto?](#open_sourced)
  * [¿Cómo puede desarrollar y desplegar servicios periféricos utilizando {{site.data.keyword.edge_devices_notm}}?](#dev_dep)
  * [¿Qué plataformas de hardware de nodo periférico admite {{site.data.keyword.edge_devices_notm}}?](#hw_plat)
  * [¿Puedo ejecutar cualquier distribución de {{site.data.keyword.linux_notm}} en mis nodos periféricos con {{site.data.keyword.edge_devices_notm}}?](#lin_dist)
  * [¿Qué lenguajes de programación y entornos admite {{site.data.keyword.edge_devices_notm}}?](#pro_env)
  * [¿Existe documentación detallada para las API REST proporcionadas por los componentes en {{site.data.keyword.edge_devices_notm}}?](#rest_doc)
  * [¿{{site.data.keyword.edge_devices_notm}} utiliza Kubernetes?](#use_kube)
  * [¿{{site.data.keyword.edge_devices_notm}} utiliza MQTT??](#use_mqtt)
  * [¿Cuánto tiempo transcurre normalmente después de registrar el nodo periférico hasta que se establecen los acuerdos y los contenedores correspondientes empiezan a ejecutarse?](#agree_run)
  * [¿Se puede eliminar el software de {{site.data.keyword.horizon}} y todo el resto de software o datos relacionados con {{site.data.keyword.edge_devices_notm}} de un host de nodo periférico?](#sw_rem)
  * [¿Hay un panel de control para visualizar los acuerdos y servicios que están activos en un nodo periférico?](#db_node)
  * [¿Qué sucede si una descarga de imagen de contenedor se interrumpe debido a un corte de red?](#image_download)
  * [¿Por qué IEAM es seguro?](#ieam_secure)
  * [¿Cómo gestiono la IA en el borde con modelos frente a la IA en la nube?](#ai_cloud)

## ¿El software de {{site.data.keyword.edge_devices_notm}} es de código abierto?
{: #open_sourced}

{{site.data.keyword.edge_devices_notm}} es un producto de IBM. Pero los componentes principales utilizan
mucho el proyecto de código abierto de
[Open Horizon - EdgeX Project Group
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). Muchos de los programas de muestra y de ejemplo que están disponibles en el proyecto {{site.data.keyword.horizon}} funcionan con {{site.data.keyword.edge_devices_notm}}. Para
obtener más información sobre el proyecto, consulte
[Open Horizon - EdgeX Project Group ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Seabre en otro separador")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).


## ¿Cómo puedo desarrollar y desplegar servicios periféricos utilizando {{site.data.keyword.edge_devices_notm}}?
{: #dev_dep}

Consulte [Utilización de servicios periféricos](../developing/using_edge_services.md).

## ¿Qué plataformas de hardware de nodo periférico admite {{site.data.keyword.edge_devices_notm}}?
{: #hw_plat}

{{site.data.keyword.edge_devices_notm}} admite diferentes arquitecturas de hardware a través del paquete binario {{site.data.keyword.linux_notm}} de Debian para {{site.data.keyword.horizon}} o mediante contenedores de Docker. Para
obtener más información, consulte [Instalación del software
de {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## ¿Puedo ejecutar cualquier distribución de {{site.data.keyword.linux_notm}} en mis nodos periféricos con {{site.data.keyword.edge_devices_notm}}?
{: #lin_dist}

Sí y no.

Puede desarrollar software periférico que utilice cualquier distribución de {{site.data.keyword.linux_notm}} como imagen base de los contenedores de Docker (si utiliza la sentencia Dockerfile `FROM`) si esa base funciona en el kernel {{site.data.keyword.linux_notm}} del host en las máquinas perimetrales. Esto significa que puede utilizar para los contenedores cualquier distribución que Docker pueda ejecutar en los hosts periféricos.

Sin embargo, el sistema operativo de host de la máquina perimetral debe poder ejecutar una versión reciente de Docker y poder ejecutar el software {{site.data.keyword.horizon}}. Actualmente, el software {{site.data.keyword.horizon}} se proporciona sólo como un paquete Debian para máquinas perimetrales que ejecutan {{site.data.keyword.linux_notm}}. Para las máquinas Apple Macintosh, se proporciona una versión de contenedor Docker. El equipo de desarrollo de {{site.data.keyword.horizon}} utiliza principalmente Apple Macintosh, o las distribuciones de {{site.data.keyword.linux_notm}} Ubuntu o Raspbian.

## ¿Qué lenguajes de programación y entornos admite {{site.data.keyword.edge_devices_notm}}?
{: #pro_env}

{{site.data.keyword.edge_devices_notm}} admite casi cualquier lenguaje de programación y biblioteca de software que pueda configurar para ejecutarlos en un contenedor de Docker adecuado de los nodos periféricos.

Si su software requiere acceso a hardware o a servicios de sistema operativo específicos, es posible que tenga que especificar argumentos equivalentes a `docker run` para dar soporte a dicho acceso. Puede especificar argumentos soportados dentro de la sección `deployment` del archivo de definición del contenedor de Docker.

## ¿Existe documentación detallada para las API REST proporcionadas por los componentes de {{site.data.keyword.edge_devices_notm}}?
{: #rest_doc}

Sí. Para obtener más información, consulte [API de {{site.data.keyword.edge_devices_notm}}](../installing/edge_rest_apis.md). 

## ¿{{site.data.keyword.edge_devices_notm}} utiliza Kubernetes?
{: #use_kube}

Sí. {{site.data.keyword.edge_devices_notm}} utiliza servicios de Kubernetes de [{{site.data.keyword.open_shift_cp}} ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

## ¿{{site.data.keyword.edge_devices_notm}} utiliza MQTT?
{: #use_mqtt}

{{site.data.keyword.edge_devices_notm}} no utiliza Message Queuing Telemetry Transport (MQTT) para dar soporte a sus propias funciones internas; sin embargo, los programas que despliegue en las máquinas perimetrales son libres de utilizar MQTT para sus propios fines. Hay
programas de ejemplo disponibles que utilizan MQTT y otras tecnologías (por ejemplo,
{{site.data.keyword.message_hub_notm}}, basándose en Apache Kafka) para transportar datos a y desde
máquinas perimetrales.

## ¿Cuánto tiempo transcurre normalmente después de registrar el nodo periférico hasta que se establecen los acuerdos y los contenedores correspondientes empiezan a ejecutarse?
{: #agree_run}

Normalmente, solo son necesarios unos segundos después del registro para el agente y un agbot remoto para finalizar un acuerdo para desplegar software. Después de eso, el agente de {{site.data.keyword.horizon}} descarga (`docker pull`) los contenedores en la máquina perimetral, verifica sus firmas criptográficas con {{site.data.keyword.horizon_exchange}} y los ejecuta. Dependiendo de los tamaños de los contenedores y del tiempo que tardarán en arrancar y funcionar, pueden ser necesarios sólo unos pocos segundos o muchos minutos para que la máquina perimetral esté completamente operativa.

Tras registrar una máquina perimetral, puede ejecutar el mandato `hzn node list` para ver el estado de {{site.data.keyword.horizon}} en la máquina perimetral. Cuando el mandato `hzn node list` muestra que el estado es `configured`, los agbots de {{site.data.keyword.horizon}} son capaces de descubrir la máquina perimetral e iniciar el establecimiento de acuerdos.

Para observar las fases del proceso de negociación del acuerdo, puede utilizar el mandato `hzn agreement list` .

Una vez finalizada una lista de acuerdos, puede utilizar el mandato `docker ps` para ver los contenedores en ejecución. También puede emitir `docker inspect <container>` para ver información más detallada acerca del despliegue de cualquier `<container>` específico.

## ¿Se pueden eliminar el software de {{site.data.keyword.horizon}} y todo el resto de software o datos relacionados con {{site.data.keyword.edge_devices_notm}} de un host de nodo periférico?
{: #sw_rem}

Sí. Si la máquina perimetral está registrada, anule el registro de la máquina perimetral ejecutando: 
```
hzn unregister -f -r
```
{: codeblock}

Una vez anulado el registro de la máquina perimetral, elimine el software {{site.data.keyword.horizon}} instalado:
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## ¿Hay un panel de control para visualizar los acuerdos y servicios que están activos en un nodo periférico?
{: #db_node}

Puede utilizar la interfaz de usuario web de {{site.data.keyword.edge_devices_notm}}
para observar los nodos y servicios periféricos. 

Además, puede utilizar el mandato `hzn` para obtener información sobre los acuerdos y servicios
activos utilizando la API REST de agente de {{site.data.keyword.horizon}} local en el nodo periférico. Ejecute los mandatos siguientes para utilizar la API para recuperar la información relacionada:
```
hzn node list
hzn agreement list
docker ps
```
{: codeblock}

## ¿Qué sucede si una descarga de imagen de contenedor se interrumpe debido a un corte de red?
{: #image_download}

La API de Docker se utiliza para descargar imágenes de contenedor. Si la API de Docker termina
la descarga, devuelve un error al agente. A su vez, el agente cancela el intento de despliegue actual. Cuando
el Agbot detecta la cancelación, inicia un nuevo intento de despliegue con el agente. Durante el siguiente
intento de despliegue, la API de Docker reanuda la descarga desde el lugar donde se ha dejado. Este proceso
continúa hasta que la imagen se ha descargado por completo y el despliegue puede continuar. La API de
enlace de Docker es responsable de la extracción de imagen y, en caso de anomalía, el acuerdo se cancela.

## ¿Por qué IEAM es seguro?
{: #ieam_secure}

* {{site.data.keyword.ieam}} automatiza y utiliza la autenticación de clave pública-privada
firmada criptográficamente de los dispositivos periféricos mientras se comunica con el centro de gestión de
{{site.data.keyword.ieam}} durante el suministro. La comunicación siempre la inicia y la controla
el dispositivo periférico. 
* El sistema tiene credenciales de nodo y servicio.
* Verificación y autenticidad de software utilizando la verificación de hash.

Consulte [Seguridad en el borde
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/blog/security-at-the-edge).

## ¿Cómo gestiono la IA en el borde con modelos frente a la IA en la nube?
{: #ai_cloud}

Normalmente, la IA en el borde le permite realizar la inferencia de máquina en el acto con
latencia subsecundaria, lo que permite la respuesta en tiempo real basándose en el caso de uso
y el hardware (por ejemplo, RaspberryPi, Intel x86 y Nvidia Jetson Nano). El sistema de gestión de modelos de
{{site.data.keyword.ieam}} le permite desplegar modelos de IA actualizados sin
tiempo de inactividad de servicio. 

Consulte [Modelos desplegados en
el borde ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
