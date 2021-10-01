---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・クラスターの準備
{: #preparing_edge_cluster}

## 始める前に

エッジ・クラスターの作業を始める前に、以下を検討してください。

* [前提条件](#preparing_clusters)
* [エッジ・クラスター用の必要な情報とファイルの収集](#gather_info)

## 前提条件
{: #preparing_clusters}

エッジ・クラスターにエージェントをインストールする前に:

1. エージェント・インストール・スクリプトを実行する環境に Kubectl をインストールします。
2. エージェント・インストール・スクリプトを実行する環境に {{site.data.keyword.open_shift}} Client (oc) CLI をインストールします。
3. 関連するクラスター・リソースの作成に必要となる、クラスター管理者権限を取得します。
4. エージェント Docker イメージをホストするためのエッジ・クラスター・レジストリーを用意します。
5. **cloudctl** および **kubectl** コマンドと、解凍した **ibm-edge-computing-4.1-x86_64.tar.gz** をインストールします。 [インストール・プロセス](../installing/install.md#process)を参照してください。

## エッジ・クラスター用の必要な情報とファイルの収集
{: #gather_info}

エッジ・クラスターをインストールして {{site.data.keyword.edge_notm}} に登録するには、いくつかのファイルが必要になります。 このセクションでは、それらのファイルを収集して、各エッジ・クラスターで使用できる 1 つの tar ファイルにする方法をガイドします。

1. 以下のようにして、**CLUSTER_URL** 環境変数を設定します。

    ```
    export CLUSTER_URL=<cluster-url>
   export USER=<your-icp-admin-user>
   export PW=<your-icp-admin-password>
    ```
    {: codeblock}

    あるいは、**oc login** を使用してクラスターに接続した後、以下を実行することもできます。

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. 以下のように、クラスター管理者特権でクラスターに接続し、名前空間として **kube-system** を選択して、{{site.data.keyword.mgmt_hub}} の[インストール・プロセス](../installing/install.md#process)で config.yaml に定義したパスワードを入力します。

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <your-icp-admin-password> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. 環境変数にエッジ・クラスター・レジストリーでのエッジ・クラスター・レジストリー・ユーザー名、パスワード、完全イメージ名を設定します。 IMAGE_ON_EDGE_CLUSTER_REGISTRY の値は、次の形式で指定されます。

    ```
    <registry-name>/<repo-name>/<image-name>.
    ```
    {: codeblock} 

    レジストリーとして Docker Hub を使用する場合は、次の形式で値を指定します。
    
    ```
    <docker-repo-name>/<image-name>
    ```
    {: codeblock}
    
    以下に例を示します。
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<your-edge-cluster-registry-username>
    export EDGE_CLUSTER_REGISTRY_PW=<your-edge-cluster-registry-password>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<full-image-name-on-your-edge-cluster registry>
    ```
    {: codeblock}
    
4. 最新バージョンの **edgeDeviceFiles.sh** をダウンロードします。

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. **edgeDeviceFiles.sh** スクリプトを実行して、必要なファイルを収集します。

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <hzn-org-id> -n <node-id> <other flags>
   ```
   {: codeblock}
    
   これにより、agentInstallFiles-x86_64-Cluster..tar.gz という名前のファイルが作成されます。 
    
**コマンド引数**
   
注: エッジ・クラスターにエージェントをインストールするには、x86_64-Cluster を指定してください。
   
|コマンド引数|結果|
|-----------------|------|
|t                |収集されたすべてのファイルを含んでいる 1 つの **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルを作成します。 このフラグが設定されていない場合、収集されたファイルは現行ディレクトリーに入れられます。|
|f                |収集されたファイルの移動先ディレクトリーを指定します。 このディレクトリーが存在しない場合は、作成されます。 現行ディレクトリーがデフォルトになります。|
|r                |このフラグを使用する場合、**EDGE_CLUSTER_REGISTRY_USER**、**EDGE_CLUSTER_REGISTRY_PW**、および **IMAGE_ON_EDGE_CLUSTER_REGISTRY** を環境変数に設定する (ステップ 1) 必要があります。 4.1 で、これは必須フラグです。|
|o                |**HZN_ORG_ID** を指定します。 この値は、エッジ・クラスター登録に使用されます。|
|n                |エッジ・クラスター名の値にする **NODE_ID** を指定します。 この値は、エッジ・クラスター登録に使用されます。|
|s                |パーシスタント・ボリューム・クレームが使用するクラスター・ストレージ・クラスを指定します。 デフォルト・ストレージ・クラスは「gp2」です。|
|i                |エッジ・クラスターにデプロイされるエージェント・イメージ・バージョン。|


エッジ・クラスターにエージェントをインストールする準備ができたら、[エージェントのインストールとエッジ・クラスターの登録](importing_clusters.md)を参照してください。

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## 次の作業

* [エージェントのインストールとエッジ・クラスターの登録](importing_clusters.md)

## 関連情報

* [エッジ・クラスター](edge_clusters.md)
* [{{site.data.keyword.edge_notm}} 入門](../getting_started/getting_started.md)
* [インストール・プロセス](../installing/install.md#process)
