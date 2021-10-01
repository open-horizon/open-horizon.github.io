---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Knoten und -Services überwachen
{: #monitoring_edge_nodes_and_services}

Zur Überwachung der Edge-Knoten und Services von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) müssen Sie sich [bei der Managementkonsole anmelden](../console/accessing_ui.md).

* Edge-Knoten überwachen:
  * Als Erstes wird die Seite 'Knoten' angezeigt. Dort finden Sie ein Ringdiagramm, das den Zustand aller Edge-Knoten angibt.
  * Alle Knoten mit einem bestimmten Status können Sie anzeigen, indem Sie im Ringdiagramm auf die jeweilige Farbe klicken. Klicken Sie z. B. zum Anzeigen aller Edge-Knoten mit Fehlern (soweit vorhanden) auf die Farbe, die laut Legende für Knoten **mit Fehler** verwendet wird.
  * Daraufhin wird eine Liste der Knoten mit Fehlern angezeigt. Klicken Sie auf den Namen eines Knotens, wenn Sie einen Drilldown für einen bestimmten Knoten durchführen möchten, um den jeweiligen Fehler anzuzeigen.
  * Auf der daraufhin angezeigten Seite mit den Knotendetails werden im Abschnitt **Fehler des Edge-Agenten** die Services angezeigt, die Fehler aufweisen, sowie die jeweilige Fehlernachricht und die zugehörige Zeitmarke.
* Edge-Services überwachen:
  * Klicken Sie auf der Registerkarte **Services** auf den Service, für den Sie einen Drilldown durchführen möchten, wodurch die Detailseite für den Edge-Service angezeigt wird.
  * Im Abschnitt **Bereitstellung** der Detailseite werden die Richtlinien und Muster angezeigt, über die der betreffende Service auf Edge-Knoten bereitgestellt wird.
* Edge-Services auf einem Edge-Knoten überwachen:
  * Wechseln Sie auf der Registerkarte **Knoten** in die Listenansicht und klicken Sie auf den Edge-Knoten, für den Sie einen Drilldown durchführen möchten.
  * Auf der Detailseite für den Knoten werden im Abschnitt **Services** die Edge-Services angezeigt, die auf dem jeweiligen Edge-Knoten derzeit ausgeführt werden.
