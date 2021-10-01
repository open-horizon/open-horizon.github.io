---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 보안 및 개인정보 보호
{: #security_privacy}

{{site.data.keyword.horizon}} 기반의 {{site.data.keyword.edge_devices_notm}}는 공격으로부터 최대한 안전하며 참가자 개인정보를 보호합니다. {{site.data.keyword.edge_devices_notm}}는 지리적으로 분산된 자율 에이전트 프로세스 및 계약 봇(agbot) 프로세스에 의존하여 에지 소프트웨어를 관리하고 익명성을 유지합니다.
{:shortdesc}

익명성을 유지하기 위해 에이전트 및 agbot 프로세스가 {{site.data.keyword.edge_devices_notm}}에 대한 전체 발견 및 협상 프로세스에서 공개 키만 공유합니다. 기본적으로 {{site.data.keyword.edge_devices_notm}} 내의 모든 당사자는 서로를 신뢰할 수 없는 엔티티로 취급합니다. 당사자는 신뢰가 설정되고, 당사자 간의 협상이 완료되고, 정식 계약이 체결된 경우에만 정보를 공유하고 협업합니다.

## 분산 제어 플레인
{: #dc_pane}

일반적인 중앙 집중식 IoT(Internet of Things) 플랫폼 및 클라우드 기반 제어 시스템과 대조적으로 {{site.data.keyword.edge_devices_notm}}의 제어 플레인은 대부분 분산됩니다. 각 역할이 연관된 태스크를 완료하는 데 필요한 최소 레벨의 권한만 가지도록 시스템 내 각 역할의 권한 범위는 제한되어 있습니다. 단일 권한으로 전체 시스템을 제어할 수 없습니다. 사용자 또는 역할은 단일 호스트 또는 소프트웨어 컴포넌트를 절충하여 시스템의 모든 노드에 대한 액세스 권한을 얻을 수 없습니다.

제어 플레인은 세 개의 다른 소프트웨어 엔티티로 구현됩니다.
* {{site.data.keyword.horizon}} 에이전트
* {{site.data.keyword.horizon}} agbot
* {{site.data.keyword.horizon_exchange}}

{{site.data.keyword.horizon}} 에이전트 및 agbot은 기본 엔티티이며 에지 노드를 관리하기 위해 자율적으로 작동합니다. {{site.data.keyword.horizon_exchange}}는 발견, 협상 및 에이전트와 agbot 간의 보안 통신을 용이하게 합니다.

### 에이전트
{: #agents}

{{site.data.keyword.horizon}} 에이전트는 {{site.data.keyword.edge_devices_notm}}의 다른 모든 액터보다 수가 많습니다. 에이전트는 각 관리 에지 노드에서 실행됩니다. 각 에이전트에는 해당 단일 에지 노드만 관리할 수 있는 권한이 있습니다. 에이전트가 {{site.data.keyword.horizon_exchange}}에 공개 키를 알리고 로컬 노드의 소프트웨어를 관리하기 위해 원격 agbot 프로세스와 협상합니다. 에이전트는 에이전트의 조직 내에서 배치 패턴을 담당하는 agbot으로부터의 통신만 수신할 것으로 예상합니다.

손상된 에이전트에는 다른 에지 노드 또는 시스템의 다른 컴포넌트에 영향을 미칠 수 있는 권한이 없습니다. 호스트 운영 체제 또는 에지 노드의 에이전트 프로세스가 해킹되었거나 다른 방식으로 손상된 경우 해당 에지 노드만 손상됩니다. {{site.data.keyword.edge_devices_notm}} 시스템의 다른 모든 파트는 영향을 받지 않습니다.

에지 노드 에이전트는 에지 노드의 가장 강력한 컴포넌트일 수 있지만 전체 {{site.data.keyword.edge_devices_notm}} 시스템의 보안을 손상시킬 가능성이 가장 적은 컴포넌트입니다. 에이전트는 소프트웨어를 에지 노드로 다운로드하고 소프트웨어를 확인한 후 소프트웨어를 실행하고 에지 노드의 다른 소프트웨어 및 하드웨어와 링크합니다. 그러나 {{site.data.keyword.edge_devices_notm}}에 대한 전체 시스템 전반의 보안 내에서 에이전트에는 에이전트가 실행 중인 에지 노드를 넘어서는 권한이 없습니다.

### Agbot
{: #agbots}

{{site.data.keyword.horizon}} agbot 프로세스는 어디서나 실행될 수 있습니다. 기본적으로 이 프로세스는 자동으로 실행됩니다. agbot 인스턴스는 {{site.data.keyword.horizon}}에서 두 번째로 가장 일반적인 액터입니다. 각 agbot은 해당 agbot에 지정된 배치 패턴만 담당합니다. 배치 패턴은 주로 정책과 소프트웨어 서비스 Manifest로 구성됩니다. 단일 agbot 인스턴스가 조직에 대한 다중 배치 패턴을 관리할 수 있습니다.

개발자가 {{site.data.keyword.edge_devices_notm}} 사용자 조직의 컨텍스트에서 배치 패턴을 공개합니다. agbot이 {{site.data.keyword.horizon}} 에이전트에 배치 패턴을 제공합니다. 에지 노드가 {{site.data.keyword.horizon_exchange}}에 등록되면 조직에 대한 배치 패턴이 에지 노드에 지정됩니다. 해당 에지 노드의 에이전트는 해당 특정 조직의 해당 특정 배치 패턴을 나타내는 agbot의 요청만 승인합니다. agbot이 배치 패턴의 전달 수단이지만 에지 노드 소유자가 에지 노드에 대해 설정한 정책에서 배치 패턴 자체를 허용할 수 있어야 합니다. 배치 패턴은 서명 유효성 검증을 통과해야 합니다. 그렇지 않으면 에이전트가 패턴을 승인하지 않습니다.

손상된 agbot은 에지 노드와의 악성 계약을 제안하고 에지 노드에 악성 배치 패턴을 배치하려고 시도할 수 있습니다. 그러나 에지 노드 에이전트는 에이전트가 등록을 통해 요청했으며 에지 노드에 설정된 정책에서 허용되는 배치 패턴에 대한 계약만 승인합니다. 또한 에이전트는 패턴을 승인하기 전에 공개 키를 사용하여 패턴의 암호화 서명을 유효성 검증합니다.

agbot 프로세스가 소프트웨어 설치 및 유지보수 업데이트를 오케스트레이션하지만 agbot에는 강제로 에지 노드 또는 에이전트에게 agbot이 제공하는 소프트웨어를 승인하도록 할 수 있는 권한이 없습니다. 각 개별 에지 노드의 에이전트가 승인하거나 거부할 소프트웨어를 결정합니다. 에이전트는 설치한 공개 키 및 에지 노드 소유자가 에지 노드를 {{site.data.keyword.horizon_exchange}}에 등록할 때 설정한 정책을 기반으로 의사결정을 합니다.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

{{site.data.keyword.horizon_exchange}}는 분산 에이전트와 agbot이 만나 계약을 협약할 수 있도록 하는 중앙 집중식이지만 지리적으로 복제되고 로드 밸런싱된 서비스입니다. 자세한 정보는 [{{site.data.keyword.edge}} 개요](../../getting_started/overview_ieam.md)를 참조하십시오.

{{site.data.keyword.horizon_exchange}}는 또한 사용자, 조직, 에지 노드와 공개된 모든 서비스, 정책 및 배치 패턴에 대한 메타데이터의 공유 데이터베이스 역할을 합니다.

개발자는 작성한 소프트웨어 서비스 구현, 정책 및 배치 패턴에 대한 JSON 메타데이터를 {{site.data.keyword.horizon_exchange}}에 공개합니다. 개발자가 이 정보를 해시하고 암호화 서명합니다. 로컬 에이전트가 키를 사용하여 서명의 유효성을 검증할 수 있도록 에지 노드 소유자가 에지 노드 등록 중에 소프트웨어에 대한 공개 키를 설치해야 합니다.

손상된 {{site.data.keyword.horizon_exchange}}는 에이전트 및 agbot 프로세스에 악의적으로 잘못된 정보를 제공할 수 있지만 시스템에 기본 제공되는 검증 메커니즘으로 인해 최소한의 영향만 미칩니다. {{site.data.keyword.horizon_exchange}}에는 메타데이터에 악의적으로 서명하는 데 필요한 인증 정보가 없습니다. 손상된 {{site.data.keyword.horizon_exchange}}가 사용자 또는 조직을 악의적으로 위조할 수 없습니다. {{site.data.keyword.horizon_exchange}}는 개발자 또는 에지 노드 소유자가 발견 및 협상 프로세스 중에 agbot을 사용으로 설정하는 데 사용하기 위해 공개한 아티팩트에 대한 웨어하우스 역할을 합니다.

또한 {{site.data.keyword.horizon_exchange}}는 에이전트와 agbot 간의 모든 통신을 중재하고 보호합니다. 이는 참가자가 처리된 메시지를 다른 참가자에게 남길 수 있는 메일함 메커니즘을 구현합니다. 메시지를 수신하려면 참가자가 Horizon 스위치보드를 폴링하여 메일함에 메시지가 포함되어 있는지 확인해야 합니다.

또한 에이전트와 agbot이 모두 {{site.data.keyword.horizon_exchange}}와 공개 키를 공유하여 보안 사설 통신을 가능하게 합니다. 참가자가 다른 참가자와 통신해야 하는 경우 해당 송신자가 정해진 수신자의 공개 키를 사용하여 수신자를 식별합니다. 송신자가 해당 공개 키를 사용하여 수신자에게 보낼 메시지를 암호화합니다. 그런 다음, 수신자가 송신자의 공개 키를 사용하여 응답을 암호화할 수 있습니다.

이 접근 방식을 사용하면 메시지를 복호화하는 데 필요한 공유 키가 없으므로 Horizon Exchange에서 메시지를 도청할 수 없습니다. 정해진 수신자만 메시지를 복호화할 수 있습니다. 손상된 Horizon Exchange는 참가자의 통신을 볼 수 없으며 참가자 간의 대화에 악의적인 통신을 삽입할 수 없습니다.

## 서비스 거부(DoS) 공격
{: #denial}

{{site.data.keyword.horizon}}은 중앙 집중식 서비스에 의존합니다. 일반 IoT(Internet of Things) 시스템의 중앙 집중식 서비스는 일반적으로 서비스 거부(DoS) 공격에 취약합니다. {{site.data.keyword.edge_devices_notm}}의 경우 이러한 중앙 집중식 서비스는 발견, 협상 및 업데이트 태스크에만 사용됩니다. 분산된 자율 에이전트 및 agbot 프로세스는 발견, 협상 및 업데이트 태스크를 완료해야 하는 경우에만 중앙 집중식 서비스를 사용합니다. 그렇지 않으면, 계약이 형성될 때 해당 중앙 집중식 서비스가 오프라인 상태인 경우에도 시스템이 계속 정상적으로 작동할 수 있습니다. 이 동작은 중앙 집중식 서비스에 대한 공격이 있는 경우에 {{site.data.keyword.edge_devices_notm}}가 활성 상태로 유지되도록 합니다.

## 비대칭 암호화
{: #asym_crypt}

대부분의 {{site.data.keyword.edge_devices_notm}} 암호화는 비대칭 키 암호화를 기반으로 합니다. 이 암호화 양식을 사용하는 경우 사용자와 개발자가 `hzn key` 명령을 사용하여 키 쌍을 생성하고 사용자의 개인 키를 사용하여 공개할 소프트웨어 또는 서비스에 암호화 서명해야 합니다. 소프트웨어 또는 서비스의 암호화 서명이 확인될 수 있도록 소프트웨어 또는 서비스가 실행되어야 하는 에지 노드에 공개 키를 설치해야 합니다.

에이전트와 agbot이 개인 키를 사용하여 서로 메시지에 암호화 서명하고 상대방의 공개 키를 사용하여 수신하는 메시지를 확인합니다. 또한 정해진 수신자만 메시지를 복호화할 수 있도록 에이전트와 agbot이 상대방의 공개 키로 메시지를 암호화합니다.

에이전트, agbot 또는 사용자에 대한 개인 키와 인증 정보가 손상되면 해당 엔티티에서 제어하는 아티팩트만 노출됩니다. 

## 요약
{: #summary}

{{site.data.keyword.edge_devices_notm}}는 해시, 암호화 서명 및 암호화를 사용하여 대부분의 플랫폼 파트를 원치 않는 액세스로부터 보호합니다. {{site.data.keyword.edge_devices_notm}}는 주로 분산되어 있으므로 일반적으로 기존 IoT(Internet of Things) 플랫폼에서 발견되는 대부분의 공격에 노출되지 않습니다. 참가자 역할에 대한 권한 및 영향의 범위를 제한하여 {{site.data.keyword.edge_devices_notm}}에는 손상된 호스트 또는 손상된 소프트웨어 컴포넌트로 인한 해당 시스템 파트의 잠재적인 손상이 포함됩니다. {{site.data.keyword.edge_devices_notm}}에서 사용되는 {{site.data.keyword.horizon}} 서비스의 중앙 집중식 서비스에 대한 대규모 외부 공격도 이미 계약이 이루어진 참가자에게 최소한의 영향을 미칩니다. 작업 계약의 적용을 받는 참가자는 중단 없이 계속 정상적으로 작동합니다.
