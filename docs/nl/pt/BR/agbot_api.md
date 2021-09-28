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

# API do Agbot
{: #agbot_api}

No {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), o software do robô de contrato do {{site.data.keyword.horizon}} é executado automaticamente. Cada robô de contrato é responsável por se comunicar com todos os agentes que estão registrados para executar serviços, negociando acordos com os agentes. Os comandos `hzn agbot` interagem com essas APIs de REST. Essas APIs não são acessíveis remotamente; elas só podem ser usadas por processos em execução no mesmo host que o robô de contrato.

Para obter mais informações, consulte [{{site.data.keyword.horizon}} APIs  de robô de contrato](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md).

O {{site.data.keyword.horizon_exchange}} também expõe as APIs de REST de configuração do robô de contrato, que são acessadas pelo comando `hzn exchange agbot`.
