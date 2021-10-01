---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 문제점 해결 팁
{: #troubleshooting_devices}

{{site.data.keyword.edge_notm}}에 문제가 발생한 경우 다음 질문을 검토하십시오. 각 질문에 대한 팁과 안내서가 공통 문제를 해결하고 근본 원인을 식별하기 위한 정보를 얻는 데 도움이 될 수 있습니다.
{:shortdesc}

  * [현재 릴리스된 버전의 {{site.data.keyword.horizon}} 패키지가 설치되어 있습니까?](#install_horizon)
  * [{{site.data.keyword.horizon}} 에이전트가 현재 시작되어 활발히 실행 중입니까?](#setup_horizon)
  * [에지 노드가 {{site.data.keyword.horizon_exchange}}와 상호작용하도록 구성되었습니까?](#node_configured)
  * [에지 노드에 필요한 Docker 컨테이너가 실행 중입니까?](#node_running)
  * [예상되는 서비스 컨테이너 버전이 실행 중입니까?](#run_user_containers)
  * [예상 컨테이너가 안정적입니까?](#containers_stable)
  * [Docker 컨테이너가 네트워크로 올바르게 연결되어 있습니까?](#container_networked)
  * [컨테이너의 컨텍스트 내에서 종속성 컨테이너에 연결할 수 있습니까?](#setup_correct)
  * [사용자 정의 컨테이너가 로그에 오류 메시지를 생성하고 있습니까?](#log_user_container_errors)
  * [{{site.data.keyword.message_hub_notm}} Kafka 브로커의 조직 인스턴스를 사용할 수 있습니까?](#kafka_subscription)
  * [컨테이너가 {{site.data.keyword.horizon_exchange}}에 공개됩니까?](#publish_containers)
  * [공개된 배치 패턴에 모든 필수 서비스 및 버전이 포함되어 있습니까?](#services_included)
  * [{{site.data.keyword.open_shift_cp}} 환경에 특정한 문제점 해결 팁](#troubleshooting_icp)
  * [노드 오류 문제점 해결](#troubleshooting_node_errors)
  * [RHEL에서 Podman을 설치 제거하는 방법은 무엇입니까?](#uninstall_podman)

## 현재 릴리스된 버전의 {{site.data.keyword.horizon}} 패키지가 설치되어 있습니까?
{: #install_horizon}

에지 노드에 설치된 {{site.data.keyword.horizon}} 소프트웨어가 항상 최근 릴리스된 버전인지 확인하십시오.

{{site.data.keyword.linux_notm}} 시스템에서 일반적으로 다음 명령을 실행하여 설치된 {{site.data.keyword.horizon}} 패키지 버전을 확인할 수 있습니다.  
```
dpkg -l | grep horizon
```
{: codeblock}

시스템에서 패키지 관리자를 사용하는 {{site.data.keyword.horizon}} 패키지를 업데이트할 수 있습니다. 예를 들어, Ubuntu 기반 {{site.data.keyword.linux_notm}} 시스템에서 다음 명령을 사용하여 {{site.data.keyword.horizon}}을 현재 버전으로 업데이트하십시오.
```
sudo apt update sudo apt install -y blue horizon
```

## {{site.data.keyword.horizon}} 에이전트가 시작되어 활발히 실행 중입니까?
{: #setup_horizon}

다음 {{site.data.keyword.horizon}} CLI 명령을 사용하여 에이전트가 실행 중인지 확인할 수 있습니다.
```
hzn node list | jq .
```
{: codeblock}

또한 호스트의 시스템 관리 소프트웨어를 사용하여 {{site.data.keyword.horizon}} 에이전트 상태를 확인할 수 있습니다. 예를 들어, Ubuntu 기반 {{site.data.keyword.linux_notm}} 시스템에서 `systemctl` 유틸리티를 사용할 수 있습니다.
```
sudo systemctl status horizon
```
{: codeblock}

에이전트가 활성 상태인 경우 다음과 유사한 행이 표시됩니다.
```
Active: active (running) since Thu 2020-10-01 17:56:12 UTC; 2 weeks 0 days ago
```
{: codeblock}

## 에지 노드가 {{site.data.keyword.horizon_exchange}}와 상호작용하도록 구성되었습니까? 
{: #node_configured}

{{site.data.keyword.horizon_exchange}}에서 통신할 수 있는지 확인하려면 다음 명령을 실행하십시오.
```
hzn exchange version
```
{: codeblock}

{{site.data.keyword.horizon_exchange}}에 액세스 가능한지 확인하려면 다음 명령을 실행하십시오.
```
hzn exchange user list
```
{: codeblock}

에지 노드가 {{site.data.keyword.horizon}}에 등록된 후 로컬 {{site.data.keyword.horizon}} 에이전트 구성을 확인하여 노드가 {{site.data.keyword.horizon_exchange}}와 상호작용하고 있는지 확인할 수 있습니다. 다음 명령을 실행하여 에이전트 구성을 보십시오.
```
hzn node list | jq .configuration.exchange_api
```
{: codeblock}

## 에지 노드에 필요한 Docker 컨테이너가 실행 중입니까?
{: #node_running}

에지 노드가 {{site.data.keyword.horizon}} 등록되면 {{site.data.keyword.horizon}} Agbot이 에지 노드와의 계약을 작성하여 게이트웨이 유형(배치 패턴)에서 참조되는 서비스를 실행합니다. 계약이 작성되지 않은 경우 다음 검사를 완료하여 문제를 해결하십시오.

에지 노드가 `configured` 상태이고 `id`, `organization` 값이 올바른지 확인하십시오. 또한 {{site.data.keyword.horizon}}에서 보고하는 아키텍처가 서비스에 대한 메타데이터에 사용한 아키텍처와 동일한지 확인하십시오. 다음 명령을 실행하여 이러한 설정을 나열하십시오.
```
hzn node list | jq .
```
{: codeblock}

해당 값이 예상대로이면 다음을 실행하여 에지 노드의 계약 상태를 확인할 수 있습니다. 
```
hzn agreement list | jq .
```
{: codeblock}

이 명령이 계약을 표시하지 않으면 해당 계약이 구성되었어도 문제점이 발견되었을 수 있습니다. 이 경우 계약은 이전 명령의 출력에 표시되기 전에 취소되었을 수 있습니다. 계약이 취소된 경우 취소된 계약은 아카이브된 계약 목록에 `terminated_description` 상태로 표시됩니다. 다음 명령을 실행하여 아카이브된 목록을 볼 수 있습니다. 
```
hzn agreement list -r | jq .
```
{: codeblock}

계약이 작성되기 전에 문제점이 발생할 수도 있습니다. 이 문제점이 발생하면 {{site.data.keyword.horizon}} 에이전트에 대한 이벤트 로그를 검토하여 가능한 오류를 식별하십시오. 다음 명령을 실행하여 로그를 보십시오. 
```
hzn eventlog list
``` 
{: codeblock}

이벤트 로그에는 다음이 포함될 수 있습니다. 

* 서비스 메타데이터, 특히 `deployment` 필드의 서명을 확인할 수 없습니다. 이 오류는 일반적으로 서명 공개 키를 에지 노드로 가져오지 않았음을 의미합니다. `hzn key import -k <pubkey>` 명령을 사용하여 키를 가져올 수 있습니다. `hzn key list` 명령을 사용하여 로컬 에지 노드로 가져온 키를 볼 수 있습니다. 다음 명령을 사용하여 {{site.data.keyword.horizon_exchange}}의 서비스 메타데이터가 키로 서명되었는지 확인할 수 있습니다.
  ```
  hzn exchange service verify -k $PUBLIC_KEY_FILE <service-id>
  ```
  {: codeblock} 

`<service-id>`를 서비스의 ID로 바꾸십시오. 이 ID는 샘플 형식 `workload-cpu2wiotp_${CPU2WIOTP_VERSION}_${ARCH2}`와 유사합니다.

* 서비스 `deployment` 필드의 Docker 이미지에 대한 경로가 올바르지 않습니다. 에지 노드에서 해당 이미지 경로를 `docker pull`할 수 있는지 확인하십시오.
* 에지 노드의 {{site.data.keyword.horizon}} 에이전트가 Docker 이미지를 보유하는 Docker 레지스트리에 액세스할 수 없습니다. 원격 Docker 레지스트리의 Docker 이미지가 누구나 읽을 수 있는 이미지가 아닌 경우 `docker login` 명령을 사용하여 에지 노드에 인증 정보를 추가해야 합니다. 인증 정보는 에지 노드에 저장되기 때문에 이 단계를 한 번 완료해야 합니다.
* 컨테이너가 계속해서 다시 시작되는 경우 컨테이너 로그에서 세부사항을 검토하십시오. `docker ps` 명령을 실행할 때 컨테이너가 몇 초 동안만 나열되거나 계속 다시 시작 중으로 나열되는 경우 컨테이너가 계속해서 다시 시작되고 있을 수 있습니다. 다음 명령을 실행하여 컨테이너 로그에서 세부사항을 볼 수 있습니다.
  ```
  grep --text -E ' <service-id>\[[0-9]+\]' /var/log/syslog
  ```
  {: codeblock}

## 예상되는 서비스 컨테이너 버전이 실행 중입니까?
{: #run_user_containers}

컨테이너 버전은 서비스를 배치 패턴에 추가하고 에지 노드를 해당 패턴에 등록한 후에 작성되는 계약을 통해 제어됩니다. 다음 명령을 실행하여 에지 노드에 패턴에 대한 현재 계약이 있는지 확인하십시오.

```
hzn agreement list | jq .
```
{: codeblock}

패턴에 대한 올바른 계약을 확인한 경우 다음 명령을 사용하여 실행 중인 컨테이너를 보십시오. 사용자 정의 컨테이너가 나열되고 실행 중인지 확인하십시오.
```
docker ps
```
{: codeblock}

{{site.data.keyword.horizon}} 에이전트에서 계약이 승인된 후 해당 컨테이너가 다운로드되고 확인되고 실행되기 시작할 때까지 몇 분이 걸릴 수 있습니다. 이 계약은 원격 저장소에서 가져와야 하는 컨테이너 자체의 크기에 주로 의존합니다.

## 예상 컨테이너가 안정적입니까?
{: #containers_stable}

다음 명령을 실행하여 컨테이너가 안정적인지 여부를 확인하십시오.
```
docker ps
```
{: codeblock}

명령 출력에서 각 컨테이너가 실행 중인 기간을 볼 수 있습니다. 시간이 경과함에 따라 컨테이너가 예기치 않게 다시 시작되고 있음을 발견하면 컨테이너 로그에서 오류를 확인하십시오.

개발 우수 사례로, 다음 명령을 실행하여 개별 서비스 로깅을 구성하는 방법을 고려하십시오({{site.data.keyword.linux_notm}} 시스템만 해당).
```bash
cat <<'EOF' > /etc/rsyslog.d/10-horizon-docker.conf $template DynamicWorkloadFile,"/var/log/workload/%syslogtag:R,ERE,1,DFLT:.*workload-([^\[]+)--end%.log"  :syslogtag, startswith, "workload-" -?DynamicWorkloadFile & stop :syslogtag, startswith, "docker/" -/var/log/docker_containers.log & stop :syslogtag, startswith, "docker" -/var/log/docker.log & stop EOF service rsyslog restart
```
{: codeblock}

이전 단계를 완료했으면 컨테이너에 대한 로그는 `/var/log/workload/` 디렉토리 내부의 별도 파일에 기록됩니다. 컨테이너의 전체 이름을 찾으려면 `docker ps` 명령을 사용하십시오. 이 디렉토리에서 `.log` 접미부가 있는 해당 이름의 로그 파일을 찾을 수 있습니다.

개별 서비스 로깅이 구성되지 않은 경우 서비스 로그가 다른 모든 로그 메시지와 함께 시스템 로그에 추가됩니다. 컨테이너에 대한 데이터를 검토하려면 `/var/log/syslog` 디렉토리 내의 시스템 로그 출력에서 컨테이너 이름을 검색해야 합니다. 예를 들어, 다음과 유사한 명령을 실행하여 로그를 검색할 수 있습니다.
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## 컨테이너가 Docker와 네트워크로 올바르게 연결되었습니까?
{: #container_networked}

필요한 서비스에 액세스할 수 있도록 컨테이너가 Docker와 네트워크로 올바르게 연결되었는지 확인하십시오. 다음 명령을 실행하여 에지 노드에서 활성화된 Docker 가상 네트워크를 볼 수 있는지 확인하십시오.
```
docker network list
```
{: codeblock}

네트워크에 대한 자세한 정보를 보려면 `docker inspect X` 명령을 사용합니다. 여기서, `X`는 네트워크의 이름입니다. 이 명령 출력에는 가상 네트워크에서 실행되는 모든 컨테이너가 나열됩니다.

각 컨테이너에서 `docker inspect Y` 명령을 실행하여 자세한 정보를 가져올 수도 있습니다. 여기서 `Y`는 컨테이너의 이름입니다. 예를 들어, `NetworkSettings` 컨테이너 정보를 검토하고 `Networks` 컨테이너를 검색하십시오. 이 컨테이너 내에서 관련 네트워크 ID 문자열과 컨테이너가 네트워크에 표시되는 방법에 대한 정보를 볼 수 있습니다. 이 표시 정보에는 컨테이너 `IPAddress` 및 이 네트워크에 있는 네트워크 별명의 목록이 포함됩니다. 

별명은 이 가상 네트워크의 모든 컨테이너에서 사용할 수 있으며 이러한 이름은 일반적으로 코드 배치 패턴의 컨테이너에서 가상 네트워크에 있는 다른 컨테이너를 발견하는 데 사용됩니다. 예를 들어, 서비스 이름을 `myservice`로 지정할 수 있습니다. 그러면 다른 컨테이너가 해당 이름을 사용하여 네트워크에서 직접 액세스할 수 있습니다(예: `ping myservice` 명령 사용). 컨테이너의 별명은 `hzn exchange service publish` 명령으로 전달한 서비스 정의 파일의 `deployment` 필드에 지정됩니다.

Docker 명령행 인터페이스에서 지원하는 명령에 대한 자세한 정보는 [Docker 명령 참조](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)를 참조하십시오.

## 컨테이너의 컨텍스트 내에서 종속성 컨테이너에 연결할 수 있습니까?
{: #setup_correct}

실행 중인 컨테이너의 컨텍스트를 입력하여 `docker exec` 명령을 사용해 런타임에 문제점을 해결하십시오. `docker ps` 명령을 사용하여 실행 중인 컨테이너의 ID의 찾은 후 다음과 유사한 명령을 사용하여 컨텍스트로 들어가십시오. `CONTAINERID`를 해당 컨테이너의 ID로 바꾸십시오.
```
docker exec -it CONTAINERID /bin/sh
```
{: codeblock}

컨테이너에 bash가 포함된 경우 앞의 명령 끝에 `/bin/sh` 대신, `/bin/bash`를 지정할 수 있습니다.

컨테이너 컨텍스트 내부인 경우 `ping` 또는 `curl`과 같은 명령을 사용하여 필요한 컨테이너와 상호작용하고 연결을 확인할 수 있습니다.

Docker 명령행 인터페이스에서 지원하는 명령에 대한 자세한 정보는 [Docker 명령 참조](https://docs.docker.com/engine/reference/commandline/docker/#child-commands)를 참조하십시오.

## 사용자 정의 컨테이너가 로그에 오류 메시지를 생성하고 있습니까?
{: #log_user_container_errors}

개별 서비스 로깅을 구성한 경우 각 컨테이너가 `/var/log/workload/` 디렉토리 내의 개별 파일에 로깅합니다. 컨테이너의 전체 이름을 찾으려면 `docker ps` 명령을 사용하십시오. 그런 다음, 이 디렉토리 내에서 `.log` 접미부를 포함하는 해당 이름의 파일을 찾으십시오.

개별 서비스 로깅이 구성되지 않은 경우 서비스가 다른 모든 세부사항이 포함된 시스템 로그에 로깅합니다. 데이터를 검토하려면 `/var/log/syslog` 디렉토리 내의 시스템 로그 출력에서 컨테이너 로그를 검색합니다. 예를 들어, 다음과 유사한 명령을 실행하여 로그를 검색하십시오.
```
grep --text -E 'YOURSERVICENAME\[[0-9]+\]' /var/log/syslog
```
{: codeblock}

## {{site.data.keyword.message_hub_notm}} Kafka 브로커의 조직 인스턴스를 사용할 수 있습니까?
{: #kafka_subscription}

{{site.data.keyword.message_hub_notm}}에서 조직에 대한 Kafka 인스턴스를 구독하면 Kafka 사용자가 인증 정보가 올바른지 확인하는 데 도움이 될 수 있습니다. 이 구독은 Kafka 서비스 인스턴스가 클라우드에서 실행 중인지와 데이터가 발행될 때 에지 노드가 데이터를 전송하는지 확인하는 데 도움이 될 수도 있습니다.

Kafka 브로커를 구독하려면 `kafkacat` 프로그램을 설치하십시오. 예를 들어, Ubuntu {{site.data.keyword.linux_notm}} 시스템에서 다음 명령을 사용하십시오.

```bash
sudo apt install kafkacat
```
{: codeblock}

설치 후, 일반적으로 환경 변수 참조에 배치하는 인증 정보를 사용하는 다음 예와 유사한 명령을 사용하여 구독할 수 있습니다.

```bash
kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t $EVTSTREAMS_TOPIC
```
{: codeblock}

여기서 `EVTSTREAMS_BROKER_URL`은 Kafka 브로커에 대한 URL이고 `EVTSTREAMS_TOPIC`은 Kafka 토픽이며 `EVTSTREAMS_API_KEY`는 {{site.data.keyword.message_hub_notm}} API에 인증하기 위한 API 키입니다.

구독 명령이 성공하면 이 명령이 무기한 차단됩니다. 그런 다음, 이 명령이 Kafka 브로커에 대한 발행을 대기하고 결과 메시지를 검색하여 표시합니다. 몇 분 후 에지 노드에서 메시지가 표시되지 않으면 서비스 로그에서 오류 메시지를 검토하십시오.

예를 들어, `cpu2evtstreams` 서비스에 대한 로그를 검토하려면 다음 명령을 실행하십시오.

* {{site.data.keyword.linux_notm}} 및 {{site.data.keyword.windows_notm}}의 경우 

```bash
tail -n 500 -f /var/log/syslog | grep -E 'cpu2evtstreams\[[0-9]+\]:'
```
{: codeblock}

* macOS의 경우

```bash
docker logs -f $(docker ps --filter 'name=-cpu2evtstreams' | tail -n +2 | awk '{print $1}')
```
{: codeblock}

## 컨테이너가 {{site.data.keyword.horizon_exchange}}에 공개됩니까?
{: #publish_containers}

{{site.data.keyword.horizon_exchange}}는 에지 노드를 위해 공개된 코드에 대한 메타데이터의 중앙 웨어하우스입니다. 코드에 서명하고 {{site.data.keyword.horizon_exchange}}에 공개하지 않은 경우 코드를 에지 노드로 가져와서 확인하고 실행할 수 없습니다.

모든 서비스 컨테이너가 성공적으로 공개되었는지 확인하기 위해 공개된 코드의 목록을 보려면 `hzn` 명령을 다음 인수와 함께 실행하십시오.

```
hzn exchange service list | jq .
hzn exchange service list $ORG_ID/$SERVICE | jq .
```
{: codeblock}

매개변수 `$ORG_ID`는 조직 ID이고, `$SERVICE`는 정보를 확보하려는 서비스 이름입니다.

## 공개된 배치 패턴에 모든 필수 서비스 및 버전이 포함되어 있습니까?
{: #services_included}

`hzn` 명령이 설치된 에지 노드에서 이 명령을 사용하여 배치 패턴에 대한 세부사항을 가져올 수 있습니다. {{site.data.keyword.horizon_exchange}}에서 배치 패턴 목록을 가져오려면 `hzn` 명령을 다음 인수와 함께 사용하십시오. 

```
hzn exchange pattern list | jq .
hzn exchange pattern list $ORG_ID/$PATTERN | jq .
```
{: codeblock}

매개변수 `$ORG_ID`는 조직 ID이고, `$PATTERN`은 정보를 확보하려는 배치 패턴 이름입니다.

## {{site.data.keyword.open_shift_cp}} 환경에 특정한 문제점 해결 팁
{: #troubleshooting_icp}

이 컨텐츠를 검토하여 {{site.data.keyword.edge_notm}} 관련 {{site.data.keyword.open_shift_cp}} 환경의 공통 문제를 해결하는 데 도움을 받으십시오. 해당 팁이 공통 문제를 해결하고 근본 원인을 식별하기 위한 정보를 얻는 데 도움이 될 수 있습니다.
{:shortdesc}

### {{site.data.keyword.edge_notm}} 인증 정보가 {{site.data.keyword.open_shift_cp}} 환경에서 사용하도록 올바르게 구성되었습니까?
{: #setup_correct}

이 환경에서 {{site.data.keyword.edge_notm}} 내 조치를 완료하려면 {{site.data.keyword.open_shift_cp}} 사용자 계정이 필요합니다. 해당 계정에서 작성된 API 키도 필요합니다.

이 환경에서 {{site.data.keyword.edge_notm}} 인증 정보를 확인하려면 다음 명령을 실행하십시오.

   ```
   hzn exchange user list
   ```
   {: codeblock}

Exchange에서 하나 이상의 사용자를 표시하는 JSON으로 형식화된 항목이 리턴되는 경우 {{site.data.keyword.edge_notm}} 인증 정보도 올바르게 구성된 것입니다.

오류 응답이 리턴되는 경우 인증 정보 설정 문제점을 해결하기 위한 단계를 수행할 수 있습니다.

오류 메시지에서 잘못된 API 키를 표시하는 경우 다음 명령을 사용하는 새 API 키를 작성할 수 있습니다.

[API 키 작성](../hub/prepare_for_edge_nodes.md)을 참조하십시오.

## 노드 오류 문제점 해결
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_notm}}에서는 {{site.data.keyword.gui}}에서 볼 수 있는 exchange에 이벤트 로그 서브세트를 공개합니다. 이 오류는 문제점 해결 안내에 링크됩니다.
{:shortdesc}

  - [이미지 로드 오류](#eil)
  - [배치 구성 오류](#eidc)
  - [컨테이너 시작 오류](#esc)
  - [OCP 에지 클러스터 TLS 내부 오류](#tls_internal)

### 이미지 로드 오류
{: #eil}

이 오류는 서비스 정의에서 참조하는 서비스 이미지가 이미지 저장소에 없는 경우 발생합니다. 이 오류를 해결하려면 다음을 수행하십시오.

1. **-I** 플래그 없이 서비스를 다시 공개하십시오.
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. 서비스 이미지를 이미지 저장소에 직접 푸시하십시오. 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
### 배치 구성 오류
{: #eidc}

이 오류는 서비스 정의 배치 구성이 루트로 보호된 파일에 대한 바인드를 지정하는 경우에 발생합니다. 이 오류를 해결하려면 다음을 수행하십시오.

1. 루트로 보호되지 않은 파일에 컨테이너를 바인드하십시오.
2. 사용자의 파일에 대한 읽기 및 쓰기를 허용하도록 파일 권한을 변경하십시오.

### 컨테이너 시작 오류
{: #esc}

이 오류는 서비스 컨테이너를 시작한 경우 Docker에서 오류가 발생하면 나타납니다. 오류 메시지는 컨테이너 시작이 실패한 이유를 나타내는 세부사항을 포함할 수 있습니다. 오류 해결 단계는 오류에 따라 다릅니다. 다음 오류가 발생할 수 있습니다.

1. 디바이스는 배치 구성에서 지정한 공개된 포트를 이미 사용하고 있습니다. 오류를 해결하려면 다음을 수행하십시오. 

    - 다른 포트를 서비스 컨테이너 포트에 맵핑하십시오. 표시되는 포트 번호가 서비스 포트 번호와 일치할 필요는 없습니다.
    - 동일한 포트를 사용하는 프로그램을 중지하십시오.

2. 배치 구성에서 지정한 공개된 포트가 유효한 포트 번호가 아닙니다. 포트 번호는 1 - 65535 범위의 숫자여야 합니다.
3. 배치 구성에서 볼륨 이름은 유효한 파일 경로가 아닙니다. 볼륨 경로는 절대 경로(상대 경로가 아님)로 지정해야 합니다. 

### OCP 에지 클러스터 TLS 내부 오류

  ```
  Error from server: error dialing backend: remote error: tls: internal error
  ```
  {: codeblock} 

클러스터 에이전트 설치 프로세스가 끝날 때 또는 에이전트 팟(Pod)과 상호작용하려고 시도하는 동안 이 오류가 표시되는 경우 OCP 클러스터의 인증서 서명 요청(CSR)에 문제가 있을 수 있습니다. 

1. 보류 상태의 CSR이 있는지 확인하십시오.

    ```
    oc get csr
    ```
    {: codeblock} 

2. 보류 중인 CSR을 승인하십시오.

  ```
  oc adm certificate approve <csr-name>
  ```
  {: codeblock}
    
**참고**: 하나의 명령으로 모든 CSR을 승인할 수 있습니다.

  ```
  for i in `oc get csr |grep Pending |awk '{print $1}'`; do oc adm certificate approve $i; done
  ```
  {: codeblock}

### 추가 정보

자세한 정보는 다음을 참조하십시오.
  * [문제점 해결](../troubleshoot/troubleshooting.md)
