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

# 에지 소프트웨어 관리
{: #edge_software_mgmt}

{{site.data.keyword.edge_devices_notm}}는 지리적으로 분산된 자율 프로세스에 의존하여 모든 에지 노드의 소프트웨어 라이프사이클을 관리합니다.
{:shortdesc}

에지 노드 소프트웨어 관리를 처리하는 자율 프로세스는 {{site.data.keyword.horizon_exchange}} 및 {{site.data.keyword.horizon_switch}} 서비스를 사용하여 해당 주소를 표시하지 않고 인터넷에서 서로를 찾습니다. 서로를 찾은 후 프로세스가 {{site.data.keyword.horizon_exchange}} 및 {{site.data.keyword.horizon_switch}}를 사용하여 관계를 협상한 다음 에지 노드 소프트웨어를 관리하기 위해 협업합니다. 자세한 정보는 [발견 및 협상](discovery_negotiation.md)을 참조하십시오.

모든 호스트의 {{site.data.keyword.horizon}} 소프트웨어는 에지 노드 에이전트, agbot 또는 둘 다의 역할을 수행할 수 있습니다.

## Agbot(계약 봇)

agbot 인스턴스는 {{site.data.keyword.horizon_exchange}}에 공개된 {{site.data.keyword.edge_devices_notm}}에 대한 각 소프트웨어 배치 패턴을 관리하기 위해 중앙 집중식으로 작성됩니다. 또한 사용자 또는 개발자 중 한 명이 {{site.data.keyword.horizon_exchange}} 및 {{site.data.keyword.horizon_switch}}에 액세스할 수 있는 모든 머신에서 agbot 프로세스를 실행할 수 있습니다.

agbot이 시작되고 특정 소프트웨어 배치 패턴을 관리하도록 구성되면 agbot이 {{site.data.keyword.horizon_exchange}}에 등록하고 동일한 배치 패턴을 실행하도록 등록된 에지 노드를 폴링하기 시작합니다. 에지 노드가 발견되면 agbot이 해당 에지 노드의 로컬 에이전트에 소프트웨어 관리 협업 요청을 전송합니다.

계약이 협상되면 agbot이 에이전트에 다음 정보를 전송합니다.

* 배치 패턴에 포함된 정책 세부사항
* 배치 패턴에 포함된 {{site.data.keyword.horizon}} 서비스 및 버전의 목록
* 해당 서비스 간의 종속성
* 서비스의 공유 가능성. 서비스는 `exclusive`, `singleton` 또는 `multiple`로 설정될 수 있습니다.
* 각 서비스의 각 컨테이너에 대한 세부사항. 이러한 세부사항에는 다음 정보가 포함됩니다. 
  * 컨테이너가 등록된 Docker 레지스트리(예: 공용 DockerHub 레지스트리 또는 개인용 레지스트리)
  * 개인용 레지스트리에 대한 레지스트리 인증 정보
  * 구성 및 사용자 정의를 위한 쉘 환경 세부사항
  * 컨테이너 및 해당 구성의 암호화 서명된 해시

agbot은 {{site.data.keyword.horizon_exchange}}의 소프트웨어 배치 패턴에 변경사항이 있는지 계속 모니터합니다(예: 패턴에 대한 새 버전의 {{site.data.keyword.horizon}} 서비스가 공개되었는지 여부). 변경사항이 발견되면 agbot이 패턴에 등록된 각 에지 노드에 새 소프트웨어 버전으로의 전환 관리에 대한 협업 요청을 다시 전송합니다.

또한 agbot은 배치 패턴에 등록된 각 에지 노드를 주기적으로 검사하여 패턴에 대한 정책이 적용되는지 확인합니다. 정책이 적용되지 않는 경우 agbot이 협상된 계약을 중지할 수 있습니다. 예를 들어, 에지 노드가 오랫동안 데이터 전송 또는 하트비트 제공을 중지하는 경우 agbot이 계약을 취소할 수 있습니다.  

### 에지 노드 에이전트

에지 노드 에이전트는 {{site.data.keyword.horizon}} 소프트웨어 패키지가 에지 머신에 설치될 때 작성됩니다. 소프트웨어 설치에 대한 자세한 정보는 [{{site.data.keyword.horizon}} 소프트웨어 설치](../installing/adding_devices.md)를 참조하십시오.

나중에 에지 노드를 {{site.data.keyword.horizon_exchange}}에 등록할 때 다음 정보를 제공해야 합니다.

* {{site.data.keyword.horizon_exchange}} URL
* 에지 노드 이름 및 에지 노드에 대한 액세스 토큰
* 에지 노드에서 실행될 소프트웨어 배치 패턴. 패턴을 식별하기 위해 조직 및 패턴 이름을 모두 제공해야 합니다.

등록에 대한 자세한 정보는 [에지 머신 등록](../installing/registration.md)을 참조하십시오.

에지 시스템이 등록된 후 로컬 에이전트가 {{site.data.keyword.horizon_switch}}에서 원격 agbot 프로세스의 협업 요청을 폴링합니다. agbot이 구성된 배치 패턴에 대한 에이전트를 발견하면 에지 노드의 소프트웨어 라이프사이클 관리에 대한 협업을 협상하기 위해 에지 노드 에이전트에 요청을 전송합니다. 계약이 이루어지면 agbot이 에지 노드에 정보를 전송합니다.

에이전트가 해당 레지스트리에서 지정된 Docker 컨테이너를 가져옵니다. 그런 다음, 에이전트가 컨테이너 해시 및 암호화 서명을 확인합니다. 이후 에이전트가 지정된 환경 구성을 사용하여 종속성의 역순으로 컨테이너를 시작합니다. 컨테이너가 실행되는 동안 로컬 에이전트가 컨테이너를 모니터합니다. 컨테이너가 예기치 않게 실행을 중지하면 에이전트가 컨테이너를 재실행하여 에지 노드에서 배치 배턴을 손상되지 않은 상태로 유지하려고 시도합니다.

### {{site.data.keyword.horizon}} 서비스 종속성

{{site.data.keyword.horizon}} 에이전트가 지정된 배치 패턴에서 컨테이너를 시작하고 관리하기 위해 작업하지만 서비스 간의 종속성은 서비스 컨테이너 코드에서 관리되어야 합니다. 컨테이너는 종속성의 역순으로 시작되지만 {{site.data.keyword.horizon}}은 서비스 이용자가 시작되기 전에 서비스 제공자가 완전히 시작되고 서비스를 제공할 준비가 되도록 할 수 없습니다. 이용자가 자신이 종속된 서비스의 잠재적인 느린 시작을 전략적으로 처리해야 합니다. 서비스 제공 컨테이너에 장애가 발생하고 사용 안함으로 설정될 수 있으므로 서비스 이용자는 자신이 이용하는 서비스의 부재를 처리해야 합니다. 

서비스가 작동 중단되면 로컬 에이전트가 이를 발견하고 동일한 Docker 사설 네트워크에서 동일한 네트워크 이름으로 서비스를 시작합니다. 재실행 프로세스 중에 짧은 중단 시간이 발생합니다. 이용 서비스가 짧은 중단 시간도 처리해야 합니다. 그렇지 않으면 이용 서비스도 실패할 수 있습니다.

에이전트의 결함 허용은 제한되어 있습니다. 컨테이너가 반복적으로 빠르게 작동 중단되는 경우 에이전트가 영구적으로 실패한 서비스의 다시 시작을 포기하고 계약을 취소할 수 있습니다.

### {{site.data.keyword.horizon}} Docker 네트워킹

{{site.data.keyword.horizon}}에서는 Docker 네트워킹 기능을 사용하여 서비스를 제공하는 Docker 컨테이너를 격리합니다. 이와 같이 격리하면 권한 부여된 이용자만 컨테이너에 액세스할 수 있습니다. 각 컨테이너는 별도의 사설 Docker 가상 네트워크에서 종속성의 역순으로 시작됩니다(생성자가 먼저 시작된 후 나중에 이용자가 시작됨). 서비스 이용 컨테이너가 시작될 때마다 컨테이너가 생성자 컨테이너의 사설 네트워크에 접속됩니다. 생성자에 대한 종속성이 {{site.data.keyword.horizon}}에 알려진 이용자만 생성자 컨테이너에 접속할 수 있습니다. Docker 네트워크가 구현되는 방법에 따라 호스트 쉘에서 모든 컨테이너에 접속할 수 있습니다. 

컨테이너의 IP 주소를 얻어야 하는 경우 `docker inspect <containerID>` 명령을 사용하여 지정된 `IPAddress`를 가져올 수 있습니다. 호스트 쉘에서 컨테이너에 연결할 수 있습니다.

## 보안 및 개인정보 보호

에지 노드 에이전트와 배치 패턴 agbot이 서로를 발견할 수 있지만 협업을 위한 계약이 공식적으로 협상될 때까지 컴포넌트가 완전한 개인정보 보호를 유지합니다. 에이전트 및 agbot ID와 모든 통신이 암호화됩니다. 소프트웨어 관리 협업도 암호화됩니다. 관리되는 모든 소프트웨어가 암호화 서명됩니다. {{site.data.keyword.edge_devices_notm}}의 개인정보 보호 및 보안 측면에 대한 자세한 정보는 [보안 및 개인정보 보호](../user_management/security_privacy.md)를 참조하십시오.
