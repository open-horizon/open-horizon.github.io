---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 발견 및 협상
{: #discovery_negotiation}

{{site.data.keyword.horizon_open}} 프로젝트를 기반으로 하는 {{site.data.keyword.edge_devices_notm}}는 주로 분산되고 분배됩니다. 자율 에이전트 및 계약 봇(agbot) 프로세스가 등록된 모든 에지 노드의 소프트웨어 관리를 위해 협업합니다.
{:shortdesc}

{{site.data.keyword.horizon_open}} 프로젝트에 대한 자세한 정보는 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/)의 내용을 참조하십시오.

자율 에이전트 프로세스가 각 Horizon 에지 노드에서 실행되어 에지 머신 소유자가 설정한 정책을 적용합니다.

동시에 각 소프트웨어 배치 패턴에 지정되는 자율 agbot 프로세스가 지정된 패턴에 대해 정의된 정책을 사용하여 패턴에 등록된 각 노드 에이전트를 찾습니다. 이러한 자율 agbot 및 에이전트는 에지 머신 소유자 정책에 따라 협업을 위해 정식 계약을 협상합니다. agbot 및 에이전트는 계약이 이루어질 때마다 협력하여 해당 에지 노드의 소프트웨어 라이프사이클을 관리합니다.

agbot 및 에이전트는 다음과 같은 중앙 집중식 서비스를 사용하여 서로를 찾고 신뢰를 구축하며 {{site.data.keyword.edge_devices_notm}}에서 안전하게 통신합니다.

* {{site.data.keyword.horizon_switch}}: agbot과 에이전트 간의 안전한 사설 피어 투 피어 통신을 가능하게 합니다.
* {{site.data.keyword.horizon_exchange}}: 발견을 용이하게 합니다.

<img src="../../images/edge/distributed.svg" width="90%" alt="중앙 집중식 및 분산형 서비스">

## {{site.data.keyword.horizon_exchange}}

에지 머신 소유자는 {{site.data.keyword.horizon_exchange}}를 사용하여 소프트웨어 라이프사이클 관리를 위해 에지 노드를 등록할 수 있습니다. {{site.data.keyword.edge_devices_notm}}용 {{site.data.keyword.horizon_exchange}}에 에지 노드를 등록할 때 에지 노드에 대한 배치 패턴을 지정합니다. 배치 패턴은 에지 노드, 암호화 서명된 소프트웨어 Manifest 및 연관된 구성을 관리하기 위한 정책 세트입니다. 배치 패턴은 {{site.data.keyword.horizon_exchange}}에서 디자인, 개발, 테스트, 서명 및 공개되어야 합니다.

각 에지 노드가 에지 머신 소유자의 조직 아래의 {{site.data.keyword.horizon_exchange}}에 등록되어야 합니다. 각 에지 노드는 해당 노드에 적용할 수 있는 ID 및 보안 토큰으로 등록됩니다. 자체 조직에서 제공된 소프트웨어 배치 패턴 또는 다른 조직에서 제공된 패턴(배치 패턴이 공개적으로 사용 가능한 경우)을 실행하도록 노드를 등록할 수 있습니다.

배치 패턴이 {{site.data.keyword.horizon_exchange}}에 공개되면 해당 배치 패턴 및 연관된 정책을 관리하도록 하나 이상의 agbot이 지정됩니다. 이러한 agbot이 배치 패턴에 등록된 에지 노드를 발견하려고 합니다. 등록된 에지 노드가 발견되면 agbot이 에지 노드에 대한 로컬 에이전트 프로세스와 협상합니다.

{{site.data.keyword.horizon_exchange}}는 agbot이 등록된 배치 패턴에 해당하는 에지 노드를 찾을 수 있도록 하지만 {{site.data.keyword.horizon_exchange}}는 에지 노드 소프트웨어 관리 프로세스에 직접 관여하지 않습니다. agbot과 에이전트는 소프트웨어 관리 프로세스를 처리합니다. {{site.data.keyword.horizon_exchange}}는 에지 노드에 대한 권한을 갖지 않으며 에지 노드 에이전트와의 연결을 초기화하지 않습니다.

