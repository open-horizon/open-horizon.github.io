---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 对节点错误进行故障诊断
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} 将事件日志的子集发布到在 {{site.data.keyword.gui}} 中可查看的 Exchange。这些错误链接到故障诊断指南。
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

当服务定义中引用的服务映像在映像存储库中不存在时，会发生此错误。要解决此错误，请执行以下操作：

1. 在没有 **-I** 标志的情况下重新发布服务。
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. 将服务映像直接推送到映像存储库。
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

当服务定义部署配置指定与根受保护的文件的绑定时，会发生此错误。要解决此错误，请执行以下操作：

1. 将容器绑定到根不受保护的文件。
2. 将文件许可权更改为允许用户对文件进行读取和写入。

## error_start_container
{: #esc}

如果 Docker 在启动服务容器时遇到错误，那么会发生此错误。错误消息可能包含指示容器启动失败原因的详细信息。错误解决步骤取决于错误。可能会发生以下错误：

1. 设备已在使用部署配置所指定的已发布端口。要解决错误，请执行以下操作： 

    - 将其他端口映射到服务容器端口。显示的端口号不必与服务端口号匹配。
    - 停止正在使用同一端口的程序。

2. 部署配置所指定的已发布端口不是有效的端口号。端口号必须是范围在 1 - 65535 内的数字。
3. 部署配置中的卷名不是有效的文件路径。卷路径必须由其绝对（而非相对）路径指定。 

## 其他信息

有关更多信息，请参阅：
  * [{{site.data.keyword.edge_devices_notm}} 故障诊断指南](../troubleshoot/troubleshooting.md)
