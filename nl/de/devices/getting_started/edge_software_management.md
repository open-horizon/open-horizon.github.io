---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Edge-Software-Management
{: #edge_software_mgmt}

{{site.data.keyword.edge_devices_notm}} basiert auf der Verwendung geografisch verteilter autonomer Prozesse für das Management des Softwarelebenszyklus für alle Edge-Knoten.
{:shortdesc}

Die autonomen Prozesse, die das Software-Management der Edge-Knoten durchführen, verwenden die Services {{site.data.keyword.horizon_exchange}} und {{site.data.keyword.horizon_switch}}, um sich im Internet zu erkennen, ohne dabei die jeweiligen Adressen sichtbar zu machen. Nachdem die gegenseitige Erkennung erfolgreich ausgeführt wurde, verwenden die Prozesse {{site.data.keyword.horizon_exchange}} und {{site.data.keyword.horizon_switch}} zur Vereinbarung der Beziehungen und arbeiten dann zusammen, um die Edge-Knoten-Software zu verwalten. Weitere Informationen hierzu finden Sie im Abschnitt zur [Erkennung und Verhandlung](discovery_negotiation.md).

Die {{site.data.keyword.horizon}}-Software auf jedem Host kann als Edge-Knoten-Agent und/oder als Agbot (Agreement Bot; Vereinbarungsbot) verwendet werden.

## Agbot (Agreement Bot)

Agbot-Instanzen werden zentral erstellt, um alle Softwarebereitstellungsmuster für {{site.data.keyword.edge_devices_notm}}, die in {{site.data.keyword.horizon_exchange}} publiziert werden, zu verwalten. Sie bzw. einer Ihrer Entwickler kann Agbot-Prozesse auch auf jeder Maschine ausführen, die auf die Services {{site.data.keyword.horizon_exchange}} und {{site.data.keyword.horizon_switch}} zugreifen kann.

Wenn ein Agbot gestartet und konfiguriert wird, um ein bestimmtes Softwarebereitstellungsmuster zu verwalten, dann führt der Agbot eine Registrierung bei {{site.data.keyword.horizon_exchange}} durch und beginnt mit der Abfrage der Edge-Knoten, die zur Ausführung dieses Bereitstellungsmusters registriert wurden. Wird ein Edge-Knoten erkannt, dann sendet der Agbot eine Anforderung an den lokalen Agenten auf dem entsprechenden Edge-Knoten, in der die Zusammenarbeit beim Management der Software angefragt wird.

Wenn eine Vereinbarung verhandelt wird, sendet der Agbot die folgenden Informationen an den Agenten:

* Die Richtliniendetails, die im Bereitstellungsmuster enthalten sind.
* Die Liste der {{site.data.keyword.horizon}}-Services und -Versionen, die im Bereitstellungsmuster enthalten sind.
* Alle Abhängigkeiten zwischen diesen Services.
* Die gemeinsame Nutzbarkeit der Services. Die Nutzbarkeit eines Service kann als exklusiv (`exclusive`), einzeln (`singleton`) oder mehrfach (`multiple`) definiert werden.
* Details zu jedem Container aller Services. Diese Details umfassen die folgenden Informationen: 
  * Die Docker-Registry, bei der der Container registriert ist, z. B. die öffentliche DockerHub-Registry oder eine private Registry.
  * Die Registry-Berechtigungsnachweise für private Registrys.
  * Die Details zur Shellumgebung für die Konfiguration und Anpassung.
  * Die kryptografisch signierten Hashwerte des Containers und seiner Konfiguration.

Der Agbot überwacht weiterhin die Softwarebereitstellungsmuster in {{site.data.keyword.horizon_exchange}} auf Änderungen und stellt z. B. fest, ob neue Versionen von {{site.data.keyword.horizon}}-Services für das Muster publiziert wurden. Werden Änderungen festgestellt, dann sendet der Agbot erneut Anforderungen an jeden Edge-Knoten, der für das betreffende Muster registriert ist, um die Zusammenarbeit beim Management der Umstellung auf die neue Softwareversion zu vereinbaren.

Der Agbot überprüft außerdem in regelmäßigen Zeitabständen alle Edge-Knoten, die für das Bereitstellungsmuster registriert sind, um sicherzustellen, dass alle Richtlinien für das Muster umgesetzt werden. Wenn eine Richtlinie nicht umgesetzt wird, kann der Agbot die verhandelte Vereinbarung stoppen. Wenn der Edge-Knoten z. B. das Senden von Daten oder die Bereitstellung von Überwachungssignalen (Heartbeats) für einen längeren Zeitraum einstellt, dann kann der Agbot die Vereinbarung stornieren.  

### Edge-Knoten-Agent

Ein Edge-Knoten-Agent wird erstellt, wenn das {{site.data.keyword.horizon}}-Softwarepaket auf einer Edge-Maschine installiert wird. Weitere Informationen zur Installation der Software finden Sie im Abschnitt zum [Installieren der {{site.data.keyword.horizon}}-Software](../installing/adding_devices.md).

Wenn Sie Ihren Edge-Knoten zu einem späteren Zeitpunkt bei {{site.data.keyword.horizon_exchange}} registrieren, müssen Sie die folgenden Informationen bereitstellen:

* Die URL für {{site.data.keyword.horizon_exchange}}.
* Den Namen des Edge-Knotens und das Zugriffstoken für den Edge-Knoten.
* Das Softwarebereitstellungsmuster, das auf dem Edge-Knoten ausgeführt werden soll. Sie müssen sowohl den Organisations- als auch den Musternamen angeben, um das Muster zu identifizieren.

Weitere Informationen zur Registrierung finden Sie im Abschnitt zum [Registrieren von Edge-Maschinen](../installing/registration.md).

Nachdem der Edge-Knoten registriert wurde, fragt der lokale Agent {{site.data.keyword.horizon_switch}} ab, um festzustellen, ob Anforderungen für die Zusammenarbeit von fernen Agbot-Prozessen vorliegen. Wenn der Agent von einem Agbot in Bezug auf sein konfiguriertes Bereitstellungsmuster erkannt wird, dann sendet der Agbot eine Anforderung an den Edge-Knoten-Agenten, um über die Zusammenarbeit beim Software-Lifecycle-Management des Edge-Knotens zu verhandeln. Kommt eine Vereinbarung zustande, dann sendet der Agbot Informationen an den Edge-Knoten.

Der Agent extrahiert die angegebenen Docker-Container aus den jeweiligen Registrys. Anschließend verifiziert der Agent die Hashwerte und die kryptografischen Signaturen der Container. Nach Abschluss dieses Vorgangs startet der Agent die Container in umgekehrter Reihenfolge der Abhängigkeiten mit den angegebenen Umgebungskonfigurationen. Wenn die Container aktiv sind, überwacht der lokale Agent die Container. Wird die Ausführung eines Containers unvorhergesehen gestoppt, startet der Agent den Container erneut, um das Bereitstellungsmuster auf dem Edge-Knoten intakt zu halten.

### {{site.data.keyword.horizon}}-Serviceabhängigkeiten

Obwohl der {{site.data.keyword.horizon}}-Agent die Container für das zugewiesene Bereitstellungsmuster startet und verwaltet, müssen die Abhängigkeiten zwischen Services im Service-Container-Code verwaltet werden. Auch wenn die Container in umgekehrter Reihenfolge der Abhängigkeiten gestartet werden, kann {{site.data.keyword.horizon}} nicht sicherstellen, dass die Service-Provider vollständig gestartet wurden und bereit sind, um den Service bereitzustellen, bevor die Servicenutzer gestartet wurden. Die Nutzer müssen den möglicherweise langsamen Startvorgang der Services, von denen sie abhängig sind, strategisch berücksichtigen. Da bei den Containern zur Bereitstellung der Services ein Fehler auftreten kann, sodass diese nicht mehr verfügbar sind, müssen die Servicenutzer auch den Ausfall der von ihnen genutzten Services angemessen verarbeiten können. 

Der lokale Agent erkennt, wenn ein Service abstürzt, und startet den Service mit demselben Netznamen in demselben privaten Docker-Netz erneut. Während des Neustartprozesses kommt es zu einer kurzen Ausfallzeit. Der nutzende Service muss diese kurze Ausfallzeit auch überbrücken können, da ansonsten auch er ausfallen kann.

Der Agent besitzt eine eingeschränkte Fehlertoleranz. Wenn ein Container wiederholt und in schneller Abfolge abstürzt, dann stellt der Agent das erneute Starten des ständig ausfallenden Service möglicherweise ein und storniert die Vereinbarung.

### {{site.data.keyword.horizon}}-Docker-Vernetzung

{{site.data.keyword.horizon}} verwendet die Docker-Vernetzungsfunktionen zur Isolierung von Docker-Containern, die Services bereitstellen. Diese Isolation stellt sicher, dass nur berechtigte Nutzer auf die Container zugreifen können. Jeder Container wird in umgekehrter Reihenfolge seiner Abhängigkeiten gestartet, d. h., die Produzenten (Producer) werden zuerst und erst dann die Nutzer (Consumer) in einem separaten privaten virtuellen Docker-Netz gestartet. Sobald ein Container, der einen Service nutzt, gestartet wird, wird dieser Container mit dem privaten Netz des zugehörigen Producer-Containers verbunden. Producer-Container können nur von den Consumern erreicht werden, deren Abhängigkeiten zum Producer in {{site.data.keyword.horizon}} bekannt sind. Aufgrund der Art und Weise, in der Docker-Netze implementiert werden, können sämtliche Container über Host-Shells erreicht werden. 

Wenn Sie für einen Container die IP-Adresse anfordern müssen, können Sie dazu den Befehl `docker inspect <containerID>` verwenden, um die zugewiesene IP-Adresse (`IPAddress`) abzurufen. Sie können jeden Container über Ihre Host-Shells erreichen.

## Sicherheit und Datenschutz

Obwohl die Edge-Knoten-Agenten und die Agbots für Bereitstellungsmuster sich gegenseitig erkennen können, bleibt die Geheimhaltung der Daten dieser Komponenten vollständig erhalten, bis eine formale Vereinbarung zur Zusammenarbeit verhandelt wurde. Die Identitäten des Agenten und des Agbots sowie die gesamte Kommunikation werden verschlüsselt. Die Daten zur Zusammenarbeit beim Software-Management werden ebenfalls verschlüsselt. Sämtliche Softwarekomponenten, die verwaltet werden, werden kryptografisch signiert. Weitere Informationen zum Datenschutz und zu weiteren Sicherheitsaspekten bei {{site.data.keyword.edge_devices_notm}} finden Sie im Abschnitt zu [Sicherheit und Datenschutz](../user_management/security_privacy.md).
