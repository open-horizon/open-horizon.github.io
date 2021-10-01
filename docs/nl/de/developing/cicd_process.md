---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CI/CD-Prozess für Edge-Services
{: #edge_native_practices}

Für den effizienten Einsatz von {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ist es unabdingbar, dass sich die Edge-Services beständig weiterentwickeln; besonders wichtig ist in diesem Zusammenhang ein stabiler Prozess für die kontinuierliche Integration und kontinuierliche Bereitstellung (Continuous Delivery und Continuous Deployment, CI/CD). 

Nachfolgend werden die einzelnen Bausteine vorgestellt, mit denen Sie Ihren eigenen CI/CD-Prozess erstellen können. Weitere Informationen zu diesem Prozess finden Sie im [`open-horizon/examples`-Repository](https://github.com/open-horizon/examples).

## Konfigurationsvariablen
{: #config_variables}

Berücksichtigen Sie als Entwickler von Edge-Services die Größe des Service-Containers in der Entwicklung. Ausgehend von diesen Informationen müssen Sie möglicherweise Ihre Servicefunktionen in separate Container aufteilen. In einer solchen Situation fördern Konfigurationsvariablen, die für Testzwecke verwendet werden, die Simulation von Daten, die aus einem noch nicht entwickelten Container stammen. In der [cpu2evtstreams-Service-Definitionsdatei](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json) können Sie Eingabevariablen wie **PUBLISH** und **MOCK** anzeigen. Bei einer Untersuchung des Codes von `service.sh` können Sie feststellen, dass das Script diese und weitere Konfigurationsvariablen einsetzt, um sein Verhalten zu steuern. Die Variable **PUBLISH** steuert, ob der Code versucht, Nachrichten an IBM Event Streams zu senden. Die Variable **MOCK** steuert, ob das Script 'service.sh' versucht, Kontakt zu den REST-APIs und ihren abhängigen Services ('cpu' und 'gps') aufzunehmen, oder ob das Script `service.sh` Pseudodaten erzeugt.

Zum Zeitpunkt der Servicebereitstellung können Sie die Standardwerte der Konfigurationsvariablen außer Kraft setzen, indem Sie sie in der Knotendefinition oder im Befehl `hzn register` angeben.

## Cross-Kompilierung
{: #cross_compiling}

Mit Docker können Sie ausgehend von einem einzigen amd64-System einen containerisierten Service für mehrere Architekturen erstellen. Analog können Sie Edge-Services mit kompilierten Programmiersprachen entwickeln, die eine Cross-Kompilierung unterstützen (z. B. Go). Falls Sie beispielsweise Code auf einem Mac-Computer (einer Einheit mit amd64-Architektur) für eine arm-Einheit (Raspberry Pi) schreiben, müssen Sie unter Umständen einen Docker-Container erstellen, der Parameter wie GOARCH angibt, um arm als Ziel zu definieren. Diese Konfiguration kann Bereitstellungsfehler verhindern. Siehe [open-horizon-GPS-Service](https://github.com/open-horizon/examples/tree/master/edge/services/gps).

## Test
{: #testing}

Häufige und automatisierte Tests sind ein wichtiger Bestandteil des Entwicklungsprozesses. Zur Vereinfachung der Tests können Sie Ihren Service mit dem Befehl  `hzn dev service start` in einer simulierten Horizon-Agentenumgebung ausführen. Diese Strategie ist auch in DevOps-Umgebungen von Nutzen, in denen die Installation und Registrierung des vollständigen Horizon-Agenten problematisch wäre. Dieses Verfahren automatisiert Tests im Repository `open-horizon examples` mit dem Ziel **make test**. Siehe [Testziel erstellen](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30).


Führen Sie **make test** aus, um den Service zu erstellen und auszuführen, der **hzn dev service start** verwendet. Nach der Ausführung überwacht [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) die Serviceprotokolle, um nach Daten zu suchen, die darauf hinweisen, dass der Service ordnungsgemäß ausgeführt wird.

## Bereitstellung testen
{: #testing_deployment}

Im Idealfall haben Sie bei der Entwicklung einer neuen Serviceversion Zugang zu einem vollständigen und realistischen Test. Hierzu können Sie Ihren Service auf Edge-Knoten bereitstellen; da es sich um einen Test handelt, ist es jedoch unter Umständen sinnvoll, Ihren Service nicht auf allen Edge-Knoten bereitzustellen.

Zu diesem Zweck erstellen Sie eine Bereitstellungsrichtlinie oder ein Muster, die/das sich ausschließlich auf Ihre neue Serviceversion bezieht. Anschließend registrieren Sie Ihre Testknoten bei dieser neuen Richtlinie bzw. diesem neuen Muster. Bei Verwendung einer Richtlinie besteht unter anderem die Möglichkeit, eine Eigenschaft für einen Edge-Knoten festzulegen (z. B.  "name": "mode", "value": "testing") und diese Bedingung zu Ihrer Bereitstellungsrichtlinie hinzuzufügen ("mode == testing"). Dies gewährleistet, dass nur diejenigen Knoten, die Sie für den Test vorgesehen haben, die neue Version des Service erhalten.

**Hinweis:** Sie können auch eine Bereitstellungsrichtlinie oder ein Muster über die Managementkonsole erstellen. Weitere Informationen hierzu finden Sie in [Managementkonsole verwenden](../console/accessing_ui.md).

## Bereitstellung in der Produktionsumgebung
{: #production_deployment}

Nachdem Sie die neue Version Ihres Service von einer Test- in eine Produktionsumgebung verschoben haben, können Probleme auftreten, die beim Testen nicht festgestellt wurden. Zur Behandlung solcher Probleme sind die Rollback-Einstellungen Ihrer Bereitstellungsrichtlinie bzw. Ihres Musters von Nutzen. Im Abschnitt  `serviceVersions` eines Musters oder einer Bereitstellungsrichtlinie können Sie mehrere ältere Versionen Ihres Service angeben. Legen Sie für jede Version eine Priorität fest, damit für den Edge-Knoten ein Rollback auf diese Version durchgeführt wird, falls im Zusammenhang mit der neuen Version ein Fehler auftritt. Neben dem Zuweisen einer Priorität zu jeder Rollback-Version können Sie außerdem Optionen wie die Anzahl und Dauer von Wiederholungsversuchen vor dem Zurücksetzen auf eine Version des angegebenen Service mit einer geringeren Priorität festlegen.Informationen zur spezifischen Syntax finden Sie im Abschnitt [Beispiel für diese Implementierungsrichtlinie](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json).

## Edge-Knoten anzeigen
{: #viewing_edge_nodes}

Nachdem Sie eine neue Version Ihres Service auf Knoten bereitgestellt haben, müssen Sie unbedingt in der Lage sein, ohne großen Aufwand den Allgemeinzustand Ihrer Knoten zu überwachen. Verwenden Sie für diese Task die {{site.data.keyword.ieam}}-{{site.data.keyword.gui}}. Beispielsweise können Sie im Prozess für die [Testbereitstellung](#testing_deployment) oder die [Bereitstellung in der Produktionsumgebung](#production_deployment) schnell nach Knoten mit Fehlern oder nach Knoten suchen, die Ihre Bereitstellungsrichtlinie verwenden.

## Services migrieren
{: #migrating_services}

An einem bestimmten Punkt müssen Sie möglicherweise Services, Muster oder Richtlinien aus einer  {{site.data.keyword.ieam}}-Instanz in eine andere Instanz verschieben oder auch Services aus einer Exchange-Organisation in eine andere Organisation. Dies kann der Fall sein, wenn Sie eine neue {{site.data.keyword.ieam}}-Instanz in einer anderen Hostumgebung installiert haben. Es könnte auch erforderlich sein, Services zu verschieben, wenn Sie zwei {{site.data.keyword.ieam}}-Instanzen nutzen, von denen eine für die Entwicklung und die andere für die Produktion dediziert ist. Um diesen Prozess zu vereinfachen, können Sie das [`loadResources`-Script)](https://github.com/open-horizon/examples/blob/master/tools/loadResources) im open-horizon-Beispielrepository verwenden.

## Automatisierte Tests von Pull-Anforderungen mit Travis
{: #testing_with_travis}

Sie können das Testen automatisieren, wenn eine Pull-Anforderung (PR) für Ihr GitHub-Repository mit [Travis CI](https://travis-ci.com) geöffnet wird. 

Nachfolgend erfahren Sie, wie Sie Travis und die Verfahren im GitHub-Repository 'open-horizon examples' nutzen.

Im Repository mit den Beispielen wird Travis CI zum Erstellen, Testen und Publizieren von Beispielen verwendet. In der Datei [`.travis.yml`](https://github.com/open-horizon/examples/blob/master/.travis.yml) wird eine virtuelle Umgebung eingerichtet, die als Linux-amd64-Maschine mit hzn, Docker und [qemu](https://github.com/multiarch/qemu-user-static) für den Aufbau auf mehreren Architekturen ausgeführt werden soll.

In diesem Szenario wird außerdem 'kafkacat' installiert, damit 'cpu2evtstreams' Daten an IBM Event Streams senden kann. Analog zur Nutzung der Befehlszeile kann Travis Umgebungsvariablen wie `EVTSTREAMS_TOPIC` und `HZN_DEVICE_ID` zur Verwendung mit den Edge-Beispielservices einsetzen. Die Variable HZN_EXCHANGE_URL ist so festgelegt, dass sie auf die Exchange-Staging-Instanz für die Publizierung von geänderten Services zeigt.

Das Script [travis-find](https://github.com/open-horizon/examples/blob/master/tools/travis-find) wird dann verwendet, um Services zu identifizieren, die durch die geöffnete Pull-Anforderung geändert wurden.

Falls ein Beispiel geändert worden ist, wird das Ziel `test-all-arches` in der  **Makefile** dieses Service ausgeführt. Mit den aktiven qemu-Containern der unterstützten Architekturen werden architekturübergreifende Builds unter Verwendung dieses  **Makefile**-Ziels ausgeführt, indem die Umgebungsvariable `ARCH` unmittelbar vor dem Build und dem Test festgelegt wird. 

Mit dem Befehl `hzn dev service start` wird der Edge-Service ausgeführt, und die Datei [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) überwacht die Serviceprotokolle, um festzustellen, ob der Service ordnungsgemäß funktioniert.

Siehe [helloworld Makefile](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24), um das dedizierte Makefile-Ziel `test-all-arches` anzuzeigen.

Das folgende Szenario veranschaulicht einen eingehenderen durchgängigen Test. Falls eines der geänderten Beispiele  `cpu2evtstreams` einbezieht, kann eine IBM Event Streams-Instanz im Hintergrund überwacht und auf HZN_DEVICE_ID überprüft werden. Es kann den Test bestehen und zu einer Liste aller Services mit bestandenem Test hinzugefügt werden, wenn es  lediglich die Knoten-ID **travis-test** in den Daten findet, die aus dem Abschnitt für 'cpu2evtstreams' eingelesen werden. Hierzu sind ein API-Schlüssel für IBM Event Streams und eine Broker-URL erforderlich, die als Umgebungsvariablen für den geheimen Schlüssel festgelegt sind.

Nachdem die Pull-Anforderung zusammengeführt wurde, wird dieser Prozess wiederholt und anhand der Liste der  Services mit bestandenem Test festgestellt, welche Services bei Exchange publiziert werden können. Die Travis-Umgebungsvariablen für den geheimen Schlüssel, die in diesem Beispiel verwendet werden, beinhalten alle Angaben, die zum Senden, Signieren und Publizieren von Services für Exchange benötigt werden. Hierzu gehören Docker-Berechtigungsnachweise, HZN_EXCHANGE_USER_AUTH sowie ein kryptografisches Signierschlüsselpaar, das mit dem Befehl `hzn key create` abgerufen werden kann. Damit die Signierschlüssel als sichere Umgebungsvariablen gespeichert werden können, müssen sie in Base64 codiert sein.

Anhand der Liste der Services, die den Funktionstest bestanden haben, wird ermittelt, welche Services mit dem dedizierten  `Makefile`-Ziel für die Publizierung publiziert werden sollten. Siehe [helloworld-Beispiel](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45).

Da die Services erstellt und getestet worden sind, publiziert dieses Ziel den Service, die Servicerichtlinie, das Muster und die Bereitstellungsrichtlinie in allen Architekturen in Exchange.

**Hinweis:** Außerdem können Sie viele dieser Tasks über die Managementkonsole ausführen. Weitere Informationen hierzu finden Sie in [Managementkonsole verwenden](../console/accessing_ui.md).

