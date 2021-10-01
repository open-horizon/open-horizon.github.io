---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Beispiele für Bereitstellungsmuster
{: #deploy_pattern_ex}

Um Ihnen den Einstieg in die Nutzung von {{site.data.keyword.edge_devices_notm}}-Bereitstellungsmustern zu vereinfachen, werden Beispielprogramme bereitgestellt, die Sie als Bereitstellungsmuster laden können.
{:shortdesc}

Testen Sie die Registrierung der hier bereitgestellten vordefinierten Beispiele für Bereitstellungsmuster, um mehr über deren Verwendung zu erfahren.

Zum Registrieren eines Edge-Knotens für eines der folgenden Beispiele eines Bereitstellungsmusters müssen Sie zuerst alle vorhandenen Registrierungen für Bereitstellungsmuster für Ihren Edge-Knoten entfernen. Führen Sie die folgenden Befehle auf Ihrem Edge-Knoten aus, um alle Registrierungen für Bereitstellungsmuster zu entfernen:
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

Beispielausgabe:
```
"unconfigured"
```
{: codeblock}

Wenn in der Befehlsausgabe `"unconfiguring"` (Dekonfiguration wird ausgeführt) anstelle von `"unconfigured"` (Dekonfiguriert) ausgegeben wird, dann warten Sie einige Minuten, bevor Sie den Befehl wiederholen. Normalerweise dauert die Ausführung des Befehls nur wenige Sekunden. Wiederholen Sie den Befehl, bis in der Ausgabe `"unconfigured"` anzeigt wird.

## Beispiele
{: #pattern_examples}

* [Hello, world ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld)
  Eine Minimalinstanz des Beispiels `"Hello, world."` zur Einführung in die {{site.data.keyword.edge_devices_notm}}-Bereitstellungsmuster.

* [Prozentsatz der CPU-Belastung des Hosts](cpu_load_example.md)
  Ein Beispiel für ein Bereitstellungsmuster, das die Daten zum Prozentsatz der CPU-Belastung nutzt und diese über {{site.data.keyword.message_hub_notm}} verfügbar macht.

* [Software-Defined Radio](software_defined_radio_ex.md)
  Ein mit allen Funktionen versehenes Beispiel, mit dem Audiodaten einer Funkstation genutzt, Sprachdaten extrahiert und die extrahierten Sprachdaten in Text umgewandelt werden können. Das Beispiel führt Stimmungsanalysen für den Text aus und stellt die gewonnenen Daten und Ergebnisse über eine Benutzerschnittstelle bereit, in der Sie die Details zu den Daten aller Edge-Knoten anzeigen können. Verwenden Sie dieses Beispiel, um mehr über die Edge-Verarbeitung zu erfahren.
