---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 既知の問題および制限  
{: #knownissues}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) の既知の問題および制限を以下に示します。

{{site.data.keyword.ieam}} オープン・ソース層の公開済みの問題の全リストについては、[Open Horizon リポジトリー](https://github.com/open-horizon/) の各リポジトリーの GitHub 問題を確認してください。

{:shortdesc}

## {{site.data.keyword.ieam}} {{site.data.keyword.version}} の既知の問題

{{site.data.keyword.ieam}} {{site.data.keyword.version}} の既知の問題および制限を以下に示します。

* {{site.data.keyword.ieam}} は、モデル管理システム (MMS) にアップロードされたデータに対してマルウェア・スキャンもウィルス・スキャンも実行しません。 MMS セキュリティーについて詳しくは、[セキュリティーおよびプライバシー](../OH/docs/user_management/security_privacy.md#malware)を参照してください。

* **edgeNodeFiles.sh** の **-f &lt;directory&gt;** フラグが意図された効力を持ちません。 代わりに、ファイルは現行ディレクトリーで収集されます。 詳しくは、[問題 2187](https://github.com/open-horizon/anax/issues/2187) を参照してください。 回避策としては、以下のようにコマンドを実行してください。

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* {{site.data.keyword.ieam}} インストールの一環として、インストールされた {{site.data.keyword.common_services}} のバージョンによっては、自動更新につながる短い有効期間で証明書が作成されている可能性があります。 以下の証明書問題が起こる可能性があります ([この手順で解決できます](cert_refresh.md))。
  * {{site.data.keyword.ieam}} 管理コンソールへのアクセス時に予期しない JSON 出力があり、「状況コード 502 で要求は失敗しました」というメッセージが表示される。
  * 証明書が更新されたときにエッジ・ノードが更新されず、{{site.data.keyword.ieam}} Hub への正常な通信を確実にするために手動での更新が必要になる。

* ローカル・データベースで {{site.data.keyword.ieam}} を使用する場合、Kubernetes scheduler を使用して手動または自動で **cssdb** ポッドを削除して再作成すると、Mongo データベースのデータが失われます。 データ損失を軽減するために、[バックアップとリカバリー](../admin/backup_recovery.md)の資料に従ってください。

* ローカル・データベースで {{site.data.keyword.ieam}} を使用する場合、**create-agbotdb-cluster** または **create-exchangedb-cluster** ジョブ・リソースが削除されると、ジョブは、各データベースを再実行し、再初期化し、結果としてデータが失われます。 データ損失を軽減するために、[バックアップとリカバリー](../admin/backup_recovery.md)の資料に従ってください。

* ローカル・データベースを使用する場合、postgres データベースの一方または両方が応答しなくなることがあります。 これを解決するには、応答しないデータベースのすべての標識とプロキシーを再始動します。 影響を受けたアプリケーションとカスタム・リソース (CR) を使用して、以下のコマンドを変更して実行します。
`oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` および `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` (標識交換の例: `oc rollout restart deploy ibm-edge-exchangedb-sentinel`)。

* どのアーキテクチャーの {{site.data.keyword.rhel}} でも、**hzn service log** コマンドを実行するとハングします。詳しくは、[問題 2826](https://github.com/open-horizon/anax/issues/2826) を参照してください。 この状態を回避するには、コンテナー・ログを取得します (tail に -f を指定することもできます)。

   ```
   docker logs <container>
   ```
   {: codeblock}


## {{site.data.keyword.ieam}} {{site.data.keyword.version}} の制限

* {{site.data.keyword.ieam}} の製品資料は、関係する地域用に翻訳されていますが、英語版は継続的に更新されています。 翻訳サイクルの合間では、英語版と翻訳版で矛盾する点がある可能性があります。 翻訳版が公開された後に矛盾する点が解決されたかどうかを確認するには、英語版をチェックしてください。

* Exchange 内のサービス、パターン、またはデプロイメント・ポリシーの **owner** または **public** 属性を変更した場合、それらのリソースにアクセスして変更を表示できるようになるまでに最長 5 分かかることがあります。 同様に、Exchange ユーザーに管理特権を付与した場合、その変更がすべての Exchange インスタンスに伝搬されるまで最長 5 分かかる場合があります。 時間を削減するには、Exchange の `config.json` ファイル内の `api.cache.resourcesTtlSeconds` の値をより低い値 (デフォルトは 300 秒) に設定します。ただし、それと引き換えにパフォーマンスは若干低下します。

* エージェントは、従属サービスに対して [Model Management System](../developing/model_management_system.md) (MMS) をサポートしません。

* シークレット・バインディングは、パターン内に定義された合意なしのサービスに対しては機能しません。
 
* マウントされるボリューム・ディレクトリーには 0700 の許可しかないため、エッジ・クラスター・エージェントは K3S v1.21.3+k3s1 をサポートしません。一時的解決策については、[Cannot write data to local PVC](https://github.com/k3s-io/k3s/issues/3704) を参照してください。
 
* 各 {{site.data.keyword.ieam}} エッジ・ノード・エージェントが、{{site.data.keyword.ieam}} 管理ハブとのすべてのネットワーク接続を開始します。管理ハブがエッジ・ノードへの接続を開始することはありません。したがって、管理ハブへの TCP 接続が可能な NAT ファイアウォールの背後にエッジ・ノードを置くことが可能です。ただし、現在のところ、エッジ・ノードは SOCKS プロキシーを介して管理ハブと通信することはできません。
  
* Fedora または SuSE でのエッジ・デバイスのインストールは、[エージェントの拡張手動インストールおよび登録](../installing/advanced_man_install.md)の方法でのみサポートされます。
