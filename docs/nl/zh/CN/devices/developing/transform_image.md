---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 将映像转换为边缘服务
{: #transform_image}

此示例引导您完成发布现有 Docker 映像作为边缘服务、创建关联的部署模式以及注册边缘节点来运行该部署模式的步骤。
{:shortdesc}

## 准备工作
{: #quickstart_ex_begin}

完成[准备创建边缘服务](service_containers.md)中的先决条件步骤。 因此，应该设置这些环境变量、安装这些命令，并且这些文件应该存在：

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## 过程
{: #quickstart_ex_procedure}

注：请参阅[此文档中使用的约定](../../getting_started/document_conventions.md)以获取有关命令语法的更多信息。

1. 创建项目目录。

  1. 在开发主机上，切换到现有 Docker 项目目录。 **如果您没有现有 Docker 项目，但是仍想要继续此示例**，请使用以下命令以创建可用于本过程的其余部分的简单 Dockerfile：

    ```bash
    cat << EndOfContent > Dockerfile
    FROM alpine:latest
    CMD while :; do echo "Hello, world."; sleep 3; done
    EndOfContent
    ```
    {: codeblock}

  2. 为项目创建边缘服务元数据：

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    此命令创建 **horizon/service.definition.json** 以描述您的服务，并创建 **horizon/pattern.json** 以描述部署模式。 您可以打开这些文件并浏览其内容。

2. 构建和测试服务。

  1. 构建 Docker 映像。映像名称必须匹配在 **horizon/service.definition.json** 中引用的名称。

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)
    export ARCH=$(hzn architecture)
    sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. 在 {{site.data.keyword.horizon}} 模拟代理程序环境中运行此服务容器映像：

    ```bash
    hzn dev service start -S
    ```
    {: codeblock}

  3. 验证服务容器是否正在运行：

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. 查看在启动时传递到容器的环境变量。 （以下是完整代理程序将传递到服务容器的相同环境变量。）

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. 查看服务容器日志：

    在 **{{site.data.keyword.linux_notm}}** 上：

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    在 **{{site.data.keyword.macOS_notm}}** 上：

    ```bash
    sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. 停止服务：

    ```bash
    hzn dev service stop
    ```
    {: codeblock}

3. 将服务发布到 {{site.data.keyword.edge_devices_notm}}。 既然您已确认服务代码在模拟的代理程序环境中按预期运行，即可将服务发布到 {{site.data.keyword.horizon_exchange}}，从而使其变为可部署到边缘节点。

  以下 **publish** 命令使用 **horizon/service.definition.json** 文件和密钥对来对服务进行签名并将服务发布到 {{site.data.keyword.horizon_exchange}}。 它还将映像推送到 Docker Hub。

  ```bash
  hzn exchange service publish -f horizon/service.definition.json
  hzn exchange service list
  ```
  {: codeblock}

4. 发布服务的部署模式。 边缘节点可使用此部署模式以使 {{site.data.keyword.edge_devices_notm}} 向其部署服务：

  ```bash
  hzn exchange pattern publish -f horizon/pattern.json
    hzn exchange pattern list
  ```
  {: codeblock}

5. 注册边缘节点以运行部署模式。

  1. 通过先前向来自 **IBM** 组织的公共部署模式注册边缘节点的同一方式，向在您自己的组织下发布的部署模式注册边缘节点：

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. 列出已作为结果启动的 Docker 容器边缘服务：

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. 查看 myservice 边缘服务输出：

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. 查看在 {{site.data.keyword.edge_devices_notm}} 控制台中创建的节点、服务和模式。 您可以使用以下命令显示控制台 URL：

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. 注销边缘节点并停止 **myservice** 服务：

  ```bash
  hzn unregister -f
  ```
  {: codeblock}

## 后续操作
{: #quickstart_ex_what_next}

* 尝试[使用 {{site.data.keyword.edge_devices_notm}} 开发边缘服务](developing.md)中的其他边缘服务示例。
