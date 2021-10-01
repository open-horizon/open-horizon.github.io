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

# Installation et enregistrement d'agents en bloc
{: #batch-install}

Utilisez le processus d'installation en bloc pour configurer plusieurs dispositifs de périphérie de types similaires (en d'autres termes, ayant la même architecture, le même système d'exploitation, le même pattern ou la même règle).

**Remarque** :  les dispositifs de périphérie cible qui sont des ordinateurs de macOs ne sont pas pris en charge. Toutefois, vous pouvez piloter ce processus à partir d'un ordinateur macOs, si vous le souhaitez. (Autrement dit, cet hôte peut être un ordinateur macOs.)

### Prérequis

* Les dispositifs à installer et à enregistrer doivent disposer d'un accès réseau au concentrateur de gestion.
* Les dispositifs doivent avoir un système d'exploitation installé.
* Si vous utilisez le protocole DHCP pour les dispositifs de périphérie, chaque dispositif doit conserver la même adresse IP jusqu'à ce que la tâche soit terminée (ou le même `nom d'hôte` si vous utilisez DDNS).
* Toutes les entrées utilisateur concernant le service de périphérie doivent être spécifiées comme valeurs par défaut dans la définition de service, dans le pattern ou dans la règle de déploiement. Les entrées utilisateurs qui ne sont pas spécifiques à un noeud ne peuvent pas être utilisées.

### Procédure
{: #proc-multiple}

1. Si vous n'avez pas obtenu ou créé le fichier **agentInstallFiles-<edge-device-type>.tar.gz** et la clé d'API en suivant la procédure de la section [Collecte des informations et fichiers nécessaires pour les dispositifs de périphérie](../hub/gather_files.md#prereq_horizon), faites-le maintenant. Indiquez le nom du fichier et la valeur de clé d'API dans les variables d'environnement suivantes :

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. Le package **pssh** inclut les commandes **pssh** et **pscp** pour vous permettre d'exécuter des commandes et de copier les fichiers sur plusieurs dispositifs de périphérie en parallèle. Si ces commandes ne figurent pas sur cet hôte, installez le package maintenant :

  * Sous {{site.data.keyword.linux_notm}} :

   ```bash
   sudo apt install pssh    alias pssh=parallel-ssh    alias pscp=parallel-scp
   ```
   {: codeblock}

  * Sous {{site.data.keyword.macOS_notm}} :

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (Si **brew** n'est pas encore installé, voir [Install pssh on macOs computer with Brew](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/).)

3. Pour donner à **pscp** et à **pssh** l'accès à vos dispositifs de périphérie, vous pouvez procéder de plusieurs manières. Ce contenu explique comment utiliser une clé publique ssh. Tout d'abord, cet hôte doit disposer d'une paire de clés ssh (généralement dans **~/.ssh/id_rsa** et **~/.ssh/id_rsa.pub**). S'il ne dispose pas d'une paire de clés ssh, générez-la :

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. Placez le contenu de votre clé publique (**~/.ssh/id_rsa.pub**) sur chaque dispositif de périphérie dans **/root/.ssh/authorized_keys**.

5. Créez un fichier de mappage à deux colonnes intitulé **node-id-mapping.csv** qui mappe chaque adresse IP ou nom d'hôte de dispositif de périphérie sur le nom de noeud {{site.data.keyword.ieam}} à indiquer lors de l'enregistrement. Lorsque **agent-install.sh** s'exécute sur chaque dispositif de périphérie, ce fichier indique quel nom attribuer à ce dispositif. Utilisez un format CSV comme suit :

   ```bash
   Hostname/IP, Node Name    1.1.1.1, factory2-1    1.1.1.2, factory2-2
   ```
   {: codeblock}

6. Ajoutez **node-id-mapping.csv** au fichier tar de l'agent :

   ```bash
   gunzip $AGENT_TAR_FILE    tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv    gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. Placez la liste des dispositifs de périphérie que vous souhaitez installer et enregistrer en bloc dans un ficher appelé **nodes.hosts**. Ceux-ci seront utilisés par les commandes **pscp** et **pssh**. Chaque ligne doit être au format ssh standard `<user>@<IP-or-hostname>` :

   ```bash
   root@1.1.1.1    root@1.1.1.2
   ```
   {: codeblock}

   **Remarque** : si vous utilisez un utilisateur non-root pour l'un des hôtes, sudo doit être configuré pour autoriser sudo pour l'utilisateur sans avoir à saisir de mot de passe.

8. Copiez le fichier tar de l'agent sur les dispositifs de périphérie. Cette étape peut prendre quelques instants :

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   **Remarque** : si vous obtenez **[FAILURE]** dans la sortie **pscp** pour n'importe quels dispositifs de périphérie, les erreurs figurent dans **/tmp/pscp-errors**.

9. Exécutez **agent-install.sh** sur chaque dispositif de périphérie pour installer l'agent Horizon et enregistrer les dispositifs de périphérie. Vous pouvez utiliser un canevas ou une règle pour enregistrer les dispositifs de périphérie :

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
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json       pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp       pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      Les dispositifs de périphérie sont maintenant prêts mais ils ne vont pas démarrer les services de périphérie tant que vous n'avez pas créé une règle de déploiement (règle métier) indiquant qu'un service doit être déployé sur ce type de dispositif de périphérie (dans cet exemple, les dispositifs dont le**type de noeud** est **special-node**). Voir [Utilisation d'une règle de déploiement](../using_edge_services/detailed_policy.md) pour plus de détails.

10. Si **[FAILURE]** s'affiche dans la sortie **pssh** pour l'un des dispositifs de périphérie, vous pouvez enquêter sur le problème en accédant au dispositif de périphérie et en consultant le fichier **/tmp/agent-install.log**.

11. Pendant l'exécution de la commande **pssh**, vous pouvez afficher le statut de vos noeuds de périphérie dans la console {{site.data.keyword.edge_notm}}. Voir [Utilisation de la console de gestion](../console/accessing_ui.md).
