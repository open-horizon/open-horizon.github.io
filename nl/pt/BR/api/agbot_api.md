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

No {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), o software do robô de contrato do {{site.data.keyword.horizon}} é executado automaticamente. Cada robô de contrato é responsável por comunicar-se com todos os agentes que estão registrados para executar o padrão de implementação designado para o robô de contrato, incluindo todos os serviços do padrão. Os robôs de contrato negociam os contratos com os agentes. Com as APIs de REST do robô de contrato, é possível configurar o robô de contrato usando `http://localhost:8046`. Os comandos `hzn agbot` interagem com essas APIs de REST.

Para obter mais informações, consulte [{{site.data.keyword.horizon}} APIs  de robô de contrato](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

O {{site.data.keyword.horizon_exchange}} também expõe as APIs de REST de configuração do robô de contrato, que são acessadas pelo comando `hzn exchange agbot`.
