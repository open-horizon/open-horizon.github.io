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

# Tipps zur Fehlerbehebung
{: #troubleshooting_devices}

Lesen Sie die folgenden Fragen, wenn Probleme bei der Verwendung von {{site.data.keyword.edge_devices_notm}} auftreten. Die Tipps und Anleitungen zu den einzelnen Fragen können Sie bei der Behebung allgemeiner Probleme und beim Ermitteln von Informationen zur Klärung der Fehlerursache unterstützen.
{:shortdesc}

  * [Wurden die aktuellen Versionen der {{site.data.keyword.horizon}}-Pakete installiert?](#install_horizon)
  * [Wird der {{site.data.keyword.horizon}}-Agent momentan ausgeführt?](#setup_horizon)
  * [Ist der Edge-Knoten zur Interaktion mit {{site.data.keyword.horizon_exchange}} konfiguriert?](#node_configured)
  * [Wurden die erforderlichen Docker-Container für den Edge-Knoten gestartet?](#node_running)
  * [Werden die erwarteten Service-Container ausgeführt?](#run_user_containers)
  * [Sind die erwarteten Container stabil?](#containers_stable)
  * [Sind die Docker-Container korrekt vernetzt?](#container_networked)
  * [Kann auf die Abhängigkeitscontainer im Kontext Ihres Containers zugegriffen werden?](#setup_correct)
  * [Geben die benutzerdefinierten Container Fehlernachrichten ins Protokoll aus?](#log_user_container_errors)
  * [Können Sie die Instanz des {{site.data.keyword.message_hub_notm}}-Kafka-Brokers Ihrer Organisation verwenden?](#kafka_subscription)
  * [Werden Ihre Container in {{site.data.keyword.horizon_exchange}} publiziert?](#publish_containers)
  * [Enthält Ihr publiziertes Bereitstellungsmuster alle erforderlichen Services und Versionen?](#services_included)
  * [Tipps zur Fehlerbehebung mit Bezug auf die {{site.data.keyword.open_shift_cp}}-Umgebung](#troubleshooting_icp)
  * [Fehlerbehebung bei Knotenfehlern](#troubleshooting_node_errors)

## Wurden die aktuellen Versionen der {{site.data.keyword.horizon}}-Pakete installiert?
{: #install_horizon}

Vergewissern Sie sich, dass die {{site.data.keyword.horizon}}-Software, die auf Ihren Edge-Knoten installiert ist, immer die neueste freigegebene Version aufweist. 

Auf einem {{site.data.keyword.linux_notm}}-System können Sie normalerweise den folgenden Befehl ausführen, um die Version der installierten {{site.data.keyword.horizon}}-Pakete zu überprüfen:   
```
dpkg -l | grep horizon
```
{: codeblock}

Sie können die {{site.data.keyword.horizon}}-Pakete, die den Paketmanager verwenden, auf Ihrem System aktualisieren. Verwenden Sie beispielsweise die folgenden Befehle, um {{site.data.keyword.horizon}} auf einem {{site.data.keyword.linux_notm}}-System auf die aktuelle Version zu aktualisieren: 
```
sudo apt update
sudo apt install -y blue horizon
```

## Wird der {{site.data.keyword.horizon}}-Agent momentan ausgeführt?
{: #setup_horizon}

Verwenden Sie den folgenden {{site.data.keyword.horizon}}-CLI-Befehl, um zu überprüfen, ob der Agent momentan ausgeführt wird: 
```
hzn node list | jq .
```
{: codeblock}

Sie können den Status des {{site.data.keyword.horizon}}-Agenten auch mit der System-Management-Software des Hosts überprüfen. Auf einem Ubuntu-basierten {{site.data.keyword.linux_notm}}-System können Sie beispielsweise das Dienstprogramm `systemctl` wie folgt verwenden: 
```
sudo systemctl status horizon
```
{: codeblock}

Wenn der Agent aktiv ist, wird eine Zeile ähnlich der folgenden ausgegeben: 
```
Active: active (running) since Fri 2018-09-02 15:00:04 UTC; 2h 29min ago
```
{: codeblock}

## Ist der Edge-Knoten zur Interaktion mit {{site.data.keyword.horizon_exchange}} konfiguriert? 
{: #node_configured}

Führen Sie den folgenden Befehl aus, um zu überprüfen, ob Sie mit {{site.data.keyword.horizon_exchange}} kommunizieren können: 
```
hzn exchange version
```
{: codeblock}

Führen Sie den folgenden Befehl aus, um zu überprüfen, ob {{site.data.keyword.horizon_exchange}} akzeptiert wird: 
```
    hzn exchange user list
    ```
{: codeblock}

Nach der Registrierung Ihres Edge-Knotens bei {{site.data.keyword.horizon}} können Sie überprüfen, ob der Knoten mit {{site.data.keyword.horizon_exchange}} interagiert, indem Sie die Konfiguration des lokalen {{site.data.keyword.horizon}}-Agenten anzeigen. Führen Sie den folgenden Befehl aus, um die Agentenkonfiguration anzuzeigen: 
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## Wurden die erforderlichen Docker-Container für den Edge-Knoten gestartet?
{: #node_running}

Wenn Ihr Edge-Knoten bei {{site.data.keyword.horizon}} registriert wird, dann erstellt ein {{site.data.keyword.horizon}}-Agbot (Agreement Bot; Vereinbarungsbot) eine Vereinbarung mit dem Edge-Knoten über die Ausführung der Services, auf die in Ihrem Gateway-Typ (Bereitstellungsmuster) verwiesen wird. Wenn diese Vereinbarung nicht erstellt werden kann, sollten Sie die im Folgenden beschriebenen Prüfungen ausführen, um den Fehler zu beheben. 

Vergewissern Sie sich, dass sich Ihr Edge-Knoten im Status `configured` (Konfiguriert) befindet und über die korrekten Werte für `id` und `organization` verfügt. Stellen Sie außerdem sicher, dass die Architektur, die von {{site.data.keyword.horizon}} für die Berichterstellung verwendet wird, mit der Architektur übereinstimmt, die Sie in den Metadaten für Ihre Services verwendet haben. Führen Sie den folgenden Befehl aus, um diese Einstellungen aufzulisten: 
```
hzn node list | jq .
```
{: codeblock}

Wenn diese Werte Ihren Erwartungen entsprechen, können Sie den folgenden Befehl ausführen, um den Vereinbarungsstatus des Edge-Knotens zu überprüfen:  
```
hzn agreement list -r | jq .
```
{: codeblock}

Wenn durch diesen Befehl keine Vereinbarungen angezeigt werden, ist es möglich, dass diese Vereinbarungen zwar erstellt wurden, dass aber ein Problem aufgetreten ist. In diesem Fall kann eine Vereinbarung storniert werden, bevor sie in der Ausgabe des vorherigen Befehls angezeigt werden kann. Tritt diese Stornierung der Vereinbarung auf, wird die stornierte Vereinbarung mit dem Status `terminated_description` in der Liste der archivierten Vereinbarungen angezeigt. Führen Sie den folgenden Befehl aus, um die Liste der archivierten Vereinbarungen anzuzeigen:  
```
hzn agreement list -r | jq .
```
{: codeblock}

Auch vor der Erstellung einer Vereinbarung kann es zu Problemen kommen. Tritt dieses Problem auf, dann sollten Sie das Ereignisprotokoll für den {{site.data.keyword.horizon}}-Agenten überprüfen, um mögliche Fehler zu ermitteln. Führen Sie den folgenden Befehl aus, um das Protokoll anzuzeigen:  
```
hzn eventlog list
``` 
{: codeblock}

Das Ereignisprotokoll kann Folgendes enthalten:  

* Die Signatur der Servicemetadaten (insbesondere der Wert im Feld `deployment`) kann nicht überprüft werden. Dieser Fehler ist normalerweise darauf zurückzuführen, dass Ihr öffentlicher Signierschlüssel nicht auf den Edge-Knoten importiert wurde. Sie können den Schlüssel mit dem Befehl `hzn key import -k <pubkey>` importieren. Sie können die Schlüssel anzeigen, die auf Ihren lokalen Edge-Knoten importiert werden, indem Sie den Befehl `hzn key list` ausführen. Sie können überprüfen, ob die Servicemetadaten in {{site.data.keyword.horizon_exchange}} mit Ihrem Schlüssel signiert werden, indem Sie den folgenden Befehl ausführen: 
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

  Ersetzen Sie `<service-id>` durch die ID für Ihren Service. Diese ID kann das folgende Format aufweisen: `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`.


* Der Pfad des Docker-Images im Feld `deployment` des Service ist nicht korrekt. Vergewissern Sie sich, dass der Edge-Knoten den Imagepfad mit `docker pull` übertragen kann. 
* Der {{site.data.keyword.horizon}}-Agent auf Ihrem Edge-Knoten verfügt nicht über Zugriff auf die Docker-Registry, in der Ihre Docker-Images gespeichert sind. Wenn die Docker-Images in der fernen Docker-Registry nicht global lesbar sind, müssen Sie die Berechtigungsnachweise mit dem Befehl `docker login` zu Ihrem Edge-Knoten hinzufügen. Sie müssen diesen Schritt nur einmal ausführen, da die Berechtigungsnachweise auf dem Edge-Knoten gespeichert werden.
* Wenn ein Container fortlaufend neu gestartet wird, dann überprüfen Sie das Containerprotokoll auf detaillierte Informationen zu diesem Vorgang. Ein Container wird dann fortlaufend neu gestartet, wenn er nur für wenige Sekunden aufgelistet wird oder wenn er weiterhin mit dem Status 'restarting' (Neustart wird ausgeführt) aufgelistet wird, wenn Sie den Befehl `docker ps` ausführen. Sie können die Details im Containerprotokoll anzeigen, indem Sie den folgenden Befehl ausführen: 
  ```
  grep --text -E ' <service>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## Werden die erwarteten Versionen der Service-Container ausgeführt?
{: #run_user_containers}

Ihre Containerversionen werden durch eine Vereinbarung gesteuert, die nach dem Hinzufügen Ihres Service zum Bereitstellungsmuster und nach der Registrierung Ihres Edge-Knotens für dieses Muster erstellt wird. Stellen Sie sicher, dass Ihr Edge-Knoten über eine aktuelle Vereinbarung für Ihr Muster verfügt, indem Sie den folgenden Befehl ausführen: 

```
hzn agreement list | jq .
```
{: codeblock}

Wenn Sie sich vergewissert haben, dass Sie über die korrekte Vereinbarung für Ihr Muster verfügen, dann verwenden Sie den folgenden Befehl, um die aktiven Container anzuzeigen. Vergewissern Sie sich, dass Ihre benutzerdefinierten Container aufgelistet werden und aktiv sind: 
```
docker ps
```
{: codeblock}

Nachdem die Vereinbarung akzeptiert wurde, benötigt der {{site.data.keyword.horizon}}-Agent möglicherweise mehrere Minuten, bevor die entsprechenden Container heruntergeladen, überprüft und gestartet werden können. Diese Vereinbarung hängt hauptsächlich von der Größe der Container ab, die aus fernen Repositorys abgerufen werden müssen. 

## Sind die erwarteten Container stabil?
{: #containers_stable}

Führen Sie den folgenden Befehl aus, um zu überprüfen, ob die Container stabil sind: 
```
docker ps
```
{: codeblock}

In der Befehlsausgabe können Sie die Ausführungsdauer der einzelnen Container ersehen. Wenn Sie im Zeitverlauf feststellen, dass Ihre Container unerwartet neu gestartet werden, dann überprüfen Sie die Containerprotokolle auf Fehler. 

Es wird empfohlen, die folgenden Befehle auszuführen, um die Protokollierung einzelner Services zu konfigurieren, da die ein bewährtes Verfahren bei der Entwicklung ist (nur für {{site.data.keyword.linux_notm}}-Systeme): 
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf
$template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"

:syslogtag, startswith, "workload-" -?DynamicWorkloadFile
& stop
:syslogtag, startswith, "docker/" -/var/log/docker_containers.log
& stop
:syslogtag, startswith, "docker" -/var/log/docker.log
& stop
EOF
service rsyslog restart
```
{: codeblock}

Wenn Sie den vorherigen Schritt ausgeführt haben, werden die Protokolle für die Container in separaten Dateien im Verzeichnis `/var/log/workload/` aufgezeichnet. Verwenden Sie den Befehl `docker ps`, um die vollständigen Namen Ihrer Container zu ermitteln. Sie können die Protokolldatei mit diesem Namen und dem Suffix `.log` in diesem Verzeichnis finden.

Wenn die Protokollierung einzelner Services nicht konfiguriert wurde, wird Ihr Service zusammen mit allen anderen Protokollnachrichten im Systemprotokoll protokolliert. Um die Daten für Ihre Container zu überprüfen, müssen Sie den Containernamen in der Systemprotokollausgabe in der Datei `/var/log/syslog` nach dem Containerprotokoll suchen. Sie können das Protokoll beispielsweise durchsuchen, indem Sie einen Befehl ähnlich dem folgenden ausführen:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Verfügen die Container über die korrekten Docker-Netzverbindungen?
{: #container_networked}

Vergewissern Sie sich, dass Ihre Container über die korrekten Docker-Netzverbindungen verfügen, damit sie auf erforderliche Services zugreifen können. Führen Sie den folgenden Befehl aus, um sicherzustellen, dass Sie die virtuellen Docker-Netze anzeigen können, die auf Ihrem Edge-Knoten aktiv sind: 
```
docker network list
```
{: codeblock}

Zur Anzeige weiterer Informationen zu den Netzen können Sie den Befehl `docker inspect X` verwenden. Hierbei steht `X` für den Namen des Netzes. In der Befehlsausgabe werden alle Container aufgelistet, die in dem virtuellen Netz ausgeführt werden.

Sie können den Befehl `docker inspect Y` auch für jeden Container ausführen, um weitere Informationen abzurufen. Hierbei steht `Y` für den Namen des Containers. Sie können beispielsweise die Informationen des Containers `NetworkSettings` überprüfen und den Container `Networks` durchsuchen. In diesem Container können Sie die Zeichenfolge mit der relevanten Netz-ID und Informationen zur Darstellung des Containers im Netz anzeigen. Diese Darstellungsinformationen umfassen den Wert für die IP-Adresse (`IPAddress`) des Containers und die Liste der Netzaliasnamen, die in diesem Netz definiert sind.  

Aliasnamen stehen für alle Container in diesem virtuellen Netz zur Verfügung. Diese Namen werden normalerweise von den Containern in Ihrem Codebereitstellungsmuster zur Erkennung anderer Container im virtuellen Netz verwendet. Sie können Ihrem Service beispielsweise den Namen `myservice` zuordnen. Andere Container können diesen Namen dann direkt verwenden, um im Netz auf den Service zuzugreifen, z. B. mit dem Befehl `ping myservice`. Der Aliasname Ihres Containers wird im Feld `deployment` der zugehörigen Servicedefinitionsdatei angegeben, die Sie an den Befehl `hzn exchange service publish` übergeben haben. 

Weitere Informationen zu den Befehlen, die von der Docker-Befehlszeilenschnittstelle unterstützt werden, finden Sie in der [Docker-Befehlsreferenz ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Kann auf die Abhängigkeitscontainer im Kontext Ihres Containers zugegriffen werden?
{: #setup_correct}

Geben Sie den Kontext eines aktiven Containers ein, um Fehler während der Laufzeit mithilfe des Befehls `docker exec` zu beheben. Verwenden Sie den Befehl `docker ps`, um die ID des aktiven Containers zu suchen. Verwenden Sie anschließend einen Befehl wie den folgenden, um den Kontext einzugeben. Ersetzen Sie dabei `CONTAINERID` durch die ID Ihres Containers: 
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

Wenn Ihr Container Bash enthält, können Sie am Ende des obigen Befehls `/bin/bash` anstelle von `/bin/sh` angeben.

Wenn Sie sich im Containerkontext befinden, können Sie Befehle wie `ping` oder `curl` ausführen, um mit den im Kontext erforderlichen Containern zu interagieren und die Konnektivität zu überprüfen. 

Weitere Informationen zu den Befehlen, die von der Docker-Befehlszeilenschnittstelle unterstützt werden, finden Sie in der [Docker-Befehlsreferenz ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.docker.com/engine/reference/commandline/docker/#child-commands).

## Geben die benutzerdefinierten Container Fehlernachrichten ins Protokoll aus?
{: #log_user_container_errors}

Wenn Sie die Protokollierung einzelner Services konfiguriert haben, wird das Protokoll der einzelnen Container in eine separate Datei im Verzeichnis `/var/log/workload/` geschrieben. Verwenden Sie den Befehl `docker ps`, um die vollständigen Namen Ihrer Container zu ermitteln. Anschließend müssen Sie in diesem Verzeichnis nach der Datei mit diesem Namen suchen, die über das Suffix `.log` verfügt.

Wenn die Protokollierung einzelner Services nicht konfiguriert wurde, dann wird Ihr Service zusammen mit allen anderen Details im Systemprotokoll protokolliert. Um die Daten zu überprüfen, müssen Sie in der Systemprotokollausgabe im Verzeichnis `/var/log/syslog` nach dem Containerprotokoll suchen. Sie können das Protokoll beispielsweise durchsuchen, indem Sie einen Befehl ähnlich dem folgenden ausführen:
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## Können Sie die Instanz des {{site.data.keyword.message_hub_notm}}-Kafka-Brokers Ihrer Organisation verwenden?
{: #kafka_subscription}

Die Subskription der Kafka-Instanz für Ihre Organisation über {{site.data.keyword.message_hub_notm}} kann die Überprüfung Ihrer Kafka-Benutzerberechtigungsnachweise vereinfachen. Diese Subskription kann Sie auch bei der Überprüfung Ihrer Kafka-Serviceinstanz unterstützen, um festzustellen, ob diese Instanz in der Cloud ausgeführt wird und ob Ihr Edge-Knoten Daten sendet, wenn Daten publiziert werden. 

Um eine Subskription für Ihren Kafka-Broker durchzuführen, müssen Sie das Programm `kafkacat` installieren. Verwenden Sie beispielsweise auf einem Ubuntu {{site.data.keyword.linux_notm}}-System den folgenden Befehl: 

```bash
sudo apt install kafkacat
```
{: codeblock}

Nach der Installation können Sie die Subskription mit dem im folgenden Beispiel aufgeführten Befehl durchführen. In diesem Beispiel werden die Berechtigungsnachweise verwendet, die normalerweise in den Verweisen auf Umgebungsvariablen platziert werden:

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

Hierbei steht `EVTSTREAMS_BROKER_URL` für die URL Ihres Kafka-Brokers, `EVTSTREAMS_TOPIC` für Ihr Kafka-Topic und `EVTSTREAMS_API_KEY` für den API-Schlüssel zur Authentifizierung bei der {{site.data.keyword.message_hub_notm}}-API.

Wenn der Subskriptionsbefehl erfolgreich ausgeführt werden konnte, wird der Befehl dauerhaft geblockt. Der Befehl wartet auf eine Publizierung beim Kafka-Broker und ruft die dabei generierten Nachrichten ab und zeigt sie an. Werden nach einigen Minuten keine Nachrichten Ihres Edge-Knotens angezeigt, sollten Sie das Serviceprotokoll auf Fehlernachrichten überprüfen. 

Führen Sie beispielsweise den folgenden Befehl aus, um das Protokoll für den Service `cpu2evtstreams` zu überprüfen: 

* Für {{site.data.keyword.linux_notm}} und {{site.data.keyword.windows_notm}} 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* Für macOS

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## Werden Ihre Container in {{site.data.keyword.horizon_exchange}} publiziert?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}} ist das zentrale Warehouse für Metadaten zu dem Code, der für Ihre Edge-Knoten publiziert wird. Wenn Sie Ihren Code weder signiert noch in {{site.data.keyword.horizon_exchange}} publiziert haben, kann der Code nicht mit einer Pull-Operation auf die verifizierten Edge-Knoten übertragen und ausgeführt werden. 

Führen Sie den Befehl `hzn` mit den folgenden Argumenten aus, um die Liste des publizierten Codes anzuzeigen und zu überprüfen, ob alle Service-Container erfolgreich publiziert werden konnten: 

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

Der Parameter `$ORG_ID` gibt Ihre Organisations-ID an  und in `$SERVICE` wird der Name des Service angegeben, zu dem Sie Informationen abrufen wollen. 

## Enthält Ihr publiziertes Bereitstellungsmuster alle erforderlichen Services und Versionen?
{: #services_included}

Sie können den Befehl `hzn` auf allen Maschinen, auf denen er installiert wurde, zum Abrufen der Details zu den Bereitstellungsmustern verwenden. Führen Sie den Befehl mit den folgenden Argumenten aus, um die Liste der Bereitstellungsmuster aus {{site.data.keyword.horizon_exchange}} zu extrahieren: 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

Der Parameter `$ORG_ID` gibt Ihre Organisations-ID an und in `$PATTERN` wird der Name des Bereitstellungsmusters angegeben, zu dem Sie Informationen abrufen wollen. 

## Tipps zur Fehlerbehebung mit Bezug auf die {{site.data.keyword.open_shift_cp}}-Umgebung
{: #troubleshooting_icp}

Lesen Sie die folgenden Informationen, um die Behebung allgemeiner Fehler in {{site.data.keyword.open_shift_cp}}-Umgebungen, die bei {{site.data.keyword.edge_devices_notm}} auftreten können, zu vereinfachen. Diese Tipps können Sie bei der Behebung allgemeiner Probleme und beim Ermitteln von Informationen zur Klärung der Fehlerursache unterstützen.
{:shortdesc}

### Sind die Berechtigungen für {{site.data.keyword.edge_devices_notm}} ordnungsgemäß für die Verwendung in der {{site.data.keyword.open_shift_cp}}-Umgebung konfiguriert?
{: #setup_correct}

Sie benötigen ein {{site.data.keyword.open_shift_cp}}-Benutzerkonto, um Aktionen in {{site.data.keyword.edge_devices_notm}} in dieser Umgebung ausführen zu können. Darüber hinaus benötigen Sie einen API-Schlüssel, der aus diesem Konto erstellt wurde. 

Führen Sie den folgenden Befehl aus, um Ihre Berechtigungsnachweise für {{site.data.keyword.edge_devices_notm}} in dieser Umgebung zu überprüfen: 

   ```
    hzn exchange user list
    ```
   {: codeblock}

Wenn Exchange einen für JSON-formatierten Eintrag zurückgibt, in dem mindestens ein Benutzer angegeben wird, sind die Berechtigungsnachweise für {{site.data.keyword.edge_devices_notm}} ordnungsgemäß konfiguriert. 

Wird eine Fehlerantwort zurückgegeben, können Sie entsprechende Schritte ausführen, um die Konfigurationsfehler bei den Berechtigungsnachweisen zu suchen. 

Wenn die Fehlernachricht angibt, dass ein falscher API-Schlüssel vorliegt, können Sie mit den folgenden Befehlen einen neuen API-Schlüssel erstellen. 

Weitere Informationen finden Sie unter [Erforderliche Informationen und Dateien zusammenstellen](../developing/software_defined_radio_ex_full.md#prereq-horizon). 

## Fehlerbehebung bei Knotenfehlern
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} publiziert eine Untergruppe von Ereignisprotokollen in Exchange, die in der {{site.data.keyword.gui}} angezeigt werden können. Die folgenden Fehler enthalten Links zu Hinweisen für die Fehlerbehebung.
{:shortdesc}

  - [Fehler beim Laden des Images](#eil)
  - [Fehler bei der Bereitstellungskonfiguration](#eidc)
  - [Fehler beim Containerstart](#esc)

### Fehler beim Laden des Images
{: #eil}

Dieser Fehler tritt auf, wenn das Service-Image, auf das in der Servicedefinition verwiesen wird, nicht im Image-Repository vorhanden ist. Gehen Sie wie folgt vor, um diesen Fehler zu beheben: 

1. Publizieren Sie den Service ohne das Flag **-I** erneut.
    ```
    hzn exchange service publish -f <servicedefinitionsdatei>
    ```
    {: codeblock}

2. Publizieren Sie das Service-Image direkt im Image-Repository.
    ```
    docker push <imagename>
    ```
    {: codeblock} 
    
### Fehler bei der Bereitstellungskonfiguration
{: #eidc}

Dieser Fehler tritt auf, wenn die Bereitstellungskonfigurationen für die Servicedefinitionen eine Bindung an eine Datei angeben, auf die nur der Rootbenutzer Zugriff hat. Gehen Sie wie folgt vor, um diesen Fehler zu beheben: 

1. Binden Sie den Container an eine Datei, auf die nicht nur der Rootbenutzer Zugriff hat. 
2. Ändern Sie die Dateiberechtigungen so, dass Benutzer die Datei lesen und schreiben können. 

### Fehler beim Containerstart
{: #esc}

Dieser Fehler tritt auf, wenn Docker beim Starten des Service-Containers einen Fehler feststellt. Die Fehlernachricht enthält möglicherweise weitere Informationen, die angeben, warum der Start des Containers fehlgeschlagen ist. Die Schritte zur Fehlerbehebung hängen vom Fehler ab. Die folgenden Fehler können auftreten: 

1. Die Einheit verwendet bereits einen publizierten Port, der von den Bereitstellungskonfigurationen angegeben wird. Gehen Sie wie folgt vor, um diesen Fehler zu beheben:  

    - Ordnen Sie dem Service-Container-Port einen anderen Port zu. Die angezeigte Portnummer muss nicht mit der Nummer des Service-Ports übereinstimmen. 
    - Stoppen Sie das Programm, dass denselben Port verwendet. 

2. Ein publizierter Port, der von den Bereitstellungskonfigurationen angegeben wird, hat keine gültige Portnummer. Eine Portnummer muss eine Zahl im Bereich zwischen 1 und 65535 sein. 
3. Ein Datenträgername in den Bereitstellungskonfigurationen ist kein gültiger Dateipfad. Datenträgerpfade müssen mit absoluten (und nicht mit relativen) Pfaden angegeben werden.  

### Zusätzliche Informationen

Weitere Informationen finden Sie in den folgenden Abschnitten:
  * [Fehlerbehebung](../troubleshoot/troubleshooting.md)
