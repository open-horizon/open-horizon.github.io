---

copyright:
  years: 2020
lastupdated: "2020-04-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Anwendungsfälle für Bereitstellungsrichtlinien
{: #developing_edge_services}

In diesem Abschnitt wird ein realistisches Szenario beleuchtet, in dem die verschiedenen Richtlinientypen beschrieben werden.

<img src="../../images/edge/04_Defining_an_edge_policy.svg" width="90%" alt="Edge-Richtlinie definieren">

Angenommen, ein Kunde hat an seinen Geldautomaten Sicherungskameras installiert (und er hat außerdem noch andere Typen von Edge-Knoten). Der Kunde verwendet sowohl für Fußgänger erreichbare Automaten als auch solche, an die man mit dem Auto heranfahren kann ("drive-through"). In diesem Fall sind zwei Services von Drittanbietern verfügbar. Beide Services können verdächtige Aktivitäten an den Geldautomaten erkennen, aber der Kunde hat in einer Prüfung festgestellt, dass der Service 'atm1' verdächtige Aktivitäten an fußläufig erreichbaren Geldautomaten zuverlässiger erkennt, Service 'atm2' hingegen an den Drive-through-Geldautomaten.

Die Richtlinie zum Erreichen der gewünschten Service- und Modellbereitstellung wird folgendermaßen ausgedrückt:

* Legen Sie die Eigenschaften in der Knotenrichtlinie für alle fußläufig erreichbaren ("walk-up") Geldautomaten fest: properties: `sensor: camera`, `atm-type: walk-up`
* Legen Sie die Eigenschaften in der Knotenrichtlinie für alle Drive-through-Geldautomaten ("drive-through atms") fest: properties: `sensor: camera`, `atm-type: drive-thru`
* Legen Sie die Eigenschaften in der Servicerichtlinie von Drittanbieter-Entwicklern sowohl für 'atm1' als auch für 'atm2' fest: constraints: `sensor == camera`
* Legen Sie Bedingungen in der Bereitstellungsrichtlinie fest, die der Kunde für den Service 'atm1' festgelegt hat: constraints: `atm-type == walk-up`
* Legen Sie Bedingungen in der Bereitstellungsrichtlinie fest, die der Kunde für den Service 'atm2' festgelegt hat: constraints: `atm-type == drive-thru`

Hinweis: Der Befehl `hzn` verwendet in Bezug auf die Bereitstellungsrichtlinie zuweilen den Begriff 'Geschäftsrichtlinie'.

Die Knotenrichtlinie (von dem Techniker festgelegt, der die Geldautomaten einrichtet) gibt Fakten zu jedem Knoten an, z. B. ob der Geldautomat eine Kamera hat, und den Positionstyp des Geldautomaten. Diese Informationen sind für den Techniker leicht zu ermitteln und anzugeben.

Die Servicerichtlinie ist eine Anweisung darüber, was für den Service erforderlich ist, um ordnungsgemäß zu arbeiten (in diesem Fall eine Kamera). Der Entwickler des Drittanbieter-Service kennt diese Informationen, auch wenn er nicht weiß, welcher Kunde sie verwendet. Wenn der Kunde weitere Geldautomaten ohne Kameras hat, werden diese Services an diesen Geldautomaten aufgrund dieser Bedingung nicht bereitgestellt.

Die Bereitstellungsrichtlinie wird vom IT-Leiter des Kunden definiert (bzw. demjenigen, der seine Edge-Fabric verwaltet). Damit wird die gesamte Servicebereitstellung für das Geschäft definiert. In diesem Fall drückt der IT-Leiter das gewünschte Ergebnis der Servicebereitstellung aus, dass 'atm1' für fußläufig erreichbare Geldautomaten und 'atm2' für Drive-through-Geldautomaten verwendet werden soll.

## Knotenrichtlinie
{: #node_policy}

Die Richtlinie kann an einen Knoten angehängt werden. Der Knoteneigner kann dies zum Registrierungszeitpunkt angeben und jederzeit direkt auf dem Knoten oder zentral durch einen {{site.data.keyword.edge_devices_notm}}-Administrator ändern lassen. Wenn die Knotenrichtlinie zentral geändert wird, wird sie beim nächsten Überwachungssignal des Knotens an den Management-Hub vom Knoten übernommen. Wenn die Knotenrichtlinie direkt auf dem Knoten geändert wird, werden die Änderungen sofort vom Management-Hub übernommen, sodass der Service und die Modellbereitstelllung sofort neu bewertet werden können. Ein Knoten verfügt standardmäßig über einige [integrierte Eigenschaften](#node_builtins), die Arbeitsspeicher, Architektur und Anzahl der CPUs widerspiegeln. Er kann optional beliebige Eigenschaften enthalten, z. B. Produktmodell, angeschlossene Einheiten, Softwarekonfiguration oder andere Eigenschaften, die vom Knoteneigner als relevant erachtet werden. Bedingungen für die Knotenrichtlinie können verwendet werden, um einzuschränken, welche Services auf diesem Knoten ausgeführt werden dürfen. Jeder Knoten hat nur eine einzige Richtlinie, die alle Eigenschaften und Bedingungen enthält, die diesem Knoten zugeordnet sind.

## Servicerichtlinie
{: #service_policy}

Hinweis: Die Funktion 'Servicerichtlinie' ist optional.

Wie Knoten können Services die Richtlinie ausdrücken und auch einige [integrierte Eigenschaften](#service_builtins) aufweisen. Diese Richtlinie wird auf einen publizierten Service in Exchange angewendet und wird vom Serviceentwickler erstellt. Die Eigenschaften der Servicerichtlinie können Merkmale des Servicecodes angeben, die für die Autoren der Knotenrichtlinien relevant sein könnten. Mit Bedingungen für Servicerichtlinien können Sie festlegen, wo und auf welchem Einheitentyp dieser Service ausgeführt werden kann. Beispielsweise kann der Serviceentwickler zusichern, dass dieser Service ein bestimmtes Hardware-Setup benötigt, wie CPU/GPU-Bedingungen, Speicherbedingungen, bestimmte Sensoren, Aktuatoren oder andere Peripheriegeräte. In der Regel bleiben Eigenschaften und Bedingungen über den Lebenszyklus des Service statisch, da sie Aspekte der Servicebereitstellung beschreiben. In erwarteten Anwendungsszenarios fällt eine Änderung an einem dieser Szenarien meist mit Codeänderungen zusammen, die eine neue Serviceversion erforderlich machen. Bereitstellungsrichtlinien werden verwendet, um die dynamischeren Aspekte der Servicebereitstellung zu erfassen, die sich aus den Geschäftsanforderungen ergeben.

## Bereitstellungsrichtlinie
{: #deployment_policy}

Die Bereitstellungsrichtlinie steuert die Servicebereitstellung. Wie die anderen Richtlinientypen enthält sie eine Reihe von Eigenschaften und Bedingungen, aber auch andere Dinge. So gibt sie beispielsweise explizit einen Service an, der bereitgestellt werden soll, und kann optional Werte von Konfigurationsvariablen, Rollback-Versionen von Services und Konfigurationsinformationen zum Knotenzustand enthalten. Der Ansatz der Bereitstellungsrichtlinie für Konfigurationswerte ist leistungsfähig, da diese Operation zentral durchgeführt werden kann, ohne dass eine direkte Verbindung zum Edge-Knoten hergestellt werden muss.

Administratoren können eine Bereitstellungsrichtlinie erstellen, die dann von {{site.data.keyword.edge_devices_notm}} verwendet wird, um alle Einheiten zu finden, die mit den definierten Bedingungen übereinstimmen, und den angegebenen Service auf denjenigen Einheiten bereitzustellen, die die in der Richtlinie konfigurierten Servicevariablen verwenden. Die Service-Rollbackversionen informieren {{site.data.keyword.edge_devices_notm}} darüber, welche Serviceversionen bereitzustellen sind, wenn die Bereitstellung einer höheren Version des Service fehlschlägt. Die Knotenzustandskonfiguration gibt an, wie {{site.data.keyword.edge_devices_notm}} den Zustand eines Knotens messen sollte (mit Überwachungssignalen und Management-Hub-Kommunikation), bevor festgestellt wird, ob der Knoten außerhalb der Richtlinienbedingungen liegt.

Da Bereitstellungsrichtlinien die dynamischeren, geschäftsähnlichen Serviceeigenschaften und -bedingungen erfassen, wird erwartet, dass sie sich häufiger ändern als eine Servicerichtlinie. Ihr Lebenszyklus ist unabhängig von dem Service, auf den sie sich beziehen. Dies gibt dem Richtlinienadministrator die Möglichkeit, eine bestimmte Serviceversion oder einen Versionsbereich zu definieren. Anschließend führt {{site.data.keyword.edge_devices_notm}} die Servicerichtlinie und die Bereitstellungsrichtlinie zusammen und versucht dann, Knoten zu finden, deren Richtlinie damit kompatibel ist.

## Modellrichtlinie
{: #model_policy}

Für Services, die auf maschinellem Lernen basieren, sind bestimmte Modelltypen erforderlich, um ordnungsgemäß zu arbeiten, und {{site.data.keyword.edge_devices_notm}}-Kunden müssen in der Lage sein, bestimmte Modelle auf denselben oder einer Untergruppe von Knoten, auf denen diese Services angeordnet wurden, anzuordnen. Der Zweck der Modellrichtlinie besteht darin, die Gruppe der Knoten, in denen ein bestimmter Service bereitgestellt ist, weiter einzugrenzen, wodurch eine Untergruppe dieser Knoten über ['Hello World' mit Model Management](../developing/model_management_system.md) ein bestimmtes Modellobjekt empfangen kann.

## Erweiterter Anwendungsfall für Richtlinien
{: #extended_policy_use_case}

In dem Beispiel mit den Geldautomaten betreibt der Kunde fußläufig erreichbare Geldautomaten an ländlichen Standorten, die selten aufgesucht werden. Der Kunde möchte nicht, dass die Geldautomaten an den ländlichen Standorten kontinuierlich laufen, und auch nicht, dass sie sich jedes Mal einschalten, wenn ein Objekt in der Nähe wahrgenommen wird. Deshalb fügt der Serviceentwickler dem Service 'atm1' ein ML-Modell hinzu, das den Geldautomaten einschaltet, wenn eine sich nähernde Person wahrgenommen wird. Um das ML-Modell gezielt an diesen ländlichen Geldautomaten bereitzustellen, konfiguriert der Entwickler die Richtlinie:

* Knotenrichtlinie für fußläufig erreichbare Geldautomaten ("walk-up atms"): properties: `sensor: camera`, `atm-type: walk-up`, `location: rural`
* Die Bedingungen für Servicerichtlinien, die von den Drittanbieter-Entwicklern für 'atm1' festgelegt wurden, bleiben unverändert: constraints: `sensor == camera`
* Auch die Bereitstellungsrichtlinie, die vom Kunden für den Service 'atm1' festgelegt wurde, bleibt unverändert: constraints: `atm-type == walk-up`
* Die Bedingungen der Modellrichtlinie werden von Drittanbieter-Entwicklern im MMS-Objekt für den Service 'atm1' festgelegt:

```
"destinationPolicy": {
  "constraints": [ "location == rural"  ],
  "services": [
       { "orgID": "$HZN_ORG_ID",
         "serviceName": "atm1",
         "arch": "$ARCH",  
         "version": "$VERSION"
       }
  ]
}
```
{: codeblock}

Innerhalb des MMS-Objekts deklariert die Modellrichtlinie einen Service (oder eine Liste von Services), der auf das Objekt (in diesem Fall 'atm1') zugreifen kann, und deklariert außerdem Eigenschaften und Bedingungen, die es {{site.data.keyword.edge_devices_notm}} ermöglichen, die ordnungsgemäße Anordnung des Objekts auf den Geldautomaten an den ländlichen Standorten weiter einzuengen. Andere Services, die auf dem Geldautomaten ausgeführt werden, können nicht auf das Objekt zugreifen.

## Eigenschaften
{: #properties}

Eigenschaften sind im Wesentlichen Aussagen über Fakten, die als Name/Wert-Paare ausgedrückt werden. Eigenschaften werden auch eingegeben, wodurch sich ein Weg zum Erstellen leistungsfähiger Ausdrücke bietet. Die folgenden Tabellen enthalten die von {{site.data.keyword.edge_devices_notm}} unterstützten Eigenschaftswerttypen sowie die integrierten Knoten- und Servicerichtlinien-Eigenschaften. Knoteneigner, Serviceentwickler und Bereitstellungsrichtlinien-Administratoren können einzelne Eigenschaften entsprechend ihrem Bedarf definieren. Eigenschaften müssen nicht in einem zentralen Repository definiert werden. Sie werden nach Bedarf definiert und (in Bedingungsausdrücken) referenziert.

|Akzeptierte Eigenschaftswerttypen|
|-----------------------------|
|Version - Ausdrücke in Schreibweise mit Trennzeichen, die 1, 2 oder 3 Teile unterstützen, z. B. 1.2, 2.0.12 usw.|
|Zeichenfolge *|
|Liste von Zeichenfolgen (durch Kommas getrennte Zeichenfolgen)|
|Ganze Zahl|
|Boolescher Wert|
|Gleitkomma|
{: caption="Tabelle 1. Akzeptierte Eigenschaftswerttypen"}

*Zeichenfolgewerte, die Leerzeichen enthalten, müssen in Anführungszeichen gesetzt werden.

Integrierte Eigenschaften stellen klar definierte Namen für allgemeine Eigenschaften bereit, sodass Bedingungen alle auf gleiche Weise referenzieren können. Wenn ein Service beispielsweise `x` CPUs benötigt, um ordnungsgemäß oder effizient ausgeführt zu werden, kann er die Eigenschaft `openhorizon.cpu` in seiner Bedingung verwenden. Die meisten dieser Eigenschaften können nicht festgelegt werden, sondern werden aus dem zugrundeliegenden System gelesen und ignorieren alle von einem Benutzer festgelegten Werte.

### Integrierte Knoteneigenschaften
{: #node_builtins}

|Name|Typ|Beschreibung|Richtlinientyp|
|----|----|-----------|-----------|
|openhorizon.cpu|Ganzzahl|Anzahl CPUs|Knoten|
|openhorizon.memory|Ganzzahl|Größe des Speichers in M.|Knoten|
|openhorizon.arch|Zeichenfolge|Die Hardwarearchitektur des Knotens (z. B. amd64, armv6 usw.)|Knoten|
|openhorizon.hardwareId|Zeichenfolge|Die Seriennummer der Knotenhardware, sofern sie über die Linux-API verfügbar ist; andernfalls eine kryptosichere Zufallszahl, die sich für die Lebensdauer der Knotenregistrierung nicht ändert.|Knoten|
|openhorizon.allowPrivileged|Boolescher Wert|Zulassen, dass Container privilegierte Funktionen nutzen, wie das privilegierte Ausführen oder das Anhängen des Hostnetzes an den Container.|Knoten|
{: caption="Tabelle 2. Integrierte Knoteneigenschaften"}

### Integrierte Serviceeigenschaften
{: #service_builtins}

|Name|Typ|Beschreibung|Richtlinientyp|
|----|----|-----------|-----------|
|openhorizon.service.url|Zeichenfolge|Der eindeutige Name des Service.|Service|
|openhorizon.service.org|Zeichenfolge|Die Multi-Tenant-Organisation, in der der Service definiert ist*|Service|
|openhorizon.service.version|Version|Die Version eines Service mit derselben Syntax für die semantische Version (z. B. 1.0.0)|Service|
{: caption="Tabelle 3. Integrierte Serviceeigenschaften"}

*In einer Bedingung, wenn service.url angegeben ist, aber service.org weggelassen wird, nimmt die Organisation standardmäßig den Wert der Knoten- oder Bereitstellungsrichtlinie an, von der die Bedingung definiert wird.

## Bedingungen
{: #constraints}

In {{site.data.keyword.edge_devices_notm}} können Knoten-, Service-und Bereitstellungsrichtlinien Bedingungen definieren. Bedingungen werden als Vergleichselement in einfacher Textform ausgedrückt und beziehen sich auf Eigenschaften und ihre Werte bzw. einen Bereich ihrer möglichen Werte. Bedingungen können auch boolesche Operatoren wie AND (&&), OR (||) zwischen Ausdrücken von Eigenschaft und Wert enthalten, mit denen längere Klauseln gebildet werden. Beispiel: `openhorizon.arch == amd64 && OS == Mojave`. Schließlich kann eine runde Klammer verwendet werden, um eine Bewertungsrangfolge innerhalb eines einzelnen Ausdrucks zu erstellen.

|Eigenschaftswerttyp|Unterstützte Operatoren|
|-------------------|-------------------|
|Ganze Zahl|==, <, >, <=, >=, =, !=|
|Zeichenfolge*|==, !=, =|
|Liste von Zeichenfolgen|in|
|Boolescher Wert|==, =|
|Version|==, =, in**|
{: caption="Tabelle 4. Bedingungen"}

*Bei Zeichenfolgetypen eine Zeichenfolge in Anführungszeichen, in die eine Liste mit durch Kommas getrennten Zeichenfolgen eingeschlossen ist; geben Sie eine Liste der zulässigen Werte an. Zum Beispiel wird `hello == "beautiful, world"` wahr, wenn "hello" "beautiful" oder "world" ist.

**Bei einem Versionsbereich verwenden Sie `in` anstelle von `==`.

## Noch weiter erweiterter Anwendungsfall für Richtlinien
{: #extended_policy_use_case_more}

Um die volle Leistung der bidirektionalen Natur der Richtlinie zu veranschaulichen, berücksichtigen Sie das Praxisbeispiel in diesem Abschnitt und fügen Sie dem Knoten einige Bedingungen hinzu. In unserem Beispiel heißt dies: Einige der ländlichen, fußläufig erreichbaren Geldautomaten stehen in der Nähe eines Gewässers, das Reflexionen erzeugt. Diese kann der vorhandene Service 'atm1', der von den anderen fußläufig erreichbaren Geldautomaten verwendet wird, nicht verarbeiten. Dies erfordert einen dritten Service, der die Reflexionen für diese wenigen Geldautomaten besser handhaben kann, und eine Richtlinie, die wie folgt konfiguriert ist:

* Knotenrichtlinie für fußläufig erreichbare Geldautomaten in Wassernähe: properties: `sensor: camera`, `atm-type: walk-up`; constraints: `feature == glare-correction`
* Servicerichtlinie, die von Drittanbieter-Entwicklern für 'atm3' festgelegt wurde: constraints: `sensor == camera`
* Bereitstellungsrichtlinie, die vom Kunden für den Service 'atm3' festgelegt wurde: constraints: `atm-type == walk-up`; properties: `feature: glare-correction`  

Auch hier gibt die Knotenrichtlinie die Fakten zum Knoten an. In diesem Fall hat jedoch der Techniker, der die Geldautomaten in Wassernähe eingerichtet hat, eine Bedingung angegeben, dass der Service, der auf diesem Knoten bereitgestellt werden soll, über die Funktion für Reflexionskorrektur verfügen muss.

Die Servicerichtlinie für 'atm3' hat dieselbe Bedingungen wie die anderen, was eine Kamera für den Geldautomaten erforderlich macht.

Da der Kunde weiß, dass der Service 'atm3' die Reflexion besser verarbeiten kann, legt er diese Bedingung in der mit 'atm3' verknüpften Bereitstellungsrichtlinie fest, was die für den Knoten festgelegte Eigenschaft erfüllt und dazu führt, dass Ergebnisse in diesem Service auf den Geldautomaten in Wassernähe bereitgestellt werden.

## Richtlinienbefehle
{: #policy_commands}

|Befehl|Beschreibung|
|-------|-----------|
|`hzn policy list`|Die Richtlinie dieses Edge-Knotens.|
|`hzn policy new`|Eine leere Vorlage für eine Knotenrichtlinie, die ausgefüllt werden kann.|
|hzn policy update --input-file=INPUT-FILE|Aktualisiert die Richtlinie des Knotens. Die integrierten Eigenschaften des Knotens werden automatisch hinzugefügt, wenn sie nicht in der Eingaberichtlinie enthalten sind.|
|`hzn policy remove [<flags>]`|Entfernt die Richtlinie des Knotens. |
|`hzn exchange node listpolicy [<flags>`] <node>|Zeigt die Knotenrichtlinie in Horizon Exchange an.|
|`hzn exchange node addpolicy --json-file=JSON-FILE [<flags>`] <node>|Fügt die Knotenrichtlinie in Horizon Exchange hinzu oder ersetzt sie.|
|`hzn exchange node updatepolicy --json-file=JSON-FILE [<flags>`] <node>|Aktualisiert ein Attribut der Richtlinie für diesen Knoten in Horizon Exchange.|
|`hzn exchange node removepolicy [<flags>`] <node>|Entfernt die Knotenrichtlinie in Horizon Exchange.|
|`hzn exchange service listpolicy [<flags>`] <service>|Zeigt die Servicerichtlinie in Horizon Exchange an.|
|`hzn exchange service newpolicy|Zeigt eine leere Vorlage für eine Servicerichtlinie an, die mit Daten gefüllt werden kann.|
|`hzn exchange service addpolicy --json-file=JSON-FILE [<flags>`] <service>|Fügt die Servicerichtlinie in Horizon Exchange hinzu oder ersetzt sie.|
|`hzn exchange service removepolicy [<flags>`] <service>|Entfernt die Servicerichtlinie in Horizon Exchange.|
|`hzn exchange business listpolicy [<flags>] [<policy>]`|Zeigt die Geschäftsrichtlinien in Horizon Exchange an.|
|`hzn exchange business new`|Zeigt eine leere Vorlage für eine Bereitstellungsrichtlinie an, die mit Daten gefüllt werden kann.|
|`hzn exchange business addpolicy --json-file=JSON-FILE [<flags>`] <policy>|Fügt eine Bereitstellungsrichtlinie in Horizon Exchange hinzu oder ersetzt sie. Verwenden Sie 'hzn exchange business new' für eine leere Bereitstellungsrichtlinienvorlage.|
|`hzn exchange business updatepolicy --json-file=JSON-FILE [<flags>`] <policy>|Aktualisiert ein Attribut einer vorhandenen Bereitstellungsrichtlinie in Horizon Exchange. Die unterstützten Attribute sind Attribute der obersten Ebene in der Richtliniendefinition; dies wird beim Absetzen des Befehls 'hzn exchange business new' angezeigt.|
|`hzn exchange business removepolicy [<flags>`] <policy>|Entfernt die Bereitstellungsrichtlinie aus Horizon Exchange.|
|`hzn dev service new [<flags>`]|Erstellt ein neues Serviceprojekt.Dieser Befehl generiert alle IEC-Service-Metadatendateien, einschließlich der Servicerichtlinienvorlage.|
|`hzn deploycheck policy [<flags>`]|Überprüft die Richtlinienkompatibilität zwischen einem Knoten, einem Service und einer Bereitstellungsrichtlinie. Es wird empfohlen, auch ' hzn deploycheck all' zu verwenden, um zu überprüfen, ob die Konfiguration der Servicevariablen korrekt ist.|
{: caption="Tabelle 5. Tools für die Richtlinienentwicklung"}

Im Abschnitt [Informationen zum Befehl 'hzn'](../installing/exploring_hzn.md) finden Sie weitere Informationen zur Verwendung des Befehls `hzn`.
