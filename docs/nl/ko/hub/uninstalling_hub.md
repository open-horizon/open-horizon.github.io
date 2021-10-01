---

copyright:
years: 2020
lastupdated: "2020-10-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# 설치 제거
{: #uninstalling_hub}

**경고:** **EamHub** 사용자 정의 리소스를 삭제하면 IBM Cloud Platform Common Services 컴포넌트를 포함하여 {{site.data.keyword.ieam}} 관리 허브가 의존하는 리소스가 즉시 제거됩니다. 진행하기 전에 사용자 의도에 부합하는지 확인하십시오.

이전 상태로 쉽게 복원하도록 이 설치 제거를 수행하는 경우 [백업 및 복구](../admin/backup_recovery.md) 페이지를 참조하십시오.

* {{site.data.keyword.ieam}} 운영자가 설치된 네임스페이스에 대해 **cloudctl** 또는 **oc login**을 사용하여 클러스터 관리자로 클러스터에 로그인하십시오.
* 다음을 실행하여 사용자 정의 리소스를 삭제하십시오(기본 **ibm-edge**).
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* 다음 단계로 진행하기 전에 모든 {{site.data.keyword.ieam}} 관리 허브 팟(Pod)이 종료되었고 여기에 표시된 두 개의 운영자 팟(Pod)만 실행 중인지 확인하십시오.
  ```
  $ oc get pods   NAME                                           READY   STATUS    RESTARTS   AGE   ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h   ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* OpenShift 클러스터 콘솔을 사용하여 {{site.data.keyword.ieam}} 관리 허브 운영자를 설치 제거하십시오. {{site.data.keyword.ieam}} 운영자가 설치된 네임스페이스를 선택하고 **운영자** > **설치된 운영자** > **IEAM 관리 허브**의 오버플로우 메뉴 아이콘 > **운영자 설치 제거**로 이동하십시오.
* IBM Cloud Platform Common Services [설치 제거](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services) 페이지의 **모든 서비스 설치 제거** 지시사항에 따라 **common-service** 네임스페이스를 {{site.data.keyword.ieam}} 운영자가 설치된 네임스페이스로 바꾸십시오.
