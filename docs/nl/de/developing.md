---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Service für Einheiten entwickeln
{: #developing}

Um mit der Entwicklung von Edge-Services für {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) zu beginnen, müssen Sie zunächst Ihre Berechtigungsnachweise für das Publizieren von Inhalten definieren. Da alle Services sein werden müssen, müssen Sie auch ein verschlüsseltes Signierschlüsselpaar erstellen. Stellen Sie sicher, dass die vorausgesetzten Schritte (siehe [Erstellung eines Edge-Service vorbereiten](service_containers.md)) ausgeführt wurden.

Im folgenden Diagramm sind die typischen Interaktionen zwischen den Komponenten in {{site.data.keyword.horizon}} dargestellt.

<img src="../images/edge/03a_Developing_edge_service_for_device.svg" style="margin: 3%" alt="Edge-Einheiten"> 

## Beispiele
{: #edge_devices_ex_examples}

Verwenden Sie Ihre Berechtigungsnachweise und Signierschlüssel, um die Entwicklungsbeispiele auszuführen. Diese Beispiele stellen dar, wie Sie einfache Services erstellen können, und veranschaulichen die wichtigsten Grundlagen der Entwicklung mit {{site.data.keyword.ieam}}.

Jedes dieser Entwicklungsbeispiele veranschaulicht eine Reihe weiterer Aspekte der Entwicklung von Edge-Services. Sie erzielen das optimale Lernergebnis, wenn Sie die Beispiele in der hier angegebenen Reihenfolge durcharbeiten.

* [Image in Edge-Service umwandeln](transform_image.md) - Stellt dar, wie ein vorhandenes Docker-Image als Edge-Service bereitgestellt wird.

* [Eigenen Edge-Service ('Hello World') erstellen](developingstart_example.md) - Vermittelt grundlegende Kenntnisse für das Entwickeln, Testen, Publizieren und Bereitstellen eines Edge-Service.

* [Service für 'CPU zu {{site.data.keyword.message_hub_notm}}'](cpu_msg_example.md) - Stellt dar, wie Konfigurationsparameter für Edge-Services definiert werden, wie angegeben wird, dass für Ihren Edge-Service andere Edge-Services erforderlich sind, und wie Daten an einen Aufnahmeservice für Clouddaten gesendet werden.

* [Hello World mit Modell-Management-Service](model_management_system.md) - Stellt dar, wie ein Edge-Service entwickelt wird, der den Model Management Service verwendet. Der Model Management Service stellt Dateiaktualisierungen für Edge-Services auf Edge-Knoten asynchron zur Verfügung, um z. B. ein Modell für maschinelles Lernen bei jedem Evolutionsschritt dynamisch zu aktualisieren.

* [Hello world using secrets](developing_secrets.md) - veranschaulicht, wie ein Edge-Service entwickelt wird, der Geheimnisse verwendet. Geheimnisse werden verwendet, um sensible Daten wie Anmeldeinformationen oder private Schlüssel zu schützen. Geheimnisse werden sicher auf Services implementiert, die an der Edge ausgeführt werden.

* [Edge-Service mit Rollback aktualisieren](../using_edge_services/service_rollbacks.md) - Stellt dar, wie der Erfolg der Bereitstellung überwacht wird und wie bei einem Fehler auf einem Edge-Knoten der Knoten wieder auf die Vorgängerversion des Edge-Service zurückgesetzt wird.

Nachdem Sie die Erstellung dieser Beispielservices abgeschlossen haben, sollten Sie die weiterführenden Informationen zum Entwickeln von Services für {{site.data.keyword.ieam}} in der folgenden Dokumentation lesen:

## Weiterführende Informationen
{: #developing_more_info}

Informieren Sie sich über die wichtigen Prinzipien und bewährten Verfahren (Best Practices) für die {{site.data.keyword.ieam}}-Softwareentwicklung.

* [Bewährte Verfahren bei der Edge-nativen Entwicklung](best_practices.md)

Mit {{site.data.keyword.ieam}} können Sie Service-Container-Images anstatt im öffentlichen Docker Hub optional in der privaten sicheren IBM Container-Registry speichern. Dies kann beispielsweise empfehlenswert sein, wenn Sie ein Software-Image mit Assets verwenden, deren Speicherung in einer öffentlichen Registry unangemessen wäre.

* [Private Container-Registry verwenden](container_registry.md)

Sie können {{site.data.keyword.ieam}} verwenden, um Ihre Service-Container anstatt im öffentlichen Docker Hub auch in der privaten sicheren IBM Container-Registry zu speichern.

* [Details zur Entwicklung](developing_details.md)

Mit {{site.data.keyword.ieam}} können Sie sämtliche Service-Container entwickeln, die Sie für Ihre Edge-Maschinen benötigen.

* [APIs](../api/edge_rest_apis.md)

{{site.data.keyword.ieam}} stellt REST-konforme APIs zum Aktivieren von Komponenten für die Zusammenarbeit bereit, wodurch den Entwicklern und Benutzern Ihrer Organisation die Möglichkeit zur Steuerung der Komponenten gegeben wird.
