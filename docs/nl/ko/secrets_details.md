---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# 시크릿을 사용하여 서비스 개발
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets"> 

# 시크릿 관리자 세부사항
{: #secrets_details}

시크릿 관리자는 인증 신임 정보 또는 암호화 키와 같은 민감한 정보에 대한 보안 스토리지를 제공합니다. 이러한 시크릿은 {{site.data.keyword.ieam}}에 의해 안전하게 배치되므로 시크릿을 수신하도록 구성된 서비스만 해당 서비스에 액세스할 수 있습니다. [Hello Secret World 예제](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)는 에지 서비스의 시크릿을 활용하는 방법에 대한 개요를 제공합니다.

{{site.data.keyword.ieam}}에서는 [Hashicorp Vault](https://www.vaultproject.io/)를 시크릿 관리자로 사용할 수 있도록 지원합니다. hzn CLI를 사용하여 작성된 시크릿은 [KV V2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2)을 사용하여 Vault 시크릿에 맵핑됩니다. 이는 모든 {{site.data.keyword.ieam}} 시크릿의 세부사항이 키 및 값으로 구성됨을 의미합니다. 둘 다 시크릿 세부사항의 일부로 저장되며, 둘 다 문자열 값으로 설정할 수 있습니다. 이 기능의 일반적인 사용법은 키 및 민감한 정보에 대한 시크릿 유형을 값으로 제공하는 것입니다. 예를 들어, 키를 "basicauth"로 설정하고 값을 "user:password"로 설정합니다. 그렇게 함으로써 서비스 개발자는 시크릿 유형을 조사하여 서비스 코드가 값을 올바르게 처리할 수 있도록 합니다.

시크릿 관리자의 시크릿 이름은 서비스 구현에서 알 수 없습니다. 시크릿 이름을 사용하여 Vault에서 서비스 구현으로 정보를 전달할 수 없습니다.

시크릿은 시크릿 이름 앞에 openhorizon과 사용자의 조직을 붙여 KV V2 Secrets Engine에 저장됩니다. 이렇게 하면 {{site.data.keyword.ieam}} 사용자가 만든 시크릿이 다른 통합에 의해 Vault의 다른 사용과 격리되고 다중 테넌트 격리가 유지됩니다.

시크릿 이름은 {{site.data.keyword.ieam}} 조직 관리자(또는 사용자 개인 시크릿을 사용하는 경우 사용자)가 관리합니다. Vault 액세스 제어 목록(ACL)은 {{site.data.keyword.ieam}} 사용자가 관리할 수 있는 시크릿을 제어합니다. 이는 사용자 인증을 {{site.data.keyword.ieam}} 교환에 위임하는 Vault 인증 플러그인을 통해 수행됩니다. 사용자를 인증하면 Vault의 인증 플러그인이 이 사용자에 특정한 ACL 정책 세트를 작성합니다. 교환에서 관리 권한이 있는 사용자는 다음을 수행할 수 있습니다.
- 조직 전체의 모든 시크릿을 추가하고 제거하고 읽고 나열합니다.
- 해당 사용자에 특정한 모든 시크릿을 추가하고 제거하고 읽고 나열합니다.
- 조직에 있는 다른 사용자의 사용자 개인 시크릿을 제거하고 나열하지만 해당 시크릿을 추가하거나 읽을 수는 없습니다.

관리 권한이 없는 사용자는 다음을 수행합니다.
- 조직 전반의 모든 시크릿을 나열하지만 추가, 제거 또는 읽을 수 없습니다.
- 해당 사용자에 특정한 모든 시크릿을 추가하고 제거하고 읽고 나열합니다.

또한 {{site.data.keyword.ieam}} Agbot에는 에지 노드에 배치할 수 있도록 시크릿에 대한 액세스 권한이 있습니다. Agbot은 Vault에 대한 갱신 가능한 로그인을 유지보수하고 목적에 맞는 ACL 정책을 제공받습니다. Agbot은 다음을 수행할 수 있습니다.
- 조직 전반의 시크릿 및 조직에서 사용자 개인 시크릿을 읽을 수 있지만 시크릿을 추가, 제거 또는 나열할 수는 없습니다.

Exchange 루트 사용자 및 Exchange 허브 관리자는 Vault에 권한이 없습니다. 이러한 역할에 대한 자세한 정보는 [역할 기반 액세스 제어](../user_management/rbac.html)를 참조하십시오.
