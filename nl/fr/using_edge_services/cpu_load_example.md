---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Utilisation de l'unité centrale sur {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

Le pourcentage de charge de travail d'unité centrale hôte est un exemple de pattern de déploiement qui consomme des données de pourcentage de charge de travail d'unité centrale hôte et les rend disponibles via IBM Event Streams.

Ce service de périphérie interroge à plusieurs reprises la charge de travail d'unité centrale du dispositif de périphérie et envoie les résultats à [IBM Event Streams](https://www.ibm.com/cloud/event-streams). Ce service peut s'exécuter sur tout type de noeud de périphérie puisqu'il ne nécessite aucun capteur particulier.

Avant d'exécuter cette tâche, enregistrez et désenregistrez en exécutant la procédure de la section [Installation de l'agent Horizon sur votre dispositif de périphérie.](../installing/registration.md)

Pour acquérir de l'expérience avec un scénario encore plus réaliste, cet exemple cpu2evtstreams illustre d'autres aspects d'un service de périphérie type, notamment :

* Interrogation des données dynamiques du dispositif de périphérie
* Analyse des données du dispositif de périphérie (par exemple, `cpu2evtstreams` calcule la moyenne de la charge d'unité centrale)
* Envoi des données traitées à un service central de réception des données
* Automatisation de l'acquisition des données d'identification du flux d'événements pour authentifier le transfert de données en toute sécurité

## Avant de commencer
{: #deploy_instance}

Avant de déployer le service de périphérie cpu2evtstreams, une instance d'{{site.data.keyword.message_hub_notm}} doit être en cours d'exécution dans le cloud pour recevoir les données. Chaque membre de votre organisation peut partager une instance d'{{site.data.keyword.message_hub_notm}}. Si l'instance est déployée, récupérez les informations d'accès et définissez les variables d'environnement.

### Déploiement d'{{site.data.keyword.message_hub_notm}} dans {{site.data.keyword.cloud_notm}}
{: #deploy_in_cloud}

1. Accédez à {{site.data.keyword.cloud_notm}}.

2. Cliquez sur **Créer une ressource**.

3. Saisissez `Event Streams` dans la zone de recherche.

4. Sélectionnez l'affichage **Event Streams**.

5. Dans **Event Streams**, entrez un nom de service, sélectionnez une région, sélectionnez un plan de tarification et cliquez sur **Create** pour mettre à disposition l'instance.

6. Lorsque la mise à disposition est effective, cliquez sur l'instance.

7. Pour créer une rubrique, cliquez sur l'icône + et nommez l'instance `cpu2evtstreams`.

8. Vous pouvez soit créer des données d'identification dans votre terminal, soit les récupérer si elles ont déjà été créées. Pour créer des données d'identification, cliquez sur **Service credentials > New credential**. Créez un fichier nommé `event-streams.cfg` avec vos nouvelles données d'identification formatées de façon similaire au bloc de code suivant. Bien que ces données d'identification ne doivent être créées qu'une seule fois, sauvegardez ce fichier pour une utilisation future par vous-même ou d'autres membres de l'équipe qui pourraient avoir besoin de l'accès à {{site.data.keyword.event_streams}}.

   ```
   EVTSTREAMS_API_KEY="<the value of api_key>"    EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}
        
   Par exemple, dans le volet d'affichage des données d'identification :

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. Une fois `event-streams.cfg` créé, définissez ces variables d'environnement dans votre interpréteur de commandes :

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### Test d'{{site.data.keyword.message_hub_notm}} dans {{site.data.keyword.cloud_notm}}
{: #testing}

1. Installez `kafkacat` (https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/).

2. Sur un premier terminal, entrez la commande ci-dessous pour vous abonner à la rubrique `cpu2evtstreams` :

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. Sur un autre terminal, publiez le contenu test dans la rubrique `cpu2evtstreams` pour l'afficher sur la console d'origine. Par exemple :

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## Enregistrement de votre dispositif de périphérie
{: #reg_device}

Pour exécuter l'exemple de service cpu2evtstreams sur votre noeud de périphérie, enregistrez ce dernier auprès du pattern de déploiement `IBM/pattern-ibm.cpu2evtstreams`. Effectuez les étapes de la **première** section de [Horizon CPU To{{site.data.keyword.message_hub_notm}}](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md).

## Renseignements supplémentaires
{: #add_info}

L'exemple de code source de l'unité centrale est disponible dans le [référentiel des exemples {{site.data.keyword.horizon_open}}](https://github.com/open-horizon/examples) comme exemple de développement d'un service de périphérie {{site.data.keyword.edge_notm}}. La source inclut le code des trois services qui s'exécutent sur le noeud de périphérie dans cet exemple :

  * Le service cpu qui fournit les données de pourcentage de charge de travail de l'unité centrale en tant que service REST sur un réseau Docker privé local. Pour plus d'informations, voir [Horizon CPU Percent Service](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent).
  * Le service gps qui fournit des informations de localisation à partir du matériel GPS (le cas échéant) ou de l'emplacement estimé à partir de l'adresse IP des noeuds de périphérie. Les données d'emplacement sont fournies en tant que service REST sur un réseau Docker privé local. Pour plus d'informations, voir [Horizon GPS Service](https://github.com/open-horizon/examples/tree/master/edge/services/gps).
  * Le service cpu2evtstreams qui utilise les API REST fournies par les deux services ci-dessus. Ce service envoie les données combinées à un courtier Kafka {{site.data.keyword.message_hub_notm}} dans le cloud. Pour plus d'informations sur ce service, voir [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md).
  * Pour plus d'informations sur le {{site.data.keyword.message_hub_notm}}, voir [Event Streams - Présentation](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams).

## Etape suivante
{: #cpu_next}

Si vous voulez déployer votre propre logiciel vers un noeud de périphérie, vous devez créer vos propres services de périphérie, ainsi que le pattern ou la règle de déploiement associé(e). Pour plus d'informations, voir [Développement d'un service de périphérie pour les dispositifs](../OH/docs/developing/developing.md).
