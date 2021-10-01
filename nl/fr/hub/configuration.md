---

copyright:
  years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Configuration d'{{site.data.keyword.ieam}}

## Configuration de ressource personnalisée EamHub
{: #cr}

La configuration principale d'{{site.data.keyword.ieam}} est effectuée via la ressource personnalisée EamHub, en particulier la zone **spec** de cette ressource personnalisée.

Ce document part des principes suivants :
* L'espace de nom pour lequel vous exécutez ces commandes se trouve dans   l'emplacement où l'opérateur du concentrateur de gestion {{site.data.keyword.ieam}} est déployé.
* Le nom de la ressource personnalisée EamHub est par défaut **ibm-edge**. S'il est différent, modifiez les commandes pour remplacer **ibm-edge**.
* Le fichier binaire **jq** est installé, ce qui garantit l'affichage de la sortie dans un format lisible.


La **spécification** par défaut définie est minimale, ne contenant que l'acceptation de la licence, que vous pouvez afficher avec :
```
$ oc get eamhub ibm-edge -o yaml ... spec:   license:     accept: true ...
```

### Boucle de contrôle de l'opérateur
{: #loop}

L'opérateur du concentrateur de gestion {{site.data.keyword.ieam}} s'exécute dans une boucle idempotent continue pour synchroniser l'état actuel des ressources avec l'état attendu des ressources.

En raison de cette boucle continue, vous devez comprendre deux éléments lorsque vous configurez vos ressources gérées par l'opérateur :
* Toute modification de la ressource personnalisée est lue de manière asynchrone par la boucle de contrôle. Une fois la modification effectuée, sa mise en oeuvre par l'intermédiaire de l'opérateur peut prendre quelques minutes.
* Toute modification manuelle apportée à une ressource contrôlée par l'opérateur peut être annulée par l'opérateur qui applique un état spécifique. 

Pour voir cette boucle, consultez les journaux de pod de l'opérateur :
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

Lorsqu'une boucle se termine, elle génère un récapitulatif **PLAY RECAP**. Pour afficher le récapitulatif le plus récent, exécutez :
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

Les éléments suivants indiquent une boucle qui s'est terminée sans qu'aucune opération soit effectuée (dans son état actuel, **PLAY RECAP** affiche toujours **changed= 1**) :
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1 localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

Examinez ces 3 zones lorsque vous modifiez la configuration :
* **changed** : lorsque la valeur est supérieure à **1**, indique que l'opérateur a effectué une tâche qui a modifié l'état d'une ou de plusieurs ressources (soit sur votre demande parce que vous avez modifié la ressource personnalisée, soit parce que l'opérateur a annulé une modification manuelle).
* **rescued** : une tâche a échoué, mais il s'agissait d'un échec connu possible, et la tâche est relancée dans la boucle suivante.
* **failed** : Lors de l'installation initiale, des échecs sont attendus. Si vous constatez à plusieurs reprises le même échec et que le message n'est pas clair (ou masqué), cela signale probablement un problème.

### Options de configuration courantes pour EamHub

Plusieurs modifications de configuration peuvent être apportées, mais certaines modifications sont plus susceptibles d'être demandées que d'autres. Cette section décrit certains des paramètres les plus courants.

| Valeur de configuration | Par défaut | Description |
| :---: | :---: | :---: |
| Valeurs globales | -- | -- |
| pause_control_loop | false | Suspend la boucle de contrôle mentionnée ci-dessus pour permet des modifications manuelles temporaires pour le débogage. Ne doit pas être utilisé pour l'état stabilisé. |
| ieam_maintenance_mode | false | Définit tous les nombres de répliques de pod sans stockage permanent sur 0. Utilisé pour la restauration de la sauvegarde. |
| ieam_local_databases | true | Active ou désactive les bases de données locales. La commutation entre les états n'est pas prise en charge. Voir [Configuration de base de données distante](./configuration.md#remote). |
| ieam_database_HA | true | Active ou désactive le mode HA (haute disponibilité) pour les bases de données locales. Définit le nombre de répliques de tous les pods de base de données sur **3** lorsque la valeur est **true**, et sur **1** lorsque la valeur est **false**. |
| hide_sensitive_logs | true | Masque les journaux de l'opérateur qui traitent de la définition des **secrets Kubernetes**. Si la valeur est **false**, des échecs de tâche peuvent entraîner la journalisation par l'opérateur de valeurs d'authentification codées. |
| storage_class_name | "" | Utilise la classe de stockage par défaut si cette valeur n'est pas définie. |
| Ieam_enable_tls | false | Active ou désactive le protocole TLS interne pour le trafic entre les composants {{site.data.keyword.ieam}} . **Attention : **Si vous remplacez la configuration par défaut de l'échange, du CSS ou de la chambre forte, la configuration TLS doit être modifiée manuellement dans le remplacement de la configuration. |
| Ieam_local_secrets_manager | true | Active ou désactive le composant local du gestionnaire de secrets (coffre). |


### Options de configuration de mise à l'échelle du composant EamHub

| Valeur d'échelle du composant | Nombre de répliques  par défaut | Description |
| :---: | :---: | :---: |
| Change_répliques | 3 | Nombre par défaut de répliques pour l'échange. Si vous remplacez la configuration d'échange par défaut (exchange_config), **maxPoolSize **doit être ajusté manuellement en utilisant cette formule `((exchangedb_max_connections - 8) / exchange_replicas)` |
| css_replicas | 3 | Nombre par défaut de répliques pour le CSS. |
| Ui_replicas | 3 | Nombre par défaut de répliques pour l'interface utilisateur. |
| Agbot_replicas | 2 | Nombre par défaut de répliques pour l'agbot. Si vous remplacez la configuration d'agbot par défaut (agbot_config), **MaxOpenConnections** doit être ajusté manuellement à l'aide de cette formule `((agbotdb_max_connections-8) / agbot_replicas)` |


### Options de configuration des ressources de composant EamHub

**Remarque**: Comme les opérateurs Ansible exigent qu'un dictionnaire imbriqué soit ajouté dans son ensemble, vous devez ajouter les valeurs de configuration imbriquées dans leur intégralité.. Voir [Configuration de la mise à l'échelle](./configuration.md#scale) pour un exemple.

<table>
<tr>
<td> Valeur de ressource de composant </td> <td> Par défaut </td> <td> Description </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources : demandes : mémoire : 512Mi cpu : 10m limites : mémoire : 2Gi cpu : 2
```

</td>
<td>
Les demandes par défaut et les limites de l'échange. 
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources : demandes : mémoire : 64Mi cpu : 10m limites : mémoire : 2Gi cpu : 2
```

</td>
<td>
Les demandes et les limites par défaut pour l'agbot. 
</td>
</tr>
<tr>
<td> Ressources css_ressources </td> 
<td>

```
  css_resources : requêtes : mémoire : 64Mi cpu : 10m limites : mémoire : 2Gi cpu : 2
```

</td>
<td>
Les demandes et les limites par défaut pour le CSS. 
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources : demandes : mémoire : 1024Mi cpu : 10m limites : mémoire : 2Gi cpu : 2
```

</td>
<td>
Les demandes et les limites par défaut pour SDO. 
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  Ui_resources: requêtes: mémoire: 64Mi cpu: 10m limites: mémoire: 2Gi cpu: 2
```

</td>
<td>
Les demandes et les limites par défaut de l'interface utilisateur. 
</td>
</tr>
<tr>
<td> vault_resources </td> 
<td>

```
  vault_resources : demandes : mémoire : 1024Mi cpu : 10m limites : mémoire : 2Gi cpu : 2
```

</td>
<td>
Les demandes et les limites par défaut pour le gestionnaire de secrets. 
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources : limites : cpu : 2 mémoire : 2Gi demandes : cpu : 100m mémoire : 256Mi
```

</td>
<td>
Les demandes et les limites par défaut de la base de données CSS mongo. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_sentinel </td> 
<td>

```
  postgres_exchangedb_sentinel : ressources : demandes : cpu : "100m" mémoire : "256Mi" limites : cpu : 1 mémoire : 1Gi
```

</td>
<td>
Les demandes et les limites par défaut pour la sentinelle d'échange postgres. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_proxy </td> 
<td>

```
  postgres_exchangedb_proxy : ressources : demandes : cpu : "100m" mémoire : "256Mi" limites : cpu : 1 mémoire : 1Gi
```

</td>
<td>
Les demandes et les limites par défaut pour le proxy d'échange postgres. 
</td>
</tr>
<tr>
<td> Postgres_changedb_keeper </td> 
<td>

```
  postgres_exchangedb_keeper : ressources : demandes : cpu : "100m" mémoire : "256Mi" limites : cpu : 2 mémoire : 2Gi
```

</td>
<td>
Les requêtes et les limites par défaut pour le détenteur d'échange postgres. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_sentinel </td> 
<td>

```
  Postgres_agbotdb_sentinel : ressources : demandes : cpu : "100m" mémoire : "256Mi" limites : cpu : 1 mémoire : 1Gi
```

</td>
<td>
Les demandes et les limites par défaut pour la sentinelle de l'agbot postgres. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_proxy </td> 
<td>

```
  Postgres_agbotdb_proxy: ressources: requêtes: cpu: "100m" mémoire: "256Mi" limites: cpu: 1 mémoire: 1Gi
```

</td>
<td>
Les demandes et les limites par défaut pour le proxy d'agbot postgres. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_keeper </td> 
<td>

```
  postgres_agbotdb_keeper : ressources : demandes : cpu : "100m" mémoire : "256Mi" limites : cpu : 2 mémoire : 2Gi
```

</td>
<td>
Les demandes et les limites par défaut pour le gardien de l'agbot postgres. 
</td>
</tr>
</table>

### Options de configuration de taille de base de données locale EamHub

| module de configuration de composant | Taille de volume persistant par défaut | Description |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20 Gi | Taille de la base de données d'échange postgres. |
| postgres_agbotdb_storage_size | 20 Gi | Taille de la base de données postgres agbot. |
| mongo_cssdb_storage_size | 20 Gi | Taille de la base de données CSS mongo. |

## Configuration de l'API de traduction Exchange

Vous pouvez configurez l'API Exchange {{site.data.keyword.ieam}} pour renvoyer les réponses dans une langue spécifique. Pour ce faire, définissez une variable d'environnement avec une **LANGUE** prise en charge de votre choix (la valeur par défaut est **en**) :

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**Remarque :** pour obtenir la liste des codes de langue pris en charge, consultez le premier tableau de la page [Langues prises en charge](../getting_started/languages.md).

## Configuration de base de données distante
{: #remote}

**Remarque** : la commutation entre les bases de données distantes et locales n'est pas prise en charge.

Pour exécuter une installation avec des bases de données distantes, créez la ressource personnalisée EamHub lors de l'installation en indiquant la valeur supplémentaire dans la zone **spec** :
```
spec:   ieam_local_databases: false   license:     accept: true
```
{: codeblock}

Remplissez le modèle suivant pour créer un secret d'authentification. Veillez à lire chaque commentaire pour vous assurer qu'il est rempli correctement et sauvegardez-le dans **edge-auth-overrides.yaml** :
```
apiVersion: v1 kind: Secret metadata:   # REMARQUE : Le nom doit être ajouté en préfixe par le nom donné à votre ressource personnalisée, qui est par défaut 'ibm-edge' #name: <CR_NAME>-auth-overrides   name: ibm-edge-auth-overrides type: Opaque stringData:   # Paramètres de la connexion postgresql - Annuler la mise en commentaires et remplacer par vos paramètres   agbot-db-host: "<Nom d'hôte unique de la base de données distante>"   agbot-db-port: "<Port unique sur lequel s'exécute la base de données>"   agbot-db-name: "<Nom de la base de données à utiliser dans l'instance postgresql>"   agbot-db-user: "<Nom d'utilisateur de la connexion>"      agbot-db-pass: "<Mot de passe de la connexion>"   agbot-db-ssl: "<disable|require|verify-full>"   # Utilisez une mise en retrait adaptée (quatre espaces)      agbot-db-cert: |- -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings   exchange-db-host: "<Nom d'hôte unique de la base de données distante>"   exchange-db-port: "<Port unique sur lequel s'exécute la base de données>"   exchange-db-name: "<Nom de la base de données à utiliser dans l'instance postgresql>"   exchange-db-user: "<Nom d'utilisateur de la connexion>"   exchange-db-pass: "<Mot de passe de la connexion>"   exchange-db-ssl: "<disable|require|verify-full>"   # Utilisez une mise en retrait adaptée (quatre espaces)   exchange-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  o# paramètres de connexion css mongodb   css-db-host: "<Liste séparée par des virgules y compris les ports : hostname.domain:port,hostname2.domain:port2 >"   css-db-name: "<Nom de la base de données à utiliser avec l'instance mongodb>"   css-db-user: "<Nom d'utilisateur pour la connexion>"       css-db-pass: "<Mot de passe pour la connexion>"   css-db-auth: "<Nom de la base de données utilisée pour stocker le nom de la base de données utilisé pour stocker les données d'identification>" css-db-ssl: "<true|false>"   # Utilisez une mise en retrait adaptée (quatre espaces)   css-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

Créez le secret :
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

Observez les journaux de l'opérateur comme indiqué dans la section [Boucle de contrôle de l'opérateur](./configuration.md#remote).


## Mise à l'échelle de la configuration
{: #scale}

La configuration des ressources personnalisées de l'EamHub expose les paramètres de configuration qui peuvent être nécessaires pour augmenter les ressources des pods sur le {{site.data.keyword.ieam}}centre de gestion afin de prendre en charge un nombre élevé de nœuds périphériques.
Les clients doivent surveiller la consommation de ressources des {{site.data.keyword.ieam}}pods, en particulier des bots d'échange et d'accord (agbots) et ajouter des ressources si nécessaire. Voir [Accès au {{site.data.keyword.ieam}} tableau de bord Grafana](../admin/monitoring.md) La plateforme OpenShift reconnaît ces mises à jour et les applique automatiquement à {{site.data.keyword.ieam}} PODS fonctionnant sous {{site.data.keyword.ocp}}.

Restrictions

Avec les allocations de ressources par défaut et la désactivation du protocole TLS interne entre les {{site.data.keyword.ieam}}pods, IBM a testé jusqu'à 40 000 nœuds de périphérie enregistrés obtenant 40 000 instances de service déployées avec des mises à jour de la politique de déploiement qui ont un impact sur 25 % (ou 10 000) des services déployés.

Pour prendre en charge 40 000 nœuds de bordure enregistrés, lorsque le protocole TLS interne entre les{{site.data.keyword.ieam}} pods est activé, les pods Exchange ont besoin de ressources CPU supplémentaires. 
Apportez la modification suivante dans la configuration de la ressource personnalisée EamHub

Ajoutez la section suivante sous **spec** :

```
spec:   exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 5
```
{: codeblock}

Pour prendre en charge plus de 90 000 déploiements de services, apportez la modification suivante dans la configuration de la ressource personnalisée EamHub.

Ajoutez la section suivante sous **spec** :

```
spec : agbot_resources : demandes : mémoire : 1Gi cpu : 10m limites : mémoire : 4Gi cpu : 2
```
{: codeblock}

