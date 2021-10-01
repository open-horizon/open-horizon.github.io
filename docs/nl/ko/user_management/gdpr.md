---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# GDPR 고려사항

## 주의사항
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

이는 귀사의 GDPR 대비를 준비하도록 도와주기 위한 것입니다. 여기에서는 사용자가 구성할 수 있는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 기능 정보와 GDPR을 대비하도록 조직을 준비하는 경우 제품 사용 시 고려할 사항을 제공합니다. 이 정보는 완전한 목록이 아닙니다. 클라이언트는 다양한 여러 방법으로 기능을 선택하고 구성하며, 서드파티 애플리케이션 및 시스템과 함께 여러 방법으로 제품을 사용할 수 있습니다.

<p class="ibm-h4 ibm-bold">고객은 유럽 연합 일반 개인정보 보호법률(General Data Protection Regulation)을 포함한 다양한 법령과 규정을 준수해야 할 책임이 있습니다. 고객은 고객의 비즈니스에 영향을 줄 수 있는 관련 법령 및 규정에 대한 확인과 해석, 그러한 법령 및 규정의 준수를 위해 필요한 고객의 모든 조치와 관련하여 적절한 법률 자문을 받아야 할 단독 책임이 있습니다.</p>

<p class="ibm-h4 ibm-bold">여기에 설명된 제품, 서비스, 기타 기능은 일부 클라이언트의 상황에는 해당되지 않을 수 있으며 가용성이 제한될 수 있습니다. IBM은 법률, 회계 또는 감사 관련 자문을 제공하지 않으며, IBM의 서비스나 제품 사용이 고객의 관련 법령이나 규정 준수를 보장한다는 진술이나 보증을 제공하지 않습니다.</p>

## 목차

