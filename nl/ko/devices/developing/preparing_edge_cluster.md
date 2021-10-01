---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 클러스터 준비
{: #preparing_edge_cluster}

## 시작하기 전에

에지 클러스터에 대해 작업을 시작하기 전에 다음을 고려하십시오.

* [선행 조건](#preparing_clusters)
* [에지 클러스터에 필요한 정보 및 파일 수집](#gather_info)

## 선행 조건
{: #preparing_clusters}

에지 클러스터에 에이전트를 설치하기 전에 다음을 수행하십시오.

1. 에이전트 설치 스크립트가 실행되는 환경에서 Kubectl을 설치하십시오.
2. 에이전트 설치 스크립트가 실행되는 환경에서 {{site.data.keyword.open_shift}} 클라이언트(oc) CLI를 설치하십시오.
3. 관련 클러스터 리소스를 작성하는 데 필요한 클러스터 관리 액세스를 얻으십시오.
4. 에지 클러스터 레지스트리가 에이전트 Docker 이미지를 호스트하도록 하십시오.
5. **cloudctl** 및 **kubectl** 명령과 추출된 **ibm-edge-computing-4.1-x86_64.tar.gz**를 설치하십시오. [설치 프로세스](../installing/install.md#process)를 참조하십시오.

## 에지 클러스터에 필요한 정보 및 파일 수집
{: #gather_info}

에지 클러스터를 설치하고 {{site.data.keyword.edge_notm}}에 등록하려면 여러 파일이 필요합니다. 이 절은 각 에지 클러스터에서 사용할 수 있는 tar 파일에 해당 파일 수집을 안내합니다.

1. **CLUSTER_URL** 환경 변수를 설정하십시오.

    ```
   export CLUSTER_URL=<cluster-url>
   export USER=<your-icp-admin-user>
   export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    다른 방법으로는, **oc login**으로 클러스터에 연결한 후 다음을 실행할 수 있습니다.

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. 클러스터 관리자 권한을 사용하여 클러스터에 연결한 후 **kube-system**을 네임스페이스로 선택하고 {{site.data.keyword.mgmt_hub}} [설치 프로세스](../installing/install.md#process) 중에 config.yaml에서 정의된 비밀번호를 채우십시오.

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. 환경 변수의 에지 클러스터 레지스트리에서 각 클러스터 레지스트리 사용자 이름, 비밀번호, 전체 이미지 이름을 설정하십시오. IMAGE_ON_EDGE_CLUSTER_REGISTRY의 값이 이 형식으로 지정됩니다.

    ```
    <registry-name>/<repo-name>/<image-name>.
    ```
    {: codeblock} 

    Docker 허브를 레지스트리로 사용하는 경우 이 형식으로 값을 지정하십시오.
    
    ```
    <docker-repo-name>/<image-name>
    ```
    {: codeblock}
    
    예를 들면, 다음과 같습니다.
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. **edgeDeviceFiles.sh**의 최신 버전을 다운로드하십시오.

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. **edgeDeviceFiles.sh** 스크립트를 실행하여 필요한 파일을 수집하십시오.

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   이는 agentInstallFiles-x86_64-Cluster..tar.gz라는 파일을 작성합니다. 
    
**명령 인수**
   
참고: x86_64-Cluster를 지정하여 에지 클러스터에서 에이전트를 설치하십시오.
   
|명령 인수|결과|
|-----------------|------|
|t                |수집된 모든 파일을 포함하는 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일을 작성하십시오. 이 플래그가 설정되지 않은 경우 수집된 파일은 현재 디렉토리에 위치합니다.|
|f                |수집된 파일을 이동할 디렉토리를 지정하십시오. 디렉토리가 없으면 작성됩니다. 현재 디렉토리는 기본값입니다.|
|r                |**EDGE_CLUSTER_REGISTRY_USER**, **EDGE_CLUSTER_REGISTRY_PW**, **IMAGE_ON_EDGE_CLUSTER_REGISTRY**는 이 플래그를 사용 중인 경우 환경 변수에서 설정해야 합니다(1단계). 4.1에서는 필수 플래그입니다.|
|o                |**HZN_ORG_ID**를 지정하십시오. 이 값은 에지 클러스터 등록에 사용됩니다.|
|n                |**NODE_ID**를 지정하십시오. 이는 에지 클러스터 이름의 값이어야 합니다. 이 값은 에지 클러스터 등록에 사용됩니다.|
|s                |지속적 볼륨 청구에서 사용할 클러스터 스토리지 클래스를 지정하십시오. 기본 스토리지 클래스는 "gp2"입니다.|
|i                |에지 클러스터에 배치되는 에이전트 이미지 버전입니다.|


에지 클러스터에 에이전트를 설치할 준비가 되면 [에이전트 설치 및 에지 클러스터 등록](importing_clusters.md)을 참조하십시오.

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## 다음 수행할 작업

* [에이전트 설치 및 에지 클러스터 등록](importing_clusters.md)

## 관련 정보

* [에지 클러스터](edge_clusters.md)
* [{{site.data.keyword.edge_notm}} 사용 시작하기](../getting_started/getting_started.md)
* [설치 프로세스](../installing/install.md#process)
