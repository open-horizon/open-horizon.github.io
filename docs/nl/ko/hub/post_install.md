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

# 설치 후 구성

## 선행 조건

* [IBM Cloud Pak CLI(**cloudctl**) 및 OpenShift 클라이언트 CLI(**oc**)](../cli/cloudctl_oc_cli.md)
* [**jq**](https://stedolan.github.io/jq/download/)
* [**git**](https://git-scm.com/downloads)
* [**docker**](https://docs.docker.com/get-docker/) 버전 1.13 이상
* **make**

## 설치 확인

1. [{{site.data.keyword.ieam}} 설치](online_installation.md)의 단계를 완료하십시오.
2. {{site.data.keyword.ieam}} 네임스페이스의 모든 팟(Pod)이 **Running** 또는 **Completed**인지 확인하십시오.

   ```
   oc get pods
   ```
   {: codeblock}

   다음은 로컬 데이터베이스 및 로컬 Secrets Manager가 설치된 경우 볼 수 있는 예제입니다. 일부 초기화 다시 시작은 예상대로 작동하지만 다시 시작을 여러 번 시도하면 일반적으로 문제가 발생합니다.
   ```
   $ oc get pods NAME READY STATUS RESTARTS AGE create-agbotdb-cluster-j4fnb 0/1 Completed 0 88m create-exchangedb-cluster-hzlxm 0/1 Completed 0 88m ibm-common-service-operator-68b46458dc-nv2mn 1/1 Running 0 103m ibm-eamhub-controller-manager-7bf99c5fc8-7xdts 1/1 Running 0 103m ibm-edge-agbot-5546dfd7f4-4prgr 1/1 Running 0 81m ibm-edge-agbot-5546dfd7f4-sck6h 1/1 Running 0 81m ibm-edge-agbotdb-keeper-0 1/1 Running 0 88m ibm-edge-agbotdb-keeper-1 1/1 Running 0 87m ibm-edge-agbotdb-keeper-2 1/1 Running 0 86m ibm-edge-agbotdb-proxy-7447f6658f-7wvdh 1/1 Running 0 88m ibm-edge-agbotdb-proxy-7447f6658f-8r56d 1/1 Running 0 88m ibm-edge-agbotdb-proxy-7447f6658f-g4hls 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5qm9x 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-5whgr 1/1 Running 0 88m ibm-edge-agbotdb-sentinel-5766f666f4-9xjpr 1/1 Running 0 88m ibm-edge-css-5c59c9d6b6-kqfnn 1/1 Running 0 81m ibm-edge-css-5c59c9d6b6-sp84w 1/1 Running 0 81m
   ibm-edge-css-5c59c9d6b6-wf84s                  1/1     Running     0          81m    ibm-edge-cssdb-server-0                        1/1     Running     0          88m    ibm-edge-exchange-b6647db8d-k97r8              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-kkcvs              1/1     Running     0          81m    ibm-edge-exchange-b6647db8d-q5ttc              1/1     Running     0          81m    ibm-edge-exchangedb-keeper-0                   1/1     Running     1          88m    ibm-edge-exchangedb-keeper-1                   1/1     Running     0          85m    ibm-edge-exchangedb-keeper-2                   1/1     Running     0          84m    ibm-edge-exchangedb-proxy-6bbd5b485-cx2v8      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-hs27d      1/1     Running     0          88m    ibm-edge-exchangedb-proxy-6bbd5b485-htldr      1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-hz59z   1/1     Running     1          88m    ibm-edge-exchangedb-sentinel-6d685bf96-m4bdh   1/1     Running     0          88m    ibm-edge-exchangedb-sentinel-6d685bf96-mxv2b   1/1     Running     1          88m    ibm-edge-sdo-0                                 1/1     Running     0          81m    ibm-edge-ui-545d694f6c-4rnrf                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-97ptz                   1/1     Running     0          81m    ibm-edge-ui-545d694f6c-f7bf6                   1/1     Running     0          81m
   ibm-edge-vault-0 1/1 Running 0 81m ibm-edge-vault-bootstrap-k8km9 0/1 Completed 0 80m
   ```
   {: codeblock}

   **참고**:
   * 리소스 또는 스케줄링 문제로 인해 **Pending** 상태인 팟(Pod)에 대한 자세한 정보는 [클러스터 크기 조정](cluster_sizing.md) 페이지를 참조하십시오. 여기에는 컴포넌트의 스케줄링 비용을 줄이는 방법에 대한 정보가 포함되어 있습니다.
   * 기타 오류에 대한 자세한 정보는 [문제점 해결](../admin/troubleshooting.md)을 참조하십시오.
3. **ibm-common-services** 네임스페이스의 모든 팟(Pod)이 **Running** 또는 **Completed**인지 확인하십시오.

   ```
   oc get pods -n ibm-common-services
   ```
   {: codeblock}

4. [권한이 있는 레지스트리](https://myibm.ibm.com/products-services/containerlibrary)를 통해 인타이틀먼트 키를 사용하여 에이전트 번들을 로그인, 가져오기 및 추출하십시오.
    ```
    docker login cp.icr.io --username cp &amp;TWBAMP;&amp;TWBAMP; \ docker rm -f ibm-eam-{{site.data.keyword.semver}}-bundle; \ docker create --name ibm-eam-{{site.data.keyword.semver}}-bundle cp.icr.io/cp/ieam/ibm-eam-bundle:{{site.data.keyword.anax_ver}} bash &amp;TWBAMP;&amp;TWBAMP; \ docker cp ibm-eam-{{site.data.keyword.semver}}-bundle:/ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ tar -zxvf ibm-eam-{{site.data.keyword.semver}}-bundle.tar.gz &amp;TWBAMP;&amp;TWBAMP; \ cd ibm-eam-{{site.data.keyword.semver}}-bundle/tools
    ```
    {: codeblock}
5. 설치 상태 유효성을 검증하십시오.
    ```
    ./service_healthcheck.sh
    ```
    {: codeblock}

    다음 예제 출력을 참조하십시오.
    ```
    $ ./service_healthcheck.sh     ==Running service verification tests for IBM Edge Application Manager==     SUCCESS: IBM Edge Application Manager Exchange API is operational     SUCCESS: IBM Edge Application Manager Cloud Sync Service is operational     SUCCESS: IBM Edge Application Manager Agbot database heartbeat is current     SUCCESS: IBM Edge Application Manager SDO API is operational     SUCCESS: IBM Edge Application Manager UI is properly requiring valid authentication     ==All expected services are up and running==
    ```

   * **service_healthcheck.sh** 명령에 실패했거나 아래 명령을 실행하는 중 문제가 발생하거나 런타임 중에 문제가 있으면 [문제점 해결](../admin/troubleshooting.md)을 참조하십시오.

## 설치 후 구성
{: #postconfig}

다음 프로세스는 **hzn** CLI의 설치를 지원하는 호스트에서 실행해야 합니다. 이 CLI는 현재 Debian/apt 기반 Linux, amd64 Red Hat/rpm Linux 또는 macOS 호스트에 설치할 수 있습니다. 이러한 단계는 설치 검증 절에서 PPA로부터 다운로드된 동일한 매체를 사용합니다.

1. 지원되는 플랫폼에 대한 지침을 사용하여 **hzn** CLI를 설치하십시오.
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

2. 설치 후 스크립트를 실행하십시오. 이 스크립트는 첫 번째 조직을 작성하기 위해 모든 필요한 초기화를 수행합니다. (조직은 {{site.data.keyword.ieam}}에서 리소스를 구분하고 사용자가 멀티테넌시를 사용하는 방법에 관한 것입니다. 처음에는 이 첫 번째 조직으로 충분합니다. 나중에 추가 조직을 구성할 수 있습니다. 자세한 정보는 [멀티테넌시](../admin/multi_tenancy.md)를 참조하십시오.

   **참고**: **IBM** 및 **root**는 내부 사용 조직이므로 초기 조직으로 선택할 수 없습니다. 조직 이름은 밑줄(_), 쉼표(,), 공백( ), 작은따옴표(') 또는 물음표(?)를 포함할 수 없습니다..

   ```
   ./post_install.sh <choose-your-org-name>
   ```
   {: codeblock}

3. 다음을 실행하여 설치에 대한 {{site.data.keyword.ieam}} 관리 콘솔 링크를 인쇄하십시오.
   ```
   echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')/edge
   ```
   {: codeblock}

## 인증 

{{site.data.keyword.ieam}} 관리 콘솔에 액세스할 때 사용자 인증이 필요합니다. 초기 관리 계정은 이 설치에 의해 작성되었으며 다음 명령으로 인쇄할 수 있습니다.
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

이 관리 계정을 초기 인증에 사용할 수 있으며 다음 명령으로 인쇄된 관리 콘솔 링크에 액세스하여 추가로 [LDAP를 구성](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)할 수 있습니다.
```
echo https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
```
{: codeblock}

LDAP 연결을 설정한 후 팀을 작성하고, 해당 팀에 {{site.data.keyword.edge_notm}} 운영자가 배치된 네임스페이스에 대한 액세스를 부여하며, 해당 팀에 사용자를 추가하십시오. 이렇게 하면 개별 사용자에게 API 키를 작성할 수 있는 권한이 부여됩니다.

API 키는 {{site.data.keyword.edge_notm}} CLI를 사용하여 인증하는 데 사용되며 API 키와 연관된 권한은 생성된 사용자와 동일합니다.

LDAP 연결을 작성하지 않은 경우 초기 관리자 신임 정보를 사용하여 API 키를 작성할 수 있지만 API 키에는 **클러스터 관리자** 권한이 있습니다.

## 다음 단계

에지 노드에 대한 설치 매체를 준비하려면 [에지 노드 파일 수집](gather_files.md) 페이지의 프로세스를 수행하십시오.
