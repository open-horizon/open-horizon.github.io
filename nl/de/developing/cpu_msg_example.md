---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Service zum Senden von Daten zur CPU-Belastung an {{site.data.keyword.message_hub_notm}}
{: #cpu_msg_ex}

In diesem Beispiel werden Daten zum Prozentsatz der CPU-Belastung erfasst, um an {{site.data.keyword.message_hub_notm}} gesendet zu werden. Mithilfe dieses Beispiels können Sie eigene Edge-Anwendungen entwickeln, mit denen Daten an Cloud-Services gesendet werden können.
{:shortdesc}

## Vorbereitende Schritte
{: #cpu_msg_begin}

Führen Sie die vorausgesetzten Schritte unter [Erstellung eines Edge-Service vorbereiten](service_containers.md) aus. Danach sollten die folgenden Umgebungsvariablen definiert, die folgenden Befehle installiert und die folgenden Dateien vorhanden sein:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Vorgehensweise
{: #cpu_msg_procedure}

Dieses Beispiel ist Teil des Open-Source-Projekts [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Führen Sie die Schritte im Abschnitt [Erstellen und Veröffentlichen Ihrer eigenen Version der CPU für IBM Event Streams Edge Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service) aus und kehren Sie dann hierher zurück.

## Die Lerninhalte des vorstehenden Beispiels

### Erforderliche Services

Der Edge-Service 'cpu2evtstreams' ist ein Beispiel für einen Service, der von zwei anderen Edge-Services (**cpu** und **gps**) abhängig ist, damit er seine Tasks ausführen kann. Die Details für diese Abhängigkeiten können Sie im Abschnitt **requiredServices** der Datei **horizon/service.definition.json** sehen, der im Folgenden dargestellt ist:

```json
    "requiredServices": [         {
            "url": "ibm.cpu",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"         }
    ],
```
{: codeblock}

### Konfigurationsvariablen
{: #cpu_msg_config_var}

Zur Nutzung des Service **cpu2evtstreams** müssen vorab bestimmte Konfigurationsmaßnahmen ausgeführt werden. Edge-Services können Konfigurationsvariablen deklarieren, wobei der Typ der Konfigurationsvariablen angegeben wird und die entsprechenden Standardwerte definiert werden. Diese Konfigurationsvariablen werden im Abschnitt **userInput** der Datei **horizon/service.definition.json** dargestellt:

```json  
    "userInput": [         {
            "name": "EVTSTREAMS_API_KEY",             "label": "Der API-Schlüssel, der zum Senden von Daten an Ihre Instanz von IBM Event Streams verwendet wird",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",             "label": "Eine durch Kommas getrennte Liste der URLs, die zum Senden von Nachrichten an Ihre Instanz von IBM Event Streams verwendet werden sollen",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",             "label": "Das in base64 codierte selbst signierte Zertifikat, das zum Senden von Nachrichten an die ICP-Instanz von IBM Event Streams verwendet wird. Nicht erforderlich für IBM Cloud Event Streams.",             "type": "string",             "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",             "label": "Das Thema, das zum Senden von Daten an Ihre Instanz von IBM Event Streams verwendet wird",             "type": "string",             "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",             "label": "Die Anzahl der Stichproben, die gelesen werden, bevor der Durchschnitt berechnet wird",             "type": "int",             "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",             "label": "Die Anzahl der Sekunden zwischen den einzelnen Stichproben",             "type": "int",             "defaultValue": "2"
        },
        {
            "name": "MOCK",             "label": "CPU-Stichprobenentnahme simulieren",             "type": "boolean",             "defaultValue": "false"
        },
        {
            "name": "PUBLISH",             "label": "CPU-Stichproben in IBM Event Streams publizieren",             "type": "boolean",             "defaultValue": "true"
        },
        {
            "name": "VERBOSE",             "label": "Alle Ereignisse protokollieren",             "type": "string",             "defaultValue": "1"         }
    ],
```
{: codeblock}

Konfigurationsvariablen für die Benutzereingabe wie diese sind erforderlich, um über die benötigten Werte zu verfügen, wenn der Edge-Service auf dem Edge-Knoten gestartet wird. Die Werte können aus einer der folgenden Quellen (in der angegebenen Rangfolge) stammen:

1. Einer mit dem Flag **hzn register -f** angegebene Benutzereingabedatei
2. Dem Abschnitt **userInput** der Edge-Knoten-Ressource im Exchange
3. Dem Abschnitt **userInput** der Muster- oder Bereitstellungsrichtlinienressource im Exchange
4. Dem in der Servicedefinitionsressource im Exchange angegebenen Standardwert

Bei der Registrierung Ihrer Edge-Einheit für diesen Service haben Sie eine Datei **userinput.json** angegeben, die einige der Konfigurationsvariablen enthält, die keine Standardwerte aufweisen.

### Tipps zur Entwicklung
{: #cpu_msg_dev_tips}

Es kann hilfreich sein, Konfigurationsvariablen in Ihren Service zu integrieren, die das Testen und Debuggen des Service unterstützen. So verwenden z. B. die Metadaten dieses Service (**service.definition.json**) und der Code (**service.sh**) die folgenden Konfigurationsvariablen:

* Mit **VERBOSE** kann die Menge der Informationen erhöht werden, die während der Ausführung protokolliert werden
* **PUBLISH** steuert, ob der Code Nachrichten an {{site.data.keyword.message_hub_notm}} senden soll
* **MOCK** steuert, ob **service.sh** versucht, Aufrufe an die REST-APIs der zugehörigen Abhängigkeiten (Services **cpu** und **gps**) abzusetzen, oder stattdessen selbst Testdaten erstellt.

Die Möglichkeit zum Testen der Services, von denen Sie abhängig sind, ist optional. Bei der Entwicklung und beim Testen von Komponenten in Isolation von erforderlichen Services kann sie jedoch hilfreich sein. Dieser Ansatz kann auch die Entwicklung eines Service auf einem Einheitentyp ermöglichen, auf dem keine Hardwaresensoren oder Aktuatoren vorhanden sind.

Die Möglichkeit zum Inaktivieren der Interaktion mit Cloud-Services kann während der Entwicklungs- und Testphase nützlich sein, um z. B. unnötige Gebühren zu vermeiden und Tests in einer synthetischen DevOps-Umgebung zu erleichtern.

## Nächste Schritte
{: #cpu_msg_what_next}

* Versuchen Sie andere Beispiele für Edge Services unter [Entwicklung von Edge Services mit {{site.data.keyword.edge_notm}}](../OH/docs/developing/developing.md).
