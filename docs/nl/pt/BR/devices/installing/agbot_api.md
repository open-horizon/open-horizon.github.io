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

# API do Agbot
{: #agbot_api}

No {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_ieam}}), o software do robô de contrato do {{site.data.keyword.horizon}} é executado automaticamente. Cada agbot é responsável por comunicar-se com todos os agentes que estão registrados para executar o padrão de implementação designado para o agbot, incluindo todos os serviços do padrão. Os agbots negociam os contratos com os agentes. Com as APIs de REST do agbot, é possível configurar o agbot usando `http://localhost:8046`. Os comandos `hzn agbot` interagem com essas APIs de REST.

Para obter mais informações, consulte [API de REST do agbot do {{site.data.keyword.horizon}}![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/anax/blob/master/doc/agreement_bot_api.md).

O {{site.data.keyword.horizon_exchange}} também expõe as APIs de REST de configuração do agbot, que são acessadas pelo comando `hzn exchange agbot`.
