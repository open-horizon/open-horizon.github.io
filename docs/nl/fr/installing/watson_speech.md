---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Watson Speech to Text
{: #watson-speech}

Ce service est à l'écoute du mot Watson. Lorsqu'il l'identifie, il capture un clip audio et l'envoie à une instance du service Speech to Text.  Les mots vides sont retirés (facultatif) et le texte transcrit est envoyé à {{site.data.keyword.event_streams}}.

## Avant de commencer

Vérifiez que la configuration de votre système répond bien aux exigences suivantes :

* Vous devez procéder à l'enregistrement et à l'annulation de l'enregistrement en suivant les étapes de la section [Préparation d'un dispositif de périphérie](adding_devices.md).
* Une carte son USB et un microphone sont installés sur votre Raspberry Pi. 

Ce service nécessite une instance d'{{site.data.keyword.event_streams}} et d'IBM Speech to Text pour s'exécuter correctement. Pour en savoir plus sur les modalités de déploiement d'une instance de flux d'événements, voir l'[exemple de pourcentage de charge de travail d'unité centrale hôte (cpu2evtstreams)](../using_edge_services/cpu_load_example.md).  

Assurez-vous que les variables d'environnement {{site.data.keyword.event_streams}} requises sont définies :

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

La rubrique de flux d'événements utilisée par défaut dans cet exemple est `myeventstreams`, mais vous pouvez utiliser n'importe quelle rubrique en définissant la variable d'environnement ci-dessous :

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## Déploiement d'une instance d'IBM Speech to Text
{: #deploy_watson}

Si une instance est déjà déployée, récupérez les informations d'accès et définissez les variables d'environnement, ou suivez les étapes ci-dessous :

1. Accédez à IBM Cloud.
2. Cliquez sur **Créer une ressource**.
3. Saisissez `Speech to Text` dans la zone de recherche.
4. Sélectionnez la vignette `Speech to Text`.
5. Sélectionnez une région, sélectionnez un plan de tarification, entrez un nom de service et cliquez sur **Créer** pour mettre à disposition l'instance.
6. Une fois l'opération terminée, cliquez sur l'instance et notez la clé d'API et l'adresse URL, puis exportez-les comme les variables d'environnement ci-dessous :

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>     export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Consultez la section Prise en main pour en savoir plus sur la façon de tester le service Speech to Text.

## Enregistrement de votre dispositif de périphérie
{: #watson_reg}

Pour exécuter l'exemple de service watsons2text sur votre noeud de périphérie, enregistrez votre noeud de périphérie auprès du pattern de déploiement `IBM/pattern-ibm.watsons2text-arm`. Exécutez les étapes de la section [Using Watson Speech to Text to IBM Event Streams Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) du fichier readme.

## Renseignements supplémentaires

Le code source de l'exemple `processtect` est également disponible dans le référentiel Horizon GitHub en guise d'exemple de développement {{site.data.keyword.edge_notm}}. La source inclut le code des quatre services qui s'exécutent sur les noeuds de périphérie dans cet exemple. 

Les services sont les suivants :

* Le service [hotworddetect](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) écoute et détecte le terme Watson, puis enregistre un clip audio et le publie sur le courtier mqtt.
* Le service [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) reçoit un clip audio et l'envoie au service IBM Speech to Text, puis publie le texte déchiffré sur le courtier mqtt.
* Le service [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) s'exécute lorsqu'un serveur WSGI utilise un objet JSON, par exemple {"text": "how are you today"}, puis retire les mots vides courants et renvoie {"result": "how you today"}.
* Le service [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) publie des données vers {{site.data.keyword.event_streams}} lorsqu'il reçoit un élément sur la rubrique mqtt à laquelle il est abonné.
* Le service [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) est responsable de toute la communication inter-conteneur.

## Etape suivante

* Pour en savoir plus sur la génération et la publication de votre propre version du service de périphérie Assistant vocal hors ligne, voir [Offline Voice Assistant Edge Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service). Suivez les étapes du répertoire `watson_speech2text` dans le référentiel des exemples Open Horizon.

* Voir la page [Open Horizon examples repository](https://github.com/open-horizon/examples).
