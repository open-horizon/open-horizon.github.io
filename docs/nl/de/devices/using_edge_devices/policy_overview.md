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

# Richtlinien im Überblick
{: #policy_overview}

Eine Grafik mit den an der Richtlinie beteiligten Komponenten (Ex, Knoten, Service und Geschäftsrichtlinie, Bedingungen, Eigenschaften) ist hinzuzufügen. 

In diesem Abschnitt werden die Richtlinienkonzepte erläutert. 

Eine umfassendere Übersicht über die verschiedenen Systemkomponenten finden Sie unter [Funktionsweise von IBM Edge Application Manager for Devices im Überblick](../getting_started/overview.md). Ein praktisches Beispiel für eine Richtlinie finden Sie unter [Hello World](../getting_started/policy.md).

Da ein Administrator nicht gleichzeitig Tausende von Edge-Knoten verwalten kann, schafft eine Skalierung von bis zu Zehntausenden oder mehr eine unmögliche Situation. Um diese Skalierungsstufe zu erreichen, verwendet {{site.data.keyword.edge_devices_notm}} Richtlinien, mit denen ermittelt wird, wo und wann Services und Modelle für maschinelles Lernen autonom bereitgestellt werden sollten. Richtlinien stellen eine Alternative zu Bereitstellungsmustern dar.

Eine Richtlinie wird durch eine flexible Richtliniensprache ausgedrückt, die auf Modelle, Knoten, Services und Bereitstellungsrichtlinien angewendet wird. Die Richtliniensprache definiert Attribute (bezeichnet als `properties`, Eigenschaften) und sichert bestimmte Anforderungen zu (bezeichnet als `constraints`, Bedingungen). Auf diese Weise kann jeder Teil des Systems Eingaben für die {{site.data.keyword.edge_devices_notm}}-Bereitstellungsengine beitragen. Bevor Services bereitgestellt werden können, werden die Bedingungen für Modelle, Knoten, Services und Implementierungsrichtlinien geprüft, um sicherzustellen, dass alle Anforderungen erfüllt werden.

Weil Knoten (in denen Services bereitgestellt werden) Anforderungen ausdrücken können, wird die {{site.data.keyword.edge_devices_notm}}-Richtlinie als bidirektionales Richtliniensystem beschrieben. Knoten sind im {{site.data.keyword.edge_devices_notm}}-Richtlinienbereitstellungssystem keine Slaves. Daher bieten Richtlinien eine genauere Kontrolle über die Service- und Modellbereitstellung als Muster. Wenn eine Richtlinie verwendet wird, sucht {{site.data.keyword.edge_devices_notm}} nach Knoten, in denen es einen bestimmten Service bereitstellen kann, und analysiert vorhandene Knoten, um sicherzustellen, dass sie richtlinienkompatibel bleiben. Ein Knoten befindet sich innerhalb der Richtlinie, wenn der Knoten, der Service und die Bereitstellungsrichtlinien, die den Service ursprünglich bereitgestellt haben, in Kraft bleiben oder wenn Änderungen an einer dieser Richtlinien die Richtlinienkompatibilität nicht beeinträchtigen. Die Verwendung von Richtlinien ermöglicht eine stärkere Trennung der Belange (Separation of Concerns), sodass Eigner von Edge-Knoten, Serviceentwickler und Geschäftseigner ihre eigenen Richtlinien unabhängig voneinander artikulieren können.

Es gibt vier Richtlinientypen:

* Knoten
* Service
* Bereitstellung
* Modell
