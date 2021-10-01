# IBM&reg; Edge Application Manager

## 简介

IBM Edge Application Manager 为在边缘设备（IoT 部署中的典型设备）上部署的应用程序提供端到端**应用程序管理平台**。 该平台完全自动化，应用程序开发者不需要执行手动操作，即可安全地在数千个现场部署的边缘设备上部署边缘工作负载的修订。 应用程序开发者可以专注于完成以任何编程语言编写应用程序代码作为可独立部署的 Docker 容器的任务。 该平台负责部署完整的业务解决方案，安全且无缝地在所有设备上进行多级别 Docker 容器编排。

https://www.ibm.com/cloud/edge-application-manager

## 先决条件

请参阅以下内容，以了解[先决条件](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#prereq)。

## Red Hat OpenShift SecurityContextConstraints 需求

缺省 `SecurityContextConstraints` 名称：已针对此 Chart 验证 [`restricted`](https://ibm.biz/cpkspec-scc)。 此发行版仅限于部署到 `kube-system` 名称空间，并为主要 Chart 创建服务帐户，为缺省本地数据库子 Chart 创建其他服务帐户。

## Chart 详细信息

该 Helm Chart 将 IBM Edge Application Manager 认证的容器安装到 OpenShift 环境中并进行配置。 将安装以下组件：

* IBM Edge Application Manager - Exchange
* IBM Edge Application Manager - AgBot
* IBM Edge Application Manager - Cloud Sync Service（模型管理系统的一部分）
* IBM Edge Application Manager - 用户界面（管理控制台）

## 需要的资源

请参阅以下内容，以了解[大小设置](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/cluster_sizing.html)。

## 存储和数据库需求

需要三个数据库实例来存储 IBM Edge Application Manager 组件数据。

缺省情况下，Chart 将使用定义的缺省（或用户配置的）kubernetes 动态存储类，安装具有以下卷大小设置的三个持久数据库。 如果使用不允许卷扩展的存储类，请确保允许相应扩展。

**注：**这些缺省数据库并非用于生产用途。 要利用您自己管理的数据库，请参阅以下需求，并执行**配置远程数据库**部分中的步骤。

* PostgreSQL：存储 Exchange 和 AgBot 数据
  * 需要两个单独的实例，每个实例至少具有 20GB 存储空间
  * 实例应该支持至少 100 个连接
  * 在生产环境中使用时，这些实例应具有高可用性
* MongoDB：存储 Cloud Sync Service 数据
  * 需要具有至少 50GB 存储空间的 1 个实例。 **注：**所需大小高度取决于您所存储和使用的边缘服务模型及文件的大小和数量。
  * 在生产环境中使用时，这些实例应具有高可用性

**注：**您负责这些缺省数据库以及您自己的受管数据库的备份节奏/过程。
请参阅**备份和复原**部分以了解缺省数据库过程。

## 监视资源

安装 IBM Edge Application Manager 时，它会自动设置对 Kubernetes 中运行的产品资源的一些基本监视。 可以在以下位置的管理控制台的 Grafana 仪表板中查看监视数据：

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-ibm-edge-overview/ibm-edge-overview`

## 配置

#### 配置远程数据库

1. 要使用您自己的受管数据库，请在 `values.yaml` 中搜索以下 helm 配置参数，并将其值更改为 `false`：

```yaml
localDBs:
  enabled: true
```

2. 创建以此模板内容开头的文件（例如，`dbinfo.yaml`）：

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ibm-edge-remote-dbs
  labels:
    release: ibm-edge
type: Opaque
stringData:
  # agbot postgresql connection settings
  agbot-db-host: "Single hostname of the remote database"
  agbot-db-port: "Single port the database runs on"
  agbot-db-name: "The name of the database to utilize on the postgresql instance"
  agbot-db-user: "Username used to connect"
  agbot-db-pass: "Password used to connect"
  agbot-db-ssl: "SSL Options: <disable|require|verify-full>"

  # exchange postgresql connection settings
  exchange-db-host: "Single hostname of the remote database"
  exchange-db-port: "Single port the database runs on"
  exchange-db-name: "The name of the database to utilize on the postgresql instance"
  exchange-db-user: "Username used to connect"
  exchange-db-pass: "Password used to connect"
  exchange-db-ssl: "SSL Options: <disable|require|verify-full>"

  # css mongodb connection settings
  css-db-host: "Comma separate <hostname>:<port>,<hostname2>:<port2>"
  css-db-name: "The name of the database to utilize on the mongodb instance"
  css-db-user: "Username used to connect"
  css-db-pass: "Password used to connect"
  css-db-auth: "The name of the database used to store user credentials"
  css-db-ssl: "SSL Options: <true|false>"

  trusted-certs: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```

3. 编辑 `dbinfo.yaml`，为供应的数据库提供访问信息。 填写双引号（保留值的引号）之间的所有信息。 添加可信证书时，请确保每行缩进 4 个空格，以确保正确读取 yaml 文件。 如果两个或多个数据库使用相同的 cert ，那么**不**需要在 `dbinfo.yaml` 中重复 cert。 保存文件，然后运行：

```bash
oc --namespace kube-system apply -f dbinfo.yaml
```


#### 高级配置

要更改任何缺省 helm 配置参数，请使用下面的 `grep` 命令查看参数及其描述，然后在 `values.yaml` 中查看/编辑相应值：

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use any editor
```

## 安装 Chart

**注：**

* 这是仅 CLI 安装，不支持从 GUI 安装

* 确保[安装 IBM Edge Application Manager 基础结构 - 安装过程](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html#process)中的步骤已完成。
* 对于每个集群，只能安装一个 IBM Edge Application Manager 实例，并且只能安装到 `kubbe-system` 名称空间。
* 不支持从 IBM Edge Application Manager 4.0 升级

运行提供的安装脚本以安装 IBM Edge Application Manager。 脚本执行的主要步骤是：安装 Helm Chart，在安装后配置环境（创建 agbot、org 以及模式/策略服务）。

```bash
ibm_cloud_pak/pak_extensions/support/ieam-install.sh
```

**注：**根据网速，下载映像并部署所有 Chart 资源需要几分钟时间。

### 验证 Chart

* 上述脚本将验证 pod 是否正在运行以及 agbot 和 exchange 是否正在响应。 在安装结束时查找“RUNNING”和“PASSED”消息。
* 如果是“FAILED”，那么输出将要求您查看特定日志以获取更多信息
* 如果是“PASSED”，那么输出将显示运行的测试的详细信息以及管理 UI 的 URL
  * 使用日志末尾提供的 URL 浏览到 IBM Edge Application Manager UI 控制台。
    * `https://<MANAGEMENT_URL:PORT>/edge`

## 安装后

遵循[安装后配置](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/post_install.html)中的步骤。

## 卸载 Chart

遵循[卸载管理中心](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/uninstall.html)的步骤。

## 基于角色的访问

* 安装和管理此产品需要 `kubbe-system` 名称空间中的集群管理员权限。
* 服务帐户、角色和角色绑定将基于发布名称为此 Chart 和子 Chart 创建。
* Exchange 认证和角色：
  * 所有 Exchange 管理员和用户的认证由 IAM 通过使用 `cloudctl` 命令生成的 API 密钥提供。
  * Exchange 管理员应该在 Exchange 中被授予 `admin` 特权。 借助该特权，他们可以管理其 Exchange 组织内的所有用户、节点、服务、模式和策略
  * Exchange 非管理员用户只能管理其创建的用户、节点、服务、模式和策略

## 安全性

* 对于通过入口进入/离开 OpenShift 集群的所有数据，使用了 TLS。 在此发行版中，OpenShift 集群**内部**未使用 TLS 来进行节点间通信。 如果需要，请配置 Red Hat OpenShift 服务网以在微服务之间进行通信。 请参阅[了解 Red Hat OpenShift 服务网](https://docs.openshift.com/container-platform/4.4/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm)。
* 此 Chart 未提供静态数据的加密。  管理员可决定是否要配置静态存储加密。

## 备份和恢复

遵循[备份和恢复](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/admin/backup_recovery.html)中的步骤。

## 限制

* 安装限制：此产品只能安装一次，并且只能安装到 `kubbe-system` 名称空间中

## 文档

* 请参阅[安装](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/hub.html) Knowledge Center 文档以获取更多信息。

## Copyright

© Copyright IBM Corporation 2020. All Rights Reserved.
