---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 创建您自己的 Hello world 边缘服务
{: #dev_start_ex}

以下示例使用简单的 `Hello World` 服务来帮助您了解有关为 {{site.data.keyword.edge_devices_notm}} ({{site.data.keyword.ieam}}) 开发的更多信息。通过此示例，您可开发一个支持三种硬件体系结构且使用 {{site.data.keyword.horizon}} 开发工具的边缘服务。
{:shortdesc}

## 准备工作
{: #dev_start_ex_begin}

完成[准备创建边缘服务](service_containers.md)中的先决条件步骤。 因此，应该设置这些环境变量、安装这些命令，并且这些文件应该存在：
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 过程
{: #dev_start_ex_procedure}

此示例属于 [{{site.data.keyword.horizon_open}} ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 开放式源代码项目。遵循[构建并发布您自己的 Hello World 示例边缘服务 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) 中步骤，然后返回此处。

## 后续操作
{: #dev_start_ex_what_next}

* 尝试[使用 {{site.data.keyword.edge_devices_notm}} 开发边缘服务](developing.md)中的其他边缘服务示例。
