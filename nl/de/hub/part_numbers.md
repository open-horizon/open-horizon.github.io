---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Passport Advantage
{: #part_numbers}

Führen Sie die folgenden Schritte aus, um Ihre {{site.data.keyword.ieam}}-Pakete herunterzuladen:

1. Suchen Sie die Teilenummer von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Rufen Sie die Registerkarte "IBM Passport Advantage Online" unter [Passport Advantage](https://www.ibm.com/software/passportadvantage/) auf und melden Sie sich mit Ihrer IBM ID an.
2. Suchen Sie Ihre Dateien anhand der in [{{site.data.keyword.ieam}}-Pakete und -Teilenummern](#part_numbers_table) aufgelisteten Teilenummern:
3. Laden Sie die Dateien in ein Verzeichnis auf Ihrem Computer herunter.

## {{site.data.keyword.ieam}}-Pakete und -Teilenummern
{: #part_numbers_table}

|Teilebeschreibung|Passport Advantage-Teilenummer|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} Ressourcen-Value-Unit - Lizenz + SW-Abonnement & Support 12 Monate|D2840LL|
|{{site.data.keyword.edge_notm}} Ressourcen-Value-Unit - JÄHRLICHES SW-ABONNEMENT & SUPPORTVERLÄNGERUNG 12 Monate|E0R0HLL|
|{{site.data.keyword.edge_notm}} Ressourcen-Value-Unit - JÄHRLICHES SW-ABONNEMENT & SUPPORTWEITERFÜHRUNG 12 Monate|D2841LL|
|{{site.data.keyword.edge_notm}} Ressourcen-Value-Unit - MONATLICHE LIZENZ|D283ZLL|
|{{site.data.keyword.edge_notm}} Ressourcen-Value-Unit - Lizenz mit festgeschriebener Laufzeit|D28I1LL|
{: caption="Tabelle 1. {{site.data.keyword.ieam}}-Pakete und -Teilenummern" caption-side="top"}

## Lizenzierung
{: #licensing}

Lizenzvoraussetzungen werden auf der Basis der Gesamtsumme der registrierten Knoten berechnet. Ermitteln Sie auf jedem System, auf dem die **hzn**-CLI installiert wurde und das zur Authentifizierung bei Ihrem Management-Hub konfiguriert wurde, die Gesamtsumme der registrierten Knoten:

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

Die Ausgabe ist eine ganze Zahl wie in der folgenden Beispielausgabe:

  ```
  $ hzn exchange status | jq .numberOfNodes   2641
  ```

Verwenden Sie die folgende Konvertierungstabelle im [{{site.data.keyword.ieam}}Lizenzinformationsdokument](https://ibm.biz/ieam-43-license) , um die erforderlichen Lizenzen zu berechnen, wobei die Knotenanzahl für Ihre Umgebung aus dem vorherigen Befehl zurückgegeben wurde:

  ```
  1 bis 10 Resourcen: 1,00 UVU pro Resource   11 bis 50 Resourcen: 10,0 UVUs plus 0,87 UVUs pro Ressource ab 10 Resourcen   51 bis 100 Resourcen: 44,8 UVUs plus 0,60 UVUs pro Ressource ab 50 Resourcen   101 bis 500 Resourcen: 74,8 UVUs plus 0,25 UVUs pro Ressource ab 100 Resourcen   501 bis 1.000 Resourcen: 174.8,0 UVUs plus 0,20 UVUs pro Ressource ab 500 Resourcen   1.001 bis 10.000 Resourcen: 274,8 UVUs plus 0,07 UVUs pro Ressource ab 1.000 Resourcen   10.001 bis 25.000 Resourcen: 904,8 UVUs plus 0,04 UVUs pro Ressource ab 10.000 Resourcen   25.001 bis 50.000 Resourcen: 1.504,8 UVUs plus 0,03 UVUs pro Ressource ab 25.000 Resourcen   50.001 bis 100.000 Resourcen: 2.254,8 UVUs plus 0,02 UVUs pro Ressource ab 50.000 Resourcen   Über 100.000 Resourcen: 3.254,8 UVUs plus 0,01 UVUs pro Ressource pro Ressource ab 100.000 Resourcen
  ```

Das folgende Beispiel führt Sie durch die Berechnung der erforderlichen Lizenzen für **2641** Knoten, für die der Erwerb von **mindestens 390** Lizenzen erforderlich wäre:

  ```
  274,8 + ( ,07 * ( 2641 - 1000 ) )
  274,8 + ( ,07 * 1641 )   274,8 + 114,87   389,67
  ```

## Lizenzberichterstellung

{{site.data.keyword.edge_notm}} Die Auslastung wird automatisch berechnet und in regelmäßigen Abständen auf einen allgemeinen Lizenzierungsservice hochgeladen, der lokal in Ihrem Cluster installiert ist. Weitere Informationen zum Lizenzierungsservice finden Sie unter anderem zum Anzeigen der aktuellen Verwendung, zum Generieren von Nutzungsberichten und zum weiteren Anzeigen der [Dokumentation zu Lizenzierungsservices](https://www.ibm.com/docs/en/cpfs?topic=operator-overview).
