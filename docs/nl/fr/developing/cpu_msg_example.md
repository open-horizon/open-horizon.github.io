---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Unité centrale vers le service {{site.data.keyword.message_hub_notm}}
{: #cpu_msg_ex}

Cet exemple collecte des informations relatives au pourcentage de charge de l'unité centrale à envoyer à {{site.data.keyword.message_hub_notm}}. Servez-vous en pour vous aider à développer vos propres applications de périphérie destinées à envoyer des données aux services cloud.
{:shortdesc}

## Avant de commencer
{: #cpu_msg_begin}

Effectuez les étapes préalables décrites dans la section [Préparation de la création d'un service de périphérie](service_containers.md). Ainsi, les variables d'environnement ci-dessous doivent être définies, les commandes doivent être installées et les fichiers doivent exister :

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procédure
{: #cpu_msg_procedure}

Cet exemple fait partie du projet open source [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Suivez les étapes de la page [Building and Publishing Your Own Version of the CPU To IBM Event Streams Edge Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service), puis revenez ici.

## Enseignements tirés de cet exemple

### Services requis

Le service de périphérie cpu2evtstreams est un exemple de service qui dépend de deux autres services de périphérie (**cpu** et **gps**) pour accomplir sa tâche. Vous pouvez consulter le détail de ces dépendances dans la section **requiredServices** du fichier **horizon/service.definition.json** :

```json
    "requiredServices": [         {
            "url": "ibm.cpu",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",             "org": "IBM",             "versionRange": "[0.0.0,INFINITY)",             "arch": "$ARCH"         }
    ],
```
{: codeblock}

### Variables de configuration
{: #cpu_msg_config_var}

Le service **cpu2evtstreams** doit être configuré avant de pouvoir être exécuté. Les services de périphérie peuvent déclarer des variables de configuration, en indiquant leur type et en fournissant les valeurs par défaut. Ces variables de configuration se trouvent dans le fichier **horizon/service.definition.json**, à la section **userInput** :

```json  
    "userInput": [         {
            "name": "EVTSTREAMS_API_KEY",             "label": "The API key to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",             "label": "The comma-separated list of URLs to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",             "label": "The base64-encoded self-signed certificate to use when sending messages to your ICP instance of IBM Event Streams. Not needed for IBM Cloud Event Streams.",             "type": "string",             "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",             "label": "The topic to use when sending messages to your instance of IBM Event Streams",             "type": "string",             "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",             "label": "the number of samples to read before calculating the average",             "type": "int",             "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",             "label": "the number of seconds between samples",             "type": "int",             "defaultValue": "2"
        },
        {
            "name": "MOCK",             "label": "mock the CPU sampling",             "type": "boolean",             "defaultValue": "false"
        },
        {
            "name": "PUBLISH",             "label": "publish the CPU samples to IBM Event Streams",             "type": "boolean",             "defaultValue": "true"
        },
        {
            "name": "VERBOSE",             "label": "log everything that happens",             "type": "string",             "defaultValue": "1"         }
    ],
```
{: codeblock}

Des variables de configuration avec entrée utilisateur telles que celles mentionnées ci-dessus sont requises pour avoir des valeurs lors du démarrage du service de périphérie sur le noeud correspondant. Ces valeurs peuvent provenir de n'importe quelle source (dans l'ordre de priorité suivant) :

1. Un fichier d'entrée utilisateur spécifié avec l'indicateur **hzn register -f**
2. La section **userInput** de la ressource du noeud de périphérie dans Exchange
3. La section **userInput** du pattern ou de la ressource de la règle de déploiement dans Exchange
4. La valeur par défaut spécifiée dans la ressource de définition de service Exchange

Lorsque vous avez enregistré votre dispositif de périphérie pour ce service, vous avez fourni un fichier **userinput.json** dont certaines variables de configuration ne comportaient pas de valeurs par défaut.

### Conseils de développement
{: #cpu_msg_dev_tips}

Le fait d'intégrer des variables de configuration dans votre service peut s'avérer particulièrement utile pour vous aider à tester et à déboguer le service. Par exemple, les métadonnées (**service.definition.json**) et le code (**service.sh**) de ce service font appel aux variables de configuration ci-dessous :

* La variable **VERBOSE** augmente le volume d'informations consignées lors de son exécution.
* La variable **PUBLISH** vérifie si le code tente d'envoyer des messages à {{site.data.keyword.message_hub_notm}}.
* La variable **MOCK** vérifie si le fichier **service.sh** tente d'appeler les interfaces de programmation REST de ses dépendances (les services **cpu** et **gps**) ou tente de créer lui-même des données fictives.

Bien que facultative, l'approche qui consiste à prévoir les services dont vous avez besoin peut se montrer efficace pour développer et tester des composants dans un milieu totalement isolé des services requis. Elle peut aussi permettre de développer un service sur un type de dispositif qui ne comporte aucun matériel de détection ni de régulation.

La capacité à désactiver l'interaction avec les services cloud peut être pratique lors des phases de développement et de test afin d'éviter toutes charges inutiles et de faciliter les tests dans un environnement DevOps synthétique.

## Etape suivante
{: #cpu_msg_what_next}

* Testez les autres exemples de service de périphérie de la rubrique [Développement de services de périphérie avec {{site.data.keyword.edge_notm}}](../OH/docs/developing/developing.md).
