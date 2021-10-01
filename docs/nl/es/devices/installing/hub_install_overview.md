---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visión general de centro de gestión
{: #hub_install_overview}
 
Debe instalar y configurar un centro de gestión antes de pasar a las tareas de nodo de
IBM Edge Application Manager (IEAM).

IEAM proporciona características de computación periférica para ayudarle a gestionar y desplegar
las cargas de trabajo de un clúster de hub en instancias remotas de OpenShift® Container Platform 4.3 u
otros clústeres basados en Kubernetes.

IEAM utiliza IBM Multicloud Management Core 1.2 para controlar el despliegue de cargas de trabajo contenerizadas
en los servidores periféricos, las pasarelas y los dispositivos alojados por clústeres de
OpenShift® Container Platform 4.3 en ubicaciones remotas.

Además, IEAM incluye soporte para un perfil de gestor de computación periférica. Este perfil soportado
puede ayudarle a reducir el uso de recursos de OpenShift® Container Platform 4.3 cuando se instala
OpenShift® Container Platform 4.3 para utilizarlo en el alojamiento de un servidor periférico
remoto. Este perfil coloca los servicios mínimos que se necesitan para dar soporte a una gestión remota robusta de estos entornos de servidor y a las aplicaciones críticas de empresa que se alojan allí. Con este perfil, todavía puede autenticar usuarios, recopilar datos de registro y de sucesos y desplegar cargas de trabajo en un único nodo o en un conjunto de nodos de trabajador en clúster.

Añada un gráfico que muestre los pasos de instalación y configuración de alto nivel de hub 

## Qué hacer a continuación

Consulte [Instalación del centro de gestión](install.md) para obtener instrucciones de
instalación de centro de gestión.

## Información relacionada

* [Instalación de nodos periféricos](installing_edge_nodes.md)
* [Clústeres periféricos](../developing/edge_clusters.md)
* [Dispositivos periféricos](../developing/edge_devices.md)
