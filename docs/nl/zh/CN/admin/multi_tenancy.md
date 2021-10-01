---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 多租户
{: #multit}

## {{site.data.keyword.edge_notm}} 中的租户
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 通过组织支持常规的多租户 IT 概念，其中，每个租户具有其自己的组织。 组织分隔资源；因此，每个组织中的用户无法创建或修改不同组织中的资源。 此外，除非将组织中的资源标记为公共，否则这些资源只能由该组织中的用户查看。

### 公共用例

两个广泛用例用于利用 {{site.data.keyword.ieam}} 中的多租户：

* 一个企业具有多个业务单位，其中每个业务单位是同一 {{site.data.keyword.ieam}} 管理中心中的独立组织。 考虑为什么每个业务单位都应该是独立组织并具有缺省情况下其他业务单位无法访问的其自己的一组 {{site.data.keyword.ieam}} 资源的法律、业务或技术原因。即使具有单独的组织，企业仍可以选择使用一组公共的组织管理员来管理所有组织。
* 企业托管 {{site.data.keyword.ieam}} 作为其客户的服务，其每个客户都在管理中心中有一个或多个组织。 在这种情况下，组织管理员对每个客户都是唯一的。

您选择的用例确定如何配置 {{site.data.keyword.ieam}} 和 Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html))。

