---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU 到 {{site.data.keyword.message_hub_notm}} 服务
{: #cpu_msg_ex}

此示例收集 CPU 负载百分比信息以发送到 {{site.data.keyword.message_hub_notm}}。 使用此示例来帮助您开发自己的边缘应用程序，将数据发送到云服务。
{:shortdesc}

## 准备工作
{: #cpu_msg_begin}

完成[准备创建边缘服务](service_containers.md)中的先决条件步骤。 因此，应该设置这些环境变量、安装这些命令，并且这些文件应该存在：

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 过程
{: #cpu_msg_procedure}

此示例属于 [{{site.data.keyword.horizon_open}} ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/) 开放式源代码项目。请遵循[构建并发布自己版本的 CPU 到 IBM Event Streams 边缘服务 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service) 中的步骤，然后返回此处。

## 您在此示例中学习的内容

### 必需的服务

cpu2evtstreams 边缘服务是取决于其他两个边缘服务（**cpu** 和 **gps**）来完成其任务的服务示例。 您可以在 **horizon/service.definition.json** 文件的 **requiredServices** 部分中查看这些依赖关系的详细信息：

```json
    "requiredServices": [
        {
            "url": "ibm.cpu",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        }
    ],
```

### 配置变量
{: #cpu_msg_config_var}

**cpu2evtstreams** 服务需要一些配置才能运行。 边缘服务可声明配置变量，指示其类型并提供缺省值。 您可以在 **horizon/service.definition.json** 的 **userInput** 部分中查看这些配置变量：

```json  
    "userInput": [
        {
            "name": "EVTSTREAMS_API_KEY",
            "label": "The API key to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",
            "label": "The comma-separated list of URLs to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",
            "label": "The base64-encoded self-signed certificate to use when sending messages to your ICP instance of IBM Event Streams. Not needed for IBM Cloud Event Streams.",
            "type": "string",
            "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",
            "label": "The topic to use when sending messages to your instance of IBM Event Streams",
            "type": "string",
            "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",
            "label": "the number of samples to read before calculating the average",
            "type": "int",
            "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",
            "label": "the number of seconds between samples",
            "type": "int",
            "defaultValue": "2"
        },
        {
            "name": "MOCK",
            "label": "mock the CPU sampling",
            "type": "boolean",
            "defaultValue": "false"
        },
        {
            "name": "PUBLISH",
            "label": "publish the CPU samples to IBM Event Streams",
            "type": "boolean",
            "defaultValue": "true"
        },
        {
            "name": "VERBOSE",
            "label": "log everything that happens",
            "type": "string",
            "defaultValue": "1"
        }
    ],
```

在边缘节点上启动边缘服务时，类似这些的用户输入配置变量必需具有值。 这些值可以来自以下任何源（按照此优先顺序）：

1. 使用 **hzn register -f** 标志指定的用户输入文件
2. Exchange 中边缘节点资源的 **userInput** 部分
3. Exchange 中模式或部署策略资源的 **userInput** 部分
4. Exchange 中服务定义资源所指定的缺省值

向此服务注册边缘设备时，您提供了一个 **userinput.json** 文件，该文件指定了一些没有缺省值的配置变量。

### 开发提示
{: #cpu_msg_dev_tips}

将帮助测试和调试服务的配置变量合并到服务中会非常有用。例如，此服务的元数据 (**service.definition.json**) 和代码 (**service.sh**) 使用以下配置变量：

* **VERBOSE** 会增加运行时记录的信息量
* **PUBLISH** 控制代码是否尝试将消息发送到 {{site.data.keyword.message_hub_notm}}
* **MOCK** 控制 **service.sh** 是尝试调用其依赖项的 REST API（**cpu** 和 **gps** 服务）还是改为创建 mock 数据自身。

模拟所依赖的服务虽然是可选功能，但是在隔离必需服务的情况下有助于开发和测试组件。 还可以使用此方法，在不存在硬件传感器或传动结构的设备类型上开发服务。

开发和测试期间，可以方便地关闭与云服务的交互，以避免不必要的费用，并帮助在合成 devops 环境中进行测试。

## 后续操作
{: #cpu_msg_what_next}

* 尝试[使用 {{site.data.keyword.edge_devices_notm}} 开发边缘服务](developing.md)中的其他边缘服务示例。
