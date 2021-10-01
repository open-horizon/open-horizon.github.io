---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# エージェントの更新
{: #updating_the_agent}

更新された {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) エージェント・パッケージを受け取ったら、エッジ・デバイスを簡単に更新できます。

1. 『[エッジ・デバイス用の必要な情報とファイルの収集](../hub/gather_files.md#prereq_horizon)』のステップを実行して、更新された **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** ファイルを新しいエージェント・パッケージを使用して作成します。
  
2. 各エッジ・デバイスについて、『[エージェントの自動インストールおよび登録](automated_install.md#method_one)』のステップを実行します。ただし、**agent-install.sh** コマンドを実行するときには、エッジ・デバイスで実行するようにしたいサービスと、パターンまたはポリシーを指定します。