* [GDPR](#overview)
* [GDPR을 위한 제품 구성](#productconfig)
* [데이터 수명 주기](#datalifecycle)
* [데이터 처리](#dataprocessing)
* [개인정보 사용 제한 기능](#datasubjectrights)
* [부록](#appendix)

## GDPR
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
일반 개인정보 보호법률(General Data Protection Regulation, "GDPR")은 유럽 연합(EU)에 의해 채택되어 2018년 5월 25일부터 적용되고 있습니다.

### GDPR이 중요한 이유

GDPR은 개인정보 처리를 위해 보다 엄격한 정보 보호 규제 체계를 규정하고 있습니다. GDPR 규정 사항은 다음과 같습니다.

* 개인을 위한 새롭고 강화된 권리
* 개인정보의 정의 확장
* 개인정보를 처리하는 회사 및 조직에 대한 새로운 의무
* 미준수에 대한 상당한 금전적 제재
* 데이터 유출(breach)에 대한 의무적 고지

IBM은 GDPR을 준수하기 위해 IBM의 내부 프로세스 및 상용 오퍼링을 준비하는 임무를 맡은 글로벌 준비 프로그램을 수립했습니다.

### 자세한 정보

* [EU GDPR 정보 포털](https://gdpr.eu/)
*  [ibm.com/GDPR 웹 사이트](https://www.ibm.com/data-responsibility/gdpr/)

## 제품 구성 – GDPR 대비를 위한 고려사항
{: #productconfig}

다음 절에서는 {{site.data.keyword.ieam}}의 측면을 설명하고 GDPR 요구사항을 충족하도록 클라이언트를 지원하는 기능에 대한 정보를 제공합니다.

### 데이터 수명 주기
{: #datalifecycle}

{{site.data.keyword.ieam}}은 온프레미스의 컨테이너형 애플리케이션을 개발하고 관리하기 위한 애플리케이션입니다. 이는 에지에서 컨테이너 워크로드를 관리하기 위해 통합된 환경입니다. 여기에는 컨테이너 오케스트레이터 Kubernetes, 사설 이미지 레지스트리, 관리 콘솔, 에지 노드 에이전트, 모니터링 프레임워크가 포함됩니다.

이와 같이 {{site.data.keyword.ieam}}은 애플리케이션의 구성 및 관리와 관련된 기술 데이터와 주로 관련되며, 이중 일부 데이터는 GDPR이 적용될 수 있습니다. {{site.data.keyword.ieam}}에서는 애플리케이션을 관리하는 사용자에 대한 정보도 처리합니다. 이 데이터는 고객이 GDPR 요구사항 충족을 위한 고객의 책임을 인지할 수 있도록 본 문서 전체에 설명되어 있습니다.

이 데이터는 구성 파일로서 로컬 또는 원격 파일 시스템의 {{site.data.keyword.ieam}}에 또는 데이터베이스에 유지됩니다. {{site.data.keyword.ieam}}에서 실행하도록 개발된 애플리케이션은 GDPR을 준수하는 기타 양식으로 된 개인 데이터를 사용할 수 있습니다. 데이터를 보호 및 관리하는 데 사용되는 메커니즘을 {{site.data.keyword.ieam}}에서 실행되는 애플리케이션에도 사용할 수 있습니다. {{site.data.keyword.ieam}}에서 실행되는 애플리케이션이 수집하는 개인정보를 관리하고 보호하기 위해 추가 메커니즘이 필요할 수 있습니다.

{{site.data.keyword.ieam}} 데이터 플로우를 이해하려면 Kubernetes, Docker, 운영자의 작동 방식을 이해해야 합니다. 이러한 오픈 소스 컴포넌트는 {{site.data.keyword.ieam}}의 근간이 됩니다. {{site.data.keyword.ieam}}을 사용하여 에지 노드에서 애플리케이션 컨테이너의 인스턴스(에지 서비스)를 배치합니다. 에지 서비스는 애플리케이션에 대한 세부사항을 포함하고Docker 이미지는 애플리케이션에서 실행해야 하는 모든 소프트웨어 패키지를 포함합니다.

{{site.data.keyword.ieam}}에는 오픈 소스 에지 서비스 예제 세트가 포함됩니다. 모든 {{site.data.keyword.ieam}} 차트의 목록을 보려면 [open-horizon/examples](https://github.com/open-horizon/examples){:new_window}를 참조하십시오. 오픈 소스 소프트웨어에 대한 적절한 GDPR 제어를 판별하고 구현하는 것은 고객의 책임입니다.

### {{site.data.keyword.ieam}}을 통과하는 데이터의 유형은 무엇입니까?

{{site.data.keyword.ieam}}에서는 다음과 같은 개인 데이터로 간주할 수 있는 여러 기술 데이터 카테고리를 처리합니다.

* 관리자 또는 운영자 사용자 ID 및 비밀번호
* IP 주소
* Kubernetes 노드 이름

이러한 기술 데이터를 수집, 작성, 액세스, 보안, 로그, 삭제하는 방법에 대한 정보가 이 문서의 다음 절에 설명되어 있습니다.

### IBM과 온라인 연락 시 사용되는 개인정보

{{site.data.keyword.ieam}} 클라이언트는 다양한 방식으로 {{site.data.keyword.ieam}} 주제에 대한 온라인 의견, 피드백, 요청을 IBM에 제출할 수 있습니다. 주된 방법은 다음과 같습니다.

* 공용 {{site.data.keyword.ieam}} Slack 커뮤니티
* {{site.data.keyword.ieam}} 제품 문서 페이지에 있는 공개 의견
* dW Answers의 {{site.data.keyword.ieam}} 영역에 있는 공개 의견

일반적으로 사용자 문의사항에 대한 개별적인 답변에는 고객 이름 및 이메일 주소만 사용됩니다. 이러한 개인 데이터 사용은 [IBM 온라인 개인정보 보호정책문](https://www.ibm.com/privacy/us/en/){:new_window}을 준수합니다.

### 인증

{{site.data.keyword.ieam}} 인증 관리자는 {{site.data.keyword.gui}}에서 사용자 신임 정보를 승인한 후 해당 신임 정보를 엔터프라이즈 디렉토리에 대해 신임 정보의 유효성을 검증하는 백엔드 OIDC 제공자에게 전달합니다. 그런 다음 OIDC 공급자는 JSON 웹 토큰(`JWT`)과 함께 인증 쿠키(`auth-cookie`)를 인증 관리자에게 반환합니다. JWT 토큰은 인증 요청 시 그룹 멤버십과 함께 사용자 ID 및 이메일 주소 같은 정보를 유지합니다. 그런 다음 이 인증 쿠키를 다시 {{site.data.keyword.gui}}로 전송합니다. 세션 동안 쿠키가 새로 고쳐집니다. 쿠키는 {{site.data.keyword.gui}}에서 로그아웃하거나 웹 브라우저를 닫은 후 12시간 동안 유효합니다.

{{site.data.keyword.gui}}에서 작성되는 모든 후속 인증 요청에 대해 프론트 엔드 NodeJS 서버는 해당 요청에서 사용 가능한 인증 쿠키를 디코딩한 후 인증 관리자를 호출하여 해당 요청을 유효성 검증합니다.

{{site.data.keyword.ieam}} CLI에서 사용자는 API 키를 제공해야 합니다. API 키는 `cloudctl` 명령을 사용하여 작성됩니다.

**cloudctl**, **kubectl**, **oc** CLI에서도 클러스터에 액세스하려면 인증 정보가 필요합니다. 이러한 인증 정보는 관리 콘솔로부터 얻을 수 있으며 12시간이 지나면 만료됩니다.

### 역할 맵핑

{{site.data.keyword.ieam}}에서는 역할 기반 액세스 제어(RBAC)를 지원합니다. 역할 맵핑 단계에서는 인증 단계에서 제공된 사용자 이름이 사용자나 그룹 역할에 맵핑됩니다. 인증된 사용자가 수행할 수 있는 활동에 권한을 부여할 때 역할이 사용됩니다. {{site.data.keyword.ieam}} 역할에 대한 세부사항은 [역할 기반 액세스 제어](rbac.md)를 참조하십시오.

### 팟(Pod) 보안

팟(Pod) 보안 정책은 팟(Pod)이 수행할 수 있는 작업 또는 액세스할 수 있는 대상에 대해 허브 또는 에지 클러스터 제어를 설정하는 데 사용됩니다. 팟(Pod)에 대한 자세한 정보는 [관리 허브 설치](../hub/hub.md) 및 [에지 클러스터](../installing/edge_clusters.md)를 참조하십시오.

## 데이터 처리
{: #dataprocessing}

{{site.data.keyword.ieam}}의 사용자는 구성 및 관리와 관련된 기술 데이터가 시스템 구성을 통해 처리되고 보안되는 방식을 제어할 수 있습니다.

* 역할 기반 액세스 제어(RBAC)는 사용자가 액세스할 수 있는 데이터와 기능을 제어합니다.

* 팟(Pod) 보안 정책은 팟(Pod)이 수행할 수 있는 작업 또는 액세스할 수 있는 대상에 대해 클러스터 레벨의 제어를 설정하는 데 사용됩니다.

* 전송 중 데이터는 `TLS`를 사용하여 보호됩니다. `HTTPS`(`TLS` 기반)는 사용자 클라이언트와 백엔드 서비스 사이에 데이터 전송을 보안하는 데 사용됩니다. 사용자는 설치 중에 사용할 루트 인증서를 지정할 수 있습니다.

* 저장 데이터 보호는 데이터를 암호화하기 위해 `dm-crypt`를 사용하여 지원됩니다.

* 로깅(ELK) 및 모니터링(Prometheus)을 위한 데이터 보존 기간을 구성할 수 있으며 데이터 삭제는 제공된 API를 통해 지원됩니다.

{{site.data.keyword.ieam}} 기술 데이터를 관리하고 보안 설정하는 데 사용되는 동일한 메커니즘을 사용자 개발 또는 사용자 제공 애플리케이션의 개인정보를 관리하고 보안 설정하는 데 사용할 수 있습니다. 고객은 추가 제어를 구현하기 위한 고유한 기능을 개발할 수 있습니다.

인증서에 대한 자세한 정보는 [{{site.data.keyword.ieam}} 설치](../hub/installation.md)를 참조하십시오.

## 개인정보 사용 제한 기능
{: #datasubjectrights}

이 문서상 요약된 기능을 통해 {{site.data.keyword.ieam}}을 통해 사용자는 플랫폼 내에서 개인 정보로 간주되는 기술 정보의 사용을 제한할 수 있습니다.

GDPR 하에서 사용자는 처리를 수정 및 제한하고 액세스하는 권리를 보유합니다. 이 문서의 다른 절을 참조하여 제어하십시오.
* 액세스 권리
  * {{site.data.keyword.ieam}} 관리자는 {{site.data.keyword.ieam}} 기능을 사용하여 해당 데이터에 대한 개별 액세스를 제공할 수 있습니다.
  * {{site.data.keyword.ieam}} 관리자는 {{site.data.keyword.ieam}} 기능을 사용하여 데이터 {{site.data.keyword.ieam}}에서 수집하고 개인에 대해 보유하는 데이터에 대한 정보를 제공할 수 있습니다.
* 수정할 권리
  * {{site.data.keyword.ieam}} 관리자는 {{site.data.keyword.ieam}} 기능을 사용하여 개인이 해당 데이터를 수정하거나 정정하도록 허용할 수 있습니다.
  * {{site.data.keyword.ieam}} 관리자는 {{site.data.keyword.ieam}} 기능을 사용하여 개인 데이터를 정정할 수 있습니다.
* 처리를 제한할 권리
  * {{site.data.keyword.ieam}} 관리자는 {{site.data.keyword.ieam}} 기능을 사용하여 개인 데이터에 대한 처리를 중지할 수 있습니다.

## 부록 - {{site.data.keyword.ieam}}에서 로깅되는 데이터
{: #appendix}

애플리케이션으로, {{site.data.keyword.ieam}}에서는 개인 데이터로 간주할 수 있는 여러 기술 데이터 카테고리를 처리합니다.

* 관리자 또는 운영자 사용자 ID 및 비밀번호
* IP 주소
* Kubernetes 노드 이름. 

{{site.data.keyword.ieam}}에서는 {{site.data.keyword.ieam}}에서 실행되는 애플리케이션을 관리하는 사용자에 대한 정보도 처리하며, 애플리케이션에 알려지지 않은 개인 데이터의 다른 카테고리를 도입할 수도 있습니다.

### {{site.data.keyword.ieam}} 보안

* 로그되는 데이터
  * 로그인된 사용자의 사용자 ID, 사용자 이름, IP 주소
* 데이터가 로그되는 시기
  * 로그인 요청과 함께
* 데이터가 로그되는 위치
  * `/var/lib/icp/audit`의 감사 로그에서???
  * `/var/log/audit`의 감사 로그에서???
  * ???에서 로그 교환
* 데이터를 삭제하는 방법
  * 데이터를 검색하고 감사 로그에서 레코드 삭제

### {{site.data.keyword.ieam}} API

* 로그되는 데이터
  * 컨테이너 로그에서 클라이언트의 사용자 ID, 사용자 이름, IP 주소
  * `etcd` 서버에서 Kubernetes 클러스터 상태 데이터
  * `etcd` 서버의 OpenStack 및 VMware 인증 정보
* 데이터가 로그되는 시기
  * API 요청과 함께
  * `credentials-set` 명령에서 저장된 인증 정보
* 데이터가 로그되는 위치
  * 컨테이너 로그, Elasticsearch, `etcd` 서버에서
* 데이터를 삭제하는 방법
  * 컨테이너 로그(`platform-api`, `platform-deploy`)를 컨테이너에서 삭제하거나 사용자 특정 로그 항목을 Elasticsearch에서 삭제하십시오.
  * `etcdctl rm` 명령을 사용하여 선택된 `etcd` 키 값 쌍을 선택 취소하십시오.
  * `credentials-unset` 명령을 호출하여 인증 정보를 제거하십시오.


자세한 정보는 다음을 참조하십시오.

  * [Kubernetes 로깅](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### {{site.data.keyword.ieam}} 모니터링

* 로그되는 데이터
  * IP 주소, 팟(Pod)의 이름, 릴리스, 이미지
  * 클라이언트 개발 애플리케이션에서 제거된 데이터가 개인정보를 포함할 수 있음
* 데이터가 로그되는 시기
  * Prometheus가 구성된 대상에서 메트릭을 제거할 때
* 데이터가 로그되는 위치
  * Prometheus 서버 또는 구성된 지속적 볼륨에서
* 데이터를 삭제하는 방법
  * Prometheus API를 사용하여 데이터 검색 및 삭제

자세한 정보는 [Prometheus 문서](https://prometheus.io/docs/introduction/overview/){:new_window}를 참조하십시오.


### {{site.data.keyword.ieam}} Kubernetes

* 로그되는 데이터
  * 클러스터 배치 토폴로지(제어기, 작업자, 프록시, VA의 노드 정보)
  * 서비스 구성(k8s 구성 맵) 및 시크릿(k8s 시크릿)
  * apiserver 로그에서 사용자 ID
* 데이터가 로그되는 시기
  * 클러스터를 배치할 때
  * Helm 카탈로그에서 애플리케이션을 배치할 때
* 데이터가 로그되는 위치
  * `etcd`의 클러스터 배치 토폴로지
  * `etcd`에서 배치된 애플리케이션의 구성 및 시크릿
* 데이터를 삭제하는 방법
  * {{site.data.keyword.ieam}} {{site.data.keyword.gui}} 사용
  * k8s {{site.data.keyword.gui}}(`kubectl`) 또는 `etcd` REST API를 사용하여 데이터 검색 및 삭제
  * Elasticsearch API를 사용하여 apiserver 로그 데이터 검색 및 삭제

Kubernetes 클러스터 구성을 수정하거나 클러스터 데이터를 삭제할 때 주의하십시오.

  자세한 정보는 [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}을 참조하십시오.

### {{site.data.keyword.ieam}} Helm API

* 로그되는 데이터
  * 사용자 이름 및 역할
* 데이터가 로그되는 시기
  * 사용자가 팀에 추가되는 차트 또는 저장소를 검색할 때
* 데이터가 로그되는 위치
  * helm-api 배치 로그, Elasticsearch
* 데이터를 삭제하는 방법
  * Elasticsearch API를 사용하여 helm-api 로그 데이터 검색 및 삭제

### {{site.data.keyword.ieam}} 서비스 브로커

* 로그되는 데이터
  * 사용자 ID(기본 로그 레벨에서가 아니라 디버그 로그 레벨 10에서만)
* 데이터가 로그되는 시기
  * 서비스 브로커에 대해 API 요청이 작성될 때
  * 서비스 브로커가 서비스 카탈로그에 액세스할 때
* 데이터가 로그되는 위치
  * 서비스 브로커 컨테이너 로그, Elasticsearch
* 데이터를 삭제하는 방법
  * Elasticsearch API를 사용하는 apiserver 로그 검색 및 삭제
  * apiserver 컨테이너에서 로그 검색 및 삭제
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  자세한 정보는 [Kubernetes kubectl](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}을 참조하십시오.
