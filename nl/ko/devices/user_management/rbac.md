---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 역할 기반 액세스 제어
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}}에서는 여러 역할을 지원합니다. 역할은 사용자가 수행할 수 있는 조치를 결정합니다.
{:shortdesc}

## 조직
{: #orgs}

{{site.data.keyword.ieam}} 내 조직을 사용하여 리소스에 대한 액세스를 분리합니다. 조직의 리소스는 리소스를 명시적으로 공용으로 설정하지 않는 한, 해당 조직에서만 볼 수 있습니다. 공용으로 표시된 리소스는 조직에서 볼 수 있는 유일한 리소스입니다.

IBM 조직은 사전정의된 서비스 및 패턴을 제공하는 데 사용됩니다.

{{site.data.keyword.ieam}} 내에서 조직 이름은 클러스터 이름입니다.

## ID
{: #ids}

{{site.data.keyword.ieam}}에는 세 가지 유형의 ID가 있습니다.

* 두 가지 유형의 사용자가 있습니다. 사용자가 {{site.data.keyword.ieam}} 콘솔과 Exchange에 액세스할 수 있습니다.
  * IAM(Identity and Access Management) 사용자. IAM 사용자는 {{site.data.keyword.ieam}} Exchange에서 인식합니다.
    * IAM에서 LDAP 플러그인을 제공하므로, IAM에 연결된 LDAP 사용자가 IAM 사용자와 같이 동작합니다.
    * IAM API 키(**hzn** 명령과 함께 사용)는 IAM 사용자와 같이 동작합니다.
  * 로컬 Exchange 사용자: Exchange 루트 사용자가 이 예에 해당합니다. 일반적으로 다른 로컬 Exchange 사용자는 작성하지 않아도 됩니다.
* 노드(에지 디바이스 또는 에지 클러스터)
* AgBot

### 역할 기반 액세스 제어(RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}}에는 다음 역할이 포함되어 있습니다.

| **역할**    | **액세스**    |  
|---------------|--------------------|
| Exchange 루트 사용자 | Exchange에서 무제한 권한이 있습니다. 이 사용자는 Exchange 구성 파일에 정의됩니다. 원하는 경우 사용 안함으로 설정할 수 있습니다. |
| 관리자 또는 API 키 | 조직에서 무제한 권한이 있습니다. |
|비관리자 또는 API 키 | 조직에 Exchange 리소스(노드, 서비스, 패턴, 정책)를 작성할 수 있습니다. 이 사용자가 소유한 리소스를 업데이트하거나 삭제할 수 있습니다. 조직의 모든 서비스, 패턴 및 정책과 다른 조직의 공용 서비스 및 패턴을 읽을 수 있습니다. |
| 노드 | Exchange의 고유 노드를 읽고, 조직의 모든 서비스, 패턴 및 정책과 다른 조직의 공용 서비스와 패턴을
읽을 수 있습니다. |
|Agbot | IBM 조직의 Agbot은 모든 조직의 모든 노드, 서비스, 패턴 및 정책을 읽을 수 있습니다. |
{: caption="표 1. RBAC 역할" caption-side="top"}
