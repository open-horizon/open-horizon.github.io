---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.icp_notm}} 환경에 특정한 문제점 해결 팁
{: #troubleshooting_icp}

이 컨텐츠를 검토하여 {{site.data.keyword.edge_devices_notm}} 관련 {{site.data.keyword.icp_notm}} 환경의 공통 문제를 해결하는 데 도움을 받으십시오. 해당 팁이 공통 문제를 해결하고 근본 원인을 식별하기 위한 정보를 얻는 데 도움이 될 수 있습니다.
{:shortdesc}

## {{site.data.keyword.edge_devices_notm}} 인증 정보가 {{site.data.keyword.icp_notm}} 환경에서 사용하도록 올바르게 구성되었습니까?
{: #setup_correct}

이 환경에서 {{site.data.keyword.edge_devices_notm}} 내 조치를 완료하려면 {{site.data.keyword.icp_notm}} 사용자 계정이 필요합니다. 해당 계정에서 작성된 API 키도 필요합니다.

이 환경에서 {{site.data.keyword.edge_devices_notm}} 인증 정보를 확인하려면 다음 명령을 실행하십시오.

   ```
    hzn exchange user list
   ```
   {: codeblock}

Exchange에서 하나 이상의 사용자를 표시하는 JSON으로 형식화된 항목이 리턴되는 경우 {{site.data.keyword.edge_devices_notm}} 인증 정보도 올바르게 구성된 것입니다.

오류 응답이 리턴되는 경우 인증 정보 설정 문제점을 해결하기 위한 단계를 수행할 수 있습니다.

오류 메시지에서 잘못된 API 키를 표시하는 경우 다음 명령을 사용하는 새 API 키를 작성할 수 있습니다.

[필수 정보 및 파일 수집](../developing/software_defined_radio_ex_full.md#prereq-horizon)을 참조하십시오.
