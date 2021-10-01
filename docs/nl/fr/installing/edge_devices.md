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

# Dispositifs de périphérie
{: #edge_devices}

Un dispositif de périphérie fournit un point d'entrée dans les réseaux principaux de l'entreprise ou du fournisseur de service. Cela concerne par exemple les smartphones, les caméras de surveillance, voire les fours micro-ondes connectés.

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) est disponible pour des concentrateurs de gestion ou des serveurs, y compris des dispositifs distribués. Consultez les sections suivantes pour en savoir plus sur l'installation de l'agent {{site.data.keyword.ieam}} léger sur des dispositifs de périphérie :

* [Préparation d'un dispositif de périphérie](../installing/adding_devices.md)
* [Installation de l'agent](../installing/registration.md)
* [Mise à jour de l'agent](../installing/updating_the_agent.md)

Tous les dispositifs de périphérie (noeuds de périphérie) nécessitent l'installation du logiciel de l'{{site.data.keyword.horizon_agent}}. L'{{site.data.keyword.horizon_agent}} dépend également du logiciel [Docker](https://www.docker.com/). 

Le diagramme ci-dessous illustre le flux des étapes nécessaires à la configuration du dispositif de périphérie, ainsi que les opérations exécutées par l'agent une fois celui-ci démarré.

<img src="../OH/docs/images/edge/05a_Installing_edge_agent_on_device.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}, agbots and agents">
