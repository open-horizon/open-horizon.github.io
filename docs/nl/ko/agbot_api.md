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

# Agbot API
{: #agbot_api}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서 {{site.data.keyword.horizon}} agbot 소프트웨어가 자동으로 실행됩니다. 각 agbot는 에이전트와 계약을 협상하여 서비스를 실행하기 위해 등록된 모든 에이전트와 통신할 책임이 있습니다. `hzn agbot` 명령이 이러한 REST API와 상호작용합니다. 이러한 API는 원격으로 액세스할 수 없으며, agbot와 동일한 호스트에서 실행 중인 프로세스에서만 사용할 수 있습니다.

자세한 정보는 [{{site.data.keyword.horizon}} 계약 봇 API](https://github.com/open-horizon/anax/blob/master/docs/agreement_bot_api.md)를 참조하십시오.

또한 {{site.data.keyword.horizon_exchange}}는 `hzn exchange agbot` 명령을 통해 액세스하는 agbot 구성 REST API를 노출합니다.
