---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Assistant vocal hors ligne
{: #offline-voice-assistant}

Chaque minute, l'assistant vocal hors ligne enregistre un clip audio de cinq secondes, le convertit en texte localement sur le dispositif de périphérie et demande à la machine hôte d'exécuter la commande et de lire la sortie. 

## Avant de commencer
{: #before_beginning}

Vérifiez que la configuration de votre système répond bien aux exigences suivantes :

* Vous devez procéder à l'enregistrement et à l'annulation de l'enregistrement en suivant les étapes de la section [Préparation d'un dispositif de périphérie](../installing/adding_devices.md).
* Une carte son USB et un microphone sont installés sur votre Raspberry Pi. 

## Enregistrement de votre dispositif de périphérie
{: #reg_edge_device}

Pour exécuter l'exemple de service `processtext` sur votre dispositif de périphérie, vous devez enregistrer votre noeud de périphérie auprès du pattern de déploiement `IBM/pattern-ibm.processtext`. 

Effectuez les étapes de la section Utilisation de l'exemple du service de périphérie Assistant vocal hors ligne avec le pattern de déploiement [Using the Offline Voice Assistant Example Edge Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) du fichier Readme.

## Renseignements supplémentaires
{: #additional_info}

Le code source de l'exemple `processtext` est également disponible dans le référentiel Horizon GitHub en guise d'exemple de développement {{site.data.keyword.edge_notm}}. La source inclut le code de tous les services qui s'exécutent sur les noeuds de périphérie dans cet exemple. 

Ces exemples de service [Open Horizon](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) incluent :

* Le service [voice2audio](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) qui enregistre le clip audio de cinq secondes et le publie sur le courtier MQTT.
* Le service [audio2text](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text), qui utilise le clip audio et le convertit en texte hors ligne à l'aide de pocket sphinx.
* Le service [processtext](https://github.com/open-horizon/examples/tree/master/edge/services/processtext), qui utilise le texte et tente d'exécuter les commandes enregistrées.
* Le service [text2speech](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech), qui lit la sortie de la commande en utilisant un haut-parleur.
* Le courtier [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker), qui gère toute la communication inter-conteneur.

## Etape suivante
{: #what_next}

Pour obtenir des instructions relatives à la génération et à la publication de votre propre version de Watson Speech to Text, suivez les étapes du répertoire `processtext` dans le référentiel des [exemples Open Horizon](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service). 
