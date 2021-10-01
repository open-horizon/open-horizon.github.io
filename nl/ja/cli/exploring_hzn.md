---

copyright:
years: 2019
lastupdated: "2019-11-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# hzn CLI の探索
{: #exploring-hzn}

{{site.data.keyword.horizon}} エッジ・ノードでは、`hzn` コマンドを使用して、ローカル・システム、およびエッジ・ノードの外部にあるより大きい {{site.data.keyword.edge_notm}} エコシステムの状態の多くの側面を検査します。 `hzn` コマンドを使用して、システムと対話し、所有しているリソースの状態を変更します。

任意のサブコマンド・レベルで `--help` (または `-h`) フラグを使用することで、任意のサブコマンドの詳細も含め、`hzn` コマンドのヘルプを表示できます。 例えば、以下のコマンドを試してください。

```
hzn --help
  hzn node --help
  hzn exchange pattern --help
```
{: codeblock}

`hzn` コマンドで `--verbose` (または `-v`) フラグを使用して、詳細な出力を表示できます。 ほとんどの場合、`hzn` コマンドは、{{site.data.keyword.horizon}} コンポーネントで提供されている REST API の簡便なラッパーであり、`--verbose` フラグを指定することで通常、水面下で行われている REST の対話の詳細が表示されます。 例えば、次のようにします。

```
hzn node list -v
```  
{: codeblock}

このコマンドの出力では、`localhost` URL での 2 つの REST `GET` メソッドの呼び出しが示されており、ローカル {{site.data.keyword.horizon}} エージェントが REST 要求に応答しています。

以下に例を示します。

```
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
{: codeblock}
