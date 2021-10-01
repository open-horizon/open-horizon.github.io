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

# Edge-Service für Cluster entwickeln
{: #developing_clusters}

Die Edge-Cluster-Funktion von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) bietet Ihnen Edge-Computing-Funktionen, mit denen Sie Workloads von einem Management-Hub-Cluster aus verwalten und in fernen Instanzen von OpenShift® Container Platform oder anderen Kubernetes-basierten Clustern bereitstellen können. Edge-Cluster sind {{site.data.keyword.ieam}}-Edge-Knoten, die als Kubernetes-Cluster dienen. Ein Edge-Cluster ermöglicht Anwendungsfälle beim Edge-Computing, die eine Zusammenstellung von Rechen- und Geschäftsoperationen erforderlich machen oder eine größere Skalierungs-, Verfügbarkeits- und Rechenfunktionalität benötigen, als von einer Edge-Einheit unterstützt werden kann. Außerdem werden Edge-Cluster aufgrund ihrer räumlichen Nähe zu Edge-Einheiten teilweise auch dazu eingesetzt, Anwendungsservices bereitstellen, die zur Unterstützung von auf einer Edge-Einheit ausgeführten Services benötigt werden, wodurch eine mehrschichtige Edge-Anwendung entsteht.{{site.data.keyword.ieam}} stellt Edge-Services über einen Kubernetes-Operator in einem Edge-Cluster bereit, was denselben autonomen Bereitstellungsmechanismus wie bei Edge-Einheiten ermöglicht. Für Edge-Services, die durch {{site.data.keyword.ieam}} bereitgestellt werden, ist die volle Leistungsstärke von Kubernetes als Container-Management-Plattform verfügbar.

<img src="../../images/edge/03b_Developing_edge_service_for_cluster.svg" width="80%" alt="Entwicklung eines Edge-Service für Cluster">

* [Kubernetes-Operator entwickeln](service_operators.md)
* [Eigenen Hello World-Service für Cluster erstellen](creating_hello_world.md)
