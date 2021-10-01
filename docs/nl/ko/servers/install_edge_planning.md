---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_servers_notm}} 설치 준비
{: #edge_planning}

{{site.data.keyword.icp_server}}를 설치하기 전에 {{site.data.keyword.mgmt_hub}}를 사용으로 설정하고 {{site.data.keyword.edge_servers_notm}}를 구성한 후, 시스템이 다음 요구사항을 만족하는지 확인하십시오. 이러한 요구사항은 계획된 에지 서버의 최소 필수 컴포넌트 및 구성을 식별합니다.
{:shortdesc}

또한 이러한 요구사항은 에지 서버를 관리하는 데 사용하려는 {{site.data.keyword.mgmt_hub}} 클러스터에 대한 최소 구성 설정을 식별합니다.

이 정보를 사용하면 에지 컴퓨팅 토폴로지와 전체 {{site.data.keyword.icp_server}} 및 {{site.data.keyword.mgmt_hub}} 설정에 대한 리소스 요구사항을 계획하는 데 도움이 될 수 있습니다.

   * [하드웨어 요구사항](#prereq_hard)
   * [지원되는 IaaS](#prereq_iaas)
   * [지원 환경](#prereq_env)
   * [필수 포트](#prereq_ports)
   * [클러스터 크기 조정 고려사항](#cluster)

## 하드웨어 요구사항
{: #prereq_hard}

에지 컴퓨팅 토폴로지에 대한 관리 노드의 크기를 조정할 때 클러스터의 크기를 조정하는 데 도움을 받으려면 단일 또는 다중 노드 배치에 대한 {{site.data.keyword.icp_server}} 크기 조정 가이드라인을 사용하십시오. 자세한 정보는 [{{site.data.keyword.icp_server}} 클러스터 크기 조정![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)을 참조하십시오.

다은 에지 서버 요구사항은 {{site.data.keyword.edge_profile}}을 사용하여 원격 오퍼레이션 센터에 배치되는 {{site.data.keyword.icp_server}} 인스턴스에만 적용됩니다.

|요구사항 |노드(부트, 마스터, 관리) |작업자 노드 |
|-----------------|-----------------------------|--------------|
|호스트 수 |1 |1 |
|코어 |4 이상 |4 이상 |
|CPU |>= 2.4GHz |>= 2.4GHz |
|RAM |8GB 이상 |8GB 이상 |
|설치를 위한 디스크 여유 공간 |150GB 이상 | |
{: caption="표 1. 최소 에지 서버 클러스터 하드웨어 요구사항" caption-side="top"}

참고: 중앙 데이터 센터에서 네트워크 연결이 끊어진 경우 150GB의 스토리지로 최대 3일 동안의 로그 및 이벤트 데이터를 보존할 수 있습니다.

## 지원되는 IaaS
{: #prereq_iaas}

다음 표는 에지 서비스에 사용할 수 있는 지원되는 IaaS(Infrastructure as a Service)를 식별합니다.

|IaaS |버전 |
|------|---------|
|에지 서버 위치에서 사용할 수 있는 Nutanix NX-3000 시리즈 |NX-3155G-G6 |
|에지 서버에서 사용할 수 있는 Nutanix에서 제공되는 IBM Hyperconverged Systems |CS821 및 CS822|
{: caption="표 2. {{site.data.keyword.edge_servers_notm}}에 지원되는 IaaS" caption-side="top"}

자세한 정보는 [IBM Hyperconverged Systems powered by Nutanix PDF ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/downloads/cas/BZP46MAV)를 참조하십시오.

## 지원 환경
{: #prereq_env}

다음 표는 에지 서버에 사용할 수 있는 추가 Nutanix 구성 시스템을 식별합니다.

|LOE 사이트 유형 |노드 유형 |클러스터 크기 |노드당 코어 수(총계) |노드당 논리 프로세서 수(총계)	|노드당 메모리(GB)(총계) |디스크 그룹당 캐시 디스크 크기(GB) |	노드당 캐시 디스크 수량	|노드당 캐시 디스크 크기(GB)	|스토리지 총 클러스터 풀 크기(모든 플래시)(TB) |
|---|---|---|---|---|---|---|---|---|---|
|소형	|NX-3155G-G6	|3노드	|24(72)	|48(144)	|256(768)	|해당사항 없음	|해당사항 없음	|해당사항 없음	|8TB |
|중형 |NX-3155G-G6 |3노드 |24(72)	|48(144)	|512(1,536)	|해당사항 없음	|해당사항 없음	|해당사항 없음	|45TB |
|대형	|NX-3155G-G6	|4노드	|24(96)	|48(192)	|512(2,048)	|해당사항 없음	|해당사항 없음	|해당사항 없음	|60TB |
{: caption="표 3. Nutanix NX-3000 시리즈에서 지원되는 구성" caption-side="top"}

|LOE 사이트 유형	|노드 유형	|클러스터 크기 |	노드당 코어 수(총계) |노드당 논리 프로세서 수(총계)	|노드당 메모리(GB)(총계)	|디스크 그룹당 캐시 디스크 크기(GB) |노드당 캐시 디스크 수량	|노드당 캐시 디스크 크기(GB)	|스토리지 총 클러스터 풀 크기(모든 플래시)(TB) |
|---|---|---|---|---|---|---|---|---|---|
|소형	|CS821(2소켓, 1U) |3노드 |20(60)	|80(240) |256(768) |해당사항 없음	|해당사항 없음	|해당사항 없음	|8TB |
|중형 |CS822(2소켓, 2U) |3노드	|22(66)	|88(264) |512(1,536) |해당사항 없음 |해당사항 없음 |해당사항 없음 |45TB |
|대형	|CS822(2소켓, 2U) |4노드 |22(88) |88(352) |512(2,048) |해당사항 없음 |해당사항 없음 |해당사항 없음 |60TB |
{: caption="표 4. Nutanix에서 제공되는 IBM Hyperconverged Systems" caption-side="top"}

자세한 정보는 [IBM Hyperconverged Systems that are powered by Nutanix ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/downloads/cas/BZP46MAV)를 참조하십시오.

## 필수 포트
{: #prereq_ports}

표준 클러스터 구성으로 원격 에지 서버를 배치하려는 경우 노드에 대한 포트 요구사항은 {{site.data.keyword.icp_server}}을 배치하기 위한 포트 요구사항과 동일합니다. 이러한 요구사항에 대한 자세한 정보는 [필수 포트 ![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html)를 참조하십시오. 허브 클러스터를 위한 필수 포트의 경우 _{{site.data.keyword.mcm_core_notm}}의 필수 포트_ 섹션을 참조하십시오.

{{site.data.keyword.edge_profile}}을 사용하여 에지 노드를 구성하려면 다음 포트를 사용으로 설정하십시오.

|포트 |프로토콜 |요구사항 |
|------|----------|-------------|
|해당사항 없음 |IPv4 | IP-in-IP를 사용하는 Calico(calico_ipip_mode: Always) |
|179 |TCP	| Calico를 Always로 설정(network_type:calico) |
|500 | TCP 및 UDP	| IPSec(ipsec.enabled: true, calico_ipip_mode: Always) |
|2380 |TCP | etcd가 사용되는 경우 Always로 설정 |
|4001 |TCP | etcd가 사용되는 경우 Always로 설정 |
|4500 |UDP | IPSec(ipsec.enabled: true) |
|9091 |TCP | Calico(network_type:calico) |
|9099 |TCP | Calico(network_type:calico) |
|10248:10252 |TCP	| Kubernetes를 Always로 설정 |
|30000:32767 | TCP 및 UDP | Kubernetes를 Always로 설정 |
{: caption="표 5. {{site.data.keyword.edge_servers_notm}}에 대한 필수 포트" caption-side="top"}

참고: 30000:32767 포트에는 외부 액세스가 있습니다. 이 포트는 Kubernetes 서비스 유형을 NodePort로 설정하는 경우에만 열려야 합니다.

## 클러스터 크기 조정 고려사항
{: #cluster}

{{site.data.keyword.edge_servers_notm}}의 경우 허브 클러스터는 일반적으로 표준 {{site.data.keyword.icp_server}} 호스팅 환경입니다. 이 환경을 사용하여 중앙 위치에서 제공되어야 하거나 제공되기를 원하는 다른 컴퓨팅 워크로드를 호스팅할 수도 있습니다. {{site.data.keyword.mcm_core_notm}} 클러스터 및 환경에서 호스팅하려는 추가 워크로드를 호스팅하기에 충분한 리소스가 있도록 허브 클러스터 환경의 크기를 조정해야 합니다. 표준 {{site.data.keyword.icp_server}} 호스팅 환경 크기 조정에 대한 자세한 정보는 [{{site.data.keyword.icp_server}} 클러스터 크기 조정![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)을 참조하십시오.

필요한 경우 리소스가 제한된 환경 내에서 원격 에지 서버를 작동할 수 있습니다. 리소스가 제한된 환경 내에서 에지 서버를 작동해야 하는 경우 {{site.data.keyword.edge_profile}} 사용을 고려하십시오. 이 프로파일은 에지 서버 환경에 필요한 최소 필수 컴포넌트만 구성합니다. 이 프로파일을 사용하는 경우에도 {{site.data.keyword.edge_servers_notm}} 아키텍처에 필요한 컴포넌트 세트 및 에지 서버 환경에서 호스팅되는 다른 애플리케이션 워크로드에 필요한 리소스를 제공하기에 충분한 리소스를 할당해야 합니다. {{site.data.keyword.edge_servers_notm}} 아키텍처에 대한 자세한 정보는 [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch)의 내용을 참조하십시오.

{{site.data.keyword.edge_profile}} 구성은 메모리 및 스토리지 리소스를 절약할 수 있지만 이 구성으로 인해 복원력 수준이 낮아집니다. 이 프로파일을 기반으로 하는 에지 서버는 허브 클러스터가 있는 중앙 데이터 센터에서 연결이 끊어진 상태로 작동할 수 있습니다. 이 연결이 끊어진 오퍼레이션은 일반적으로 최대 3일 동안 지속될 수 있습니다. 에지 서버가 실패하면 서버가 원격 운영 센터에 대한 운영 지원 제공을 중지합니다.

{{site.data.keyword.edge_profile}} 구성은 다음과 같은 기술 및 프로세스만 지원하도록 제한됩니다.
  * {{site.data.keyword.linux_notm}} 64비트 플랫폼
  * 비고가용성(HA) 배치 토폴로지
  * 작업자 노드를 day-2 오퍼레이션으로 추가 및 제거
  * 클러스터에 대한 CLI 액세스 및 클러스터 제어
  * Calico 네트워크

더 많은 복원력이 필요하거나 선행 제한사항이 너무 제약적인 경우 대신 향상된 장애 복구 지원을 제공하는 {{site.data.keyword.icp_server}}에 대한 다른 표준 배치 구성 프로파일 중 하나를 사용하도록 선택할 수 있습니다.

### 샘플 배치

* {{site.data.keyword.edge_profile}}을 기반으로 하는 에지 서버 환경(복원력 낮음)

|노드 유형 |노드 수 |CPU |메모리(GB) |디스크(GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
|부트       |1           |1   |2           |8   |
|마스터     |1           |2   |4           |16  |
|관리 |1           |1   |2           |8   |
|작업자     |1           |4   |8           |32  |
{: caption="표 6. 복원력이 낮은 에지 서버 환경의 에지 프로파일 값" caption-side="top"}

* 다른 {{site.data.keyword.icp_server}} 프로파일을 기반으로 하는 에지 서버 환경(복원력 중간-높음)

  에지 서버 환경에 {{site.data.keyword.edge_profile}} 이외의 구성을 사용해야 하는 경우 소규모, 중간 규모 및 대규모 샘플 배치 요구사항을 사용하십시오. 자세한 정보는 [{{site.data.keyword.icp_server}} 클러스터 샘플 배치![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples)를 참조하십시오.
