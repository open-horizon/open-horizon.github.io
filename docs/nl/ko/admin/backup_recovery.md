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

# 데이터 백업 및 복구
{: #data_backup}

## {{site.data.keyword.open_shift_cp}} 백업 및 복구

클러스터 전체 데이터 백업 및 복구에 대한 자세한 정보는 다음 항목을 참조하십시오.

* [{{site.data.keyword.open_shift_cp}} 4.6 백업 etcd](https://docs.openshift.com/container-platform/4.6/backup_and_restore/backing-up-etcd.html).

## {{site.data.keyword.edge_notm}} 백업 및 복구

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 백업 프로시저는 사용하는 데이터베이스 유형에 따라 조금 다릅니다. 이러한 데이터베이스는 로컬 또는 원격이라고 합니다.

|데이터베이스 유형|설명|
|-------------|-----------|
|로컬|이러한 데이터베이스는 기본적으로 {{site.data.keyword.open_shift}} 리소스로 {{site.data.keyword.open_shift}} 클러스터에 설치됨|
|원격|이러한 데이터베이스는 클러스터 외부에서 프로비저닝됩니다. 예를 들어, 이러한 데이터베이스는 온프레미스 또는 클라우드 제공자 SaaS 오퍼링일 수 있습니다.|

사용되는 데이터베이스를 제어하는 구성 설정은 설치 중에 사용자 정의 리소스에 **spec.ieam\_local\_databases**로 설정되며, 기본적으로 true입니다.

설치된 {{site.data.keyword.ieam}} 인스턴스의 활성 값을 판별하려면 다음을 실행하십시오.

```
oc get eamhub ibm-edge -o jsonpath="{.spec.ieam_local_databases}"
```
{: codeblock}

설치 시 원격 데이터베이스를 구성하는 방법에 대한 자세한 정보는 [구성](../hub/configuration.md) 페이지를 참조하십시오.

**참고**: 로컬 및 원격 데이터베이스 사이에서 전환하는 작업은 지원되지 않습니다.

{{site.data.keyword.edge_notm}} 제품은 데이터를 자동으로 백업하지 않습니다. 사용자가 선택한 주기로 컨텐츠를 백업한 다음, 복구 가능하도록 개별 보안 위치에 해당 백업을 저장해야 합니다. 시크릿 백업은 데이터베이스 연결과 {{site.data.keyword.mgmt_hub}} 애플리케이션 인증 둘 다에 맞게 인코딩된 인증 컨텐츠를 포함하고 있으므로, 안전한 위치에 저장하십시오.

고유한 원격 데이터베이스를 사용하는 경우 해당 데이터베이스가 백업되었는지 확인하십시오. 이 문서에서는 해당 원격 데이터베이스의 데이터 백업 방법을 설명하지 않습니다.

{{site.data.keyword.ieam}} 백업 프로시저에는 `yq` v3도 필요합니다.

### 백업 프로시저

1. 클러스터 관리자로 **cloudctl login** 또는 **oc login**을 사용하여 클러스터에 연결하십시오. Passport Advantage에서 {{site.data.keyword.mgmt_hub}} 설치에 사용되는 압축 해제된 매체에 있는 다음 스크립트를 사용하여 데이터와 시크릿을 백업하십시오. 사용법을 보려면 **-h**와 함께 스크립트를 실행하십시오.

   ```
   ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh -h
   ```
   {: codeblock}
   
   **참고**: 백업 스크립트는 설치 중에 사용된 데이터베이스 유형을 자동으로 발견합니다.

   * 다음 예를 옵션 없이 실행하면 스크립트가 실행되는 폴더가 생성됩니다. 이 폴더는 이름 패턴 **ibm-edge-backup/$DATE/**를 따릅니다.

     ```
     ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-backup.sh
     ```
     {: codeblock}
     
     **로컬 데이터베이스** 설치가 발견된 경우 백업에 **customresource** 디렉토리, **databaseresources** 디렉토리 및 두 개의 yaml 파일이 포함됩니다.

     ```
     $ ls -l ibm-edge-backup/20201026_215107/   	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:51 customresource 	  drwxr-xr-x  5 staff  staff    160 Oct 26 21:51 databaseresources 	  -rw-r--r--  1 staff  staff  13308 Oct 26 21:51 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   3689 Oct 26 21:51 ibm-edge-config.yaml
     ```
     {: codeblock}
     
	  **원격 데이터베이스** 설치가 감지된 경우에는 이전에 나열된 것과 동일한 디렉토리를 볼 수 있으나 yaml 파일이 두 개가 아니라 세 개입니다.
	  
	  ```
     $ ls -l ibm-edge-backup/20201026_215518/ 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 customresource 	  drwxr-xr-x  3 staff  staff     96 Oct 26 21:55 databaseresources 	  -rw-r--r--  1 staff  staff  10477 Oct 26 21:55 ibm-edge-auth-overrides.yaml 	  -rw-r--r--  1 staff  staff  11433 Oct 26 21:55 ibm-edge-auth-secret.yaml 	  -rw-r--r--  1 staff  staff   2499 Oct 26 21:55 ibm-edge-config.yaml
     ```
     {: codeblock}

### 복원 프로시저

**참고**: 로컬 데이터베이스가 사용되거나 신규 또는 비어 있는 원격 데이터베이스로 복원되는 경우 {{site.data.keyword.ieam}}의 자율 설계로 인해 {{site.data.keyword.mgmt_hub}}로 백업을 복원할 때 알려진 문제가 발생합니다.

백업을 복원하려면 동일한 {{site.data.keyword.mgmt_hub}}를 설치해야 합니다. 초기 설치 중에 **ieam\_maintenance\_mode**를 입력하지 않은 상태로 이 새 허브가 설치된 경우에는 이전에 등록된 모든 에지 노드가 자체적으로 등록 취소될 가능성이 높습니다. 이 경우에는 이들을 다시 등록해야 합니다.

이 상황은 데이터베이스가 지금 비어 있어 에지 노드가 더 이상 자신이 Exchange에 존재하지 않는다고 인식하는 경우 발생합니다. **ieam\_maintenance\_mode**를 사용하여 {{site.data.keyword.mgmt_hub}}에 대해서만 데이터베이스 리소스를 시작해 이를 방지하십시오. 이는 나머지 {{site.data.keyword.mgmt_hub}} 리소스(해당 데이터베이스를 사용하는)가 시작되기 전에 복원을 완료할 수 있게 해 줍니다.

**참고**: 

* **사용자 정의 리소스** 파일이 백업된 경우, 이는 클러스터에 다시 적용될 때 바로 **ieam\_maintenance\_mode**로 설정되도록 자동으로 수정되어 있습니다.

* 복원 스크립트는 **\<path/to/backup\>/customresource/eamhub-cr.yaml** 파일을 검사하여 이전에 사용된 데이터베이스 유형을 자동으로 판별합니다.

1. 클러스터 관리자는 **cloudctl login** 또는 **oc login**으로 클러스터에 연결되었는지, 그리고 올바른 백업이 작성되었는지 확인해야 합니다. 백업이 작성된 클러스터에서, 다음 명령을 실행하여 **eamhub** 사용자 정의 리소스를 삭제하십시오(이는 **ibm-edge**의 기본 이름이 사용자 정의 리소스에 사용되었다고 가정함).
	```
	oc delete eamhub ibm-edge
	```
	{: codeblock}

2. **ieam\_maintenance\_mode**가 올바르게 설정되었는지 확인하십시오.
	```
	yq r ibm-edge-backup/20201026_215738/customresource/eamhub-cr.yaml 'items[0].spec.ieam_maintenance_mode'
	```
	{: codeblock}
	

3. **-f** 옵션을 정의하여 `ieam-restore-k8s-resources.sh` 스크립트를 실행해 백업을 가리키십시오.
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-k8s-resources.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}

   계속하기 전에 모든 데이터베이스 및 SDO 팟(Pod)이 실행될 때까지 기다리십시오.
	
4. 연산자를 일시정지하도록 **ibm-edge** 사용자 정의 리소스를 편집하십시오.
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": true}}'
	```
	{: codeblock}

5. **1**로 복제본 수를 확장하도록 **ibm-edge-sdo** stateful 세트를 편집하십시오.
	```
	oc patch statefulset ibm-edge-sdo --type merge --patch '{"spec":{"replicas": 1}}'
	```
	{: codeblock}

6. **ibm-edge-sdo-0** 팟(Pod)이 실행 중 상태가 될 때까지 기다리십시오.
	```
   	watch oc get pods -n ibm-edge | grep ibm-edge-sdo-0
   	```
	{: codeblock}

7. 백업을 지시하도록 정의된 **-f** 옵션을 사용하여 `ieam-restore-data.sh` 스크립트를 실행하십시오.
	```
	ibm-eam-{{site.data.keyword.semver}}-bundle/tools/ieam-restore-data.sh -f ibm-edge-backup/20201026_215738/
	```
	{: codeblock}
	
8. 스크립트가 완료되고 데이터가 복원되면 운영자의 일시정지를 제거하여 제어 루프를 재개하십시오.
	```
	oc patch eamhub ibm-edge --type merge --patch '{"spec":{"pause_control_loop": false}}'
	```
	{: codeblock}

