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

# エージェントのインストール
{: #importing_clusters}

以下のいずれかのタイプの Kubernetes エッジ・クラスターに {{site.data.keyword.edge_notm}} エージェントをインストールすることから始めます。

* [{{site.data.keyword.ocp}} Kubernetes エッジ・クラスターへのエージェントのインストール](#install_kube)
* [k3s エッジ・クラスターおよび microk8s エッジ・クラスターへのエージェントのインストール](#install_lite)

次に、エッジ・クラスターにエッジ・サービスをデプロイします。

* [エッジ・クラスターへのサービスのデプロイ](#deploying_services)

エージェントを削除する必要がある場合は、以下を行います。

* [エッジ・クラスターからのエージェントの削除](#remove_agent)

## {{site.data.keyword.ocp}} Kubernetes エッジ・クラスターへのエージェントのインストール
{: #install_kube}

このセクションでは、{{site.data.keyword.ocp}} エッジ・クラスターに {{site.data.keyword.ieam}} エージェントをインストールする方法について説明します。エッジ・クラスターへの管理者アクセス権限を持つホスト上で、以下のステップを実行します。

1. **admin** としてエッジ・クラスターにログインします。

   ```bash
	oc login https://<API_ENDPOINT_HOST>:<PORT> -u <ADMIN_USER> -p <ADMIN_PASSWORD> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. エージェント名前空間変数をデフォルト値 (または、エージェントを明示的にインストールしたい名前空間) に設定します。

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

3. エージェントが使用するようにしたいストレージ・クラスを、組み込みストレージ・クラスまたは作成したストレージ・クラスに設定します。以下に例を示します。

   ```bash
   export EDGE_CLUSTER_STORAGE_CLASS=rook-ceph-cephfs-internal
   ```
   {: codeblock}

4. エッジ・クラスター上でイメージ・レジストリーをセットアップするには、『[OpenShift イメージ・レジストリーの使用](../developing/container_registry.md##ocp_image_registry)』のステップ 2 から 8 を実行します。ただし、1 つ変更点があり、ステップ 4 で **OCP_PROJECT** を **$AGENT_NAMESPACE** に設定してください。

5. **agent-install.sh** スクリプトは、{{site.data.keyword.ieam}} エージェントをエッジ・クラスター・コンテナー・レジストリーに保管します。使用される必要のあるレジストリー・ユーザー、パスワード、およびフル・イメージ・パス (タグを除く) を設定します。

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_DOCKER_HOST/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **注:** {{site.data.keyword.ieam}} エージェント・イメージはローカル・エッジ・クラスター・レジストリーに保管されます。それを再始動したり別のポッドへ移動したりすることが必要になった場合にエッジ・クラスター kubernetes が持続的にそれにアクセスできる必要があるためです。

6. Horizon exchange ユーザー資格情報をエクスポートします。

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

7. 管理者から **agentInstallFiles-x86_64-Cluster.tar.gz** ファイルおよび API 鍵を取得します。 [エッジ・クラスター用の必要な情報とファイルの収集](preparing_edge_cluster.md)で、既にそれらが作成されているはずです。

8. tar ファイルから **agent-install.sh** スクリプトを解凍します。

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

9. **agent-install.sh** コマンドを実行して、Horizon エージェントをインストールおよび構成し、エッジ・クラスターをポリシーに登録します。

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **注:**
   * 使用可能なすべてのフラグを表示するには、**./agent-install.sh -h** を実行します。
   * エラーが発生して **agent-install.sh** が完了しない場合、**agent-uninstall.sh** を実行 (『[エッジ・クラスターからのエージェントの削除](#remove_agent)』を参照) してから、このセクションのステップを繰り返します。

10. エージェントの名前空間/プロジェクトに移動し、エージェント・ポッドが実行中であることを確認します。

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

11. これで、エージェントはエッジ・クラスターにインストールされました。エージェントに関連付けられた kubernetes リソースについてよく知りたい場合は、以下のコマンドを実行することができます。

   ```bash
   oc get namespace $AGENT_NAMESPACE
   oc project $AGENT_NAMESPACE   # ensure this is the current namespace/project
   oc get deployment -o wide
   oc get deployment agent -o yaml   # get details of the deployment
   oc get configmap openhorizon-agent-config -o yaml
   oc get secret openhorizon-agent-secrets -o yaml
   oc get pvc openhorizon-agent-pvc -o yaml   # persistent volume
   ```
   {: codeblock}

12. 多くの場合、エッジ・クラスターにポリシーに登録されながら、そのエッジ・クラスターにユーザー指定のノード・ポリシーがないと、どのデプロイメント・ポリシーもそのエッジ・クラスターにエッジ・サービスをデプロイしません。これは、Horizon サンプルでの事例です。このエッジ・クラスターにエッジ・サービスがデプロイされるようにノード・ポリシーを設定するには、[エッジ・クラスターへのサービスのデプロイ](#deploying_services)に進みます。

## k3s エッジ・クラスターおよび microk8s エッジ・クラスターへのエージェントのインストール
{: #install_lite}

このセクションでは、軽量の小さな kubernetes クラスターである k3s または microk8s に {{site.data.keyword.ieam}} エージェントをインストールする方法について説明します。

1. **root** としてエッジ・クラスターにログインします。

2. 管理者から **agentInstallFiles-x86_64-Cluster.tar.gz** ファイルおよび API 鍵を取得します。 [エッジ・クラスター用の必要な情報とファイルの収集](preparing_edge_cluster.md)で、既にそれらが作成されているはずです。

3. tar ファイルから **agent-install.sh** スクリプトを解凍します。

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-install.sh
   ```
   {: codeblock}

4. Horizon exchange ユーザー資格情報をエクスポートします。

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

5. **agent-install.sh** スクリプトは、{{site.data.keyword.ieam}} エージェントをエッジ・クラスター・イメージ・レジストリーに保管します。使用される必要のあるフル・イメージ・パス (タグを除く) を設定します。以下に例を示します。

   ```bash
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
   ```
   {: codeblock}

   **注:** {{site.data.keyword.ieam}} エージェント・イメージはローカル・エッジ・クラスター・レジストリーに保管されます。それを再始動したり別のポッドへ移動したりすることが必要になった場合にエッジ・クラスター kubernetes が持続的にそれにアクセスできる必要があるためです。

6. デフォルトのストレージ・クラスを使用するように **agent-install.sh** に指示します。

   * k3s の場合:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=local-path
      ```
      {: codeblock}

   * microk8s の場合:

      ```bash
      export EDGE_CLUSTER_STORAGE_CLASS=microk8s-hostpath
      ```
      {: codeblock}

7. **agent-install.sh** コマンドを実行して、Horizon エージェントをインストールおよび構成し、エッジ・クラスターをポリシーに登録します。

   ```bash
   ./agent-install.sh -D cluster -z agentInstallFiles-x86_64-Cluster.tar.gz -d <node-id>
   ```
   {: codeblock}

   **注:**
   * 使用可能なすべてのフラグを表示するには、**./agent-install.sh -h** を実行します。
   * エラーが発生して **agent-install.sh** が完了しない場合、**agent-uninstall.sh** を実行 (『[エッジ・クラスターからのエージェントの削除](#remove_agent)』を参照) してから、**agent-install.sh** を再実行します。

8. エージェント・ポッドが実行中であることを確認します。

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

9. 多くの場合、エッジ・クラスターにポリシーに登録されながら、そのエッジ・クラスターにユーザー指定のノード・ポリシーがないと、どのデプロイメント・ポリシーもそのエッジ・クラスターにエッジ・サービスをデプロイしません。これは、Horizon サンプルでの事例です。このエッジ・クラスターにエッジ・サービスがデプロイされるようにノード・ポリシーを設定するには、[エッジ・クラスターへのサービスのデプロイ](#deploying_services)に進みます。

## エッジ・クラスターへのサービスのデプロイ
{: #deploying_services}

このエッジ・クラスターにノード・ポリシーを設定することで、デプロイメント・ポリシーがエッジ・サービスをここにデプロイするようにできます。このセクションでは、それを行う例を示します。

1. `hzn` コマンドの実行をより便利にするいくつかの別名を設定します。(`hzn` コマンドはエージェント・コンテナー内にありますが、これらの別名によって `hzn` をこのホストから実行することが可能になります。)

   ```bash
   cat << 'END_ALIASES' >> ~/.bash_aliases
   alias getagentpod='kubectl -n openhorizon-agent get pods --selector=app=agent -o jsonpath={.items[*].metadata.name}'
   alias hzn='kubectl -n openhorizon-agent exec -i $(getagentpod) -- hzn'
   END_ALIASES
   source ~/.bash_aliases
   ```
   {: codeblock}

2. エッジ・ノードが構成されている ({{site.data.keyword.ieam}} 管理ハブに登録されている) ことを確認します。

   ```bash
   hzn node list
   ```
   {: codeblock}

3. エッジ・クラスター・エージェントをテストするため、サンプル helloworld オペレーターおよびサービスをこのエッジ・ノードにデプロイするプロパティーを指定してノード・ポリシーを設定します。

   ```bash
   cat << 'EOF' > operator-example-node.policy.json
   {
     "properties": [
       { "name": "openhorizon.example", "value": "operator" }
     ]
   }
   EOF

   cat operator-example-node.policy.json | hzn policy update -f-
   hzn policy list
   ```
   {: codeblock}

   **注:**
   * 実際の **hzn** コマンドをエージェント・コンテナー内部で実行されているため、入力ファイルを必要とする `hzn` サブコマンドに対しては、ファイルをコマンドにパイプして、その内容がコンテナーに転送されるようにする必要があります。

4. 1 分後に、合意および実行中のエッジ・オペレーターおよびサービス・コンテナーを確認します。

   ```bash
   hzn agreement list
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

5. 前のコマンドからのポッド ID を使用して、エッジ・オペレーターおよびサービスのログを表示します。

   ```bash
   kubectl -n openhorizon-agent logs -f <operator-pod-id>
   # control-c to get out
   kubectl -n openhorizon-agent logs -f <service-pod-id>
   # control-c to get out
   ```
   {: codeblock}

6. エージェントがエッジ・サービスに渡す環境変数を表示することもできます。

   ```bash
   kubectl -n openhorizon-agent exec -i <service-pod-id> -- env | grep HZN_
   ```
   {: codeblock}

### エッジ・クラスターにデプロイされるサービスの変更
{: #changing_services}

* どのサービスがエッジ・クラスターにデプロイされるのかを変更するには、ノード・ポリシーを変更します。

  ```bash
  cat <new-node-policy>.json | hzn policy update -f-
  hzn policy list
  ```
  {: codeblock}

   1、2 分後に、新しいサービスがこのエッジ・クラスターにデプロイされます。

* 注: 一部のタイプの VM 上の microk8s では、停止 (置換) されているサービス・ポッドが **Terminating** 状態で動作しなくなることがあります。これが発生した場合は、以下を実行してクリーンアップできます。

  ```bash
  kubectl delete pod <pod-id> -n openhorizon-agent --force --grace-period=0
  pkill -fe <service-process>
  ```
  {: codeblock}

* ポリシーの代わりにパターンを使用してエッジ・クラスター上でサービスを実行する場合は、以下のようにします。

  ```bash
  hzn unregister -f
  hzn register -n $HZN_EXCHANGE_NODE_AUTH -p <pattern-name>
  ```
  {: codeblock}

## エッジ・クラスターからのエージェントの削除
{: #remove_agent}

エッジ・クラスターを登録抹消し、そのクラスターから {{site.data.keyword.ieam}} エージェントを削除するには、以下のステップを実行します。

1. tar ファイルから **agent-uninstall.sh** スクリプトを解凍します。

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Horizon exchange ユーザー資格情報をエクスポートします。

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. エージェントを削除します。

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

注: 場合によっては、名前空間を削除すると「終了中」状態になることがあります。 このシチュエーションになる場合、[名前空間が「終了中」状態でスタックする ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) を参照して、名前空間を手動で削除してください。
