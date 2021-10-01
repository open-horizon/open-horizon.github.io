---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 针对边缘服务的 CI-CD 流程
{: #edge_native_practices}

一组演化的边缘服务对有效使用 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 是至关重要的，健壮的持续集成和持续部署 (CI/CD) 流程是关键组成部分。 

使用此内容来布置可供您用于创建自己的 CI/CD 流程的构建块。 然后，在 [`open-horizon/examples` 存储库 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples) 中进一步了解此流程。

## 配置变量
{: #config_variables}

作为边缘服务开发人员，请考虑正在开发中的服务容器大小。 基于该信息，您可能需要将服务功能划分到单独的容器。 在这种情况下，用于测试的配置变量可帮助模拟来自尚未开发的容器的数据。 在 [cpu2evtstreams 服务定义文件 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json) 中，您可以看到像 **PUBLISH** 和 **MOCK** 一样的输入变量。 如果检查 `service.sh` 代码，您会发现它使用这些配置变量和其他配置变量来控制其行为。 **PUBLISH** 控制代码是否尝试将消息发送到 IBM Event Streams。 **MOCK** 控制 service.sh 是否尝试联系 REST API 及其相依服务（cpu 和 gps）或 `service.sh` 是否创建假数据。

在服务部署时，您可以通过在节点定义中或在 `hzn register` 命令上指定配置变量值来覆盖配置变量缺省值。

## 交叉编译
{: #cross_compiling}

您可以使用 Docker 为单个 amd64 机器中的多个体系结构构建容器化服务。 同样地，您可以使用支持交叉编译的编译型编程语言（如 Go）来开发边缘服务。 例如，如果要在 Mac（amd64 体系结构设备）上为 arm 设备 (Raspberry Pi) 编写代码，您可能需要向目标 arm 构建指定如 GOARCH 之类参数的 Docker 容器。 此设置可防止部署错误。 请参阅 [open-horizon gps 服务 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/tree/master/edge/services/gps)。

## 测试
{: #testing}

频繁的自动测试是开发流程的一个重要部分。 为方便测试，您可以使用 `hzn dev service start` 命令在 Horizon 代理程序模拟环境中运行您的服务。 此方法在安装和注册完整的 Horizon 代理程序可能会有问题的 DevOps 环境中也很有用。 此方法使用 **make test** 目标在 `open-horizon examples` 存储库中自动执行服务测试。 请参阅 [make test 目标 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30)。


运行 **make test** 以构建和运行使用 **hzn dev service start** 的服务。 在该服务运行后，[serviceTest.sh ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) 监视服务日志以找到指示该服务正在正常运行的数据。

## 测试部署
{: #testing_deployment}

在您开发新服务版本时，理想的做法是访问全面、真实的测试。 为此，您可以将服务部署到边缘节点；但是，因为这是测试，您可能不希望最初就将服务部署到所有边缘节点。

为此，请创建仅引用新服务版本的部署策略或模式。 然后，使用这个新策略或模式注册您的测试节点。 如果使用策略，一个选项是在边缘节点上设置属性。 例如，"name": "mode"、"value": "testing"，并将该约束添加到您的部署策略 ("mode == testing")。 这使您能够确保为测试而留出的节点接收服务的新版本。

**注**：您还可以从管理控制台创建部署策略或模式。请参阅[使用管理控制台](../console/accessing_ui.md)。

## 生产部署
{: #production_deployment}

将服务的新版本从测试环境移至生产环境后，会遇到在测试期间没遇到的问题。 您的部署策略或模式回滚设置对解决这些问题很有用。 在模式或部署策略 `serviceVersions` 部分中，您可以指定服务的多个较早版本。 如果新版本存在错误，请针对要回滚到的边缘节点为每个版本提供优先级。 除了将优先级分配到每个回滚版本，您可以在退回到指定服务的较低优先级版本前指定重新尝试次数和持续时间之类的内容。有关特定语法，请参阅[此部署策略示例 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json)。

## 查看边缘节点
{: #viewing_edge_nodes}

在将服务的新版本部署到节点后，能够轻松监视边缘节点的运行状态是非常重要的。 将 {{site.data.keyword.ieam}} {{site.data.keyword.gui}} 用于此任务。 例如，当您处于[测试部署](#testing_deployment)或[生产部署](#production_deployment)流程中时，您可以快速搜索使用部署策略的节点，或存在错误的节点。

## 迁移服务
{: #migrating_services}

有时您可能需要将服务、模式或策略从 {{site.data.keyword.ieam}} 的一个实例移至另一个实例。 同样地，您可能需要将服务从一个 Exchange 组织移至另一个 Exchange 组织。 如果您已将 {{site.data.keyword.ieam}} 的新实例安装到其他主机环境，这可能会发生。 或者，如果您有两个 {{site.data.keyword.ieam}} 实例（一个专用于开发，另一个专用于生产），您可能需要移动服务。 为促进此流程，您可以在 open-horizon examples 存储库中使用 [`loadResources` 脚本 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/tools/loadResources)。

## 使用 Travis 自动执行拉取请求测试
{: #testing_with_travis}

通过使用 [Travis CI ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://travis-ci.com)，每当对 GitHub 存储库打开拉取请求 (PR) 时，您可以自动执行测试。 

继续阅读此内容以了解如何利用 Travis 和 open-horizon 示例 GitHub 存储库中的方法。

在示例存储库中，Travis CI 用于构建、策略和发布样本。 在 [`.travis.yml` 文件 ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/.travis.yml) 中，设置虚拟环境以使用 hzn、Docker 和 [qemu ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/multiarch/qemu-user-static) 作为 Linux amd64 机器运行，以在多个体系结构上构建。

在此场景中，还安装 kafkacat 以允许 cpu2evtstreams 将数据发送到 IBM Event Streams。 与使用命令行类似，Travis 可使用 `EVTSTREAMS_TOPIC` 和 `HZN_DEVICE_ID` 之类的环境变量以与样本边缘服务配合使用。 HZN_EXCHANGE_URL 设置为指向用于发布任何已修改服务的暂存交换。

然后，[travis-find ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/tools/travis-find) 脚本用于识别已打开的拉取请求已修改的服务。

如果已修改样本，那么该服务的 **makefile** 中的 `test-all-arches` 目标运行。 在受支持体系结构的 qemu 容器运行的情况下，通过在构建和测试前立即设置 `ARCH` 环境变量，跨体系结构构建与此 **makefile** 目标一起运行。 

`hzn dev service start` 命令运行边缘服务，[serviceTest.sh ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) 文件监视服务日志以确定服务是否正确运行。

请参阅 [helloworld Makefile ![在新的选项卡中打开](../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24) 以查看专用的 `test-all-arches` Makefile 目标。

以下场景展示了更深入的端到端测试。 如果其中一个已修改的样本包含 `cpu2evtstreams`，那么可在后台监视 IBM Event Streams 的实例并对其进行检查以找到 HZN_DEVICE_ID。 仅当在从 cpu2evtstreams 主题读取的数据中找到 **travis-test** 节点标识时，它才可以通过测试并添加到所有传递服务的列表中。 这需要设置为秘密环境变量的 IBM Event Streams API 密钥和代理 URL。

在合并 PR 后，此过程重复，传递服务的列表用于标识哪些服务可发布到 Exchange。 此示例中使用的 Travis 秘密环境变量包含向 Exchange 推送、签署和发布服务所需的所有内容。 这包括 Docker 凭证、HZN_EXCHANGE_USER_AUTH 以及使用 `hzn key create` 命令可获取的加密签名密钥对。 为将签名密钥另存为安全环境变量，它们必须使用 base64 进行编码。

通过功能测试的服务的列表用于标识哪些服务应使用专用的发布 `Makefile` 目标进行发布。 请参阅 [helloworld 样本 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45)。

因为已构建并测试服务，此目标将所有体系结构中的服务、服务策略、模式和部署策略发布到 Exchange。

**注**：此外，您可以从管理控制台执行许多这些任务。请参阅[使用管理控制台](../console/accessing_ui.md)。

