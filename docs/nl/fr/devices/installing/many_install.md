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

# Procédure d'installation et d'enregistrement d'un agent en bloc
{: #batch-install}

Utilisez la procédure d'installation en bloc pour configurer plusieurs dispositifs de périphérie de types similaires (autrement dit, ayant la même architecture, le même système d'exploitation, le même pattern ou la même règle).

Remarque : Les dispositifs de périphérie cible de type macOs ne sont pas pris en charge dans le cadre de ce processus. Vous pouvez cependant exécuter ce processus depuis un ordinateur macOs, si vous le souhaitez. (Autrement dit, cet hôte peut être un ordinateur macOs.)

### Prérequis

* Les dispositifs à installer et à enregistrer doivent disposer d'un accès réseau au concentrateur de gestion.
* Les dispositifs doivent déjà avoir un système d'exploitation installé.
* Si vous utilisez le protocole DHCP pour les dispositifs de périphérie, chaque dispositif doit conserver la même adresse IP jusqu'à ce que la tâche soit terminée (ou le même `nom d'hôte` si vous utilisez DDNS).
* Toutes les entrées utilisateur concernant le service de périphérie doivent être spécifiées comme valeurs par défaut dans la définition de service, dans le pattern ou dans la règle de déploiement. Les entrées utilisateurs qui ne sont pas spécifiques à un noeud ne peuvent pas être utilisées.

### Procédure
{: #proc-multiple}

1. Si ce n'est pas déjà fait, obtenez ou créez le fichier **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** et la clé d'API en suivant les instructions de la section [Collecte des informations et des fichiers nécessaires aux dispositifs de périphérie](../../hub/gather_files.md#prereq_horizon). Indiquez le nom du fichier et la valeur de clé d'API dans les variables d'environnement suivantes :

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. Le package **pssh** inclut les commandes **pssh** et **pscp** pour vous permettre d'exécuter des commandes et de copier les fichiers sur plusieurs dispositifs de périphérie en parallèle. Si ces commandes n'existent pas sur cet hôte, installez le package dès maintenant :

  * Sous {{site.data.keyword.linux_notm}} :

   ```bash
   sudo apt install pssh
   alias pssh=parallel-ssh
   alias pscp=parallel-scp
   ```
   {: codeblock}

  * Sous {{site.data.keyword.macOS_notm}} :

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (Si **brew** n'est pas encore installé, voir [Install pssh on macOs computer with Brew ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/).)

3. Les programmes **pscp** et **pssh** peuvent accéder à vos dispositifs de périphérie de plusieurs manières. Cette section décrit l'utilisation d'une clé publique ssh. La première exigence est que cet hôte doit avoir une paire de clés ssh (généralement dans **~/.ssh/id_rsa** et **~/.ssh/id_rsa.pub**). Si aucune paire de clés n'existe, générez-en une :

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. Placez le contenu de votre clé publique (**~/.ssh/id_rsa.pub**) sur chaque dispositif de périphérie dans **/root/.ssh/authorized_keys**.

5. Créez un fichier de mappage à deux colonnes intitulé **node-id-mapping.csv** qui mappe chaque adresse IP ou nom d'hôte de dispositif de périphérie sur le nom de noeud {{site.data.keyword.ieam}} à indiquer lors de l'enregistrement. Lorsque **agent-install.sh** s'exécute sur chaque dispositif de périphérie, ce fichier indique quel nom attribuer à ce dispositif. Utilisez un format CSV comme suit :

   ```bash
   Hostname/IP, Node Name
   1.1.1.1, factory2-1
   1.1.1.2, factory2-2
   ```
   {: codeblock}

6. Ajoutez **node-id-mapping.csv** au fichier tar de l'agent :

   ```bash
   gunzip $AGENT_TAR_FILE
   tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv
   gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. Placez la liste des dispositifs de périphérie que vous souhaitez installer et enregistrer en bloc dans un ficher appelé **nodes.hosts**. Ceux-ci seront utilisés par les commandes **pscp** et **pssh**. Chaque ligne doit être au format ssh standard `<user>@<IP-or-hostname>` :

   ```bash
   root@1.1.1.1
   root@1.1.1.2
   ```
   {: codeblock}

   Remarque : Si vous utilisez un utilisateur non root pour l'un des hôtes, sudo doit être configuré pour permettre à l'utilisateur de l'exécuter sans avoir à saisir de mot de passe.

8. Copiez le fichier tar de l'agent sur les dispositifs de périphérie. Cette étape peut prendre quelques instants :

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   Remarque : Si vous obtenez le message **[FAILURE]** dans la sortie **pscp** pour l'un des dispositifs de périphérie, vous pouvez consulter les erreurs dans **/tmp/pscp-errors**.

9. Exécutez **agent-install.sh** sur chaque dispositif de périphérie pour installer l'agent Horizon et enregistrer les dispositifs de périphérie. vous pouvez enregistrer le dispositif de périphérie à l'aide 'un pattern ou d'une règle :

   1. Enregistrer les dispositifs de périphérie avec un pattern :

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Plutôt que d'enregistrer les dispositifs de périphérie avec le pattern de déploiement **IBM/pattern-ibm.helloworld**, vous pouvez utiliser un autre pattern de déploiement en modifiant les indicateurs **-p**, **-w** et **-o**. Pour afficher la description de tous les indicateurs **agent-install.sh** :

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. Ou bien, enregistrez les dispositifs de périphérie avec la règle. Créez une règle de noeud, copiez-la sur les dispositifs de périphérie, puis enregistrez les dispositifs avec cette règle :

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json
      pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      A ce stade, les dispositifs de périphérie sont prêts mais ne démarreront pas tant que vous n'aurez pas créé une règle de déploiement (règle métier) spécifiant qu'un service doit être déployé sur ce type de dispositif de périphérie (dans cet exemple, les dispositifs avec **nodetype** de **special-node**). Voir [Utilisation d'une règle de déploiement](../using_edge_devices/detailed_policy.md) pour plus de détails.

10. Si **[FAILURE]** s'affiche dans la sortie **pssh** pour l'un des dispositifs de périphérie, vous pouvez enquêter sur le problème en accédant au dispositif de périphérie et en consultant le fichier **/tmp/agent-install.log**.

11. Pendant l'exécution de la commande **pssh**, vous pouvez afficher le statut de vos noeuds de périphérie dans la console {{site.data.keyword.edge_notm}}. Voir [Utilisation de la console de gestion](../getting_started/accessing_ui.md).
