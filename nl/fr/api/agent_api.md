---

copyright:
years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# API d'agent
{: #agent_api}

Le logiciel agent {{site.data.keyword.horizon}} s'exécute sur chaque noeud de périphérie. Chaque agent est responsable de la gestion du cycle de vie logiciel des services qui sont déployés sur le noeud de périphérie. A l'aide de l'interface de programmation REST pour l'agent, vous pouvez configurer l'agent localement sur le noeud en utilisant les API REST à l'adresse `http://localhost:8510`. La commande `hzn node` interagit avec ces API REST.

Pour plus d'informations sur ces API, voir [API locales {{site.data.keyword.horizon}}](https://github.com/open-horizon/anax/blob/master/docs/api.md).
