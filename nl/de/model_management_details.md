---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Model Management-System
{: #model_management_details}

Das Model Management System (MMS) vereinfacht die Last der Artificial Intelligence (AI)-Modellverwaltung für kognitive Services, die auf Edge-Knoten ausgeführt werden. Das MMS kann auch verwendet werden, um andere Datendateitypen an Edge-Knoten zu übermitteln. Das MMS erleichtert die Speicherung, Übermittlung und Sicherheit von Modellen, Daten und anderen Metadatenpaketen, die von Edge-Services benötigt werden. Auf diese Weise können Edge-Knoten Modelle und Metadaten einfach an die Cloud senden und aus ihr empfangen.

Das MMS wird im {{site.data.keyword.edge_notm}}-Hub ({{site.data.keyword.ieam}}-Hub) und auf Edge-Knoten ausgeführt. Cloud Sync Service (CSS) stellt Modelle, Metadaten oder Daten für bestimmte Knoten oder Gruppen von Knoten innerhalb einer Organisation bereit. Nachdem die Objekte an die Edge-Knoten übergeben wurden, steht eine API zur Verfügung, mit der der Edge-Service die Modelle oder Daten von Edge Sync Service (ESS) abrufen kann.

Objekte werden von Serviceentwicklern, DevOps-Administratoren und Modellautoren in das MMS-System eingegeben. Die MMS-Komponenten ermöglichen die Integration zwischen den KI-Modelltools und den kognitiven Services, die in der Edge ausgeführt werden. Die von den Autoren fertiggestellten Modelle werden im MMS publiziert, wodurch sie sofort für Edge-Knoten verfügbar werden. Standardmäßig wird die Integrität des Modells durch das Hashing und Signieren des Modells und das anschließende Hochladen des Signatur-und Prüfschlüssels sichergestellt, bevor das Modell veröffentlicht wird. Das MMS verwendet die Signatur und den Schlüssel, um sicherzustellen, dass das hochgeladene Modell nicht manipuliert wurde. Dieselbe Prozedur wird auch verwendet, wenn das MMS-Modell das Modell auf Edge-Knoten implementiert.

{{site.data.keyword.ieam}} stellt auch eine CLI (**hzn mms**) bereit, die die Bearbeitung der Modellobjekte und ihrer Metadaten ermöglicht.

Die folgenden Diagramme zeigen den Arbeitsablauf, der mit der Entwicklung und Aktualisierung von KI-Modellen unter Verwendung von MMS verbunden ist.

### KI-Modell mit MMS entwickeln und verwenden

<img src="../images/edge/02a_Developing_AI_model_using_MMS.svg" style="margin: 3%" alt="KI-Service mit MMS entwickeln"> 

### KI-Modell mit MMS aktualisieren

<img src="../images/edge/02b_Updating_AI_model_using_MMS.svg" style="margin: 3%" alt="KI-Service mit MMS aktualisieren"> 

## Konzepte des MMS

Das MMS setzt sich aus mehreren Komponenten zusammen: CSS, ESS und Objekten.

Die CSS- und ESS-APIs stellen APIs bereit, die von Entwicklern und Administratoren für die Interaktion mit dem MMS verwendet werden. Objekte sind die Modelle für maschinelles Lernen und andere Typen von Datendateien, die auf Edge-Knoten bereitgestellt werden.

### CSS

CSS wird im {{site.data.keyword.ieam}}-Management-Hub bereitgestellt, wenn {{site.data.keyword.ieam}} installiert wird. CSS verwendet die MongoDB-Datenbank, um Objekte zu speichern und den Status jedes Edge-Knotens zu verwalten.

### ESS

ESS ist in den {{site.data.keyword.ieam}}-Agenten eingebettet, der auf dem Edge-Knoten ausgeführt wird. ESS fragt CSS kontinuierlich nach Objektaktualisierungen ab und speichert alle Objekte, die an den Knoten übergeben werden, in einer lokalen Datenbank auf dem Edge-Knoten. ESS-APIs können von Services verwendet werden, die auf dem Edge-Knoten bereitgestellt sind, um auf die Metadaten- und Daten- oder Modellobjekte zuzugreifen.

### Objekte (Metadaten und Daten)

Metadaten beschreiben Ihre Datenmodelle. Ein Objekt wird im MMS mit Metadaten und Daten oder nur mit Metadaten publiziert. In den Metadaten definieren die Felder **objectType** und **objectID** die Identität des Objekts innerhalb einer bestimmten Organisation. Diese zielbezogenen Felder legen fest, an welche Edge-Knoten das Objekt gesendet werden soll:

* **destinationOrgID**
* **destinationType**
* **destinationID**
* **destinationList**
* **destinationPolicy**

Andere Objektinformationen wie Beschreibung, Version usw. können in den Metadaten angegeben werden. Der Versionswert hat für den Synchronisationsservice keine semantische Bedeutung. Daher ist nur eine Kopie des Objekts in CSS vorhanden.

Eine Datendatei ist die Datei, die die ML-spezifische Modelldefinition enthält, die von einem kognitiven Service verwendet wird. KI-Modelldateien, Konfigurationsdateien und Binärdaten sind Beispiele für Datendateien.

### KI-Modell

Das KI (künstliche Intelligenz)-Modell ist kein MMS-spezifisches Konzept, aber ein Hauptanwendungsfall des MMS. KI-Modelle sind mathematische Darstellungen eines realistisches Prozesses, der mit der KI zusammenhängt. Kognitive Services, die die kognitiven Funktionen des Menschen nachahmen, nutzen und gebrauchen das KI-Modell. Um ein KI-Modell zu generieren, wenden Sie KI-Algorithmen auf Trainingsdaten an. Zusammenfassend lässt sich sagen, dass das KI-Modell vom MMS verteilt und von einem kognitiven Service verwendet wird, der auf einem Edge-Knoten ausgeführt wird.

## MMS-Konzepte in {{site.data.keyword.ieam}}

Spezifische Beziehungen bestehen zwischen den MMS-Konzepten und anderen Konzepten in {{site.data.keyword.ieam}}.

{{site.data.keyword.ieam}} kann einen Knoten mit einem Muster oder mit einer Richtlinie registrieren. Wenn Sie die Metadaten für ein Objekt erstellen, legen Sie das Feld **destinationType** in den Objektmetadaten auf den Musternamen von Knoten fest, die dieses Objekt empfangen sollen. Alle {{site.data.keyword.ieam}}-Knoten, die dasselbe Muster verwenden, können als zur selben Gruppe zugehörig angesehen werden. Diese Zuordnung ermöglicht es daher, Objekte auf alle Knoten eines bestimmten Typs zu richten. Das Feld **destinationID** ist mit der Knoten-ID des {{site.data.keyword.ieam}}-Edge-Knotens identisch. Wenn Sie das Metadatenfeld **destinationID** nicht festlegen, wird das Objekt an alle Knoten mit dem Muster (**destinationType**) gesendet.

Wenn Sie Metadaten für Objekte erstellen, die an Knoten übergeben werden sollen, die mit einer Richtlinie registriert sind, lassen Sie **destinationType** und **destinationID** leer und legen Sie stattdessen das Feld **destinationPolicy** fest. Es enthält die Zielinformationen (Richtlinieneigenschaft, Bedingung und Service), die definieren, welche Knoten das Objekt empfangen. Legen Sie die Felder für **services** fest, um anzugeben, welcher Service das Objekt verarbeitet. Die Felder **properties** und **constraints** sind optional und werden verwendet, um weiter einzugrenzen, welche Knoten das Objekt empfangen sollen.

Auf einem Edge-Knoten können mehrere Services ausgeführt werden, die von unterschiedlichen Identitäten entwickelt worden sein können. Die {{site.data.keyword.ieam}}-Schicht für Agentenauthentifizierung und -autorisierung steuert, welche Services auf ein bestimmtes Objekt zugreifen können. Über Richtlinien bereitgestellte Objekte sind nur für die Services sichtbar, die in **destinationPolicy** referenziert werden. Für Objekte, die auf Knoten bereitgestellt sind, auf denen ein Muster ausgeführt wird, ist diese Isolationsstufe jedoch nicht verfügbar. Auf einem Knoten, der ein Muster verwendet, sind alle Objekte, die an diesen Knoten übermittelt werden, für alle Services auf dem Knoten sichtbar.

## CLI-Befehle im MMS

In diesem Abschnitt werden ein MMS-Beispiel und die Verwendung einiger MMS-Befehle beschrieben.

Beispiel: Ein Benutzer betreibt drei Kameras, auf denen ein Service für maschinelles Lernen (**weaponDetector**, "Waffendetektor") bereitgestellt ist, um Personen zu identifizieren, die Waffen tragen. Dieses Modell ist bereits trainiert und der Service wird auf den Kameras ausgeführt (die als Knoten fungieren).

### MMS-Status prüfen

Bevor das Modell publiziert wird, geben Sie den Befehl **hzn mms status** aus, um den MMS-Status zu prüfen. Überprüfen Sie **heathStatus** unter **Allgemein** und **dbStatus** unter **dbHealth**. Die Werte dieser Felder sollten grün dargestellt sein, was darauf hinweist, dass CSS und die Datenbank aktiv sind.

```
$ hzn mms status {   "general": {     "nodeType": "CSS",     "healthStatus": "green",     "upTime": 21896   },   "dbHealth": {     "dbStatus": "green",     "disconnectedFromDB": false,     "dbReadFailures": 0,     "dbWriteFailures": 0   }
}
```
{: codeblock}

### MMS-Objekt erstellen

Im MMS wird die Datenmodelldatei nicht unabhängig publiziert. Das MMS benötigt eine Metadatendatei zusammen mit der Datenmodelldatei für die Publizierung und Verteilung. Die Metadatendatei konfiguriert eine Gruppe von Attributen für das Datenmodell. Das MMS speichert, verteilt und ruft die Modellobjekte basierend auf den in den Metadaten definierten Attributen ab.

Die Metadatendatei ist eine JSON-Datei.

1. So können Sie eine Vorlage der Metadatendatei anzeigen:

   ```
   hzn mms object new
   ```
   {: codeblock}
2. Kopieren Sie die Vorlage in eine Datei mit dem Namen **my_metadata.json**:

   ```
   hzn mms object new >> my_metadata.json
   ```
   {: codeblock}

   Alternativ können Sie die Vorlage aus dem Terminal kopieren und in eine Datei einfügen.

Es ist wichtig, die Bedeutung der Metadatenfelder zu kennen und zu verstehen, wie sie sich auf das Metadatenbeispiel beziehen.

|Feld|Beschreibung|Anmerkungen|
|-----|-----------|-----|
|**objectID**|Die Objekt-ID.|Eine erforderliche eindeutige Kennung des Objekts innerhalb Ihrer Organisation.|
|**objectType**|Der Objekttyp.|Ein erforderliches Feld, das vom Benutzer definiert wird. Es gibt keine integrierten Objekttypen.|
|**destinationOrgID**|Die Zielorganisation.|Ein erforderliches Feld, das verwendet wird, um das Objekt an Knoten innerhalb derselben Organisation zu verteilen.|
|**destinationType**|Der Zieltyp.|Das Muster, das von Knoten verwendet wird, die dieses Objekt empfangen sollen.|
|**destinationID**|Die Ziel-ID.|Ein Wahlfeld, das auf die ID des Einzelknotens (ohne Organisationspräfix) gesetzt ist, auf dem das Objekt angeordnet werden soll. Wird kein Wert angegeben, so wird das Objekt an alle Knoten mit dem Zieltyp (destinationType) gesendet.|
|**destinationsList**|Die Zieladressenliste.|Ein Wahlfeld, das auf ein Array von Muster/Knoten-ID-Paaren gesetzt ist, die dieses Objekt empfangen sollen. Dies ist eine Alternative zum Festlegen von **destinationType** und **destinationID**.|
|**destinationPolicy**|Die Zielrichtlinie.|Sie wird beim Verteilen des Objekts an Knoten verwendet, die mit Richtlinie registriert sind. Legen Sie in diesem Fall **destinationType**, **destinationID** oder **destinationsList** nicht fest.|
|**expiration**|Ein Wahlfeld.|Es gibt an, wann das Objekt abläuft und aus dem MMS entfernt werden soll.|
|**activationTime**|Ein Wahlfeld.|Das Datum, an dem dieses Objekt automatisch aktiviert werden soll. Erst nach der Aktivierungszeit wird es an Knoten übermittelt.|
|**version**|Ein Wahlfeld.|Ein beliebiger Zeichenfolgewert. Der Wert wird nicht semantisch interpretiert. Im Model Management-System werden nicht mehrere Versionen eines Objekts aufbewahrt.| 
|**description**|Ein Wahlfeld.|Eine beliebige Beschreibung.|

Hinweise:

1. Wenn **destinationPolicy** verwendet wird, entfernen Sie die Felder **destinationType**, **destinationID** und **destinationsList** für Zieltyp, Ziel-ID und Zielliste in den Metadaten. Die Felder für Eigenschaften, Bedingungen und Services (**properties**, **constraints** und **services**) in der Zielrichtlinie **destinationPolicy** bestimmen die Ziele, an denen das Objekt empfangen wird.
2. Version und Beschreibung (**version** und **description**) können als Zeichenfolgen in den Metadaten angegeben werden. Der Wert der Version wird nicht semantisch interpretiert. Das MMS bewahrt nicht mehrere Versionen eines Objekts auf.
3. Ablauf und Aktivierungszeit (**expiration** und **activationTime**) sollten im RFC3339-Format angegeben werden.

Füllen Sie die Felder in der Datei **my_metadata.json** aus, indem Sie eine der folgenden beiden Optionen verwenden:

1. Senden Sie das MMS-Objekt an die Edge-Knoten, die mit Richtlinie ausgeführt werden.

   In diesem Beispiel sind die Kamera-Edge-Knoten 'node1', 'node2' und 'node3' bei der Richtlinie registriert. Der Service **weaponDetector** ist einer der Services, die auf den Knoten ausgeführt werden, und Sie möchten, dass Ihre Modelldatei von dem Service **weaponDetector** verwendet wird, der auf den Kamera-Edge-Knoten ausgeführt wird. Da die Zielknoten mit Richtlinie registriert sind, verwenden Sie nur **destinationOrgID** und **destinationPolicy**. Setzen Sie das Feld **ObjectType** auf **model**. Es kann aber auch auf eine beliebige Zeichenfolge gesetzt werden, die für den Service, der das Objekt abruft, aussagekräftig ist.

   In diesem Szenario kann die Metadatendatei folgendermaßen aussehen:

   ```json
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationPolicy": {        "properties": [],        "constraints": [],        "services": [          {            "orgID": "$SERVICE_ORG_ID",            "arch": "$ARCH",            "serviceName": "weaponDetector",            "version": "$VERSION"          }        ]      },      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

2. Senden Sie das MMS-Objekt an die Edge-Knoten, die mit Muster ausgeführt werden.

   In diesem Szenario werden dieselben Knoten verwendet, aber jetzt werden sie mit dem Muster **pattern.weapon-detector** registriert, das **weaponDetector** als einen der Services hat.

   Um das Modell an die Knoten mit Muster zu senden, ändern Sie die Metadatendatei:

   1. Geben Sie das Knotenmuster im Feld **destinationType** an.
   2. Entfernen Sie das Feld **destinationPolicy**.

   Die Metadatendatei sieht etwa wie folgt aus:

   ```
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationType": "pattern.weapon-detector",      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

Jetzt sind die Modelldatei und die Metadatendatei bereit für die Publizierung.

### MMS-Objekt publizieren

Publizieren Sie das Objekt sowohl mit der Metadatendatei als auch mit der Datendatei:

```
hzn mms object publish -m my_metadata.json -f my_model
```
{: codeblock}

### MMS-Objekt auflisten

Listen Sie das MMS-Objekt mit dieser Objekt-ID (**objectID**) und diesem Objekttyp (**objectType**) innerhalb der relevanten Organisation auf:

```
hzn mms object list --objectType=model --objectId=my_model
```
{: codeblock}

Das Ergebnis des Befehls sieht etwa wie folgt aus:

```
Listing objects in org userdev: [   {     "objectID": "my_model",     "objectType": "model"   }
]
```

Um alle MMS-Objektmetadaten anzuzeigen, fügen Sie **-l** zum Befehl hinzu:

```
hzn mms object list --objectType=model --objectId=my_model -l
```
{: codeblock}

Um Objektstatus und Ziele zusammen mit dem Objekt anzuzeigen, fügen Sie dem Befehl **-d** hinzu. Das folgende Zielergebnis zeigt an, dass das Objekt an die Kameras übergeben wird: node1, node2 und node3.

```
hzn mms object list --objectType=model --objectId=my_model -d
```
{: codeblock}

Die Ausgabe des vorherigen Befehls sieht wie folgt aus:

```
[   {     "objectID": "my_model",     "objectType": "model",     "destinations": [       {         "destinationType": "pattern.mask-detector",         "destinationID": "node1",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node2",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node3",         "status": "delivered",         "message": ""       },     ],     "objectStatus": "ready"   }
]
```

Es stehen noch weitere erweiterte Filteroptionen zur Verfügung, um die MMS-Objektliste einzugrenzen. So können Sie eine vollständige Liste der Flags anzeigen:

```
hzn mms object list --help
```
{: codeblock}

### MMS-Objekt löschen

Löschen Sie das MMS-Objekt:

```
hzn mms object delete --type=model --id=my_model
```
{: codeblock}

Das Objekt wird aus dem MMS entfernt.

### MMS-Objekt aktualisieren

Modelle können sich im Laufe der Zeit ändern. Um ein aktualisiertes Modell zu publizieren, verwenden Sie **hzn mms object publish** zusammen mit derselben Metadatendatei (empfohlen wird der Versionswert **upgrade**). Mit dem MMS ist es nicht nötig, die Modelle für alle drei Kameras nacheinander zu aktualisieren. Verwenden Sie diese Option, um das Objekt **my_model** auf allen drei Knoten zu aktualisieren.

```
hzn mms object publish -m my_metadata.json -f my_updated_model
```
{: codeblock}

## Anhang

Hinweis: Weitere Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../getting_started/document_conventions.md).

