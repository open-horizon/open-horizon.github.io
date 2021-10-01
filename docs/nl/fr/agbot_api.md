---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# API d'agbot
{: #agbot_api}

Dans {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), le logiciel agbot {{site.data.keyword.horizon}} s'exécute automatiquement. Chaque bot d'accord est responsable de la communication avec tous les agents enregistrés pour exécuter les services en négociant des accords avec les agents. Les commandes `hzn agbot` interagissent avec ces interfaces de programmation REST. Ces API ne sont pas accessibles à distance ; elles ne peuvent être utilisées que par des processus exécutés sur le même hôte que le bot d'accord.

Pour plus d'informations, voir [{{site.data.keyword.horizon}} Agreement Bot APIs](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} expose également la configuration des API REST, qui sont accessibles via la commande `hzn exchange agbot`.
