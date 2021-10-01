---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에이전트 업데이트
{: #updating_the_agent}

업데이트된 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 에이전트 패키지를 받은 경우 에지 디바이스를 쉽게 업데이트할 수 있습니다.

1. [에지 디바이스를 위한 필요한 정보 및 파일 수집](../hub/gather_files.md#prereq_horizon)의 단계를 수행하여 최신 에이전트 패키지를 갖는 업데이트된 **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** 파일을 작성하십시오.
  
2. 각 에지 디바이스에 대해, **agent-install.sh** 명령을 실행할 때를 제외하고 [에이전트의 자동화된 에이전트 설치 및 등록](automated_install.md#method_one)의 단계를 수행하고, 에지 디바이스에서 실행하려는 서비스와 패턴 또는 정책을 지정하십시오.
