---

copyright:
  years: 2020
lastupdated: "2020-04-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 部署策略用例
{: #developing_edge_services}

此部分重点说明描述这些策略类型的真实场景。

<img src="../images/edge/04_Defining_an_edge_policy.svg" style="margin: 3%" alt="定义边缘策略">

考虑客户已经安装了 ATM 摄像头来检测盗窃（该客户还具有其他类型的边缘节点）。 客户使用 walk-up (still) 和 drive-through (motion) ATM 组合。 在此情况下，有两个第三方服务可用。 每个服务都可以在 ATM 上检测可疑活动，但客户测试已确定服务 atm1 更可靠地检测到 walk-up (still) ATM 处的可疑活动，而服务 atm2 更可靠地检测到 drive-through (motion) ATM 处的可疑活动。

这就是策略的表达方式，以实现期望的服务和模型部署：

* 在所有 walk-up ATM 上的节点策略中设置属性：properties: `camera-type: still`, `atm-type: walk-up`
* 在所有 drive-through ATM 上的节点策略中设置属性：properties: `camera-type: motion`, `atm-type: drive-thru`
* （可选）由 atm1 和 atm2 的第三方开发者在服务策略中设置约束：constraints: `(Optional)`
* 在 atm1 服务的客户设置的部署策略中设置约束：constraints: `camera-type == still`
* 在 atm2 服务的客户设置的部署策略中设置约束：constraints: `camera-type == motion`

注：在引用部署策略时，`hzn` 命令有时使用术语业务策略。

节点策略（由设置 ATM 的技术人员设置）声明有关每个节点的事实，例如，ATM 是否具有摄像头以及 ATM 所在的位置类型。 技术人员可轻松确定和指定此信息。

服务策略是关于服务正确运行所需满足的条件的声明（在本示例中是摄像头）。 第三方服务开发者知道此信息，即使他们不知道哪个客户正在使用。 如果客户拥有其他没有摄像头的 ATM，那么由于这种限制，这些服务不会部署到这些 ATM。

部署策略由客户 CIO（或管理其边缘光纤网的人员）定义。 这定义了业务的整体服务部署。 在此情况下，CIO 表示期望的服务部署结果是，应该将 atm1 用于 walk-up ATM，将 atm2 用于 drive-through ATM。

## 节点策略
{: #node_policy}

可以将策略连接到节点。 节点所有者可以在注册时提供此信息，并且可以随时直接在节点上更改或由 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 管理员进行集中更改。 集中更改节点策略时，它会在下一次节点脉动信号传输到管理中心时反映到节点。 在节点上直接更改节点策略时，更改会立即反映到管理中心，以便可以立即重新评估服务和模型部署。 缺省情况下，节点具有一些反映内存、体系结构和 CPU 数量的[内置属性](#node_builtins)。 它可以有选择地包含任意属性；例如，产品模型、连接的设备、软件配置或节点所有者认为相关的任何其他项。 节点策略约束可用于限制允许哪些服务在此节点上运行。每个节点仅具有一个策略，该策略包含分配给该节点的所有属性和约束。

## 服务策略
{: #service_policy}

注：服务策略是可选功能。

与节点一样，服务可以表示策略并具有一些[内置属性](#service_builtins)。 此策略适用于 Exchange 中的已发布服务；由服务开发人员创建。 服务策略属性可以声明节点策略作者可能发现相关的服务代码的特征。服务策略约束可用于限制此服务可在何处以及在哪些类型的设备上运行。 例如，服务开发者可以断言此服务需要特定硬件设置，例如，CPU/GPU 约束、内存约束、特定传感器、传动结构或其他外围设备。 通常，属性和约束在服务的生命周期内保持静态，因为它们描述了服务实现的各个方面。 在预期使用场景中，对属性或约束进行更改通常与需要新服务版本的代码更改一致。 部署策略用于捕获服务部署因业务需求而产生的更为动态的各个方面。

## 部署策略
{: #deployment_policy}

部署策略推动服务部署。 与其他策略类型一样，它包含一组属性和约束，但还包含其他内容。 例如，它明确标识要部署的服务，并且可以选择包含配置变量值、服务回滚版本和节点运行状况配置信息。 配置值的部署策略方法很强大，因为可以集中执行此操作，无需直接连接到边缘节点。

管理员可以创建部署策略，并且 {{site.data.keyword.ieam}} 使用该策略来查找与定义的约束匹配的所有设备，并使用策略中配置的服务变量将指定的服务部署到这些设备。 服务回滚版本指示 {{site.data.keyword.ieam}}，当更高版本的服务部署失败时，应部署哪些服务版本。 节点运行状况配置指示，在确定节点是否超出策略之前，{{site.data.keyword.ieam}} 应如何评估节点的运行状况（脉动信号和管理中心通信）。

由于部署策略捕获更动态、与业务类似的服务属性和约束，因此预期它们的更改会比服务策略更频繁。 它们的生命周期与所引用的服务无关，这使策略管理员能够声明特定服务版本或版本范围。 {{site.data.keyword.ieam}} 合并服务策略和部署策略，然后尝试查找其策略与该策略兼容的节点。

## 模型策略
{: #model_policy}

基于机器学习 (ML) 的服务需要特定模型类型才能正常运行，并且 {{site.data.keyword.ieam}} 客户需要能够将特定模型放置在已放置这些服务的相同或部分节点上。 模型策略的目的是进一步缩小部署给定服务的节点集，这可使部分节点能够通过[使用模型管理的 Hello World](../developing/model_management_system.md) 接收特定模型对象。

## 扩展策略用例
{: #extended_policy_use_case}

在 ATM 示例中，客户在经常使用的农村地区运行 walk-up ATM。 客户不希望农村 ATM 持续运行，在每次感知附近对象时都不希望打开 ATM。 因此，服务开发者将 ML 模型添加到 atm1 服务，如果它识别出有人靠近，就会打开 ATM。 为了将 ML 模型专门部署到这些农村 ATM，配置策略：

* 农村 walk-up ATM 上的节点策略：properties: `camera-type: still`, `atm-type: walk-up`, `location:  rural`
* （可选）第三方开发者为 atm1 设置的服务策略约束保持不变：constraints: `(Optional)`
* 客户为 atm1 服务设置的部署策略也保持不变：constraints: `camera-type == still
* 模型策略约束由第三方开发者在 MMS 对象中为 atm1 服务设置：

```
"destinationPolicy": {
  "constraints": [ "location == rural"  ],
  "services": [
       { "orgID": "$HZN_ORG_ID",
         "serviceName": "atm1",
         "arch": "$ARCH",  
         "version": "$VERSION"
       }
  ]
}
```
{: codeblock}

在 MMS 对象中，模型策略声明可访问该对象（在本例中为 atm1）的服务（或服务列表），并声明属性和约束，使 {{site.data.keyword.ieam}} 能够进一步缩小对象在农村地区 ATM 上的正确放置位置。 在 ATM 上运行的其他服务将无法访问该对象。

## 属性
{: #properties}

属性本质上是事实的声明，表示为“名称=值”对。 还输入了属性，这提供了构造功能强大的表达式的方法。 下表显示了 {{site.data.keyword.ieam}} 以及内置节点和服务策略属性支持的属性值类型。 节点所有者、服务开发者和部署策略管理员可以定义个人属性以满足其需求。 不需要在中央存储库中定义属性，将根据需要设置和引用（在约束表达式中）这些属性。

|接受的属性值类型|
|-----------------------------|
|版本 - 点分十进制表达式（支持 1、2 或 3 部件），例如，1.2 和 2.0.12 等|
|字符串 *|
|字符串列表（以逗号分隔的字符串）|
|整数|
|布尔值|
|浮点值|
{: caption="表 1. 接受的属性值类型"}

*必须使用引号将包含空格的字符串值括起来。

内置属性为公共属性提供明确定义的名称，以便约束都可以以相同方式进行引用。 例如，如果服务需要 `x` 个 CPU 才能正确或有效地执行，那么可以在其约束中使用 `openhorizon.cpu` 属性。 大多数属性无法设置，而是从底层系统中读取，并且会忽略用户设置的任何值。

### 节点内置属性
{: #node_builtins}

|名称|类型|描述|策略类型|
|----|----|-----------|-----------|
|openhorizon.cpu|整数|CPU 的数量|节点|
|openhorizon.memory|整数|内存量 (MB)|节点|
|openhorizon.arch|字符串|节点硬件体系结构（例如，amd64 和 armv6 等）|节点|
|openhorizon.hardwareId|字符串|通过 linux API 提供的节点硬件序列号；否则是加密安全随机数，在节点注册期间不会更改|节点|
|openhorizon.allowPrivileged|布尔值|允许容器使用特权功能，例如，以特权方式运行或将主机的网络连接到容器。|节点|
{: caption="表 2. 节点内置属性"}

### 服务内置属性
{: #service_builtins}

|名称|类型|描述|策略类型|
|----|----|-----------|-----------|
|openhorizon.service.url|字符串|服务的唯一名称|服务|
|openhorizon.service.org|字符串|定义了服务的多租户组织*|服务|
|openhorizon.service.version|版本|使用相同语义版本语法的服务版本（例如，1.0.0）|服务|
{: caption="表 3. 服务内置属性"}

*在约束中，如果指定了 service.url，但省略了 service.org，那么组织缺省为定义约束的节点或部署策略的值。

## 约束
{: #constraints}

在 {{site.data.keyword.ieam}} 中，节点、服务和部署策略可定义约束。 约束以简单文本形式表示为谓词，并引用属性及其值或其可能值范围。 约束还可以在属性和值的表达式之间包含 AND (&&) 和 OR (||) 之类的布尔运算符，以形成较长的子句。 例如，`openhorizon.arch == amd64 && OS == Mojave`。 最后，可以使用圆括号在单个表达式中创建求值优先顺序。

|属性值类型|受支持的运算符|
|-------------------|-------------------|
|整数|==, <, >, <=, >=, =, !=|
|字符串*|==, !=, =|
|字符串列表|in|
|布尔值|==, =|
|版本|==、=、in**|
{: caption="表 4. 约束"}

*对于字符串类型，带引号字符串（包含逗号分隔的字符串列表）提供可接受的值的列表；例如，如果 hello 是“beautiful”或“world”，那么 `hello == "beautiful, world"` 将为 true。

** 对于版本范围，使用 `in` 而不是 `==`。

## 策略用例较大程度地进行了扩展
{: #extended_policy_use_case_more}

为了说明策略双向性质的全部功能，请考虑本部分中的实际示例，并向节点添加一些约束。 在我们的示例中，如果一些位于农村的无电梯大楼中的 ATM 由于处于滨水位置而产生眩光，而其他无电梯大楼中的 ATM 使用的现有 atm1 服务无法处理这一情况。 这需要可以更好地处理这些少数 ATM 的眩光问题的第三个服务，以及按如下所示进行配置的策略：

* 海滨 walk-up ATM 上的节点策略：properties: `camera-type: still`, `atm-type: walk-up`; constraints: `feature == glare-correction`
* （可选）第三方开发者为 atm3 设置的服务策略：constraints: `(Optional)`
* 客户为 atm3 服务设置的部署策略：constraints: `camera-type == still`; properties: `feature: glare-correction`  

节点策略再次声明有关节点的事实，但是，在这种情况下，设置海滨 ATM 的技术人员指定了以下约束：要在此节点上部署的服务必须具有眩光校正功能。

atm3 的服务策略具有与其他项相同的约束，这需要在 ATM 上使用摄像头。

由于客户知道 atm3 服务会更好地处理眩光，因此他们在与 atm3 相关联的部署策略中设置此约束，这满足节点上设置的属性并会将此服务部署到海滨 ATM。

## 策略命令
{: #policy_commands}

|命令|描述|
|-------|-----------|
|`hzn policy list`|此边缘节点的策略。|
|`hzn policy new`|可以填写的空节点策略模板。|
|`hzn policy update --input-file=INPUT-FILE`|更新节点的策略。 如果输入策略不包含节点的内置属性，那么会自动添加。|
|`hzn policy remove [<flags>]`|移除节点的策略。|
|`hzn exchange node listpolicy [<flags>] <node>`|从 Horizon Exchange 显示节点策略。|
|`hzn exchange node addpolicy --json-file=JSON-FILE [<flags>] <node>`|在 Horizon Exchange 中添加或替换节点策略。|
|`hzn exchange node updatepolicy --json-file=JSON-FILE [<flags>] <node>`|在 Horizon Exchange 中更新此节点的策略的属性。|
|`hzn exchange node removepolicy [<flags>] <node>`|在 Horizon Exchange 中移除节点策略。|
|`hzn exchange service listpolicy [<flags>] <service>`|从 Horizon Exchange 显示服务策略。|
|`hzn exchange service newpolicy`|显示可以填写的空服务策略模板。|
|`hzn exchange service addpolicy --json-file=JSON-FILE [<flags>] <service>`|在 Horizon Exchange 中添加或替换服务策略。|
|`hzn exchange service removepolicy [<flags>] <service>`|在 Horizon Exchange 中移除服务策略。|
|`hzn exchange deployment listpolicy [<flags>] [<policy>]`|显示 Horizon Exchange 中的业务策略。|
|`hzn exchange deployment new`|显示可以填写的空部署策略模板。|
|`hzn exchange deployment addpolicy --json-file=JSON-FILE [<flags>] <policy>`|在 Horizon Exchange 中添加或替换部署策略。 对空部署策略模板使用 `hzn exchange deployment new`。|
|`hzn exchange deployment updatepolicy --json-file=JSON-FILE [<flags>] <policy>`|在 Horizon Exchange 中更新现有部署策略的一个属性。 受支持的属性是策略定义中的顶级属性，如命令 `hzn exchange deployment new` 所示。|
|`hzn exchange deployment removepolicy [<flags>] <policy>`|从 Horizon Exchange 中移除部署策略。|
|`hzn dev service new [<flags>]`|创建新的服务项目。 此命令将生成所有 IEC 服务元数据文件，包括服务策略模板。|
|`hzn deploycheck policy [<flags>]`|检查节点、服务和部署策略之间的策略兼容性。 您也可以使用 `hzn deploycheck all` 检查服务变量配置是否正确。|
{: caption="表 5. 策略开发工具"}

请参阅[探索 hzn 命令](../cli/exploring_hzn.md)，以获取有关使用 `hzn` 命令的更多信息。
