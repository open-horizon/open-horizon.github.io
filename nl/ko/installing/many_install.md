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

# 대량 에이전트 설치 및 등록
{: #batch-install}

비슷한 유형(다시 말하면, 동일한 아키텍처, 운영 체제 및 패턴 또는 정책)의 복수 에지 디바이스를 설정하려면 대량 설치 프로세스를 사용하십시오.

**참고**: 이 프로세스의 경우 macOs 컴퓨터인 대상 에지 디바이스는 지원되지 않습니다. 그러나 원하는 경우 macOs에서 이 프로세스를 구동할 수 있습니다. (달리 말하면, 이 호스트가 macOs일 수 있습니다.)

### 선행 조건

* 설치 및 등록될 디바이스가 관리 허브에 네트워크를 통해 액세스할 수 있어야 합니다.
* 디바이스에 운영 체제가 설치되어 있어야 합니다.
* 에지 디바이스에 대해 DHCP를 사용 중인 경우 태스크가 완료될 때까지 각 디바이스가 동일한 IP 주소를 유지해야 합니다(또는 DDNS를 사용 중인 경우 동일한 `hostname`).
* 모든 에지 서비스 사용자 입력이 서비스 정의 또는 패턴이나 배치 정책에서 기본값으로 지정되어야 합니다. 노드에 특정한 사용자 입력은 사용할 수 없습니다.

### 프로시저
{: #proc-multiple}

1. [에지 디바이스를 위해 필요한 정보 및 파일 수집](../hub/gather_files.md#prereq_horizon)에 따라 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일 및 API 키를 얻거나 작성하지 않은 경우 지금 이를 수행하십시오. 다음 환경 변수에서 파일의 이름과 API 키 값을 설정하십시오.

   ```bash
   export AGENT_TAR_FILE=agentInstallFiles-<edge-device-type>.tar.gz    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
  {: codeblock}

2. **pssh** 패키지는 **pssh** 및 **pscp** 명령을 포함하는데, 이들을 사용하면 많은 에지 디바이스에 병렬로 명령을 실행하고 파일을 많은 에지 디바이스에 병렬로 복사할 수 있습니다. 이 호스트에 이러한 명령이 없는 경우 지금 패키지를 설치하십시오.

  * {{site.data.keyword.linux_notm}}의 경우:

   ```bash
   sudo apt install pssh    alias pssh=parallel-ssh    alias pscp=parallel-scp
   ```
   {: codeblock}

  * {{site.data.keyword.macOS_notm}}의 경우:

   ```bash
   brew install pssh
   ```
   {: codeblock}

   (**brew**가 아직 설치되지 않은 경우 [Brew를 사용하여 macOs 컴퓨터에 pssh 설치](https://brewinstall.org/Install-pssh-on-Mac-with-Brew/)를 참조하십시오.)

3. 여러 가지 방법으로 에지 디바이스에 대한 **pscp** 및 **pssh** 액세스 권한을 부여할 수 있습니다. 이 컨텐츠는 ssh 공개 키를 사용하는 방법에 대해 설명합니다. 먼저, 이 호스트에 ssh 키 쌍(일반적으로 **~/.ssh/id_rsa** 및 **~/.ssh/id_rsa.pub**에 있음)이 있어야 합니다. ssh 키 쌍이 없는 경우 생성하십시오.

   ```bash
   ssh-keygen -t rsa
   ```
   {: codeblock}

4. 공개 키의 컨텐츠(**~/.ssh/id_rsa.pub**)를 **/root/.ssh/authorized_keys**의 각 에지 디바이스에 배치하십시오.

5. 각 에지 디바이스의 IP 주소나 호스트 이름을 {{site.data.keyword.ieam}} 노드 이름에 맵핑하는 **node-id-mapping.csv**라는 2열 맵핑 파일을 작성하십시오. 이 파일은 등록 중에 제공되어야 합니다. **agent-install.sh**가 각 에지 디바이스에서 실행할 때, 이 파일은 해당 디바이스에 제공할 에지 노드 이름을 말합니다. CSV 형식을 사용하십시오.

   ```bash
   Hostname/IP, Node Name    1.1.1.1, factory2-1    1.1.1.2, factory2-2
   ```
   {: codeblock}

6. **node-id-mapping.csv**를 에이전트 tar 파일에 추가하십시오.

   ```bash
   gunzip $AGENT_TAR_FILE    tar -uf ${AGENT_TAR_FILE%.gz} node-id-mapping.csv    gzip ${AGENT_TAR_FILE%.gz}
   ```
   {: codeblock}

7. 대량 설치하려는 에지 디바이스의 목록을 넣고 **nodes.hosts**라는 파일에 등록하십시오. 이 파일은 **pscp** 및 **pssh** 명령과 함께 사용됩니다. 각 행은 표준 ssh 형식 `<user>@<IP-or-hostname>`이어야 합니다.

   ```bash
   root@1.1.1.1    root@1.1.1.2
   ```
   {: codeblock}

   **참고**: 임의의 호스트에 대해 비루트 사용자를 사용하는 경우 비밀번호를 입력하지 않고 해당 사용자로부터의 sudo를 허용하도록 sudo를 구성해야 합니다.

8. 에이전트 tar 파일을 에지 디바이스에 복사하십시오. 이 단계에는 시간이 약간 소요될 수 있습니다.

   ```bash
   pscp -h nodes.hosts -e /tmp/pscp-errors $AGENT_TAR_FILE /tmp
   ```
   {: codeblock}

   **참고**: 임의의 에지 디바이스에 대한 **pscp** 출력에서 **[FAILURE]**가 표시되는 경우 **/tmp/pscp-errors**에서 오류를 확인할 수 있습니다.

9. 각 에지 디바이스에서 **agent-install.sh**를 실행하여 Horizon 에이전트를 설치하고 에지 디바이스를 등록하십시오. 패턴 또는 정책을 사용하여 에지 디바이스를 등록할 수 있습니다.

   1. 패턴을 가진 에지 디바이스를 등록하십시오.

      ```bash
      pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -p IBM/pattern-ibm.helloworld -w ibm.helloworld -o IBM -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      **IBM/pattern-ibm.helloworld** 배치 패턴을 가진 에지 디바이스를 등록하는 대신 **-p**, **-w** 및 **-o** 플래그를 수정하여 다른 배치 패턴을 사용할 수 있습니다. 모든 사용 가능한 **agent-install.sh** 플래그 설명을 보려면 다음을 수행하십시오.

      ```bash
      tar -zxf $AGENT_TAR_FILE agent-install.sh &&./agent-install.sh -h
      ```
      {: codeblock}

   2. 또는 정책을 가진 에지 디바이스를 등록하십시오. 노드 정책을 작성하고, 이를 에지 디바이스에 복사한 후 해당 정책을 가진 디바이스를 등록하십시오.

      ```bash
      echo '{ "properties": [ { "name": "nodetype", "value": "special-node" } ] }' > node-policy.json       pscp -h nodes.hosts -e /tmp/pscp-errors node-policy.json /tmp       pssh -h nodes.hosts -t 0 "bash -c \"tar -zxf /tmp/$AGENT_TAR_FILE agent-install.sh && sudo -s ./agent-install.sh -i . -u $HZN_EXCHANGE_USER_AUTH -n /tmp/node-policy.json  -z /tmp/$AGENT_TAR_FILE 2>&1 >/tmp/agent-install.log \" "
      ```
      {: codeblock}

      이제 에지 디바이스가 준비되었지만 이 유형의 에지 디바이스(이 예제에서는 **nodetype**이 **special-node**인 디바이스)로 서비스를 배치하도록 지정하는 배치 정책(비즈니스 정책)을 작성할 때까지 실행 중인 에지 서비스는 시작되지 않습니다. 세부사항은 [배치 정책 사용](../using_edge_services/detailed_policy.md)을 참조하십시오.

10. 에지 디바이스의 **pssh** 출력에 **[FAILURE]**가 표시되면, 에지 디바이스로 이동하고 **/tmp/agent-install.log**를 표시하여 문제점을 조사할 수 있습니다.

11. **pssh** 명령이 실행 중인 동안 {{site.data.keyword.edge_notm}} 콘솔에서 에지 노드의 상태를 볼 수 있습니다. [관리 콘솔 사용](../console/accessing_ui.md)을 참조하십시오.
