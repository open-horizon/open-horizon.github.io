---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Fehlerbehebung
{: #troubleshooting}

Informieren Sie sich über die Tipps zur Fehlerbehebung und die allgemeinen Probleme, die bei Verwendung von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) auftreten können, um so die Fehlerbehebung von Problemen zu vereinfachen.
{:shortdesc}

Der folgende Leitfaden zur Fehlerbehebung enthält Beschreibungen der Hauptkomponenten eines {{site.data.keyword.ieam}}-Systems und Informationen dazu, wie die integrierten Schnittstellen untersucht werden können, um den Status des Systems zu ermitteln.

## Fehlerbehebungstools
{: #ts_tools}

Zahlreiche Schnittstellen, die zum Lieferumfang von {{site.data.keyword.ieam}} gehören, stellen Informationen bereit, die zum Diagnostizieren von Problemen verwendet werden können. Diese Informationen sind über die {{site.data.keyword.gui}} sowie über HTTP-REST-APIs und das {{site.data.keyword.linux_notm}}-Shell-Tool `hzn` verfügbar. 

Auf einem Edge-System müssen möglicherweise Probleme mit dem Host, Probleme mit der Horizon-Software, Docker-Probleme oder Probleme mit der Konfiguration oder dem Code in Service-Containern behoben werden. Probleme mit dem Host der Edge-Machine liegen außerhalb des Umfangs dieser Dokumentation. Wenn Sie Fehler in Docker beheben müssen, ist eine Reihe von Docker-Befehlen und -Schnittstellen verfügbar, die Sie verwenden können.
Weiterführende Informationen erhalten Sie in der Docker-Dokumentation.

Wenn die ausgeführten Servicecontainer {{site.data.keyword.message_hub_notm}} (das auf Kafka basiert) zur Nachrichtenübermittlung verwenden, können Sie manuell eine Verbindung zu den Kafka-Datenströmen für {{site.data.keyword.ieam}} herstellen, um Probleme zu diagnostizieren. Sie können ein Nachrichtenthema subskribieren, um zu beobachten, welche Informationen von {{site.data.keyword.message_hub_notm}} empfangen wurden, oder Sie können in einem Nachrichtenthema publizieren, um Nachrichten aus einer anderen Einheit zu simulieren. Der {{site.data.keyword.linux_notm}}-Befehl `kafkacat` stellt eine einfache Methode zum Publizieren oder Subskribieren bei {{site.data.keyword.message_hub_notm}} dar. Verwenden Sie die neueste Version dieses Tools. {{site.data.keyword.message_hub_notm}} stellt darüber hinaus grafische Webseiten bereit, die Sie zum Zugriff auf bestimmte Informationen verwenden können. 

Verwenden Sie auf allen Maschinen, auf denen {{site.data.keyword.horizon}} installiert ist, den Befehl `hzn`, um Fehler beim lokalen {{site.data.keyword.horizon}}-Agenten und dem fernen {{site.data.keyword.horizon_exchange}} zu beheben. Intern interagiert der Befehl `hzn` mit den bereitgestellten HTTP-REST-APIs. Der Befehl `hzn` vereinfacht den Zugriff und bietet eine bessere Benutzererfahrung als die eigentlichen REST-APIs. Der Befehl `hzn` stellt in seiner Ausgabe häufig zusätzlichen beschreibenden Text bereit, und er enthält ein integriertes Onlinehilfesystem. Verwenden Sie das Hilfesystem, um Informationen und Details zu den zu verwendenden Befehlen sowie Details zur Befehlssyntax und den Argumenten abzurufen. Führen Sie den Befehl `hzn --help` oder `hzn \<subcommand\> --help` aus, um diese Hilfeinformationen anzuzeigen. 

Auf Knoten, auf denen {{site.data.keyword.horizon}}-Pakete nicht unterstützt werden oder nicht installiert sind, können Sie stattdessen direkt mit den zugrunde liegenden HTTP-REST-APIs interagieren. Sie können beispielsweise das Dienstprogramme `curl` oder andere Dienstprogramme der Befehlszeilenschnittstelle der REST-API verwenden. Sie können auch ein Programm in einer Sprache schreiben, die REST-Abfragen unterstützt.  

## Tipps zur Fehlerbehebung
{: #ts_tips}

Zur Vereinfachung der Fehlerbehebung bei bestimmten Problemen sollten Sie die Fragen zum Status Ihres Systems und alle zugehörigen Tipps überprüfen, die in den folgenden Abschnitten aufgeführt werden. Für jede Frage wird beschrieben, warum die Frage für die Fehlerbehebung auf Ihrem System relevant ist. Bei einigen Fragen werden Tipps oder detaillierte Anleitungen gegeben, in denen Sie Informationen zur Vorgehensweise erhalten, die bei der Abfrage der zugehörigen Informationen für Ihr System anzuwenden ist. 

Diese Fragen basieren auf der Vorgehensweise beim Debuggen von Problemen und beziehen sich auf verschiedene Umgebungen. Wenn beispielsweise Probleme auf einem Edge-Knoten behoben werden sollen, benötigen Sie möglicherweise vollständigen Zugriff und volle Kontrolle über den Knoten, um die Erfassung und Anzeige der benötigten Informationen zu verbessern. 

* [Tipps zur Fehlerbehebung](troubleshooting_devices.md)

  Informieren Sie sich über häufig auftretende Probleme, die bei Verwendung von {{site.data.keyword.ieam}} auftreten können. 
