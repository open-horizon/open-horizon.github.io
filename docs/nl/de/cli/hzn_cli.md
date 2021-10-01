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

Der Befehl `hzn` dient als Befehlszeilenschnittstelle von {{site.data.keyword.ieam}}. Bei der Installation der {{site.data.keyword.ieam}}-Agentensoftware auf einem Edge-Knoten wird automatisch die CLI `hzn` installiert. Sie können die CLI `hzn` jedoch auch ohne den Agenten installieren. Dies kann z. B. sinnvoll sein, wenn ein Edge-Administrator eine Abfrage für {{site.data.keyword.ieam}} Exchange plant oder ein Edge-Entwickler Tests mit `hzn**-Befehlen ohne den vollständigen Agenten beabsichtigt.

1. Rufen Sie das Paket `horizon-cli` ab. Abhängig von der Vorgehensweise Ihrer Organisation im Schritt [Edge-Knotendateien zusammenstellen](../hub/gather_files.md) können Sie das Paket `horizon-cli` von CSS oder in der TAR-Datei `agentInstallFiles-<edge-knotentyp>.tar.gz` erhalten:

   * Rufen Sie das Paket `horizon-cli` von CSS ab:

      * Wenn Sie noch nicht über einen API-Schlüssel verfügen, erstellen Sie einen, indem Sie die Schritte unter [API-Schlüssel erstellen](../hub/prepare_for_edge_nodes.md) befolgen. Legen Sie die Umgebungsvariablen anhand des folgenden Schrittes fest:

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-schlüssel>   export HZN_ORG_ID=<ihre_exchange-organisation>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
         ```
         {: codeblock}

      * Legen Sie für `HOST_TYPE` einen der folgenden Werte fest, der mit Typ des Hosts entspricht, auf dem Sie das Paket `horizon-cli` installieren möchten:

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<hosttyp>
         ```
         {: codeblock}

      * Laden Sie das Zertifikat, die Konfigurationsdatei und die TAR-Datei mit dem Paket `horizon-cli` von CSS herunter:

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * Extrahieren Sie das Paket `horizon-cli` aus der TAR-Datei:

         ```bash
         rm -f horizon-cli*   # remove any previous versions          tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * Alternativ finden Sie das Paket `horizon-cli` in der TAR-Datei `agentInstallFiles-<edge-knotentyp>.tar.gz`:

      * Fordern Sie die Datei `agentInstallFiles-<edge-knotentyp>.tar.gz` bei Ihrem Management-Hub-Administrator an. Dabei steht `<edge-knotentyp>` für den Host, auf dem `horizon-cli` installiert werden soll. Kopieren Sie diese Datei auf diesen Host.

      * Entpacken Sie die TAR-Datei:

         ```bash
         tar -zxvf agentInstallFiles-<edge-einheitentyp>.tar.gz
         ```
         {: codeblock}

2. Erstellen Sie das Verzeichnis `/etc/default/horizon` oder aktualisieren Sie es:

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon    sudo cp agent-install.crt /etc/horizon    sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. Installieren Sie das Paket `horizon-cli`:

   * Vergewissern Sie sich, dass die Paketversion der Version des Einheitenagenten in der Liste im Abschnitt [Komponenten](../getting_started/components.md) entspricht.

   * Debian-basierte Distribution:

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * RPM-basierte Distribution:

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * Unter {{site.data.keyword.macOS_notm}}:

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt      sudo installer -pkg horizon-cli-*.pkg -target /      pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## CLI 'hzn' deinstallieren

Gehen Sie wie folgt vor, wenn Sie das Paket `horizon-cli` auf einem Host entfernt werden soll:

* Deinstallation von `horizon-cli` unter einer Debian-basierten Distribution:

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Deinstallation von `horizon-cli` unter einer RPM-basierten Distribution:

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* Deinstallation von `horizon-cli` unter {{site.data.keyword.macOS_notm}}:

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
