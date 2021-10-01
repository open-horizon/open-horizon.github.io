---

copyright:
  years: 2016, 2019
lastupdated: "2019-03-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Funktionen zur barrierefreien Bedienung

Funktionen zur barrierefreien Bedienung unterstützen Benutzer mit einer Behinderung, wie z. B. einer eingeschränkten Bewegungsfähigkeit oder Sehbehinderung, damit sie informationstechnologische Inhalte erfolgreich verwenden können.
{:shortdesc}

## Übersicht

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) umfasst folgende Hauptfunktionen zur barrierefreien Bedienung:

* Bedienung nur über die Tastatur
* Operationen, bei denen ein Sprachausgabeprogramm verwendet wird
* Befehlszeilenschnittstelle (Command Line Interface, CLI) zum Verwalten des {{site.data.keyword.ieam}}-Clusters

{{site.data.keyword.ieam}} verwendet den aktuellen W3C-Standard [WAI-ARIA 1.0 ![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")](http://www.w3.org/TR/wai-aria/){: new_window}, um die Einhaltung von [US-Standards für Elektronik und Informationstechnologie gemäß Abschnitt 508 ![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards){: new_window} und [Web Content Accessibility Guidelines (WCAG) 2.0 ![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")](http://www.w3.org/TR/WCAG20/){: new_window} sicherzustellen. Um die Funktionen zur barrierefreien Bedienung nutzen zu können, verwenden Sie das aktuelle Release Ihres Sprachausgabeprogramms und den aktuellen Web-Browser, der von {{site.data.keyword.ieam}} unterstützt wird.

Die {{site.data.keyword.ieam}}-Onlineproduktdokumentation in der IBM Dokumentation ist für die Barrierefreiheit aktiviert. Allgemeine Informationen zur barrierefreien Bedienung finden Sie in [Accessibility in IBM ![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")](http://www.ibm.com/accessibility/us/en/){: new_window}.

## Hyperlinks

Alle externen Links, die Links zu Inhalten sind, die außerhalb der IBM Dokumentation gehostet werden, öffnen sich in einem neuen Fenster. Diese externen Links werden auch mit einem Symbol für externe Links (![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")) markiert.

## Tastaturnavigation

{{site.data.keyword.ieam}} verwendet Standardnavigationstasten.

{{site.data.keyword.ieam}} verwendet die folgenden Direktaufrufe über die Tastatur.

|Aktion|Direktaufruf für Internet Explorer|Direktaufruf für Firefox|
|------|------------------------------|--------------------|
|Aufrufen des Frames 'Inhaltsansicht'|Alt+C, dann Eingabetaste und Umschalttaste+F6|Umschalttaste+Alt+C und Umschalttaste+F6|
{: caption="Tabelle 1. Direktaufrufe in {{site.data.keyword.ieam}}" caption-side="top"}

## Schnittstelleninformationen

Verwenden Sie die neueste Version eines Sprachausgabeprogramms mit {{site.data.keyword.ieam}}.

In den Benutzerschnittstellen von {{site.data.keyword.ieam}} gibt es keine Inhalte, die 2 bis 55 Mal pro Sekunde blinken.

Die Webbenutzerschnittstelle von {{site.data.keyword.ieam}} basiert auf Cascading Style Sheets, um Inhalte richtig und benutzerfreundlich wiederzugeben. Die Anwendung bietet eine funktional entsprechende Möglichkeit für Benutzer mit eingeschränktem Sehvermögen, um die Einstellungen für die Systemanzeige, einschließlich des Modus für kontraststarke Anzeige, zu verwenden. Sie können die Schriftgröße über die Einstellungen für das Gerät oder den Web-Browser steuern.

Um auf die {{site.data.keyword.gui}} zuzugreifen, öffnen Sie einen Web-Browser und navigieren Sie zu der folgenden URL:

`https://<Cluster-Master-Host>:<Port_für_Cluster-Master-API>/edge`

Der Benutzername und das Kennwort sind in der Datei 'config.yaml' definiert.

Die {{site.data.keyword.gui}} basiert nicht auf Cascading Style Sheets, um Inhalte richtig und benutzerfreundlich wiederzugeben. Die Produktdokumentation, die in der IBM Knowledge Documentation verfügbar ist, setzt jedoch auf Cascading Style Sheets. {{site.data.keyword.ieam}} bietet eine funktional entsprechende Möglichkeit für Benutzer mit eingeschränktem Sehvermögen, um die Einstellungen für die Systemanzeige, einschließlich des Modus für kontraststarke Anzeige, zu verwenden. Sie können die Schriftgröße über die Einstellungen für das Gerät oder den Browser steuern. Beachten Sie, dass die Produktdokumentation Dateipfade, Umgebungsvariablen, Befehle und andere Inhalte enthält, die von Standardsprachausgabeprogrammen möglicherweise nicht richtig ausgesprochen werden. Um möglichst zuverlässige Beschreibungen zu erhalten, konfigurieren Sie die Einstellungen für das Sprachausgabeprogramm so, dass alle Interpunktionszeichen gelesen werden.


## Software anderer Anbieter

{{site.data.keyword.ieam}} enthält bestimmte Software anderer Anbieter, die nicht unter die IBM Lizenzvereinbarung fällt. IBM gibt keine Erklärung zu den Funktionen zur barrierefreien Bedienung dieser Produkte ab. Wenn Sie solche Informationen benötigen, wenden Sie sich bitte an den Anbieter.

## Zugehörige Informationen zur barrierefreien Bedienung

Neben dem gewohnten IBM Help-Desk und den Support-Websites bietet IBM einen TTY-Telefonservice für gehörlose oder hörgeschädigte Kunden für den Zugriff auf Vertriebs- und Support-Services:

TTY-Service  
 800-IBM-3383 (800-426-3383)  
 (in Nordamerika)

Weitere Informationen zum Engagement von IBM für barrierefreie Bedienung finden Sie in [IBM Accessibility ![Symbol für externen Link](../images/icons/launch-glyph.svg "Symbol für externen Link")](http://www.ibm.com/able){: new_window}.
