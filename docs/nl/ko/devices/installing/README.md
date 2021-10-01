# IBM Edge Computing Manager

## 소개

IBM Edge Computing Manager for Devices는 IoT 배치에서 일반적인 에지 디바이스에 배치된 애플리케이션을 위한 엔드-투-엔드 **애플리케이션 플랫폼 플랫폼**을 제공합니다. 이 플랫폼은 현장 배치된 수 천개의 에지 디바이스에 에지 워크로드의 개정판을 안전하게 배치하는 태스크를 완전히 자동화하고 애플리케이션 개발자를 해당 태스크로부터 자유롭게 합니다. 애플리케이션 개발자는 대신 임의의 프로그래밍 언어로 된 애플리케이션 코드를 독립적으로 배치 가능한 Docker 컨테이너로서 작성하는 태스크에 집중할 수 있습니다. 이 플랫폼은 모든 디바이스에 전체 비즈니스 솔루션을 Docker 컨테이너의 다중 레벨 오케스트레이션으로서 안전하고 끊임없이 배치하는 부담을 가져갑니다.

## 선행 조건

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management core 1.2
* 사용자 고유의 데이터베이스를 호스팅하는 경우, IBM Edge Computing Manager for Devices 컴포넌트를 위한 데이터를 저장하기 위해 PostgreSQL의 두 인스턴스와 MongoDB의 한 인스턴스를 프로비저닝하십시오. 자세한 내용은 아래의 **스토리지** 절을 참조하십시오.
* 설치를 구동할 Ubuntu Linux 또는 macOS 호스트. 다음 소프트웨어가 설치되어 있어야 합니다.
  * [Kubernetes CLI(kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) 버전 1.14.0 이상
  * [IBM Cloud Pak CLI(cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [OpenShift CLI(oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [Helm CLI](https://helm.sh/docs/using_helm/#installing-the-helm-client) 버전 2.9.1 이상
  * 기타 소프트웨어 패키지:
    * jq
    * git
    * docker(버전 18.06.01 이상)
    * make

## Red Hat OpenShift SecurityContextConstraints 요구사항

기본 `SecurityContextConstraints` 이름: [`restricted`](https://ibm.biz/cpkspec-scc)가 이 차트에 대해 검증되었습니다. 이 릴리스는 `kube-system` 네임스페이스로의 배치로 제한되며 선택적인 로컬 데이터베이스 서브차트에 대한 고유한 서비스 계정 작성에 추가하여 두 개의 `default` 서비스 계정을 모두 사용합니다.

## 차트 세부사항

이 helm 차트는 OpenShift 환경에 IBM Edge Computing Manager for Devices 인증 컨테이너를 설치 및 구성합니다. 다음 컴포넌트가 설치됩니다.

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Cloud Sync Service(모델 관리 시스템의 일부)
* IBM Edge Computing Manager for Devices - 사용자 인터페이스(관리 콘솔)

## 필수 리소스

필요한 리소스에 대한 정보는 [설치 - 크기 조정](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)을 참조하십시오.

## 스토리지 및 데이터베이스 요구사항

IBM Edge Computing Manager for Devices 컴포넌트 데이터를 저장하기 위해 세 개의 데이터베이스 인스턴스가 필요합니다.

기본적으로 차트는 정의된 기본(또는 사용자가 구성한) kubernetes 동적 스토리지 클래스를 사용하여 아래의 볼륨 크기 조정을 갖는 세 개의 지속적 데이터베이스를 설치합니다.

**참고:** 이런 기본 데이터베이스는 프로덕션용이 아닙니다. 사용자 자신의 관리 데이터베이스를 이용하려면 아래의 요구사항을 참조하고 **원격 데이터베이스 구성** 절의 단계를 수행하십시오.

* PostgreSQL: Exchange 및 AgBot 데이터 저장
  * 각각 최소한 10GB의 스토리지를 갖는 2개의 별도 인스턴스 필요
  * 인스턴스는 최소한 100 연결을 지원해야 함
  * 프로덕션을 위해서는 세 개의 인스턴스가 고가용성이어야 합니다.
* MongoDB: Cloud Sync Service 데이터 저장
  * 최소한 50GB의 스토리지를 갖는 1개의 인스턴스가 필요합니다. **참고:** 필요한 크기는 사용자가 저장하고 사용하는 에지 서비스 모델 및 파일의 크기와 수에 크게 의존합니다.
  * 프로덕션을 위해서는 이 인스턴스가 고가용성이어야 합니다.

**참고:** 사용자가 자신의 관리 데이터베이스를 사용하는 경우 백업/복원 프로시저를 책임집니다.
기본 데이터베이스 프로시저에 대해서는 **백업 및 복구** 절을 참조하십시오.

## 리소스 모니터링

IBM Edge Computing Manager for Devices는 설치될 때 제품의 모니터링 및 그것이 실행하는 팟(Pod)을 자동으로 설정합니다. 다음 위치에 있는 관리 콘솔의 Grafana 대시보드에서 모니터링 데이터를 볼 수 있습니다.

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

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
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
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

기본 helm 구성 매개변수 중 하나를 변경하기 위해 아래의 `grep` 명령을 사용하여 매개변수 및 해당 설명을 검토한 후 `values.yaml`에서 대응하는 값을 보기/편집할 수 있습니다.

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use your preferred editor
```

## 차트 설치

**참고:**

* 이것은 CLI 전용 설치이며, GUI로부터의 설치는 지원되지 않습니다.

* [IBM Edge Computing Manager for Devices 인프라 설치 - 설치 프로세스](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)의 단계를 이미 완료했어야 합니다.
* 클러스터당 설치된 IBM Edge Computing Manager for Devices의 인스턴스가 하나만 존재할 수 있으며, `kube-system` 네임스페이스에만 설치될 수 있습니다.
* IBM Edge Computing Manager for Devices 3.2로부터의 업그레이드는 지원되지 않습니다.

제공되는 설치 스크립트를 실행하여 IBM Edge Computing Manager for Devices를 설치하십시오. 스크립트가 수행하는 주요 단계는 helm 차트 설치 및 설치 후 환경 구성(agbot, org 및 패턴/정책 서비스 작성)입니다.

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**참고:** 네트워크 속도에 따라서는 이미지를 다운로드하고 팟(Pod)이 RUNNING 상태로 전이하고 모든 서비스가 활성이 되는 데 몇 분이 걸립니다.

### 차트 확인

* 위의 스크립트는 팟(Pod)이 실행 중이고 agbot과 exchange가 응답 중인지 확인합니다. 설치의 끝을 향해서 "RUNNING" 및 "PASSED" 메시지를 찾으십시오.
* "FAILED"인 경우 출력이 사용자에게 자세한 정보에 대해 특정 로그를 보도록 요청합니다.
* "PASSED"인 경우 출력은 실행된 테스트의 세부사항 및 확인할 두 개의 추가 항목을 표시합니다.
  * 로그의 끝에서 제공되는 URL에 있는 IBM Edge Computing Manager UI 콘솔로 이동하십시오.
    * `https://<MANAGEMENT_URL:PORT>/edge`

## 사후 설치

[사후 설치 구성](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig)의 단계를 수행하십시오.

## 차트 설치 제거

**참고:** 로컬 데이터베이스가 구성된 채로 설치 제거하려는 경우 **모든 데이터가 삭제됩니다**. 설치 제거 전에 이 데이터를 유지하려는 경우 아래의 **백업 프로시저** 절을 참조하십시오.

이 README.md의 위치로 돌아가서 제공되는 설치 제거 스크립트를 실행하여 설치 제거 태스크를 자동화하십시오. 스크립트가 담당하는 주요 단계는 Helm 차트 설치 제거, 본인확인정보의 제거입니다. 먼저, `cloudctl`을 사용하여 클러스터 관리자로서 클러스터에 로그인하십시오. 그런 다음,

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```

**참고:** 원격 데이터베이스를 프로비저닝한 경우 인증 본인확인정보가 삭제되지만 해당 원격 데이터베이스에서 데이터를 해체/삭제하기 위해 실행하는 태스크는 없습니다. 해당 데이터를 삭제하려는 경우 지금 삭제하십시오.

## 역할 기반 액세스

* `kube-system` 네임스페이스의 클러스터 관리자 권한이 이 제품을 설치 및 관리하기 위해 필요합니다.
* Exchange 인증 및 역할:
  * 모든 exchange 관리자 및 사용자의 인증은 `cloudctl` 명령으로 생성되는 API 키를 통해 IAM에 의해 제공됩니다.
  * exchange 관리자는 exchange 내에서 `admin` 권한이 제공되어야 합니다. 해당 권한으로 exchange 조직 내의 모든 사용자, 노드, 서비스, 패턴 및 정책을 관리할 수 있습니다.
  * Exchange 비관리자 사용자는 자신이 작성한 사용자, 노드, 서비스, 패턴 및 정책만 관리할 수 있습니다.

## 보안

* TLS가 유입을 통해 OpenShift 클러스터에 들어오고/나가는 모든 데이터에 사용됩니다. 이 릴리스에서 TLS는 노드간 통신을 위해 OpenShift 클러스터 **내에서** 사용되지 않습니다. 원하는 경우 마이크로서비스 사이의 통신을 위해 Red Hat OpenShift 서비스 메시를 구성할 수 있습니다. [Red Hat OpenShift 서비스 메시](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm)를 참조하십시오.
* 이 차트는 저장 데이터의 암호화를 제공하지 않습니다.  스토리지 암호화를 구성하는 것은 관리자 책임입니다.

## 백업 및 복구

### 백업 프로시저

클러스터를 이들 백업을 저장하기에 충분한 공간이 있는 위치의 클러스터에 연결한 후 이들 명령을 실행하십시오.


1. 아래의 백업을 저장하는 데 사용되는 디렉토리를 작성하고 원하는 대로 조정하십시오.

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. 백업 인증/본인확인정보를 백업하려면 다음을 실행하십시오.

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. 다음을 실행하여 데이터베이스 컨텐츠를 백업하십시오.

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. 백업이 확인된 후, Stateless 컨테이너에서 백업을 제거하십시오.

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### 복원 프로시저

**참고:** 새 클러스터에 복원하는 경우 해당 '클러스터 이름'이 백업을 가져온 클러스터의 이름과 일치해야 합니다.

1. 클러스터에서 이미 존재하는 모든 본인확인정보를 삭제하십시오.
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. 이들 값을 로컬 머신으로 내보내십시오.

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. 다음을 실행하여 인증/본인확인정보를 복원하십시오.

```bash
oc apply -f $BACKUP_DIR
```

4. 추가로 진행하기 전에 IBM Edge Computing Manager를 다시 설치하고, **차트 설치** 절의 지시사항을 따르십시오.

5. 다음을 실행하여 백업을 컨테이너에 복사하고 복원하십시오.

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. 다음을 실행하여 kubernetes pod 데이터베이스 연결을 새로 고치십시오.
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## 제한사항

* 설치 한계: 이 제품은 한 번만, `kube-system` 네임스페이스에만 설치할 수 있습니다.
* 이 릴리스에는 제품의 관리 및 제품 운영을 위한 독특한 권한 부여 권한이 없습니다.

## 문서

* 추가 지침 및 업데이트에 대해서는 [설치](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) Knowledge Center 문서를 참조하십시오.

## 저작권

© Copyright IBM Corporation 2020. All Rights Reserved.
