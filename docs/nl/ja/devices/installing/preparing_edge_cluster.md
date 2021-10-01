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

エッジ・クラスターをインストールし、それを {{site.data.keyword.edge_notm}} エージェント用に準備するには、以下のタスクを実行します。

* 以下のいずれかのタイプのエッジ・クラスターをインストールします。
  * [OCP エッジ・クラスターのインストール](#install_ocp_edge_cluster)
  * [k3s エッジ・クラスターのインストールと構成](#install_k3s_edge_cluster)
  * [microk8s エッジ・クラスターのインストールと構成](#install_microk8s_edge_cluster) (開発およびテスト向けであり、実動には推奨されません)
* [エッジ・クラスター用の必要な情報とファイルの収集](#gather_info)

## OCP エッジ・クラスターのインストール
{: #install_ocp_edge_cluster}

1.  [{{site.data.keyword.open_shift_cp}} 資料 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://docs.openshift.com/container-platform/4.4/welcome/index.html) で説明されているインストール手順に従って OCP をインストールします。

2. OCP クラスターの管理を行う管理ホスト (エージェント・インストール・スクリプトを実行するのと同じホスト) に Kubenetes CLI (**kubectl**) および Openshift クライアント CLI (**oc**) をインストールします。[cloudctl、kubectl、および oc のインストール](../installing/cloudctl_oc_cli.md)を参照してください。

## k3s エッジ・クラスターのインストールと構成
{: #install_k3s_edge_cluster}

このセクションでは、軽量の小さな kubernetes クラスターである k3s (rancher) を Ubuntu 18.04 にインストールする手順の要約を示します。(詳しい手順については、[k3s 資料 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://rancher.com/docs/k3s/latest/en/) を参照してください)

1. **root** としてログインするか、`sudo -i` を使用して **root** に昇格します。

2. k3s をインストールします。

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

3. イメージ・レジストリー・サービスを作成します。

   1. 以下の内容で **k3s-registry-deployment.yml** という名前のファイルを作成します。

      ```yaml
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: docker-registry
        labels:
          app: docker-registry
      spec:
        replicas: 1
        selector:
          matchLabels:
            app: docker-registry
        template:
          metadata:
            labels:
              app: docker-registry
          spec:
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: storage
                mountPath: /var/lib/registry
            volumes:
            - name: storage
              emptyDir: {} # FIXME: make this a persistent volume if using in production
      ---
      apiVersion: v1
      kind: Service
      metadata:
        name: docker-registry-service
      spec:
        selector:
          app: docker-registry
        type: NodePort
        ports:
          - protocol: TCP
            port: 5000
      ```
      {: codeblock}

   2. レジストリー・サービスを作成します。

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   3. サービスが作成されたことを確認します。

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   4. レジストリー・エンドポイントを定義します。

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get ep docker-registry-service | grep docker-registry-service | awk '{print $2}')
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   5. **/etc/rancher/k3s/registries.yaml** への変更を有効にするために k3s を再始動します。

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

4. このレジストリーを、セキュアでないレジストリーとして docker に定義します。

   1. **/etc/docker/daemon.json** を作成するか、これに追加します (`$REGISTRY_ENDPOINT` の値は置換してください)。

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   2. 変更を有効にするために docker を再始動します。

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s エッジ・クラスターのインストールと構成
{: #install_microk8s_edge_cluster}

このセクションでは、軽量の小さな kubernetes クラスターである microk8s を Ubuntu 18.04 にインストールする手順の要約を示します。(詳しい手順については、[microk8s 資料 ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://microk8s.io/docs) を参照してください)

注: 単一ワーカー・ノード kubernetes クラスターではスケーラビリティーや高可用性が提供されないため、このタイプのエッジ・クラスターは、開発およびテスト用のものです。

1. microk8s をインストールします。

   ```bash
   sudo snap install microk8s --classic --channel=stable
   ```
   {: codeblock}

2. **root** として実行しない場合は、ユーザーを **microk8s** グループに追加します。

   ```bash
   sudo usermod -a -G microk8s $USER
   sudo chown -f -R $USER ~/.kube
   su - $USER   # create new session for group update to take place
   ```
   {: codeblock}

3. microk8s 内で dns および storage モジュールを使用可能にします。

   ```bash
   microk8s.enable dns
   microk8s.enable storage
   ```
   {: codeblock}

4. 状況を確認します。

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. 既にインストール済みの **kubectl** コマンドとの競合を防ぐため、microK8s の kubectl コマンドは **microk8s.kubectl** と呼ばれます。 まだ **kubectl** がインストールされていない場合は、**microk8s.kubectl** 用にこの別名を追加してください。

   ```bash
   echo 'alias kubectl=microk8s.kubectl' >> ~/.bash_aliases
   source ~/.bash_aliases
   ```
   {: codeblock}

6. コンテナー・レジストリーを有効にし、セキュアでないレジストリーを許容するように Docker を構成します。

   1. コンテナー・レジストリーを有効にします。

      ```bash
      microk8s.enable registry
      export REGISTRY_ENDPOINT=localhost:32000
      ```
      {: codeblock}

   2. docker をインストールします (まだインストールされていない場合)。

      ```bash
      curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
      add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
      apt-get install docker-ce docker-ce-cli containerd.io
      ```
      {: codeblock}

   3. このレジストリーを、セキュアでないレジストリーとして docker に定義します。**/etc/docker/daemon.json** を作成するか、これに追加します (`$REGISTRY_ENDPOINT` の値は置換してください)。

      ```json
      {
        "insecure-registries": [ "$REGISTRY_ENDPOINT" ]
      }
      ```
      {: codeblock}

   4. 変更を有効にするために docker を再始動します。

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## 次の作業

* [エージェントのインストール](edge_cluster_agent.md)
