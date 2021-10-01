---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 관리 허브 설치
{: #hub_install_overview}
 
{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 노드 태스크로 이동하기 전에 관리 허브를 설치 및 구성해야 합니다.

{{site.data.keyword.ieam}}은 허브 클러스터의 워크로드를 관리하고 OpenShift® Container Platform 4.2 또는 기타 Kubernetes 기반 클러스터의 원격 인스턴스에 배치하는 데 도움이 되는 에지 컴퓨팅 기능을 제공합니다.

{{site.data.keyword.ieam}}은 IBM Multicloud Management Core 1.2를 사용하여 원격 위치에 있는 OpenShift® Container Platform 4.2 클러스터에서 호스팅되는 에지 서버, 게이트웨이, 디바이스에 컨테이너화된 워크로드의 배치를 제어합니다.

또한 {{site.data.keyword.ieam}}은 에지 컴퓨팅 관리자 프로파일에 대한 지원을 포함합니다. 원격 에지 서버를 호스팅하는 데 사용하기 위해 OpenShift® Container Platform 4.2가 설치된 경우 이 지원되는 프로파일이 OpenShift® Container Platform 4.2의 리소스 사용량을 줄이는 데 도움이 될 수 있습니다. 이 프로파일은 이러한 서버 환경 및 여기서 호스팅하는 엔터프라이즈 크리티컬 애플리케이션의 강력한 원격 관리를 지원하는 데 필요한 최소 서비스를 배치합니다. 여전히 이 프로파일을 사용하여 단일 노드 또는 클러스터된 작업자 노드에서 사용자를 인증하고 로그 및 이벤트 데이터를 수집하며 워크로드를 배치할 수 있습니다.

# 관리 허브 설치

{{site.data.keyword.edge_notm}} 설치 프로세스는 다음과 같은 상위 레벨 설치 및 구성 단계를 안내합니다.
{:shortdesc}

  - [설치 요약](#sum)
  - [크기 조정](#size)
  - [선행 조건](#prereq)
  - [설치 프로세스](#process)
  - [설치 후 구성](#postconfig)
  - [필수 정보 및 파일 수집](#prereq_horizon)
  - [설치 제거](#uninstall)

## 설치 요약
{: #sum}

* 다음 관리 허브 컴포넌트를 배치하십시오.
  * {{site.data.keyword.edge_devices_notm}} exchange API.
  * {{site.data.keyword.edge_devices_notm}} agbot.
  * {{site.data.keyword.edge_devices_notm}} CSS(Cloud Sync Service).
  * {{site.data.keyword.edge_devices_notm}} 사용자 인터페이스.
* 설치에 성공했는지 확인하십시오.
* 샘플 에지 서비스를 채우십시오.

## 크기 조정
{: #size}

이 크기 조정 정보는 {{site.data.keyword.edge_notm}} 서비스만을 위한 것이며, [여기에 문서화됨](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/cluster_sizing.html)을 찾을 수 있는 {{site.data.keyword.edge_shared_notm}}에 대한 크기 조정 권장사항의 그 이상입니다.

### 데이터베이스 스토리지 요구사항

* PostgreSQL Exchange
  * 기본 10GB
* PostgreSQL AgBot
  * 기본 10GB  
* MongoDB Cloud Sync Service
  * 기본 50GB

### 컴퓨팅 요구사항

서비스 레버리징 [Kubernetes 컴퓨팅 리소스](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)가 사용 가능한 작업자 노드 사이에서 스케줄됩니다. 최소한 세 개의 작업자 노드가 권장됩니다.

* 이런 구성 변경사항은 최대 10,000개의 에지 디바이스를 지원합니다.

  ```
  exchange:
    replicaCount: 5
    dbPool: 18
    cache:
      idsMaxSize: 11000
    resources:
      limits:
        cpu: 5
  ```

  참고: 해당 변경사항 작성에 대한 지시는 [README.md](README.md)의 **고급 구성** 섹션에 설명되어 있습니다.

* 기본 구성은 최대 4,000개의 에지 디바이스를 지원하며 기본 컴퓨팅 리소스에 대한 차트 총계는 다음과 같습니다.

  * 요청
     * 5GB 미만의 RAM
     * 1개 미만의 CPU
  * 한계
     * 18GB의 RAM
     * 18 CPU


## 선행 조건
{: #prereq}

* [{{site.data.keyword.edge_shared_notm}}](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) 설치
* **macOS 또는 Ubuntu {{site.data.keyword.linux_notm}} 호스트**
* [OpenShift 클라이언트 CLI(oc) 4.2 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.2/)
* **jq** [다운로드 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://stedolan.github.io/jq/download/)
* **git**
* **docker** 1.13+
* **make**
* {{site.data.keyword.mgmt_hub}} 클러스터 설치(`https://<CLUSTER_URL_HOST>/common-nav/cli`)에서 구할 수 있는 다음 CLI

    참고: 비인증 액세스가 시작 페이지로 재지정될 수 있으므로 위의 URL을 두 번 탐색해야 할 수 있습니다.

  * Kubernetes CLI(**kubectl**)
  * Helm CLI(**helm**)
  * IBM Cloud Pak CLI(**cloudctl**)

참고: 기본적으로, 로컬 개발 데이터베이스는 차트 설치의 일부로 프로비저닝됩니다. 사용자 고유 데이터베이스 프로비저닝에 대한 지침은 [README.md](README.md)를 참조하십시오. 사용자가 자신의 데이터베이스를 백업 또는 복원할 책임을 갖습니다.

## 설치 프로세스
{: #process}

1. **CLUSTER_URL** 환경 변수를 설정하십시오. 이 값은 {{site.data.keyword.mgmt_hub}} 설치의 결과물에서 얻을 수 있습니다.

    ```
    export CLUSTER_URL=<CLUSTER_URL>
    ```
    {: codeblock}

    다른 방법으로는, **oc login**으로 클러스터에 연결한 후 다음을 실행할 수 있습니다.

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)
    ```
    {: codeblock}

2. **kube-system**을 네임스페이스로 선택하여 클러스터 관리자 권한으로 클러스터에 연결하고 {{site.data.keyword.mgmt_hub}} 설치 중에 config.yaml에서 정의한 **비밀번호를 채우십시오**.

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}

3. 이미지 레지스트리 호스트를 정의하고, 자체 서명 인증서를 신뢰하도록 Docker CLI를 구성하십시오.

    ```
    export REGISTRY_HOST=$(oc get routes -n openshift-image-registry default-route -o jsonpath='{.spec.host}')

    ```
    {: codeblock}

   macOS의 경우:

      1. 인증서 신뢰

      ```
      mkdir -p ~/.docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > ~/.docker/certs.d/$REGISTRY_HOST/ca.crt && \
      sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ~/.docker/certs.d/$REGISTRY_HOST/ca.crt

      ```
      {: codeblock}
      
      2. 메뉴 표시줄에서 Docker 서비스를 다시 시작하십시오.

   Ubuntu의 경우:

      1. 인증서 신뢰

      ```
      mkdir /etc/docker/certs.d/$REGISTRY_HOST && \
      echo | openssl s_client -showcerts -connect $REGISTRY_HOST:443 2>/dev/null | openssl x509 -outform PEM > /etc/docker/certs.d/$REGISTRY_HOST/ca.crt && \
      service docker restart

      ```
      {: codeblock}

4. {{site.data.keyword.open_shift_cp}} 이미지 레지스트리에 로그인하십시오.

      ```
      docker login $REGISTRY_HOST -u $(oc whoami) -p $(oc whoami -t)
      ```
      {: codeblock}

5. IBM Passport Advantage에서 다운로드한 {{site.data.keyword.edge_devices_notm}} 설치 압축 파일을 압축 해제하십시오.

    ```
    tar -zxvf ibm-ecm-4.1.0-x86_64.tar.gz && \
    cd ibm-ecm-4.1.0-x86_64
    ```
    {: codeblock}

6. 아카이브 컨텐츠를 카탈로그에 로드하고, 이미지를 레지스트리의 ibmcom 네임스페이스에 로드하십시오.

    ```
    cloudctl catalog load-archive --archive ibm-ecm-prod-catalog-archive-4.1.0.tgz --registry $REGISTRY_HOST/ibmcom
    ```
    {: codeblock}

  참고: {{site.data.keyword.edge_devices_notm}}에서는 CLI 구동 설치만 지원하며, 이 릴리스의 경우 카탈로그로의 설치는 지원되지 않습니다.

7. 차트의 압축된 파일 컨텐츠를 현재 디렉토리로 추출하고 작성한 디렉토리로 이동하십시오.

    ```
    tar -O -zxvf ibm-ecm-prod-catalog-archive-4.1.0.tgz charts/ibm-ecm-prod-4.1.0.tgz | tar -zxvf - && \
    cd ibm-ecm-prod
    ```
    {: codeblock}

8. 하나가 설정되지 않은 경우 기본 스토리지 클래스를 정의하십시오.

   ```
   # oc get storageclass
   NAME                                 PROVISIONER                     AGE
   rook-ceph-block-internal             rook-ceph.rbd.csi.ceph.com      8h
   rook-ceph-cephfs-internal (default)  rook-ceph.cephfs.csi.ceph.com   8h
   rook-ceph-delete-bucket-internal     ceph.rook.io/bucket             8h
   ```
   
   위의 **(default)** 문자열을 갖는 행이 보이지 않는 경우, 선호하는 기본 스토리지를 다음으로 태그 지정하십시오.

   ```
   oc patch storageclass <PREFERRED_DEFAULT_STORAGE_CLASS_NAME> -p '{"metadata": {"annotations": {"storageclass.kubernetes.io/is-default-class": "true"}}}'
   ```
   {: codeblock}

9. 구성 옵션을 읽고 고려한 후, [README.md](README.md)의 **차트 설치** 섹션을 따르십시오.

  스크립트는 위의 **설치 요약** 섹션에서 언급된 관리 허브 컴포넌트를 설치하고 설치 검증을 실행한 후 아래의 **사후 설치 구성** 섹션을 다시 참조합니다.

## 설치 후 구성
{: #postconfig}

초기 설치를 실행한 것과 동일한 호스트에서 다음 명령을 실행하십시오.

1. 위의 **설치 프로세스** 섹션에 있는 단계 1과 2를 참조하여 클러스터에 로그인하십시오.
2. 위 [설치 프로세스](#process)의 5단계에서 추출한 압축 컨텐츠의 해당 OS/ARCH 디렉토리에 **horizon-edge-packages**에서 발견한 Ubuntu {{site.data.keyword.linux_notm}} 또는 macOS 패키지 설치 프로그램으로 **hzn** CLI를 설치하십시오.
  * Ubuntu {{site.data.keyword.linux_notm}} 예:

    ```
    sudo dpkg -i horizon-edge-packages/linux/ubuntu/bionic/amd64/horizon-cli*.deb
    ```
    {: codeblock}

  * macOS 예:

    ```
    sudo installer -pkg horizon-edge-packages/macos/horizon-cli-*.pkg -target /
    ```
    {: codeblock}

3. 다음 단계에 필요한 다음 변수를 내보내십시오.

    ```
    export EXCHANGE_ROOT_PASS=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-config}" | base64 --decode | jq -r .api.root.password)
    export HZN_EXCHANGE_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}' -n kube-system)/ec-exchange/v1
    export HZN_EXCHANGE_USER_AUTH="root/root:$EXCHANGE_ROOT_PASS"
    export HZN_ORG_ID=IBM
    ```
    {: codeblock}

4. {{site.data.keyword.open_shift_cp}} 인증 기관을 신뢰하십시오.
    ```
    oc --namespace kube-system get secret cluster-ca-cert -o jsonpath="{.data['tls\.crt']}" | base64 --decode > /tmp/icp-ca.crt
    ```
    {: codeblock}

  * Ubuntu {{site.data.keyword.linux_notm}} 예:
     ```
     sudo cp /tmp/icp-ca.crt /usr/local/share/ca-certificates &&sudo update-ca-certificates
     ```
    {: codeblock}

  * macOS 예:

    ```
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain /tmp/icp-ca.crt
    ```
    {: codeblock}

5. 서명 키 쌍을 작성하십시오. 자세한 정보는 [에지 서비스 작성 준비](../developing/service_containers.md)에서 5단계를 참조하십시오.
    ```
    hzn key create <company-name> <owner@email>
    ```
    {: codeblock}

6. 설정이 {{site.data.keyword.edge_devices_notm}} exchange API와 통신할 수 있는지 확인하려면 다음을 실행하십시오.
    ```
    hzn exchange status
    ```
    {: codeblock}

7. 샘플 에지 서비스를 채우십시오.

    ```
    curl https://raw.githubusercontent.com/open-horizon/examples/v4.1/tools/exchangePublishScript.sh | bash -s -- -c $(oc get -n kube-public configmap -o jsonpath="{.items[]..data.cluster_name}")
    ```
    {: codeblock}

8. 다음 명령을 실행하여 {{site.data.keyword.edge_devices_notm}} exchange에서 작성한 일부 서비스 및 정책을 확인하십시오.

    ```
    hzn exchange service list IBM/
    hzn exchange pattern list IBM/
    hzn exchange service listpolicy
    ```
    {: codeblock}

9. 아직 설정하지 않은 경우 {{site.data.keyword.open_shift_cp}} 관리 콘솔을 사용하여 LDAP 연결을 작성하십시오. LDAP 연결을 설정한 후 팀을 작성하고, 해당 팀에 네임스페이스에 대한 액세스를 부여하며, 해당 팀에 사용자를 추가하십시오. 이렇게 하면 개별 사용자에게 API 키를 작성할 수 있는 권한이 부여됩니다.

  참고: API 키는 {{site.data.keyword.edge_devices_notm}} CLI에서 인증을 위해 사용됩니다. LDAP에 대한 자세한 정보는 [LDAP 연결 구성 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/iam/3.4.0/configure_ldap.html)을 참조하십시오.


## 에지 디바이스를 위해 필요한 정보 및 파일 수집
{: #prereq_horizon}

에지 디바이스에 {{site.data.keyword.edge_devices_notm}} 에이전트를 설치하고 {{site.data.keyword.edge_devices_notm}}에 등록하려면 여러 파일이 필요합니다. 이 절은 각 에지 디바이스에서 사용할 수 있는 tar 파일에 해당 파일 수집을 안내합니다.

이미 **cloudctl** 및 **kubectl** 명령을 설치하고 이 페이지의 앞에서 설명한 대로 설치 컨텐츠에서 **ibm-edge-computing-4.1.0-x86_64.tar.gz**를 추출했다고 가정합니다.

1. 위의 **설치 프로세스** 섹션에 있는 단계 1과 2를 참조하여 다음 환경 변수를 설정하십시오.

   ```
   export CLUSTER_URL=<cluster-url>
   export CLUSTER_USER=<your-icp-admin-user>
   export CLUSTER_PW=<your-icp-admin-password>
   ```
   {: codeblock}

2. **edgeDeviceFiles.sh**의 최신 버전을 다운로드하십시오.

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/v4.0/tools/edgeDeviceFiles.sh
   chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

3. **edgeDeviceFiles.sh** 스크립트를 실행하여 필요한 파일을 수집하십시오.

   ```
   ./edgeDeviceFiles.sh <edge-device-type> -t
   ```
   {: codeblock}

   명령 인수:
   * 지원되는 **<edge-device-type>** 값: **32-bit-ARM** , **64-bit-ARM**, **x86_64-{{site.data.keyword.linux_notm}}** 또는 **{{site.data.keyword.macOS_notm}}**
   * **-t**: 수집된 모드 파일을 포함하는 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일을 작성하십시오. 이 플래그가 설정되지 않은 경우 수집된 파일은 현재 디렉토리에 위치합니다.
   * **-k**: **$USER-Edge-Device-API-Key**라는 새 API 키를 작성하십시오. 이 플래그가 설정되지 않으면 기존 API 키가 **$USER-Edge-Device-API-Key**라는 하나에 대해 검사되고 키가 이미 존재하면 작성을 건너뜁니다.
   * **-d** **<distribution>**: **64-bit-ARM** 또는 **x86_64-Linux**에 설치하는 경우 기본 바이오닉 대신 Ubuntu의 이전 버전에 대해 **-d xenial**을 지정할 수 있습니다. **32-bit-ARM**에 설치하는 경우 기본 부스터 대신 **-d stretch**를 지정할 수 있습니다. -d 플래그는 macOS에서 무시됩니다.
   * **-f** **<directory>**: 수집된 파일을 이동할 디렉토리를 지정하십시오. 디렉토리가 없으면 작성됩니다. 기본값은 현재 디렉토리입니다.

4. 이전 단계의 명령은 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**라는 파일을 작성합니다. 에지 디바이스의 추가 유형(다른 아키텍처)이 있는 경우 각 유형에 대해 이전 단계를 반복하십시오.

5. **edgeDeviceFiles.sh** 명령에 의해 작성 및 표시되는 API 키를 기록해 두십시오.

6. 이제 **cloudctl**을 통해 로그인되었으며, 사용자가 {{site.data.keyword.horizon}} **hzn** 명령으로 시작하기 위한 추가 API 키를 작성해야 하는 경우

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   명령 출력에서 **API 키**로 시작하는 행의 키 값을 검색하고 이후 사용을 위해 키 값을 저장하십시오.

7. 에지 디바이스를 설정할 준비가 되었을 때 [{{site.data.keyword.edge_devices_notm}}를 사용한 시작하기](../getting_started/getting_started.md)를 따르십시오.

## 설치 제거
{: #uninstall}

참고: 기본적으로 **로컬 데이터베이스**가 구성됩니다. 이 경우, 설치 제거로 모든 지속적 데이터가 삭제됩니다. 설치 제거 스크립트를 실행하기 전에 모든 필수적인 지속적 데이터의 백업을 작성했는지 확인하십시오(백업 지시사항은 README에 문서화되어 있음). **원격 데이터베이스**를 구성한 경우 데이터가 설치 제거 중에 삭제되지 않으며 필요에 따라 수동으로 제거해야 합니다.

설치의 일부로 압축이 풀린 차트의 위치로 돌아가서 제공되는 설치 제거 스크립트를 실행하십시오. 이 스크립트는 helm 릴리스 및 모든 연관된 리소스를 설치 제거합니다. 먼저, **cloudctl**을 사용하여 클러스터 관리자로서 클러스터에 로그인한 후 다음을 실행하십시오.

```
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```
{: codeblock}
