---

copyright:
years: 2019
lastupdated: "2019-09-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 보안 
{: #security}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 경우 [Open Horizon](https://github.com/open-horizon)을 기반으로 여러 보안 기술을 사용하여 공격에 대해 보안을 유지하고 개인정보를 보호합니다. {{site.data.keyword.ieam}} 보안 및 역할에 대한 자세한 정보는 다음을 참조하십시오.

* [보안 및 개인정보 보호](../OH/docs/user_management/security_privacy.md)
* [역할 기반 액세스 제어](rbac.md)
* [GDPR 대비를 위한 {{site.data.keyword.edge_notm}} 고려사항](gdpr.md)
{: childlinks}

고유한 RSA 키가 아직 없는 경우 워크로드 서명 키 작성에 대한 자세한 정보는 [에지 서비스 작성 준비](../developing/service_containers.md)를 참조하십시오. 교환을 위해 공개하고 {{site.data.keyword.ieam}} 에이전트를 사용하여 올바른 워크로드를 시작했는지 확인하는 경우 이러한 키를 사용하여 서비스에 서명합니다.
