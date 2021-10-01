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

# API 鍵の作成
{: #prepare_for_edge_nodes}

ここでは、API 鍵を作成し、エッジ・ノードのセットアップ時に必要になるファイルおよび環境変数の値を収集する方法について説明します。 これらのステップは、{{site.data.keyword.ieam}} 管理ハブ・クラスターに接続できるホストで実行します。

## 始める前に

* まだ **cloudctl** がインストールされていない場合は、『[cloudctl、oc、および kubectl のインストール](../cli/cloudctl_oc_cli.md)』を参照してインストールします。
* {{site.data.keyword.ieam}} 管理者に連絡して、**cloudctl** を介して管理ハブにログインするために必要な情報を入手します。

## 手順

LDAP 接続を構成済みの場合、追加されたユーザー資格情報を使用してログインおよび API 鍵の作成を行うことも、以下のコマンドで出力される初期管理者資格情報を使用することもできます。
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. `cloudctl` を使用して {{site.data.keyword.ieam}} 管理ハブにログインします。 以下のように、API 鍵を作成する対象のユーザーを指定します。

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. エッジ・ノードをセットアップする各ユーザーに API 鍵が必要です。 同じ API 鍵を使用してすべてのエッジ・ノードをセットアップできます (エッジ・ノードには保存されません)。 次のように API 鍵を作成します。

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   コマンドの出力で鍵の値を見つけます。これは、**API Key** で始まっている行です。 後からシステムで鍵の値を照会することはできないため、後の使用に備えて鍵の値を保存します。

3. 以下の環境変数を設定するために、{{site.data.keyword.ieam}} 管理者に連絡して値を入手します。

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')
  export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/
  echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## 次の作業

エッジ・ノードをセットアップする準備ができたら、[エッジ・ノードのインストール](../installing/installing_edge_nodes.md)に従います。

