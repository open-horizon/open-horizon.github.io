---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Desarrollo de un servicio periférico para clústeres
{: #developing_clusters}

La función de clúster periférico {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) le proporciona características de de computación periférica para ayudarle a gestionar y desplegar cargas de trabajo de un clúster de centro de gestión en instancias remotas de OpenShift® Container Platform u otros clústeres basados en Kubernetes. Los clústeres periféricos son nodos periféricos de {{site.data.keyword.ieam}} que son clústeres de Kubernetes. Un clúster periférico permite utilizar casos en la periferia, que requieren una ubicación compartida de cálculo con operaciones de negocio o que requieren más escalabilidad, disponibilidad y capacidad de cálculo de lo que puede soportar un dispositivo periférico. Además, con frecuencia los clústeres periféricos proporcionan servicios de aplicación que son necesarios para soportar servicios que se ejecutan en dispositivos periféricos debido a su estrecha proximidad con los dispositivos periféricos, produciendo una aplicación periférica multinivel. {{site.data.keyword.ieam}} despliega servicios periféricos en un clúster periférico a través de un operador de Kubernetes, permitiendo los mismos mecanismos de despliegue autónomos utilizados con los dispositivos periféricos. La potencia completa de Kubernetes como plataforma de gestión de contenedores está disponible para los servicios periféricos desplegados por {{site.data.keyword.ieam}}.

<img src="../OH/docs/images/edge/03b_Developing_edge_service_for_cluster.svg" style="margin: 3%" alt="Developing an edge service for clusters">

* [Desarrollo de un operador de Kubernetes](service_operators.md)
* [Creación de su propio hello world para clústeres](creating_hello_world.md)
