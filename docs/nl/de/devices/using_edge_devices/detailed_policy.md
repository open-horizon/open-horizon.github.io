---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Services bereitstellen
{: #detailed_deployment_policy}

Sie können {{site.data.keyword.ieam}}-Richtlinien für {{site.data.keyword.edge_notm}} mithilfe von Richtlinien oder Mustern bereitstellen. Eine umfassendere Übersicht über die verschiedenen Systemkomponenten finden Sie in den Abschnitten [{{site.data.keyword.edge}} im Überblick](../../getting_started/overview_ieam.md) und [Anwendungsfälle für Bereitstellungsrichtlinien](policy_user_cases.md). Ein praktisches Beispiel für eine Richtlinie finden Sie unter [CI/CD-Prozess für Edge-Services](../developing/cicd_process.md).

Hinweis: Sie können auch Bereitstellungsrichtlinien oder Muster über die Managementkonsole erstellen und verwalten. Weitere Informationen hierzu finden Sie in [Managementkonsole verwenden](../getting_started/accessing_ui.md).

Dieser Abschnitt enthält eine Erläuterung der den Richtlinien und Mustern zugrunde liegenden Konzepte sowie ein Anwendungsfallszenario. 

Da ein Administrator nicht gleichzeitig Tausende von Edge-Knoten verwalten kann, schafft eine Skalierung von bis zu Zehntausenden oder mehr eine unmögliche Situation. Um diese Skalierungsstufe zu erreichen, verwendet {{site.data.keyword.edge_devices_notm}} Richtlinien, mit denen ermittelt wird, wo und wann Services und Modelle für maschinelles Lernen autonom bereitgestellt werden sollten.  

Eine Richtlinie wird durch eine flexible Richtliniensprache ausgedrückt, die auf Modelle, Knoten, Services und Bereitstellungsrichtlinien angewendet wird. Die Richtliniensprache definiert Attribute (bezeichnet als `properties`, Eigenschaften) und sichert bestimmte Anforderungen zu (bezeichnet als `constraints`, Bedingungen). Auf diese Weise kann jeder Teil des Systems Eingaben für die {{site.data.keyword.edge_devices_notm}}-Bereitstellungsengine beitragen. Bevor Services bereitgestellt werden können, werden die Bedingungen für Modelle, Knoten, Services und Implementierungsrichtlinien geprüft, um sicherzustellen, dass alle Anforderungen erfüllt werden.

Weil Knoten (in denen Services bereitgestellt werden) Anforderungen ausdrücken können, wird die {{site.data.keyword.edge_devices_notm}}-Richtlinie als bidirektionales Richtliniensystem beschrieben. Knoten sind im {{site.data.keyword.edge_devices_notm}}-Richtlinienbereitstellungssystem keine Slaves. Daher bieten Richtlinien eine genauere Kontrolle über die Service- und Modellbereitstellung als Muster. Wenn eine Richtlinie verwendet wird, sucht {{site.data.keyword.edge_devices_notm}} nach Knoten, in denen es einen bestimmten Service bereitstellen kann, und analysiert vorhandene Knoten, um sicherzustellen, dass sie richtlinienkompatibel bleiben. Ein Knoten befindet sich innerhalb der Richtlinie, wenn der Knoten, der Service und die Bereitstellungsrichtlinien, die den Service ursprünglich bereitgestellt haben, in Kraft bleiben oder wenn Änderungen an einer dieser Richtlinien die Richtlinienkompatibilität nicht beeinträchtigen. Die Verwendung von Richtlinien ermöglicht eine stärkere Trennung der Belange (Separation of Concerns), sodass Eigner von Edge-Knoten, Serviceentwickler und Geschäftseigner ihre eigenen Richtlinien unabhängig voneinander artikulieren können.

Richtlinien stellen eine Alternative zu Bereitstellungsmustern dar. Sie können Muster auf dem {{site.data.keyword.ieam}}-Hub veröffentlichen, nachdem ein Entwickler einen Edge-Service in Horizon Exchange veröffentlicht hat. Die CLI 'hzn' bietet Funktionen zum Auflisten und Verwalten von Mustern in Horizon Exchange sowie Befehle zum Auflisten, Veröffentlichen, Verifizieren, Aktualisieren und Entfernen von Servicebereitstellungsmustern. Darüber hinaus bietet sie eine Möglichkeit, kryptografische Schlüssel aufzulisten und zu entfernen, die einem bestimmten Bereitstellungsmuster zugeordnet sind.

* [Anwendungsfälle für Bereitstellungsrichtlinien](policy_user_cases.md)
* [Muster verwenden](using_patterns.md)
