---

copyright:
  years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Edge-Service für Cluster im Überblick
{: #cluster_deployment}

Die Edge-Cluster-Funktion von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) bietet Ihnen Edge-Computing-Funktionen, mit denen Sie Workloads aus einem Hub-Cluster einfacher verwalten und in fernen Instanzen von OpenShift® Container Platform 4.2 oder anderen Kubernetes-basierten Clustern bereitstellen können. Edge-Cluster sind {{site.data.keyword.ieam}}-Edge-Knoten, die als Kubernetes-Cluster bereitgestellt werden. Ein Edge-Cluster ermöglicht Anwendungsfälle an der Peripherie eines Systems, die eine Zusammenstellung von Rechen- und Geschäftsoperationen erforderlich machen oder eine größere Skalierungs- und Rechenfunktionalität benötigen, als von einer Edge-Device unterstützt werden kann. Außerdem ist es nicht ungewöhnlich, dass Edge-Cluster Anwendungsservices bereitstellen, die zur Unterstützung von Services benötigt werden, deren Ausführung aufgrund ihrer großen Ähnlichkeit mit Edge-Einheiten auf einer Edge-Einheit erfolgt. {{site.data.keyword.ieam}} stellt Edge-Services über einen Kubernetes-Operator in einem Edge-Cluster bereit, was denselben autonomen Bereitstellungsmechanismus wie bei Edge-Einheiten ermöglicht. Für Edge-Services, die durch {{site.data.keyword.ieam}} bereitgestellt werden, ist die volle Leistungsstärke von Kubernetes als Container-Management-Plattform verfügbar.

Mit IBM Cloud Pak for Multicloud Management kann optional ein intensiveres Kubernetes-spezifisches Management von Edge-Clustern erreicht werden, selbst bei Edge-Services, die durch {{site.data.keyword.ieam}} bereitgestellt werden.

Eine Grafik mit übergeordneten Schritten für die Installation und Konfiguration von Edge-Knoten (inklusive Darstellung von Einheiten und Clustern) ist hinzuzufügen.
