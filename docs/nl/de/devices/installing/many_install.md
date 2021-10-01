---

copyright:
years: 2020
lastupdated: "2020-5-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Masseninstallation und -registrierung von Agenten
{: #batch-install}

Mit dem Masseninstallationsprozess können Sie mehrere Edge-Einheiten mit ähnlichen Typen (also gleicher Architektur oder Richtlinie, gleichem Betriebssystem oder Muster) einrichten.

Hinweis: Bei diesem Prozess werden macOS-Computer nicht als Ziel-Edge-Einheiten unterstützt. Sie können diesen Prozess jedoch bei Bedarf von einem macOS-Computer aus ansteuern. (Mit anderen Worten, bei diesem Host kann es sich um einen macOS-Computer handeln.)

### Voraussetzungen

* Die zu installierenden und registrierenden Einheiten müssen über Netzzugriff auf den Management-Hub verfügen.
* Die Einheiten müssen über ein bereits installiertes Betriebssystem verfügen.
* Wenn Sie DHCP für Edge-Einheiten verwenden, muss jede Einheit bis zum Abschluss der Task dieselbe IP-Adresse (oder bei Verwendung von DDNS denselben `Hostnamen`) beibehalten.
* Alle Benutzereingaben für Edge-Services müssen in der Servicedefinition, im Muster oder in der Bereitstellungsrichtlinie als Standardwerte angegeben sein. Es können keine knotenspezifischen Benutzereingaben verwendet werden.

### Vorgehensweise
{: #proc-multiple}

1. Wenn noch nicht geschehen, rufen Sie die Datei **agentInstallFiles-&lt;edge-einheitentyp&gt;.tar.gz** und den API-Schlüssel ab oder erstellen Sie sie anhand der Anweisungen unter [Erforderliche Informationen und Dateien für Edge-Einheiten zusammenstellen](../../hub/gather_files.md#prereq_horizon). Legen Sie den Namen der Datei und des API-Schlüsselwerts in diesen Umgebungsvariablen fest:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-einheitentyp>.tar.gz
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. Das **pssh**-Paket enthält die Befehle **pssh** und **pscp**, mit denen Sie Befehle parallel an viele Edge-Einheiten ausgeben und ebenso parallel Dateien auf viele Edge-Einheiten kopieren können. Wenn Sie diese Befehle noch nicht auf diesem Host haben, installieren Sie das Paket jetzt:

  * Unter {{site.data.keyword.linux_notm}}:
    

   ```bash
   sudo apt install pssh
   alias pssh=parallel-ssh
   alias pscp=parallel-scp
   ```
   {: codeblock}

  * Unter {{site.data.keyword.macOS_notm}}:
    

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (Wenn **brew** noch nicht installiert ist, ziehen Sie den Abschnitt zur [Installation von pssh auf macOS-Computer mit Brew ![Wird in einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/) zurate.)

3. Sie können **pscp** und **pssh** auf unterschiedliche Weise den Zugriff auf Ihre Edge-Einheiten ermöglichen. In diesem Abschnitt wird die Verwendung eines öffentlichen SSH-Schlüssels beschrieben. Die erste Anforderung ist, dass dieser Host über ein SSH-Schlüsselpaar verfügen muss (zumeist in **~/.ssh/id_rsa** und **~/.ssh/id_rsa.pub**). Wenn noch keines vorhanden ist, generieren Sie es:

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. Ordnen Sie den Inhalt Ihres öffentlichen Schlüssels (**~/.ssh/id_rsa.pub**) auf jeder Edge-Einheit in **/root/.ssh/authorized_keys** an.

5. Erstellen Sie eine zweispaltige Zuordnungsdatei **node-id-mapping.csv**, in der die IP-Adresse oder der Hostname jeder Edge-Einheit dem {{site.data.keyword.ieam}}-Knotennamen zugeordnet wird, der ihr bei der Registrierung gegeben wurde. Wenn **agent-install.sh** auf jeder Edge-Einheit ausgeführt wird, liefert diese Datei die Informationen dazu, welcher Edge-Knotenname dieser Einheit gegeben werden soll. Verwenden Sie das CSV-Format:

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```
   {: codeblock}

6. Fügen Sie **node-id-mapping.csv** zur TAR-Datei des Agenten hinzu:

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. Ordnen Sie die Liste von Edge-Einheiten, die mittels Masseninstallation installiert und registriert werden sollen, in einer Datei mit dem Namen **nodes.hosts** an. Diese wird mit den Befehlen **pscp** und **pssh** verwendet werden. Jede Zeile sollte das Standard-SSH-Format `<user>@<IP-or-hostname>` aufweisen:

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```
   {: codeblock}

   Hinweis: Wenn Sie für einen der Hosts einen Benutzer ohne Rootberechtigung verwenden, muss 'sudo' so konfiguriert werden, dass dieser Benutzer 'sudo' ausführen kann, ohne ein Kennwort eingeben zu müssen.

8. Kopieren Sie die TAR-Datei des Agenten auf die Edge-Einheiten. Dieser Schritt kann einige Momente in Anspruch nehmen:

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   Hinweis: Wenn in der **pscp**-Ausgabe für eine der Edge-Einheiten die Nachricht  **[FAILURE]** ausgegeben wird, können Sie den Fehler in **/tmp/pscp-errors** anzeigen.

9. Führen Sie **agent-install.sh** auf jeder Edge-Einheit aus, um den Horizon-Agenten zu installieren und die Edge-Einheiten zu registrieren. Sie können die Edge-Einheiten mit einem Muster oder mit einer Richtlinie registrieren. Die Vorgehensweisen werden im Folgenden beschrieben. 

   1. Registrieren Sie die Edge-Einheiten mit einem Muster:

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Wenn Sie die Edge-Einheiten nicht mit dem Bereitstellungsmuster **IBM/pattern-ibm.helloworld** registrieren wollen, können Sie auch ein anderes Bereitstellungsmuster verwenden. Ändern Sie dazu die Flags **-p**, **-w** und **-o**. Um alle verfügbaren **agent-install.sh**-Flagbeschreibungen anzuzeigen, gehen Sie folgendermaßen vor:

      ```bash
tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
   ```
      {: codeblock}

   2. Registrieren Sie die Edge-Einheiten alternativ dazu mit einer Richtlinie. Erstellen Sie eine Knotenrichtlinie, kopieren Sie sie in die Edge-Einheiten und registrieren Sie die Einheiten mit dieser Richtlinie: 

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Zu diesem Zeitpunkt sind die Edge-Einheiten bereit; sie können jedoch erst mit dem Ausführen von Edge-Services beginnen, nachdem Sie eine Bereitstellungsrichtlinie (Geschäftsrichtlinie) erstellt haben, in der angegeben wird, dass für diesen Typ von Edge-Einheit ein Service bereitgestellt werden muss (im vorliegenden Beispiel sind dies Einheiten mit dem Knotentyp (**nodetype**) **special-node**). Weitere Einzelheiten finden Sie unter [Bereitstellungsrichtlinie verwenden](../using_edge_devices/detailed_policy.md).

10. Wenn in der **pssh**-Ausgabe für eine der Edge-Einheiten die Nachricht **[FAILURE]** ausgegeben wird, können Sie das Problem untersuchen, indem Sie zur Edge-Einheit wechseln und **/tmp/agent-install.log** anzeigen.

11. Während der Befehl **pssh** ausgeführt wird, können Sie den Status Ihrer Edge-Knoten in der {{site.data.keyword.edge_notm}}-Konsole anzeigen. Weitere Informationen hierzu finden Sie in [Managementkonsole verwenden](../getting_started/accessing_ui.md).