Im Folgenden sehen Sie ein Beispiel für die Ausgabe des Befehls **hzn mms object new**, der zum Generieren einer Vorlage der MMS-Objektmetadaten verwendet wird:

```
{     "objectID": "",            /* Erforderlich: eine eindeutige ID des Objekts. */   "objectType": "",          /* Erforderlich: der Typ des Objekts. */   "destinationOrgID": "$HZN_ORG_ID", /* Erforderlich: Die Organisations-ID des Objekts (ein Objekt gehört zu genau einer Organisation). */   "destinationID": "",       /* Die Knoten-ID (ohne Organisationspräfix), an der das Objekt angeordnet werden soll. */                              /* Wenn ausgelassen, wird das Objekt an alle Knoten mit demselben 'destinationType' gesendet. */                              /* Dieses Feld löschen, wenn Sie 'destinationPolicy' verwenden. */   "destinationType": "",     /* Das Muster, das von Knoten verwendet wird, die dieses Objekt empfangen sollen. */                              /* Wenn ausgelassen (und auch 'destinationsList' ausgelassen), wird dieses Objekt an alle bekannten Knoten gesendet. */                              /* Dieses Feld löschen, wenn Sie eine Richtlinie verwenden. */   "destinationsList": null,  /* Die Liste von Zielen als Array von Muster/Knoten-Paaren, die dieses Objekt empfangen sollen. */                              /* Wenn angegeben, müssen 'destinationType' und 'destinationID' ausgelassen werden. */                              /* Dieses Feld löschen, wenn Sie eine Richtlinie verwenden. */   "destinationPolicy": {     /* Die Richtlinienspezifikation, die zur Verteilung dieses Objekts verwendet werden soll. */                              /* Diese Felder löschen, wenn der Zielknoten ein Muster verwendet. */     "properties": [          /* Eine Liste von Richtlinieneigenschaften, die das Objekt beschreiben. */       {         "name": "",         "value": null,         "type": ""           /* Gültige Typen sind Zeichenfolge, boolescher Wert, Ganzzahl, Gleitkomma, Liste von Zeichenfolgen (durch Kommas getrennt), Version. */                              /* Typ kann ausgelassen werden, wenn er vom Wert unterscheidbar ist; z. B. ist true ohne Anführungszeichen ein boolescher Wert. */       }     ],     "constraints": [         /* Eine Liste von Bedingungsausdrücken im Format <property name> <operator> <property value>, getrennt durch die booleschen Operatoren AND (&&) oder OR (||). */       ""     ],     "services": [            /* Der oder die Services, die dieses Objekt verwenden werden. */       {         "orgID": "",         /* Die Organisation des Service. */         "serviceName": "",   /* Der Name des Service. */         "arch": "",          /* Auf '*' festlegen, um Services einer beliebigen Hardwarearchitektur anzugeben. */         "version": ""        /* Ein Versionsbereich. */       }     ]   },   "expiration": "",          /* Eine Zeitmarke/ein Datum, die bzw. das angibt, wann das Objekt abläuft (es wird automatisch gelöscht). Die Zeitmarke muss im RFC3339-Format angegeben werden.  */   "version": "",             /* Beliebiger Zeichenfolgewert. Der Wert wird nicht semantisch interpretiert. Im Model Management-System werden nicht mehrere Versionen eines Objekts aufbewahrt. */   "description": "",         /* Eine beliebige Beschreibung. */   "activationTime": ""       /* Eine Zeitmarke/ein Datum, an der bzw. dem dieses Objekt automatisch aktiviert werden soll. Die Zeitmarke muss im RFC3339-Format angegeben werden. */ }
```
{: codeblock}

## Beispiel
{: #mms}

In diesem Beispiel erfahren Sie, wie Sie einen {{site.data.keyword.edge_service}} entwickeln, der das Model Management System (MMS) verwendet. Sie können dieses System verwenden, um die lernenden Maschinenmodelle bereitzustellen und zu aktualisieren, die von den auf Ihren Edge-Knoten ausgeführten Edge-Services verwendet werden.
{:shortdesc}

Ein Beispiel, das MMS verwendet, finden Sie im Abschnitt [Horizon Hello Model Management Service (MMS)-Beispiel-Edge-Service](https://github.com/open-horizon/examples/tree/master/edge/services/helloMMS).

## Vorbereitende Schritte
{: #mms_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Vorgehensweise
{: #mms_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Folgen Sie den Schritten im Abschnitt [Eigenen Hello MMS-Edge-Service erstellen](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) und kehren Sie dann hierher zurück.

## Nächste Schritte
{: #mms_what_next}

* Unter [Edge-Service für Einheiten entwickeln](developing.md) finden Sie weitere Beispiele für Edge-Services, mit denen Sie arbeiten können.

## Weiterführende Informationen

* ['Hello World' mit Model Management](model_management_system.md)
