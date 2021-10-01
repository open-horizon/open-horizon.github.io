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

# API de l'agbot
{: #agbot_api}

Dans {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_ieam}}), le logiciel agbot {{site.data.keyword.horizon}} s'exécute automatiquement. Chaque agbot est chargé de communiquer avec l'ensemble des agents enregistrés pour exécuter le pattern de déploiement affecté à l'agbot, y compris tous les services du pattern. Les agbots négocient des accords avec les agents. Avec les interfaces de programmation REST de l'agbot, vous pouvez configurer l'agbot via `http://localhost:8046`. Les commandes `hzn agbot` interagissent avec ces interfaces de programmation REST.

Pour plus d'informations, voir [{{site.data.keyword.horizon}} agbot REST API ![S'ouvre dans un nouvel onglet](../../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://github.com/open-horizon/anax/blob/master/doc/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} expose également la configuration des API REST, qui sont accessibles via la commande `hzn exchange agbot`.
