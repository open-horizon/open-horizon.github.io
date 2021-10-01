---

copyright:
years: 2019
lastupdated: "2019-011-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 고급 수동 에이전트 설치 및 등록
{: #advanced_man_install}

이 절에서는 에지 디바이스에 {{site.data.keyword.edge_devices_notm}} 에이전트를 설치하고 등록하기 위한 각 수동 단계에 대해 설명합니다. 자동화된 메소드는 [자동화된 에이전트 설치 및 등록](automated_install.md)을 참조하십시오.
{:shortdesc}

## 에이전트 설치
{: #agent_install}

참고: 명령 구문에 대한 정보는 [이 문서에서 사용된 규칙](../../getting_started/document_conventions.md)을 참조하십시오.

1. 계속하기 전에 `agentInstallFiles-<edge-device-type>.tar.gz` 파일 및 계속하기 전에 이 파일과 함께 작성된 API 키를 확보하십시오.

    [관리 허브 설치](../../hub/offline_installation.md)의 사후 구성 단계로서, 에지 디바이스에 {{site.data.keyword.horizon}} 에이전트를 설치하고 helloworld 예에 등록하기 위해 필요한 파일이 들어 있는 압축 파일이 작성되었습니다.

2. USB 스틱, 보안 복사 명령 또는 기타 방법을 사용하여 에지 디바이스에 이 파일을 복사하십시오.

3. 다음 tar 파일을 압축 해제하십시오.

   ```bash
   tar -zxvf agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

4. 에지 디바이스의 유형에 적용되는 다음 섹션 중 하나를 사용하십시오.

### Linux(ARM 32비트, ARM 64비트 또는 x86_64) 에지 디바이스나 가상 머신에 에이전트 설치
{: #agent_install_linux}

해당 단계를 따르십시오.

1. 로그인하고, 루트가 아닌 사용자로서 로그인한 경우 루트 권한을 갖는 사용자로 전환하십시오.

   ```bash
   sudo -s
   ```
   {: codeblock}

2. Docker 버전을 조회하여 최신 버전인지 확인하십시오.

   ```bash
   docker --version
   ```
   {: codeblock}

      Docker가 설치되지 않았거나 버전이 `18.06.01` 이전 버전인 경우 최신 버전의 Docker를 설치하십시오.

   ```bash
curl -fsSL get.docker.com | sh
      docker --version
   ```
   {: codeblock}

3. 이 에지 디바이스에 복사한 Horizon Debian 패키지를 설치하십시오.

   ```bash
   apt update && apt install ./*horizon*.deb
   ```
   {: codeblock}
   
4. 환경 변수로 특정 정보를 설정하십시오.

   ```bash
   eval export $(cat agent-install.cfg)
   ```
   {: codeblock}

5. `/etc/default/horizon`을 올바른 정보로 채워 에지 디바이스 horizon 에이전트를 {{site.data.keyword.edge_notm}} 클러스터에 지정하십시오.

   ```bash
   sed -i.bak -e "s|^HZN_EXCHANGE_URL=[^ ]*|HZN_EXCHANGE_URL=${HZN_EXCHANGE_URL}|g" -e "s|^HZN_FSS_CSSURL=[^ ]*|HZN_FSS_CSSURL=${HZN_FSS_CSSURL}|g" /etc/default/horizon
   ```
   {: codeblock}

6. Horizon 에이전트가 `agent-install.crt`를 신뢰하게 하십시오.

   ```bash
   if grep -qE '^HZN_MGMT_HUB_CERT_PATH=' /etc/default/horizon; then sed -i.bak -e "s|^HZN_MGMT_HUB_CERT_PATH=[^ ]*|HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt|" /etc/default/horizon; else echo "HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt" >> /etc/default/horizon; fi
   ```
   {: codeblock}
   
7. `/etc/default/horizon`의 변경사항을 적용하려면 에이전트를 다시 시작하십시오.

   ```bash
   systemctl restart horizon.service
   ```
   {: codeblock}

8. 에이전트가 실행 중이고 올바르게 구성되었는지 확인하십시오.

   ```bash
   hzn version
   hzn exchange version
   hzn node list
   ```
   {: codeblock}  

      출력은 다음과 유사해야 합니다(버전 번호 및 URL은 다를 수 있음).

   ```bash
   $ hzn version
   Horizon CLI version: 2.23.29
   Horizon Agent version: 2.23.29
   $ hzn exchange version
   1.116.0
   $ hzn node list
   {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
      ```
   {: codeblock}

9. 이전에 권한 있는(루트) 쉘로 전환한 경우 지금 종료하십시오. 디바이스를 등록하는 다음 단계를 위해 루트 액세스 권한이 필요하지 않습니다.

   ```bash
   exit
   ```
   {: codeblock}

10. [에이전트 등록](#agent_reg)을 계속하십시오.

### macOS 에지 디바이스에서 에이전트 설치
{: #mac-os-x}

1. `horizon-cli` 패키지 인증서를 {{site.data.keyword.macOS_notm}} 키 체인에 가져오십시오.

   ```bash
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain horizon-cli.crt
   ```
   {: codeblock}

      참고: 각 {{site.data.keyword.macOS_notm}} 시스템에서 이 단계를 한 번만 완료하면 됩니다. 이 신뢰할 수 있는 인증서를 가져와서 향후 버전의 {{site.data.keyword.horizon}} 소프트웨어를 설치할 수 있습니다.

2. {{site.data.keyword.horizon}} CLI 패키지를 설치하십시오.

   ```bash
      sudo installer -pkg horizon-cli-*.pkg -target /
   ```
   {: codeblock}

3. 이전 명령은 `/usr/local/bin`에 명령을 추가합니다. `~/.bashrc`에 추가하여 쉘 경로에 해당 디렉토리를 추가하십시오.

   ```bash
   export PATH="/usr/local/bin:$PATH"
   ```
   {: codeblock}

4. `~/.bashrc`에 추가함으로써 해당 디렉토리를 쉘 경로에 추가하여 `/usr/local/share/man`을 man 페이지 경로에 추가하십시오.

  ```bash
  export MANPATH="/usr/local/share/man:$MANPATH"
  ```
  {: codeblock}

5. `~/.bashrc`에 추가하여 `hzn` 명령의 하위 명령 이름 완료를 사용으로 설정하십시오.

  ```bash
      source /usr/local/share/horizon/hzn_bash_autocomplete.sh
  ```
  {: codeblock}

6. **새 디바이스**를 설치하는 경우 이 단계는 필요하지 **않습니다**. 그러나 이 머신에서 이전에 horizon 컨테이너를 설치 및 시작한 경우 다음을 실행하여 지금 중지하십시오.

  ```bash
      horizon-container stop
  ```
  {: codeblock}
7. 환경 변수로 특정 정보를 설정하십시오.

  ```bash
  eval export $(cat agent-install.cfg)
  ```
  {: codeblock}

8. `/etc/default/horizon`을 올바른 정보로 채워 에지 디바이스 horizon 에이전트를 {{site.data.keyword.edge_notm}} 클러스터에 지정하십시오.

  ```bash
  sudo mkdir -p /etc/default

  sudo sh -c "cat << EndOfContent > /etc/default/horizon
  HZN_EXCHANGE_URL=$HZN_EXCHANGE_URL
  HZN_FSS_CSSURL=$HZN_FSS_CSSURL
  HZN_MGMT_HUB_CERT_PATH=${PWD}/agent-install.crt
  HZN_DEVICE_ID=$(hostname)
  EndOfContent"
  ```
  {: codeblock}

9. {{site.data.keyword.horizon}} 에이전트를 시작하십시오.

  ```bash
      horizon-container start
  ```
  {: codeblock}

10. 에이전트가 실행 중이고 올바르게 구성되었는지 확인하십시오.

  ```bash
       hzn version
       hzn exchange version
       hzn node list
  ```
  {: codeblock}

      출력은 다음과 유사해야 합니다(버전 번호 및 URL은 다를 수 있음).

  ```bash
  $ hzn version
  Horizon CLI version: 2.23.29
  Horizon Agent version: 2.23.29
  $ hzn exchange version
  1.116.0
  $ hzn node list
      {
         "id": "",
         "organization": null,
         "pattern": null,
         "name": null,
         "token_last_valid_time": "",
         "token_valid": null,
         "ha": null,
         "configstate": {
            "state": "unconfigured",
            "last_update_time": ""
         },
         "configuration": {
            "exchange_api": "https://9.30.210.34:8443/ec-exchange/v1/",
            "exchange_version": "1.116.0",
            "required_minimum_exchange_version": "1.116.0",
            "preferred_exchange_version": "1.116.0",
            "mms_api": "https://9.30.210.34:8443/ec-css",
            "architecture": "amd64",
            "horizon_version": "2.23.29"
         },
         "connectivity": {
            "firmware.bluehorizon.network": true,
            "images.bluehorizon.network": true
         }
      }
  ```
  {: codeblock}

11. [에이전트 등록](#agent_reg)을 계속하십시오.

## 에이전트 등록
{: #agent_reg}

1. **환경 변수**로 특정 정보를 설정하십시오.

  ```bash
  eval export $(cat agent-install.cfg)
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

2. 샘플 에지 서비스 배치 패턴 목록을 보십시오.

  ```bash
    hzn exchange pattern list IBM/
  ```
  {: codeblock}

3. helloworld 에지 서비스는 가장 기초적인 예제이며 초보자가 사용하기에 좋습니다. 에지 디바이스를 {{site.data.keyword.horizon}}에 **등록**하여 **helloworld 개발 패턴**을 실행하십시오.

  ```bash
  hzn register -p IBM/pattern-ibm.helloworld
  ```
  {: codeblock}

  참고: **노드 ID 사용**으로 시작하는 행의 출력에 노드 ID가 표시됩니다.

4. 에지 디바이스는 {{site.data.keyword.horizon}} 계약 봇 중 하나와 계약을 작성합니다(일반적으로 약 15초가 걸림). `agreement_finalized_time` 및 `agreement_execution_start_time` 필드가 가득 찰 때까지 이 디바이스의 **계약을 반복적으로 조회**하십시오.

  ```bash
        hzn agreement list
  ```
  {: codeblock}

5. **계약이 작성되면** 결과로 시작되었던 Docker 컨테이너 에지 서비스를 나열하십시오.

  ```bash
  sudo docker ps
  ```
  {: codeblock}

6. helloworld 에지 서비스 **출력**을 보십시오.

  ```bash
  sudo hzn service log -f ibm.helloworld
  ```
  {: codeblock}

## 다음에 수행할 작업
{: #what_next}

[IBM Event Streams에 대한 CPU 사용량](cpu_load_example.md)을 탐색하여 기타 에지 서비스 예제를 계속하십시오.
