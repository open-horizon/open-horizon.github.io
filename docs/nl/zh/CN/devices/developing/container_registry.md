---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 使用专用容器注册表
{: #container_registry}

如果边缘服务映像包含的资产不适合包含在公用注册表中，那么您可以使用专用 Docker 容器注册表，例如，{{site.data.keyword.open_shift}} 映像注册表或 {{site.data.keyword.ibm_cloud}} 容器注册表，其中访问权受严格控制。
{:shortdesc}

如果您尚未这样做，请遵循[为设备开发边缘服务](developing.md)中的步骤，来创建和部署至少一个示例边缘服务，以确保您熟悉基本过程。

此页面描述可存储边缘服务映像的两个注册表：
* [使用 {{site.data.keyword.open_shift}} 映像注册表](#ocp_image_registry)
* [使用 {{site.data.keyword.cloud_notm}} 容器注册表](#ibm_cloud_container_registry)

这些示例还说明了如何将任何专用映像注册表与 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 配合使用。

## 使用 {{site.data.keyword.open_shift}} 映像注册表
{: #ocp_image_registry}

### 准备工作

* 如果尚未执行此操作，请安装 [cloudctl 命令 ![（在新选项卡中打开）](../../images/icons/launch-glyph.svg "（在新选项卡中打开）")](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.3.0/cloudctl/install_cli.html)
* 如果尚未执行此操作，请安装 [{{site.data.keyword.open_shift}}oc 命令 ![（在新选项卡中打开）](../../images/icons/launch-glyph.svg "（在新选项卡中打开）")](https://docs.openshift.com/container-platform/4.4/cli_reference/openshift_cli/getting-started-cli.html)
* 在 {{site.data.keyword.macOS_notm}} 上，您可以使用 [homebrew ![在新的选项卡中打开](../../images/icons/launch-glyph.svg "在新的选项卡中打开")](https://docs.brew.sh/Installation) 安装 {{site.data.keyword.open_shift}} **oc** 命令

    ```bash
    brew install openshift-cli
    ```
    {: codeblock}

### 过程

注：请参阅[此文档中使用的约定](../../getting_started/document_conventions.md)以获取有关命令语法的更多信息。

1. 确保您以集群管理员特权连接到 {{site.data.keyword.open_shift}} 集群。

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> -n kube-system --skip-ssl-validation
   ```
   {: codeblock}

2. 确定是否已创建 {{site.data.keyword.open_shift}} 映像注册表的缺省路由，以使其可从集群外部访问：

   ```bash
   oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'
   ```
   {: codeblock}

   如果命令响应指示找不到 **default-route**，请进行创建 (请参阅[公开注册表 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.4/registry/securing-exposing-registry.html) 以获取详细信息）：

   ```bash
   oc patch configs.imageregistry.operator.openshift.io/cluster --patch '{"spec":{"defaultRoute":true}}' --type=merge
   ```
   {: codeblock}

3. 检索您需要使用的存储库路由名称：

   ```bash
   export OCP_DOCKER_HOST=`oc get route default-route -n openshift-image-registry --template='{{ .spec.host }}'`
   ```
   {: codeblock}

4. 创建新项目以存储映像：

   ```bash
   export OCP_PROJECT=<your-new-project>
   oc new-project $OCP_PROJECT
   ```
   {: codeblock}

5. 使用您选择的名称创建服务帐户：

   ```bash
   export OCP_USER=<service-account-name>
   oc create serviceaccount $OCP_USER
   ```
   {: codeblock}

6. 将角色添加到当前项目的服务帐户：

   ```bash
   oc policy add-role-to-user edit system:serviceaccount:$OCP_PROJECT:$OCP_USER
   ```
   {: codeblock}

7. 将令牌分配到服务帐户：

   ```bash
   export OCP_TOKEN=`oc serviceaccounts get-token $OCP_USER`
   ```
   {: codeblock}

8. 获取 {{site.data.keyword.open_shift}} 证书并使 docker 信任此证书：

   ```bash
   echo | openssl s_client -connect $OCP_DOCKER_HOST:443 -showcerts | sed -n "/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/p" > ca.crt
   ```
   {: codeblock}

   在 {{site.data.keyword.linux_notm}} 上：

   ```bash
   mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
   systemctl restart docker.service
   ```
   {: codeblock}

   在 {{site.data.keyword.macOS_notm}} 上：

   ```bash
   mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
   cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
   ```
   {: codeblock}

   在 {{site.data.keyword.macOS_notm}} 上，通过单击桌面菜单栏右侧的鲸鱼图标并选择**重新启动**来重新启动 Docker。

9. 登录到 {{site.data.keyword.ocp}} Docker 主机：

   ```bash
   echo "$OCP_TOKEN" | docker login -u $OCP_USER --password-stdin $OCP_DOCKER_HOST
   ```
   {: codeblock}

10. 使用此路径格式构建映像，例如：

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t $OCP_DOCKER_HOST/$OCP_PROJECT/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

11. 准备发布边缘服务时，修改 **service.definition.json** 文件，以使其 **deployment** 部分引用映像注册表路径。 您可以使用以下方式创建服务和模式定义文件：

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i $OCP_DOCKER_HOST/$OCP_PROJECT/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** 应该是没有 arch 或版本的基本映像名称。 然后，您可以根据需要在创建的文件 **horizon/hzn.json** 中编辑变量。

   或者，如果已创建自己的服务定义文件，请确保 **deployment.services.&lt;service-name&gt;.image** 字段引用映像注册表路径。

12. 在准备好发布服务映像时，将映像推送到专用容器注册表，并将其发布到 {{site.data.keyword.horizon}} Exchange：

   ```bash
   hzn exchange service publish -r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "$OCP_DOCKER_HOST:$OCP_USER:$OCP_TOKEN"** 自变量为 {{site.data.keyword.horizon_open}} 边缘节点指定凭证，从而可拉取服务映像。

   该命令将完成以下任务：

   * 将 Docker 映像推送到 {{site.data.keyword.cloud_notm}} 容器注册表，并在此过程中获取映像的摘要。
   * 利用您的专用密钥对摘要和部署信息进行签名。
   * 将服务元数据（包括签名）放入 {{site.data.keyword.horizon}} Exchange 中。
   * 将公用密钥放入 {{site.data.keyword.horizon}} Exchange 中的服务定义下，从而使 {{site.data.keyword.horizon}} 边缘节点可在需要时自动检索定义以验证签名。
   * 将 OpenShift 用户和令牌放入 {{site.data.keyword.horizon}} Exchange 中的服务定义下，从而使 {{site.data.keyword.horizon}} 边缘节点可在需要时自动检索定义。
   
### 在 {{site.data.keyword.horizon}} 边缘节点上使用服务
{: #using_service}

要允许边缘节点从 {{site.data.keyword.ocp}} 映像注册表中拉取必需的服务映像，必须在每个边缘节点上配置 Docker 以信任 {{site.data.keyword.open_shift}} 证书。将 **ca.crt** 文件复制到每个边缘节点，然后：

在 {{site.data.keyword.linux_notm}} 上：

```bash
mkdir -p /etc/docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt /etc/docker/certs.d/$OCP_DOCKER_HOST
systemctl restart docker.service
```
{: codeblock}

在 {{site.data.keyword.macOS_notm}} 上：

```bash
mkdir -p ~/.docker/certs.d/$OCP_DOCKER_HOST
cp ca.crt ~/.docker/certs.d/$OCP_DOCKER_HOST
```
{: codeblock}

在 {{site.data.keyword.macOS_notm}} 上，通过单击桌面菜单栏右侧的鲸鱼图标并选择**重新启动**来重新启动 Docker。

现在，{{site.data.keyword.horizon}} 具有所有所需内容，可从 {{site.data.keyword.open_shift}} 映像注册表获取此边缘服务映像，并将其部署到您创建的部署模式或策略所指定的边缘节点。

## 使用 {{site.data.keyword.cloud_notm}} 容器注册表
{: #ibm_cloud_container_registry}

### 准备工作

* 安装 [{{site.data.keyword.cloud_notm}} CLI 工具 (ibmcloud) ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://cloud.ibm.com/docs/cli?topic=cloud-cli-install-ibmcloud-cli)。
* 确保您的 {{site.data.keyword.cloud_notm}} 帐户中具有**集群管理员**或**团队管理员**访问级别。

### 过程

1. 登录到 {{site.data.keyword.cloud_notm}} 并设置您的目标组织：

   ```bash
   ibmcloud login -a cloud.ibm.com -u <cloud-username> -p <cloud-password
   ibmcloud target -o <organization-id> -s <space-id>
   ```
   {: codeblock}

   如果您不知道组织标识和空间标识，可以登录到 [{{site.data.keyword.cloud_notm}} 控制台 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://cloud.ibm.com/) 进行查找或创建。

2. 创建云 API 密钥：

   ```bash
   ibmcloud iam api-key-create <key-name> -d "<key-description>"
   ```
   {: codeblock}

   将 API 密钥值（显示在以 **API Key** 开头的行中）保存在安全位置，并在以下环境变量中设置此密钥值：

   ```bash
   export CLOUD_API_KEY=<your-cloud-api-key>
   ```
   {: codeblock}

   注：此 API 密钥与您创建的要与 `hzn` 命令一起使用的 {{site.data.keyword.open_shift}} API 密钥不同。

3. 获取容器注册表插件并创建专用注册表名称空间。 （此注册表名称空间将是用于标识 Docker 映像的路径的一部分。）

   ```bash
   ibmcloud plugin install container-registry
   export REGISTRY_NAMESPACE=<your-registry-namespace>
   ibmcloud cr namespace-add $REGISTRY_NAMESPACE
   ```
   {: codeblock}

4. 登录到 Docker 注册表名称空间：

   ```bash
   ibmcloud cr login
   ```
   {: codeblock}

   有关使用 **ibmcloud cr** 的更多信息，请参阅 [ibmcloud cr CLI Web 文档 ![在新选项卡中打开](../../images/icons/launch-glyph.svg "在新选项卡中打开")](https://cloud.ibm.com/docs/services/Registry/)。 另外，您可以运行以下命令以查看帮助信息：

   ```bash
   ibmcloud cr --help
   ```
   {: codeblock}

   登录到 {{site.data.keyword.cloud_registry}} 中的专用名称空间后，无需使用 `docker login` 即可登录到注册表。 您能够在 **docker push** 和 **docker pull** 命令中使用类似以下路径的容器注册表路径：

   ```bash
   us.icr.io/$REGISTRY_NAMESPACE/<base-image-name>_<arch>:<version>
   ```
   {: codeblock}

5. 使用此路径格式构建映像，例如：

   ```bash
   export BASE_IMAGE_NAME=myservice
   docker build -t us.icr.io/$REGISTRY_NAMESPACE/${BASE_IMAGE_NAME}_amd64:1.2.3 -f ./Dockerfile.amd64 .
   ```
   {: codeblock}

6. 准备发布边缘服务时，修改 **service.definition.json** 文件，以使其 **deployment** 部分引用映像注册表路径。 您可以使用以下方式创建服务和模式定义文件：

   ```bash
   hzn dev service new -s $BASE_IMAGE_NAME -i us.icr.io/$REGISTRY_NAMESPACE/$BASE_IMAGE_NAME
   ```
   {: codeblock}

   **&lt;base-image-name&gt;** 应该是没有 arch 或版本的基本映像名称。 然后，您可以根据需要在创建的文件 **horizon/hzn.json** 中编辑变量。

   或者，如果已创建自己的服务定义文件，请确保 **deployment.services.&lt;service-name&gt;.image** 字段引用映像注册表路径。

7. 在准备好发布服务映像时，将映像推送到专用容器注册表，并将其发布到 {{site.data.keyword.horizon}} Exchange：

   ```bash
   hzn exchange service publish -r "us.icr.io:iamapikey:$CLOUD_API_KEY" -f horizon/service.definition.json
   ```
   {: codeblock}

   **-r "us.icr.io:iamapikey:$CLOUD_API_KEY"** 自变量为 {{site.data.keyword.horizon_open}} 边缘节点指定凭证，从而可拉取服务映像。

   该命令将完成以下任务：

   * 将 Docker 映像推送到 {{site.data.keyword.cloud_notm}} 容器注册表，并在此过程中获取映像的摘要。
   * 利用您的专用密钥对摘要和部署信息进行签名。
   * 将服务元数据（包括签名）放入 {{site.data.keyword.horizon}} Exchange 中。
   * 将公用密钥放入 {{site.data.keyword.horizon}} Exchange 中的服务定义下，从而使 {{site.data.keyword.horizon}} 边缘节点可在需要时自动检索定义以验证签名。
   * 将 {{site.data.keyword.cloud_notm}} API 密钥放入 {{site.data.keyword.horizon}} Exchange 中的服务定义下，从而使 {{site.data.keyword.horizon}} 边缘节点可在需要时自动检索定义。

8. 验证您的服务映像是否已推送到 {{site.data.keyword.cloud_notm}} 容器注册表：

   ```bash
   ibmcloud cr images
   ```
   {: codeblock}

9. 发布用于将服务部署到某些边缘节点的部署模式或策略。 例如：

   ```bash
   hzn exchange pattern publish -f horizon/pattern.json
   ```
   {: codeblock}

现在，{{site.data.keyword.horizon}} 具有所有所需内容，可从 {{site.data.keyword.cloud_notm}} 容器注册表获取此边缘服务映像，并将其部署到您创建的部署模式或策略所指定的边缘节点。
