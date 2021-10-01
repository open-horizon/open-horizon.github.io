---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 클러스터에서 에이전트 제거
{: #remove_agent}

에지 클러스터를 등록 취소하고 해당 클러스터에서 {{site.data.keyword.ieam}} 에이전트를 제거하려면 다음 단계를 수행하십시오.

1. tar 파일로부터 **agent-uninstall.sh** 스크립트를 추출하십시오.

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Horizon Exchange 사용자 인증 정보를 가져오십시오.

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. 에이전트를 제거하십시오.

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

참고: 네임스페이스 삭제가 "종료 중" 상태에서 중지하는 경우가 있습니다. 이 상황에서는 [네임스페이스가 종료 상태에 머물러 있음](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html)을 참조하여 네임스페이스를 수동으로 삭제하십시오.
