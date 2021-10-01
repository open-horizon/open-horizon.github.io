---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} im Überblick
{: #overviewofedge}

Dieser Abschnitt vermittelt Ihnen einen Überblick über {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Leistungsspektrum von {{site.data.keyword.ieam}}
{: #capabilities}

{{site.data.keyword.ieam}} bietet Ihnen Edge-Computing-Funktionen, die Sie bei der Verwaltung von Workloads über einen Management-Hub-Cluster und der Bereitstellung von Workloads in Edge-Einheiten und fernen Instanzen von OpenShift® Container Platform oder anderen Kubernetes-basierten Clustern unterstützen.

## Architektur

Das Ziel besteht beim Edge-Computing im Schutz der Bereiche, die für das hybride Cloud-Computing erstellt wurden, um so den fernen Betrieb der Edge-Computing-Einrichtungen zu unterstützen. {{site.data.keyword.ieam}} wurde für diesen Zweck entworfen.

Die Bereitstellung von {{site.data.keyword.ieam}} beinhaltet den Management-Hub; dieser wird in einer Instanz von OpenShift Container Platform ausgeführt, die in Ihrem Rechenzentrum installiert ist. Der Management-Hub ist der Verbund, in dem die Verwaltung Ihrer fernen Edge-Knoten (Edge-Einheiten und Edge-Cluster) stattfindet.

Diese Edge-Knoten können an fernen lokalen Standorten installiert werden, um Ihre Anwendungsworkloads dort zu verarbeiten, wo auch der unternehmenskritische Betrieb physisch stattfindet, also in Ihren Fabriken, Warehouses, Einzelhandelsverkaufsstellen, Vertriebszentren und anderen Einrichtungen.

Im folgenden Diagramm wird die allgemeine Topologie einer typischen Edge-Computing-Konfiguration dargestellt:

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM overview">

Der {{site.data.keyword.ieam}}-Management-Hub wurde speziell für das Edge-Knoten-Management konzipiert, um die Bereitstellungsrisiken zu minimieren und den Softwarelebenszyklus von Services auf Edge-Knoten vollkommen autonom zu verwalten. Die Komponenten des {{site.data.keyword.ieam}}-Management-Hubs werden von einem Cloud-Installationsprogramm installiert und verwaltet. Softwareentwickler entwickeln Edge-Services und stellen sie auf dem Management-Hub bereit. Administratoren definieren die Bereitstellungsrichtlinien, die steuern, wo die Edge-Services bereitgestellt werden. Alle anderen Aufgaben werden von {{site.data.keyword.ieam}} übernommen.

# Komponenten
{: #components}

Weitere Informationen zu Komponenten, die im Lieferumfang von {{site.data.keyword.ieam}} enthalten sind, finden Sie unter [Komponenten](components.md).

## Weitere Schritte

Weitere Informationen zur Verwendung von {{site.data.keyword.ieam}} und zur Entwicklung von Edge-Services finden Sie in den Abschnitten, die auf der [Begrüßungsseite](../kc_welcome_containers.html) von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) aufgelistet sind.
