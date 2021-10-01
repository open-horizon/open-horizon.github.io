---

copyright:
years: 2020
lastupdated: "2020-10-7"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# GDPR 注意事项

## 声明
{: #notice}
<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->

本文档旨在帮助您准备 GDPR 准备就绪状态。 其提供可配置的 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 功能信息，以及在针对 GDPR 准备组织时要考虑的产品使用的各个方面。 本信息并非详尽列表。 客户可以通过多种不同的方式选择和配置功能，并以多种方式与第三方应用程序和系统一起使用产品。

<p class="ibm-h4 ibm-bold">客户负责确保其自己符合各种法律和法规，包括《欧盟通用数据保护条例》。 对于识别和解释可能影响客户的业务的任何相关法律和法规以及客户为遵守此类法律和法规而可能需要执行的任何操作，客户单独负责向主管法律顾问寻求建议。</p>

<p class="ibm-h4 ibm-bold">此处描述的产品、服务和其他功能并不适合所有客户情况并且可能限制可用性。 IBM 不提供法律、会计或审计建议，或者表示或保证其服务或产品确保客户遵守任何法律或法规。</p>

## 目录

* [GDPR](#overview)
* [适用于 GDPR 的产品配置](#productconfig)
* [数据生命周期](#datalifecycle)
* [数据处理](#dataprocessing)
* [限制使用个人数据的功能](#datasubjectrights)
* [附录](#appendix)

## GDPR
{: #overview}

<!-- This is boilerplate text provided by the GDPR team. It cannot be changed. -->
欧盟 (EU) 于 2018 年 5 月 25 日起采用《通用数据保护条例》(GDPR)。

### 为何 GDPR 重要？

GDPR 建立了更强大的数据保护控制框架，用于处理个人数据。 GDPR 将带来：

* 新的和增强的个人权限
* 个人数据的扩展定义
* 公司和组织在处理个人数据时的新义务
* 对不合规情况进行重大经济处罚
* 强制数据违规通知

IBM 已制定全球准备计划，旨在使 IBM 的内部流程和商品符合 GDPR 的规定。

### 更多信息

* [EU GDPR 信息门户网站 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://gdpr.eu/)
*  [ibm.com/GDPR Web 站点![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/data-responsibility/gdpr/)

## 产品配置 - GDPR 准备就绪状态的注意事项
{: #productconfig}

以下部分描述 {{site.data.keyword.ieam}} 的各个方面，并提供有关帮助客户满足 GDPR 需求的功能的信息。

### 数据生命周期
{: #datalifecycle}

{{site.data.keyword.ieam}} 是用于开发和管理本地、容器化应用程序的应用程序。 这是用于管理边缘处的容器工作负载的集成环境。 其包含容器编排器 Kubernetes、边缘节点代理程序专用映像注册表、管理控制台、边缘节点代理程序和监视框架。

例如，{{site.data.keyword.ieam}} 主要处理与应用程序的配置和管理相关的技术数据，其中某些可能受 GDPR 管辖。 {{site.data.keyword.ieam}} 还处理有关管理应用程序的用户的信息。 在本文中描述此数据以了解负责满足 GDPR 需求的客户。

在 {{site.data.keyword.ieam}} 上的本地或远程文件系统中作为配置文件或者在数据库中持久存储此数据。 为在 {{site.data.keyword.ieam}} 上运行而开发的应用程序可能使用符合 GDPR 的其他格式的个人数据。 用于保护和管理数据的机制也适用于在 {{site.data.keyword.ieam}} 上运行的应用程序。 可能需要更多机制来管理和保护在 {{site.data.keyword.ieam}} 上运行的应用程序所收集的个人数据。

要了解 {{site.data.keyword.ieam}} 数据流，您必须了解 Kubernetes、Docker 和操作程序的工作方式。 这些开放式源代码组件是 {{site.data.keyword.ieam}} 的基础。 使用 {{site.data.keyword.ieam}} 以将应用程序容器（边缘服务）的实例放置在边缘节点上。 边缘服务包含有关应用程序的详细信息，而 Docker 映像包含应用程序需要运行的所有软件包。

{{site.data.keyword.ieam}} 包含一组开放式源代码边缘服务示例。 要查看所有 {{site.data.keyword.ieam}} Chart 的列表，请参阅 [open-horizon/examples ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples){:new_window}。 客户负责针对开放式源代码软件确定和实施任何相应的 GDPR 控制。

### 通过 {{site.data.keyword.ieam}} 的数据流的类型

{{site.data.keyword.ieam}} 处理多种类别的可视为个人数据的技术数据，例如：

* 管理员或操作员用户标识和密码
* IP 地址
* Kubernetes 节点名

在本文的稍后章节中描述了有关如何收集和创建、存储、访问、保护、记录和删除此技术数据的信息。

### 用于在线联系 IBM 的个人数据

{{site.data.keyword.ieam}} 客户可通过各种方式在线向 IBM 提交有关 {{site.data.keyword.ieam}} 主题的评论、反馈和请求，主要是：

* 公共 {{site.data.keyword.ieam}} Slack 社区
* {{site.data.keyword.ieam}} 产品文档页面上的公共评论区域
* dW Answers 的 {{site.data.keyword.ieam}} 空间中的公共评论

通常，仅使用客户名称和电子邮件地址来支持联系人主题的个人回复。 此个人数据使用符合 [IBM 在线隐私声明 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/privacy/us/en/){:new_window}。

### 认证

{{site.data.keyword.ieam}} 认证管理器接受来自 {{site.data.keyword.gui}} 的用户凭证并将凭证转发给后端 OIDC 提供程序，此程序针对企业目录验证用户凭证。 然后，OIDC 提供程序向认证管理器返回认证 cookie (`auth-cookie`) 以及 JSON Web 令牌 (`JWT`) 的内容。 除了认证请求时的组成员资格，JWT 令牌持久存储用户标识和电子邮件地址之类的信息。 然后，将此认证 cookie 发送回 {{site.data.keyword.gui}}。 会话期间，cookie 将刷新。 在注销 {{site.data.keyword.gui}} 或关闭 Web 浏览器后，其保持有效 12 个小时。

对于从 {{site.data.keyword.gui}} 生成的所有后续认证请求，前端 NodeJS 服务器解码请求中的可用认证 cookie，并通过调用认证管理器来验证请求。

{{site.data.keyword.ieam}} CLI 需要用户提供 API 密钥。 使用 `cloudctl` 命令创建 API 密钥。

**cloudctl**、**kubectl** 和 **oc** CLI 还需要凭证以访问集群。 这些凭证可从管理控制台获取并且在 12 小时后到期。

### 角色映射

{{site.data.keyword.ieam}} 支持基于角色的访问控制 (RBAC)。 在角色映射阶段中，认证阶段中提供的用户名将映射到用户或组角色。 角色用于授权已认证的用户可执行的活动。 请参阅[基于角色的访问控制](rbac.md)以获取有关 {{site.data.keyword.ieam}} 角色的详细信息。

### Pod 安全性

Pod 安全策略用于设置 pod 可执行的或可访问的管理中心或边缘集群控制。 有关 pod 的更多信息，请参阅[安装管理中心](../hub/hub.md)和[边缘集群](../installing/edge_clusters.md)。

## 数据处理
{: #dataprocessing}

{{site.data.keyword.ieam}} 用户可控制通过系统配置处理和保护与配置和管理相关的技术数据的方式。

* 基于角色的访问控制 (RBAC) 控制用户可访问的数据和功能。

* Pod 安全策略用于设置针对 pod 可执行的操作或可访问的内容的集群级别控制。

* 使用 `TLS` 保护传输中的数据。 `HTTPS`（`TLS` 底层）用于保护用户客户机与后端服务之间的数据传输。 用户可指定根证书以在安装期间使用。

* 使用 `dm-crypt` 加密数据以支持静态数据保护。

* 用于日志记录 (ELK) 和监视 (Prometheus) 的数据保留时间段可配置，并且通过提供的 API 支持数据删除。

用于管理和保护 {{site.data.keyword.ieam}} 技术数据的这些相同机制可用于管理和保护用户开发或用户提供的应用程序的个人数据。 客户可开发其自己的功能以实施进一步控制。

有关证书的更多信息，请参阅[安装 {{site.data.keyword.ieam}}](../hub/installation.md)。

## 限制使用个人数据的功能
{: #datasubjectrights}

使用本文档中概述的工具，{{site.data.keyword.ieam}} 支持用户限制在应用程序中使用被视为个人数据的任何技术数据。

根据 GDPR，用户有权访问、修改和限制处理。 请参阅本文档的其他部分以进行控制：
* 访问权
  * {{site.data.keyword.ieam}} 管理员可以使用 {{site.data.keyword.ieam}} 功能以向个人提供其数据的访问权。
  * {{site.data.keyword.ieam}} 管理员可以使用 {{site.data.keyword.ieam}} 功能以向个人提供有关 {{site.data.keyword.ieam}} 所收集和保留的有关个人的数据的信息。
* 修改权
  * {{site.data.keyword.ieam}} 管理员可以使用 {{site.data.keyword.ieam}} 功能以允许个人修改或纠正其数据。
  * {{site.data.keyword.ieam}} 管理员可以使用 {{site.data.keyword.ieam}} 功能以针对其纠正个人的数据。
* 限制处理权
  * {{site.data.keyword.ieam}} 管理员可以使用 {{site.data.keyword.ieam}} 功能以停止处理个人的数据。

## 附录 - {{site.data.keyword.ieam}} 记录的数据
{: #appendix}

{{site.data.keyword.ieam}} 作为应用程序处理可视为个人数据的多种类别的技术数据：

* 管理员或操作员用户标识和密码
* IP 地址
* Kubernetes 节点名。 

{{site.data.keyword.ieam}} 还处理有关管理在 {{site.data.keyword.ieam}} 上运行的应用程序的用户的信息，并且可引入对于应用程序未知其他类别的个人数据。

### {{site.data.keyword.ieam}} 安全性

* 记录的数据
  * 已登录用户的用户标识、用户名和 IP 地址
* 记录数据的时间
  * 使用登录请求
* 记录数据的位置
  * 在 `/var/lib/icp/audit` 的审计日志中
  * 在 `/var/log/audit` 的审计日志中
  * Exchange 日志，地址为：
* 如何删除数据
  * 搜索数据并从审计日志中删除记录

### {{site.data.keyword.ieam}} API

* 记录的数据
  * 容器日志中客户的用户标识、用户名和 IP 地址
  * `etcd` 服务器中 Kubernetes 集群状态数据
  * `etcd` 服务器中的 OpenStack 和 VMware 凭证
* 记录数据的时间
  * 使用 API 请求
  * 从 `credentials-set` 命令存储的凭证
* 记录数据的位置
  * 在容器日志、Elasticsearch 和 `etcd` 服务器中。
* 如何删除数据
  * 从容器删除容器日志（`platform-api` 和 `platform-deploy`），或者从 Elasticsearch 删除特定于用户的日志条目。
  * 使用 `etcdctl rm` 命令，清除所选 `etcd` 键值对。
  * 通过调用 `credentials-unset` 命令，除去凭证。


有关更多信息，请参阅：

  * [Kubernetes 日志记录 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/concepts/cluster-administration/logging/){:new_window}
  * [etcdctl ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/coreos/etcd/blob/master/etcdctl/READMEv2.md){:new_window}

### {{site.data.keyword.ieam}} 监视

* 记录的数据
  * IP 地址、pod 名称、发行版和映像
  * 从客户开发的应用程序提取的数据可能包含个人数据
* 记录数据的时间
  * 来自配置的目标的 Prometheus 提取度量
* 记录数据的位置
  * 在 Prometheus 服务器或配置的持久卷中
* 如何删除数据
  * 使用 Prometheus API 搜索并删除数据

有关更多信息，请参阅 [Prometheus 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://prometheus.io/docs/introduction/overview/){:new_window}。


### {{site.data.keyword.ieam}} Kubernetes

* 记录的数据
  * 集群部署的拓扑（控制器、工作程序、代理和 va 的节点信息）
  * 服务配置（k8s 配置映射）和密钥（k8s 密钥）
  * apiserver 日志中的用户标识
* 记录数据的时间
  * 部署集群的时间
  * 从 Helm 目录部署应用程序的时间
* 记录数据的位置
  * `etcd` 中容器部署的拓扑
  * `etcd` 中已部署的应用程序的配置和密钥
* 如何删除数据
  * 使用 {{site.data.keyword.ieam}} {{site.data.keyword.gui}}
  * 搜索并使用 k8s {{site.data.keyword.gui}} (`kubectl`) 或 `etcd` REST API 删除数据
  * 使用 Elasticsearch API 搜索并删除 apiserver 日志数据

修改 Kubernetes 集群配置或删除集群数据时，请谨慎操作。

  有关更多信息，请参阅 [Kubernetes kubectl ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}。

### {{site.data.keyword.ieam}} Helm API

* 记录的数据
  * 用户名和角色
* 记录数据的时间
  * 用户检索添加到团队的 Chart 或存储库的时间
* 记录数据的位置
  * helm-api 部署日志，Elasticsearch
* 如何删除数据
  * 使用 Elasticsearch API，搜索并删除 helm-api 数据

### {{site.data.keyword.ieam}} 服务代理

* 记录的数据
  * 用户标识（仅限调试日志级别 10，而非缺省日志级别）
* 记录数据的时间
  * 向服务代理程序生成 API 请求的时间
  * 服务代理访问服务目录时
* 记录数据的位置
  * 服务代理容器日志，Elasticsearch
* 如何删除数据
  * 搜索并删除使用 Elasticsearch API 的 apiserver 日志
  * 搜索并删除 apiserver 容器中的日志
      ```
      kubectl logs $(kubectl get pods -n kube-system | grep  service-catalogapiserver | awk '{print $1}') -n kube-system | grep admin
      ```
      {: codeblock}


  有关更多信息，请参阅 [Kubernetes kubectl ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://kubernetes.io/docs/reference/kubectl/overview/){:new_window}。
