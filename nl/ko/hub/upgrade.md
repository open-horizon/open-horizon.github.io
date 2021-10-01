---

copyright:
years: 2021
lastupdated: "2021-03-23"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 업그레이드
{: #hub_upgrade_overview}

## 업그레이드 요약
{: #sum}
* {{site.data.keyword.ieam}} 관리 허브의 현재 버전은 {{site.data.keyword.semver}}입니다.
* {{site.data.keyword.ieam}} {{site.data.keyword.semver}}은 {{site.data.keyword.ocp}} 버전 4.6에서 지원됩니다.

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 관리 허브 및 [IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs)에 대한 동일한 OLM(Operator Lifecycle Manager) 채널로 업그레이드하면 {{site.data.keyword.open_shift_cp}}({{site.data.keyword.ocp}}) 클러스터에 사전 설치되어 있는 OLM을 통해 자동으로 업그레이드됩니다.

{{site.data.keyword.ieam}} 채널은 **부 버전**(예: v4.2 및 v4.3)에 의해 정의되며 자동으로 **패치 버전**(예: 4.2.x)만 업데이트합니다. **부 버전** 업그레이드의 경우, 업그레이드를 시작하도록 채널을 수동으로 변경해야 합니다. **부 버전** 업그레이드를 시작하려면 이전 **부 버전**에서 사용 가능한 최신 **패치 버전**에 있어야 하며, 전환 채널이 업그레이드를 시작합니다.

**참고:**
* 다운그레이드가 지원되지 않음
* {{site.data.keyword.ieam}} 4.1.x에서 4.2.x로 업그레이드가 지원되지 않음
* [알려진 {{site.data.keyword.ocp}} 문제](https://access.redhat.com/solutions/5493011)로 인해 수동 승인을 위해 구성된 프로젝트에 `InstallPlans`가 있는 경우 해당 프로젝트의 다른 모든 `InstallPlans`도 마찬가지입니다. 계속하려면 운영자의 업그레이드를 수동으로 승인해야 합니다.

### 4.2.x에서 4.3.x로 {{site.data.keyword.ieam}} 관리 허브 업그레이드

1. 업그레이드하기 전에 백업을 수행하십시오. 자세한 정보는 [백업 및 복구](../admin/backup_recovery.md)를 참조하십시오.
2. 클러스터의 {{site.data.keyword.ocp}} 웹 콘솔로 이동하십시오.
3. **운영자** &gt; **설치된 운영자**로 이동하십시오.
4. **{{site.data.keyword.ieam}}**을(를) 검색하고 **{{site.data.keyword.ieam}} 관리 허브** 결과를 클릭하십시오.
5. **등록** 탭으로 이동하십시오.
6. **채널** 섹션에서 **v4.2** 링크를 클릭하십시오.
7. 단일 선택 단추를 클릭하여 활성 채널을 **v4.3**으로 전환하여 업그레이드를 시작하십시오.

업그레이드가 완료되었는지 확인하려면 [설치 검증 설치 후 작업 섹션의 1-5단계](post_install.md)를 참조하십시오.

예제 서비스를 업데이트하려면 [설치 후 작업 구성 섹션의 1-3단계](post_install.md)를 참조하십시오.

## 에지 노드 업그레이드

기존 {{site.data.keyword.ieam}} 노드는 자동으로 업그레이드되지 않습니다. {{site.data.keyword.ieam}} 4.2.1 에이전트 버전(2.28.0-338)은 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 관리 허브에서 지원됩니다. 에지 디바이스 및 에지 클러스터에서 {{site.data.keyword.edge_notm}} 에이전트를 업그레이드하려면 먼저 {{site.data.keyword.semver}} 에지 노드 파일을 CSS( Cloud Sync Service)에 배치해야 합니다.

현재 에지 노드를 업그레이드하지 않으려는 경우에도 **사용자 환경에 최신 CLI 설치**의 1-3단계를 수행하십시오. 이렇게 하면 최신 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 에이전트 코드로 새 에지 노드가 설치됩니다.

### 환경에 최신 CLI 설치
1. [권한이 있는 레지스트리](https://myibm.ibm.com/products-services/containerlibrary)를 통해 인타이틀먼트 키를 사용하여 에이전트 번들을 로그인, 가져오기 및 추출하십시오.
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \ docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \ docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \ docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz
    ```
    {: codeblock}
2. 지원되는 플랫폼에 대한 지침을 사용하여 **hzn** CLI를 설치하십시오.
  * **agent** 에이전트로 이동하고 에이전트 파일을 압축 해제하십시오.
    ```
    cd ibm-eam-{{site.data.keyword.semver}}-bundle/agent &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf edge-packages-{{site.data.keyword.semver}}.tar.gz
    ```
    {: codeblock}

    * Debian {{site.data.keyword.linux_notm}} 예제:
      ```
      sudo apt-get install ./edge-packages-{{site.data.keyword.semver}}/linux/deb/amd64/horizon-cli*.deb
      ```
      {: codeblock}

    * Red Hat {{site.data.keyword.linux_notm}} 예제:
      ```
      sudo dnf install -yq ./edge-packages-{{site.data.keyword.semver}}/linux/rpm/x86_64/horizon-cli-*.x86_64.rpm
      ```
      {: codeblock}

    * macOS 예:
      ```
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli.crt && \       sudo installer -pkg edge-packages-{{site.data.keyword.semver}}/macos/pkg/x86_64/horizon-cli-*.pkg -target /
      ```
      {: codeblock}
3. [에지 노드 파일 수집](../hub/gather_files.md)의 단계를 따라 에이전트 설치 파일을 CSS에 푸시하십시오.

### 에지 노드에서 에이전트 업그레이드
1. 디바이스에서 **루트**로 또는 클러스터에서 **admin**으로 에지 노드에 로그인하고 horizon 환경 변수를 설정하십시오.
```bash
export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
```
{: codeblock}

2. 클러스터 유형에 따라 필요한 환경 변수를 설정하십시오(디바이스를 업그레이드하는 경우 이 단계를 건너뜀).

  * **OCP 에지 클러스터:**
  
    에이전트에서 사용할 스토리지 클래스를 설정하십시오.
    
    ```bash
    oc get storageclass    export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
    ```
    {: codeblock}

    레지스트리 사용자 이름을 사용자가 작성한 서비스 계정 이름으로 설정하십시오.
    ```bash     oc get serviceaccount -n openhorizon-agent     export EDGE_CLUSTER_REGISTRY_USERNAME=<service-account-name>
    ```
    {: codeblock}

    레지스트리 토큰을 설정하십시오. 
    ```bash     export EDGE_CLUSTER_REGISTRY_TOKEN=`oc serviceaccounts get-token $EDGE_CLUSTER_REGISTRY_USERNAME`
    ```
    {: codeblock}

  * **k3s:**
  
    기본 스토리지 클래스를 사용하도록 **agent-install.sh**에 지시하십시오.
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=local-path
    ```
    {: codeblock}

  * **microk8s:**
  
    기본 스토리지 클래스를 사용하도록 **agent-install.sh**에 지시하십시오.
    
    ```bash
    export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
    ```
    {: codeblock}

3. CSS에서 **agent-install.sh**를 가져오십시오.
```bash
curl -u $HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data -o agent-install.sh --insecure && chmod +x agent-install.sh
```
{: codeblock}

4. **agent-install.sh**를 실행하여 CSS에서 업데이트된 파일을 가져온 후 Horizon 에이전트를 구성하십시오.
  *  **에지 디바이스:**
    ```bash     sudo -s -E ./agent-install.sh -i 'css:' -s
    ```
    {: codeblock}

  *  **에지 클러스터:**
    ```bash     ./agent-install.sh -D cluster -i 'css:' -s
    ```
    {: codeblock}

**참고**: 에지 노드가 업그레이드 이전과 동일한 상태로 유지되도록 하려면 에이전트 설치를 실행하는 중에 -s 옵션을 포함시켜 등록을 건너뛰십시오.

## 알려진 문제점 및 FAQ
{: #FAQ}

### {{site.data.keyword.ieam}} 4.2
* {{site.data.keyword.ieam}} 4.2.0 로컬 cssdb mongo 데이터베이스에 알려진 문제점이 있습니다. 이는 팟(Pod)이 다시 스케줄될 때 데이터가 손실됩니다. 로컬 데이터베이스(기본값)를 사용하는 경우 {{site.data.keyword.ocp}} 클러스터를 4.6으로 업데이트하기 전에 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 업그레이드를 완료하십시오. 자세한 정보는 [알려진 문제](../getting_started/known_issues.md) 페이지를 참조하십시오.

* 버전 4.4 이후 {{site.data.keyword.ocp}} 클러스터를 업그레이드하지 않았는데 자동 업그레이드가 중단된 것처럼 보입니다.

  * 이 문제를 해결하려면 다음 단계를 수행하십시오.
  
    1) 현재 {{site.data.keyword.ieam}} 관리 허브 컨텐츠의 백업을 작성하십시오.  백업 문서는 [데이터 백업 및 복구](../admin/backup_recovery.md)에 있습니다.
    
    2) {{site.data.keyword.ocp}} 클러스터를 버전 4.6으로 업그레이드하십시오.
    
    3) {{site.data.keyword.ieam}} 4.2.0 로컬 **cssdb** mongo 데이터베이스의 알려진 문제로 인해 **2단계**의 업그레이드 시 데이터베이스가 다시 초기화됩니다.
    
      * {{site.data.keyword.ieam}}의 MMS 기능을 활용했으며 데이터 손실이 신경쓰이는 경우 **1단계**에서 작성한 백업을 사용하여 [데이터 백업 및 복구](../admin/backup_recovery.md) 페이지의 **복원 프로시저**를 수행하십시오. (**참고:** 복원 프로시저를 수행하는 경우 가동 중단 시간이 발생합니다.)
      
      * MMS 기능을 활용하지 않았거나, MMS 데이터 손실을 신경쓰지 않거나, 원격 데이터베이스를 사용하는 경우 다음 작업을 수행하여 {{site.data.keyword.ieam}} 운영자를 설치 제거한 후 다시 설치하십시오.
      
        1) {{site.data.keyword.ocp}} 클러스터의 설치된 운영자 페이지로 이동하십시오.
        
        2) IEAM 관리 허브 운영자를 찾아서 해당 페이지를 여십시오.
        
        3) 왼쪽에 있는 조치 메뉴에서 운영자를 설치 제거하도록 선택하십시오.
        
        4) 운영자 허브 페이지로 이동하여 IEAM 관리 허브 운영자를 다시 설치하십시오.

* {{site.data.keyword.ocp}} 버전 4.5가 지원됩니까?

  * {{site.data.keyword.ocp}} 버전 4.5에서는 {{site.data.keyword.ieam}} 관리 허브가 테스트되지 않았으며 지원되지 않습니다.  {{site.data.keyword.ocp}} 버전 4.6으로 업그레이드할 것을 권장합니다.

* 이 버전의 {{site.data.keyword.ieam}} 관리 허브를 사용하지 않을 방법이 있습니까?

  * 버전 {{site.data.keyword.semver}}의 릴리스에서는 {{site.data.keyword.ieam}} 관리 허브 버전 4.2.0이 더 이상 지원되지 않습니다.
