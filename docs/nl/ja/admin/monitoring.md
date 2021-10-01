---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# モニター

## {{site.data.keyword.ieam}} Grafana ダッシュボードへのアクセス 
{: #monitoring_dashboard}

1. [管理コンソールの使用](../console/accessing_ui.md)の手順に従って、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理コンソールに確実にアクセスできるようにします。
2. `https://<cluster-url>/grafana` にナビゲートして Grafana ダッシュボードを表示します。 
3. 左下隅にプロファイル・アイコンがあります。その上にカーソルを移動し、組織の切り替えオプションを選択します。 
4. `ibm-edge` 組織を選択します。別の名前空間に {{site.data.keyword.ieam}} をインストールした場合は、代わりにその組織を選択してください。
5. {{site.data.keyword.ieam}} インストールの全体的な CPU、メモリー、およびネットワーク圧力をモニターできるように、「{{site.data.keyword.ieam}}」を検索します。

   <img src="../images/edge/ieam_monitoring_dashboard.png" style="margin: 3%" alt="IEAM モニタリング・ダッシュボード" width="85%" height="85%" align="center">


# エッジ・ノードおよびサービスのモニター
{: #monitoring_edge_nodes_and_services}

[管理コンソールにログイン](../console/accessing_ui.md)し、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エッジ・ノードおよびサービスをモニターします。

* エッジ・ノードのモニター:
  * ノード・ダッシュボードが表示される最初のページであり、すべてのエッジ・ノードの状態を示すドーナツ・グラフが含まれています。
  * 特定の状態のノードをすべて表示するには、ドーナツ・グラフでその色をクリックします。 例えば、エラーがあるエッジ・ノードがある場合にそのすべて表示するには、**「エラーあり」**に使用されると凡例に示されている色をクリックします。
  * エラーがあるノードのリストが表示されます。 1 つのノードを詳しく調べて具体的なエラーを確認するには、そのノード名をクリックします。
  * 表示されるノード詳細ページの**「エッジ・エージェント・エラー」**セクションに、エラーのあるサービス、具体的なエラー・メッセージ、およびタイム・スタンプが示されます。
* エッジ・サービスのモニター:
  * **「サービス」**タブで、ドリルダウンするサービスをクリックします。エッジ・サービスの詳細ページが表示されます。
  * 詳細ページの**「デプロイメント」**セクションに、このサービスをエッジ・ノードにデプロイするポリシーおよびパターンが表示されます。
* 1 つのエッジ・ノード上のエッジ・サービスのモニター:
  * **「ノード」**タブで、リスト・ビューに切り替え、詳しく調べたいエッジ・ノードをクリックします。
  * ノード詳細ページの**「サービス」**セクションに、そのエッジ・ノードで現在実行中のエッジ・サービスが表示されます。
