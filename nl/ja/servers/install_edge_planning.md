---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_servers_notm}} のインストールの準備
{: #edge_planning}

{{site.data.keyword.icp_server}} をインストールする前に、{{site.data.keyword.mgmt_hub}} を有効にして、{{site.data.keyword.edge_servers_notm}} を構成し、ご使用のシステムが以下の要件を満たしていることを確認してください。 これらの要件によって、予定するエッジ・サーバーの最低限必要なコンポーネントと構成が示されます。
{:shortdesc}

これらの要件により、エッジ・サーバーの管理に使用する予定の {{site.data.keyword.mgmt_hub}} クラスターの最小構成設定も示されます。

この情報を使用すると、エッジ・コンピューティング・トポロジーおよび {{site.data.keyword.icp_server}} と {{site.data.keyword.mgmt_hub}} 全体のセットアップのリソース要件を計画する際に役立ちます。

   * [ハードウェア要件](#prereq_hard)
   * [サポートされる IaaS](#prereq_iaas)
   * [サポートされる環境](#prereq_env)
   * [必要なポート](#prereq_ports)
   * [クラスターのサイジングの考慮事項](#cluster)

## ハードウェア要件
{: #prereq_hard}

ご使用のエッジ・コンピューティング・トポロジーの管理ノードをサイジングする場合は、クラスターのサイズ設定に役立つ単一ノード・デプロイメントまたはマルチノード・デプロイメントのための {{site.data.keyword.icp_server}} サイジング・ガイドラインを使用してください。 詳しくは、『[{{site.data.keyword.icp_server}} クラスターのサイジング![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)』を参照してください。

以下のエッジ・サーバー要件は、{{site.data.keyword.edge_profile}} を使用してリモート・オペレーション・センターにデプロイされる {{site.data.keyword.icp_server}} インスタンスにのみ適用されます。

| 要件 | ノード (ブート、マスター、管理) | ワーカー・ノード |
|-----------------|-----------------------------|--------------|
| ホストの数       　 | 1 | 1 |
| コア | 4 以上 | 4 以上 |
| CPU | 2.4 GHz 以上 | 2.4 GHz 以上 |
| RAM | 8 GB 以上 | 8 GB 以上 |
| インストールのための空きディスク・スペース | 150 GB 以上 | |
{: caption="表 1. エッジ・サーバー・クラスター・ハードウェアの最小要件" caption-side="top"}

注: ストレージが 150 GB の場合、中央データ・センターへのネットワークが切断した場合でも、ログとイベント・データを 3 日間まで保存できます。

## サポートされる IaaS
{: #prereq_iaas}

以下の表は、エッジ・サービスに使用できる、サポート対象の Infrastructure as a Service (IaaS) を示します。

| IaaS | バージョン |
|------|---------|
|エッジ・サーバー・ロケーションで使用するための Nutanix NX-3000 シリーズ | NX-3155G-G6 |
|エッジ・サーバーで使用するために Nutanix によって提供される IBM Hyperconverged Systems | CS821 および CS822|
{: caption="表 2. {{site.data.keyword.edge_servers_notm}} のサポート対象の IaaS" caption-side="top"}

詳しくは、[Nutanix によって提供される IBM Hyperconverged Systems の PDF ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/downloads/cas/BZP46MAV)を参照してください。

## サポートされる環境
{: #prereq_env}

以下の表は、エッジ・サーバーで使用できる追加の Nutanix 構成済みシステムを示します。

| LOE サイト・タイプ | ノード・タイプ | クラスター・サイズ | ノード当たりのコア数 (合計) | ノード当たりの論理プロセッサー数 (合計)	| ノード当たりのメモリー (GB) (合計) | ディスク・グループ当たりのキャッシュ・ディスク・サイズ (GB) |	ノード当たりのキャッシュ・ディスクの数	| ノード当たりのキャッシュ・ディスク・サイズ (GB)	| ストレージの合計クラスター・プール・サイズ (すべてのフラッシュ) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| 小規模	| NX-3155G-G6	| 3 ノード	| 24 (72)	| 48 (144)	| 256 (768)	| N/A	| N/A	| N/A	| 8 TB |
| 中規模 | NX-3155G-G6 | 3 ノード | 24 (72)	| 48 (144)	| 512 (1,536)	| N/A	| N/A	| N/A	| 45 TB |
| 大規模	| NX-3155G-G6	| 4 ノード	| 24 (96)	| 48 (192)	| 512 (2,048)	| N/A	| N/A	| N/A	| 60 TB |
{: caption="表 3. Nutanix NX-3000 シリーズでサポートされる構成" caption-side="top"}

| LOE サイト・タイプ	| ノード・タイプ	| クラスター・サイズ |	ノード当たりのコア数 (合計) | ノード当たりの論理プロセッサー数 (合計)	| ノード当たりのメモリー (GB) (合計)	| ディスク・グループ当たりのキャッシュ・ディスク・サイズ (GB) | ノード当たりのキャッシュ・ディスクの数	| ノード当たりのキャッシュ・ディスク・サイズ (GB)	| ストレージの合計クラスター・プール・サイズ (すべてのフラッシュ) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| 小規模	| CS821 (2 ソケット、1U) | 3 ノード | 20 (60)	| 80 (240) | 256 (768) | N/A	| N/A	| N/A	| 8 TB |
| 中規模 | CS822 (2 ソケット、2U) | 3 ノード	| 22 (66)	| 88 (264) | 512 (1,536) | N/A | N/A | N/A | 45 TB |
| 大規模	| CS822 (2 ソケット、2U) | 4 ノード | 22 (88) | 88 (352) | 512 (2,048) | N/A | N/A | N/A | 60 TB |
{: caption="表 4. Nutanix によって提供される IBM Hyperconverged Systems" caption-side="top"}

詳しくは、[IBM Hyperconverged Systems that are powered by Nutanix ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/downloads/cas/BZP46MAV)を参照してください。

## 必要なポート
{: #prereq_ports}

標準クラスター構成でリモート・エッジ・サーバーをデプロイする予定の場合、ノードのポート要件は、{{site.data.keyword.icp_server}} をデプロイする際のポート要件と同じです。 これらの要件について詳しくは、『[必須ポート![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html)』を参照してください。 ハブ・クラスターに必要なポートについては、「_{{site.data.keyword.mcm_core_notm}} の必須ポート_」のセクションを参照してください。

{{site.data.keyword.edge_profile}} を使用してエッジ・サーバーを構成する予定の場合は、以下のポートを使用可能にします。

| ポート | プロトコル | 要件 |
|------|----------|-------------|
| NA | IPv4 | IP-in-IP を使用した Calico (calico_ipip_mode: 必須) |
| 179 | TCP	| Calico では必須  (network_type:calico) |
| 500 | TCP および UDP	| IPSec (ipsec.enabled: true、calico_ipip_mode: 必須) |
| 2380 | TCP | etcd が有効な場合には必須 |
| 4001 | TCP | etcd が有効な場合には必須 |
| 4500 | UDP | IPSec (ipsec.enabled: true) |
| 9091 | TCP | Calico (network_type:calico) |
| 9099 | TCP | Calico (network_type:calico) |
| 10248:10252 | TCP	| Kubernetes では必須 |
| 30000:32767 | TCP および UDP | Kubernetes では必須 |
{: caption="表 5. {{site.data.keyword.edge_servers_notm}} の必須ポート" caption-side="top"}

注: ポート 30000:32767 には外部アクセスがあります。 これらのポートは、Kubernetes サービス・タイプを NodePort に設定した場合にのみ開く必要があります。

## クラスターのサイジングの考慮事項
{: #cluster}

{{site.data.keyword.edge_servers_notm}} の場合、ハブ・クラスターが一般的な標準の {{site.data.keyword.icp_server}} ホスト環境です。 この環境を使用すると、中央の一か所から提供する必要がある、または提供したい他のコンピュート・ワークロードもホストできます。 {{site.data.keyword.mcm_core_notm}} クラスター、および環境でホストする予定の追加ワークロードのホストに十分なリソースを確保するように、ハブ・クラスター環境をサイズ設定する必要があります。 標準の {{site.data.keyword.icp_server}} ホスト環境のサイジングについて詳しくは、『[{{site.data.keyword.icp_server}} クラスターのサイジング![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html)』を参照してください。

必要に応じて、リソースが制約された環境内でリモート・エッジ・サーバーを操作できます。 リソースが制約された環境内でエッジ・サーバーを操作する必要がある場合は、{{site.data.keyword.edge_profile}} を使用することをご検討ください。 このプロファイルでは、エッジ・サーバー環境に最小限必要なコンポーネントのみを構成します。 このプロファイルを使用する場合でも、{{site.data.keyword.edge_servers_notm}} アーキテクチャーに必要な一連のコンポーネントのために、またエッジ・サーバー環境でホストされるその他のアプリケーション・ワークロードに必要なリソースを提供するために十分なリソースを割り振る必要があります。 {{site.data.keyword.edge_servers_notm}} アーキテクチャーについて詳しくは、[{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch)を参照してください。

{{site.data.keyword.edge_profile}} 構成はメモリーやストレージ・リソースを節約できるものの、回復力は低レベルになります。 このプロファイルに基づくエッジ・サーバーは、ハブ・クラスターが配置されている中央データ・センターから切断された状態で操作することができます。 この切断された状態の操作は、通常は最長 3 日間可能です。 エッジ・サーバーに障害が発生すると、サーバーは、リモート・オペレーション・センター向けの運用サポートを提供しなくなります。

また {{site.data.keyword.edge_profile}} 構成は、以下のテクノロジーおよび処理のみのサポートに制限されています。
  * {{site.data.keyword.linux_notm}} 64 ビット・プラットフォーム
  * 非高可用性 (HA) デプロイメント・トポロジー
  * 2 日目操作としてのワーカー・ノードの追加および除去
  * クラスターへの CLI アクセスおよびクラスターの制御
  * Calico ネットワーク

より高レベルの回復力が必要な場合や上記の制限の制約が過度である場合は、柔軟性のあるフェイルオーバー・サポートを提供するために {{site.data.keyword.icp_server}} の他の標準デプロイメント構成プロファイルを代わりに使用できます。

### サンプル・デプロイメント

* {{site.data.keyword.edge_profile}} に基づいたエッジ・サーバー環境 (回復力は低レベル)

| ノード・タイプ | ノード数 | CPU | メモリー (GB) | ディスク (GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
| ブート       | 1           | 1   | 2           | 8   |
| マスター     | 1           | 2   | 4           | 16  |
| 管理 | 1           | 1   | 2           | 8   |
| ワーカー     | 1           | 4   | 8           | 32  |
{: caption="表 6: 低レベルの回復力のエッジ・サーバー環境のエッジ・プロファイル値" caption-side="top"}

* 他の {{site.data.keyword.icp_server}} プロファイルに基づいたエッジ・サーバー環境 (回復力は中レベルから高レベル)

  エッジ・サーバー環境に {{site.data.keyword.edge_profile}} 以外の構成を使用する必要がある場合は、小規模、中規模、および大規模のサンプル・デプロイメント要件を使用してください。 詳しくは、『[{{site.data.keyword.icp_server}} クラスターのサンプル・デプロイメントのサイジング![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples)』を参照してください。
