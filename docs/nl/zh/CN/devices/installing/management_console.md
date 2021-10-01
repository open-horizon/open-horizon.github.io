---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 使用 {{site.data.keyword.edge_notm}} 控制台
{: #accessing_ui}

使用控制台来执行边缘计算管理功能。 
 
## 导航到 {{site.data.keyword.edge_notm}} 控制台

1. 通过浏览到 `https://<cluster-url>/edge` 导航到 {{site.data.keyword.edge_notm}} 控制台，其中，`<cluster-url>` 是集群的外部入口。
2. 输入您的用户凭证。 此时将显示 {{site.data.keyword.mcm}} 登录页面。
3. 在浏览器地址栏中，从 URL 末尾移除 `/multicloud/welcome` 并添加 `/edge`，然后按 **Enter** 键。 此时将显示 {{site.data.keyword.edge_notm}} 页面。

## 受支持的浏览器

{{site.data.keyword.edge_notm}} 已成功地使用这些浏览器进行测试。

|平台|受支持的浏览器|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - 用于 Windows 的最新版本</li><li>Google Chrome - 用于 Windows 的最新版本</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - 用于 Mac 的最新版本</li><li>Google Chrome - 用于 Mac 的最新版本</li></ul>|
{: caption="表 1. {{site.data.keyword.edge_notm}} 中受支持的浏览器" caption-side="top"}


## 浏览 {{site.data.keyword.edge_notm}} 控制台
{: #exploring-management-console}

{{site.data.keyword.edge_notm}} 控制台功能包括：

* 用户友好的登录，具有外围站点链接以获取强大支持
* 丰富的可视性和管理功能：
  * Chart 综合视图，包括节点状态、体系结构和错误信息
  * 错误详细信息以及解决方案支持链接
  * 位置和过滤内容，包括有关以下内容的信息： 
    * 所有者
    * 体系结构 
    * 脉动信号（例如，最近 10 分钟、今天等）
    * 节点状态（活动、不活动、发生错误等）
    * 部署类型（策略或模式）
  * 有关 Exchange 边缘节点的实用详细信息，包括：
    * 属性
    * 约束 
    * 部署
    * 活动服务

* 强大的视图功能

  * 可以快速查找和过滤： 
    * 所有者
    * 体系结构
    * 版本
    * 公共（true 或 false）
  * 列表或卡服务视图
  * 共享一个名称的分组服务
  * Exchange 中每个服务的详细信息，包括： 
    * 属性
    * 约束
    * 部署
    * 服务变量
    * 服务依赖性
  
* 部署策略管理

  * 可以快速查找和过滤：
    * 策略标识
    * 所有者
    * 标签
  * 从 Exchange 部署任何服务
  * 将属性添加到部署策略
  * 用于构建表达式的约束构建器 
  * 直接将约束写入 JSON 的高级方式
  * 可以调整回滚部署版本和节点运行状况设置
  * 查看和编辑策略详细信息，包括：
    * 服务和部署属性
    * 约束
    * 回滚
    * 节点运行状况设置
  