## {{site.data.keyword.horizon_switch}}

agbot이 주기적으로 {{site.data.keyword.horizon_exchange}}를 폴링하여 배치 패턴에 등록된 모든 에지 노드를 찾습니다. agbot이 배치 패턴에 등록된 에지 노드를 발견하면 agbot이 {{site.data.keyword.horizon}} Switchboard를 사용하여 해당 노드의 에이전트에 개인 메시지를 전송합니다. 이 메시지는 에지 노드의 소프트웨어 라이프사이클 관리에 대해 협업하도록 에이전트에 요청하는 것입니다. 그 동안 에이전트는 {{site.data.keyword.horizon_switch}}의 개인 메일함에서 agbot 메시지를 폴링합니다. 메시지가 수신되면 에이전트가 요청을 복호화하고 유효성 검증하며 승인을 위해 응답합니다.

각 agbot은 {{site.data.keyword.horizon_exchange}}를 폴링할 뿐 아니라 {{site.data.keyword.horizon_switch}}의 개인 메일함도 폴링합니다. agbot이 에이전트로부터 요청 승인을 수신하면 협상이 완료됩니다.

에이전트와 agbot이 모두 {{site.data.keyword.horizon_switch}}와 공개 키를 공유하여 보안 사설 통신을 가능하게 합니다. 이 암호화를 통해 {{site.data.keyword.horizon_switch}}는 메일함 관리자 역할만 수행합니다. {{site.data.keyword.horizon_switch}}에 전송되기 전에 송신자가 모든 메시지를 암호화합니다. {{site.data.keyword.horizon_switch}}는 메시지를 복호화할 수 없습니다. 그러나 수신자는 공개 키를 사용하여 암호화된 메시지를 복호화할 수 있습니다. 또한 수신자는 송신자의 공개 키를 사용하여 수신자가 송신자에게 보내는 응답을 암호화할 수 있습니다.

**참고:** 모든 통신이 {{site.data.keyword.horizon_switch}}를 통해 중개되기 때문에 각 에지 노드의 에이전트가 이 정보를 표시하도록 선택할 때까지 각 노드의 IP 주소가 agbot에 표시되지 않습니다. 에이전트와 agbot이 성공적으로 계약을 협상하면 에이전트가 이 정보를 표시합니다.

## 소프트웨어 라이프사이클 관리

에지 노드가 특정 배치 패턴에 대해 {{site.data.keyword.horizon_exchange}}에 등록되면 해당 배치 패턴에 대한 agbot이 에지 노드에서 에이전트를 찾을 수 있습니다. 배치 패턴에 대한 agbot은 {{site.data.keyword.horizon_exchange}}를 사용하여 에이전트를 찾고 {{site.data.keyword.horizon_switch}}를 사용하여 소프트웨어 관리에 대한 협업을 위해 에이전트와 협상합니다.

에지 노드 에이전트가 agbot으로부터 협업에 대한 요청을 수신하고 제안을 평가하여 에지 노드 소유자가 정의한 정책을 준수하는지 확인합니다. 에이전트가 로컬로 설치된 키 파일을 사용하여 암호화 서명을 확인합니다. 로컬 정책에 따라 제안이 승인 가능하고 서명이 확인된 경우 에이전트가 제안을 승인하고 에이전트와 agbot이 계약을 완료합니다. 

계약이 이루어지면 agbot과 에이전트가 협업하여 에지 노드에 대한 배치 배턴의 소프트웨어 라이프사이클을 관리합니다. agbot은 시간 경과에 따라 진화하는 배치 패턴에 대한 세부사항을 제공하고 에지 노드의 준수를 모니터합니다. 에이전트가 에지 노드에 로컬로 소프트웨어를 다운로드하고 소프트웨어에 대한 서명을 확인하며, 승인된 경우 소프트웨어를 실행하고 모니터합니다. 필요한 경우 에이전트가 소프트웨어를 업데이트하고 적절한 때에 소프트웨어를 중지합니다.

소프트웨어 관리 프로세스에 대한 자세한 정보는 [에지 소프트웨어 관리](edge_software_management.md)를 참조하십시오.
