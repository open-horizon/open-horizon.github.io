---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Préparation de l'installation d'{{site.data.keyword.edge_servers_notm}}
{: #edge_planning}

Avant d'installer {{site.data.keyword.icp_server}}, activez le {{site.data.keyword.mgmt_hub}} et configurez {{site.data.keyword.edge_servers_notm}}, puis vérifiez que votre système est conforme aux exigences ci-après. Ces exigences déterminent les composants et les paramètres minimum requis pour vos serveurs de périphérie planifiés.
{:shortdesc}

Elles identifient également les paramètres de configuration minimum pour le cluster {{site.data.keyword.mgmt_hub}} que vous souhaitez utiliser pour gérer vos serveurs de périphérie.

Les informations de cette section vous aideront à planifier les besoins en ressources de votre topologie d'informatique Edge ainsi que l'ensemble de votre configuration d'{{site.data.keyword.icp_server}} et du {{site.data.keyword.mgmt_hub}}.

   * [Configuration matérielle requise](#prereq_hard)
   * [Fournisseurs IaaS pris en charge](#prereq_iaas)
   * [Environnements pris en charge](#prereq_env)
   * [Ports requis](#prereq_ports)
   * [Remarques relatives au dimensionnement des clusters](#cluster)

## Configuration matérielle requise
{: #prereq_hard}

Lorsque vous définissez la taille du noeud de gestion de votre topologie d'informatique Edge, appuyez-vous sur les instructions relatives au dimensionnement d'{{site.data.keyword.icp_server}} pour un déploiement à noeud unique ou multiple pour définir la taille de votre cluster. Pour plus d'informations, voir [Dimensionnement de votre cluster {{site.data.keyword.icp_server}} ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Les exigences de serveur de périphérie ci-dessous s'appliquent uniquement aux instances {{site.data.keyword.icp_server}} qui sont déployées sur des centres d'opérations distants via le {{site.data.keyword.edge_profile}}.

| Exigences | Noeuds (amorçage, maître, gestion) | Noeuds worker |
|-----------------|-----------------------------|--------------|
| Nombre d'hôtes | 1 | 1 |
| Coeurs | 4 ou plus | 4 ou plus |
| Unité centrale | >= 2,4 GHz | >= 2,4 GHz |
| Mémoire RAM | 8 Go ou plus | 8 Go ou plus |
| Espace disque libre pour l'installation | 150 Go ou plus | |
{: caption="Tableau 1. Configuration matérielle minimale pour le clusters de serveurs." caption-side="top"}

Remarque : Un espace de 150 Go de stockage permet de conserver jusqu'à trois jours de données d'événement et journaux en cas de déconnexion du réseau au centre de données principal.

## Fournisseurs IaaS pris en charge
{: #prereq_iaas}

Le tableau ci-dessous vous permet d'identifier l'infrastructure IaaS (Infrastructure as a Service) qui est compatible avec vos services de périphérie.

| IaaS | Versions |
|------|---------|
|Nutanix NX-3000 Series à utiliser aux emplacements de serveur de périphérie | NX-3155G-G6 |
|Systèmes IBM Hyperconverged basés sur Nutanix à utiliser dans des serveurs de périphérie | CS821 et CS822|
{: caption="Tableau 2. Infrastructure IaaS prise en charge pour {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Pour plus d'informations, consultez le PDF [IBM Hyperconverged Systems powered by Nutanix ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Environnements pris en charge
{: #prereq_env}

Les tableaux ci-dessous vous permettent d'identifier les systèmes configurés Nutanix supplémentaires que vous pouvez utiliser avec vos serveurs de périphérie.

| Type de site LOE | Type de noeud | Taille de cluster | Coeurs par noeud (total) | Processeurs logiques par noeud (total)	| Mémoire (Go) par noeud (total) | Taille de disque du cache par groupe de disques (Go) |	Quantité de disque du cache par noeud	| Taille de disque du cache par noeud (Go)	| Taille de pool de cluster du stockage total (flash) (To) |
|---|---|---|---|---|---|---|---|---|---|
| Petit	| NX-3155G-G6	| 3 noeuds	| 24 (72)	| 48 (144)	| 256 (768)	| Sans objet	| Sans objet	| Sans objet	| 8 To |
| Moyen | NX-3155G-G6 | 3 noeuds | 24 (72)	| 48 (144)	| 512 (1,536)	| Sans objet	| Sans objet	| Sans objet	| 45 To |
| Grand	| NX-3155G-G6	| 4 noeuds	| 24 (96)	| 48 (192)	| 512 (2,048)	| Sans objet	| Sans objet	| Sans objet	| 60 To |
{: caption="Tableau 3. Configurations prises en charge par Nutanix NX-3000 Series" caption-side="top"}

| Type de site LOE	| Type de noeud	| Taille de cluster |	Coeurs par noeud (total) | Processeurs logiques par noeud (total)	| Mémoire (Go) par noeud (total)	| Taille de disque du cache par groupe de disques (Go) | Quantité de disque du cache par noeud	| Taille de disque du cache par noeud (Go)	| Taille de pool de cluster du stockage total (flash) (To) |
|---|---|---|---|---|---|---|---|---|---|
| Petit	| CS821 (2 socket, 1U) | 3 noeuds | 20 (60)	| 80 (240) | 256 (768) | Sans objet	| Sans objet	| Sans objet	| 8 To |
| Moyen | CS822 (2 socket, 2U) | 3 noeuds	| 22 (66)	| 88 (264) | 512 (1,536) | Sans objet | Sans objet | Sans objet | 45 To |
| Grand	| CS822 (2 socket, 2U) | 4 noeuds | 22 (88) | 88 (352) | 512 (2,048) | Sans objet | Sans objet | Sans objet | 60 To |
{: caption="Tableau 4. Systèmes IBM Hyperconverged basés sur Nutanix" caption-side="top"}

Pour toute information supplémentaire, voir [IBM Hyperconverged Systems that are powered by Nutanix ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Ports requis
{: #prereq_ports}

Si vous envisagez d'effectuer le déploiement sur un serveur de périphérie distant avec une configuration de cluster standard, les conditions de port requises pour les noeuds sont les mêmes que celles utilisées pour le déploiement d'{{site.data.keyword.icp_server}}. Pour plus d'informations sur ces exigences, voir [Ports requis ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dan un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html). Pour connaître les ports requis pour le cluster concentrateur, lisez la section _Ports requis pour {{site.data.keyword.mcm_core_notm}}_.

Si vous envisagez de configurer vos serveurs de périphérie à l'aide du {{site.data.keyword.edge_profile}}, activez les ports ci-dessous :

| Port | Protocole | Exigences |
|------|----------|-------------|
| Non applicable | IPv4 | Calico avec IP-in-IP (calico_ipip_mode: Always) |
| 179 | TCP	| Toujours pour Calico (network_type : calico) |
| 500 | TCP et UDP	| IPSec (ipsec.enabled: true, calico_ipip_mode: Always) |
| 2380 | TCP | Toujours si etcd est activé |
| 4001 | TCP | Toujours si etcd est activé |
| 4500 | UDP | IPSec (ipsec.enabled: true) |
| 9091 | TCP | Calico (network_type:calico) |
| 9099 | TCP | Calico (network_type:calico) |
| 10248:10252 | TCP	| Toujours pour Kubernetes |
| 30000:32767 | TCP et UDP | Toujours pour Kubernetes |
{: caption="Tableau 5. Ports requis pour {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Remarque : Les ports 30000:32767 disposent d'un accès externe. Ces ports ne doivent être ouverts que si vous définissez le type de service Kubernetes à NodePort.

## Remarques relatives au dimensionnement des clusters
{: #cluster}

Pour {{site.data.keyword.edge_servers_notm}}, le cluster concentrateur est généralement un environnement hébergé {{site.data.keyword.icp_server}} standard. Vous pouvez utiliser cet environnement pour héberger d'autres charges de travail accessibles depuis un emplacement central. L'environnement du cluster concentrateur doit être dimensionné de manière à disposer de suffisamment de ressources pour héberger le cluster {{site.data.keyword.mcm_core_notm}} et les charges de travail supplémentaires que vous prévoyez d'héberger dessus. Pour en savoir plus sur le dimensionnement d'un environnement hébergé {{site.data.keyword.icp_server}} standard, voir [Dimensionnement de votre cluster {{site.data.keyword.icp_server}} ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Si nécessaire, vous pouvez exploiter un serveur de périphérie distant au sein d'un environnement à ressources limitées. Si vous avez besoin de faire fonctionner un serveur de périphérie dans un environnement à ressources limitées, pensez à utiliser le {{site.data.keyword.edge_profile}}. Ce profil ne configure que le minimum de composants requis pour un environnement de serveur de périphérie. Si vous avez recours à ce profil, vous devez quand même allouer suffisamment de ressources pour l'ensemble des composants requis pour une architecture {{site.data.keyword.edge_servers_notm}} et pour les autres charges de travail des applications qui sont hébergées sur vos environnements de serveurs de périphérie. Pour plus d'informations sur l'architecture {{site.data.keyword.edge_servers_notm}}, voir [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch).

Bien que les configurations du {{site.data.keyword.edge_profile}} permettent de préserver des ressources de mémoire et de stockage, elles peuvent aussi se traduire par un faible niveau de résilience. Un serveur de périphérie basé sur ce profil peut fonctionner sans connexion au centre de données central où est installé votre cluster concentrateur. Cette opération hors ligne peut prendre jusqu'à 3 jours. Si le serveur de périphérie tombe en panne, il cesse de fournir une prise en charge opérationnelle pour le centre d'opérations distant.

En outre, les configurations du {{site.data.keyword.edge_profile}} se limitent à prendre en charge les technologies et processus ci-dessous :
  * Plateformes {{site.data.keyword.linux_notm}} 64 bits
  * Topologie de déploiement sans haute disponibilité
  * Ajout et retrait de noeuds worker en tant qu'opérations au 2e jour
  * Accès et contrôle du cluster par interface CLI
  * Réseaux Calico

Si vous avez besoin de davantage de résilience ou si les contraintes précédentes sont trop restrictives, vous pouvez choisir d'utiliser l'un des profils de configuration de déploiement standard pour {{site.data.keyword.icp_server}} qui fournit un meilleur support de reprise en ligne.

### Exemples de déploiement

* Environnement de serveur de périphérie basé sur le {{site.data.keyword.edge_profile}} (faible résilience)

| Type de noeud | Nombre de noeuds | Unité centrale | Mémoire (Go) | Disque (Go) |
|------------|:-----------:|:---:|:-----------:|:---:|
| Amorçage       | 1           | 1   | 2           | 8   |
| Maître     | 1           | 2   | 4           | 16  |
| Gestion | 1           | 1   | 2           | 8   |
| Worker     | 1           | 4   | 8           | 32  |
{: caption="Tableau 6. Valeurs de profil de périphérie pour un environnement de serveur de périphérie à faible résilience" caption-side="top"}

* Environnements de serveur de périphérie basés sur d'autres profils {{site.data.keyword.icp_server}} (résilience moyenne à élevée)

  Utilisez les valeurs des exemples de déploiement petit, moyen et grand lorsque vous avez besoin d'une configuration différente de celle du {{site.data.keyword.edge_profile}} pour votre environnement de serveur de périphérie. Pour plus d'informations, voir [Dimensionnement de votre cluster {{site.data.keyword.icp_server}} - Exemples de déploiement ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples).
