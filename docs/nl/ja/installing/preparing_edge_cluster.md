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

以下のエッジ・クラスターの 1 つをインストールし、{{site.data.keyword.edge_notm}} エージェント用に準備します。
* [OCP エッジ・クラスターのインストール](#install_ocp_edge_cluster)
* [k3s エッジ・クラスターのインストールと構成](#install_k3s_edge_cluster)
* [microk8s エッジ・クラスターのインストールと構成](#install_microk8s_edge_cluster) (開発およびテスト向けであり、実動には推奨されません)

## OCP エッジ・クラスターのインストール
{: #install_ocp_edge_cluster}

1. [{{site.data.keyword.open_shift_cp}} 資料](https://docs.openshift.com/container-platform/4.6/welcome/index.html) で説明されているインストール手順に従って OCP をインストールします。 ({{site.data.keyword.ieam}} では、x86_64 プラットフォーム上の OCP のみがサポートされます)。

2. OCP エッジ・クラスターを管理する管理ホストで Kubernetes CLI (**kubectl**)、Openshift クライアント CLI (**oc**)、および Docker をインストールします。 これは、エージェント・インストール・スクリプトを実行するのと同じホストです。 詳しくは、『[cloudctl、kubectl、および oc のインストール](../cli/cloudctl_oc_cli.md)』を参照してください。

## k3s エッジ・クラスターのインストールと構成
{: #install_k3s_edge_cluster}

ここでは、軽量の小さな Kubernetes クラスターである k3s (rancher) を Ubuntu 18.04 にインストールする手順の要約を示します。 詳しくは、[k3s 資料](https://rancher.com/docs/k3s/latest/en/)を参照してください。

**注:** インストールされている場合は、以下のステップを実行する前に kubectl をアンインストールします。

1. **root** としてログインするか、`sudo -i` を使用して **root** に昇格します。

2. マシンの完全なホスト名には、2 つ以上のドットが含まれている必要があります。 以下のようにして、完全なホスト名を確認します。

   ```bash
   hostname
   ```
    {: codeblock}

   マシンの完全なホスト名に含まれているドットが 2 つ未満の場合は、以下のようにホスト名を変更します。

   ```bash
   hostnamectl set-hostname <your-new-hostname-with-2-dots>
   ```
   {: codeblock}

   詳しくは、[github 問題](https://github.com/rancher/k3s/issues/53)を参照してください

3. k3s をインストールします。

   ```bash
   curl -sfL https://get.k3s.io | sh -
   ```
   {: codeblock}

4. イメージ・レジストリー・サービスを作成します。
   1. 以下の内容で **k3s-persistent-claim.yml** という名前のファイルを作成します。
      ```yaml
      apiVersion: v1
      kind: PersistentVolumeClaim
      metadata:
        name: docker-registry-pvc
      spec:
        storageClassName: "local-path"
        accessModes:
          - ReadWriteOnce
        resources:
          requests:
            storage: 10Gi
      ```
      {: codeblock}

   2. 次のように永続ボリューム・クレームを作成します。

      ```bash
      kubectl apply -f k3s-persistent-claim.yml
      ```
      {: codeblock}

   3. 永続ボリューム・クレームが作成済みで、保留状況になっていることを確認します。

      ```bash
      kubectl get pvc
      ```
      {: codeblock}

   4. 以下の内容で **k3s-registry-deployment.yml** という名前のファイルを作成します。

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
            volumes:
            - name: registry-pvc-storage
              persistentVolumeClaim:
                claimName: docker-registry-pvc
            containers:
            - name: docker-registry
              image: registry
              ports:
              - containerPort: 5000
              volumeMounts:
              - name: registry-pvc-storage
                mountPath: /var/lib/registry
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

   5. 以下のようにして、レジストリー・デプロイメントおよびサービスを作成します。

      ```bash
      kubectl apply -f k3s-registry-deployment.yml
      ```
      {: codeblock}

   6. サービスが作成されたことを確認します。

      ```bash
      kubectl get deployment
      kubectl get service
      ```
      {: codeblock}

   7. レジストリー・エンドポイントを定義します。

      ```bash
      export REGISTRY_ENDPOINT=$(kubectl get service docker-registry-service | grep docker-registry-service | awk '{print $3;}'):5000
      cat << EOF >> /etc/rancher/k3s/registries.yaml
      mirrors:
        "$REGISTRY_ENDPOINT":
          endpoint:
            - "http://$REGISTRY_ENDPOINT"
      EOF
      ```
      {: codeblock}

   8. **/etc/rancher/k3s/registries.yaml** への変更を有効にするために k3s を再始動します。

      ```bash
      systemctl restart k3s
      ```
      {: codeblock}

5. このレジストリーを、セキュアでないレジストリーとして docker に定義します。

   1. **/etc/docker/daemon.json** を作成するか、このファイルに追記します (`<registry-endpoint>` は、前のステップで取得した `$REGISTRY_ENDPOINT` 環境変数の値に置き換えてください)。

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   2. (オプション) 必要に応じて、以下のように、Docker がご使用のマシンにあるかを確認します。

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}     

   3. 変更を有効にするために docker を再始動します。

      ```bash
      systemctl restart docker
      ```
      {: codeblock}

## microk8s エッジ・クラスターのインストールと構成
{: #install_microk8s_edge_cluster}

この内容では、軽量の小さな Kubernetes クラスターである microk8s を Ubuntu 18.04 にインストールする手順の要約を示します。 (詳しい手順については、[microk8s 資料](https://microk8s.io/docs) を参照してください)

**注**: 単一ワーカー・ノード Kubernetes クラスターではスケーラビリティーや高可用性が提供されないため、このタイプのエッジ・クラスターは、開発およびテスト用のものです。

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

   **注:** Microk8s は、デフォルトで `8.8.8.8` および `8.8.4.4` をアップストリーム・ネーム・サーバーとして使用します。 これらのネーム・サーバーが管理ハブのホスト名を解決できない場合は、microk8s が使用しているネーム・サーバーを変更する必要があります。
   
   1. `/etc/resolv.conf` または `/run/systemd/resolve/resolv.conf` 内のアップストリーム・ネーム・サーバーのリストを取得します。

   2. `kube-system` 名前空間の `coredns` configmap を編集します。 `forward` セクションにアップストリーム・ネーム・サーバーを設定します。
   
      ```bash
      microk8s.kubectl edit -n kube-system cm/coredns
      ```
      {: codeblock}
   
   3. Kubernetes DNS について詳しくは、[Kubernetes の資料](https://kubernetes.io/docs/tasks/administer-cluster/dns-custom-nameservers/) を参照してください。


4. 状況を確認します。

   ```bash
   microk8s.status --wait-ready
   ```
   {: codeblock}

5. 既にインストール済みの **kubectl** コマンドとの競合を防ぐため、microK8s の kubectl コマンドは **microk8s.kubectl** と呼ばれます。 **kubectl** がインストールされていない場合、**microk8s.kubectl** 用にこの別名を追加します。

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

   3. Docker に対してセキュアでないものとしてこのレジストリーを定義します。 **/etc/docker/daemon.json** を作成するか、このファイルに追記します (`<registry-endpoint>` は、前のステップで取得した `$REGISTRY_ENDPOINT` 環境変数の値に置き換えてください)。

      ```json
      {
        "insecure-registries": [ "<registry-endpoint>" ]
      }
      ```
      {: codeblock}

   4. (オプション) 以下のようにして、Docker がご使用のマシンにあるかを確認します。

      ```bash
      curl -fsSL get.docker.com | sh
      ```
      {: codeblock}   

   5. 変更を有効にするために docker を再始動します。

      ```bash
      sudo systemctl restart docker
      ```
      {: codeblock}

## 次の作業

* [エージェントのインストール](edge_cluster_agent.md)
