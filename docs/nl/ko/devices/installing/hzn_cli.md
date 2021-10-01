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

에지 노드에 {{site.data.keyword.ieam}} 에이전트 소프트웨어를 설치할 때 **hzn** CLI가 자동으로 설치됩니다. 그러나 agen 없이 **hzn** CLI도 설치할 수 있습니다. 예를 들어 에지 관리자가 {{site.data.keyword.ieam}} Exchange를 조회하거나 에지 개발자가 **hzn dev** 명령을 사용하여 이를 테스트하려고 할 수 있습니다.

1. 관리 허브 관리자로부터 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일을 가져오십시오.
여기서 **&lt;edge-device-type&gt;**은 **hzn**을 설치할 호스트와 일치합니다. 관리자는 [에지 디바이스를 위해 필요한 정보 및 파일 수집](../../hub/gather_files.md#prereq_horizon)에서 이미 해당 파일을 작성했어야 합니다. 이 파일을 **hzn**을 설치할 호스트에 복사하십시오.

2. 후속 단계에 대해 환경 변수에서 파일 이름을 설정하십시오.

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

3. tar 파일에서 horizon CLI 패키지를 추출하십시오.

   ```bash
   tar -zxvf $AGENT_TAR_FILE 'horizon-cli*'
   ```
   {: codeblock}

   * 패키지 버전이 [컴포넌트](../getting_started/components.md)에 나열된 디바이스 에이전트와 같은지 확인하십시오.

4. **horizon-cli** 패키지를 설치하십시오.

   * debian 기반 배포판에서 다음을 수행하십시오.

     ```bash
     sudo apt update && sudo apt install horizon-cli*.deb
     ```
     {: codeblock}

   * {{site.data.keyword.macOS_notm}}의 경우:

     ```bash
      sudo installer -pkg horizon-cli-*.pkg -target /
     ```
     {: codeblock}

     참고: {{site.data.keyword.macOS_notm}}의 Finder에서 horizon-cli 패키지도 설치할 수 있습니다.
파일을 두 번 클릭하여 설치 프로그램을 여십시오. "식별되지 않는 개발자로부터 받았기 때문에 프로그램을 열 수 없음"이라는 오류 메시지를 받는 경우 파일을 마우스 오른쪽 단추로 클릭하여 **열기**를 선택하십시오. "이를 여시겠습니까"란 프롬프트가 표시되면 다시 **열기**를 클릭하십시오. 그런 다음, 프롬프트에 따라 CLI Horizon 패키지를 설치하고 사용자 ID에 관리 권한이 있는지 확인하십시오.

## hzn CLI 설치 제거

호스트에서 **horizon-cli** 패키지를 제거하려면 다음을 수행하십시오.

* 다음과 같이 debian 기반 배포판에서 **horizon-cli**를 설치 제거하십시오.

  ```bash
  sudo apt-get remove horizon-cli
  ```
  {: codeblock}

* 또는 {{site.data.keyword.macOS_notm}}에서 **horizon-cli**를 설치 제거하십시오.

  * hzn 클라이언트 폴더(/usr/local/bin)를 열고 `hzn` 앱을 휴지통(Dock의 끝에 있음)으로 끌어서 놓으십시오.
