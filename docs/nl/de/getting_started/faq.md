---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Häufig gestellte Fragen (FAQs)
{: #faqs}

Nachfolgend erhalten Sie Antworten auf einige der häufig gestellten Fragen (FAQs = Frequently Asked Questions) zu {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

  * [Gibt es eine Möglichkeit zum Erstellen einer eigenständigen Umgebung zu Entwicklungszwecken?](#one_click)
  * [Handelt es sich bei der {{site.data.keyword.ieam}}-Software um ein Open-Source-Produkt?](#open_sourced)
  * [Wie können Edge-Services mithilfe von {{site.data.keyword.ieam}} entwickelt und bereitgestellt werden?](#dev_dep)
  * [Welche Hardwareplattformen für Edge-Knoten werden von {{site.data.keyword.ieam}} unterstützt?](#hw_plat)
  * [Kann ich mit {{site.data.keyword.ieam}} alle {{site.data.keyword.linux_notm}}-Distributionen auf meinen Edge-Knoten ausführen?](#lin_dist)
  * [Welche Programmiersprachen und Umgebungen werden von {{site.data.keyword.ieam}} unterstützt?](#pro_env)
  * [Steht ausführliches Dokumentationsmaterial für die REST-APIs zur Verfügung, die in den Komponenten in {{site.data.keyword.ieam}} bereitgestellt werden?](#rest_doc)
  * [Verwendet {{site.data.keyword.ieam}} Kubernetes?](#use_kube)
  * [Verwendet {{site.data.keyword.ieam}} MQTT?](#use_mqtt)
  * [Wie lange dauert es normalerweise nach dem Registrieren eines Edge-Knotens, bis Vereinbarungen erstellt und die entsprechenden Container aktiv werden?](#agree_run)
  * [Kann die {{site.data.keyword.horizon}}-Software und können alle anderen Softwarekomponenten und Daten, die in Zusammenhang mit {{site.data.keyword.ieam}} stehen, vom Host eines Edge-Knotens entfernt werden?](#sw_rem)
  * [Gibt es ein Dashboard zur Darstellung der Vereinbarungen und Services, die auf einem Edge-Knoten aktiv sind?](#db_node)
  * [Was passiert, wenn der Download eines Container-Image durch einen Netzausfall unterbrochen wird?](#image_download)
  * [Wie sicher ist {{site.data.keyword.ieam}}?](#ieam_secure)
  * [Wie unterscheidet sich die Verwaltung von edgebasierter KI mit Modellen von der Verwaltung cloudbasierter KI?](#ai_cloud)

## Gibt es eine Möglichkeit zum Erstellen einer eigenständigen Umgebung zu Entwicklungszwecken?
{: #one_click}

Sie können den Open-Source-Management-Hub (ohne {{site.data.keyword.ieam}}-Managementkonsole) mit dem umfassenden Installationsprogramm für Entwickler installieren. Das umfassende Installationsprogramm erstellt einen vollständigen, aber minimal konfigurierten Management-Hub, der nicht für den Produktionsbetrieb geeignet ist. Außerdem wird ein Edge-Beispielknoten konfiguriert. Mit diesem Tool können Entwickler von Open-Source-Komponenten schnell mit ihrer Arbeit beginnen, ohne dass zunächst ein vollständiger {{site.data.keyword.ieam}}-Management-Hub für die Produktion konfiguriert werden muss. Weitere Informationen zum umfassenden Installationsprogramm finden Sie unter [Open Horizon - Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub).

## Handelt es sich bei der {{site.data.keyword.ieam}}-Software um ein Open-Source-Produkt?
{: #open_sourced}

{{site.data.keyword.ieam}} ist ein IBM Produkt. Die Kernkomponenten basieren jedoch weitgehend auf dem Open-Source-Projekt [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). Zahlreiche Muster- und Beispielprogramme, die im {{site.data.keyword.horizon}}-Projekt zur Verfügung stehen, können auch mit {{site.data.keyword.ieam}} genutzt werden. Weitere Informationen zu dem Projekt finden Sie unter [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## Wie können Edge-Services mit {{site.data.keyword.ieam}} entwickelt und bereitgestellt werden?
{: #dev_dep}

Weitere Informationen hierzu finden Sie im Abschnitt [Edge-Services verwenden](../using_edge_services/using_edge_services.md).

## Welche Hardwareplattformen für Edge-Knoten werden von {{site.data.keyword.ieam}} unterstützt?
{: #hw_plat}

{{site.data.keyword.ieam}} unterstützt über das verfügbare Debian {{site.data.keyword.linux_notm}}-Paket mit Binärkomponenten für {{site.data.keyword.horizon}} oder durch Docker-Container unterschiedliche Hardwarearchitekturen. Weitere Informationen hierzu finden Sie im Abschnitt zur [Installation der {{site.data.keyword.horizon}}-Software](../installing/installing_edge_nodes.md).

## Kann ich mit {{site.data.keyword.ieam}} alle {{site.data.keyword.linux_notm}}-Distributionen auf meinen Edge-Knoten ausführen?
{: #lin_dist}

Ja und nein.

Sie können Edge-Software entwickeln, die eine beliebige {{site.data.keyword.linux_notm}}-Distribution als Basisimage der Docker-Container verwendet (wenn sie die Dockerfile-Anweisung `FROM` verwendet), sofern diese Basis auf dem Host {{site.data.keyword.linux_notm}}-Kernel auf Ihren Edge-Knoten funktioniert. Dies bedeutet, dass Sie für Ihre Container jede Distribution verwenden können, die Docker auf den Edge-Hosts ausführen kann.

Das Hostbetriebssystem des Edge-Knotens muss jedoch eine aktuelle Version von Docker ausführen können und muss in der Lage sein, die {{site.data.keyword.horizon}}-Software auszuführen. Momentan wird die {{site.data.keyword.horizon}}-Software nur als Debian- und RPM-Pakete für Edge-Knoten bereitgestellt, die unter {{site.data.keyword.linux_notm}} ausgeführt werden. Für Apple Macintosh-Maschinen wird eine Version mit Docker-Containern bereitgestellt. Das {{site.data.keyword.horizon}}-Entwicklerteam verwendet hauptsächlich Apple Macintosh oder die {{site.data.keyword.linux_notm}}-Distributionen Ubuntu und Raspbian.

Die Installation des RPM-Pakets wurde darüber hinaus auf Edge-Knoten getestet, die mit Red Hat Enterprise Linux (RHEL) Version 8.2 konfiguriert sind.

## Welche Programmiersprachen und Umgebungen werden von {{site.data.keyword.ieam}} unterstützt?
{: #pro_env}

{{site.data.keyword.ieam}} unterstützt nahezu alle Programmiersprachen und Softwarebibliotheken, die Sie für die Ausführung in einem entsprechenden Docker-Container auf Ihren Edge-Knoten konfigurieren können.

Wenn für Ihre Software der Zugriff auf spezielle Hardwarekomponenten oder Betriebssystemservices erforderlich ist, müssen Sie möglicherweise Argumente bereitstellen, die äquivalent zu `docker run`-Argumenten sind, um diesen Zugriff zu unterstützen. Sie können unterstützte Argumente im Abschnitt `deployment` Ihrer Docker-Container-Definitionsdatei angeben.

## Steht ausführliches Dokumentationsmaterial für die REST-APIs zur Verfügung, die in den Komponenten in {{site.data.keyword.ieam}} bereitgestellt werden?
{: #rest_doc}

Ja. Weitere Informationen finden Sie unter [{{site.data.keyword.ieam}}-APIs](../api/edge_rest_apis.md). 

## Verwendet {{site.data.keyword.ieam}} Kubernetes?
{: #use_kube}

Ja. {{site.data.keyword.ieam}} verwendet [{{site.data.keyword.open_shift_cp}})](https://docs.openshift.com/container-platform/4.6/welcome/index.md)-Kubernetes-Services.

## Verwendet {{site.data.keyword.ieam}} MQTT?
{: #use_mqtt}

{{site.data.keyword.ieam}} verwendet zum Unterstützen eigener interner Funktionen kein Message Queuing Telemetry Transport (MQTT); die Programme, die Sie auf Ihren Edge-Knoten bereitstellen, können MQTT jedoch für ihre eigenen Zwecke nutzen. Es sind Beispielprogramme verfügbar, die MQTT und andere Technologien (beispielsweise {{site.data.keyword.message_hub_notm}} basierend auf Apache Kafka) zum Transportieren von Daten an und von Edge-Knoten verwenden.

## Wie lange dauert es normalerweise nach dem Registrieren eines Edge-Knotens, bis Vereinbarungen erstellt und die entsprechenden Container aktiv werden?
{: #agree_run}

Im Allgemeinen dauert es nach der Registrierung nur einige Sekunden, bis der Agent und der ferne Agbot eine Vereinbarung treffen und die Software bereitstellen. Nach diesen Schritten lädt der {{site.data.keyword.horizon}}-Agent Ihre Container auf den Edge-Knoten herunter (`Docker Pull`), überprüft deren kryptografischen Signaturen bei {{site.data.keyword.horizon_exchange}} und führt sie aus. Abhängig von der Größe der Container und der Geschwindigkeit, mit der sie gestartet und aktiviert werden können, kann es einige weitere Sekunden bis zu mehreren Minuten dauern, bis der Edge-Knoten vollständig funktionsbereit ist.

Nachdem Sie einen Edge-Knoten registriert haben, können Sie den Befehl `hzn node list` ausführen, um den Status von {{site.data.keyword.horizon}} auf dem Edge-Knoten anzuzeigen. Wenn die Ausführung des Befehls `hzn node list` ergibt, dass der Status `configured` (Konfiguriert) lautet, dann können die {{site.data.keyword.horizon}}-Agbots den Edge-Knoten erkennen und mit dem Erstellen von Vereinbarungen beginnen.

Verwenden Sie den Befehl `hzn agreement list`, wenn Sie die Phasen des Vereinbarungsprozesses beobachten wollen.

Nachdem eine Vereinbarungsliste erstellt wurde, können Sie den Befehl `docker ps` verwenden, um die aktiven Container anzuzeigen. Sie können auch den Befehl `docker inspect <container>` ausführen, um detaillierte Informationen zur Bereitstellung eines bestimmten Containers (`<container>`) anzuzeigen.

## Kann die {{site.data.keyword.horizon}}-Software und können alle anderen Softwarekomponenten und Daten, die in Zusammenhang mit {{site.data.keyword.ieam}} stehen, vom Host eines Edge-Knotens entfernt werden?
{: #sw_rem}

Ja. Wenn der Edge-Knoten registriert ist, müssen Sie die Registrierung des Edge-Knotens zurücknehmen. Führen Sie dazu den folgenden Befehl aus: 
```
hzn unregister -f -r
```
{: codeblock}

Wenn der Edge-Knoten nicht registriert ist, können Sie die installierte {{site.data.keyword.horizon}}-Software entfernen. Führen Sie hierzu beispielsweise bei Systemen mit Debian-Basis Folgendes aus:
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## Gibt es ein Dashboard zur Darstellung der Vereinbarungen und Services, die auf einem Edge-Knoten aktiv sind?
{: #db_node}

Sie können die Webbenutzerschnittstelle von {{site.data.keyword.ieam}} verwenden, um die Edge-Knoten und -Services zu überwachen.

Mit dem Befehl `hzn` können Sie außerdem Informationen zu den aktiven Vereinbarungen und Services über die REST-API des lokalen {{site.data.keyword.horizon}}-Agenten auf dem Edge-Knoten abrufen. Führen Sie die folgenden Befehle aus, um die API zum Abrufen der zugehörigen Informationen zu verwenden:

```
hzn node list hzn agreement list docker ps
```
{: codeblock}

## Was passiert, wenn der Download eines Container-Image durch einen Netzausfall unterbrochen wird?
{: #image_download}

Zum Herunterladen von Container-Images wird die Docker-API eingesetzt. Falls die Docker-API den Download beendet, gibt sie an den Agenten einen Fehler zurück. Der Agent bricht daraufhin den aktuellen Bereitstellungsversuch ab. Sobald der Agbot den Abbruch erkennt, leitet er beim Agenten einen neuen Bereitstellungsversuch ein. Während des nachfolgenden Bereitstellungsversuchs nimmt die Docker-API den Download an der Stelle wieder auf, an der er unterbrochen wurde. Dieser Prozess wird fortgesetzt, bis das Image vollständig heruntergeladen ist und die Bereitstellung fortgesetzt werden kann. Für die Image-Pull-Operation ist die API für die Docker-Bindung zuständig; im Fehlerfall wird die Vereinbarung abgebrochen.

## Wie sicher ist {{site.data.keyword.ieam}}?
{: #ieam_secure}

* {{site.data.keyword.ieam}} automatisiert die verschlüsselt signierte Authentifizierung von Edge-Einheiten mit privatem und öffentlichem Schlüssel und wendet sie bei der Kommunikation mit dem {{site.data.keyword.ieam}}-Management-Hub während der Bereitstellung an. Die Kommunikation wird immer vom Edge-Knoten initiiert und gesteuert. 
* Das System verfügt über Knoten- und Serviceberechtigungsnachweise.
* Softwareverifizierung und -authentizität werden mithilfe von Hashfunktionen sichergestellt.

Siehe [Sicherheit in der Peripherie](https://www.ibm.com/cloud/blog/security-at-the-edge).

## Wie unterscheidet sich die Verwaltung von edgebasierter KI mit Modellen von der Verwaltung cloudbasierter KI?
{: #ai_cloud}

In der Regel ermöglicht der Einsatz von KI beim Edge-Computing die Ausführung einer ad-hoc-Maschineninferenzierung mit minimaler Latenzzeit, die je nach Anwendungsfall und Hardware (z. B. RaspberryPi, Intel x86 und Nvidia Jetson nano) Echtzeitantworten liefert. Durch das {{site.data.keyword.ieam}}-MSS (Model Management System) können aktualisierte AI-Modelle ohne Ausfallzeiten bereitgestellt werden.

Siehe [Modelle, die in der Peripherie eingesetzt werden](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
