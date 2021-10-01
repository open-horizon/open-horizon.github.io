---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 노드 파일 수집
{: #prereq_horizon}

에지 디바이스와 에지 클러스터에 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 에이전트를 설치하는 데 여러 파일이 필요하며, {{site.data.keyword.ieam}}에 등록해야 합니다. 이 컨텐츠는 에지 노드에 필요한 파일 번들 과정을 안내합니다. {{site.data.keyword.ieam}} 관리 허브에 연결된 관리 호스트에서 이 단계를 수행하십시오.

다음 단계에서는 [IBM Cloud Pak CLI(**cloudctl**) 및 OpenShift 클라이언트 CLI(**oc**)](../cli/cloudctl_oc_cli.md) 명령을 설치했으며 압축 해제된 설치 매체 디렉토리 **ibm-eam-{{site.data.keyword.semver}}-bundle**내에서 단계를 실행하고 있다고 가정합니다. 이 스크립트는 필요한 {{site.data.keyword.horizon}} 패키지를 **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** 파일에서 검색하여 필요한 에지 노드 구성 및 인증 파일을 작성합니다.

1. 관리 신임 정보 및 {{site.data.keyword.ieam}}에 설치한 네임스페이스를 사용하여 관리 허브 클러스터에 로그인하십시오.
   ```bash
   cloudctl login -a &amp;TWBLT;cluster-url&gt; -u &amp;TWBLT;cluster-admin-user&gt; -p &amp;TWBLT;cluster-admin-password&gt; -n &amp;TWBLT;namespace&gt; --skip-ssl-validation
   ```
   {: codeblock}

2. 다음 환경 변수를 설정하십시오.

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}') oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode &gt; ieam.crt export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt" export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   사용자의 **ENTITLEMENT_KEY**를 제공하여 다음 Docker 인증 환경 변수를 정의하십시오.
   ```
   export REGISTRY_USERNAME=cp    export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **참고:** [내 IBM 키](https://myibm.ibm.com/products-services/containerlibrary)를 통해 인타이틀먼트 키를 확보하십시오.

3. **edge-packages-{{site.data.keyword.semver}}.tar.gz**가 있는 **agent** 디렉토리로 이동하십시오.

   ```bash
   cd agent
   ```
   {: codeblock}

4. **edgeNodeFiles.sh** 스크립트를 사용하여 에지 노드 설치용 파일을 수집하는 두 가지 선호 방식이 있습니다. 자체 요구사항에 따라 다음 방법 중 하나를 선택하십시오.

   * **edgeNodeFiles.sh** 스크립트를 실행하여 필요한 파일을 수집하고 모델 관리 시스템(MMS)의 CSS(Cloud Sync Service) 컴포넌트에 넣으십시오.

     **참고**: **edgeNodeFiles.sh script**는 horizon-cli 패키지의 일부로 설치되었으며 사용자의 경로에 있어야 합니다.

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     각 에지 노드에서 **agent-install.sh**의 **-i 'css:'** 플래그를 사용하여 CSS에서 필요한 파일을 가져오십시오.

     **참고**: [SDO 사용 에지 디바이스](../installing/sdo.md)를 사용하려는 경우 이 양식의 `edgeNodeFiles.sh` 명령을 실행해야 합니다.

   * 또는 **edgeNodeFiles.sh**를 사용하여 tar 파일로 파일을 번들하십시오.

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     각 에지 노드에 tar 파일을 복사하고 **agent-install.sh**의 **-z** 플래그를 사용하여 tar 파일에서 필요한 파일을 가져오십시오.

     이 호스트에 아직 **horizon-cli** 패키지를 설치하지 않은 경우 지금 이 작업을 수행하십시오. 이 프로세스 예제에 대해서는 [설치 후 구성](post_install.md#postconfig)을 참조하십시오.

     **horizon-cli** 패키지의 일부로 설치된 **agent-install.sh** 및 **agent-uninstall.sh** 스크립트를 찾으십시오.    이러한 스크립트는 설정 중 각 에지 노드에 필요합니다(현재 **agent-uninstall.sh**는 에지 클러스터만 지원함).
    * {{site.data.keyword.linux_notm}} 예제:

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * macOS 예:

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**참고**: **edgeNodeFiles.sh**에는 수집되는 파일 및 해당 파일이 배치되는 위치를 제어하기 위한 추가 플래그가 존재합니다. 사용 가능한 플래그를 모두 보려면 **edgeNodeFiles.sh -h**를 실행하십시오.

## 다음 수행할 작업

에지 노드가 설정되기 전에 사용자 또는 노드 기술자가 API 키를 작성하고 다른 환경 변수 값을 수집해야 합니다. [API 키 작성](prepare_for_edge_nodes.md)의 단계를 수행하십시오.
