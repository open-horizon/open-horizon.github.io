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


# 크기 조정 및 시스템 요구사항
{: #size}

## 크기 조정 고려사항

클러스터 크기를 조정할 때는 여러 가지 고려사항이 있습니다. 이 컨텐츠에서는 이러한 고려사항 중 일부를 제공하고 클러스터 크기를 조정하는 데 도움이 되는 최상의 안내서를 제공합니다.

기본 고려사항은 클러스터에서 실행되어야 하는 서비스입니다. 이 컨텐츠에서는 다음 서비스에 대한 크기 조정 지침만 제공합니다.

* {{site.data.keyword.common_services}}
* {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 관리 허브

선택적으로 [{{site.data.keyword.open_shift_cp}} 클러스터 로깅](../admin/accessing_logs.md#ocp_logging)을 설치할 수 있습니다.

## {{site.data.keyword.ieam}} 데이터베이스 고려사항

지원되는 두 가지 데이터베이스 구성이 {{site.data.keyword.ieam}} 관리 허브에 대한 크기 조정 고려사항에 영향을 미칩니다.

* **로컬** 데이터베이스는 기본적으로 {{site.data.keyword.open_shift}} 리소스로 {{site.data.keyword.open_shift}} 클러스터에 설치됩니다.
* **원격** 데이터베이스는 사용자가 프로비저닝한 데이터베이스이며 온프레미스, 클라우드 제공자 SaaS 오퍼링 등일 수 있습니다.

### {{site.data.keyword.ieam}} 로컬 스토리지 요구사항

항상 설치되어 있는 SDO(Secure Device Onboarding) 컴포넌트 외에도 **로컬** 데이터베이스 및 Secrets Manager에는 지속적 스토리지가 필요합니다. 이 스토리지는 {{site.data.keyword.open_shift}} 클러스터에 대해 구성된 동적 스토리지 클래스를 사용합니다.

자세한 정보는 [지원되는 동적 {{site.data.keyword.open_shift}} 스토리지 옵션 및 구성 지시사항](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html)을 참조하십시오.

클러스터 작성 시 암호화를 사용하도록 설정해야 합니다. 클라우드 플랫폼에서 클러스터 작성의 일부로 포함될 수 있습니다. 자세한 정보는 [다음 문서](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html)를 참조하십시오.

선택한 스토리지 클래스 유형에 대한 기본 고려사항은 스토리지 클래스에서 **allowVolumeExpansion**을 지원하는지 여부입니다. 지원하는 경우 다음이 **true**를 리턴합니다.

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

스토리지 클래스에서 볼륨 확장을 허용하면 설치 후 크기를 조정할 수 있습니다(기본 스토리지 공간을 할당할 수 있는 경우). 스토리지 클래스에서 볼륨 확장을 허용하지 않으면 유스 케이스에 대한 스토리지를 사전 할당해야 합니다. 

볼륨 확장을 허용하지 않는 스토리지 클래스를 사용한 초기 설치 이후 추가 스토리지가 필요한 경우 [백업 및 복구](../admin/backup_recovery.md) 페이지에서 설명하는 단계를 통해 재설치를 실행해야 합니다.

할당은 {{site.data.keyword.ieam}} 관리 허브 설치 이전에 [구성](configuration.md) 페이지에서 설명한 대로, **스토리지** 값을 수정하여 변경할 수 있습니다. 할당의 기본값은 다음과 같이 설정됩니다.

* PostgreSQL Exchange(Exchange용 데이터를 저장하며 사용량에 따라 크기가 변동되지만 기본 스토리지 설정에서 표시된 에지 노드 한계까지 지원할 수 있음)
  * 20GB
* PostgreSQL AgBot(AgBot용 데이터를 저장하며 기본 스토리지 설정에서 표시된 에지 노드 한계까지 지원할 수 있음)
  * 20GB
* MongoDB Cloud Sync Service(MMS(Model Management Service)용 컨텐츠를 저정함). 모델 수와 크기에 따라 이 기본 할당을 수정할 수 있습니다.
  * 50GB
* Hashicorp Vault 지속적 볼륨(에지 디바이스 서비스에서 사용되는 시크릿 저장)
  * 10GB(이 볼륨 크기는 구성할 수 없음)
* Secure Device Onboarding 지속적 볼륨(각 디바이스의 배치 상태, 디바이스 구성 옵션, 디바이스 소유권 바우처 저장)
  * 1GB(이 볼륨 크기는 구성할 수 없음)

* **참고:**
  * {{site.data.keyword.ieam}} 볼륨은 **ReadWriteOnce** 액세스 모드로 작성됩니다.
  * IBM Cloud Platform Common Services에는 해당 서비스에 대한 추가 스토리지 요구사항이 있습니다. 다음 볼륨은 {{site.data.keyword.ieam}} 기본값으로 설치할 때 **ibm-common-services** 네임스페이스에서 작성됩니다.
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE     alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h     prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    [여기](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html)에서 IBM Cloud Platform Common Services 스토리지 요구사항 및 구성에 대해 자세히 알아볼 수 있습니다.

### {{site.data.keyword.ieam}} 원격 데이터베이스 고려사항

동일한 클러스터에 프로비저닝되지 않는 경우에 한해, 고유 **원격** 데이터베이스를 이용하면 이 설치에 필요한 스토리지 클래스 및 컴퓨팅 요구사항이 감소됩니다.

최소한 다음 리소스 및 설정을 사용하여 **원격** 데이터베이스를 프로비저닝하십시오.

* 2vCPU
* 2GB RAM
* 이전 절에서 언급한 기본 스토리지 크기
* PostgreSQL 데이터베이스의 경우 100 **max_connections**(일반적으로 기본값)

## 작업 노드 크기 조정

[Kubernetes 컴퓨팅 리소스](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)를 사용하는 서비스는 사용 가능한 작업자 노드 전체에서 스케줄됩니다.

### 기본 {{site.data.keyword.ieam}} 구성에 대한 최소 요구사항
| 작업자 노드 수 | 작업자 노드당 vCPU 수 | 작업자 노드당 메모리(GB) | 작업자 노드당 로컬 디스크 스토리지(GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**참고:** 일부 고객 환경에는 작업자 노드 또는 추가 작업자 노드당 추가 vCPU가 필요할 수 있으므로 더 많은 CPU 용량을 Exchange 컴포넌트에 할당할 수 있습니다.


&nbsp;
&nbsp;

클러스터에 적합한 크기를 판별한 후 [설치](online_installation.md)를 시작할 수 있습니다.
