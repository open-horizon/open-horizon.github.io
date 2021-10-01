---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エージェントのインストールとエッジ・クラスターの登録
{: #importing_clusters}

以下のエッジ・クラスターにエージェントをインストールできます。

* Kubernetes
* 軽量の小さい Kuberetes (テスト用に推奨されます)

## Kubernetes エッジ・クラスターへのエージェントのインストール
{: #install_kube}

`agent-install.sh` スクリプトを実行することによって、エージェントの自動インストールが可能です。 

agent install スクリプトを実行する予定の環境で、以下のステップに従ってください。

1. 管理者から `agentInstallFiles-x86_64-Cluster.tar.gz` ファイルおよび API 鍵を取得します。 [エッジ・クラスター用の必要な情報とファイルの収集](preparing_edge_cluster.md)で、既にそれらが作成されているはずです。

2. 以降のステップのために環境変数にファイル名を設定します。

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. tar ファイルからファイルを解凍します。

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. Horizon exchange ユーザー資格情報をエクスポートします。以下のいずれかの形式です。

   ```
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

   または

   ```
   export HZN_EXCHANGE_USER_AUTH=<username>/<username>:<password>
   ```
   {: codeblock}

5. `agent-install.sh` コマンドを実行して、Horizon エージェントをインストールおよび構成し、helloworld サンプル・エッジ・サービスを実行するためにエッジ・クラスターを登録します。

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   注: エージェントのインストール中に、「**Horizon を上書きしますか?[y/N]: **」というプロンプトが出されることがあります。 **y** を選択して **Enter** キーを押してください。`agent-install.sh` は構成を正しく設定します。

6. (オプション) 使用可能な `agent-install.sh` フラグ説明を表示するには、以下のようにします。 

   ```
   ./agent-install.sh -h
   ```
   {: codeblock}

7. Kubernetes で実行中のエージェント・リソースをリストします。 現時点でエージェントがエッジ・クラスターにインストールされ、エッジ・クラスターが登録されていて、以下のエッジ・クラスター・リソースをリストできます。

   * 名前空間:

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * デプロイメント:

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   エージェント・デプロイメント詳細をリストするには、次のようにします。

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Configmap:

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * 秘密:
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim:
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * ポッド:

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. ログを表示し、ポッド ID を取得します。 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. エージェント・コンテナー内部で `hzn` コマンドを実行します。

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. `hzn` コマンドのフラグおよびサブコマンドを検討します。

   ```
   hzn --help
   ```
   {: codeblock}

## 軽量の小さな Kubernetes エッジ・クラスターへのエージェントのインストール

ここでは、ローカルにインストールして構成できる計量の小さな Kubernetes (microk8s) にエージェントをインストールする方法を説明します。以下の内容が含まれています。

* microk8s のインストールと構成
* microk8s へのエージェントのインストール

### microk8s のインストールと構成

1. microk8s をインストールします。

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. microk8s.kubectl の別名を設定します。

   注: microk8s でテストを行いたい場合は、`kubectl` コマンドがないことを確認してください。 

  * MicroK8s は、名前空間を指定した kubectl コマンドを使用して、既にインストールされている kubectl との競合を防止します。 既存のインストールがない場合は、別名を追加する (`append to ~/.bash_aliases`) ほうが簡単です。 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * その後、以下を実行します。

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. microk8s 内で dns および storage モジュールを使用可能にします。

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. microk8s 内でストレージ・クラスを作成します。 エージェント・インストール・スクリプトは、永続ボリューム・クレームのデフォルト・ストレージ・クラスとして `gp2` を使用します。 エージェントをインストールする前に、このストレージ・クラスが microk8s 環境で作成される必要があります。 エッジ・クラスター・エージェントが別のストレージ・クラスを使用する場合も、それが前もって作成される必要があります。 

   ストレージ・クラスとして `gp2` を作成する例を以下に示します。  

   1. storageClass.yml ファイルを作成します。 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. `kubectl` コマンドは、microk8s 内で storageClass オブジェクトを作成します。

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### microk8s へのエージェントのインストール

以下のステップに従って、microk8s にエージェントをインストールします。

1. [ステップ 1 から 3](#install_kube) を実行します。

2. `agent-install.sh` コマンドを実行して、Horizon エージェントをインストールおよび構成し、helloworld サンプル・エッジ・サービスを実行するためにエッジ・クラスターを登録します。

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   注: エージェントのインストール中に、「**Horizon を上書きしますか?[y/N]: **」というプロンプトが出されることがあります。 **y** を選択して **Enter** キーを押してください。`agent-install.sh` は構成を正しく設定します。

## 軽量 Kubernetes クラスターからのエージェントの削除 

注: エージェント・アンインストール・スクリプトはこのリリースでは完全ではないため、エージェントの削除は openhorizon-agent 名前空間を削除することによって行われます。

1. 名前空間を削除します。

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      注: 場合によっては、名前空間を削除すると「終了中」状態になることがあります。 このシチュエーションになる場合、[名前空間が「終了中」状態でスタックする ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) を参照して、名前空間を手動で削除してください。

2. clusterrolebinding を削除します。 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
