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

# Procédure automatique d'installation et d'enregistrement d'un agent
{: #method_one}

Remarque : Ces étapes sont identiques pour tous les types de dispositifs (architectures).

1. Procurez-vous le fichier **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** et une clé d'interface de programmation (clé d'API) auprès de votre administrateur. Ceux-ci doivent avoir été créés à la section [Collecte des informations et des fichiers nécessaires aux dispositifs de périphérie](../../hub/gather_files.md#prereq_horizon). Copiez ce fichier sur votre dispositif de périphérie à l'aide d'une commande de copie sécurisée, d'une clé USB ou d'une autre méthode. Notez également la valeur de la clé d'interface de programmation. Vous en aurez besoin plus tard. Définissez ensuite le nom de fichier dans une variable d'environnement pour les étapes suivantes :

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

2. Extrayez la commande **agent-install.sh** du fichier tar :

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. Exportez vos données d'identification {{site.data.keyword.horizon}} Exchange (la clé d'API) :

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. Exécutez la commande **agent-install.sh** pour installer et configurer l'agent {{site.data.keyword.horizon}} et pour enregistrer votre dispositif de périphérie afin qu'il exécute l'exemple de service de périphérie helloworld :

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  Remarque : Lors de l'installation des packages d'agent, il se peut que le système vous demande si vous voulez écraser la configuration du noeud actuelle : "Do you want to overwrite the current node configuration?`[y/N]`:" Vous pouvez choisir "y" et appuyer sur la touche Entrée, car la commande **agent-install.sh** procédera à la nouvelle configuration.

  Pour afficher la description de tous les indicateurs **agent-install.sh** :

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. Maintenant que votre dispositif de périphérie est installé et enregistré, définissez vos informations spécifiques comme variables d'environnement dans votre shell. Vous pouvez ainsi exécuter la commande **hzn** pour afficher la sortie helloworld :

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  Remarque : Appuyez sur **Ctrl** **C** pour arrêter l'affichage de la sortie.

6. Passez en revue les indicateurs et les sous-commandes de la commande **hzn** :

  ```bash
  hzn --help
  ```
  {: codeblock}

7. Vous pouvez également afficher vos noeuds de périphérie (dispositifs), services, patterns et règles à l'aide de la console d'{{site.data.keyword.ieam}}. Voir [Utilisation de la console de gestion](../getting_started/accessing_ui.md).

8. Accédez à la rubrique [Utilisation de l'unité centrale sur IBM Event Streams](cpu_load_example.md) pour découvrir d'autres exemples de services de périphérie.
