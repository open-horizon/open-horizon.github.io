---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 멀티테넌시
{: #multit}

## {{site.data.keyword.edge_notm}}의 테넌트
{: #tenants}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서는 조직을 통해 멀티테넌시의 IT 개념을 지원합니다. 여기에서 각 테넌트는 고유한 조직을 갖고 있습니다. 조직은 리소스를 분리합니다. 따라서 각 조직 내 사용자는 다른 조직에서 리소스를 작성하거나 수정할 수 없습니다. 또한 리소스가 공용으로 표시되지 않는 한 조직의 리소스는 해당 조직의 사용자만 볼 수 있습니다.

### 일반적인 유스 케이스

두 가지 광범위한 유스 케이스가 {{site.data.keyword.ieam}}에서 멀티테넌시를 활용하는 데 사용됩니다.

* 엔터프라이즈에는 여러 비즈니스 단위가 있으며, 각 비즈니스 단위는 동일한 {{site.data.keyword.ieam}} 관리 허브에 있는 별도의 조직입니다. 각각의 비즈니스 단위에서 기본적으로 액세스할 수 없는 고유한 {{site.data.keyword.ieam}} 리소스 세트가 있는 별도의 조직이어야 하는 법적, 비즈니스 또는 기술적 이유를 고려하십시오. 별도의 조직인 경우에도 엔터프라이즈에는 공통 조직 관리자 그룹을 사용하여 모든 조직을 관리하는 옵션이 존재합니다.
* 엔터프라이즈는 자체 클라이언트를 위한 서비스로 {{site.data.keyword.ieam}}을 호스팅하며, 여기서 각 클라이언트는 관리 허브에서 하나 이상의 조직을 보유합니다. 이 경우 조직 관리자는 각 클라이언트에 대해 고유합니다.

선택한 유스 케이스는 {{site.data.keyword.ieam}} 및 [IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)(Identity and Access Manager)을 구성하는 방법을 판별합니다.

### {{site.data.keyword.ieam}} 사용자의 유형
{: #user-types}

{{site.data.keyword.ieam}}에서는 다음 사용자 역할을 지원합니다.

| **역할** | **액세스** |
|--------------|-----------------|
| **허브 관리자** | 필요에 따라 조직을 작성, 수정 및 삭제하고 각 조직 내에 조직 관리자를 작성하여 {{site.data.keyword.ieam}} 조직의 목록을 관리합니다. |
| **조직 관리자** | 하나 이상의 {{site.data.keyword.ieam}} 조직에 있는 리소스를 관리합니다. 조직 관리자는 리소스의 소유자가 아닌 경우에도 조직 내의 모든 리소스(사용자, 노드, 서비스, 정책 또는 패턴)를 작성하거나 보거나 수정할 수 있습니다. |
| **일반 사용자** | 조직 내에 노드, 서비스, 정책 및 패턴을 작성하고 작성한 리소스를 수정하거나 삭제합니다. 다른 사용자가 작성한 조직의 모든 서비스, 정책 및 패턴을 봅니다. |
{: caption="표 1. {{site.data.keyword.ieam}} 사용자 역할" caption-side="top"}

모든 {{site.data.keyword.ieam}} 역할의 설명에 대해서는 [역할 기반 액세스 제어](../user_management/rbac.md)를 참조하십시오.

## IAM 및 {{site.data.keyword.ieam}} 간의 관계
{: #iam-to-ieam}

IAM(Identity and Access Manager) 서비스는 {{site.data.keyword.ieam}}을 포함한 모든 Cloud Pak 기반 제품의 사용자를 관리합니다. IAM은 LDAP을 사용하여 사용자를 저장합니다. 각 IAM 사용자는 하나 이상의 IAM 팀의 구성원일 수 있습니다. 각 IAM 팀은 IAM 계정과 연관되므로 IAM 사용자는 간접적으로 하나 이상의 IAM 계정의 구성원일 수 있습니다. 세부사항은 [IAM 멀티테넌시](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html)를 참조하십시오.

{{site.data.keyword.ieam}} Exchange는 다른 {{site.data.keyword.ieam}} 컴포넌트에 대한 인증 및 권한 서비스를 제공합니다. Exchange는 사용자 인증을 IAM에 위임합니다. 즉, IAM 사용자 인증 정보가 Exchange에 전달되며 IAM에 의존하여 해당 인증 정보가 유효한지 여부를 판별합니다. 각 사용자 역할(허브 관리자, 조직 관리자 또는 일반 사용자)이 Exchange에 정의되고 사용자가 {{site.data.keyword.ieam}}에서 수행하도록 허용되는 조치를 판별합니다.

{{site.data.keyword.ieam}} Exchange의 각 조직은 IAM 계정과 연관됩니다. 따라서 IAM 계정의 IAM 사용자는 자동으로 해당 {{site.data.keyword.ieam}} 조직의 구성원이 됩니다. 이 규칙의 한 가지 예외는 {{site.data.keyword.ieam}} 허브 관리자 역할이 특정 조직 외부에 있는 것으로 간주된다는 것입니다. 따라서 허브 관리자 IAM 사용자가 어떤 IAM 계정에 있는지는 중요하지 않습니다.

IAM 및 {{site.data.keyword.ieam}} 간의 맵핑을 요약하면 다음과 같습니다.

| **IAM** | **관계** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| IAM 계정 | 맵핑 대상 | {{site.data.keyword.ieam}} 조직 |
| IAM 사용자 | 맵핑 대상 | {{site.data.keyword.ieam}} 사용자 |
| 역할에 상응하는 IAM이 없음 | 없음 | {{site.data.keyword.ieam}} 역할 |
{: caption="표 2. IAM - {{site.data.keyword.ieam}} 맵핑" caption-side="top"}

{{site.data.keyword.ieam}} 콘솔에 로그인하는 데 사용되는 인증 정보는 IAM 사용자 및 비밀번호입니다. {{site.data.keyword.ieam}} CLI(`hzn`)에 사용되는 인증 정보는 IAM API 키입니다.

## 초기 조직
{: #initial-org}

기본적으로 조직은 선택한 이름으로 {{site.data.keyword.ieam}} 설치 중에 작성됩니다. {{site.data.keyword.ieam}}의 다중 테넌트 기능이 필요하지 않은 경우 이 초기 조직에는 {{site.data.keyword.ieam}}만 사용해도 충분하며 이 페이지의 나머지를 건너뛸 수 있습니다.

## 허브 관리자 작성
{: #create-hub-admin}

{{site.data.keyword.ieam}} 멀티테넌시를 사용하는 첫 번째 단계는 조직을 작성하고 관리할 수 있는 하나 이상의 허브 관리자를 작성하는 것입니다. 이를 수행하기 전에 허브 관리자 역할이 지정될 IAM 계정 및 사용자를 작성하거나 선택해야 합니다.

1. `cloudctl`을 사용하여 클러스터 관리자로 {{site.data.keyword.ieam}} 관리 허브에 로그인하십시오. (`cloudctl`을 아직 설치하지 않은 경우 지시사항은 [cloudctl, kubectl 및 oc 설치](../cli/cloudctl_oc_cli.md)를 참조하십시오.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. LDAP 인스턴스를 IAM에 아직 연결하지 않은 경우 [LDAP 디렉토리에 연결](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)에 따라 지금 수행하십시오.

3. 허브 관리자는 IAM 계정에 있어야 합니다. (어떤 계정이든 문제가 되지 않습니다.) 허브 관리자가 소속될 IAM 계정이 아직 존재하지 않을 경우 해당 계정을 작성하십시오.

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. {{site.data.keyword.ieam}} 관리자 역할 전용 LDAP 사용자를 작성하거나 선택하십시오. {{site.data.keyword.ieam}} 허브 관리자 및 {{site.data.keyword.ieam}} 조직 관리자(또는 일반 {{site.data.keyword.ieam}} 사용자) 양쪽에 동일한 사용자를 사용하지 마십시오.

5. 사용자를 IAM으로 가져오십시오.

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>    cloudctl iam user-import -u $HUB_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. IAM 사용자에 허브 관리자 역할을 지정하십시오.

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>    export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW    export HZN_EXCHANGE_URL=<the URL of your exchange>    hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. 사용자에게 허브 관리자 사용자 역할이 있는지 확인하십시오. 다음 명령의 출력에 `"hubAdmin": true`가 표시되어야 합니다.

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### {{site.data.keyword.ieam}} CLI로 허브 관리자 사용
{: #verify-hub-admin}

허브 관리자에 대한 API 키를 작성하고 허브 관리자 기능이 있는지 확인하십시오.

1. `cloudctl`을 사용하여 허브 관리자로 {{site.data.keyword.ieam}} 관리 허브에 로그인하십시오.

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. 허브 관리자에 대한 API 키를 작성하십시오.

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   **API 키**로 시작하는 명령 출력 행에서 API 키 값을 찾으십시오. 나중에 시스템에서 조회할 수 없으므로 이후에 사용하도록 키 값을 안전한 위치에 저장하십시오. 또한 후속 명령을 위해 이 변수에 설정하십시오.

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 관리 허브의 모든 조직을 표시하십시오. 설치 중 작성된 초기 조직과 **root** 및 **IBM** 조직이 표시되어야 합니다.

   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    hzn exchange org list -o root
   ```
   {: codeblock}

4. 허브 관리자 IAM 사용자 및 비밀번호로 [{{site.data.keyword.ieam}} 관리 콘솔](../console/accessing_ui.md)에 로그인하십시오. 로그인 인증 정보에 허브 관리자 역할이 포함되어 있기 때문에 조직 관리 콘솔이 표시됩니다. 이 콘솔을 사용하여 조직을 보고 관리하고 추가할 수 있습니다. 또는 다음 절의 CLI를 사용하여 조직을 추가할 수 있습니다.

## CLI를 사용하여 조직 작성
{: #create-org}

{{site.data.keyword.ieam}} 조직 관리 콘솔을 사용하는 대신 CLI를 사용하여 조직을 작성할 수 있습니다. 조직을 작성하기 위한 전제조건은 조직과 연관될 IAM 계정을 작성하거나 선택하는 것입니다. 다른 전제조건은 조직 관리자 역할이 지정될 IAM 사용자를 작성하거나 선택하는 것입니다.

**참고**: 조직 이름은 밑줄(_), 쉼표(,), 공백( ), 작은따옴표(') 또는 물음표(?)를 포함할 수 없습니다..

다음 단계를 수행하십시오.

1. 아직 수행하지 않은 경우 이전 절의 단계를 수행하여 허브 관리자를 작성하십시오. 허브 관리자 API 키가 다음 변수에 설정되었는지 확인하십시오.

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. `cloudctl`을 사용하여 클러스터 관리자로 {{site.data.keyword.ieam}} 관리 허브에 로그인하고 새 {{site.data.keyword.ieam}} 조직이 연관될 IAM 계정을 작성하십시오. (`cloudctl`을 아직 설치하지 않은 경우 [cloudctl, kubectl 및 oc 설치](../cli/cloudctl_oc_cli.md)를 참조하십시오.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation    NEW_ORG_ID=<new organization name>    IAM_ACCOUNT_NAME="$NEW_ORG_ID"    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. 조직 관리자 역할이 지정될 LDAP 사용자를 작성하거나 선택하여 IAM으로 가져오십시오. 허브 관리자를 조직 관리자로 사용할 수는 없지만 둘 이상의 IAM 계정에서 동일한 조직 관리자를 사용할 수 있습니다. 따라서 이 기능을 통해 둘 이상의 {{site.data.keyword.ieam}} 조직을 관리할 수 있습니다.

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>    cloudctl iam user-import -u $ORG_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. 다음 환경 변수를 설정하고 {{site.data.keyword.ieam}} 조직을 작성한 후 존재하는지 확인하십시오.
   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    export HZN_EXCHANGE_URL=<URL of your exchange>    hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID    hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID    hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. 조직 관리자 사용자 역할을 이전에 선택한 IAM 사용자에게 지정하고 사용자가 {{site.data.keyword.ieam}} Exchange에서 조직 관리자 역할로 작성되었는지 확인하십시오.

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"    hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   사용자 목록에 다음이 표시되어야 합니다. `"admin": true`

<div class="note"><span class="notetitle">참고:</span> 여러 조직을 작성하고 동일한 조직 관리자가 모든 조직을 관리하도록 하려면 이 절을 통해 매번 `ORG_ADMIN_USER`에 동일한 값을 사용하십시오.</div>

이제 조직 관리자가 [{{site.data.keyword.ieam}} 관리 콘솔](../console/accessing_ui.md)을 사용하여 이 조직 내의 {{site.data.keyword.ieam}} 리소스를 관리할 수 있습니다.

### 조직 관리자가 CLI를 사용하도록 설정

조직 관리자가 `hzn exchange` 명령을 사용하여 CLI를 통해 {{site.data.keyword.ieam}} 리소스를 관리하도록 하려면 다음 작업을 수행해야 합니다.

1. `cloudctl`을 사용하여 {{site.data.keyword.ieam}} 관리 허브에 로그인하고 API 키를 작성하십시오.

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   **API 키**로 시작하는 명령 출력 행에서 API 키 값을 찾으십시오. 나중에 시스템에서 조회할 수 없으므로 이후에 사용하도록 키 값을 안전한 위치에 저장하십시오. 또한 후속 명령을 위해 이 변수에 설정하십시오.

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **팁:** 나중에 이 사용자를 추가 IAM 계정에 추가하는 경우 각 계정에 대한 API 키를 작성할 필요가 없습니다. 동일한 API 키가 이 사용자가 구성원인 모든 IAM 계정에서 작동하므로 이 사용자가 구성원인 모든 {{site.data.keyword.ieam}} 조직에서 작동합니다.

2. `hzn exchange` 명령을 사용하여 API 키가 작동하는지 확인하십시오.

   ```bash
   export HZN_ORG_ID=<organization id>    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY    hzn exchange user list
   ```
   {: codeblock}


새 조직을 사용할 준비가 되었습니다. 이 조직의 최대 에지 노드 수를 설정하거나 기본 에지 노드 하트비트 설정을 사용자 정의하려면 [조직 구성](#org-config)을 참조하십시오.

## 조직 내 비관리 사용자
{: #org-users}

IAM 사용자(`MEMBER`로)를 해당 IAM 계정으로 가져오고 온보딩하여 새 사용자를 조직에 추가할 수 있습니다. 필요한 경우 자동으로 수행되므로 명시적으로 {{site.data.keyword.ieam}} Exchange에 사용자를 추가할 필요가 없습니다.

그러면 사용자가 [{{site.data.keyword.ieam}} 관리 콘솔](../console/accessing_ui.md)을 사용할 수 있습니다. 사용자가 `hzn exchange` CLI를 사용하려면 다음을 수행해야 합니다.

1. `cloudctl`을 사용하여 {{site.data.keyword.ieam}} 관리 허브에 로그인하고 API 키를 작성하십시오.

   ```bash
   IAM_USER=<iam user>    cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   **API 키**로 시작하는 명령 출력 행에서 API 키 값을 찾으십시오. 나중에 시스템에서 조회할 수 없으므로 이후에 사용하도록 키 값을 안전한 위치에 저장하십시오. 또한 후속 명령을 위해 이 변수에 설정하십시오.

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 다음 환경 변수를 설정하고 사용자를 확인하십시오.

```bash
export HZN_ORG_ID=<organization-id> export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY hzn exchange user list
```
{: codeblock}

## IBM 조직
{: #ibm-org}

IBM 조직은 모든 조직의 모든 사용자가 사용할 수 있는 기술 예제로 의도된 사전 정의된 서비스와 패턴을 제공하는 고유 조직입니다. IBM 조직은 {{site.data.keyword.ieam}} 관리 허브가 설치될 때 자동으로 작성됩니다.

**참고**: IBM 조직의 리소스는 공용이지만 IBM 조직에서 {{site.data.keyword.ieam}} 관리 허브에 모든 공용 컨텐츠를 보유하도록 의도된 것은 아닙니다.

## 조직 구성
{: #org-config}

모든 {{site.data.keyword.ieam}} 조직에는 다음 설정이 있습니다. 대개의 경우 이러한 설정은 기본값으로 충분합니다. 설정을 사용자 정의하도록 선택하는 경우 `hzn exchange org update -h` 명령을 실행하여 사용할 수 있는 명령 플래그를 보십시오.

| **설정** | **설명** |
|--------------|-----------------|
| `description` | 조직에 대한 설명입니다. |
| `label` | 조직의 이름입니다. 이 값은 {{site.data.keyword.ieam}} 관리 콘솔에 조직 이름을 표시하는 데 사용됩니다. |
| `heartbeatIntervals` | 지침을 위해 조직의 에지 노드 에이전트가 관리 허브를 폴링하는 빈도입니다. 세부사항은 다음 절을 참조하십시오. |
| `limits` | 이 조직에 대한 한계입니다. 현재 유일한 한계는 이 조직에서 허용되는 최대 에지 노드 수인 `maxNodes`입니다. 단일 {{site.data.keyword.ieam}} 관리 허브에서 지원할 수 있는 총 에지 노드 수에 대한 실질적 한계가 있습니다. 허브 관리자는 이 설정을 통해 각 조직이 보유할 수 있는 노드 수를 제한하여 하나의 조직이 모든 용량을 사용하지 않도록 할 수 있습니다. `0` 값은 한계가 없음을 의미합니다. |
{: caption="표 3. 조직 설정" caption-side="top"}

### 에이전트 하트비트 폴링 간격
{: #agent-hb}

모든 에지 노드에 설치된 {{site.data.keyword.ieam}} 에이전트는 주기적으로 관리 허브에 하트비트를 전송하여 관리 허브에서 해당 에이전트가 여전히 실행 중이고 연결되어 있음을 파악하고 지침을 수신하도록 합니다. 대규모 환경에서만 이러한 설정을 변경하면 됩니다.

하트비트 간격은 에이전트가 관리 허브에 대한 하트비트 사이에 대기하는 시간입니다. 이 간격은 응답을 최적화하고 관리 허브의 로드를 줄이기 위해 시간 경과에 따라 자동으로 조정됩니다. 간격 조정은 다음 세 가지 설정으로 제어됩니다.

| **설정** | **설명**|
|-------------|----------------|
| `minInterval` | 관리 허브에 대한 하트비트 사이에 에이전트가 대기해야 하는 가장 짧은 시간(초)입니다. 에이전트가 등록되면 이 간격에서 폴링이 시작됩니다. 간격은 이 값 미만이 되지 않습니다. `0` 값은 기본값을 사용함을 의미합니다. |
| `maxInterval` | 관리 허브에 대한 하트비트 사이에 에이전트가 대기해야 하는 가장 긴 시간(초)입니다. `0` 값은 기본값을 사용함을 의미합니다. |
| `intervalAdjustment` | 에이전트가 간격을 늘릴 수 있음을 감지하는 경우 현재 하트비트 간격에 추가할 시간(초)입니다. 관리 허브에 하트비트를 전송한 후에 한동안 지침을 수신하지 않으면 최대 하트비트 간격에 도달할 때까지 하트비트 간격이 점차적으로 증가합니다. 마찬가지로, 지침이 수신되면 후속 지침이 빠르게 처리되는지 확인하기 위해 하트비트 간격이 감소합니다. `0` 값은 기본값을 사용함을 의미합니다. |
{: caption="표 4. 하트비트 간격 설정" caption-side="top"}

조직의 하트비트 폴링 간격 설정은 명시적으로 하트비트 간격이 구성되지 않은 노드에 적용됩니다. 노드가 명시적으로 하트비트 간격 설정을 설정했는지 확인하려면 `hzn exchange node list <node id>`를 사용하십시오.

대규모 환경에서 설정을 변경하는 방법에 대한 자세한 정보는 [스케일링 구성](../hub/configuration.md#scale)을 참조하십시오.
