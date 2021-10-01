---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Clústeres periféricos
{: #edge_clusters}

La función de clúster periférico de
{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) le ayuda a gestionar
y desplegar cargas de trabajo de un clúster de centro de gestión
en instancias remotas de OpenShift® Container Platform u otros clústeres basados en Kubernetes. Los
clústeres periféricos son nodos periféricos de {{site.data.keyword.ieam}} que son clústeres de
Kubernetes. Un clúster periférico permite utilizar casos en el borde, que requieren una ubicación compartida
de cálculo con operaciones de negocio o que requieren más escalabilidad, disponibilidad y capacidad de cálculo
de lo que puede soportar un dispositivo periférico. Además, con frecuencia los clústeres periféricos
proporcionan servicios de aplicaciones que son necesarios para soportar los servicios que se ejecutan
en dispositivos periféricos debido a su estrecha proximidad a los dispositivos periféricos. {{site.data.keyword.ieam}} despliega
servicios periféricos en un clúster periférico, a través de un operador de Kubernetes, permitiendo
los mismos mecanismos de despliegue autónomo utilizados con los dispositivos periféricos. La potencia completa
de Kubernetes como plataforma de gestión de contenedores está disponible para los servicios periféricos
desplegados por {{site.data.keyword.ieam}}.

<img src="../../images/edge/05b_Installing_edge_agent_on_cluster.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, agbots y agentes">

En la secciones siguientes se describe cómo instalar un clúster periférico e instalar en él
el agente de {{site.data.keyword.ieam}}.

- [Preparación de un clúster periférico](preparing_edge_cluster.md)
- [Instalación del agente](edge_cluster_agent.md)
{: childlinks}
