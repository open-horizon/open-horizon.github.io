---

copyright:
years: 2020
lastupdated: "2020-5-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 자동화된 에이전트 설치 및 등록
{: #method_one}

참고: 해당 단계는 모든 디바이스 유형(아키텍처)에 대해 동일합니다.

1. 관리자로부터 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일과 API 키를 확보하십시오. 관리자는 [에지 디바이스를 위한 필요한 정보 및 파일 수집](../../hub/gather_files.md#prereq_horizon)에서 이미 이들을 작성했어야 합니다. 보안 복사 명령, USB 스틱 또는 다른 방법을 사용하여 이 파일을 에지 디바이스에 복사하십시오. 또한, API 키 값을 기록해 두십시오. 후속 단계에서 필요합니다. 그런 다음, 후속 단계를 위해 환경 변수에서 파일 이름을 설정하십시오.

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz
   ```
   {: codeblock}

2. tar 파일로부터 **agent-install.sh** 명령을 추출하십시오.

   ```bash
   tar -zxvf $AGENT_TAR_FILE agent-install.sh
   ```
   {: codeblock}

3. {{site.data.keyword.horizon}} exchange 사용자 인증 정보(API 키)를 내보내십시오.

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  ```
  {: codeblock}

4. **agent-install.sh** 명령을 실행하여 {{site.data.keyword.horizon}} 에이전트를 설치 및 구성하고 에지 디바이스를 등록하여 helloworld 샘플 에지 서비스를 실행하십시오.

  ```bash
  sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z $AGENT_TAR_FILE
  ```
  {: codeblock}

  참고: 에이전트 패키지의 설치 중에 "현재 노드 구성을 겹쳐쓰시겠습니까?`[y/N]`"라는 질문이 프롬프트될 수 있습니다. **agent-install.sh**가 구성을 올바르게 설정하기 때문에 "y"를 응답하고 Enter를 누를 수 있습니다.

  모든 사용 가능한 **agent-install.sh** 플래그 설명을 보려면 다음을 수행하십시오.

  ```bash
  ./agent-install.sh -h
  ```
  {: codeblock}

5. 이제 에지 디바이스가 설치 및 등록되었으므로, 특정 정보를 사용자 쉘의 환경 변수로 설정하십시오. 그러면 **hzn** 명령을 실행하여 helloworld 결과를 볼 수 있습니다.

  ```bash
  eval export $(cat agent-install.cfg)
  hzn service log -f ibm.helloworld
  ```
  {: codeblock}
  
  참고: 출력 표시를 중지하려면 **Ctrl** **C**를 누르십시오.

6. **hzn** 명령의 플래그와 하위 명령을 탐색하십시오.

  ```bash
  hzn --help
  ```
  {: codeblock}

7. 또한 {{site.data.keyword.ieam}} 콘솔을 사용하여 에지 디바이스(노드), 서비스, 패턴 및 정책을 볼 수도 있습니다. [관리 콘솔 사용](../getting_started/accessing_ui.md)을 참조하십시오.

8. [IBM Event Streams에 대한 CPU 사용량](cpu_load_example.md)을 탐색하여 기타 에지 서비스 예제를 계속하십시오.
