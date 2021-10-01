---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visión general
{: #Overview}

Edge Computing sirve para colocar aplicaciones empresariales más cerca del lugar donde se crean los datos.
{:shortdesc}

* [Ventajas de Edge Computing](#edge_benefits)
* [Ejemplos](#examples)
* [Conceptos](#concepts)
  
Edge Computing es un importante paradigma emergente que amplía el modelo operativo virtualizando la nube más allá de un centro de datos o un centro de Cloud Computing. La
computación periférica lleva las cargas de trabajo de aplicación desde una ubicación centralizada hasta ubicaciones remotas, como por ejemplo plantas de fábricas, almacenes, centros de distribución, tiendas, centros de transporte y otras. Básicamente, el cálculo periférico proporciona la capacidad de mover cargas de trabajo de aplicación a cualquier lugar en que sea necesario realizar proceso informático fuera de los centros de datos y del entorno de alojamiento en la nube.

{{site.data.keyword.ieam}} proporciona características de Edge Computing para ayudarle a gestionar y desplegar cargas de trabajo de un clúster de hub en instancias remotas de {{site.data.keyword.open_shift_cp}} u otros clústeres basados en Kubernetes.

{{site.data.keyword.ieam}} también incluye soporte para un {{site.data.keyword.edge_profile}}. Este perfil soportado puede ayudarle a reducir el uso de recursos de {{site.data.keyword.open_shift_cp}} cuando se instala {{site.data.keyword.open_shift_cp}} para utilizarse en el alojamiento de un clúster periférico remoto. Este perfil coloca los servicios mínimos que se necesitan para dar soporte a una gestión remota robusta de estos entornos de servidor y a las aplicaciones críticas de empresa que se alojan allí. Con este perfil, todavía puede autenticar usuarios, recopilar datos de registro y de sucesos y desplegar cargas de trabajo en un único nodo o en un conjunto de nodos de trabajador en clúster.

## Ventajas de Edge Computing
{: #edge_benefits}

* Cambio de valor añadido para la organización: mover cargas de trabajo de aplicación a nodos periféricos para dar soporte a operaciones en ubicaciones remotas en las que se recopilan los datos en lugar de enviar los datos al centro de datos para su proceso.

* Reducir la dependencia del personal de TI: la utilización de {{site.data.keyword.ieam}} puede ayudar a reducir la dependencia del personal de TI. Utilice {{site.data.keyword.ieam}} para desplegar y gestionar cargas de trabajo críticas de clústeres periféricos de forma segura y fiable en cientos de ubicaciones remotas desde una ubicación central. Esta prestación elimina la necesidad de personal de TI a tiempo completo en cada ubicación remota para gestionar las cargas de trabajo en el sitio.

## Ejemplos
{: #examples}

Edge Computing sirve para colocar aplicaciones empresariales más cerca del lugar donde se crean los datos. Por ejemplo, si gestiona una fábrica, el equipo de planta de la fábrica puede incluir sensores para registrar cualquier número de puntos de datos que proporcione detalles sobre cómo está funcionando la planta. Los sensores pueden registrar el número de piezas ensambladas por hora, el tiempo necesario para que un apilador regrese a su posición inicial o la temperatura de funcionamiento de una máquina de fabricación. La información de estos puntos de datos puede ser beneficiosa para ayudarle a determinar si está funcionando a máxima eficiencia, identificar los niveles de calidad que está alcanzando o predecir cuándo es probable que una máquina falle y requiera mantenimiento preventivo.

En otro ejemplo, si tiene trabajadores en ubicaciones remotas cuyo trabajo puede implicar que trabajen en situaciones peligrosas, como entornos calientes o ruidosos, que estén expuestos a gases de escape o de producción o a maquinaria pesada, es posible que tenga que supervisar las condiciones del entorno. Puede recopilar información de varios orígenes que se puede utilizar en las ubicaciones remotas. Los supervisores pueden utilizar estos datos para determinar cuándo indicar a los trabajadores que hagan una pausa, se rehidraten o apaguen el equipo.

En otro ejemplo, puedes usar cámaras de vídeo para supervisar las propiedades, por ejemplo para identificar la afluencia de personas a tiendas, restaurantes o lugares de entretenimiento, a modo de vigilancia de seguridad para registrar actos de vandalismo u otras actividades no deseadas o para reconocer condiciones de emergencia. Si también recopila datos de los vídeos, puede utilizar Edge Computing para procesar la analítica de vídeo localmente para ayudar a sus trabajadores a responder más rápido a las oportunidades y a los incidentes. Los trabajadores de restaurantes pueden estimar mejor la cantidad de alimentos que se deben preparar, los jefes de tienda pueden determinar si abrir más mostradores de venta y el personal de seguridad puede responder más rápidamente a las emergencias o avisar a los servicios de emergencias.

En todos estos casos, el envío de los datos registrados a un centro de Cloud Computing o a un centro de datos puede añadir latencia al proceso de datos. Esta pérdida de tiempo puede tener consecuencias negativas cuando intenta responder a situaciones u oportunidades críticas.

Si los datos registrados son datos que no necesitan ningún proceso especial ni ningún proceso sensible al tiempo, puede incurrir en costes de red y almacenamiento sustanciales por el envío innecesario de estos datos normales.

Por otro lado, si entre los datos recopilados, también hay datos confidenciales, como por ejemplo información personal, aumenta el riesgo de exposición de los datos cada vez que los mueve a otra ubicación distinta de aquella en la que se crearon.

Además, si alguna de las conexiones de red no es fiable, también puede correr el riesgo de interrumpir operaciones críticas.

## Conceptos
{: #concepts}

**dispositivo periférico**: una pieza de equipo, como una máquina de ensamblaje en una fábrica, un cajero automático, una cámara inteligente o un automóvil, que tiene capacidad de cálculo integrada en la que se pueden realizar trabajo significativo y se recopilan o producen datos.

**pasarela periférica**: un clúster periférico que tiene servicios que realizan funciones de red como conversión de protocolos, terminación de red, tunelado, protección de cortafuegos o conexiones inalámbricas. Una pasarela periférica sirve como punto de conexión entre un dispositivo periférico o un clúster periférico y la nube o una red más grande.

**nodo periférico**: cualquier dispositivo periférico, clúster periférico o pasarela periférica donde tiene lugar la computación periférica.

**clúster periférico**: un sistema de una instalación operativa remota que ejecuta cargas de trabajo de aplicación empresarial y servicios compartidos. Un clúster periférico se puede utilizar para conectarse a un dispositivo periférico, conectarse a otro clúster periférico o servir como pasarela periférica para conectar con la nube o con una red más grande.

**servicio periférico**: un servicio diseñado específicamente para desplegarse en un clúster periférico, una pasarela periférica o un dispositivo periférico. El reconocimiento visual, la percepción acústica y el reconocimiento de voz son todos ejemplos de posibles servicios periféricos.

**carga de trabajo periférica**: cualquier servicio, microservicio o fragmento de software que realiza un trabajo significativo cuando se ejecuta en un nodo periférico.

Las redes públicas, privadas y de suministro de contenido se están transformando de simples interconexiones a entornos de alojamiento de valor superior para las aplicaciones en forma de nube de red periférica. Los casos de uso típicos para {{site.data.keyword.ieam}} incluyen:

* Despliegue de nodos periféricos
* Capacidad de operaciones de cálculo de nodos periféricos
* Soporte y optimización de nodos periféricos

{{site.data.keyword.ieam}} unifica las plataformas de nube de varios proveedores en un panel de control coherente desde la instalación local al borde. {{site.data.keyword.ieam}} es una extensión natural que permite la distribución y gestión de cargas de trabajo más allá de la red periférica a los dispositivos y pasarelas periféricos. {{site.data.keyword.ieam}} también reconoce las cargas de trabajo de aplicaciones empresariales con componentes periféricos, entornos de nube privados e híbridos y nube pública; donde {{site.data.keyword.ieam}} proporciona un nuevo entorno de ejecución para que la IA distribuida alcance orígenes de datos críticos.

Además, {{site.data.keyword.ieam}} proporciona herramientas de IA para acelerar el aprendizaje profundo, el reconocimiento visual y de voz y el análisis de vídeo y acústica, lo que permite la inferencia en todas las resoluciones y la mayoría de los formatos de los servicios de conversación de vídeo y audio y el descubrimiento.

## Qué hacer a continuación

- [Requisitos de sistema y dimensionamiento](cluster_sizing.md)
- [Instalación del centro de gestión](hub.md)
