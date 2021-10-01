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

# Procédure manuelle avancée d'installation et d'enregistrement d'un agent
{: #advanced_man_install}

La présente section décrit chacune des étapes manuelles requises pour installer et enregistrer l'agent {{site.data.keyword.edge_devices_notm}} sur un dispositif de périphérie. Si vous préférez utiliser une méthode automatisée, voir [Procédure automatique d'installation et d'enregistrement d'un agent](automated_install.md).
{:shortdesc}

## Installation de l'agent
{: #agent_install}

Remarque : Pour plus d'informations sur la syntaxe de commande, voir [Conventions de ce guide](../../getting_started/document_conventions.md).

1. Dans un premier temps, procurez-vous le fichier `agentInstallFiles-<edge-device-type>.tar.gz` ainsi que la clé d'interface de programmation créée en même temps que ce fichier.

    Un fichier compressé contenant les fichiers nécessaires à l'installation de l'agent {{site.data.keyword.horizon}} sur votre dispositif de périphérie et à son enregistrement à l'aide de l'exemple Hello world a été créé pour vous au moment de l'étape de post-configuration de la section [Installation du concentrateur de gestion](../../hub/offline_installation.md).

2. Copiez ce fichier sur le dispositif de périphérie à l'aide d'une clé USB, d'une commande de copie sécurisée ou d'une autre méthode.

3. Décompressez le fichier tar :

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. Suivez la section ci-dessous qui s'applique à votre type de dispositif de périphérie.

### Installation de l'agent sur des dispositifs de périphérie ou des machines virtuelles Linux (ARM 32 bits, ARM 64 bits ou x86_64)
{: #agent_install_linux}

Effectuez les étapes suivantes :

1. Connectez-vous en tant qu'utilisateur disposant de privilèges root :

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Interrogez la version Docker pour savoir si elle est suffisamment récente :

   ```bash
   docker --version
   ```
   {: codeblock}

      Si Docker n'est pas installé ou si la version est antérieure à la version `18.06.01`, installez la version la plus récente de Docker :

   ```bash
   curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. Installez les packages Horizon Debian que vous avez copiés sur ce dispositif de périphérie :

   ```bash
   apt update && apt install ./*horizon*.deb
   ```
   {: codeblock}
   
4. Renseignez vos informations spécifiques comme variables d'environnement :

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. Pointez l'agent Horizon de votre dispositif de périphérie vers votre cluster {{site.data.keyword.edge_notm}} en renseignant `/etc/default/horizon` avec les informations appropriées :

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Indiquez à l'agent Horizon de faire confiance au fichier `agent-install.crt`:

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. Redémarrez l'agent pour récupérer les modifications apportées à `/etc/default/horizon` :

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. Vérifiez que l'agent est en cours d'exécution et qu'il est correctement configuré :

   ```bash
   hzn version
       hzn exchange version
       hzn node list
   ```
   {: codeblock}  

      La sortie doit être similaire à ce qui suit (les numéros de version et adresses URL peuvent légèrement différer) :

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

9. Si vous avez déjà basculé vers un shell avec privilèges, fermez la fenêtre. Vous n'avez pas besoin de droits d'accès root pour l'étape suivante d'enregistrement de votre dispositif.

   ```bash
   exit
   ```
   {: codeblock}

10. Passez à l'étape [Enregistrement de l'agent](#agent_reg).

### Installation de l'agent sur un dispositif de périphérie macOS
{: #mac-os-x}

1. Importez le certificat du package `horizon-cli` dans votre chaîne de certificats {{site.data.keyword.macOS_notm}} :

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      Remarque : Vous devez exécuter cette étape une seule fois sur chaque machine {{site.data.keyword.macOS_notm}}. Une fois le certificat de confiance importé, vous pouvez installer n'importe quelle future version du logiciel {{site.data.keyword.horizon}}.

2. Installez le package d'interface de ligne de commande {{site.data.keyword.horizon}} :

   ```bash
   sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. La commande précédente ajoute les commandes dans le répertoire `/usr/local/bin`. Ajoutez ce répertoire au chemin d'accès à votre shell en ajoutant ceci à `~/.bashrc` :

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. Ajoutez `/usr/local/share/man` au chemin d'accès de votre page man en associant ce répertoire au chemin de votre shell en ajoutant ceci à `~/.bashrc`:

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. Activez l'exécution du nom de la sous-commande `hzn`, en ajoutant ceci à `~/.bashrc` :

  ```bash
  source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

6. Lorsque vous installez un **nouveau dispositif**, cette étape n'est **pas** nécessaire. En revanche, si vous avez déjà installé et démarré le conteneur Horizon sur cette machine, arrêtez-le à l'aide de la commande :

  ```bash
  horizon-container stop
  ```
  {: codeblock}
7. Renseignez vos informations spécifiques comme variables d'environnement :

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. Pointez l'agent Horizon de votre dispositif de périphérie vers votre cluster {{site.data.keyword.edge_notm}} en renseignant `/etc/default/horizon` avec les informations appropriées :

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

9. Démarrez l'agent {{site.data.keyword.horizon}} :

  ```bash
  horizon-container start
  ```
  {: codeblock}

10. Vérifiez que l'agent est en cours d'exécution et qu'il est correctement configuré :

  ```bash
  hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      La sortie doit être similaire à ce qui suit (les numéros de version et adresses URL peuvent légèrement différer) :

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

11. Passez à l'étape [Enregistrement de l'agent](#agent_reg).

## Enregistrement de l'agent
{: #agent_reg}

1. Renseignez vos informations spécifiques comme **variables d'environnement** :

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. Affichez la liste des exemples de patterns de déploiement de service de périphérie :

  ```bash
  hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. Le service de périphérie helloworld constitue l'exemple le plus élémentaire, ce qui en fait un parfait point de départ. **Enregistrez** votre dispositif de périphérie auprès de {{site.data.keyword.horizon}} pour exécuter le **pattern de déploiement helloworld** :

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  Remarque : L'ID de noeud qui figure dans la sortie à la ligne commence par **Utilisation de l'ID noeud**.

4. Le dispositif de périphérie conclura un accord avec l'un des bots d'accord {{site.data.keyword.horizon}} (ce processus dure environ 15 secondes). **Interrogez à plusieurs reprises les accords** de ce dispositif jusqu'à ce que les champs `agreement_finalized_time` et `agreement_execution_start_time` soient renseignés :

  ```bash
  hzn agreement list
  ```
  {: codeblock}

5. **Une fois l'accord conclu**, notez le service de périphérie du conteneur Docker qui a été démarré à la suite de cela :

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. Examinez la **sortie** du service de périphérie helloworld :

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## Etape suivante
{: #what_next}

Accédez à la rubrique [Utilisation de l'unité centrale sur IBM Event Streams](cpu_load_example.md) pour découvrir d'autres exemples de services de périphérie.
