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

**注**: {{site.data.keyword.ieam}} エージェントをインストールするには、エッジ・クラスターでのクラスター管理者のアクセス権限が必要です。

以下のいずれかのタイプの Kubernetes エッジ・クラスターに {{site.data.keyword.edge_notm}} エージェントをインストールすることから始めます。

* [{{site.data.keyword.ocp}} Kubernetes エッジ・クラスターへのエージェントのインストール](#install_kube)
* [k3s エッジ・クラスターおよび microk8s エッジ・クラスターへのエージェントのインストール](#install_lite)

次に、エッジ・クラスターにエッジ・サービスをデプロイします。

* [エッジ・クラスターへのサービスのデプロイ](#deploying_services)

エージェントを削除する必要がある場合は、以下を行います。

* [エッジ・クラスターからのエージェントの削除](../using_edge_services/removing_agent_from_cluster.md)

## {{site.data.keyword.ocp}} Kubernetes エッジ・クラスターへのエージェントのインストール
{: #install_kube}

このコンテンツでは、{{site.data.keyword.ocp}} エッジ・クラスターに {{site.data.keyword.ieam}} エージェントをインストールする方法について説明します。 エッジ・クラスターへの管理者アクセス権限を持つホスト上で、以下のステップを実行します。

1. **admin** としてエッジ・クラスターにログインします。

   ```bash
   oc login https://<api_endpoint_host>:<port> -u <admin_user> -p <admin_password> --insecure-skip-tls-verify=true
   ```
   {: codeblock}

2. [API 鍵の作成](../hub/prepare_for_edge_nodes.md)の手順をまだ実行していない場合、ここで実行します。 このプロセスでは、API 鍵を作成し、エッジ・ノードのセットアップ時に必要ないくつかのファイルを見つけて環境変数値を収集します。 このエッジ・クラスターで同じ環境変数を設定します。

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. エージェント名前空間変数をデフォルト値 (または、エージェントを明示的にインストールしたい名前空間) に設定します。

   ```bash
   export AGENT_NAMESPACE=openhorizon-agent
   ```
   {: codeblock}

4. エージェントで使用するストレージ・クラス (組み込みストレージ・クラスまたは作成したストレージ・クラス) を設定します。 以下の 2 つのコマンドの 1 つ目で使用可能なストレージ・クラスを確認してから、2 番目のコマンドで、使用するストレージ・クラスの名前に置き換えることができます。 1 つのストレージ・クラスは、`(default)` というラベルでなければなりません。

   ```bash
   oc get storageclass
   export EDGE_CLUSTER_STORAGE_CLASS=<rook-ceph-cephfs-internal>
   ```
   {: codeblock}

5. {{site.data.keyword.open_shift}} イメージ・レジストリーのデフォルト・ルートが、クラスターの外部からアクセス可能であるように作成されているかどうかを判別します。

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   **default-route** が見つからないとコマンド応答で示された場合は、それを公開する必要があります (詳しくは、『[Exposing the registry](https://docs.openshift.com/container-platform/4.6/registry/securing-exposing-registry.html)』を参照)。

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

6. 使用する必要があるリポジトリー・ルート名を取得します。

   ```bash
   export OCP_IMAGE_REGISTRY=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

7. 以下のようにして、イメージを格納するための新規プロジェクトを作成します。

   ```bash
   export OCP_PROJECT=$AGENT_NAMESPACE
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

8. 選択した名前を使用してサービス・アカウントを作成します。

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

9. 現行プロジェクトのサービス・アカウントに役割を追加します。

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

10. サービス・アカウント・トークンを以下の環境変数に設定します。

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

11. {{site.data.keyword.open_shift}} 証明書を取得し、Docker がそれを信頼できるようにします。

   ```bash
   echo | openssl s_client -connect $OCP_IMAGE_REGISTRY:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   {{site.data.keyword.linux_notm}} の場合:

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
   cp ca.crt /etc/docker/certs.d/$OCP_IMAGE_REGISTRY
   systemctl restart docker.service
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}} の場合:

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   cp ca.crt ~/.docker/certs.d/$OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

   {{site.data.keyword.macOS_notm}} で、デスクトップ・メニュー・バーの右側にある Docker デスクトップ・アイコンを使用し、ドロップダウン・メニューの**「Restart」**をクリックして、Docker を再始動します。

12. {{site.data.keyword.ocp}} Docker ホストにログインします。

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_IMAGE_REGISTRY
   ```
   {: codeblock}

13. 以下のようにして、イメージ・レジストリー・アクセス用の追加のトラストストアを構成します。   

    ```bash
    oc create configmap registry-config --from-file=$OCP_IMAGE_REGISTRY=ca.crt -n openshift-config
    ```
    {: codeblock}

14. 以下のようにして、新しい `registry-config` を編集します。

    ```bash
    oc edit image.config.openshift.io cluster
    ```
    {: codeblock}

15. 以下のようにして、`spec:` セクションを更新します。

    ```bash
    spec:
      additionalTrustedCA:
      name: registry-config
    ```
    {: codeblock}

16. **agent-install.sh** スクリプトは、{{site.data.keyword.ieam}} エージェントをエッジ・クラスター・コンテナー・レジストリーに保管します。 レジストリー・ユーザー、パスワード、およびフル・イメージ・パス (タグを除く) を設定します。

   ```bash
   export EDGE_CLUSTER_REGISTRY_USERNAME=$OCP_USER
   export EDGE_CLUSTER_REGISTRY_TOKEN="$OCP_TOKEN"
   export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$OCP_IMAGE_REGISTRY/$OCP_PROJECT/amd64_anax_k8s
   ```
   {: codeblock}

   **注**: {{site.data.keyword.ieam}} エージェント・イメージはローカル・エッジ・クラスター・レジストリーに保管されます。これは、エッジ・クラスター Kubernetes がこのエージェント・イメージを再始動したり別のポッドに移動したりしなければならなくなった場合に、エージェント・イメージに持続的にアクセスする必要があるためです。

17. クラウド同期サービス (CSS) から **agent-install.sh** スクリプトをダウンロードして実行可能にします。

   ```bash
   curl -u "$HZN_ORG_ID/$HZN_EXCHANGE_USER_AUTH" -k -o agent-install.sh $HZN_FSS_CSSURL/api/v1/objects/IBM/agent_files/agent-install.sh/data
   chmod +x agent-install.sh
   ```
   {: codeblock}

18. **agent-install.sh** を実行して CSS から必要なファイルを取得し、{{site.data.keyword.horizon}} エージェントをインストールおよび構成し、エッジ・クラスターをポリシーに登録します。

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **注**:
   * 使用可能なすべてのフラグを表示するには、**./agent-install.sh -h** を実行します。
   * エラーが原因で **agent-install.sh** が失敗する場合は、そのエラーを修正し、**agent-install.sh** を再実行します。 これが機能しない場合、**agent-uninstall.sh** を実行 ([エッジ・クラスターからのエージェントの削除](../using_edge_services/removing_agent_from_cluster.md)を参照) してから、**agent-install.sh** を再実行します。

19. エージェント名前空間 (プロジェクトとも呼ばれます) に移動して、エージェント・ポッドが実行中であることを確認します。

   ```bash
   oc project $AGENT_NAMESPACE
   oc get pods
   ```
   {: codeblock}

20. これで、エージェントはエッジ・クラスターにインストールされました。エージェントに関連付けられた Kubernetes リソースについてよく知りたい場合は、以下のコマンドを実行します。

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

21. 多くの場合、エッジ・クラスターがポリシーに登録されていても、そのエッジ・クラスターにユーザー指定のノード・ポリシーがないときは、どのデプロイメント・ポリシーもそのエッジ・クラスターにエッジ・サービスをデプロイしません。 これは、Horizon サンプルでの事例です。 このエッジ・クラスターにエッジ・サービスがデプロイされるようにノード・ポリシーを設定するには、[エッジ・クラスターへのサービスのデプロイ](#deploying_services)に進みます。

## k3s エッジ・クラスターおよび microk8s エッジ・クラスターへのエージェントのインストール
{: #install_lite}

このコンテンツでは、軽量の小さな Kubernetes クラスターである [k3s](https://k3s.io/) または [microk8s](https://microk8s.io/) に {{site.data.keyword.ieam}} エージェントをインストールする方法について説明します。

1. **root** としてエッジ・クラスターにログインします。

2. [API 鍵の作成](../hub/prepare_for_edge_nodes.md)の手順をまだ実行していない場合、ここで実行します。 このプロセスでは、API 鍵を作成し、エッジ・ノードのセットアップ時に必要ないくつかのファイルを見つけて環境変数値を収集します。 このエッジ・クラスターで同じ環境変数を設定します。

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
  export HZN_ORG_ID=<your-exchange-organization>
  export HZN_FSS_CSSURL=https://<ieam-management-hub-ingress>/edge-css/
  ```
  {: codeblock}

3. **agent-install.sh** スクリプトを新しいエッジ・クラスターにコピーします。

4. **agent-install.sh** スクリプトは、{{site.data.keyword.ieam}} エージェントをエッジ・クラスター・イメージ・レジストリーに保管します。 使用される必要のあるフル・イメージ・パス (タグを除く) を設定します。 以下に例を示します。

   * k3s の場合:

      ```bash
      REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=$REGISTRY_ENDPOINT/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   * microk8s の場合:

      ```bash
      export IMAGE_ON_EDGE_CLUSTER_REGISTRY=localhost:32000/openhorizon-agent/amd64_anax_k8s
      ```
      {: codeblock}

   **注**: {{site.data.keyword.ieam}} エージェント・イメージはローカル・エッジ・クラスター・レジストリーに保管されます。これは、エッジ・クラスター Kubernetes がこのエージェント・イメージを再始動したり別のポッドに移動したりしなければならなくなった場合に、エージェント・イメージに持続的にアクセスする必要があるためです。

5. デフォルトのストレージ・クラスを使用するように **agent-install.sh** に指示します。

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

6. **agent-install.sh** を実行して CSS (クラウド同期サービス) から必要なファイルを取得し、{{site.data.keyword.horizon}} エージェントをインストールおよび構成し、エッジ・クラスターをポリシーに登録します。

   ```bash
   ./agent-install.sh -D cluster -i 'css:'
   ```
   {: codeblock}

   **注**:
   * 使用可能なすべてのフラグを表示するには、**./agent-install.sh -h** を実行します。
   * エラーが発生して **agent-install.sh** が正常に完了しない場合、表示されたエラーを修正し、**agent-install.sh** を再実行します。 これが機能しない場合、**agent-uninstall.sh** を実行 ([エッジ・クラスターからのエージェントの削除](../using_edge_services/removing_agent_from_cluster.md)を参照) してから、**agent-install.sh** を再実行します。

7. エージェント・ポッドが実行中であることを確認します。

   ```bash
   kubectl get namespaces
   kubectl -n openhorizon-agent get pods
   ```
   {: codeblock}

8. 通常、エッジ・クラスターがポリシーに登録されていても、そのエッジ・クラスターにユーザー指定のノード・ポリシーがないときは、どのデプロイメント・ポリシーもそのエッジ・クラスターにエッジ・サービスをデプロイしません。 これは、予期されていることです。 このエッジ・クラスターにエッジ・サービスがデプロイされるようにノード・ポリシーを設定するには、[エッジ・クラスターへのサービスのデプロイ](#deploying_services)に進みます。

## エッジ・クラスターへのサービスのデプロイ
{: #deploying_services}

このエッジ・クラスターにノード・ポリシーを設定することで、デプロイメント・ポリシーがエッジ・サービスをここにデプロイするようにできます。 このコンテンツでは、これを行う例を示します。

1. `hzn` コマンドの実行をより便利にするいくつかの別名を設定します。 (`hzn` コマンドはエージェント・コンテナー内にありますが、これらの別名によって `hzn` をこのホストから実行することが可能になります。)

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

   **注**:
   * 実際の **hzn** コマンドをエージェント・コンテナー内部で実行されているため、入力ファイルを必要とする `hzn` コマンドに対しては、ファイルをコマンドにパイプして、その内容がコンテナーに転送されるようにする必要があります。

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

* **注**: microk8s がインストールされた一部の VM では、停止 (置換) されているサービス・ポッドが **Terminating** 状態で停止することがあります。 これが発生した場合は、以下を実行します。

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
