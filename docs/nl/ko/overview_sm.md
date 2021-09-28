---

copyright:
years: 2021
lastupdated: "2021-07-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 시크릿 관리자 개요
{: #overviewofsm}

에지에 배치된 서비스는 종종 클라우드 서비스에 액세스해야 하는데, 이는 서비스가 클라우드 서비스를 인증하기 위해 신임 정보를 필요로 한다는 것을 의미합니다. 시크릿 관리자는 {{site.data.keyword.ieam}} 메타데이터(예: 서비스 정의 및 정책) 내의 세부사항을 노출하지 않고 신임 정보를 저장, 배치 및 관리할 수 있는 보안 메커니즘을 제공합니다. 시크릿 관리자는 {{site.data.keyword.ieam}}의 플러그 가능한 구성요소입니다. 현재, HashiCorp Vault는 유일하게 지원되는 시크릿 관리자입니다.

시크릿은 사용자 ID/비밀번호, 인증서, RSA 키 또는 에지 애플리케이션이 기능을 수행하기 위해 필요로 하는 보호된 리소스에 대한 액세스 권한을 부여하는 기타 신임 정보입니다. 시크릿은 시크릿 관리자에 저장됩니다. 시크릿은 시크릿을 식별하는 데 사용되지만 시크릿 자체의 세부사항에 대한 정보를 제공하지 않는 이름을 가지고 있습니다. 시크릿은 시크릿 관리자의 UI 또는 CLI를 사용하여 {{site.data.keyword.ieam}} CLI 또는 관리자에 의해 관리됩니다.

서비스 개발자는 {{site.data.keyword.ieam}} 서비스 정의 내에서 시크릿의 필요성을 선언합니다. 서비스 배치자는 시크릿 관리자의 시크릿과 서비스를 연관시켜 시크릿 관리자의 시크릿을 서비스 배치에 연결(또는 바인드) 합니다. 예를 들어, 개발자가 기본 인증을 통해 XYZ 클라우드 서비스에 액세스해야 한다고 가정합니다. 개발자는 myCloudServiceCred 시크릿을 포함하도록 {{site.data.keyword.ieam}} 서비스 정의를 업데이트합니다. 서비스 배치자는 서비스를 배치하기 위해 시크릿이 필요하다는 것을 확인하고 시크릿 관리자에서 기본 인증 신임 정보를 포함하는 cloudServiceXYZSecret이라는 시크릿을 알고 있습니다. 서비스 배치자는 myCloudServiceCreds라는 서비스의 시크릿이 cloudServiceXYZSecret라는 시크릿 관리자 시크릿의 신임 정보를 포함해야 함을 나타내기 위해 배치 정책(또는 패턴)을 업데이트합니다. 서비스 배치자가 배치 정책(또는 패턴)을 게시하면 {{site.data.keyword.ieam}}은(는) 배치 정책(또는 패턴)과 호환되는 모든 에지 노드에 cloudServiceXYZSecret의 세부사항을 안전하게 배치합니다.
