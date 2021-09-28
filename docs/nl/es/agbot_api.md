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

# API de Agbot
{: #agbot_api}

En {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), el software de agbot de {{site.data.keyword.horizon}} se ejecuta automáticamente. Cada agbot es responsable de comunicarse con todos los agentes que están registrados para ejecutar servicios negociando acuerdos con los agentes. Los mandatos `hzn agbot` interactúan con estas API REST. Estas API no son accesibles de forma remota; solo pueden utilizarlas los procesos que se ejecuten en el mismo host que el agbot.

Para obtener más información, consulte [{{site.data.keyword.horizon}} Agreement Bot APIs](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

{{site.data.keyword.horizon_exchange}} también expone las API REST de configuración de agbot, a las que se accede mediante el mandato `hzn exchange agbot`.
