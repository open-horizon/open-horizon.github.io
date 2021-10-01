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

# Visión general de servicio periférico para clústeres
{: #edge_clusters_overview}

La función de clúster periférico {{site.data.keyword.edge_notm}}
({{site.data.keyword.ieam}}) le proporciona características de computación periférica
para ayudarle a gestionar y desplegar las cargas de trabajo de un clúster de hub en
instancias remotas de OpenShift® Container Platform 4.2 u otros clústeres basados en Kubernetes. Los
clústeres periféricos son nodos periféricos de {{site.data.keyword.ieam}}
que se despliegan como clústeres de Kubernetes. Un clúster periférico permite casos de uso
en el borde que necesitan la ubicación conjunta del cálculo con operaciones de negocio
o que necesitan más escalabilidad y capacidad de cálculo de lo que puede soportar un
dispositivo periférico. Además, es frecuente que los clústeres periféricos proporcionen servicios de aplicación
necesarios para soportar servicios que se ejecutan en un dispositivo periférico
debido a su estrecha proximidad a los dispositivos periféricos. IEAM despliega servicios periféricos en un
clúster periférico, a través de un operador Kubernetes, habilitando los mismos mecanismos de despliegue
autónomos utilizados con los dispositivos periféricos. La potencia completa
de Kubernetes como plataforma de gestión de contenedores está disponible para los servicios periféricos
desplegados por {{site.data.keyword.ieam}}.

Opcionalmente se puede utilizar IBM Cloud Pak for Multicloud Management para proporcionar un nivel más
profundo de gestión específica de Kubernetes de clústeres periféricos, incluso para
los servicios periféricos desplegados por IEAM.

Añada un gráfico que muestre los pasos de instalación y configuración de alto nivel de clúster periférico. 

## Qué hacer a continuación

Consulte [Clústeres periféricos](../developing/edge_clusters.md) para obtener
información de instalación de clúster periférico.

## Información relacionada

* [Instalación de nodos periféricos](installing_edge_nodes.md)
* [Dispositivos periféricos](../developing/edge_devices.md)
* [Clústeres periféricos](../developing/edge_clusters.md)
