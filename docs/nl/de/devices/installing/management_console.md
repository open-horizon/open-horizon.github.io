---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}}-Konsole verwenden
{: #accessing_ui}

In der Konsole können Sie Managementfunktionen für das Edge-Computing ausführen. 
 
## Zur {{site.data.keyword.edge_notm}}-Konsole navigieren

1. Navigieren Sie zur {{site.data.keyword.edge_notm}}-Konsole, indem Sie zu `https://<cluster-url>/edge` navigieren, wobei `<cluster-url>` für den externen Ingress des Clusters steht.
2. Geben Sie Ihre Benutzerberechtigungsnachweise ein. Die {{site.data.keyword.mcm}}-Anmeldeseite wird angezeigt.
3. Entfernen Sie in der Adressleiste Ihres Browsers `/multicloud/welcome` am Ende der URL, fügen Sie `/edge` hinzu und drücken Sie die **Eingabetaste**. Die {{site.data.keyword.edge_notm}}-Seite wird angezeigt.

## Unterstützte Browser

{{site.data.keyword.edge_notm}} wurde erfolgreich mit den folgenden Browsern getestet.

|Plattform|Unterstützte Browser|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - neueste Version für Windows</li><li>Google Chrome - Neueste Version für Windows</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - neueste Version für Mac</li><li>Google Chrome - neueste Version für Mac</li></ul>|
{: caption="Tabelle 1. Unterstützte Browser in {{site.data.keyword.edge_notm}}" caption-side="top"}


## {{site.data.keyword.edge_notm}}-Konsole erkunden
{: #exploring-management-console}

Zu den Funktionen der {{site.data.keyword.edge_notm}}-Konsole gehören:

* Benutzerfreundliches Onboarding mit Links zu peripheren Sites für robuste Unterstützung
* Umfangreiche Sichtbarkeits- und Managementfunktionen:
  * Umfangreiche Diagrammansichten, einschließlich Informationen zu Knotenstatus, Architektur und Fehlern
  * Fehlerdetails mit Links für Auflösungsunterstützung
  * Positions- und Filterinhalt, einschließlich Informationen zu: 
    * Eigner
    * Architektur 
    * Heartbeat (z. B. die letzten 10 Jahre, aktueller Tag usw.)
    * Knotenstatus (Aktiv, Inaktiv, Mit Fehler usw.)
    * Bereitstellungstyp (Richtlinie oder Muster)
  * Nützliche Details zu Exchange-Edge-Knoten, einschließlich:
    * Eigenschaften
    * Bedingungen 
    * Bereitstellungen
    * Aktive Services

* Robuste Ansichtsfunktionalität

  * Fähigkeit zur schnellen Suche und Filterung nach: 
    * Eigner
    * Architektur
    * Version
    * Öffentlich (wahr oder falsch)
  * Listen- oder Kartenserviceansichten
  * Gruppierte Services mit identischem Namen
  * Details für jeden Service in Exchange, einschließlich: 
    * Eigenschaften
    * Bedingungen
    * Bereitstellungen
    * Servicevariablen
    * Serviceabhängigkeiten
  
* Verwaltung von Bereitstellungsrichtlinien

  * Fähigkeit zur schnellen Suche und Filterung nach:
    * Richtlinien-ID
    * Eigner
    * Bezeichnung
  * Bereitstellen beliebiger Services aus Exchange
  * Hinzufügen von Eigenschaften zu Bereitstellungsrichtlinien
  * Ein Constraint Builder für die Erstellung von Ausdrücken 
  * Ein erweiterter Modus zum direkten Schreiben von Bedingungen in die JSON-Datei
  * Möglichkeit zur Anpassung von Rollback-Bereitstellungsversionen und Knotenzustandseinstellungen
  * Anzeigen und Bearbeiten von Richtliniendetails, einschließlich:
    * Service- und Bereitstellungseigenschaften
    * Bedingungen
    * Rollbacks
    * Einstellungen für den Knotenzustand
  
