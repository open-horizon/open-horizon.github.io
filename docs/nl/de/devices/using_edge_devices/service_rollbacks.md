---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Service mit Rollback aktualisieren
{: #service_rollback}

Services auf Edge-Knoten führen in der Regel kritische Funktionen aus. Wenn eine neue Version eines Edge-Service auf vielen Edge-Knoten implementiert wird, muss daher unbedingt der Erfolg der Bereitstellung überwacht werden und bei einer fehlgeschlagenen Bereitstellung auf einem der Edge-Knoten dieser Knoten auf die vorherige Version des Edge-Service zurückgesetzt werden. {{site.data.keyword.edge_notm}} kann dies automatisch übernehmen. Welche vorherige(n) Serviceversion(en) verwendet werden soll(en), wenn eine neue Serviceversion fehlschlägt, können Sie in Mustern oder Bereitstellungsrichtlinien definieren.

Nachfolgend erfahren Sie weitere Details über das Implementieren einer neuen Version für einen vorhandenen Edge-Service sowie über die bewährten Verfahren bei der Softwareentwicklung in Bezug auf die Aktualisierung von Rollback-Einstellungen in Mustern oder Bereitstellungsrichtlinien.

## Neue Edge-Service-Definition erstellen
{: #creating_edge_service_definition}

Wie unter [Edge-Services mit  {{site.data.keyword.edge_notm}} entwickeln](../developing/developing.md) und [Details zur Entwicklung](../developing/developing_details.md) erläutert, vollzieht sich die Freigabe einer neuen Version für einen Edge-Service in den folgenden Hauptschritten:

- Der Code des Edge-Service wird für die neue Version wie benötigt bearbeitet.
- Die semantische Versionsnummer des Codes wird in der Variablen für die Serviceversion in der Konfigurationsdatei **hzn.json** bearbeitet.
- Der Service-Container wird neu erstellt.
- Die neue Version des Edge-Service wird signiert und in Horizon Exchange publiziert.

## Rollback-Einstellungen im Muster oder in der Bereitstellungsrichtlinie aktualisieren
{: #updating_rollback_settings}

Die Versionsnummer für einen neuen Edge-Service ist im Feld `version` der Servicedefinition angegeben.

Muster oder Bereitstellungsrichtlinien legen fest, welche Services auf welchen Edge-Knoten bereitgestellt werden. Zur Nutzung der Rollback-Funktionalität für Edge-Services müssen Sie die Referenz für Ihre neue Serviceversionsnummer im Abschnitt **serviceVersions** der Konfigurationsdatei für das Muster bzw. die Bereitstellungsrichtlinie hinzufügen.

Wenn ein Edge-Service infolge eines Musters oder einer Richtlinie auf einem Edge-Knoten bereitgestellt wird, stellt der Agent diejenige Serviceversion mit dem höchsten Prioritätswert bereit.

Beispiel:

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
      {
        "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
      {
        "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

Der Abschnitt 'priority' enthält weitere Variablen. Die Eigenschaft `priority_value` legt die Reihenfolge dafür fest, welche Serviceversion zuerst ausprobiert werden soll; praktisch bedeutet hier eine niedrigere Zahl eine höhere Priorität. Der Wert der Variablen `retries` definiert, wie häufig Horizon versucht, diese Serviceversion innerhalb des durch `retry_durations` angegebenen Zeitrahmens zu starten, bevor ein Rollback auf die nächste Version mit der höchsten Priorität stattfindet. Die Variable `retry_durations` definiert das entsprechende Zeitintervall in Sekunden. Beispielsweise führen drei Servicefehler innerhalb eines Monats nicht unbedingt zu einem Rollback des Service auf eine frühere Version, während 3 Fehler innerhalb von 5 Minuten ein Hinweis darauf sein könnten, dass eine neue Serviceversion fehlerhaft ist.

Als Nächstes müssen Sie Ihr Bereitstellungsmuster erneut publizieren oder die Bereitstellungsrichtlinie mit den Änderungen im Abschnitt **serviceVersion** in Horizon Exchange aktualisieren.

Die Kompatibilität der aktualisierten Einstellungen für die Bereitstellungsrichtlinie oder das Muster können Sie übrigens auch mit dem CLI-Befehl  `deploycheck` überprüfen. Geben Sie zum Anzeigen weiterer Details den folgenden Befehl aus:

```bash
hzn deploycheck -h
```
{: codeblock}

Die {{site.data.keyword.ieam}}-Agbots erkennen die Änderungen am Bereitstellungsmuster bzw. der Bereitstellungsrichtlinie umgehend. Anschließend kontaktieren die Agbots die einzelnen Agenten, deren Edge-Knoten entweder zur Ausführung dieses Bereitstellungsmusters registriert wurde oder mit der aktualisierten Bereitstellungsrichtlinie kompatibel ist. Der Agbot und der Agent koordinieren den Download der neuen Container, stoppen und entfernen die alten Container und starten die neuen Container.

Im Ergebnis werden alle für die Ausführung des aktualisierten Bereitstellungsmusters registrierten oder mit der Bereitstellungsrichtlinie kompatiblen Edge-Knoten schnell auf die Ausführung der neuen Version für den Edge-Service umgestellt. Dabei spielt es keine Rolle, an welchem geografischen Standort sich der jeweilige Edge-Knoten befindet.

## Fortschritt für die Implementierung der neuen Serviceversion anzeigen
{: #viewing_rollback_progress}

Fragen Sie wiederholt die Vereinbarungen für die Einheiten ab, bis die Felder `agreement_finalized_time` und `agreement_execution_start_time` Werte enthalten: 

```bash
        hzn agreement list
        ```
{: codeblock}

Dabei ist zu beachten, dass die aufgeführte Vereinbarung die Version zeigt, die dem Service zugeordnet ist, und dass die Werte für Datum/Uhrzeit in den Variablen (z. B. "agreement_creation_time": "",) angezeigt werden.

Das Versionsfeld wird außerdem mit der neuen (und aktiven) Serviceversion mit dem höchsten Prioritätswert gefüllt:

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

Weitere Details können Sie den Ereignisprotokollen für den aktuellen Knoten entnehmen, die Sie mit dem folgenden CLI-Befehl aufrufen:

```bash
hzn eventlog list
```
{: codeblock}

Zum Ändern der Einstellungen für das Rollback von Bereitstellungsversionen können Sie außerdem auch die [Managementkonsole](../getting_started/accessing_ui.md) verwenden. Dies ist beim Erstellen einer neuen Bereitstellungsrichtlinie oder durch das Anzeigen und Bearbeiten der Details von vorhandenen Richtlinien, zu denen auch die Rollback-Einstellungen gehören, möglich. Der Begriff 'Zeitrahmen' im Rollbackabschnitt der Benutzerschnittstelle entspricht übrigens der Variablen 'retry_durations' in der CLI.
