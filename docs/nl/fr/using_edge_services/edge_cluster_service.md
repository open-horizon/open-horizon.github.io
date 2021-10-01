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

Généralement, le développement d'un service prévu pour s'exécuter dans un cluster de périphérie est similaire à celui d'un service s'exécutant sur un dispositif de périphérie, si ce n'est la façon de déployer le service de périphérie. Pour déployer un service de périphérie conteneurisé sur un cluster de périphérie, les développeurs doivent d'abord concevoir un opérateur Kubernetes destiné à déployer le service de périphérie conteneurisé dans un cluster Kubernetes. Une fois l'opérateur testé, les développeurs créent et publient l'opérateur sous forme de service {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Le service d'opérateur peut être déployé sur ces clusters de périphérie avec une règle ou un pattern comme n'importe quel autre service {{site.data.keyword.edge_notm}}.

L'Exchange {{site.data.keyword.ieam}} comporte un service appelé `hello-operator` qui vous permet d'exposer un port sur votre cluster de périphérie auquel vous pouvez accéder en externe à l'aide de la commande `curl`. Pour déployer cet exemple de service sur votre cluster de périphérie, voir [Horizon Operator Example Edge Service](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
