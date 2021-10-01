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

# Automatisierte Agenteninstallation und -registrierung
{: #method_one}

Hinweis: Diese Schritte sind für alle Typen von Edge-Einheiten (Architekturen) identisch.

1. Wenn Sie noch nicht über einen API-Schlüssel verfügen, erstellen Sie einen, indem Sie die Schritte unter [API-Schlüssel erstellen](../hub/prepare_for_edge_nodes.md) befolgen. Durch diesen Vorgang wird ein API-Schlüssel erstellt. Außerdem werden bestimmte Dateien gesucht und Umgebungsvariablenwerte erfasst, die für die Einrichtung von Edge-Knoten erforderlich sind.

2. Melden Sie sich bei Ihrer Edge-Einheit an und legen Sie dieselben Umgebungsvariablen fest, die Sie in Schritt 1 abgerufen haben:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. Wenn Sie kein von einem Administrator vorbereitetes Installationspaket verwenden, laden Sie das Script **agent-install.sh** von Cloud Sync Service (CSS) auf Ihre Einheit herunter und machen Sie sie ausführbar:

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

4. Führen Sie das Script **agent-install.sh** aus, um die erforderlichen Dateien aus CSS abzurufen, den {{site.data.keyword.horizon}}-Agenten zu installieren und zu konfigurieren und die Edge-Einheit zu registrieren, um den Beispiel-Edge-Service 'helloworld' auszuführen:

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   Führen Sie den Befehl **./agent-install.sh -h** aus, um Beschreibungen aller verfügbaren Flags für **agent-install.sh** anzuzeigen.

   Hinweis: Unter {{site.data.keyword.macOS_notm}} wird der Agent in einem als Root ausgeführten Docker-Container ausgeführt.

5. Zeigen Sie die Ausgabe von 'helloworld' an:

   ```bash
   hzn service log -f ibm.helloworld   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. Wenn der Edge-Service 'helloworld' nicht gestartet wird, können Sie den folgenden Befehl ausführen, um die Fehlernachricht anzuzeigen:

   ```bash
   hzn eventlog list -f   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (Optional) Verwenden Sie auf diesem Knoten den Befehl **hzn**, um Services, Muster und Bereitstellungsrichtlinien in {{site.data.keyword.horizon}} Exchange anzuzeigen. Legen Sie Ihre jeweiligen Informationen in Ihrer Shell als Umgebungsvariablen fest und führen Sie die folgenden Befehle aus:

   ```bash
   eval export $(cat agent-install.cfg)   hzn exchange service list IBM/   hzn exchange pattern list IBM/   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. Informieren Sie sich über alle Befehlsflags und Unterbefehle von **hzn**:

   ```bash
   hzn --help
   ```
   {: codeblock}

## Weitere Schritte

* Verwenden Sie die {{site.data.keyword.ieam}}-Konsole, um Ihre Edge-Knoten (Einheiten), Services, Muster und Richtlinien anzuzeigen. Weitere Informationen finden Sie unter [Managementkonsole verwenden](../console/accessing_ui.md).
* Zeigen Sie ein weiteres Beispiel für einen Edge-Service an und führen Sie es aus. Weitere Informationen finden Sie unter [CPU-Auslastung für IBM Event Streams](../using_edge_services/cpu_load_example.md).
