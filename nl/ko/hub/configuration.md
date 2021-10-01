---

copyright:
  years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.ieam}} 구성

## EamHub 사용자 정의 리소스 구성
{: #cr}

{{site.data.keyword.ieam}}에 대한 기본 구성은 EamHub 사용자 정의 리소스, 특히 해당 사용자 정의 리소스의 **spec** 필드를 통해 수행됩니다.

이 문서에서는 다음을 가정합니다.
* 이러한 명령을 실행하는 네임스페이스는 {{site.data.keyword.ieam}} 관리 허브 운영자가 배치된 위치에 있습니다.
* EamHub 사용자 정의 리소스 이름은 기본값 **ibm-edge**입니다. 다른 경우 명령을 변경하여 **ibm-edge**를 바꾸십시오.
* 2진 **jq**가 설치되어 출력이 읽을 수 있는 형식으로 표시되도록 보장합니다.


정의된 기본 **spec**은 최소이며, 라이센스 승인만 포함합니다. 다음을 통해 볼 수 있습니다.
```
$ oc get eamhub ibm-edge -o yaml ... spec:   license:     accept: true ...
```

### Operator Control 루프
{: #loop}

{{site.data.keyword.ieam}} 관리 허브 운영자는 예상되는 리소스 상태와 현재 리소스 상태를 동기화하기 위해 연속 멱등원 루프에서 실행됩니다.

이러한 연속 루프로 인해, 운영자가 관리하는 리소스를 구성하려는 경우 두 가지 사항을 이해해야 합니다.
* 사용자 정의 리소스에 대한 변경사항은 제어 루프를 통해 비동기적으로 읽어들입니다. 변경한 후에 운영자를 통해 해당 변경을 적용하는 데 몇 분 정도 걸릴 수 있습니다.
* 운영자가 제어하는 리소스에 대한 모든 수동 변경사항은 운영자가 특정 상태를 시행하여 겹쳐쓸 수 있습니다(실행 취소 가능). 

운영자 팟(Pod) 로그를 감시하여 이 루프를 관찰하십시오.
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

루프가 끝나면 **PLAY RECAP** 요약을 생성합니다. 최신 요약을 보려면 다음을 수행하십시오.
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

다음은 오퍼레이션 없이 완료된 루프가 수행 중임을 나타냅니다(현재 상태에서 **PLAY RECAP**은 항상 **changed=1**을 표시함).
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1 localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

구성을 변경하는 경우 다음과 같은 세 개의 필드를 검토하십시오.
* **changed**: **1**보다 큰 경우 운영자가 하나 이상의 리소스 상태를 변경하는 태스크를 수행했음을 나타냅니다(요청 시 사용자 정의 리소스를 대체하거나 운영자가 작성된 수동 변경사항을 되돌리는 경우에 이에 해당함).
* **rescued**: 태스크가 실패했지만 알려진 가능한 실패였으며 다음 루프에 해당 태스크를 다시 시도합니다.
* **failed**: 초기 설치 중에 예상되는 몇 가지 실패가 있습니다. 동일한 실패가 반복적으로 나타나고 메시지가 명백하지 않거나 숨겨진 경우 문제를 나타낼 수 있습니다.

### EamHub 공통 구성 옵션

여러 구성 변경사항을 수행할 수 있지만, 일부는 다른 구성보다 변경될 가능성이 더 큽니다. 이 절에서는 보다 일반적인 설정 중 몇 가지를 설명합니다.

| 구성 값 | 기본값 | 설명 |
| :---: | :---: | :---: |
| 글로벌 값 | -- | -- |
| pause_control_loop | false | 디버깅을 위해 임시 수동 변경사항을 사용할 수 있도록 위에서 언급된 제어 루프를 일시정지합니다. 안정 상태에 대해서는 사용되지 않습니다. |
| ieam_maintenance_mode | false | 지속적 스토리지 없이 모든 팟(Pod) 복제본 수를 0으로 설정합니다. 백업 복원 용도에 사용됩니다. |
| ieam_local_databases | true | 로컬 데이터베이스를 사용 또는 사용 안함으로 설정합니다. 상태 간 전환은 지원되지 않습니다. [원격 데이터베이스 구성](./configuration.md#remote)을 참조하십시오. |
| ieam_database_HA | true | 로컬 데이터베이스에 대해 HA 모드를 사용 또는 사용 안함으로 설정합니다. 이는 모든 데이터베이스 팟(Pod)의 복제본 수를 **3**(**true**일 때) 및 **1**(**false**일 때)로 설정합니다. |
| hide_sensitive_logs | true | **Kubernetes 시크릿** 설정을 처리하는 운영자 로그를 숨깁니다. **false**로 설정하면 태스크 실패 시 운영자가 인코딩된 인증 값을 로깅할 수 있습니다. |
| storage_class_name | "" | 설정되지 않은 경우 기본 스토리지 클래스를 사용합니다. |
| ieam_enable_tls | false | {{site.data.keyword.ieam}} 컴포넌트 간 트래픽에 대해 내부 TLS를 사용 또는 사용 안함으로 설정합니다. **주의:** Exchange, CSS 또는 볼트에 대한 기본 구성을 재정의하려면 구성 재정의에서 TLS 구성을 수동으로 수정해야 합니다. |
| ieam_local_secrets_manager | true | 로컬 Secrets Manager 컴포넌트(볼트)를 사용 또는 사용 안함으로 설정합니다. |


### EamHub 컴포넌트 스케일링 구성 옵션

| 컴포넌트 스케일링 값 | 기본 복제본 수 | 설명 |
| :---: | :---: | :---: |
| exchange_replicas | 3 | Exchange에 대한 기본 복제본 수입니다. 기본 Exchange 구성(exchange_config)을 재정의하는 경우, **maxPoolSize**는 다음 공식을 사용하여 수동으로 조정해야 합니다. `((exchangedb_max_connections - 8) / exchange_replicas)` |
| css_replicas | 3 | CSS에 대한 기본 복제본 수입니다. |
| ui_replicas | 3 | UI에 대한 기본 복제본 수입니다. |
| agbot_replicas | 2 | Agbot에 대한 기본 복제본 수입니다. 기본 Agbot 구성(agbot_config)을 재정의하는 경우, **MaxOpenConnections**는 다음 공식을 사용하여 수동으로 조정해야 합니다. `((agbotdb_max_connections - 8) / agbot_replicas)` |


### EamHub 컴포넌트 자원 구성 옵션

**참고**: Ansible 운영자에는 중첩된 사전이 전체적으로 추가되어야 하므로 전체적으로 중첩된 구성 값을 추가해야 합니다. 예제는 [스케일링 구성](./configuration.md#scale)을 참조하십시오.

<table>
<tr>
<td> 컴포넌트 자원 값 </td> <td> 기본값 </td> <td> 설명 </td>
</tr>
<tr>
<td> exchange_resources </td> 
<td>

```
  exchange_resources: requests: memory: 512Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Exchange에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> agbot_resources </td> 
<td>

```
  agbot_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Agbot에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> css_resources </td> 
<td>

```
  css_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
CSS에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> sdo_resources </td> 
<td>

```
  sdo_resources: requests: memory: 1024Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
SDO에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> ui_resources </td> 
<td>

```
  ui_resources: requests: memory: 64Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
UI에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> vault_resources </td> 
<td>

```
  vault_resources: requests: memory: 1024Mi cpu: 10m limits: memory: 2Gi cpu: 2
```

</td>
<td>
Secrets Manager에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> mongo_resources </td> 
<td>

```
  mongo_resources: limits: cpu: 2 memory: 2Gi requests: cpu: 100m memory: 256Mi
```

</td>
<td>
CSS mongo 데이터베이스에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_sentinel </td> 
<td>

```
  postgres_exchangedb_sentinel: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Exchange Postgres Sentinel에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_proxy </td> 
<td>

```
  postgres_exchangedb_proxy: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Exchange Postgres 프록시에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_exchangedb_keeper </td> 
<td>

```
  postgres_exchangedb_keeper: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 2 memory: 2Gi
```

</td>
<td>
Exchange Postgres 키퍼에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_sentinel </td> 
<td>

```
  postgres_agbotdb_sentinel: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Agbot Postgres Sentinel에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_proxy </td> 
<td>

```
  postgres_agbotdb_proxy: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 1 memory: 1Gi
```

</td>
<td>
Agbot Postgres 프록시에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
<tr>
<td> postgres_agbotdb_keeper </td> 
<td>

```
  postgres_agbotdb_keeper: resources: requests: cpu: "100m" memory: "256Mi" limits: cpu: 2 memory: 2Gi
```

</td>
<td>
Agbot Postgres 키퍼에 대한 기본 요청 및 한계입니다. 
</td>
</tr>
</table>

### EamHub 로컬 데이터베이스 크기 구성 옵션

| 컴포넌트 구성 값 | 기본 지속적 볼륨 크기 | 설명 |
| :---: | :---: | :---: |
| postgres_exchangedb_storage_size | 20Gi | Postgres Exchange 데이터베이스의 크기입니다. |
| postgres_agbotdb_storage_size | 20Gi | Postgres Agbot 데이터베이스의 크기입니다. |
| mongo_cssdb_storage_size | 20Gi | Mongo CSS 데이터베이스의 크기입니다. |

## Exchange API 번역 구성

특정 언어로 응답을 리턴하도록 {{site.data.keyword.ieam}} Exchange API를 구성할 수 있습니다. 이 작업을 수행하려면 지원되는 **LANG** 중에서 선택하여 환경 변수를 정의하십시오(기본값은 **en**).

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**참고:** 지원되는 언어 코드의 목록은 [지원되는 언어](../getting_started/languages.md) 페이지의 첫 번째 테이블을 참조하십시오.

## 원격 데이터베이스 구성
{: #remote}

**참고**: 원격 및 로컬 데이터베이스 사이에서 전환하는 작업은 지원되지 않습니다.

원격 데이터베이스로 설치하려면 **spec** 필드에서 추가 값을 사용한 설치 중에 EamHub 사용자 정의 리소스를 작성하십시오.
```
spec:   ieam_local_databases: false   license:     accept: true
```
{: codeblock}

인증 시크릿을 작성하려면 다음 템플리트를 완성하십시오. 각각의 주석을 읽고 정확하게 채워졌는지 확인한 후 **edge-auth-overrides.yaml**에 저장하십시오.
```
apiVersion: v1 kind: Secret metadata:   # NOTE: The name -must- be prepended by the name given to your Custom Resource, this defaults to 'ibm-edge'   #name: <CR_NAME>-auth-overrides   name: ibm-edge-auth-overrides type: Opaque stringData:   # agbot postgresql connection settings uncomment and replace with your settings to use   agbot-db-host: "<Single hostname of the remote database>"   agbot-db-port: "<Single port the database runs on>"   agbot-db-name: "<The name of the database to utilize on the postgresql instance>"   agbot-db-user: "<Username used to connect>"   agbot-db-pass: "<Password used to connect>"   agbot-db-ssl: "<disable|require|verify-full>"   # Ensure proper indentation (four spaces)   agbot-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings   exchange-db-host: "<Single hostname of the remote database>"   exchange-db-port: "<Single port the database runs on>"   exchange-db-name: "<The name of the database to utilize on the postgresql instance>"   exchange-db-user: "<Username used to connect>"   exchange-db-pass: "<Password used to connect>"   exchange-db-ssl: "<disable|require|verify-full>"   # Ensure proper indentation (four spaces)   exchange-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # css mongodb connection settings   css-db-host: "<Comma separated list including ports: hostname.domain:port,hostname2.domain:port2 >"   css-db-name: "<The name of the database to utilize on the mongodb instance>"   css-db-user: "<Username used to connect>"   css-db-pass: "<Password used to connect>"   css-db-auth: "<The name of the database used to store user credentials>"   css-db-ssl: "<true|false>"   # Ensure proper indentation (four spaces)   css-db-cert: |-     -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

시크릿을 작성하십시오.
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

[Operator Control 루프](./configuration.md#remote) 절에서 설명한 대로, 운영자 로그를 감시하십시오.


## 스케일링 구성
{: #scale}

EamHub 사용자 정의 자원 구성은 많은 수의 에지 노드를 지원하기 위해 {{site.data.keyword.ieam}} 관리 허브에서 자원을 늘리는 데 필요한 구성 매개변수를 표시합니다.
고객은 {{site.data.keyword.ieam}} 팟(Pod), 특히 Exchanges및 Agreement bots(Agbots)의 자원 소비량을 모니터하고 필요한 경우 자원을 추가해야 합니다. [{{site.data.keyword.ieam}} Grafana 대시보드 액세스](../admin/monitoring.md)를 참조하십시오. OpenShift 플랫폼은 이러한 업데이트를 인식하고 {{site.data.keyword.ocp}}에서 실행 중인 {{site.data.keyword.ieam}} 팟(Pod)을 자동으로 적용합니다.

제한사항

{{site.data.keyword.ieam}} 팟(Pod) 사이에 기본 자원 할당 및 내부 TLS를 사용하지 않는 경우, 배치된 서비스의 25%(또는 10,000)에 영향을 주는 배치 정책 업데이트로 배치된 40,000개의 서비스 인스턴스를 확보하는 최대 40,000개의 등록된 에지 노드를 테스트했습니다.

{{site.data.keyword.ieam}} 팟(Pod) 사이에 내부 TLS가 사용 가능한 경우 등록된 40,000개의 에지 노드를 지원하려면 Exchange 팟(Pod)에 추가 CPU 자원이 필요합니다. 
EamHub 사용자 정의 자원 구성에서 다음과 같이 변경

**spec** 아래 다음 섹션을 추가하십시오.

```
spec:   exchange_resources:     requests:       memory: 512Mi       cpu: 10m     limits:       memory: 2Gi       cpu: 5
```
{: codeblock}

90,000개 이상의 서비스 배치를 지원하려면 EamHub 사용자 정의 자원 구성에서 다음과 같이 변경하십시오.

**spec** 아래 다음 섹션을 추가하십시오.

```
spec: agbot_resources: requests: memory: 1Gi cpu: 10m limits: memory: 4Gi cpu: 2
```
{: codeblock}

