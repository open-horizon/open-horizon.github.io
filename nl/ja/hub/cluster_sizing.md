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


# サイジングおよびシステム要件
{: #size}

## サイジングの考慮事項

クラスターのサイジングには多くの考慮事項があります。 このコンテンツでは、これらのいくつかの考慮事項について説明し、クラスターのサイジングについて最善の決定を行うために役立つガイドを提供します。

主な考慮事項は、クラスターでどのサービスを実行する必要があるかです。 このコンテンツでは、以下のサービスについてのみサイジングのガイダンスを示します。

* {{site.data.keyword.common_services}}
* {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理ハブ

オプションで、[{{site.data.keyword.open_shift_cp}} クラスター・ロギング](../admin/accessing_logs.md#ocp_logging)をインストールできます。

## {{site.data.keyword.ieam}} データベースの考慮事項

以下のサポートされる 2 つのデータベース構成により、{{site.data.keyword.ieam}} 管理ハブのサイジング考慮事項が影響を受けます。

* **ローカル**・データベースは、{{site.data.keyword.open_shift}} リソースとして {{site.data.keyword.open_shift}} クラスターに (デフォルトで) インストールされます。
* **リモート**・データベースは、ユーザーがプロビジョンしたデータベースであり、オンプレミスやクラウド・プロバイダー SaaS オファリングなどです。

### {{site.data.keyword.ieam}} ローカル・ストレージ要件

常にインストールされる Secure Device Onboarding (SDO) コンポーネントに加えて、**ローカル**・データベースおよびシークレット・マネージャーには永続ストレージが必要です。このストレージは、{{site.data.keyword.open_shift}} クラスター用に構成された動的ストレージ・クラスを使用します。

詳しくは、[サポートされる動的 {{site.data.keyword.open_shift}} ストレージのオプションおよび構成手順](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html) を参照してください。

クラスター作成時に保存データの暗号化を有効にする必要があります。多くの場合、クラウド・プラットフォームでのクラスター作成の一環としてこれを組み込むことができます。詳しくは、[以下の資料](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html)を参照してください。

選択されるストレージ・クラスのタイプに関する主な考慮事項は、そのストレージ・クラスが **allowVolumeExpansion** をサポートするかどうかです。 サポートする場合は、以下を実行すると **true** が返されます。

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

ストレージ・クラスがボリューム拡張を許可する場合、インストール後にサイジングを調整できます (基礎となるストレージ・スペースが割り振りに使用可能である場合)。 ストレージ・クラスがボリューム拡張を許可しない場合、ユース・ケース用のストレージを事前に割り振る必要があります。 

ボリューム拡張を許可しないストレージ・クラスを使用した初期インストールの後で追加ストレージが必要になった場合は、[バックアップおよびリカバリー](../admin/backup_recovery.md)のページで説明されている手順を使用して再インストールを実行する必要があります。

{{site.data.keyword.ieam}} 管理ハブのインストールの前に、[構成](configuration.md)ページの説明に従って**ストレージ**の値を変更することによって、割り振りを変更できます。 割り振りは、以下のデフォルト値に設定されます。

* PostgreSQL Exchange (Exchange のためにデータを保管し、使用量に応じてサイズが変動しますが、デフォルトのストレージ設定で、エッジ・ノードの公表された制限までサポートできます)
  * 20 GB
* PostgreSQL AgBot (AgBot のためにデータを保管し、デフォルトのストレージ設定で、エッジ・ノードの公表された制限までサポートできます)
  * 20 GB
* MongoDB クラウド同期サービス (モデル管理サービス (MMS) のためにコンテンツを保管します)。 モデルの数とサイズに応じて、このデフォルト割り振りを変更できます。
  * 50 GB
* Hashicorp Vault 永続ボリューム (エッジ・デバイス・サービスが使用するシークレットを保管します)
  * 10 GB (このボリューム・サイズは構成可能ではありません)
* Secure Device Onboarding 永続ボリューム (デバイス所有権証明書、デバイス構成オプション、および各デバイスのデプロイメント状況が保管されます)
  * 1 GB (このボリューム・サイズは構成可能ではありません)

* **注:**
  * {{site.data.keyword.ieam}} のボリュームは、**ReadWriteOnce** アクセス・モードを使用して作成されます。
  * IBM Cloud Platform Common Services には、そのサービスに関する追加のストレージ要件があります。 {{site.data.keyword.ieam}} のデフォルト構成でインストールした場合、インストール時に以下のボリュームが **ibm-common-services** 名前空間内に作成されます。
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h
    mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h
    prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    IBM Cloud Platform Common Services のストレージ要件および構成オプションについて詳しくは、[こちら](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html)を参照してください。

### {{site.data.keyword.ieam}} リモート・データベースの考慮事項

独自の**リモート**・データベースを使用すると、それらを同じクラスターにプロビジョンしない限り、このインストール用のストレージ・クラスおよびコンピュートの必要量は少なくなります。

**リモート**・データベースは、少なくとも以下のリソースおよび設定を使用してプロビジョンしてください。

* 2 つの vCPU
* 2 GB の RAM
* 前のセクションで説明されているデフォルトのストレージ・サイズ
* PostgreSQL データベースの場合、100 **max_connections** (通常はこれがデフォルトです)

## ワーカー・ノードのサイジング

[Kubernetes コンピュート・リソース](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container)を使用するサービスは、使用可能なワーカー・ノードすべてにわたってスケジュールされます。

### デフォルトの {{site.data.keyword.ieam}} 構成のための最小要件
| ワーカー・ノードの数 | ワーカー・ノードあたりの vCPU の数 | ワーカー・ノードあたりのメモリー (GB) | ワーカー・ノードあたりのローカル・ディスク・ストレージ (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**注:** お客様の環境によっては、ワーカー・ノード当たりの vCPU やワーカー・ノードがさらに必要な場合があるため、より多くの CPU キャパシティーが Exchange コンポーネントに割り振られることがあります。


&nbsp;
&nbsp;

クラスターの適切なサイジングを決定したら、[インストール](online_installation.md)を開始できます。
