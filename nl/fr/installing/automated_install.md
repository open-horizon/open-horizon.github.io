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

Remarque : Ces étapes sont identiques pour tous les types de dispositif de périphérie (architectures).

1. Si vous ne disposez pas déjà d'une clé d'API, créez-en une en suivant les étapes de la section [Création de votre clé d'API](../hub/prepare_for_edge_nodes.md). Ce processus crée une clé d'API, localise certains fichiers et regroupe les valeurs de variables d'environnement nécessaires lorsque vous configurez des noeuds de périphérie.

2. Connectez-vous au dispositif de périphérie et définissez les mêmes variables d'environnement que celles que vous avez obtenues à l'étape 1 :

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<votre-organisation-exchange>   export HZN_FSS_CSSURL=https://<entrée-concentrateur-gestion-ieam>/edge-css/
   ```
   {: codeblock}

3. Si vous n'utilisez pas un bundle d'installation préparé par l'administrateur, téléchargez le script **agent-install.sh** à partir de CSS (Cloud Sync Service) vers votre dispositif et rendez-le exécutable :

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data   chmod +x agent-install.sh
   ```
   {: codeblock}

4. Exécutez **agent-install.sh** pour obtenir les fichiers nécessaires à partir de CSS, installez et configurez l'agent {{site.data.keyword.horizon}}, puis enregistrez votre dispositif de périphérie pour exécuter l'exemple de service de périphérie helloworld :

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   Pour afficher la description de tous les indicateurs **agent-install.sh** disponibles, exécutez **./agent-install.sh -h**

   Remarque : Sur {{site.data.keyword.macOS_notm}}, l'agent sera exécuté dans un conteneur docker fonctionnant en tant que root.

5. Affichez la sortie helloworld :

   ```bash
   hzn service log -f ibm.helloworld   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. Si le service de périphérie helloworld ne démarre pas, exécutez la commande suivante pour afficher les messages d'erreur :

   ```bash
   hzn eventlog list -f   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (Facultatif) Utilisez la commande **hzn** sur ce noeud de périphérie pour afficher les services, les patterns et les règles de déploiement dans l'Exchange d'{{site.data.keyword.horizon}}. Renseignez vos informations spécifiques comme variables d'environnement dans votre shell et exécutez les commandes suivantes :

   ```bash
   eval export $(cat agent-install.cfg)   hzn exchange service list IBM/   hzn exchange pattern list IBM/   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. Explorez tous les indicateurs et sous-commandes de la commande **hzn** :

   ```bash
   hzn --help
   ```
   {: codeblock}

## Etapes suivantes

* Utilisez la console {{site.data.keyword.ieam}} pour afficher vos noeuds de périphérie (dispositifs), services, canevas et règles. Pour plus d'informations, voir [Utilisation de la console de gestion](../console/accessing_ui.md).
* Explorez et exécutez un autre exemple de service de périphérie. Pour plus d'informations, voir [Utilisation de l'unité centrale dans IBM Event Streams](../using_edge_services/cpu_load_example.md).
