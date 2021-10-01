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

# 浏览 hzn CLI
{: #exploring-hzn}

在 {{site.data.keyword.horizon}} 边缘节点上，使用 `hzn`命令来检查本地系统状态的许多方面，以及检查边缘节点以外更大的 {{site.data.keyword.edge_notm}}
生态系统的许多方面。 使用 `hzn` 命令与系统交互并更改您拥有的资源的状态。

通过在任何子命令级别上使用 `--help`（或 `-h`）标志，可以获得 `hzn` 命令帮助，包括任何子命令的更多详细信息。 例如，尝试以下命令：

```
hzn --help
hzn node --help
hzn exchange pattern --help
```
{: codeblock}

可以在 `hzn` 命令中使用 `--verbose`（或 `-v`）标志，以提供更详细的输出。 在很多时候，`hzn`
命令是 {{site.data.keyword.horizon}} 组件提供的 REST API 的便利包装器，`--verbose`
标志通常会显示幕后 REST 交互的详细信息。 例如，尝试以下命令：

```
hzn node list -v
```  
{: codeblock}

该命令的输出会显示 `localhost` URL 上的两个 REST `GET` 方法调用（本地 {{site.data.keyword.horizon}} 代理程序通过这些 URL 来响应 REST 请求）。

例如：

```
[verbose] GET http://localhost:8510/node
[verbose] HTTP code: 200
...
[verbose] GET http://localhost:8510/status
[verbose] HTTP code: 200
```  
{: codeblock}
