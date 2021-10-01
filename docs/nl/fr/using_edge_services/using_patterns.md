---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilisation de patterns
{: #using_patterns}

Généralement, vous pouvez publier des patterns de déploiement de service sur le concentrateur d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) après qu'un développeur a publié un service de périphérie dans Horizon Exchange.

L'interface de ligne de commande hzn intègre des fonctionnalités permettant de lister et de gérer des patterns dans {{site.data.keyword.horizon_exchange}}, notamment des commandes pour lister, vérifier, mettre à jour et retire des patterns de déploiement d'un service. Elle offre également le moyen de répertorier et de retirer les clés cryptographiques qui sont associées à un pattern de déploiement spécifique.

Pour obtenir la liste complète des commandes de l'interface de ligne de commande et des détails supplémentaires :

```
hzn exchange pattern -h
```
{: codeblock}

## Exemple

Signez et créez (ou mettez à jour) une ressource de pattern dans {{site.data.keyword.horizon_exchange}} :

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## Utilisation de patterns de déploiement

L'utilisation d'un pattern de déploiement constitue une manière simple et directe de déployer un service sur votre noeud de périphérie. Vous spécifiez un ou plusieurs services de niveau supérieur à déployer sur votre noeud de périphérie et {{site.data.keyword.ieam}} s'occupe du reste, notamment le déploiement des services dépendants.

Après avoir créé et ajouté un service à {{site.data.keyword.ieam}} Exchange, vous devez créer un fichier `pattern.json` semblable à ce qui suit :

```
{
  "IBM/pattern-ibm.cpu2evtstreams": {
    "owner": "root/root",     "label": "Edge ibm.cpu2evtstreams Service Pattern for arm architectures",     "description": "Pattern for ibm.cpu2evtstreams sending cpu and gps info to the IBM Event Streams",     "public": true,     "services": [       {
        "serviceUrl": "ibm.cpu2evtstreams",       "serviceOrgid": "IBM",       "serviceArch": "arm",       "serviceVersions": [         {
            "version": "1.4.3",             "priority": {},             "upgradePolicy": {}           }
        ],         "dataVerification": {
          "metering": {}
        },         "nodeHealth": {
          "missing_heartbeat_interval": 1800,           "check_agreement_status": 1800         }
      }
    ],     "agreementProtocols": [       {
        "name": "Basic"       }
    ],     "lastUpdated": "2020-10-24T14:46:44.341Z[UTC]"
  }
}
```
{: codeblock}

Le code ci-dessus est un exemple de fichier `pattern.json` pour le service `ibm.cpu2evtstreams` de dispositifs `arm`. Comme vous pouvez le constater, il est inutile de spécifier `cpu_percent` et `gps` (services dépendants de `cpu2evtstreams`). Cette tâche étant prise en charge par le fichier `service_definition.json`, un noeud de périphérie correctement enregistré exécute ces charges de travail automatiquement.

Le fichier `pattern.json` vous permet de personnaliser les paramètres d'annulation dans la section `serviceVersions`. Vous pouvez indiquer plusieurs anciennes versions de votre service et attribuer à chacune un ordre de priorité de restauration en cas d'erreur avec la nouvelle version. Outre l'affectation d'une priorité, vous pouvez indiquer le nombre et la durée des tentatives avant de passer à une version du service avec une priorité inférieure. 

Vous pouvez aussi définir les variables de configuration nécessaires au bon fonctionnement central de votre service lorsque vous publiez votre pattern de déploiement en incluant ces variables dans la section `userInput` vers le bas. Lorsque le service `ibm.cpu2evtstreams` est publié, il transmet également les données d'identification requises pour publier les données sur IBM Event Streams, à l'aide par exemple de la commande :

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

Une fois le pattern publié, vous pouvez enregistrer un dispositif arm auprès de lui :

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

Cette commande déploie `ibm.cpu2evtstreams` et tous les services dépendants de votre noeud.

Remarque : un fichier `userInput.json` n'est pas transmis à la commande `hzn register` ci-dessus, comme il le serait si vous suiviez les étapes décrites dans l'exemple de référentiel [Using the CPU To IBM Event Streams Edge Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern). Les entrées de l'utilisateur ayant été transmises avec le pattern lui-même, tous les noeuds de périphérie qui s'enregistrent automatiquement ont accès à ces variables d'environnement.

Vous pouvez arrêter toutes les charges de travail `ibm.cpu2evtstreams` en annulant l'enregistrement :

```
hzn unregister -fD
```
{: codeblock}