### {{site.data.keyword.ieam}} 用户的类型
{: #user-types}

{{site.data.keyword.ieam}} 支持以下用户角色：

| **角色** | **访问权** |
|--------------|-----------------|
| **中心管理员** | 通过按需创建、修改和删除组织，以及在每个组织内创建组织管理员，来管理 {{site.data.keyword.ieam}} 组织的列表。 |
| **组织管理员** | 管理一个或多个 {{site.data.keyword.ieam}} 组织中的资源。 组织管理员可以创建、查看或修改组织内的任何资源（用户、节点、服务、策略或模式），即使他们不是资源的所有者。 |
| **常规用户** | 在组织内创建节点、服务、策略和模式以及修改或删除他们创建的资源。 查看组织内其他用户已创建的所有服务、策略和模式。 |
{: caption="表 1. {{site.data.keyword.ieam}} 用户角色" caption-side="top"}

请参阅[基于角色的访问控制](../user_management/rbac.md)以获取有关所有 {{site.data.keyword.ieam}} 角色的描述。

## IAM 和 {{site.data.keyword.ieam}} 之间的关系
{: #iam-to-ieam}

IAM (Identity and Access Manager) 服务管理所有基于 Cloud Pak 的产品（包括 {{site.data.keyword.ieam}}）的用户。 IAM 转而使用 LDAP 来存储这些用户。 每个 IAM 用户都可以是一个或多个 IAM 团队的成员。 因为每个 IAM 团队都与一个 IAM 帐户关联，所以一个 IAM 用户可以间接是一个或多个 IAM 帐户的成员。 请参阅 [IAM 多租户](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html)以获取详细信息。

{{site.data.keyword.ieam}} Exchange 为其他 {{site.data.keyword.ieam}} 组件提供认证和授权服务。 Exchange 将用户认证委托给 IAM，这表示 IAM 用户凭证将传递到 Exchange 并且它依赖于 IAM 来确定这些凭证是否有效。每个用户角色（中心管理员、组织管理员或常规用户）在 Exchange 中进行定义，这决定了允许用户在 {{site.data.keyword.ieam}} 中执行的操作。

{{site.data.keyword.ieam}} Exchange 中的每个组织都与一个 IAM 帐户关联。 因此，IAM 帐户中的 IAM 用户自动是相应 {{site.data.keyword.ieam}} 组织的成员。此规则的一个例外是 {{site.data.keyword.ieam}} 中心管理员角色被视为在任何特定组织之外；因此，中心管理员 IAM 用户在哪个 IAM 帐户中都无所谓。

为总结 IAM 和 {{site.data.keyword.ieam}} 之间的映射：

| **IAM** | **关系** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| IAM 帐户 | 映射至 | {{site.data.keyword.ieam}} 组织 |
| IAM 用户 | 映射至 | {{site.data.keyword.ieam}} 用户 |
| 不存在角色的 IAM 对应项 | 无 | {{site.data.keyword.ieam}} 角色 |
{: caption="表 2. IAM - {{site.data.keyword.ieam}} 映射" caption-side="top"}

用于登录 {{site.data.keyword.ieam}} 控制台的凭证为 IAM 用户和密码。 用于 {{site.data.keyword.ieam}} CLI (`hzn`) 的凭证为 IAM API 密钥。

## 初始组织
{: #initial-org}

缺省情况下，在 {{site.data.keyword.ieam}} 安装期间使用提供的名称创建组织。 如果您不需要 {{site.data.keyword.ieam}} 的多租户功能，那么此初始组织足够您使用 {{site.data.keyword.ieam}}，您可以跳过此页面的剩余部分。

## 创建中心管理员用户
{: #create-hub-admin}

使用 {{site.data.keyword.ieam}} 多租户的第一步是创建一个或多个可创建和管理组织的中心管理员。 在执行此操作前，您必须创建或选择将向其分配中心管理员角色的 IAM 帐户和用户。

1. 使用 `cloudctl` 以集群管理员身份登录 {{site.data.keyword.ieam}} 管理中心。 （如果尚未安装 `cloudctl`，请参阅[安装 cloudctl、kubectl 和 oc](../cli/cloudctl_oc_cli.md) 以获取指示信息。）

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. 如果尚未将 LDAP 实例连接到 IAM，请遵循[连接到 LDAP 目录](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html)来执行此操作。

3. 中心管理员用户必须在 IAM 帐户中。 （无所谓在哪个帐户中。） 如果还没有您希望中心管理员用户位于的 IAM 帐户，请创建一个：

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. 创建或选择专用于 {{site.data.keyword.ieam}} 中心管理员角色的 LDAP 用户。请不要使用同一个用户作为 {{site.data.keyword.ieam}} 中心管理员和 {{site.data.keyword.ieam}} 组织管理员（或常规 {{site.data.keyword.ieam}} 用户）。

5. 将用户导入到 IAM：

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>
   cloudctl iam user-import -u $HUB_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. 将中心管理员角色分配给 IAM 用户：

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW
   export HZN_EXCHANGE_URL=<the URL of your exchange>
   hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. 验证用户是否具有中心管理员用户角色。 在以下命令的输出中，您应该会看到 `"hubAdmin": true`。

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### 将中心管理员用户与 {{site.data.keyword.ieam}} CLI 配合使用
{: #verify-hub-admin}

针对中心管理员用户创建 API 密钥并验证其是否具有中心管理员功能：

1. 使用 `cloudctl` 以中心管理员身份登录 {{site.data.keyword.ieam}} 管理中心：

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. 针对中心管理员用户创建 API 密钥：

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   在以 **API Key** 开头的命令输出行中找到 API 密钥值。 将密钥值保存在安全位置以供将来使用，因为以后无法从系统进行查询。 并且，针对后续命令在此变量中对其进行设置：

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 显示管理中心中的所有组织。 您应该看到在安装期间创建的初始组织，以及 **root** 和 **IBM** 组织：

   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   hzn exchange org list -o root
   ```
   {: codeblock}

4. 使用中心管理员 IAM 用户名和密码登录 [{{site.data.keyword.ieam}} 管理控制台](../console/accessing_ui.md)。 显示组织管理控制台，因为您的登录凭证具有中心管理员角色。使用此控制台来查看、管理和添加组织。 您可以在以下部分中使用 CLI 添加组织。

## 使用 CLI 创建组织
{: #create-org}

作为使用 {{site.data.keyword.ieam}} 组织管理控制台的替代方法，可使用 CLI 创建组织。创建组织的先决条件是创建或选择将与组织关联的 IAM 帐户。 另一个先决条件是创建或选择将被分配组织管理员角色的 IAM 用户。

执行以下步骤：

1. 如果您尚未完成此操作，请执行先前部分中的步骤来创建中心管理员用户。 请确保在以下变量中设置中心管理员 API 密钥：

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. 使用 `cloudctl` 以集群管理员身份登录 {{site.data.keyword.ieam}} 管理中心并创建将与新的 {{site.data.keyword.ieam}} 组织关联的 IAM 帐户。 （如果尚未安装 `cloudctl`，请参阅[安装 cloudctl、kubectl 和 oc](../cli/cloudctl_oc_cli.md)。）

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   NEW_ORG_ID=<new organization name>
   IAM_ACCOUNT_NAME="$NEW_ORG_ID"
   cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"
   IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. 创建或选择将分配到组织管理员角色的 LDAP 用户并将其导入到 IAM。 您不能使用中心管理员用户作为组织管理员用户，但是您可以在多个 IAM 帐户中使用同一个组织管理员用户。因此，允许其管理多个 {{site.data.keyword.ieam}} 组织。

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>
   cloudctl iam user-import -u $ORG_ADMIN_USER
   cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER
   IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. 设置这些环境变量，创建 {{site.data.keyword.ieam}} 组织，并验证它是否存在：
   ```bash
   export HZN_ORG_ID=root
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY
   export HZN_EXCHANGE_URL=<URL of your exchange>
   hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID
   hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID
   hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. 将组织管理员用户分配给您先前选择的 IAM 用户，并验证是否在 {{site.data.keyword.ieam}} Exchange 创建了具有组织管理员角色的用户：

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"
   hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   在用户列示中，您应该看到：`"admin": true`

**注**：如果您创建多个组织并且希望同一个组织管理员管理所有组织，请在每次通过此部分时对 `ORG_ADMIN_USER` 使用相同值。

组织管理员现在可以使用 [{{site.data.keyword.ieam}} 管理控制台](../console/accessing_ui.md)来管理此组织中的 {{site.data.keyword.ieam}} 资源。

### 允许组织管理员使用 CLI

为使组织管理员通过 CLI 使用 `hzn exchange` 命令来管理 {{site.data.keyword.ieam}} 资源，他们必须：

1. 使用 `cloudctl` 登录 {{site.data.keyword.ieam}} 管理中心并创建 API 密钥：

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   在以 **API Key** 开头的命令输出行中找到 API 密钥值。 将密钥值保存在安全位置以供将来使用，因为以后无法从系统进行查询。 并且，针对后续命令在此变量中对其进行设置：

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **提示：**如果未来将此用户添加到其他 IAM 帐户，那么您无需为每个帐户创建 API 密钥。 同一 API 密钥将在此用户作为成员的所有 IAM 帐户中工作，因此在所有 {{site.data.keyword.ieam}} 组织中此用户都是成员。

2. 验证 API 密钥是否与 `hzn exchange` 命令一起工作：

   ```bash
   export HZN_ORG_ID=<organization id>
   export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY
   hzn exchange user list
   ```
   {: codeblock}


新组织准备就绪可供使用。 要在此组织中设置最大数量的边缘节点，或定制缺省边缘节点脉动信号设置，请参阅[组织配置](#org-config)。

## 组织中的非管理员用户
{: #org-users}

通过将 IAM 用户（作为 `MEMBER`）导入和加载到相应的 IAM 帐户，可将新用户添加到组织。 您不需要明确地将用户添加到 {{site.data.keyword.ieam}} Exchange，因为此操作会在必要时自动发生。

然后，用户可以使用 [{{site.data.keyword.ieam}} 管理控制台](../console/accessing_ui.md)。 为使用户使用 `hzn exchange` CLI，他们必须：

1. 使用 `cloudctl` 登录 {{site.data.keyword.ieam}} 管理中心并创建 API 密钥：

   ```bash
   IAM_USER=<iam user>
   cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   在以 **API Key** 开头的命令输出行中找到 API 密钥值。 将密钥值保存在安全位置以供将来使用，因为以后无法从系统进行查询。 并且，针对后续命令在此变量中对其进行设置：

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. 设置这些环境变量并验证用户：

```bash
export HZN_ORG_ID=<organization-id>
export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY
hzn exchange user list
```
{: codeblock}

## IBM 组织
{: #ibm-org}

IBM 组织是提供预定义的服务和模式的唯一组织，这些旨在成为任何组织中的任何用户可使用的技术示例。 IBM 组织在 {{site.data.keyword.ieam}} 管理中心安装时自动创建。

**注**：虽然 IBM 组织中的资源为公共，但是 IBM 组织并非旨在保存 {{site.data.keyword.ieam}} 管理中心中的所有公共内容。

## 组织配置
{: #org-config}

每个 {{site.data.keyword.ieam}} 组织都具有以下设置。 这些设置的缺省值通常是充足的。 如果您选择定制任何这些设置，请运行命令 `hzn exchange org update -h` 以查看可使用的命令标志。

| **设置** | **描述** |
|--------------|-----------------|
| `description` | 组织的描述。 |
| `label` | 组织的名称。 此值用于在 {{site.data.keyword.ieam}} 管理控制台中显示组织名称。 |
| `heartbeatIntervals` | 组织中的边缘节点代理程序轮询管理中心以获取指令的频率。 请参阅以下部分以获取详细信息。 |
| `limits` | 此组织的限制。 目前，唯一的限制是 `maxNodes`，它是此组织中允许的边缘节点的最大数量。单个 {{site.data.keyword.ieam}} 管理中心可支持的边缘节点总数存在实际限制。 此设置允许中心管理员用户限制每个组织可具有的节点数，以阻止某个组织使用所有容量。 值 `0` 表示无限制。 |
{: caption="表 3. 组织设置" caption-side="top"}

### 代理程序脉动信号轮询时间间隔
{: #agent-hb}

在每个边缘节点上安装的 {{site.data.keyword.ieam}} 代理程序定期向管理中心发出脉动信号以使管理中心知道它仍在运行并且已连接，并接收指令。 您只需更改极大型环境的这些设置。

脉动信号时间间隔是向管理中心发出脉动信号之间代理程序等待的时间量。 时间间隔随时间自动调整以优化响应能力并减少管理中心上的负载。 时间间隔调整受三个设置控制：

| **设置** | **描述**|
|-------------|----------------|
| `minInterval` | 向管理中心发出脉动信号之间代理程序应等待的最短时间量（以秒为单位）。 注册代理程序时，其以此时间间隔启动轮询。 时间间隔将永远不低于此值。 值 `0` 表示使用缺省值。 |
| `maxInterval` | 向管理中心发出脉动信号之间代理程序应等待的最长时间量（以秒为单位）。 值 `0` 表示使用缺省值。 |
| `intervalAdjustment` | 在代理程序检测到其可以提高时间间隔时向当前脉动信号时间间隔添加的秒数。 在成功向管理中心发出脉动信号但是一段时间内未收到任何指令后，脉动信号时间间隔将逐渐增加直至达到此最大脉动信号时间间隔。 类似，在收到指令后，脉动信号时间间隔降低以确保快速处理后续指令。 值 `0` 表示使用缺省值。 |
{: caption="表 4. heartbeatIntervals 设置" caption-side="top"}

组织中的脉动信号轮询时间间隔设置应用于未显式配置脉动信号时间间隔的节点。 要检查节点是否已显式设置脉动信号时间间隔设置，请使用 `hzn exchange node list <node id>`。

有关在大型环境中配置设置的更多信息，请参阅[缩放配置](../hub/configuration.md#scale)。
