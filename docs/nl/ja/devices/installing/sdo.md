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

# SDO エージェントのインストールおよび登録
{: #sdo}

**テクノロジー・プレビュー**: 現時点では、将来の使用を計画する目的で SDO プロセスをテストしてそれについての知識を得るためにのみ SDO サポートを使用してください。将来のリリースでは、SDO サポートが実動用に使用可能になる予定です。

[SDO ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) は、Intel によって作成されたテクノロジーであり、これを使用すると、エッジ・デバイスの構成およびエッジ管理ハブとの関連付けを簡単かつセキュアに行うことができます。{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) で SDO 対応デバイスのサポートが追加されたことにより、ゼロタッチで (単にデバイスの電源オンのみで) エージェントがデバイスにインストールされ、{{site.data.keyword.ieam}} 管理ハブに登録されるようになります。

## SDO の概要
{: #sdo-overview}

SDO は、以下の 4 つのコンポーネントからなります。

1. エッジ・デバイス上の SDO モジュール (通常、デバイス製造元によってインストールされます)
2. 所有権証明書 (デバイスの購入者に物理デバイスと一緒に提供されるファイル)
3. SDO ランデブー・サーバー (SDO 対応デバイスが初めてのブート時に最初に接触する既知のサーバー)
4. SDO 所有者サービス (この特定の {{site.data.keyword.ieam}} インスタンスにデバイスを接続する {{site.data.keyword.ieam}} 管理ハブで実行されるサービス)

### テクノロジー・プレビューでの相違点
{: #sdo-tech-preview-differences}

- **SDO 対応デバイス:** SDO テストのため、ブート時の SDO 対応デバイスと同じように動作するように、VM に SDO モジュールを追加するためのスクリプトが提供されています。これにより、SDO 対応デバイスを購入することなく、{{site.data.keyword.ieam}} との SDO 統合をテストすることができます。
- **所有権証明書:** 通常はデバイス製造元から所有権証明書を受け取ります。上のリスト項目で言及されているスクリプトを使用して SDO モジュールを VM に追加する場合、スクリプトはその VM 上で所有者証明書の作成も行います。その証明書を VM からコピーすることが「デバイス製造元から所有権証明書を受け取る」ことに相当します。
- **ランデブー・サーバー:** 実動では、ブート・デバイスが、Intel のグローバル SDO ランデブー・サーバーに接触します。このテクノロジー・プレビューの開発およびテストでは、SDO 所有者サービスとバンドルされている開発ランデブー・サーバーを使用します。
- **SDO 所有者サービス:** このテクノロジー・プレビューでは、{{site.data.keyword.ieam}} 管理ハブに SDO 所有者サービスが自動的にインストールされることはありません。代わりに、{{site.data.keyword.ieam}} 管理ハブへのネットワーク・アクセスがあり、SDO デバイスがネットワークを介して到達できる任意のサーバー上で SDO 所有者サービスを開始するための便利なスクリプトが提供されています。

## SDO の使用
{: #using-sdo}

SDO を試して、{{site.data.keyword.ieam}} エージェントが自動的にインストールされ、{{site.data.keyword.ieam}} 管理ハブに登録されるのを確認するには、[open-horizon/SDO-support リポジトリー ![新しいタブで開く](../../images/icons/launch-glyph.svg "新しいタブで開く")](https://github.com/open-horizon/SDO-support/blob/master/README.md) の手順に従ってください。
