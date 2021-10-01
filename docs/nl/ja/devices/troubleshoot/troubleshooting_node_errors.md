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

# ノード・エラーのトラブルシューティング
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} は、{{site.data.keyword.gui}} で表示可能なイベント・ログのサブセットを Exchange に公開します。これらのエラーは、トラブルシューティングのガイダンスにリンクされています。{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

このエラーは、サービス定義で参照されているサービス・イメージがイメージ・リポジトリーに存在しない場合に発生します。このエラーを解決するには、以下のようにします。

1. **-I** フラグを付けずにサービスをリパブリッシュします。
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. サービス・イメージをイメージ・リポジトリーに直接プッシュします。 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

このエラーは、サービス定義のデプロイメント構成で、ルート保護ファイルへのバインドが指定されている場合に発生します。このエラーを解決するには、以下のようにします。

1. コンテナーをルート保護されていないファイルにバインドします。
2. ファイルのアクセス権を変更して、ユーザーがファイルを読み書きできるようにします。

## error_start_container
{: #esc}

このエラーは、Docker がサービス・コンテナーを開始したときにエラーを検出した場合に発生します。エラー・メッセージには、コンテナーの開始が失敗した理由を示す詳細が含まれていることがあります。エラーの解決ステップは、エラーによって異なります。以下のエラーが発生することがあります。

1. デバイスは、デプロイメント構成によって指定された公開ポートを既に使用しています。エラーを解決するには、次のようにします。 

    - サービス・コンテナー・ポートに別のポートをマップします。表示されたポート番号は、サービス・ポート番号と一致する必要はありません。
    - 同じポートを使用しているプログラムを停止します。

2. デプロイメント構成で指定された公開ポートのポート番号が有効ではありません。ポート番号は、1 から 65535 の範囲の数値でなければなりません。
3. デプロイメント構成のボリューム名は、有効なファイル・パスではありません。ボリューム・パスは、(相対パスではなく) 絶対パスで指定する必要があります。 

## 追加情報

詳しくは、以下を参照してください。
  * [{{site.data.keyword.edge_devices_notm}} トラブルシューティング・ガイド](../troubleshoot/troubleshooting.md)
