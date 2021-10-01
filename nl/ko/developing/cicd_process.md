---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 서비스에 대한 CI-CD 프로세스
{: #edge_native_practices}

발전하는 에지 서비스 세트는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 효율적인 사용에 필수적이고 강력한 CI/CD(Continuous Integration and Continuous Deployment) 프로세스는 중요한 컴포넌트입니다. 

이 컨텐츠를 사용하여 고유한 CI/CD 프로세스를 작성하는 데 사용할 수 있는 구성 요소를 레이아웃하십시오. 그런 다음, [`open-horizon/examples` 저장소](https://github.com/open-horizon/examples)에서 이 프로세스에 대해 자세히 알아보십시오.

## 구성 변수
{: #config_variables}

에지 서비스 개발자로 개발 시 서비스 컨테이너 크기를 고려하십시오. 해당 정보를 기반으로 서비스 기능을 별도의 컨테이너로 나누어야 할 수 있습니다. 이 상황에서 용도 테스트에 사용되는 구성 변수는 아직 개발되지 않은 컨테이너의 데이터를 시뮬레이션하도록 도울 수 있습니다. [cpu2evtstreams 서비스 정의 파일](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json)에서 **PUBLISH** 및 **MOCK**와 같은 입력 변수를 볼 수 있습니다. `service.sh` 코드를 검사하면 해당 작동을 제어하기 위해 해당 리터럴 문자열 및 기타 구성 변수를 사용함을 알 수 있습니다. **PUBLISH**는 코드가 IBM Event Streams에 메시지를 전송하려고 시도하는지 여부를 제어합니다. **MOCK**는 service.sh가 REST API 및 해당 종속 서비스(cpu 및 gps)에 접속하려고 시도하는지 여부 및 `service.sh`가 허위 데이터를 작성하는지 여부를 제어합니다.

서비스 배치 시 노드 정의 또는 `hzn register` 명령에서 지정하여 구성 변수 기본값을 대체할 수 있습니다.

## 교차 컴파일링
{: #cross_compiling}

Docker를 사용하여 단일 amd64 시스템에서 다중 아키텍처에 대해 컨테이너화된 서비스를 빌드할 수 있습니다. 마찬가지로 이동과 같은 교차 컴파일을 지원하는 컴파일된 프로그래밍 언어로 에지 서비스를 개발할 수 있습니다. 예를 들어, arm 디바이스(Raspberry Pi)에 대해 Mac(amd64 아키텍처 디바이스)에서 코드를 쓰는 경우 대상 arm에 GOARCH와 같은 매개변수를 지정하는 Docker 컨테이너를 빌드해야 할 수 있습니다. 이 설정으로 배치 오류를 예방할 수 있습니다. [open-horizon gps 서비스](https://github.com/open-horizon/examples/tree/master/edge/services/gps)를 참조하십시오.

## 테스트
{: #testing}

빈번하고 자동화된 테스트는 개발 프로세스의 중요한 부분입니다. 테스트를 용이하게 하려면 `hzn dev service start` 명령을 사용하여 시뮬레이션된 Horizon 에이전트 환경에서 서비스를 실행하십시오. 이 접근법은 또한 전체 Horizon 에이전트를 설치 및 등록하는 데 문제가 될 수 있는 devops 환경에서 유용합니다. 이 메소드는 **make test** 대상이 있는 `open-horizon examples` 저장소에서 서비스 테스트를 자동화합니다. [테스트 대상 작성](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30)을 참조하십시오.


**make test**를 실행하여 **hzn dev service start**를 사용하는 서비스를 실행하십시오. 실행 후에 [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh)는 서비스 로그를 모니터하여 서비스가 올바르게 실행 중임을 표시하는 데이터를 찾습니다.

## 배치 테스트
{: #testing_deployment}

새 서비스 버전을 개발할 때 전체의 실질적인 테스트에 액세스하는 것이 좋습니다. 이를 수행하기 위해 에지 노드에 서비스를 배치할 수 있습니다. 그러나 테스트이기 때문에 모든 에지 노드에 서비스를 처음에 배치하지 않으려고 할 수 있습니다.

이를 수행하려면 새 서비스 버전만 참조하는 배치 정책 또는 패턴을 작성하십시오. 그런 다음 이 새 정책 또는 패턴에 테스트 노드를 등록하십시오. 정책을 사용하는 경우 에지 노드에서 특성을 설정하는 옵션이 있습니다. 예를 들어, "이름": "모드", "값": "테스트"이며 배치 정책에 해당 제한조건을 추가하십시오("모드 == 테스트"). 그러면 테스트를 위한 노드만 새 서비스 버전을 수신하도록 할 수 있습니다.

**참고**: 관리 콘솔에서 배치 정책 또는 패턴을 작성할 수도 있습니다. [관리 콘솔 사용](../console/accessing_ui.md)을 참조하십시오.

## 프로덕션 배치
{: #production_deployment}

테스트에서 프로덕션 환경으로 서비스의 새 버전을 이동한 후에 테스트 중에 발생하지 않았던 문제가 발생할 수 있습니다. 배치 정책 또는 패턴 롤백 설정은 해당 문제를 다루는 데 유용합니다. 패턴 또는 배치 정책 `serviceVersions` 섹션에서 서비스의 다중, 이전 버전을 지정할 수 있습니다. 새 버전에 오류가 있는 경우 롤백을 위해 에지 노드의 우선순위를 각 버전에 지정하십시오. 각 롤백 버전에 우선순위 지정 외에도 지정된 서비스의 낮은 우선순위 버전으로 폴백하기 전에 재시도 지속 기간 및 재시도 수와 같은 사항을 지정할 수 있습니다.특정 구문은 [이 배치 정책 예제](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json)를 참조하십시오.

## 에지 노드 보기
{: #viewing_edge_nodes}

노드에 새 서비스 버전을 배치한 후에 에지 노드의 상태를 쉽게 모니터할 수 있어야 합니다. 이 태스크에 대해 {{site.data.keyword.ieam}} {{site.data.keyword.gui}}을 사용하십시오. 예를 들어, [배치 테스트](#testing_deployment) 또는 [프로덕션 배치](#production_deployment) 프로세스에 있는 경우 배치 정책을 사용하는 노드 또는 오류가 있는 노드를 빠르게 검색할 수 있습니다.

## 서비스 마이그레이션
{: #migrating_services}

일부 시점에 {{site.data.keyword.ieam}}의 한 인스턴스에서 다른 인스턴스로 서비스, 패턴 또는 정책을 이동해야 할 수 있습니다. 마찬가지로 한 exchange 조직에서 다른 조직으로 서비스를 이동해야 할 수 있습니다. 이는 다른 호스트 환경에 {{site.data.keyword.ieam}}의 새 인스턴스를 설치한 경우 발생할 수 있습니다. 또는 두 {{site.data.keyword.ieam}} 인스턴스(개발용 및 프로덕션용)가 있는 경우 서비스를 이동해야 할 수 있습니다. 이 프로세스를 용이하게 하기 위해 open-horizon 예제 저장소에서 [`loadResources` 스크립트)](https://github.com/open-horizon/examples/blob/master/tools/loadResources)를 사용할 수 있습니다.

## Travis로 자동화된 풀 요청 테스트
{: #testing_with_travis}

[Travis CI](https://travis-ci.com)를 사용하여 GitHub 저장소에 풀 요청(PR)이 열릴 때마다 테스트를 자동화할 수 있습니다. 

open-horizon 예제 GitHub 저장소에서 Travis 및 기술을 활용하는 방법을 알아보려면 이 컨텐츠를 계속 읽으십시오.

예제 저장소에서 Travis CI는 샘플을 빌드하고 테스트하고 공개하는 데 사용됩니다. [`.travis.yml` 파일](https://github.com/open-horizon/examples/blob/master/.travis.yml)에서 가상 환경이 hzn, Docker, [qemu](https://github.com/multiarch/qemu-user-static)가 있는 Linux amd64 시스템으로 실행하도록 설정되어 다중 아키텍처에 빌드됩니다.

이 시나리오에서 cpu2evtstreams가 BM Event Streams에 데이터를 전송하도록 하기 위해 kafkacat이 설치됩니다. 명령행 사용과 마찬가지로 Travis는 샘플 에지 서비스와 함께 사용하도록 `EVTSTREAMS_TOPIC` 및 `HZN_DEVICE_ID`와 같은 환경 변수를 사용할 수 있습니다. HZN_EXCHANGE_URL은 수정된 서비스 공개를 위해 스테이징 exchange를 가리키도록 설정됩니다.

그런 다음 [travis-find](https://github.com/open-horizon/examples/blob/master/tools/travis-find) 스크립트는 열린 풀 요청에 의해 수정된 서비스를 식별하는 데 사용됩니다.

샘플이 수정된 경우 해당 서비스의 **makefile**에서 `test-all-arches` 대상이 실행됩니다. 지원되는 아키텍처의 qemu 컨테이너가 실행 중이면 크로스 아키텍처 빌드는 빌드 및 테스트 전에 `ARCH` 환경 변수를 즉시 설정하여 이 **makefile** 대상과 함께 실행됩니다. 

`hzn dev service start` 명령은 에지 서비스를 실행하고 [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) 파일은 서비스 로그를 모니터하여 서비스가 올바르게 작동 중인지 여부를 판별합니다.

전용 `test-all-arches` Makefile 대상을 보려면 [helloworld Makefile](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24)을 참조하십시오.

다음 시나리오는 더 철저한 엔드-투-엔드 테스트를 보여줍니다. 수정된 샘플 중 하나가 `cpu2evtstreams`를 포함하는 경우 IBM Event Streams의 인스턴스는 백그라운드에서 모니터될 수 있으며 HZN_DEVICE_ID에 대해 확인될 수 있습니다. 이는 **travis-test** 노드 ID를 cpu2evtstreams 토픽의 데이터 읽기에서 발견한 경우에만 테스트를 통과하고 모든 통과된 서비스 목록에 추가될 수 있습니다. 여기에는 시크릿 환경 변수로 설정된 IBM Event Streams API 키 및 브로커 URL이 필요합니다.

PR이 병합된 후에 이 프로세스가 반복되고 전달 서비스 목록이 exchange에 공개할 수 있는 서비스 식별에 사용됩니다. 이 예제에서 사용되는 Travis 시크릿 환경 변수에는 서비스를 푸시하고 서명하고 exchange에 공개하는 데 필요한 모든 사항이 포함되어 있습니다. 여기에는 `hzn key create` 명령으로 얻을 수 있는 Docker 인증 정보, HZN_EXCHANGE_USER_AUTH, 암호화 서명 키 쌍이 포함됩니다. 보안 환경 변수로 서명 키를 저장하려면 base64로 인코딩되어야 합니다.

Functional Test를 전달한 서비스 목록은 전용 공개 `Makefile` 대상으로 공개해야 하는 서비스를 식별하는 데 사용됩니다. [helloworld 샘플](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45)을 참조하십시오.

서비스가 빌드되고 테스트되었으므로 이 대상은 모든 아키텍처의 서비스, 서비스 정책, 패턴, 배치 정책을 exchange에 공개합니다.

**참고**: 관리 콘솔에서 이러한 여러 가지 태스크를 수행할 수도 있습니다. [관리 콘솔 사용](../console/accessing_ui.md)을 참조하십시오.

