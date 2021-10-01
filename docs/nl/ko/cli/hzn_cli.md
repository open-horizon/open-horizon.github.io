---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# hzn CLI 설치
{: #using_hzn_cli}

`hzn` 명령은 {{site.data.keyword.ieam}} 명령행 인터페이스입니다. 에지 노드에 {{site.data.keyword.ieam}} 에이전트 소프트웨어를 설치할 때 `hzn` CLI가 자동으로 설치됩니다. 그러나 에이전트 없이 `hzn` CLI를 설치할 수도 있습니다. 예를 들어 전체 에이전트 없이 에지 관리자가 {{site.data.keyword.ieam}} Exchange를 조회하거나 에지 개발자가 `hzn` 명령을 사용하여 테스트하려고 할 수 있습니다.

1. `horizon-cli` 패키지를 가져오십시오. [에지 노드 파일 수집](../hub/gather_files.md) 단계에서 조직이 수행한 작업에 따라 CSS 또는 `agentInstallFiles-<edge-node-type>.tar.gz` tar 파일에서 `horizon-cli` 패키지를 가져올 수 있습니다.

   * CSS에서 `horizon-cli` 패키지를 가져오십시오.

      * API 키가 아직 없는 경우 [API 키 작성](../hub/prepare_for_edge_nodes.md)의 단계를 따라 작성하십시오. 해당 단계에서 환경 변수를 설정하십시오.

         ```bash
         export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
         ```
         {: codeblock}

      * `HOST_TYPE`을 `horizon-cli` 패키지를 설치할 호스트 유형과 일치하도록 다음 값 중 하나로 설정하십시오.

         * linux-deb-amd64
         * linux-deb-arm64
         * linux-deb-armhf
         * linux-rpm-x86_64
         * linux-rpm-ppc64le
         * macos-pkg-x86_64

         ```bash
         HOST_TYPE=<host-type>
         ```
         {: codeblock}

      * CSS에서 인증서, 구성 파일 및 `horizon-cli` 패키지가 포함된 tar 파일을 다운로드하십시오.

         ```bash
         curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.crt $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.crt/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o agent-install.cfg $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.cfg/data          curl -sSL -w "%{http_code}" -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" --cacert agent-install.crt -o horizon-agent-$HOST_TYPE.tar.gz $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/horizon-agent-$HOST_TYPE.tar.gz/data
         ```
         {: codeblock}

      * tar 파일에서 `horizon-cli` 패키지를 추출하십시오.

         ```bash
         rm -f horizon-cli*   # remove any previous versions          tar -zxvf horizon-agent-$HOST_TYPE.tar.gz
         ```
         {: codeblock}

   * 또는 `agentInstallFiles-<edge-node-type>.tar.gz` tar 파일에서 `horizon-cli` 패키지를 가져오십시오.

      * 관리 허브 관리자로부터 `agentInstallFiles-<edge-node-type>.tar.gz` 파일을 가져오십시오. 여기서 `<edge-node-type>`은 `horizon-cli`를 설치할 호스트와 일치합니다. 이 파일을 해당 호스트에 복사하십시오.

      * tar 파일의 압축을 해제하십시오.

         ```bash
         tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
         ```
         {: codeblock}

2. `/etc/default/horizon`을 작성하거나 업데이트하십시오.

   ```bash
   sudo cp agent-install.cfg /etc/default/horizon    sudo cp agent-install.crt /etc/horizon    sudo sh -c "echo 'HZN_MGMT_HUB_CERT_PATH=/etc/horizon/agent-install.crt' >> /etc/default/horizon"
   ```
   {: codeblock}

3. `horizon-cli` 패키지를 설치하십시오.

   * 패키지 버전이 [컴포넌트](../getting_started/components.md)에 나열된 디바이스 에이전트와 같은지 확인하십시오.

   * debian 기반 배포판에서 다음을 수행하십시오.

     ```bash
     sudo apt update && sudo apt install ./horizon-cli*.deb
     ```
     {: codeblock}

   * RPM 기반 배포판:

     ```bash
     sudo yum install ./horizon-cli*.rpm
     ```
     {: codeblock}

   * {{site.data.keyword.macOS_notm}}의 경우:

     ```bash
     sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt      sudo installer -pkg horizon-cli-*.pkg -target /      pkgutil --pkg-info com.github.open-horizon.pkg.horizon-cli   # confirm version installed
     ```
     {: codeblock}

## hzn CLI 설치 제거

호스트에서 `horizon-cli` 패키지를 제거하려면 다음을 수행하십시오.

* 다음과 같이 debian 기반 배포판에서 `horizon-cli`를 설치 제거하십시오.

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* RPM 기반 배포판에서 `horizon-cli`를 설치 제거하십시오.

  ```bash
  sudo yum remove horizon-cli
  ```
  {: codeblock}

* 또는 {{site.data.keyword.macOS_notm}}에서 `horizon-cli`를 설치 제거하십시오.

  ```bash
  sudo horizon-cli-uninstall.sh
  ```
  {: codeblock}
