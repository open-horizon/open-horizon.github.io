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

# Développement d'un service de périphérie pour les clusters
{: #developing_clusters}

Le cluster de périphérie d'{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur de gestion vers des instances distantes d'OpenShift® Container Platform ou d'autres clusters basés sur Kubernetes. Les clusters de périphérie sont des noeuds de périphérie {{site.data.keyword.ieam}} qui sont des clusters Kubernetes. Un cluster de périphérie autorise les cas d'utilisation à la périphérie qui nécessitent une colocalisation du calcul avec les opérations métier, ou qui nécessitent davantage d'évolutivité, de disponibilité et de capacité de calcul que celles offertes par un dispositif de périphérie. En outre, il n'est pas rare que les clusters de périphérie fournissent des services d'applications pour prendre en charge les services qui s'exécutent sur des dispositifs de périphérie du fait de leur proximité avec les dispositifs de périphérie, ce qui se traduit par une application de périphérie multiniveau. {{site.data.keyword.ieam}} déploie des services de périphérie sur un cluster de périphérie via un opérateur Kubernetes, ce qui permet d'utiliser les mêmes mécanismes de déploiement autonomes que ceux des dispositifs de périphérie. Toute la puissance de la plateforme de gestion de conteneurs Kubernetes est mise à la disposition des services de périphérie qui sont déployés par {{site.data.keyword.ieam}}.

<img src="../OH/docs/images/edge/03b_Developing_edge_service_for_cluster.svg" style="margin: 3%" alt="Developing an edge service for clusters">

* [Développement d'un opérateur Kubernetes](service_operators.md)
* [Création de votre propre Hello world pour clusters](creating_hello_world.md)
