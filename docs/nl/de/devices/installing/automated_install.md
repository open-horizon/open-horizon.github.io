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

Hinweis: Diese Schritte sind für alle drei Einheitentypen (Architekturen) identisch.

1. Fordern Sie die Datei **agentInstallFiles-&lt;edge-einheitentyp&gt;.tar.gz** und einen API-Schlüssel von Ihrem Administrator an. Diese sollten bereits im Abschnitt [Erforderliche Informationen und Dateien für Edge-Einheiten zusammenstellen](../../hub/gather_files.md#prereq_horizon) erstellt worden sein. Kopieren Sie diese Datei mit dem Befehl für Secure Copy, mit einem USB-Stick oder einer anderen Methode auf Ihre Edge-Einheit. Notieren Sie sich auch den Wert des API-Schlüssels. Dieser Wert wird in einem nachfolgenden Schritt benötigt. Legen Sie anschließend für nachfolgende Schritte den Dateinamen in einer Umgebungsvariablen fest:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-einheitentyp>.tar.gz
   ```
   {: codeblock}

2. Extrahieren Sie den Befehl **agent-install.sh** aus der TAR-Datei:

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. Exportieren Sie Ihre {{site.data.keyword.horizon}} Exchange-Benutzerberechtigungsnachweise (den API-Schlüssel):

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. Führen Sie den Befehl **agent-install.sh** aus, um den {{site.data.keyword.horizon}}-Agenten zu installieren und zu konfigurieren und um die Edge-Einheit für die Ausführung des Beispiel-Edge-Service 'helloworld' zu registrieren: 

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  Hinweis: Während der Installation des Agentenpakets wird möglicherweise die folgende Frage angezeigt: "Möchten Sie die aktuelle Knotenkonfiguration überschreiben?`[J/N]`:" Sie können "J" eingeben und die Eingabetaste drücken, da mit **agent-install.sh** die Konfiguration korrekt eingerichtet wird.

  Um alle verfügbaren **agent-install.sh**-Flagbeschreibungen anzuzeigen, gehen Sie folgendermaßen vor:

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. Nachdem nun Ihre Edge-Einheit installiert und registriert ist, legen Sie Ihre spezifischen Informationen als Umgebungsvariablen in der Shell fest. Dies gibt Ihnen die Möglichkeit, den Befehl **hzn** auszuführen, um die 'Hello World'-Ausgabe anzuzeigen:

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  Hinweis: Drücken Sie **Strg** **C**, wenn die Ausgabeanzeige gestoppt werden soll.

6. Informieren Sie sich über die Flags und Unterbefehle des Befehls **hzn**:

  ```bash
  hzn --help
  ```
  {: codeblock}

7. Sie können Ihre Edge-Knoten (Einheiten), Services, Muster und Richtlinien auch über die {{site.data.keyword.ieam}}-Konsole anzeigen. Weitere Informationen hierzu finden Sie in [Managementkonsole verwenden](../getting_started/accessing_ui.md).

8. Navigieren Sie zu [CPU-Auslastung für IBM Event Streams](cpu_load_example.md), um mit weiteren Edge-Service-Beispielen fortzufahren.
