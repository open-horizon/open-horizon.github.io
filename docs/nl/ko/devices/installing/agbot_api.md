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

# Agbot API
{: #agbot_api}

{{site.data.keyword.edge_notm}}({{site.data.keyword.edge_ieam}})에서 {{site.data.keyword.horizon}} agbot 소프트웨어가 자동으로 실행됩니다. 각 agbot은 패턴에 대한 서비스를 포함하여 agbot에 대해 지정된 배치 패턴을 실행하도록 등록된 모든 에이전트와의 통신을 담당합니다. agbot은 에이전트와 계약을 협상합니다. agbot REST API를 통해 `http://localhost:8046`을 사용하여 agbot을 구성할 수 있습니다. `hzn agbot` 명령이 이러한 REST API와 상호작용합니다.

자세한 정보는 [{{site.data.keyword.horizon}} agbot REST API ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/anax/blob/master/doc/agreement_bot_api.md)를 참조하십시오.

또한 {{site.data.keyword.horizon_exchange}}는 `hzn exchange agbot` 명령을 통해 액세스하는 agbot 구성 REST API를 노출합니다.
