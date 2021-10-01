---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Création de votre propre Hello world pour clusters
{: #creating_hello_world}

Pour déployer un service de périphérie conteneurisé sur un cluster de périphérie, la première étape consiste à concevoir un opérateur Kubernetes destiné à déployer ce service dans un cluster Kubernetes.

Utilisez cet exemple pour savoir comment :

* Créez un opérateur ansible à l'aide de `operator-sdk`
* Utiliser l'opérateur pour déployer un service sur un cluster de périphérie
* Exposer un port sur votre cluster de périphérique auquel vous pourrez accéder en externe à l'aide de la commande `curl`

Voir [Creating Your Own Operator Edge Service](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service).

Pour exécuter le service `hello-operator` publié, voir [Using the Operator Example Edge Service with Deployment Policy](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
