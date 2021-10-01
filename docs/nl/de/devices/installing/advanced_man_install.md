---

copyright:
years: 2019
lastupdated: "2019-011-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Erweiterte manuelle Agenteninstallation und -registrierung
{: #advanced_man_install}

Dieser Abschnitt beschreibt die einzelnen manuellen Schritte zur Installation des {{site.data.keyword.edge_devices_notm}}-Agenten auf einer Edge-Einheit und zur Registrierung. Eine automatisiertere Methode wird im Abschnitt [Automatisierte Agenteninstallation und -registrierung](automated_install.md) beschrieben.{:shortdesc}

## Agent installieren
{: #agent_install}

Hinweis: Informationen zur Befehlssyntax finden Sie im Abschnitt [In diesem Dokument verwendete Konventionen](../../getting_started/document_conventions.md).

1. Rufen Sie die Datei `agentInstallFiles-<edge-einheitentyp>.tar.gz` und den API-Schlüssel ab, der zusammen mit dieser Datei erstellt wurde, bevor Sie fortfahren.

    Als Nachkonfigurationsschritt für [Management-Hub installieren](../../hub/offline_installation.md) wurde eine komprimierte Datei für Sie erstellt, die die erforderlichen Dateien enthält, um den {{site.data.keyword.horizon}}-Agenten auf Ihrer Edge-Einheit zu installieren und bei dem 'helloworld'-Beispiel zu registrieren.

2. Kopieren Sie diese Datei mit einem USB-Stick, dem Befehl für Secure Copy oder einer anderen Methode auf die Edge-Einheit.

3. Erweitern Sie die TAR-Datei:

   ```bash
   tar -zxvf agentInstallFiles-<edge-einheitentyp>.tar.gz
   ```
   {: codeblock}

4. Halten Sie sich an denjenigen der nachfolgenden Abschnitte, der auf Ihren Typ einer Edge-Einheit anwendbar ist.

### Agent auf Edge-Einheiten oder virtuellen Maschinen unter Linux (ARM 32-Bit, ARM 64-Bit oder x86_64) installieren
{: #agent_install_linux}

Führen Sie die folgenden Schritte aus:

1. Melden Sie sich an. Wenn Sie als Benutzer ohne Rootberechtigung angemeldet sind, wechseln Sie zu einem Benutzer mit Rootberechtigung:

   ```bash
      sudo -s
      ```
   {: codeblock}

2. Fragen Sie die Docker-Version ab, um zu prüfen, ob sie aktuelle genug ist. Verwenden Sie dazu den folgenden Befehl: 

   ```bash
   docker --version
   ```
   {: codeblock}

      Wenn Docker nicht installiert ist oder eine Version vor Version `18.06.01` verwendet wird, müssen Sie die aktuelle Version von Docker wie folgt installieren: 

   ```bash
curl -fsSL get.docker.com | sh
      docker --version
      ```
   {: codeblock}

3. Installieren Sie die Horizon Debian-Pakete, die Sie auf diese Edge-Einheit kopiert haben. Verwenden Sie dazu den folgenden Befehl: 

   ```bash
   apt update && apt install ./*horizon*.deb
   ```
   {: codeblock}
   
4. Legen Sie Ihre jeweiligen Informationen als Umgebungsvariablen fest: 

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. Verweisen Sie mit dem Horizon-Agenten der Edge-Einheit auf den {{site.data.keyword.edge_notm}}-Cluster, indem Sie das Verzeichnis `/etc/default/horizon` ,t den korrekten Informationen füllen: 

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Veranlassen Sie, dass der Horizon-Agent dem Zertifikat `agent-install.crt` vertraut:

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. Starten Sie den Agenten neu, um alle Änderungen an `/etc/default/horizon` zu übernehmen: 

   ```bash
      systemctl restart horizon.service
      ```
   {: codeblock}

8. Überprüfen Sie wie folgt, ob der Agent aktiv und korrekt konfiguriert ist: 

   ```bash
       hzn version
       hzn exchange version
       hzn node list
       ```
   {: codeblock}  

      Die Ausgabe sollte ähnlich wie die folgende aussehen (Versionsnummern und URLs können variieren): 

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
      ```
   {: codeblock}

9. Wenn Sie zuvor zur privilegierten Shell gewechselt hatten, verlassen Sie sie jetzt. Für den nächsten Schritt der Registrierung Ihrer Einheit benötigen Sie keinen Rootzugriff.

   ```bash
      exit
      ```
   {: codeblock}

10. Fahren Sie damit fort, den [Agenten zu registrieren](#agent_reg).

### Agent auf einer macOS-Edge-Einheit installieren
{: #mac-os-x}

1. Importieren Sie das Zertifikat für das Paket `horizon-cli` in Ihre {{site.data.keyword.macOS_notm}}-Schlüsselkette. Führen Sie dazu den folgenden Befehl aus: 

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      Hinweis: Dieser Schritt muss auf jeder {{site.data.keyword.macOS_notm}}-Maschine nur einmal ausgeführt werden. Nachdem dieses vertrauenswürdige Zertifikat importiert wurde, können Sie alle zukünftigen Versionen der {{site.data.keyword.horizon}}-Software installieren. 

2. Installieren Sie das {{site.data.keyword.horizon}}-CLI-Paket: 

   ```bash
      sudo installer -pkg horizon-cli-*.pkg -target /
      ```
   {: codeblock}

3. Der vorherige Befehl fügt Befehle zum Verzeichnis `/usr/local/bin` hinzu. Fügen Sie dieses Verzeichnis zu Ihrem Shell-Pfad hinzu, indem Sie folgendes zu `~/.bashrc` hinzufügen: 

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. Fügen Sie das Verzeichnis `/usr/local/share/man` zum Pfad für die Man-Pages hinzu. Fügen Sie dazu das Verzeichnis zum Shell-Pfad hinzu, indem Sie folgendes zu `~/.bashrc` hinzufügen: 

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. Aktivieren Sie die Dateinamenvervollständigung für Unterbefehle für den Befehl `hzn`. Fügen Sie dazu folgendes zu `~/.bashrc` hinzu: 

  ```bash
      source /usr/local/share/horizon/hzn_bash_autocomplete.sh
      ```
  {: codeblock}

6. Beim Installieren einer **neuen Einheit** ist dieser Schritt **nicht** erforderlich. Wenn Sie jedoch den Horizon-Container auf dieser Maschine bereits installiert und gestartet haben, stoppen Sie ihn jetzt mit dem folgenden Befehl: 

  ```bash
      horizon-container stop
      ```
  {: codeblock}
7. Legen Sie Ihre jeweiligen Informationen als Umgebungsvariablen fest: 

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. Verweisen Sie mit dem Horizon-Agenten der Edge-Einheit auf den {{site.data.keyword.edge_notm}}-Cluster, indem Sie das Verzeichnis `/etc/default/horizon` ,t den korrekten Informationen füllen: 

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

9. Starten Sie den {{site.data.keyword.horizon}}-Agenten: 

  ```bash
      horizon-container start
      ```
  {: codeblock}

10. Überprüfen Sie wie folgt, ob der Agent aktiv und korrekt konfiguriert ist: 

  ```bash
       hzn version
       hzn exchange version
       hzn node list
       ```
  {: codeblock}

      Die Ausgabe sollte ähnlich wie die folgende aussehen (Versionsnummern und URLs können variieren): 

  ```bash
  $ hzn version
  Horizon CLI version: 2.23.29
  Horizon Agent version: 2.23.29
  $ hzn exchange version
  1.116.0
  $ hzn node list
      {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

11. Fahren Sie damit fort, den [Agenten zu registrieren](#agent_reg).

## Agent registrieren
{: #agent_reg}

1. Legen Sie Ihre jeweiligen Informationen als **Umgebungsvariablen** fest: 

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. Zeigen Sie die Liste der Bereitstellungsmusterbeispiele für den Edge-Service wie folgt an:
    

  ```bash
    hzn exchange pattern list IBM/
    ```
  {: codeblock}

3. Der Edge-Service 'Hello World' ist das einfachste Beispiel und ist daher ein günstiger Ausgangspunkt. **Registrieren** die Edge-Services bei {{site.data.keyword.horizon}} für die Ausführung des **'helloworld'-Bereitstellungsmusters**: 

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  Hinweis: Die Knoten-ID wird in der Ausgabe in der Zeile angezeigt, die mit **Using node ID** beginnt.

4. Die Edge-Einheit trifft eine Vereinbarung mit einem der {{site.data.keyword.horizon}}-Agreement-Bots (dieser Vorgang dauert im Allgemeinen etwa 15 Sekunden). **Fragen Sie die Vereinbarungen dieser Einheit wiederholt ab**, bis die Felder `agreement_finalized_time` und `agreement_execution_start_time` ausgefüllt sind. 

  ```bash
        hzn agreement list
        ```
  {: codeblock}

5. **Nachdem die Vereinbarung getroffen wurde** können Sie den Edge-Service des Docker-Containers auflisten, der als Ergebnis gestartet wurde: 

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. Zeigen Sie die **Ausgabe** des Edge-Service 'Hello World' an: 

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## Nächste Schritte
{: #what_next}

Navigieren Sie zu [CPU-Auslastung für IBM Event Streams](cpu_load_example.md), um mit weiteren Edge-Service-Beispielen fortzufahren.
