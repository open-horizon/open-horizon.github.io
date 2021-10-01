---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CLI 'hzn' installieren
{: #using_hzn_cli}

Bei der Installation der {{site.data.keyword.ieam}}-Agentensoftware auf einem Edge-Knoten wird automatisch die CLI **hzn** installiert. Sie können die CLI **hzn** jedoch auch ohne den Agenten installieren. Dies kann z. B. sinnvoll sein, wenn ein Edge-Administrator eine Abfrage für {{site.data.keyword.ieam}} Exchange plant oder ein Edge-Entwickler die Ausführung von Tests mit **hzn dev**-Befehlen beabsichtigt.

1. Besorgen Sie sich die Datei **agentInstallFiles-&lt;edge-einheitentyp&gt;.tar.gz** bei Ihrem Management-Hub-Administrator. Dabei entspricht **&lt;edge-einheitentyp&gt;** dem Host, auf dem **hzn** installiert werden soll. Die Datei sollte bereits wie im Abschnitt [Erforderliche Informationen und Dateien für Edge-Einheiten zusammenstellen](../../hub/gather_files.md#prereq_horizon) beschrieben erstellt worden sein. Kopieren Sie diese Datei auf den Host, auf dem **hzn** installiert werden soll.

2. Legen Sie den Dateinamen für nachfolgende Schritte in einer Umgebungsvariablen fest:

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-einheitentyp>.tar.gz
   ```
   {: codeblock}

3. Extrahieren Sie das Horizon-Paket mit der Befehlszeilenschnittstelle aus der TAR-Datei:

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * Vergewissern Sie sich, dass die Paketversion der Version des Einheitenagenten in der Liste im Abschnitt [Komponenten](../getting_started/components.md) entspricht.

4. Installieren Sie das Paket **horizon-cli**:

   * Debian-basierte Distribution:

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * {{site.data.keyword.macOS_notm}}:
    

     ```bash
      sudo installer -pkg horizon-cli-*.pkg -target /
      ```
     {: codeblock}

     Hinweis: Unter {{site.data.keyword.macOS_notm}} können Sie die Horizon-Paketdatei mit der Befehlszeilenschnittstelle auch über den Finder installieren: Klicken Sie doppelt auf die Datei, um das Installationsprogramm zu öffnen. Wenn Sie eine Fehlernachricht erhalten, die besagt, dass das Programm nicht geöffnet werden kann, da es von einem nicht verifizierten Entwickler stammt, klicken Sie mit der rechten Maustaste auf die Datei und wählen Sie **Öffnen** aus. Klicken Sie, wenn Sie dazu aufgefordert werden, erneut auf **Öffnen**, um zu bestätigen, dass die Datei geöffnet werden soll. Folgen Sie anschließend den Eingabeaufforderungen, um das Paket mit der Horizon-CLI zu installieren. Stellen Sie sicher, dass Ihre ID über Administratorberechtigungen verfügt.

## CLI 'hzn' deinstallieren

Gehen Sie wie folgt vor, wenn Sie das Paket **horizon-cli** auf einem Host entfernt werden soll:

* Deinstallation von **horizon-cli** unter einer Debian-basierten Distribution:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Deinstallation von **horizon-cli** unter {{site.data.keyword.macOS_notm}}:

  * Öffnen Sie den hzn-Clientordner (/usr/local/bin) und ziehen Sie die App `hzn` in den Papierkorb (am Ende des Docks).
