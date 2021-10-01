---

copyright:
years: 2020
lastupdated: "2020-02-6"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 使用模型管理的 Hello World
{: #model_management_system}

此示例帮助您了解如何开发使用模型管理系统 (MMS) 的 {{site.data.keyword.edge_service}} ({{site.data.keyword.ieam}})。 您可以使用此系统以部署和更新在边缘节点上运行的边缘服务所使用的学习机器模型。
{:shortdesc}

## 准备工作
{: #mms_begin}

完成[准备创建边缘服务](service_containers.md)中的先决条件步骤。 因此，应该设置这些环境变量、安装这些命令，并且这些文件应该存在：

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## 过程
{: #mms_procedure}

此示例属于 [{{site.data.keyword.horizon_open}} ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 开放式源代码项目。 执行 [Creating Your Own Hello MMS Edge Service![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md) 中的步骤，然后返回到此处。

## 后续操作
{: #mms_what_next}

* 在[为设备开发边缘服务](developing.md)中尝试使用其他边缘服务示例。

## 进一步阅读资料

* [模型管理详细信息](../developing/model_management_details.md)
