---

copyright:
  years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Présentation d'un service de périphérie pour les clusters
{: #cluster_deployment}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) offre des fonctionnalités d'informatique Edge pour vous aider à gérer et à déployer des charges de travail d'un cluster concentrateur vers des instances distantes d'OpenShift® Container Platform 4.2 ou d'autres clusters Kubernetes. Les clusters de périphérie sont des noeuds de périphérie d'{{site.data.keyword.ieam}} déployés en tant que clusters Kubernetes. Un cluster de périphérie autorise les cas d'utilisation à la périphérie qui nécessitent une colocalisation du calcul avec les opérations métier, ou qui nécessitent davantage d'évolutivité et de capacité de calcul que celles offertes par un dispositif de périphérie. En outre, il n'est pas rare que les clusters de périphérie fournissent des services d'applications pour prendre en charge les services qui s'exécutent sur un dispositif de périphérie du fait de leur proximité avec les dispositifs de périphérie. {{site.data.keyword.ieam}} déploie des services de périphérie via un opérateur Kubernetes, ce qui permet d'utiliser les mêmes mécanismes de déploiement autonomes que ceux des dispositifs de périphérie. Toute la puissance de la plateforme de gestion de conteneur Kubernetes est mise à la disposition des services de périphérie déployés par {{site.data.keyword.ieam}}.

IBM Cloud Pak for Multicloud Management peut également être utilisé pour offrir un plus haut niveau de gestion Kubernetes des clusters de périphérie, même pour les services de périphérie déployés par {{site.data.keyword.ieam}}.

Ajoutez un graphique illustrant les étapes détaillées d'installation et de configuration d'un noeud de périphérie (avec les dispositifs et les clusters).
