---

copyright:
years: 2019
lastupdated: "2019-09-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 安全 
{: #security}

基于 [Open Horizon ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon) 的 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 使用多种安全技术以确保可抵御攻击并保护隐私。 有关 {{site.data.keyword.ieam}} 安全性和角色的更多信息，请参阅：

* [安全与隐私](security_privacy.md)
* [基于角色的访问控制](rbac.md)
* [{{site.data.keyword.edge_notm}} 针对 GDPR 准备就绪状态的注意事项](gdpr.md)
{: childlinks}

有关在尚无自己的 RSA 密钥的情况下创建工作负载签名密钥的更多信息，请参阅[准备创建边缘服务](../developing/service_containers.md)。 在将服务发布到 Exchange 时使用这些密钥对服务进行签名，并启用 {{site.data.keyword.ieam}} 代理程序以验证已启动有效的工作负载。
