---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# API 키 작성
{: #prepare_for_edge_nodes}

이 컨텐츠는 API 키를 작성하는 방법과 에지 노드를 설정할 때 필요한 일부 파일 및 환경 변수 값을 수집하는 방법을 설명합니다. {{site.data.keyword.ieam}} 관리 허브 클러스터에 연결할 수 있는 호스트에서 다음 단계를 수행하십시오.

## 시작하기 전에

* 아직 **cloudctl**을 설치하지 않은 경우 이를 수행하기 위해 [cloudctl, oc, kubectl 설치](../cli/cloudctl_oc_cli.md)를 참조하십시오.
* **cloudctl**을 통해 관리 허브에 로그인하는 데 필요한 정보는 {{site.data.keyword.ieam}} 관리자에게 문의하십시오.

## 프로시저

LDAP 연결을 구성한 경우 추가된 사용자 신임 정보를 사용하여 로그인하고 API 키를 작성하거나 다음 명령으로 인쇄된 초기 관리 신임 정보를 사용할 수 있습니다.
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. `cloudctl`을 사용하여 {{site.data.keyword.ieam}} 관리 허브에 로그인하십시오. API 키를 작성할 사용자를 지정하십시오.

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. 에지 노드를 설정하는 각 사용자는 API 키가 있어야 합니다. 동일한 API 키를 사용하여 모든 에지 노드를 설정할 수 있습니다(에지 노드에 저장되지 않음). API 키를 작성하십시오.

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   명령 출력에서 키 값을 찾으십시오. 이는 **API 키**로 시작하는 행입니다. 나중에 시스템에서 조회할 수 없으므로 이후에 사용하도록 키 값을 저장하십시오.

3. 이 환경 변수 설정에 대한 도움을 받으려면 {{site.data.keyword.ieam}} 관리자에게 문의하십시오.

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## 다음 수행할 작업

에지 노드를 설정할 준비가 되었으면 [에지 노드 설치](../installing/installing_edge_nodes.md)의 단계를 수행하십시오.

