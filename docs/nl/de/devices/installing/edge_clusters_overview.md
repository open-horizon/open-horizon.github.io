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

# Edge-Service für Cluster im Überblick
{: #edge_clusters_overview}

Die Edge-Cluster-Funktion von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) bietet Ihnen Edge-Computing-Funktionen, mit denen Sie Workloads aus einem Hub-Cluster einfacher verwalten und in fernen Instanzen von OpenShift® Container Platform 4.2 oder anderen Kubernetes-basierten Clustern bereitstellen können. Edge-Cluster sind {{site.data.keyword.ieam}}-Edge-Knoten, die als Kubernetes-Cluster bereitgestellt werden. Ein Edge-Cluster ermöglicht Anwendungsfälle an der Peripherie eines Systems, die eine Zusammenstellung von Rechen- und Geschäftsoperationen erforderlich machen oder eine größere Skalierungs- und Rechenfunktionalität benötigen, als von einer Edge-Device unterstützt werden kann. Außerdem ist es nicht ungewöhnlich, dass Edge-Cluster Anwendungsservices bereitstellen, die zur Unterstützung von Services benötigt werden, deren Ausführung aufgrund ihrer großen Ähnlichkeit mit Edge-Einheiten auf einer Edge-Einheit erfolgt. IEAM stellt Edge-Services über einen Kubernetes-Operator in einem Edge-Cluster bereit, was denselben autonomen Bereitstellungsmechanismus wie bei Edge-Einheiten ermöglicht. Für Edge-Services, die durch {{site.data.keyword.ieam}} bereitgestellt werden, ist die volle Leistungsstärke von Kubernetes als Container-Management-Plattform verfügbar.

Mit IBM Cloud Pak for Multicloud Management kann optional ein intensiveres Kubernetes-spezifisches Management von Edge-Clustern erreicht werden, selbst bei Edge-Services, die durch IEAM bereitgestellt werden.

Eine Grafik mit übergeordneten Schritten zur Installation und Konfiguration von Edge-Clustern ist hinzuzufügen. 

## Weitere Schritte

Informationen zur Installation von Edge-Clustern enthält der Abschnitt [Edge-Cluster](../developing/edge_clusters.md).

## Zugehörige Informationen

* [Edge-Knoten installieren](installing_edge_nodes.md)
* [Edge-Einheiten](../developing/edge_devices.md)
* [Edge-Cluster](../developing/edge_clusters.md)
