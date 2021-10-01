# IBM&reg; Edge Application Manager

## 소개

IBM Edge Application Manager는 IoT 배치에서 일반적인 에지 디바이스에 배치된 애플리케이션을 위한 엔드-투-엔드 **애플리케이션 관리 플랫폼**을 제공합니다. 이 플랫폼은 현장 배치된 수 천개의 에지 디바이스에 에지 워크로드의 개정판을 안전하게 배치하는 태스크를 완전히 자동화하고 애플리케이션 개발자를 해당 태스크로부터 자유롭게 합니다. 애플리케이션 개발자는 대신 임의의 프로그래밍 언어로 된 애플리케이션 코드를 독립적으로 배치 가능한 Docker 컨테이너로서 작성하는 태스크에 집중할 수 있습니다. 이 플랫폼은 모든 디바이스에 전체 비즈니스 솔루션을 Docker 컨테이너의 다중 레벨 오케스트레이션으로서 안전하고 끊임없이 배치하는 부담을 가져갑니다.

https://www.ibm.com/cloud/edge-application-manager

## 선행 조건

[필수 소프트웨어](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq)는
다음을 참조하십시오.

## Red Hat OpenShift SecurityContextConstraints 요구사항

기본 `SecurityContextConstraints` 이름: [`restricted`](https://ibm.biz/cpkspec-scc)가 이 차트에 대해 검증되었습니다. 이 릴리스는 `kube-system` 네임스페이스로만 배치하도록 제한되며, 기본 차트의 서비스 계정과
기본 로컬 데이터베이스 서브차트의 추가 서비스 계정을 작성합니다.

## 차트 세부사항

이 helm 차트는 OpenShift 환경에 IBM Edge Application Manager 인증 컨테이너를 설치 및 구성합니다. 다음 컴포넌트가 설치됩니다.

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBots
* IBM Edge Application Manager - Cloud Sync Service(모델 관리 시스템의 일부)
* IBM Edge Application Manager - 사용자 인터페이스(관리 콘솔)

## 필수 리소스

[크기 조정](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html)은 다음을 참조하십시오.

## 스토리지 및 데이터베이스 요구사항

IBM Edge Application Manager 컴포넌트 데이터를 저장하기 위해 세 개의 데이터베이스 인스턴스가 필요합니다.

기본적으로 차트는 정의된 기본(또는 사용자가 구성한) kubernetes 동적 스토리지 클래스를 사용하여 아래의 볼륨 크기 조정을 갖는 세 개의 지속적 데이터베이스를 설치합니다. 볼륨 확장을 허용하지 않는
스토리지 클래스를 사용하는 경우 적절하게 확장할 수 있게 허용하십시오.

**참고:** 이런 기본 데이터베이스는 프로덕션용이 아닙니다. 사용자 자신의 관리 데이터베이스를 이용하려면 아래의 요구사항을 참조하고 **원격 데이터베이스 구성** 절의 단계를 수행하십시오.

* PostgreSQL: Exchange 및 AgBot 데이터 저장
  * 각각 최소한 20GB의 스토리지를 갖는 2개의 별도 인스턴스 필요
  * 인스턴스는 최소한 100 연결을 지원해야 함
  * 프로덕션을 위해서는 세 개의 인스턴스가 고가용성이어야 합니다.
* MongoDB: Cloud Sync Service 데이터 저장
  * 최소한 50GB의 스토리지를 갖는 1개의 인스턴스가 필요합니다. **참고:** 필요한 크기는 사용자가 저장하고 사용하는 에지 서비스 모델 및 파일의 크기와 수에 크게 의존합니다.
  * 프로덕션을 위해서는 이 인스턴스가 고가용성이어야 합니다.

**참고:** 고유 관리 데이터베이스 외에도 이 기본 데이터베이스의 백업 주기/프로시저는
사용자의 책임입니다.
기본 데이터베이스 프로시저에 대해서는 **백업 및 복구** 절을 참조하십시오.

## 리소스 모니터링

IBM Edge Application Manager가 설치되면 Kubernetes에서 실행 중인 제품 리소스의 기본 모니터링을 자동으로 설정합니다. 다음 위치에 있는 관리 콘솔의 Grafana 대시보드에서 모니터링 데이터를 볼 수 있습니다.

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

## 구성

#### 원격 데이터베이스 구성

1. 사용자 자신의 관리 데이터베이스를 사용하려면 `values.yaml`에서 다음 helm 구성 매개변수를 검색하고 그의 값을 `false`로 변경하십시오.

```yaml
localDBs:
  enabled: true
```

2. 이 템플리트 컨텐츠로 시작하는 파일(예를 들어, `dbinfo.yaml`이라는)을 작성하십시오.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. `dbinfo.yaml`을 편집하여 프로비저닝한 데이터베이스에 대한 액세스 정보를 제공하십시오. 모든 정보를 큰따옴표 사이에 채우십시오(인용된 값을 유지하십시오). 보안 인증을 추가할 때, 각 행을 4 공간 들여쓰기하여 yaml 파일의 적절한 읽기 보장하십시오. 2 이상의 데이터베이스가 동일한 인증을 사용하는 경우 인증은 `dbinfo.yaml`에서 반복될 필요가 **없습니다**. 파일을 저장한 후 실행하십시오.

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### 고급 구성

기본 helm 구성 매개변수 중 하나를 변경하기 위해 아래의 `grep` 명령을 사용하여 매개변수 및 해당 설명을 검토한 후 `values.yaml`에서 대응하는 값을 보기/편집하십시오.

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use any editor
```

## 차트 설치

**참고:**

* 이것은 CLI 전용 설치이며, GUI로부터의 설치는 지원되지 않습니다.

* [IBM Edge Application Manager 인프라 설치 - 설치 프로세스](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process)의 단계가 완료되었는지 확인하십시오.
* 클러스터당 설치된 IBM Edge Application Manager의 인스턴스가 하나만 존재할 수 있으며, `kube-system` 네임스페이스에만 설치될 수 있습니다.
* IBM Edge Application Manager 4.0에서 업그레이드는 지원되지 않습니다.

제공되는 설치 스크립트를 실행하여 IBM Edge Application Manager를 설치하십시오. 스크립트가 수행하는 주요 단계는 helm 차트 설치 및 설치 후 환경 구성(agbot, org 및 패턴/정책 서비스 작성)입니다.

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**참고:** 네트워크 속도에 따라 이미지를 다운로드하고 모든 차트 리소스를 배치하는 데 몇 분이 걸립니다.

### 차트 확인

* 위의 스크립트는 팟(Pod)이 실행 중이고 agbot과 exchange가 응답 중인지 확인합니다. 설치의 끝을 향해서 "RUNNING" 및 "PASSED" 메시지를 찾으십시오.
* "FAILED"인 경우 출력이 사용자에게 자세한 정보에 대해 특정 로그를 보도록 요청합니다.
* "PASSED"인 경우 출력은 실행된 테스트의 세부사항 및 관리 UI의 URL을 표시합니다.
  * 로그의 끝에서 제공되는 URL에 있는 IBM Edge Application Manager UI 콘솔로 이동하십시오.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## 사후 설치

[사후 설치 구성](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html)의 단계를 수행하십시오.

## 차트 설치 제거

[관리 허브 설치 제거](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html)의 단계를 따르십시오.

## 역할 기반 액세스

* `kube-system` 네임스페이스의 클러스터 관리자 권한이 이 제품을 설치 및 관리하기 위해 필요합니다.
* 릴리스 이름을 기반으로 이 차트와 서브차트의 서비스 계정, 역할 및 역할 바인딩이 작성됩니다.
* Exchange 인증 및 역할:
  * 모든 exchange 관리자 및 사용자의 인증은 `cloudctl` 명령으로 생성되는 API 키를 통해 IAM에 의해 제공됩니다.
  * exchange 관리자는 exchange 내에서 `admin` 권한이 제공되어야 합니다. 해당 권한으로 exchange 조직 내의 모든 사용자, 노드, 서비스, 패턴 및 정책을 관리할 수 있습니다.
  * Exchange 비관리자 사용자는 자신이 작성한 사용자, 노드, 서비스, 패턴 및 정책만 관리할 수 있습니다.

## 보안

* TLS가 유입을 통해 OpenShift 클러스터에 들어오고/나가는 모든 데이터에 사용됩니다. 이 릴리스에서 TLS는 노드간 통신을 위해 OpenShift 클러스터 **내에서** 사용되지 않습니다. 원하는 경우 마이크로서비스 사이의 통신을 위해 Red Hat OpenShift 서비스 메시를 구성하십시오. [Red Hat OpenShift 서비스 메시](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm)를 참조하십시오.
* 이 차트는 저장 데이터의 암호화를 제공하지 않습니다.  스토리지 저장 암호화를 구성하는 것은 관리자 책임입니다.

## 백업 및 복구

[백업 및 복구](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html)의 단계를 따르십시오.

## 제한사항

* 설치 한계: 이 제품은 한 번만, `kube-system` 네임스페이스에만 설치할 수 있습니다.

## 문서

* 추가 정보는 [설치](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) Knowledge Center 문서를 참조하십시오.

## 저작권

© Copyright IBM Corporation 2020. All Rights Reserved.
