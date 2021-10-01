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

참고: 해당 단계는 모든 에지 디바이스 유형(아키텍처)에 대해 동일합니다.

1. API 키가 아직 없는 경우 [API 키 작성](../hub/prepare_for_edge_nodes.md)의 단계를 따라 작성하십시오. 이 프로세스는 API 키를 작성하고 일부 파일을 찾은 후 에지 노드 설정 시 필요한 환경 변수 값을 수집합니다.

2. 에지 디바이스에 로그인하고 1단계에서 확보한 같은 환경 변수를 설정하십시오.

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
   ```
   {: codeblock}

3. 관리자가 준비한 설치 번들을 사용하지 않을 경우 CSS(Cloud Sync Service)에서 사용자 디바이스로 **agent-install.sh** 스크립트를 다운로드하여 실행 가능하도록 만드십시오.

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data    chmod +x agent-install.sh
   ```
   {: codeblock}

4. **agent-install.sh**를 실행하여 CSS에서 필요한 파일을 가져오고 {{site.data.keyword.horizon}} 에이전트를 설치 및 구성한 후 에지 디바이스를 등록하여 helloworld 샘플 에지 서비스를 실행하십시오.

   ```bash
   sudo -s -E ./agent-install.sh -i 'css:' -p IBM/pattern-ibm.helloworld -w '*' -T 120
   ```
   {: codeblock}

   사용 가능한 **agent-install.sh** 플래그 설명을 모두 보려면 **./agent-install.sh -h**를 실행하십시오.

   참고: {{site.data.keyword.macOS_notm}}에서 에이전트는 루트로 실행 중인 Docker 컨테이너에서 실행됩니다.

5. helloworld 출력을 확인하십시오.

   ```bash
   hzn service log -f ibm.helloworld   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

6. helloworld 에지 서비스가 시작되지 않을 경우 다음 명령을 실행하여 오류 메시지를 확인하십시오.

   ```bash
   hzn eventlog list -f   # Press Ctrl-c to stop the output display
   ```
   {: codeblock}

7. (선택사항) **hzn** 명령을 사용하여 {{site.data.keyword.horizon}} Exchange에서 서비스, 패턴, 배치 정책을 확인하십시오. 쉘에서 특정 정보를 환경 변수로 설정하고 다음 명령을 실행하십시오.

   ```bash
   eval export $(cat agent-install.cfg)   hzn exchange service list IBM/   hzn exchange pattern list IBM/   hzn exchange deployment listpolicy
   ```
   {: codeblock}

8. **hzn** 명령 플래그 및 하위 명령을 탐색하십시오.

   ```bash
   hzn --help
   ```
   {: codeblock}

## 다음 수행할 작업

* {{site.data.keyword.ieam}} 콘솔을 사용하여 에지 노드(디바이스), 서비스, 패턴 및 정책을 보십시오. 자세한 정보는 [관리 콘솔 사용](../console/accessing_ui.md)을 참조하십시오.
* 다른 에지 서비스 예제를 탐색하고 실행하십시오. 자세한 정보는 [IBM Event Streams에 대한 CPU 사용량](../using_edge_services/cpu_load_example.md)을 참조하십시오.
