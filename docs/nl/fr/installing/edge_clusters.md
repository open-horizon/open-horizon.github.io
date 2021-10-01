---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Clusters de périphérie
{: #edge_clusters}

La fonction de cluster de périphérie d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) vous aide à gérer et à déployer des charges de travail d'un cluster concentrateur de gestion vers des instances distantes d'OpenShift® Container Platform ou d'autres clusters basés sur Kubernetes. Les clusters de périphérie sont des noeuds de périphérie {{site.data.keyword.ieam}} qui sont des clusters Kubernetes. Un cluster de périphérie active des cas d'utilisation à la périphérie exigeant la colocalisation du traitement avec les opérations métier ou nécessitant davantage d'évolutivité, de disponibilité et de capacité de traitement que ce qui peut être pris en charge par un dispositif de périphérie. En outre, il n'est pas rare que les clusters de périphérie fournissent des services d'applications pour prendre en charge les services qui s'exécutent sur un dispositif de périphérie du fait de leur proximité avec les dispositifs de périphérie. {{site.data.keyword.ieam}} déploie des services de périphérie via un opérateur Kubernetes, ce qui permet d'utiliser les mêmes mécanismes de déploiement autonomes que ceux des dispositifs de périphérie. Toute la puissance de la plateforme de gestion de conteneurs Kubernetes est mise à la disposition des services de périphérie qui sont déployés par {{site.data.keyword.ieam}}.

<img src="../OH/docs/images/edge/05b_Installing_edge_agent_on_cluster.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}, agbots and agents">

Les sections ci-après expliquent comment installer un cluster de périphérie et comment installer l'agent {{site.data.keyword.ieam}} dessus.

- [Préparation d'un cluster de périphérie](preparing_edge_cluster.md)
- [Installation de l'agent](edge_cluster_agent.md)
{: childlinks}
