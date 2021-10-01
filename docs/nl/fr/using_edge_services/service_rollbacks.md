---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Mise à jour d'un service de périphérie avec restauration de la version précédente
{: #service_rollback}

Les services installés sur les noeuds de périphérie exécutent généralement des fonctions critiques, c'est pourquoi lorsqu'une nouvelle version d'un service de périphérie est déployée vers un grand nombre de noeuds de périphérie, il convient de surveiller le succès de l'opération, et en cas d'échec sur l'un des noeuds de périphérie, de rétablir l'ancienne version du service de périphérie. {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) peut effectuer cette opération automatiquement. Dans les patterns ou les règles de déploiement, vous pouvez définir quelles versions de service précédentes doivent être utilisées lorsqu'une nouvelle version de service ne peut pas être déployée.

Le contenu ci-dessous fournit des détails supplémentaires sur la manière de déployer une nouvelle version d'un service de périphérie, et indique les meilleures pratiques de développement logiciel visant à mettre à jour les paramètres de restauration dans le pattern ou les règles de déploiement.

## Création d'une définition de service de périphérie
{: #creating_edge_service_definition}

Comme expliqué dans les sections [Développer un service périphérique pour les appareils](../OH/docs/developing/developing.md) et [Détails du développement](../developing/developing_details.md), les principales étapes pour publier une nouvelle version d'un service périphérique sont les suivantes :

- Modifiez le code de service de périphérie comme requis pour la nouvelle version.
- Modifiez le numéro de version du code dans la variable de la version de service dans le fichier de configuration **hzn.json**.
- Regénérez vos conteneurs de services.
- Signez et publiez la nouvelle version de service de périphérie dans Horizon Exchange.

## Mise à jour des paramètres de restauration dans un pattern ou une règle de déploiement
{: #updating_rollback_settings}

Le numéro de version d'un nouveau service de périphérie est disponible dans la zone `version` de la définition de service.  

Des patterns ou des règles de déploiement déterminent quels services sont déployés sur quels noeuds de périphérie. Pour utiliser les fonctions de restauration d'un service de périphérie, vous devez ajouter la référence du numéro de version du nouveau service dans la section **serviceVersions** du fichier de configuration du pattern ou de la règle de déploiement.

Lorsqu'un service de périphérie est déployé sur un noeud de périphérie à la suite d'un pattern ou d'une règle, l'agent déploie la version de service ayant la priorité la plus élevée.

Par exemple :

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
 {
   "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
  {
   "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

Des variables supplémentaires sont fournies dans la section de priorité.La propriété `priority_value` définit l'ordre dans lequel les versions de service seront essayées, à savoir un nombre plus petit représente une priorité plus élevée. La valeur de variable `retries` définit le nombre de fois auquel Horizon tente de démarrer cette version de service dans le délai indiqué par `retry_durations` avant de rétablir la version suivante avec la priorité la plus élevé. La variable `retry_durations` permet de spécifier un intervalle de temps, en secondes. Par exemple, trois échecs de service en un mois ne justifient pas la restauration du service à la version précédente, tandis que trois échecs en cinq minutes peuvent indiquer une réelle défaillance de la nouvelle version de service.

Ensuite, republiez votre pattern de déploiement ou mettez à niveau la règle de déploiement avec les changements de la section **serviceVersion** dans Horizon Exchange.

Notez que vous pouvez aussi vérifier la compatibilité de la mise à jour des paramètres de la règle de déploiement ou du pattern en exécutant la commande `deploycheck` de l'interface de ligne de commande. Pour afficher plus de détails, exécutez : 

```bash
hzn deploycheck -h
```
{: codeblock}

Les agbots {{site.data.keyword.ieam}} détectent rapidement les modifications apportées au pattern ou à la règle de déploiement. Ils contactent alors chacun des agents dont le noeud de périphérie est soit enregistré afin d'exécuter le pattern de déploiement, soit compatible avec la règle de déploiement mise à jour. L'agbot et l'agent se coordonnent pour télécharger les nouveaux conteneurs, arrêter et retirer les anciens conteneurs, et démarrer les nouveaux.

Par conséquent, le noeud de périphérie qui est enregistré pour exécuter le pattern de déploiement mis à jour, ou qui est compatible avec la règle de déploiement, exécute rapidement la nouvelle version du service de périphérie ayant la priorité la plus élevée, quel que soit l'emplacement géographique du noeud de périphérie.  

## Affichage de la progression de la nouvelle version de service déployée
{: #viewing_rollback_progress}

Interrogez à plusieurs reprises les accords du dispositif jusqu'à ce que les zones `agreement_finalized_time` et `agreement_execution_start_time` soient renseignées : 

```bash
hzn agreement list
```
{: codeblock}

Remarquez que l'accord de la liste indique la version associée au service et que les valeurs date/heure sont affichées dans les variables (par exemple, "agreement_creation_time": "",)

De plus, la zone de la version affiche la nouvelle version de service opérationnelle avec la valeur de priorité la plus élevée :

```json
[   {     …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

Pour de plus amples détails, consultez les journaux d'événements du noeud actuel à l'aide de la commande d'interface de ligne de commande suivante :

```bash
hzn eventlog list
```
{: codeblock}

Pour finir, vous pouvez également utiliser la [console de gestion](../console/accessing_ui.md) pour modifier les paramètres des versions de déploiement à restaurer. Vous pouvez le faire pendant la création d'une règle de déploiement ou en affichant et en modifiant les détails existants d'une règle, y compris les paramètres de restauration. Notez que le terme “time frame” figurant dans la section de restauration de l'interface utilisateur est identique au terme “retry_durations” de l'interface de ligne de commande.
