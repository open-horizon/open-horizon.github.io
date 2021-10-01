---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エッジ・クラスターからのエージェントの削除
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

注: 場合によっては、名前空間を削除すると「終了中」状態になることがあります。 このシチュエーションになる場合、[名前空間が「終了中」状態でスタックする](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) を参照して、名前空間を手動で削除してください。
