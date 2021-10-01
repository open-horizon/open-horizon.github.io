---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Muster verwenden
{: #using_patterns}

In der Regel können Servicebereitstellungsmuster im {{site.data.keyword.edge_notm}}-Hub ({{site.data.keyword.ieam}}) veröffentlicht werden, nachdem ein Entwickler einen Edge-Service in Horizon Exchange veröffentlicht hat.

Die CLI 'hzn' bietet Funktionen zum Auflisten und Verwalten von Mustern in {{site.data.keyword.horizon_exchange}} sowie Befehle zum Auflisten, Veröffentlichen, Verifizieren, Aktualisieren und Entfernen von Servicebereitstellungsmustern. Darüber hinaus bietet sie eine Möglichkeit, kryptografische Schlüssel aufzulisten und zu entfernen, die einem bestimmten Bereitstellungsmuster zugeordnet sind.

Eine vollständige Liste der CLI-Befehle und weitere Details erhalten Sie wie folgt:

```
hzn exchange pattern -h
```
{: codeblock}

## Beispiel

Signieren und erstellen (oder aktualisieren) Sie eine Musterressource in {{site.data.keyword.horizon_exchange}}:

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## Bereitstellungsmuster verwenden

Die Verwendung eines Bereitstellungsmusters ist eine einfache Methode, um einen Service auf Ihrem Edge-Knoten bereitzustellen. Sie geben einzelne oder mehrere Services der höchsten Ebene an, die auf Ihrem Edge-Knoten bereitgestellt werden sollen, und {{site.data.keyword.ieam}} übernimmt die Ausführung der restlichen Operationen einschließlich der Bereitstellung aller abhängigen Services, die zu Ihrem Service der höchsten Ebene gehören.

Nachdem Sie einen Service erstellt und zu {{site.data.keyword.ieam}} Exchange hinzugefügt haben, müssen Sie eine Datei mit dem Namen `pattern.json` erstellen, die folgendes Format hat:

```
{
  "IBM/pattern-ibm.cpu2evtstreams": {
    "owner": "root/root",     "label": "Edge ibm.cpu2evtstreams Service Pattern for arm architectures",     "description": "Pattern for ibm.cpu2evtstreams sending cpu and gps info to the IBM Event Streams",     "public": true,     "services": [       {
        "serviceUrl": "ibm.cpu2evtstreams",       "serviceOrgid": "IBM",       "serviceArch": "arm",       "serviceVersions": [         {
            "version": "1.4.3",             "priority": {},             "upgradePolicy": {}           }
        ],         "dataVerification": {
          "metering": {}
        },         "nodeHealth": {
          "missing_heartbeat_interval": 1800,           "check_agreement_status": 1800         }
      }
    ],     "agreementProtocols": [       {
        "name": "Basic"       }
    ],     "lastUpdated": "2020-10-24T14:46:44.341Z[UTC]"
  }
}
```
{: codeblock}

Dieser Code ist ein Beispiel für eine Datei `pattern.json` für den Service `ibm.cpu2evtstreams` für Einheiten des Typs `arm`. Wie hier dargestellt, müssen `cpu_percent` und `gps` (abhängige Services von `cpu2evtstreams`) nicht angegeben werden. Diese Task wird von der Datei `service_definition.json` übernommen. Daher führt ein erfolgreich registrierter Edge-Knoten diese Workloads automatisch aus.

Die Datei `pattern.json` ermöglicht Ihnen die Anpassung der Rollback-Einstellungen im Abschnitt `serviceVersions`. Sie können mehrere ältere Versionen Ihres Service angeben und jeder Version eine Priorität für den Edge-Knoten zuweisen, für den ein Rollback durchgeführt werden soll, wenn bei Ihrer neuen Version ein Fehler auftritt. Neben dem Zuweisen einer Priorität zu jeder Rollback-Version können Sie außerdem Optionen wie die Anzahl und Dauer von Wiederholungsversuchen vor dem Zurücksetzen auf eine Version des angegebenen Service mit einer geringeren Priorität festlegen.

Sie können auch alle Konfigurationsvariablen zentral festlegen, die Ihr Service zum ordnungsgemäßen Funktionieren benötigt, wenn Sie Ihr Bereitstellungsmuster veröffentlichen, indem Sie sie im Abschnitt `userInput` unten eingeben. Wenn der Service `ibm.cpu2evtstreams` veröffentlicht wird, übergibt er die Berechtigungsnachweise, die für die Veröffentlichung von Daten in IBM Event Streams erforderlich sind. Hierzu geben Sie folgenden Befehl ein:

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

Nachdem das Muster veröffentlicht wurde, können Sie eine Einheit des Typs 'arm' registrieren:

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

Mit diesem Befehl werden `ibm.cpu2evtstreams` und alle abhängigen Services auf Ihrem Knoten bereitgestellt.

Hinweis: Eine Datei `userInput.json` wird nicht in den oben genannten Befehl `hzn register` übergeben, wie dies der Fall wäre, wenn Sie die Schritte im Repository-Beispiel von [Mit dem CPU für die IBM Event Streams Edge Service mit Implementierungsmuster verwenden](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern) befolgen würden. Da Benutzereingaben mit dem Muster übergeben wurden, hat jeder Edge-Knoten, der automatisch registriert wird, Zugriff auf diese Umgebungsvariablen.

Alle `ibm.cpu2evtstreams`-Workloads können durch Aufheben der Registrierung gestoppt werden:

```
hzn unregister -fD
```
{: codeblock}
