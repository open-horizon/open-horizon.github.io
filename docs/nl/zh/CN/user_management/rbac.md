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

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 支持多种角色。 您的角色决定了您可以执行的操作。
{:shortdesc}

## 组织
{: #orgs}

{{site.data.keyword.ieam}} 通过组织支持多租户常规概念，其中，每个租户具有其自己的组织。 组织分隔资源；因此，每个组织中的用户无法创建或修改不同组织中的资源。 此外，仅组织中的用户可查看此组织中的资源（除非资源标记为公共）。 标记为公共的资源是可以跨组织查看的唯一资源。

IBM 组织提供预定义的服务和模式。 虽然此组织中的资源为公共，但是并非旨在保存 {{site.data.keyword.ieam}} 管理中心中的所有公共内容。

缺省情况下，在 {{site.data.keyword.ieam}} 安装期间使用选择的名称创建一个组织。 您可以根据需要创建其他组织。 有关向管理中心添加组织的更多信息，请参阅[多租户](../admin/multi_tenancy.md)。

## 身份
{: #ids}

{{site.data.keyword.ieam}} 中有四种类型的身份：

* 身份和访问权管理 (IAM) 用户。 所有 {{site.data.keyword.ieam}} 组件均可识别 IAM 用户：UI、Exchange、**hzn** CLI、**cloudctl** CLI、**oc** CLI 和 **kubectl** CLI。
  * IAM 提供了 LDAP 插件，因此连接到 IAM 的 LDAP 用户的行为类似 IAM 用户
  * IAM API 密钥（与 **hzn** 命令搭配使用）的行为类似 IAM 用户
* 仅限 Exchange 用户：Exchange root 用户是这类用户的示例。 您通常无需创建其他本地仅限 Exchange 用户。 作为最佳实践，在 IAM 中管理用户，并使用这些用户凭证（或与这些用户相关联的 API 密钥）来向 {{site.data.keyword.ieam}} 进行认证。
* Exchange 节点（边缘设备或边缘集群）
* Exchange agbot

### 基于角色的访问控制 (RBAC)
{: #rbac_roles}

{{site.data.keyword.ieam}} 包含以下角色：

| **角色**    | **访问权**    |  
|---------------|--------------------|
| IAM 用户 | 通过 IAM，可指定这些管理中心角色：集群管理员、管理员、操作员、编辑者和查看者。 在将用户或用户组添加到 IAM 团队时，向其分配 IAM 角色。 资源的团队访问权可由 Kubernetes 名称空间进行控制。 也可以使用 **hzn exchange** CLI 为 IAM 用户指定以下任何 Exchange 角色。 |
| Exchange root 用户 | 在 Exchange 中具有无限特权。 此用户在 Exchange 配置文件中定义。 可以根据需要将其禁用。 |
| Exchange 中心管理员用户 | 可查看组织的列表、查看组织中的用户以及创建或删除组织。 |
| Exchange 组织管理用户 | 具有组织中无限的 Exchange 特权。 |
| Exchange 用户 | 可以在组织中创建 Exchange 资源（节点、服务、模式和策略）。 可以更新或删除此用户拥有的资源。 可以读取该组织中的所有服务、模式和策略，以及其他组织中的公共服务和模式。 可以读取此用户所拥有的节点。 |
| Exchange 节点 | 可以读取 Exchange 中其自己的节点，读取该组织中的所有服务、模式和策略，以及其他组织中的公共服务和模式。 这些只是边缘节点中应该保存的凭证，因为这些凭证具有操作边缘节点所需的最低权限。|
| Exchange agbot | IBM 组织中的 agbot 可以读取所有组织中的所有节点、服务、模式和策略。 |
{: caption="表 1. RBAC 角色" caption-side="top"}
