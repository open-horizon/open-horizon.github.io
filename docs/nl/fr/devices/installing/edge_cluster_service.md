---

copyright:
  years: 2020
lastupdated: "2020-05-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Service de cluster de périphérie
{: #Edge_cluster_service}

Généralement, le développement d'un service prévu pour s'exécuter dans un cluster de périphérie est similaire à celui d'un service s'exécutant sur un dispositif de périphérie, si ce n'est la façon de déployer le service de périphérie. Pour déployer un service de périphérie conteneurisé sur un cluster de périphérie, les développeurs doivent d'abord concevoir un opérateur Kubernetes destiné à déployer le service de périphérie conteneurisé dans un cluster Kubernetes. Après avoir codé et testé l'opérateur, le développeur crée et publie l'opérateur en tant que service IBM Edge Application Manager (IEAM). Un administrateur IEAM peut ainsi déployer le service de l'opérateur comme il le ferait pour n'importe quel autre service, avec une règle ou des patterns.

Pour utiliser le service `ibm.operator` déjà publié sur votre IEAM Exchange à l'aide d'une règle de déploiement et exécuter le service conteneurisé `helloworld` sur votre cluster, voir [Horizon Operator Example Edge Service ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
