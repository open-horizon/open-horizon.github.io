---

copyright:
  years: 2020
lastupdated: "2020-02-1"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# サイジングおよびシステム要件

{{site.data.keyword.edge_servers_notm}} をインストールする前に、各製品のシステム要件と、フットプリント・サイジングを確認してください。
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [マルチクラスター・エンドポイントのサイジング](#mc_endpoint)
  - [管理ハブ・サービスのサイジング](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [{{site.data.keyword.ocp_tm}} インストール資料 ![新しいタブで開く](../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* {{site.data.keyword.open_shift_cp}} コンピュート・ノードまたはワーカー・ノード: 16 コア | 32 GB RAM

  注: {{site.data.keyword.edge_servers_notm}} に加えて {{site.data.keyword.edge_devices_notm}} をインストールする場合、『[サイジング](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)』セクションに概説されているようにノード・リソースをさらに追加することが必要になります。
  
* ストレージ要件:
  - オフライン・インストールの場合、{{site.data.keyword.open_shift_cp}} イメージ・レジストリーには少なくとも 100 GB が必要です。
  - 管理サービス MongoDB およびロギングのそれぞれに、ストレージ・クラスを介して 20 GB が必要です。
  - 脆弱性アドバイザーには、ストレージ・クラスを介して 60 GB が必要です (有効にされる場合)。

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

最小フットプリントおよび実動フットプリントのサイジングがあります。

### {{site.data.keyword.open_shift}} および {{site.data.keyword.edge_servers_notm}} のデプロイメント・トポロジー

| デプロイメント・トポロジー | 用途の説明 | {{site.data.keyword.open_shift}} 4.2 ノード構成 |
| :--- | :--- | :--- | :---|
| 最小 | 小規模なクラスター・デプロイメント | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 つのマスター・ノード <br> &nbsp; 2 つ以上のワーカー・ノード </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 つの専用ワーカー・ノード </p> |
| 実動 | {{site.data.keyword.edge_servers_notm}} の <br> デフォルト構成がサポートされます| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 つのマスター・ノード (ネイティブ HA) <br>&nbsp; 4 つ以上のワーカー・ノード </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 つの専用ワーカー・ノード|
{: caption="表 1. {{site.data.keyword.edge_servers_notm}} のデプロイメント・トポロジー構成" caption-side="top"}

注: 専用 {{site.data.keyword.edge_servers_notm}} ワーカー・ノード用に、マスター・ノード、管理ノード、およびプロキシー・ノードを 1 つの {{site.data.keyword.open_shift}} ワーカー・ノードに設定します。これは、{{site.data.keyword.edge_servers_notm}} [インストール資料](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)で説明されています。

注: 以下に示すすべての永続ボリュームはデフォルトです。 長期間にわたって保管されるデータ量に基づいて、ボリュームをサイズ変更する必要があります。

### 最小のサイジング
| 構成 | ノード数 | vCPU | メモリー | 永続ボリューム (GB) | ディスク・スペース (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| マスター、管理、プロキシー	| 1| 16	| 32	| 20  | 100  |
{: caption="表 2. {{site.data.keyword.edge_servers_notm}} の {{site.data.keyword.open_shift}} ノードの最小サイジング" caption-side="top"}

### 実動のサイジング

| 構成 | ノード数 | vCPU | メモリー | 永続ボリューム (GB) | ディスク・スペース (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| マスター、管理、プロキシー	| 3| 48	| 96	| 60  | 300  |
{: caption="表 3. {{site.data.keyword.edge_servers_notm}} の {{site.data.keyword.open_shift}} ノードの実動サイジング" caption-side="top"}

## マルチクラスター・エンドポイントのサイジング
{: #mc_endpoint}

| コンポーネント名                 	| オプション 	| CPU 要求 	| CPU 制限  	| メモリー要求  	| メモリー制限 	|
|--------------------------------	|----------	|-------------	|------------	|-----------------	|--------------	|
| ApplicationManager             	| True     	| 100 mCore   	| 500mCore   	| 128 MiB         	| 2 GiB        	|
| WorkManager                    	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB       |
| ConnectionManager              	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| ComponentOperator              	| False    	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| CertManager                    	| False    	| 100 mCore   	| 300 mCore  	| 100 MiB         	| 300 MiB      	|
| PolicyController               	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| SearchCollector                	| True     	| 25 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| ServiceRegistry                	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 258 MiB      	|
| ServiceRegistryDNS             	| True     	| 100 mCore   	| 500 mCore  	| 70 MiB          	| 170 MiB      	|
| MeteringSender                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringReader                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringDataManager            	| True     	| 100 mCore   	| 1000 mCore 	| 256 MiB         	| 2560 MiB     	|
| MeteringMongoDB                	| True     	| -           	| -          	| 500 MiB           | 1 GiB        	|
| Tiller                         	| True     	| -           	| -          	| -               	| -            	|
| TopologyWeaveScope (ノード当たり 1 つ) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="表 4. マルチクラスター・エンドポイント説明" caption-side="top"}

## 管理ハブ・サービスのサイジング
{: #management_services}

| サービス名                 | オプション | CPU 要求 | CPU 制限 | メモリー要求 | メモリー制限 | 永続ボリューム (値はデフォルト) | 追加の考慮事項 |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui、Common-web-ui、iam-policy-controller、key-management、mcm-kui、metering、monitoring、multicluster-hub、nginx-ingress、search | デフォルト | 9,025 m | 29,289 m | 16,857 Mi | 56,963 Mi | 20 GiB | |
| 監査ロギング | オプション | 125 m | 500 m | 250 Mi | 700 Mi | | |
| CIS Policy Controller | オプション | 525 m | 1,450 m | 832 Mi | 2,560 Mi | | |
| Image Security Enforcement | オプション | 128 m | 256 m | 128 Mi | 256 Mi | | |
| ライセンス交付 | オプション | 200 m | 500 m | 256 Mi | 512 Mi | | |
| ロギング | オプション | 1,500 m | 3,000 m | 9,940 Mi | 10,516 Mi | 20 GiB | |
| Multitenancy Account Quota Enforcement | オプション | 25 m | 100 m | 64 Mi | 64 Mi | | |
| ミューテーション・アドバイザー | オプション | 1,000 m | 3,300 m | 2,052 Mi | 7,084 Mi | 100 GiB | |
| Notary | オプション | 600 m | 600 m  | 1,024 Mi | 1,024 Mi | | |
| Secret Encryption Policy Controller | オプション | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| Secure Token Service (STS) | オプション | 410 m | 600 m  | 94 Mi  | 314 Mi | | Red Hat OpenShift Service Mesh (Istio) が必要 |
| システム・ヘルス・チェック・サービス | オプション | 75 m | 600 m | 96 Mi | 256 Mi | | |
| 脆弱性アドバイザー (VA) | オプション | 1,940 m | 4,440 m | 8,040 Mi | 27,776 Mi | 10 GiB | Red Hat OpenShift ロギング (Elasticsearch) が必要 |
{: caption="表 5. ハブ・サービスのサイジング" caption-side="top"}

## 次の作業

{{site.data.keyword.edge_servers_notm}} [インストール資料](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)に戻ります。
