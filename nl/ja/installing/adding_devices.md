---

copyright:
years: 2019, 2020, 2021
lastupdated: "2021-09-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・デバイスの準備
{: #installing_the_agent}

以下の手順では、必要なソフトウェアをエッジ・デバイスにインストールし、{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) に登録するプロセスについて説明します。

## サポートされるアーキテクチャーおよびオペレーティング・システム
{: #suparch-horizon}

{{site.data.keyword.ieam}} では、以下のハードウェア・アーキテクチャーを備えたオペレーティング・システムおよびアーキテクチャーがサポートされます。

* x86_64
   * Ubuntu 20.x (focal)、Ubuntu 18.x (bionic)、Debian 10 (buster)、または Debian 9 (stretch) が実行されている、{{site.data.keyword.linux_bit_notm}} デバイスまたは仮想マシン
   * {{site.data.keyword.rhel}} 8.1、8.2、および 8.3
   * Fedora Workstation 32
   * CentOS 8.1、8.2、および 8.3
   * SuSE 15 SP2
* ppc64le
   * Ubuntu 20.x (focal) または Ubuntu 18.x (bionic) が実行されている {{site.data.keyword.linux_ppc64le_notm}} デバイスまたは仮想マシン
   * {{site.data.keyword.rhel}} 7.6、7.9、8.1、8.2、および 8.3
* ARM (32 ビット)
   * {{site.data.keyword.linux_notm}} on ARM (32 ビット): 例えば、Raspbian buster または stretch が実行されている Raspberry Pi
* ARM (64 ビット)
   * {{site.data.keyword.linux_notm}} on ARM (64 ビット): 例えば、Ubuntu 18.x (bionic) が実行されている、NVIDIA Jetson Nano、TX1、または TX2
* Mac
   * {{site.data.keyword.macOS_notm}}

**注**: 

* Fedora または SuSE でのエッジ・デバイスのインストールは、[エージェントの拡張手動インストールおよび登録](../installing/advanced_man_install.md)の方法でのみサポートされます。
* {{site.data.keyword.ieam}} {{site.data.keyword.version}} 上の CentOS および {{site.data.keyword.rhel}} は、コンテナー・エンジンとして Docker のみをサポートします。
* {{site.data.keyword.ieam}} {{site.data.keyword.version}} は、Docker を使用した {{site.data.keyword.rhel}} 8.x の実行をサポートしますが、これは {{site.data.keyword.rhel}} では公式にはサポートされていません。

## サイジング
{: #size}

エージェントには以下が必要です:

* 100 MB のランダム・アクセス・メモリー (RAM) (Docker を含む)。 RAM 容量は、合意ごとに約 100 K と、デバイス上で実行されるワークロードに必要な追加メモリーを加算して増加します。
* 400 MB ディスク (Docker を含む)。 ディスク容量は、ワークロードに使用されるコンテナー・イメージのサイズと、デバイスにデプロイされるモデル・オブジェクトのサイズ (2 倍) に応じて増加します。

# エージェントのインストール
{: #installing_the_agent}

以下の手順では、必要なソフトウェアをエッジ・デバイスにインストールし、{{site.data.keyword.ieam}} に登録するプロセスについて説明します。

## 手順
{: #install-config}

エッジ・デバイスをインストールして構成するには、エッジ・デバイスのタイプを示すリンクをクリックします。

* [{{site.data.keyword.linux_bit_notm}} デバイスまたは仮想マシン](#x86-machines)
* [{{site.data.keyword.rhel}} 8.x デバイスまたは仮想マシン](#rhel8)
* [{{site.data.keyword.linux_ppc64le_notm}} デバイスまたは仮想マシン](#ppc64le-machines)
* [{{site.data.keyword.linux_notm}} on ARM (32 ビット)](#arm-32-bit): Raspbian を稼働中の Raspberry Pi など
* [{{site.data.keyword.linux_notm}} on ARM (64 ビット)](#arm-64-bit): NVIDIA Jetson Nano、TX1、または TX2 など
* [{{site.data.keyword.macOS_notm}}](#mac-os-x)

## {{site.data.keyword.linux_bit_notm}} デバイスまたは仮想マシン
{: #x86-machines}

### ハードウェア要件
{: #hard-req-x86}

* 64 ビットの Intel&reg; または AMD デバイスまたは仮想マシン
* ご使用のデバイスのインターネット接続 (有線または WiFi)
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。

### 手順
{: #proc-x86}

Debian、{{site.data.keyword.rhel}} 7.x、または Ubuntu {{site.data.keyword.linux_notm}} をインストールして、デバイスを準備します。 この内容の手順は、Ubuntu 18.x を使用しているデバイスに基づいています。

デバイスに最新バージョンの Docker をインストールします。 詳しくは、[Docker のインストール](https://docs.docker.com/engine/install/ubuntu/)を参照してください。

これで、エッジ・デバイスは準備が完了し、[エージェントのインストール](registration.md)に進むことができます。

## {{site.data.keyword.rhel}} 8.x デバイスまたは仮想マシン
{: #rhel8}

### ハードウェア要件
{: #hard-req-rhel8}

* 64 ビット Intel&reg; デバイス、AMD デバイス、ppc64le デバイス、または仮想マシン
* ご使用のデバイスのインターネット接続 (有線または WiFi)
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。

### 手順
{: #proc-rhel8}

{{site.data.keyword.rhel}} 8.x をインストールして、デバイスを準備します。

以下で説明されているように、Podman およびその他の事前組み込みパッケージを削除し、Docker をインストールします。

1. 以下のようにして、パッケージをアンインストールします。
   ```
   yum remove buildah skopeo podman containers-common atomic-registries docker container-tools
   ```
   {: codeblock}

2. 残っている成果物およびファイルを削除します。
   ```
   rm -rf /etc/containers/* /var/lib/containers/* /etc/docker /etc/subuid* /etc/subgid*
   ```
   {: codeblock}

3. 以下のようにして、関連付けられているコンテナー・ストレージを削除します。
   ```
   cd ~ && rm -rf /.local/share/containers/
   ```
   {: codeblock}

4. 『[Docker CENTOS Installation](https://docs.docker.com/engine/install/centos/)』の手順に従って、Docker をインストールします。

5. デフォルトでブート時に開始するように Docker を構成し、他のすべての [Docker インストール後のステップ](https://docs.docker.com/engine/install/linux-postinstall/)に従います。
   ```
   sudo systemctl enable docker.service
   sudo systemctl enable containerd.service
   ```
   {: codeblock}

これで、エッジ・デバイスは準備が完了し、[エージェントのインストール](registration.md)に進むことができます。

## {{site.data.keyword.linux_ppc64le_notm}} デバイスまたは仮想マシン
{: #ppc64le-machines}

### ハードウェア要件
{: #hard-req-ppc64le}

* ppc64le デバイスまたは仮想マシン
* ご使用のデバイスのインターネット接続 (有線または WiFi)
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。

### 手順
{: #proc-ppc64le}

{{site.data.keyword.rhel}} をインストールして、デバイスを準備します。

デバイスに最新バージョンの Docker をインストールします。 

これで、エッジ・デバイスは準備が完了し、[エージェントのインストール](registration.md)に進むことができます。

## {{site.data.keyword.linux_notm}} on ARM (32 ビット)
{: #arm-32-bit}

### ハードウェア要件
{: #hard-req-pi}

* Raspberry Pi 3A+、3B、3B+、または 4 (推奨)
* Raspberry Pi A+、B+、2B、Zero-W、または Zero-WH
* MicroSD フラッシュ・カード (32 GB 推奨)
* ご使用のデバイスで適切な電源機構 (2 A 以上推奨)
* ご使用のデバイスのインターネット接続 (有線または WiFi)。
  **注**: WiFi をサポートするために追加のハードウェアが必要になるデバイスもあります。
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。

### 手順
{: #proc-pi}

1. Raspberry Pi デバイスを準備します。
   1. [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) {{site.data.keyword.linux_notm}} イメージを MicroSD カードにフラッシュします。

      多くのオペレーティング・システムから MicroSD イメージをフラッシュする方法について詳しくは、[Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images/README.md) を参照してください。
      手順では、WiFi および SSH 構成に Raspbian を使用しています。  

      **警告:** イメージを MicroSD カードにフラッシュすると、カード上に既に存在しているデータがすべて完全に消去されます。

   2. (オプション) デバイスに接続するために WiFi を使用する予定の場合は、新しくフラッシュしたイメージを編集して、適切な WPA2 WiFi 資格情報を指定します。 

      有線ネットワーク接続を使用する場合は、このステップを実行する必要はありません。  

      MicroSD カードで、ルート・レベル・フォルダー内に `wpa_supplicant.conf` という名前のファイルを作成し、そのファイルに WiFi 資格情報を入れます。 この資格情報には、ネットワーク SSID 名とパスフレーズがあります。 ファイルで以下の形式を使用します。 
      
      ```
      country=US
      ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev update_config=1
      network={
      ssid=“<your-network-ssid>”
      psk=“<your-network-passphrase”
      key_mgmt=WPA-PSK>
      }
      ```
      {: codeblock}

   3. (オプション) モニターやキーボードなしの Raspberry Pi デバイスを実行する必要がある場合、デバイスへの SSH 接続アクセスを有効にする必要があります。 SSH アクセスは、デフォルトでは使用不可です。

      SSH 接続を有効にするには、`ssh` という名前の空のファイルを MicroSD カード上に作成します。 このファイルをカードのルート・レベルのフォルダーに入れます。 このファイルを入れると、デフォルト資格情報を使用してデバイスに接続できるようになります。 

   4. MicroSD カードをアンマウントします。 すべての変更が書き込まれるように、カードの編集に使用しているデバイスからカードを安全に取り出してください。

   5. MicroSD カードを Raspberry Pi デバイスに挿入します。 オプションのセンサー・ハードウェアを接続し、デバイスを電源機構に接続します。

   6. デバイスを開始します。

   7. デバイスのデフォルト・パスワードを変更します。 Raspbian フラッシュ・イメージのデフォルト・アカウントでは、ログイン名 `pi` およびデフォルト・パスワード `raspberry` が使用されます。

      このアカウントにログインします。 以下のように、標準の {{site.data.keyword.linux_notm}} `passwd` コマンドを使用して、デフォルト・パスワードを変更します。

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}
     
   8. デバイスに最新バージョンの Docker をインストールします。 詳しくは、[Docker のインストール](https://docs.docker.com/engine/install/debian/)を参照してください。 

これで、エッジ・デバイスは準備が完了し、[エージェントのインストール](registration.md)に進むことができます。

## {{site.data.keyword.linux_notm}} on ARM (64 ビット)
{: #arm-64-bit}

### ハードウェア要件
{: #hard-req-nvidia}

* NVIDIA Jetson Nano または TX2 (推奨)
* NVIDIA Jetson TX1
* HDMI ビジネス・モニター、USB ハブ、USB キーボード、USB マウス
* ストレージ: 10 GB 以上 (SSD 推奨)
* ご使用のデバイスのインターネット接続 (有線または WiFi)
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。

### 手順
{: #proc-nvidia}

1. NVIDIA Jetson デバイスを準備します。
   1. ご使用のデバイスに最新の NVIDIA JetPack をインストールします。 詳しくは、以下を参照してください。
      * (TX1) [Jetson TX1](https://elinux.org/Jetson_TX1)
      * (TX2) [Jetson TX2 デベロッパー・キットによってエッジで AI を活用](https://developer.nvidia.com/embedded/jetson-tx2-developer-kit)
      * (Nano) [Jetson Nano デベロッパー・キット入門](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

      {{site.data.keyword.horizon}} ソフトウェアをインストールする前に、このソフトウェアおよび前提ソフトウェアをインストールする必要があります。

   2. デフォルト・パスワードを変更します。 JetPack のインストール手順のデフォルト・アカウントでは、ログイン名 `nvidia` およびデフォルト・パスワード `nvidia` が使用されます。 

      このアカウントにログインします。 以下のように、標準の {{site.data.keyword.linux_notm}} `passwd` コマンドを使用して、デフォルト・パスワードを変更します。

      ```
      passwd
      Enter new UNIX password:  
      Retype new UNIX password:
      passwd: password updated successfully
      ```
      {: codeblock}
      
   3. デバイスに最新バージョンの Docker をインストールします。 詳しくは、[Docker のインストール](https://docs.docker.com/engine/install/debian/)を参照してください。 

これで、エッジ・デバイスは準備が完了し、[エージェントのインストール](registration.md)に進むことができます。

## {{site.data.keyword.macOS_notm}}
{: #mac-os-x}

### ハードウェア要件
{: #hard-req-mac}

* 2010 年以降の 64 ビットの {{site.data.keyword.intel}} Mac デバイス
* MMU 仮想化が必要です。
* MacOS X バージョン 10.11 (「El Capitan」) 以降
* ご使用のマシンのインターネット接続 (有線または WiFi)
* (オプション) センサー・ハードウェア: 多くの {{site.data.keyword.horizon}} エッジ・サービスでは、特殊なセンサー・ハードウェアが必要です。
### 手順
{: #proc-mac}

1. デバイスを準備します。
   1. デバイスに最新バージョンの Docker をインストールします。 詳しくは、[Docker のインストール](https://docs.docker.com/docker-for-mac/install/)を参照してください。

   2. **socat をインストールします**。 以下のいずれかの方法を使用して、socat をインストールできます。

      * [Homebrew を使用して socat をインストールします](https://brewinstall.org/install-socat-on-mac-with-brew/)。
   
      * 既に MacPorts がインストールされている場合は、以下のようにそれを使用して socat をインストールします。
        ```
        sudo port install socat
        ```
        {: codeblock}

## 次の作業

* [エージェントのインストール](registration.md)
* [エージェントの更新](updating_the_agent.md)

## 関連情報

* [{{site.data.keyword.ieam}} のインストール](../hub/online_installation.md)
* [エージェントの拡張手動インストールおよび登録](advanced_man_install.md)
