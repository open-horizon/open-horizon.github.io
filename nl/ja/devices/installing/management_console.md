---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} コンソールの使用
{: #accessing_ui}

コンソールを使用して、エッジ・コンピューティング管理機能を実行します。 
 
## {{site.data.keyword.edge_notm}} コンソールへのナビゲート

1. `https://<cluster-url>/edge` を参照して {{site.data.keyword.edge_notm}} コンソールにナビゲートします。ここで、`<cluster-url>` はクラスターの外部 Ingress です。
2. ユーザー資格情報を入力します。 {{site.data.keyword.mcm}} ログイン・ページが表示されます。
3. ブラウザーのアドレス・バーで、URL の末尾から `/multicloud/welcome` を削除し、`/edge` を追加してから **Enter** を押します。 {{site.data.keyword.edge_notm}} ページが表示されます。

## サポートされるブラウザー

{{site.data.keyword.edge_notm}} は、以下のブラウザーでテスト済みです。

|プラットフォーム|サポートされるブラウザー|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - Windows 用の最新バージョン</li><li>Google Chrome - Windows 用の最新バージョン</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - Mac 用の最新バージョン</li><li>Google Chrome - Mac 用の最新バージョン</li></ul>|
{: caption="表 1. {{site.data.keyword.edge_notm}} でサポートされるブラウザー" caption-side="top"}


## {{site.data.keyword.edge_notm}} コンソールの探索
{: #exploring-management-console}

{{site.data.keyword.edge_notm}} コンソールの機能には以下のものがあります。

* 強固なサポートのための周辺サイトへのリンクのあるユーザー・フレンドリーなオンボーディング
* 幅広い可視性および管理機能
  * ノード状況、アーキテクチャー、およびエラー情報を含む、包括的なチャート・ビュー
  * 解決サポートのためのリンクを伴うエラー詳細
  * 以下に関する情報を含むコンテンツの検出およびフィルタリング 
    * 所有者
    * アーキテクチャー 
    * ハートビート (例えば、最近 10 分間、今日など)
    * ノード状態 (アクティブ、非アクティブ、エラーありなど)
    * デプロイメントのタイプ (ポリシーまたはパターン)
  * 以下のような、Exchange エッジ・ノードに関する有用な詳細
    * プロパティー
    * 制約 
    * デプロイメント
    * アクティブ・サービス

* 堅固な表示機能

  * 以下による迅速な検出およびフィルタリングの機能 
    * 所有者
    * アーキテクチャー
    * バージョン
    * パブリック (true または false)
  * リストまたはカード・サービス表示
  * 名前を共有するグループ化されたサービス
  * Exchange 内の各サービスの以下を含む詳細 
    * プロパティー
    * 制約
    * デプロイメント
    * サービス変数
    * サービスの依存関係
  
* デプロイメント・ポリシー管理

  * 以下による迅速な検出およびフィルタリングの機能
    * ポリシー ID
    * 所有者
    * ラベル
  * Exchange からの任意のサービスのデプロイ
  * デプロイメント・ポリシーへのプロパティーの追加
  * 式を作成するための制約ビルダー 
  * 制約を直接 JSON に書き込むための拡張モード
  * ロールバック・デプロイメントのバージョンとノード・ヘルス設定を調整する機能
  * 以下を含むポリシー詳細の表示および編集
    * サービスおよびデプロイメントのプロパティー
    * 制約
    * ロールバック
    * ノード・ヘルス設定
  
