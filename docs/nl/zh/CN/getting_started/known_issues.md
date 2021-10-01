---

copyright:
  years: 2019, 2020
lastupdated: "2020-02-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 已知问题与限制  
{: #knownissues}

以下是 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) {{site.data.keyword.semver}} 的已知问题和限制。
{:shortdesc}

## 已知问题

* [大型环境的 ORG 级别配置更改](../hub/configuration.md#largescale_env)应在注册数以千计的边缘节点代理程序前进行。

以下是 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) {{site.data.keyword.version}} 的已知问题和限制。
{:shortdesc}

## 已知问题

* 管理控制台中的服务创建不支持[专用映像存储库](../developing/container_registry.md)。

* **edgeNodeFiles.sh** 的 **-f &lt;directory&gt;** 标志没有预期的效果。 而是在当前目录中收集这些文件。 有关更多信息，请参阅[问题 2187](https://github.com/open-horizon/anax/issues/2187)。变通方法是运行如下命令：

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}

* 在从 Raspberry Pi Raspbian 9 (stretch) 升级到 Raspberry Pi Raspbian 10 (buster) 时，先前安装、配置和正在运行的代理程序可能需要重新安装。 在某些实例中，代理程序进入重新安装可解决的重新启动循环。 多次运行 `ps -aux | grep "anax"` 以观察代理程序 PID 是否在升级后增加。 这指示升级后是否遇到循环。

* 在测试使用 `hzn dev service start` 的服务时，如果相依服务容器使用[模型管理系统](../developing/model_management_system.md) (MMS) 并且如果其位于与顶级服务不同的组织中，那么会发生 403 http 日志错误。

* 如果更改 Exchange 中服务、模式或部署策略的**所有者**或**公共**属性，可能需要最多 5 分钟时间可访问这些资源以查看更改。 同样，当您授予 Exchange 用户管理特权时，可能需要最多 5 分钟时间来将此更改传播到所有 Exchange 实例。 可以通过在 Exchange `config.json` 文件中将 `api.cache.resourcesTtlSeconds` 设置为较低值（缺省为 3000 秒）来减小时间长度，代价是略微降低性能。

* 虽然已为参与区域翻译了 {{site.data.keyword.ieam}} 产品文档，但是英文版将不断更新。 英文版和翻译版之间的差异可出现在翻译周期间。 请检查英文版以查看在发布翻译版后是否解决了任何差异。

* 作为 {{site.data.keyword.ieam}} 安装的一部分，在缺省情况下创建并使用证书，有效期为 90 天。 这暴露出以下问题（[使用这些步骤进行缓解](cert_refresh.md)）
  * Common Services 通过证书管理器自动更新不会正确更新其集成服务和从属服务所使用的叶证书。
  * 边缘节点在安装时自动信任此证书，但是在创建新证书时这些节点未更新，必须使用任何新证书来手动更新。

* 使用具有本地数据库的 {{site.data.keyword.ieam}} 4.2.0 时，如果通过 Kubernetes 调度程序手动或自动删除并重新创建 **cssdb** pod，它将导致 Mongo 数据库的数据丢失。遵循[备份和恢复](../admin/backup_recovery.md)文档以缓解数据丢失。

* 使用具有本地数据库的 {{site.data.keyword.ieam}} 4.2.0 时，如果删除 **create-agbotdb-cluster** 或 **create-exchangedb-cluster** 作业资源，那么此作业将重新执行和重新初始化各自的数据库，从而导致数据丢失。遵循[备份和恢复](../admin/backup_recovery.md)文档以缓解数据丢失。

* 使用本地数据库时，这两个 postgres 数据库或其中一个可能会变得无响应。要解决此问题，请重新启动无响应数据库的所有哨兵和代理。使用受影响的应用程序以及定制资源 (CR) `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` 和 `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy`（Exchange 哨兵示例：`oc rollout restart deploy ibm-edge-exchangedb-sentinel`）修改并运行以下命令。


## 限制

* 对于 {{site.data.keyword.ieam}} {{site.data.keyword.version}}：

  代理程序不支持服务依赖关系之间的双向通信。用作必需服务的服务无法与基于其的服务（需求服务）进行通信。 有关更多信息，请参阅[代理程序不支持服务依赖关系之间的双向通信 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/anax/issues/2095)。 要解决此问题，请除去必需的服务，并向需求服务的服务定义添加必需服务的容器。

* 对于 {{site.data.keyword.ieam}} {{site.data.keyword.semver}}：

  代理程序支持服务依赖关系之间的双向通信。

* 仅[高级手动代理程序安装和注册](../installing/advanced_man_install.md)方法支持安装使用 Fedora 或 SuSE 的边缘设备。

有关 {{site.data.keyword.ieam}} OpenSource 层的未解决问题的完整列表，请复查每个 [Open Horizon 存储库 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 中的 GitHub 问题。
