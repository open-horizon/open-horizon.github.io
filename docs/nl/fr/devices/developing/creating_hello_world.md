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

* Ecrire un opérateur
* Utiliser un opérateur pour déployer un service de périphérie sur un cluster (dans notre cas, `ibm.helloworld`)
* Transmettre les variables d'environnement Horizon (et d'autres requises) aux pods de votre service déployé

Voir [Creating your own Hello World cluster service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator/CreateService.md).

Pour exécuter le service `ibm.operator` publié, voir [Operator Example Edge Service with Deployment Policy ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
