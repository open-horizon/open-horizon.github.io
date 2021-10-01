---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 알려진 문제 및 제한사항  
{: #knownissues}

이는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 알려진 문제 및 제한사항입니다.

{{site.data.keyword.ieam}} OpenSource 계층에 대한 열린 문제의 전체 목록을 보려면 각각의 [Horizon 저장소 열기](https://github.com/open-horizon/)에서 GitHub 문제를 검토하십시오.

{:shortdesc}

## {{site.data.keyword.ieam}} 및 {{site.data.keyword.version}}의 알려진 문제

이는 {{site.data.keyword.ieam}} {{site.data.keyword.version}}에 대한 알려진 문제점 및 제한사항입니다.

* {{site.data.keyword.ieam}}에서는 모델 관리 시스템(MMS)에 업로드된 데이터에 대한 악성코드 또는 바이러스 스캔을 수행하지 않습니다. MMS 보안에 대한 자세한 정보는 [보안 및 개인정보 보호](../OH/docs/user_management/security_privacy.md#malware)를 참조하십시오.

* **edgeNodeFiles.sh**의 **-f &lt;directory&gt;** 플래그에 의도한 효과가 없습니다. 대신 파일이 현재 디렉토리에 수집됩니다. 자세한 정보는 [문제 2187](https://github.com/open-horizon/anax/issues/2187)을 참조하십시오. 임시 해결책은 다음과 같은 명령을 실행하는 것입니다.

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* {{site.data.keyword.ieam}} 설치의 일부로 설치된 {{site.data.keyword.common_services}} 버전에 따라 인증서가 자동 갱신으로 이어지는 짧은 수명으로 작성되었을 수 있습니다. 다음 인증서 문제가 발생할 수 있습니다([이 단계를 사용하여 해결할 수 있음](cert_refresh.md)).
  * {{site.data.keyword.ieam}} 관리 콘솔에 액세스할 때 "상태 코드 502와 함께 요청이 실패함" 메시지가 있는 예기치 않은 JSON 출력이 표시됩니다.
  * 에지 노드는 인증서가 갱신될 때 업데이트되지 않으며 {{site.data.keyword.ieam}} 허브에 대해 성공적으로 통신하도록 하기 위해 수동으로 업데이트해야 합니다.

* 로컬 데이터베이스로 {{site.data.keyword.ieam}}을(를) 사용하는 경우 **cssdb** 팟(Pod)이 삭제된 후 Kubernetes 스케줄러를 통해 자동으로 다시 작성되면 Mongo 데이터베이스에 대한 데이터 손실이 발생합니다. 데이터 손실을 완화하려면 [백업 및 복구](../admin/backup_recovery.md) 문서의 내용을 수행하십시오.

* 로컬 데이터베이스로 {{site.data.keyword.ieam}}을(를) 사용하는 경우 **create-agbotdb-cluster** 또는 **create-ETF-cluster** 작업 자원이 삭제되면 작업은 해당 데이터베이스를 다시 실행하고 다시 초기화하여 데이터 손실이 발생합니다. 데이터 손실을 완화하려면 [백업 및 복구](../admin/backup_recovery.md) 문서의 내용을 수행하십시오.

* 로컬 데이터베이스 사용 시 Postgres 데이터베이스 중 하나 또는 둘 다 반응하지 않을 수도 있습니다. 이 문제를 해결하려면 반응하지 않는 데이터베이스의 센티넬 및 프록시를 모두 다시 시작하십시오. 영향을 받는 애플리케이션 및 사용자 정의 리소스(CR)에서 `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` 및 `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` 명령을 수정한 후 실행하십시오(Exchange 센티넬 예제: `oc rollout restart deploy ibm-edge-exchangedb-sentinel`).

* 아키텍처가 있는 {{site.data.keyword.rhel}}에서 **hzn service log**를 실행하면 명령이 정지됩니다. 자세한 정보는 [문제점 2826](https://github.com/open-horizon/anax/issues/2826)을 참조하십시오. 이 조건을 해결하려면 컨테이너 로그를 얻으십시오(또한 테일에 대해 -f를 지정할 수 있음).

   ```
   docker logs &amp;TWBLT;container&gt;
   ```
   {: codeblock}


## {{site.data.keyword.ieam}} {{site.data.keyword.version}}에 대한 제한사항

* {{site.data.keyword.ieam}} 제품 문서는 참여 지역에 따라 번역되지만 영어 버전은 지속적으로 업데이트됩니다. 번역 주기 사이에 영어 버전과 번역된 버전 간의 불일치가 발생할 수 있습니다. 번역된 버전이 공개된 후 불일치가 해결되었는지 여부를 확인하려면 영어 버전을 확인하십시오.

* Exchange에서 서비스, 패턴 또는 배치 정책의 **소유자** 또는 **공용** 속성을 변경하는 경우 변경사항을 보기 위해 해당 리소스에 액세스하는 데 최대 5분이 걸릴 수 있습니다. 마찬가지로, Exchange 사용자 관리 권한을 부여하는 경우 해당 변경사항을 모든 Exchange 인스턴스로 전파하는 데 최대 5분이 걸릴 수 있습니다. 시간 길이는 exchange `config.json` 파일에서 `api.cache.resourcesTtlSeconds`를 더 낮은 값(기본값은 300초)으로 설정하여 줄일 수 있습니다(이때 성능은 약간 저하됨).

* 에이전트는 종속 서비스에 대한 [모델 관리 시스템](../developing/model_management_system.md)(MMS)을 지원하지 않습니다.

* 시크릿 바인딩은 패턴에 정의된 계약이 없는 서비스에 대해서는 작동하지 않습니다.
 
* 마운트된 볼륨 디렉토리에는 0700 권한만 있기 때문에 에지 클러스터 에이전트는 K3S v1.21.3+k3s1을 지원하지 않습니다. 임시 솔루션은 [로컬 PVC에 데이터를 쓸 수 없음](https://github.com/k3s-io/k3s/issues/3704)을 참조하십시오.
 
* 각 {{site.data.keyword.ieam}} 에지 노드 에이전트는 {{site.data.keyword.ieam}} 관리 허브와의 모든 네트워크 연결을 시작합니다. 관리 허브는 에지 노드에 대한 연결을 시작하지 않습니다. 따라서 방화벽이 관리 허브에 대한 TCP 연결을 갖는 경우 에지 노드는 NAT 방화벽 뒤에 있을 수 있습니다. 그러나 에지 노드는 현재 SOCKS 프록시를 통해 관리 허브와 통신할 수 없습니다.
  
* Fedora 또는 SuSE에 에지 디바이스의 설치는 [고급 수동 에이전트 설치 및 등록](../installing/advanced_man_install.md) 방법에서만 지원됩니다.
