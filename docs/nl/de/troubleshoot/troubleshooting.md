---

copyright:
years: 2020
lastupdated: "2020-10-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Tipps zur Fehlerbehebung und häufig gestellte Fragen (FAQs)
{: #troubleshooting}

Die Tipp zur Fehlerbehebung und häufig gestellten Fragen helfen Ihnen bei der Behebung möglicherweise auftretender Fehler.
{:shortdesc}

* [Tipps zur Fehlerbehebung](troubleshooting_devices.md)
* [Häufig gestellte Fragen (FAQs)](../getting_started/faq.md)

Der folgende Inhalt zur Fehlerbehebung enthält Beschreibungen der Hauptkomponenten von  {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) und Informationen dazu, wie die integrierten Schnittstellen untersucht werden können, um den Status des Systems zu ermitteln.

## Fehlerbehebungstools
{: #ts_tools}

Zahlreiche Schnittstellen, die zum Lieferumfang von {{site.data.keyword.ieam}} gehören, stellen Informationen bereit, die zum Diagnostizieren von Problemen verwendet werden können. Diese Informationen sind über die {{site.data.keyword.gui}} sowie über HTTP-REST-APIs und das {{site.data.keyword.linux_notm}}-Shell-Tool `hzn` verfügbar.

Auf einem Edge-Knoten müssen möglicherweise Probleme mit dem Host, Probleme mit der Horizon-Software, Docker-Probleme oder Probleme mit der Konfiguration oder dem Code in Service-Containern behoben werden. Probleme mit dem Host des Edge-Knotens liegen außerhalb des Umfangs dieser Dokumentation. Wenn Sie Fehler in Docker beheben müssen, können Sie eine Reihe von Docker-Befehlen und -Schnittstellen nutzen. Weiterführende Informationen erhalten Sie in der Docker-Dokumentation.

Wenn die ausgeführten Servicecontainer {{site.data.keyword.message_hub_notm}} (das auf Kafka basiert) zur Nachrichtenübermittlung verwenden, können Sie manuell eine Verbindung zu den Kafka-Datenströmen für {{site.data.keyword.ieam}} herstellen, um Probleme zu diagnostizieren. Sie können ein Nachrichtenthema subskribieren, um zu beobachten, welche Informationen von {{site.data.keyword.message_hub_notm}} empfangen wurden, oder Sie können in einem Nachrichtenthema publizieren, um Nachrichten aus einer anderen Einheit zu simulieren. Der {{site.data.keyword.linux_notm}}-Befehl `kafkacat` stellt eine Methode zum Publizieren oder Subskribieren bei {{site.data.keyword.message_hub_notm}} dar. Verwenden Sie die neueste Version dieses Tools. {{site.data.keyword.message_hub_notm}} stellt darüber hinaus grafische Webseiten bereit, die Sie zum Zugriff auf bestimmte Informationen verwenden können.

Verwenden Sie auf allen Edge-Knoten, auf denen {{site.data.keyword.horizon}} installiert ist, den Befehl `hzn`, um Fehler beim lokalen {{site.data.keyword.horizon}}-Agenten und dem fernen {{site.data.keyword.horizon_exchange}} zu beheben. Intern interagiert der Befehl `hzn` mit den bereitgestellten HTTP-REST-APIs. Der Befehl `hzn` vereinfacht den Zugriff und bietet eine bessere Benutzererfahrung als die eigentlichen REST-APIs. Der Befehl `hzn` stellt in seiner Ausgabe häufig zusätzlichen beschreibenden Text bereit, und er enthält ein integriertes Onlinehilfesystem. Verwenden Sie das Hilfesystem, um Informationen und Details zu den zu verwendenden Befehlen sowie Details zur Befehlssyntax und den Argumenten abzurufen. Um diese Hilfeinformationen anzuzeigen, führen Sie die Befehle `hzn -- help` oder `hzn <subcommand> --help` aus.

Auf Edge-Knoten, auf denen {{site.data.keyword.horizon}}-Pakete nicht unterstützt werden oder nicht installiert sind, können Sie stattdessen direkt mit den zugrunde liegenden HTTP-REST-APIs interagieren. Sie können beispielsweise das Dienstprogramme `curl` oder andere Dienstprogramme der Befehlszeilenschnittstelle der REST-API verwenden. Sie können auch ein Programm in einer Sprache schreiben, die REST-Abfragen unterstützt.

Führen Sie beispielsweise das Dienstprogramm `curl` aus, um den Status Ihres Edge-Knotens zu prüfen:
```
curl localhost:8510/status
```
{: codeblock}

## Tipps zur Fehlerbehebung
{: #ts_tips}

Zur Vereinfachung der Fehlerbehebung bei bestimmten Problemen sollten Sie die Fragen zum Status Ihres Systems und alle zugehörigen Tipps überprüfen, die in den folgenden Abschnitten aufgeführt werden. Für jede Frage wird beschrieben, warum die Frage hinsichtlich der Fehlerbehebung auf Ihrem System relevant ist. Bei einigen Fragen werden Tipps oder detaillierte Anleitungen gegeben, in denen Sie Informationen zur Vorgehensweise erhalten, die bei der Abfrage der zugehörigen Informationen für Ihr System anzuwenden ist.

Diese Fragen basieren auf der Vorgehensweise beim Debuggen von Problemen und beziehen sich auf verschiedene Umgebungen. Wenn beispielsweise Probleme auf einem Edge-Knoten behoben werden sollen, benötigen Sie möglicherweise vollständigen Zugriff auf und volle Kontrolle über den Knoten, um die Erfassung und Anzeige der benötigten Informationen zu verbessern.

* [Tipps zur Fehlerbehebung](troubleshooting_devices.md)

  Informieren Sie sich über häufig auftretende Probleme, die bei Verwendung von {{site.data.keyword.ieam}} auftreten können.
  
## Risiken von {{site.data.keyword.ieam}} und deren Minimierung
{: #risks}

Obwohl {{site.data.keyword.ieam}} einzigartige Möglichkeiten schafft, birgt es auch Herausforderungen. So geht Edge-Computing beispielsweise über die physischen Begrenzungen von Cloudrechenzentren hinaus, was zu Problemen bei der Sicherheit, der Adressierbarkeit, der Verwaltung, der Eigentumsrechte und der Einhaltung von Vorschriften führen kann. Wichtiger noch: Es vervielfacht die Skalierungsproblme der cloudbasierten Managementtechniken.

Durch Edge-Netze wird die Anzahl der Rechenknoten um eine Größenordnung erhöht. Durch Edge-Gateways wird diese Anzahl zusätzlich um eine weitere Größenordnung erhöht. Durch Edge-Geräte wird diese Anzahl um 3-4 Größenordnungen erhöht. Wenn DevOps (Continuous Delivery und Continuous Deployment) für die Verwaltung einer extrem großen Cloudinfrastruktur kritisch ist, ist ZeroOps (Operationen ohne manuelle Eingriffe) kritisch für die Verwaltung der enormen Größe, die {{site.data.keyword.ieam}} darstellt.

Die vollautomatische Bereitstellung, Aktualisierung, Überwachung und Wiederherstellung des Edge-Computing-Raums ohne Bedienereingriff ist eine Grundbedingung. Für all diese Aktivitäten und Prozesse muss Folgendes gelten:

* Vollständige Automatisierung
* Fähigkeit zur unabhängigen Entscheidungsfindung über die Zuordnung von Arbeiten
* Fähigkeit zur Erkennung geänderter Bedingungen und zur Durchführung entsprechender Wiederherstellungsoperationen ohne Eingriff

Darüber hinaus müssen diese Aktivitäten geschützt, tracefähig und rechtssicher sein.
