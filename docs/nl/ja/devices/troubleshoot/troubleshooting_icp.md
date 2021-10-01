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

# {{site.data.keyword.icp_notm}} 環境におけるトラブルシューティングのヒント
{: #troubleshooting_icp}

{{site.data.keyword.edge_devices_notm}} に関連する {{site.data.keyword.icp_notm}} 環境の一般的な問題のトラブルシューティングを行う際は、以下の内容を確認してください。各質問のヒントとガイドは、一般的な問題の解決と根本原因の特定のための情報取得に役立ちます。
{:shortdesc}

   * [ユーザーの {{site.data.keyword.edge_devices_notm}} 資格情報は、{{site.data.keyword.icp_notm}} 環境で使用できるように正しく構成されていますか?](#setup_correct)

### ユーザーの {{site.data.keyword.edge_devices_notm}} 資格情報は、{{site.data.keyword.icp_notm}} 環境で使用できるように正しく構成されていますか?
{: #setup_correct}

この環境で {{site.data.keyword.edge_devices_notm}} の任意のアクションを実行するには、{{site.data.keyword.icp_notm}} ユーザー・アカウントが必要です。 また、そのアカウントから作成された API 鍵も必要です。

この環境で {{site.data.keyword.edge_devices_notm}} 資格情報を確認するには、次のコマンドを実行します。

   ```
   hzn exchange user list
   ```
   {: codeblock}

Exchange から返された JSON 形式の項目に 1 人以上のユーザーが示されている場合、{{site.data.keyword.edge_devices_notm}} 資格情報は適切に構成されています。

エラー応答が返された場合は、資格情報のセットアップをトラブルシューティングするためのステップを行います。

エラー・メッセージが正しくない API 鍵を示している場合は、以下のコマンドを使用する新しい API 鍵を作成できます。

**注:** 最初に、次のコマンドで、先頭に `$` が付いたすべての環境変数に適切な値を設定します。

   ```
   cloudctl login -a $ICP_URL -u $USER -p $PW -n kube-public --skip-ssl-validation
   cloudctl iam api-key-create "$KEY_NAME" -d "$KEY_DESC"
   ```
   {: codeblock}

証明書が無効であることをエラー・メッセージが示している場合は、次のコマンドを使用して新しい自己署名証明書を作成します。

   ```
   kubectl -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" | base64 --decode > icp.crt
   ```
   {: codeblock}

次に、この証明書を信頼するようにオペレーティング・システムに指示します。Linux マシンでは、次のコマンドを実行します。

   ```
   sudo cp icp.crt /usr/local/share/ca-certificates &&  sudo update-ca-certificates
   ````
   {: codeblock}

MacOS マシンでは、次のコマンドを実行します。

   ```
   sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain icp.crt
   ```
   {: codeblock}
