---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 자주 묻는 질문(FAQ)
{: #faqs}

다음은 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에 대한 몇 가지 자주 묻는 질문(FAQ)에 대한 답변입니다.
{:shortdesc}

  * [개발 목적으로 자체 포함 환경을 작성하는 방법이 있습니까?](#one_click)
  * [{{site.data.keyword.ieam}} 소프트웨어는 오픈 소스입니까?](#open_sourced)
  * [{{site.data.keyword.ieam}}을 사용하여 에지 서비스를 개발 및 배치하려면 어떻게 해야 합니까?](#dev_dep)
  * [{{site.data.keyword.ieam}}에서 지원하는 에지 노드 하드웨어 플랫폼은 무엇입니까?](#hw_plat)
  * [{{site.data.keyword.ieam}}을 사용하여 내 에지 노드에서 {{site.data.keyword.linux_notm}} 배포판을 실행할 수 있습니까?](#lin_dist)
  * [{{site.data.keyword.ieam}}에서 지원되는 프로그래밍 언어 및 환경은 무엇입니까?](#pro_env)
  * [{{site.data.keyword.ieam}}의 컴포넌트에서 제공하는 REST API에 대한 자세한 문서가 있습니까?](#rest_doc)
  * [{{site.data.keyword.ieam}}에서 Kubernetes를 사용합니까?](#use_kube)
  * [{{site.data.keyword.ieam}}에서 MQTT를 사용합니까?](#use_mqtt)
  * [일반적으로 내 에지 노드를 등록한 후 계약이 형성되고 해당 컨테이너가 실행될 때까지 얼마나 걸립니까?](#agree_run)
  * [{{site.data.keyword.ieam}}과 관련된 {{site.data.keyword.horizon}} 소프트웨어 및 기타 모든 소프트웨어 또는 데이터를 에지 노드 호스트에서 제거할 수 있습니까?](#sw_rem)
  * [에지 노드에서 활성 상태에 있는 계약 및 서비스를 시각화하기 위한 대시보드가 있습니까?](#db_node)
  * [컨테이너 이미지 다운로드가 네트워크 가동 중단으로 인터럽트되면 어떻게 됩니까?](#image_download)
  * [{{site.data.keyword.ieam}}의 보안 방법은 무엇입니까?](#ieam_secure)
  * [모델이 있는 에지에서 AI를 관리하는 방법과 클라우드에서 AI를 관리하는 방법은 어떻게 다릅니까?](#ai_cloud)

## 개발 목적으로 자체 포함 환경을 작성하는 방법이 있습니까?
{: #one_click}

개발자용 "올인원" 설치 프로그램을 사용하여 오픈 소스 관리 허브({{site.data.keyword.ieam}} 관리 콘솔이 없음)를 설치할 수 있습니다. 올인원 설치 프로그램은 프로덕션용으로 적합하지 않은 완전하지만 최소의 관리 허브를 작성합니다. 또한 예제 에지 노드를 구성합니다. 이 도구를 사용하면 오픈 소스 컴포넌트 개발자가 전체 프로덕션 {{site.data.keyword.ieam}} 관리 허브를 구성하는 데 소요되는 시간 없이 빠르게 시작할 수 있습니다. 올인원 설치 프로그램에 대한 정보는 [Open Horizon-Devops](https://github.com/open-horizon/devops/tree/master/mgmt-hub)를 참조하십시오.

## {{site.data.keyword.ieam}} 소프트웨어가 오픈 소스입니까?
{: #open_sourced}

{{site.data.keyword.ieam}}은 IBM 제품입니다. 그러나 핵심 컴포넌트는 [Open Horizon - EdgeX 프로젝트 그룹](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group) 오픈 소스 프로젝트를 중용합니다. {{site.data.keyword.horizon}} 프로젝트에서 사용할 수 있는 많은 샘플과 예제 프로그램이 {{site.data.keyword.ieam}}에서 작동합니다. 프로젝트에 대한 자세한 정보는 [Open Horizon - EdgeX 프로젝트 그룹](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group)을 참조하십시오.

## {{site.data.keyword.ieam}}을 사용하여 에지 서비스를 개발 및 배치하려면 어떻게 해야 합니까?
{: #dev_dep}

[에지 서비스 사용](../using_edge_services/using_edge_services.md)을 참조하십시오.

## {{site.data.keyword.ieam}}에서 지원하는 에지 노드 하드웨어 플랫폼은 무엇입니까?
{: #hw_plat}

{{site.data.keyword.ieam}}에서는 사용 가능한 {{site.data.keyword.horizon}}용 Debian {{site.data.keyword.linux_notm}} 2진 패키지 또는 Docker 컨테이너를 통해 다양한 하드웨어 아키텍처를 지원합니다. 자세한 정보는 [{{site.data.keyword.horizon}} 소프트웨어 설치](../installing/installing_edge_nodes.md)를 참조하십시오.

## {{site.data.keyword.ieam}}을 사용하여 내 에지 노드에서 {{site.data.keyword.linux_notm}} 배포판을 실행할 수 있습니까?
{: #lin_dist}

그렇기도 하고 그렇지 않기도 합니다.

기본 이미지가 에지 노드에서 호스트 {{site.data.keyword.linux_notm}} 커널에서 작동하는 경우 Docker 컨테이너의 기본 이미지로 {{site.data.keyword.linux_notm}} 배포를 사용하는 에지 소프트웨어를 개발할 수 있습니다(Dockerfile `FROM` 문을 사용하는 경우). 즉, Docker가 에지 호스트에서 실행할 수 있는 컨테이너에 대한 배포를 사용할 수 있습니다.

그러나 에지 노드 호스트 운영 체제는 최신 버전의 Docker를 실행하고 {{site.data.keyword.horizon}} 소프트웨어를 실행할 수 있어야 합니다. 현재, {{site.data.keyword.horizon}} 소프트웨어는 {{site.data.keyword.linux_notm}}를 실행하는 에지 노드에 대한 Debian 및 RPM 패키지로만 제공됩니다. Apple Macintosh 머신의 경우 Docker 컨테이너 버전이 제공됩니다. {{site.data.keyword.horizon}} 개발 팀은 주로 Apple Macintosh, Ubuntu 또는 Raspbian {{site.data.keyword.linux_notm}} 배포를 사용합니다.

또한 RPM 패키지 설치는 Red Hat Enterprise Linux(RHEL) 버전 8.2로 구성된 에지 노드에서 테스트되었습니다.

## {{site.data.keyword.ieam}}에서 지원되는 프로그래밍 언어 및 환경은 무엇입니까?
{: #pro_env}

{{site.data.keyword.ieam}}에서는 에지 노드의 적절한 Docker 컨테이너에서 실행하도록 구성할 수 있는 거의 모든 프로그래밍 언어 및 소프트웨어 라이브러리를 지원합니다.

소프트웨어에 특정 하드웨어 또는 운영 체제 서비스에 대한 액세스가 필요한 경우 해당 액세스를 지원하기 위해 `docker run`과 동등한 인수를 제공해야 할 수도 있습니다. Docker 컨테이너 정의 파일의 `deployment` 섹션 내에 지원되는 인수를 지정할 수 있습니다.

## {{site.data.keyword.ieam}}의 컴포넌트에서 제공되는 REST API에 대한 자세한 문서가 있습니까?
{: #rest_doc}

예. 자세한 정보는 [{{site.data.keyword.ieam}} API](../api/edge_rest_apis.md)를 참조하십시오. 

## {{site.data.keyword.ieam}}이 Kubernetes를 사용합니까?
{: #use_kube}

예. {{site.data.keyword.ieam}}에서는 [{{site.data.keyword.open_shift_cp}})](https://docs.openshift.com/container-platform/4.6/welcome/index.md) Kubernetes 서비스를 사용합니다.

## {{site.data.keyword.ieam}}이 MQTT를 사용합니까?
{: #use_mqtt}

{{site.data.keyword.ieam}}에서는 내부 기능을 지원하기 위해 MQTT(Message Queuing Telemetry Transport)를 사용하지 않지만, 에지 노드에 배치하는 프로그램은 고유한 용도로 MQTT를 자유롭게 사용할 수 있습니다. 에지 노드에서 데이터를 송수신하기 위해 MQTT 및 다른 기술(예: Apache Kafka를 기반으로 하는 {{site.data.keyword.message_hub_notm}})을 사용하는 예제 프로그램을 사용할 수 있습니다.

## 일반적으로 내 에지 노드를 등록한 후 계약이 형성되고 해당 컨테이너가 실행될 때까지 얼마나 걸립니까?
{: #agree_run}

일반적으로 에이전트 및 원격 agbot의 등록 후 소프트웨어를 배치하는 계약을 완료하려면 몇 초 정도밖에 걸리지 않습니다. 이후에는 {{site.data.keyword.horizon}} 에이전트가 컨테이너를 에지 노드에 다운로드하고(`docker pull`), {{site.data.keyword.horizon_exchange}}에서 암호화 서명을 확인한 후 실행합니다. 컨테이너 크기 및 시작하고 작동하는 데 걸리는 시간에 따라 에지 노드가 완전히 작동하기까지 몇 초에서 몇 분까지 걸릴 수 있습니다.

에지 노드를 등록한 후 `hzn node list` 명령을 실행하여 에지 노드에서 {{site.data.keyword.horizon}} 상태를 볼 수 있습니다. `hzn node list` 명령에서 상태가 `configured`로 표시되면 {{site.data.keyword.horizon}} agbot이 에지 노드를 검색하고 계약을 형성하기 시작할 수 있습니다.

계약 협상 프로세스 단계를 관찰하려면 `hzn agreement list` 명령을 사용할 수 있습니다.

계약 목록이 완료되면 `docker ps` 명령을 사용하여 실행 중인 컨테이너를 볼 수 있습니다. 또한 `docker inspect <container>`를 실행하여 특정 `<container>`의 배치에 대한 자세한 정보를 확인할 수 있습니다.

## {{site.data.keyword.ieam}}과 관련된 {{site.data.keyword.horizon}} 소프트웨어 및 기타 모든 소프트웨어 또는 데이터를 에지 노드 호스트에서 제거할 수 있습니까?
{: #sw_rem}

예. 에지 노드가 등록되면 다음을 실행하여 에지 노드 등록을 해제하십시오. 
```
hzn unregister -f -r
```
{: codeblock}

에지 노드가 등록 취소되면 설치된 {{site.data.keyword.horizon}} 소프트웨어(예: Debian 기반 시스템 실행을 위해)를 제거할 수 있습니다.
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## 에지 노드에서 활성 상태에 있는 계약 및 서비스를 시각화하기 위한 대시보드가 있습니까?
{: #db_node}

{{site.data.keyword.ieam}} 웹 UI를 사용하여 에지 노드 및 서비스를 관찰할 수 있습니다.

또한 `hzn` 명령을 사용하여 에지 노드에서 로컬 {{site.data.keyword.horizon}} 에이전트 REST API를 통해 활성 계약 및 서비스에 대한 정보를 얻을 수 있습니다. API를 사용하여 관련 정보를 검색하려면 다음 명령을 실행하십시오.

```
hzn node list hzn agreement list docker ps
```
{: codeblock}

## 컨테이너 이미지 다운로드가 네트워크 가동 중단으로 인터럽트되면 어떻게 됩니까?
{: #image_download}

컨테이너 이미지를 다운로드하기 위해 Docker API가 사용됩니다. Docker API가 다운로드를 종료하면 에이전트에 오류가 리턴됩니다. 결국 에이전트가 현재 배치 시도를 취소합니다. Agbot이 취소를 발견하면 에이전트로 새 배치 시도를 시작합니다. 후속 배치를 시도하는 중에 Docker API는 다운로드를 중단한 곳부터 다시 재개합니다. 이미지가 완전히 다운로드되고 배치가 진행될 수 있을 때까지 이 프로세스는 계속됩니다. Docker 바인딩 API는 이미지 풀에 대한 책임이 있고 실패하는 경우 계약이 취소됩니다.

## {{site.data.keyword.ieam}}의 보안 방법은 무엇입니까?
{: #ieam_secure}

* {{site.data.keyword.ieam}}은 프로비저닝 중에 {{site.data.keyword.ieam}} 관리 허브와 통신하므로 에지 서비스의 암호화 방식으로 서명된 공개-개인 키 인증을 자동화하고 사용합니다. 통신은 항상 에지 노드에서 초기화하고 제어합니다.
* 시스템에 노드와 서비스 인증 정보가 있습니다.
* 해시 확인을 사용하는 소프트웨어 검증 및 인증

[에지에서 보안](https://www.ibm.com/cloud/blog/security-at-the-edge)을 참조하십시오.

## 모델이 있는 에지에서 AI를 관리하는 방법과 클라우드에서 AI를 관리하는 방법은 어떻게 다릅니까?
{: #ai_cloud}

일반적으로 에지의 AI를 사용하면 1초 미만의 대기 시간으로 즉시 시스템 추론을 수행할 수 있으므로, 유스 케이스와 하드웨어(예: RaspberryPi, Intel x86 및 Nvidia Jetson nano)를 기반으로 실시간 응답이 가능합니다. {{site.data.keyword.ieam}} 모델 관리 시스템을 사용하면 서비스 가동 중단 시간 없이 업데이트된 AI 모델을 배치할 수 있습니다.

[에지에 배치된 모델](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge)을 참조하십시오.
