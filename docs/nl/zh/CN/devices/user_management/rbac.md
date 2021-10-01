---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 基于角色的访问控制
{: #rbac}

{{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} 支持多种角色。 您的角色决定了您可以执行的操作。
{:shortdesc}

## 组织
{: #orgs}

{{site.data.keyword.ieam}} 中的组织用于分隔对资源的访问。 除非将资源显式标记为公共，否则组织的资源只能由该组织查看。标记为公共的资源是可以跨组织查看的唯一资源。

IBM 组织用于为您提供预定义的服务和模式。

在 {{site.data.keyword.ieam}} 中，组织名称是集群的名称。

## 身份
{: #ids}

{{site.data.keyword.ieam}} 中有三种类型的身份：

* 有两种类型的用户。用户可以访问 {{site.data.keyword.ieam}} 控制台和 Exchange。
  * 身份和访问权管理 (IAM) 用户。{{site.data.keyword.ieam}} Exchange 能识别 IAM 用户。
    * IAM 提供了 LDAP 插件，因此连接到 IAM 的 LDAP 用户的行为类似 IAM 用户
    * IAM API 密钥（与 **hzn** 命令搭配使用）的行为类似 IAM 用户
  * 本地 Exchange 用户：Exchange root 用户是这类用户的示例。您通常无需创建其他本地 Exchange 用户。
* 节点（边缘设备或边缘集群）
* AgBot

### 基于角色的访问控制 (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} 包含以下角色：

| **角色**    | **访问权**    |  
|---------------|--------------------|
| Exchange root 用户 | 在 Exchange 中具有无限特权。此用户在 Exchange 配置文件中定义。可以根据需要将其禁用。|
| 管理员用户或 API 密钥 | 在组织中具有无限特权。|
| 非管理员用户或 API 密钥 | 可以在组织中创建 Exchange 资源（节点、服务、模式和策略）。可以更新或删除此用户拥有的资源。可以读取该组织中的所有服务、模式和策略，以及其他组织中的公共服务和模式。|
| 节点 | 可以读取 Exchange 中其自己的节点，读取该组织中的所有服务、模式和策略，以及其他组织中的公共服务和模式。|
| agbot | IBM 组织中的 agbot 可以读取所有组织中的所有节点、服务、模式和策略。|
{: caption="表 1. RBAC 角色" caption-side="top"}
