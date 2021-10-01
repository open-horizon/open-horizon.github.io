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

# Installation de l'interface de ligne de commande hzn
{: #using_hzn_cli}

La commande `hzn` est l'interface de ligne de commande {{site.data.keyword.ieam}}. Lorsque vous installez le logiciel agent {{site.data.keyword.ieam}} sur une nœud de périphérie, la CLI `hzn` est installée automatiquement. Vous pouvez aussi installer la CLI `hzn` sans l'agent. Par exemple, un administrateur de périphérie peut vouloir interroger {{site.data.keyword.ieam}} Exchange, ou un développeur de périphérie peut vouloir effectuer des tests avec les commandes `hzn` sans l'agent complet.

1. Obtenez le package `horizon-cli`. Selon ce que votre organisation a effectué dans l'étape [Collecter les fichiers de nœud de périphérie](../hub/gather_files.md), vous pouvez obtenir le package `horizon-cli` à partir de CSS ou du fichier tar `agentInstallFiles-<edge-node-type>.tar.gz` :

   * Obtenez le package `horizon-cli` à partir de CSS :

      * Si vous ne disposez pas déjà d'une clé d'API, créez-en une en suivant les étapes de la section [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md). Définissez les variables d'environnement dans cette étape :

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<votre-organisation-exchange>   export HZN_FSS_CSSURL=https://<entrée-concentrateur-gestion-ieam>/edge-css/
         ```
         {: codeblock}

      * Affectez à `HOST_TYPE` l'une de ces valeurs qui correspond au type d'hôte sur lequel vous installez le package `horizon-cli` :

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * Téléchargez le certificat, le fichier de configuration et le fichier tar contenant le package `horizon-cli` à partir de CSS :

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * Extrayez le package `horizon-cli` à partir de son fichier tar :

         ```bash
         rm -f horizon-cli*   # remove any previous versions         tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * Vous pouvez également obtenir le package `horizon-cli` à partir du fichier tar `agentInstallFiles-<edge-node-type>.tar.gz` :

      * Obtenez le fichier `agentInstallFiles-<edge-node-type>.tar.gz` à partir de votre administrateur de concentrateur de gestion, où `<edge-node-type>` correspond à l'hôte sur lequel vous installez `horizon-cli`. Copiez ce fichier sur cet hôte.

      * Décompressez le fichier tar :

         ```bash
         tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
         ```
         {: codeblock}

2. Créez ou mettez à jour `/etc/default/horizon` :

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon   sudo cp agent-install.crt /etc/horizon   sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. Installez le package `horizon-cli` :

   * Confirmez que la version du package est identique à celle de l'agent du dispositif indiqué dans [Composants](../getting_started/components.md).

   * Sur une distribution Debian :

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * Sur une distro RPM :

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * Sous {{site.data.keyword.macOS_notm}} :

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt     sudo installer -pkg horizon-cli-*.pkg -target /     pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## Désinstallation de l'interface de ligne de commande hzn

Si vous voulez retirer le package `horizon-cli` d'un hôte :

* Désinstallez `horizon-cli` d'une distribution Debian :

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* Désinstallez `horizon-cli` d'une distro RPM :

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* Ou désinstallez `horizon-cli` de {{site.data.keyword.macOS_notm}} :

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
