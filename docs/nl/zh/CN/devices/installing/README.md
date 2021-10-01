# IBM Edge Computing Manager

## 简介

IBM Edge Computing Manager for Devices 为在边缘设备（IoT 环境中的典型设备）上部署的应用程序提供端到端**应用程序管理平台**。 该平台完全自动化，应用程序开发者不需要执行手动操作，即可安全地在数千个现场部署的边缘设备上部署边缘工作负载的修订。 应用程序开发者可以专注于完成以任何编程语言编写应用程序代码作为可独立部署的 Docker 容器的任务。 该平台负责部署完整的业务解决方案，安全且无缝地在所有设备上进行多级别 Docker 容器编排。

## 先决条件

* Red Hat OpenShift Container Platform 4.2
* IBM Multicloud Management Core 1.2
* 如果托管您自己的数据库，请供应两个 PostgreSQL 实例和一个 MongoDB 实例，存储 IBM Edge Computing Manager for Devices 组件的数据。 请参阅下面的**存储**部分以获取详细信息。
* 用于从其中驱动安装的 Ubuntu Linux 或 macOS 主机。 它必须已安装以下软件：
  * [Kubernetes CLI (kubectl)](https://kubernetes.io/docs/tasks/tools/install-kubectl/) V1.14.0 或更高版本
  * [IBM Cloud Pak CLI (cloudctl)](https://www.ibm.com/support/knowledgecenter/SSFC4F_1.2.0/cloudctl/icp_cli.html)
  * [OpenShift CLI (oc)](https://docs.openshift.com/container-platform/4.2/cli_reference/openshift_cli/getting-started-cli.html)
  * [Helm CLI](https://helm.sh/docs/using_helm/#installing-the-helm-client) V2.9.1 或更高版本
  * 其他软件包：
    * jq
    * git
    * docker (V18.06.01 或更高版本)
    * make

## Red Hat OpenShift SecurityContextConstraints 需求

缺省 `SecurityContextConstraints` 名称：已针对此 Chart 验证 [`restricted`](https://ibm.biz/cpkspec-scc)。 此发行版仅限于部署到 `kubbe-system` 名称空间，并使用 `default` 服务帐户，还为可选本地数据库子 Chart 创建其自己的服务帐户。

## Chart 详细信息

该 Helm Chart 将 IBM Edge Computing Manager for Devices 认证的容器安装并配置到 OpenShift 环境中。 将安装以下组件：

* IBM Edge Computing Manager for Devices - Exchange
* IBM Edge Computing Manager for Devices - AgBots
* IBM Edge Computing Manager for Devices - Cloud Sync Service（模型管理系统的一部分）
* IBM Edge Computing Manager for Devices - 用户界面（管理控制台）

## 需要的资源

有关所需资源的信息，请参阅[安装 - 大小调整](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)。

## 存储和数据库需求

需要三个数据库实例来存储 IBM Edge Computing Manager for Devices 组件数据。

缺省情况下，Chart 将使用定义的缺省（或用户配置的）kubernetes 动态存储类，安装具有以下卷大小设置的三个持久数据库。

**注：**这些缺省数据库并非用于生产用途。 要利用您自己管理的数据库，请参阅以下需求，并执行**配置远程数据库**部分中的步骤。

* PostgreSQL：存储 Exchange 和 AgBot 数据
  * 需要两个单独的实例，每个实例至少具有 10GB 存储空间
  * 实例应该支持至少 100 个连接
  * 在生产环境中使用时，这些实例应具有高可用性
* MongoDB：存储 Cloud Sync Service 数据
  * 需要具有至少 50GB 存储空间的 1 个实例。 **注：**所需大小高度取决于您所存储和使用的边缘服务模型及文件的大小和数量。
  * 在生产环境中使用时，这些实例应具有高可用性

**注：**如果使用自己管理的数据库，那么您负责备份/复原过程。
请参阅**备份和复原**部分以了解缺省数据库过程。

## 监视资源

安装 IBM Edge Computing Manager for Devices 时，它会自动设置对产品以及在其上运行的 pod 的监视。 可以在以下位置的管理控制台的 Grafana 仪表板中查看监视数据：

* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-overview/edge-computing-overview`
* `https://<MANAGEMENT_URL:PORT>/grafana/d/kube-system-edge-computing-pod-overview/edge-computing-pod-overview`

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
  name: edge-computing-remote-dbs
  labels:
    release: edge-computing
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

要更改任何缺省 helm 配置参数，可以使用下面的 `grep` 命令查看参数及其描述，然后在 `values.yaml` 中查看/编辑相应值：

```bash
grep -v -E '(^ *#|__metadata)' ibm_cloud_pak/values-metadata.yaml
vi values.yaml   # or use your preferred editor
```

## 安装 Chart

**注：**

* 这是仅 CLI 安装，不支持从 GUI 安装

* 您应该已完成[安装 IBM Edge Computing Manager for Devices 基础结构 - 安装过程](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#process)中的步骤
* 对于每个集群，只能安装一个 IBM Edge Computing Manager for Devices 实例，并且只能安装到 `kubbe-system` 名称空间。
* 不支持从 IBM Edge Computing Manager for Devices 3.2 升级

运行提供的安装脚本以安装 IBM Edge Computing Manager for Devices。 脚本执行的主要步骤是：安装 Helm Chart，在安装后配置环境（创建 agbot、org 以及模式/策略服务）。

```bash
ibm_cloud_pak/pak_extensions/full-install/install-edge-computing.sh
```

**注：**根据您的网速，下载映像、等待 pod 转换为 RUNNING 状态以及所有服务都将变为活动状态，这些过程需要几分钟时间。

### 验证 Chart

* 上述脚本将验证 pod 是否正在运行以及 agbot 和 exchange 是否正在响应。 在安装结束时查找“RUNNING”和“PASSED”消息。
* 如果是“FAILED”，那么输出将要求您查看特定日志以获取更多信息
* 如果是“PASSED"，那么输出将显示运行的测试的详细信息以及要验证的其他两个项
  * 使用日志末尾提供的 URL 浏览到 IBM Edge Computing Manager UI 控制台。
    * `https://<MANAGEMENT_URL:PORT>/edge`

## 安装后

遵循[安装后配置](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#postconfig)中的步骤。

## 卸载 Chart

**注：**如果在配置了本地数据库的情况下要进行卸载，**所有数据将被删除**。 如果您希望在卸载之前保留此数据，请参阅下面的**备份过程**部分。

返回到此 README.md 的位置，并运行提供的卸载脚本，以自动完成卸载任务。 该脚本涵盖的主要步骤包括：卸载 Helm Chart 和移除密钥。 首先，以集群管理员身份，使用 `cloudctl` 登录集群。 然后：

```bash
ibm_cloud_pak/pak_extensions/uninstall/uninstall-edge-computing.sh <cluster-name>
```

**注：**如果供应了远程数据库，那么将删除认证密钥，但不会运行任何任务来从那些远程数据库中停用/删除数据。 如果要删除该数据，请立即执行。

## 基于角色的访问

* 安装和管理此产品需要 `kubbe-system` 名称空间中的集群管理员权限。
* Exchange 认证和角色：
  * 所有 Exchange 管理员和用户的认证由 IAM 通过使用 `cloudctl` 命令生成的 API 密钥提供。
  * Exchange 管理员应该在 Exchange 中被授予 `admin` 特权。 借助该特权，他们可以管理其 Exchange 组织内的所有用户、节点、服务、模式和策略
  * Exchange 非管理员用户只能管理其创建的用户、节点、服务、模式和策略

## 安全性

* 对于通过入口进入/离开 OpenShift 集群的所有数据，使用了 TLS。 在此发行版中，OpenShift 集群**内部**未使用 TLS 来进行节点间通信。 如果需要，您可以配置 Red Hat OpenShift 服务网以在微服务之间进行通信。 请参阅[了解 Red Hat OpenShift 服务网](https://docs.openshift.com/container-platform/4.2/service_mesh/service_mesh_arch/understanding-ossm.html#understanding-ossm)。
* 此 Chart 未提供静态数据的加密。  管理员可决定是否要配置存储加密。

## 备份和恢复

### 备份过程

在连接到集群中具有足够空间来存储这些备份的位置后，运行以下命令。


1. 创建用于存储以下备份的目录，根据需要进行调整

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/$(date +%Y%m%d_%H%M%S)
mkdir -p $BACKUP_DIR
```

2. 运行以下命令以备份认证/密钥

```bash
oc -n kube-system get secret edge-computing -o yaml > $BACKUP_DIR/edge-computing-secret.yaml && \
oc -n kube-system get secret edge-computing-agbotdb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-agbotdb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-exchangedb-postgresql-auth-secret -o yaml > $BACKUP_DIR/edge-computing-exchangedb-postgresql-auth-secret-backup.yaml && \
oc -n kube-system get secret edge-computing-css-db-ibm-mongodb-auth-secret -o yaml > $BACKUP_DIR/edge-computing-css-db-ibm-mongodb-auth-secret-backup.yaml
```

3. 运行以下命令以备份数据库内容

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-exchangedb-proxy-svc -F t postgres > /stolon-data/exchange-backup.tar" && \
oc -n kube-system cp edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar $BACKUP_DIR/exchange-backup.tar
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc -n kube-system get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_dump -U admin -h edge-computing-agbotdb-proxy-svc -F t postgres > /stolon-data/agbot-backup.tar" && \
oc -n kube-system cp edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar $BACKUP_DIR/agbot-backup.tar
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "mkdir -p /data/db/backup; mongodump -u admin -p $(oc -n kube-system get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) --out /data/db/css-backup" && \
oc -n kube-system cp edge-computing-cssdb-server-0:/data/db/css-backup $BACKUP_DIR/css-backup
```

4. 验证备份后，从无状态的容器中移除备份

```bash
oc -n kube-system exec edge-computing-exchangedb-keeper-0 -- bash -c "rm -f /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-agbotdb-keeper-0 -- bash -c "rm -f /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system exec edge-computing-cssdb-server-0 -- bash -c "rm -rf /data/db/css-backup"
```

### 复原过程

**注：**如果复原到新的集群，那么该“集群名称”必须与集群备份所源自集群的名称匹配。

1. 从集群中删除任何预先存在的密钥
```bash
oc -n kube-system delete secret edge-computing edge-computing-agbotdb-postgresql-auth-secret edge-computing-exchangedb-postgresql-auth-secret edge-computing-css-db-ibm-mongodb-auth-secret;
```

2. 将这些值导出到本地机器

```bash
export BACKUP_DIR=/tmp/edge-computing-backup/<Insert desired backup datestamp YYYYMMDD_HHMMSS>
```

3. 运行以下命令以复原认证/密钥

```bash
oc apply -f $BACKUP_DIR
```

4. 在继续操作之前重新安装 IBM Edge Computing Manager，遵循**安装 Chart** 部分中的指示信息

5. 运行以下命令以将备份复制到容器中并复原它们

```bash
oc -n kube-system cp $BACKUP_DIR/exchange-backup.tar edge-computing-exchangedb-keeper-0:/stolon-data/exchange-backup.tar && \
oc exec -n kube-system edge-computing-exchangedb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.exchange-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-exchangedb-proxy-svc -d postgres -c /stolon-data/exchange-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/agbot-backup.tar edge-computing-agbotdb-keeper-0:/stolon-data/agbot-backup.tar && \
oc exec -n kube-system edge-computing-agbotdb-keeper-0 -- bash -c "export PGPASSWORD=$(oc get secret edge-computing -o jsonpath="{.data.agbot-db-pass}" | base64 --decode) && pg_restore -U admin -h edge-computing-agbotdb-proxy-svc -d postgres -c /stolon-data/agbot-backup.tar"
```

```bash
oc -n kube-system cp $BACKUP_DIR/css-backup edge-computing-cssdb-server-0:/data/db/css-backup && \
oc exec -n kube-system edge-computing-cssdb-server-0 -- bash -c "mongorestore -u admin -p $(oc get secret edge-computing -o jsonpath="{.data.css-db-pass}" | base64 --decode) /data/db/css-backup";
```

6. 运行以下命令以刷新 kubernetes pod 数据库连接
```bash
for POD in $(oc get pods -n kube-system | grep -E '\-agbot\-|\-css\-|\-exchange\-' | awk '{print $1}'); do oc delete pod $POD -n kube-system; done
```

## 限制

* 安装限制：此产品只能安装一次，并且只能安装到 `kubbe-system` 名称空间中
* 在此发行版中，没有明确的授权特权来管理产品和操作产品。

## 文档

* 请参阅[安装](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.1/devices/installing/install.html) Knowledge Center 文档以获取更多准则和更新。

## Copyright

© Copyright IBM Corporation 2020. All Rights Reserved.
