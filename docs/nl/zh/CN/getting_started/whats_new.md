---

copyright:
  years: 2019, 2020
lastupdated: "2020-06-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 新增内容
{: #whatsnew}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) {{site.data.keyword.semver}} 介绍：

|解决方案|描述|
|----------|------|
|提高了可伸缩性|将每个 {{site.data.keyword.ieam}} 中心的[扩展](../hub/cluster_sizing.md)提高至 40,000 个边缘端点|
|扩展代理程序支持| 在 Power 单个服务器上可用
| Red Hat 支持| Red Hat OpenShift Container Platform 4.6 上的管理支持
|多租户 SDO|可以使用 [Intel© secure device onboarding](../installing/sdo.md) 在多租户 {{site.data.keyword.ieam}} 安装中为所有组织配置边缘设备。 |
| OCP 支持| 集群代理程序支持 OCP V4.6.16|
| Ubuntu 和 RHEL 支持 | Ubuntu 20.04.2 和 RHEL 8.3 操作系统上的代理程序支持|
| 网络通信| 依赖关系服务容器可以通过网络别名与其父服务容器通信。别名是服务定义的部署配置中为该容器定义的父服务的容器名称 (https://github.com/open-horizon/anax/blob/master/docs/deployment_string.md#deployment-string-fields)。|

引入了 {{site.data.keyword.ieam}} {{site.data.keyword.version}}：

|解决方案|描述|
|----------|------|
|提高了可伸缩性|将每个 {{site.data.keyword.ieam}} 中心的[扩展](../hub/cluster_sizing.md)提高至 30,000 个边缘端点|
|多租户支持|[多租户支持](../admin/multi_tenancy.md)，单个管理中心最多 1,000 个组织|
|保护边缘节点登录|配置边缘设备并将它们与边缘管理中心相关联。 通过 Intel© Secure Device Onboarding [(SDO) 代理程序安装和注册](../installing/sdo.md)提供|
|{{site.data.keyword.ocp_tm}} 支持|利用 [{{site.data.keyword.open_shift_cp}} 4.5 文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/links?url=https%3A%2F%2Fdocs.openshift.com%2Fcontainer-platform%2F4.5%2Fwelcome%2Findex.html) 提高 {{site.data.keyword.ieam}} 工作负载可移植性和灵活性|
|RHEL 操作系统货币支持|提高[边缘节点](../installing/adding_devices.md#suparch-horizon)上的合规性|
|改进了基于控制台的调试|利用直观[用户界面 (UI) 流程](../console/exploring_console.md)简化故障诊断|

请参阅此处的 {{site.data.keyword.ieam}} 免费试用版以开始：https://www.ibm.com/cloud/edge-application-manager/get-started
