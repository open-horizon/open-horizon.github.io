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

# Edge-Cluster
{: #edge_clusters}

Die Edge-Cluster-Funktion von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) unterstützt Sie bei der Verwaltung und Bereitstellung von Workloads über einen Management-Hub-Cluster in fernen Instanzen von OpenShift® Container Platform oder anderen Kubernetes-basierten Clustern. Edge-Cluster sind {{site.data.keyword.ieam}}-Edge-Knoten, die als Kubernetes-Cluster dienen. Ein Edge-Cluster ermöglicht Anwendungsfälle beim Edge-Computing, die eine Zusammenstellung von Rechen- und Geschäftsoperationen erforderlich machen oder eine umfangreichere Skalierungs-, Verfügbarkeits- und Rechenfunktionalität benötigen, als von einer Edge-Einheit unterstützt werden kann. Außerdem werden Edge-Cluster aufgrund ihrer räumlichen Nähe zu Edge-Einheiten teilweise auch dazu eingesetzt, Anwendungsservices bereitstellen, die zur Unterstützung von auf Edge-Einheiten ausgeführten Services benötigt werden. {{site.data.keyword.ieam}} stellt Edge-Services über einen Kubernetes-Operator in einem Edge-Cluster bereit, was denselben autonomen Bereitstellungsmechanismus wie bei Edge-Einheiten ermöglicht. Für Edge-Services, die durch {{site.data.keyword.ieam}} bereitgestellt werden, ist die volle Leistungsstärke von Kubernetes als Container-Management-Plattform verfügbar.

<img src="../OH/docs/images/edge/05b_Installing_edge_agent_on_cluster.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}, agbots and agents">

In den folgenden Abschnitten wird beschrieben, wie ein Edge-Cluster installiert und der {{site.data.keyword.ieam}}-Agent im Edge-Cluster installiert wird.

- [Edge-Cluster vorbereiten](preparing_edge_cluster.md)
- [Agent installieren](edge_cluster_agent.md)
{: childlinks}
