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

# 配置 {{site.data.keyword.ieam}}

## EamHub 定制资源配置
{: #cr}

{{site.data.keyword.ieam}} 的主要配置通过 EamHub 定制资源完成，尤其是此定制资源的 **spec** 字段。

本文档假定：
* 为其运行这些命令的名称空间是部署 {{site.data.keyword.ieam}} 管理中心操作程序的位置。
* EamHub 定制资源名称是缺省 **ibm-edge**。 如果不同，请变更命令以替换 **ibm-edge**。
* 安装二进制 **jq** 以确保以可读格式显示输出。


定义的缺省值 **spec** 是最小值，仅包含许可证接受，您可以通过以下方式进行查看：
```
$ oc get eamhub ibm-edge -o yaml
...
spec:
  license:
    accept: true
...
```

### 操作程序控制循环
{: #loop}

{{site.data.keyword.ieam}} 管理中心操作程序在连续幂等循环中运行以将当前资源状态与期望的资源状态进行同步。

由于该连续循环，在尝试配置操作程序管理的资源时，您需要了解两件事：
* 控制循环将异步读取对定制资源的任何更改。进行更改后，可能需要几分钟时间以通过操作程序实施此更改。
* 操作程序强制实施特定状态可能覆盖（撤销）对操作程序控制的资源进行的任何手动更改。 

查看操作程序 pod 日志以观察此循环：
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 20 -f
```
{: codeblock}

在循环完成时，其生成 **PLAY RECAP** 摘要。 要查看最新摘要，请运行：
```
oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
```
{: codeblock}

以下指示循环已完成且未发生任何操作（在其当前状态下，**PLAY RECAP** 将始终显示 **changed=1**）：
```
$ oc logs $(oc get pods | grep ibm-eamhub-operator | awk '{print $1}') --tail 5000 | grep -A 1 '^PLAY RECAP' | tail -n 1
localhost                  : ok=51   changed=1    unreachable=0    failed=0    skipped=11   rescued=0    ignored=0
```
{: codeblock}

在进行配置更改时，查看以下三个字段：
* **changed**：在大于 **1** 时，指示操作程序执行了更改一个或多个资源状态的任务（这可能是根据您的请求更改定制资源，或者操作程序还原已执行的手动更改）。
* **rescued**：任务失败，但是这是已知的可能故障，并且将在下一次循环时重试任务。
* **failed**：在初始安装时，存在一些预期的故障，如果您重复看到相同故障，并且消息未清除（或隐藏），那么这可能指示问题。

### EamHub 常见配置选项

可进行多个配置更改，但是某些配置比其他配置更有可能发生更改。 此部分描述一些更常见的设置。

**注**：必须整体添加嵌套的配置值（请参阅[缩放配置](./configuration.md#scale)以获取示例）。这是由于整体定义嵌套字典的 Ansible 操作程序需求。

| 配置值 | 缺省值 | 描述 |
| :---: | :---: | :---: |
| 全局值 | -- | -- |
| pause_control_loop | false | 暂停以上提及的控制循环，以启用临时手动更改来进行调试。不用于稳定状态。 |
| ieam_maintenance_mode | false | 将无持久存储的所有 pod 副本计数设置为 0。用于备份复原目的。 |
| ieam_local_databases | true | 启用或禁用本地数据库。 不支持状态切换。 请参阅[远程数据库配置](./configuration.md#remote)。 |
| ieam_database_HA | true | 针对本地数据库启用或禁用 HA 方式。 这将所有数据库 pod 的副本计数设置为 **3**（如果为 **true**）和 **1**（如果为 **false**）。 |
| hide_sensitive_logs | true | 隐藏处理设置 **Kubernetes 密钥**的操作程序日志，如果设置为 **false**，那么任务失败可能导致操作程序记录编码的认证值。 |
| storage_class_name | "" | 使用缺省存储类（如果未设置）。 |

## Exchange API 转换配置

您可以配置 {{site.data.keyword.ieam}} Exchange API 以使用特定语言返回响应。要执行此操作，请使用您选择的受支持的 **LANG**（缺省值为 **en**）来定义环境变量：

```
oc set env deployment <CUSTOM_RESOURCE_NAME>-exchange HZN_EXCHANGE_LANG=<LANG>
```
{: codeblock}

**注：**有关受支持的语言代码的列表，请参阅[受支持的语言](../getting_started/languages.md)页面上的第一个表。

## 远程数据库配置
{: #remote}

**注**：不支持在远程数据库和本地数据库之间进行切换。

要使用远程数据库进行安装，请在安装期间在 **spec** 字段中使用额外值来创建 EamHub 定制资源：
```
spec:
  ieam_local_databases: false
  license:
    accept: true
```
{: codeblock}

完成以下模板以创建认证密钥，请确保阅读每个注释以确保正确填写并将其保存到 **edge-auth-overrides.yaml**：
```
apiVersion: v1
kind: Secret
metadata:
  # NOTE: The name -must- be prepended by the name given to your Custom Resource, this defaults to 'ibm-edge'
  #name: <CR_NAME>-auth-overrides
  name: ibm-edge-auth-overrides
type: Opaque
stringData:
  # agbot postgresql connection settings uncomment and replace with your settings to use
  agbot-db-host: "<Single hostname of the remote database>"
  agbot-db-port: "<Single port the database runs on>"
  agbot-db-name: "<The name of the database to utilize on the postgresql instance>"
  agbot-db-user: "<Username used to connect>"
  agbot-db-pass: "<Password used to connect>"
  agbot-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  agbot-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # exchange postgresql connection settings
  exchange-db-host: "<Single hostname of the remote database>"
  exchange-db-port: "<Single port the database runs on>"
  exchange-db-name: "<The name of the database to utilize on the postgresql instance>"
  exchange-db-user: "<Username used to connect>"
  exchange-db-pass: "<Password used to connect>"
  exchange-db-ssl: "<disable|require|verify-full>"
  # Ensure proper indentation (four spaces)
  exchange-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----

  # css mongodb connection settings
  css-db-host: "<Comma separated list including ports: hostname.domain:port,hostname2.domain:port2 >"
  css-db-name: "<The name of the database to utilize on the mongodb instance>"
  css-db-user: "<Username used to connect>"
  css-db-pass: "<Password used to connect>"
  css-db-auth: "<The name of the database used to store user credentials>"
  css-db-ssl: "<true|false>"
  # Ensure proper indentation (four spaces)
  css-db-cert: |-
    -----BEGIN CERTIFICATE-----
    ....
    -----END CERTIFICATE-----
```
{: codeblock}

创建密钥：
```
oc apply -f edge-auth-overrides.yaml
```
{: codeblock}

观察操作程序日志，如[操作程序控制循环](./configuration.md#remote)部分中所述。


## 缩放配置
{: #scale}

EamHub 定制资源配置从 {{site.data.keyword.ieam}} 管理中心公开支持大量边缘节点所需的配置参数。
OpenShift 平台识别这些更改并自动将它们应用于在 OCP 下运行的 {{site.data.keyword.ieam}} PODS。 

限制

为支持 6,000 个边缘节点 ({{site.data.keyword.ieam}} {{site.data.keyword.semver}}) 或 4,000 个边缘节点 ({{site.data.keyword.ieam}} {{site.data.keyword.version}})，不需要任何配置更改。

{{site.data.keyword.ieam}} {{site.data.keyword.semver}}:

为支持超过 6,000 个边缘节点，需要在 EamHub 定制资源配置中进行以下更改。

在 **spec** 下添加以下部分：

```
spec:
  exchange_resources:
    requests:
      memory: 512Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 5
```
{: codeblock}

## 大型环境的其他 ORG 级别配置
{: #largescale_env}

最后，为支持大于 10,000 个边缘节点的大型环境，请调整边缘节点用于检查更改的脉动信号时间间隔。 

以下命令应该由超级用户发出：
```
hzn exchange org update --heartbeatmin=60 --heartbeatmax=300 --heartbeatadjust=60 <org_name>
```
{: codeblock}

如果使用多个 ORG，那么应该针对支持大量边缘节点的每个 ORG 发出命令。

**注**：因为 {{site.data.keyword.ieam}} {{site.data.keyword.semver}} 中的限制，应该先设置 ORG 级别脉动信号值，然后再注册数以千计的边缘节点，因为代理程序在注册后将不应用 ORG 更新。 



{{site.data.keyword.ieam}} {{site.data.keyword.version}}:

为支持超过 4,000 个边缘节点，需要在 EamHub 定制资源配置中进行以下更改。
在 **spec** 下添加以下部分：

```
spec:
  exchange_resources:
    requests:
      memory: 512Mi
      cpu: 10m
    limits:
      memory: 2Gi
      cpu: 5
```
{: codeblock}
   
为使安装支持 10,000 个以上的边缘节点，除上述 **exchange_resources** 外，还需要其他配置更改。

更改参数的方式如下所示。 （注：YAML 正常间隔规则是必需的。）
1. 运行 `oc get cm ibm-edge-config -o yaml` 并抽取 **agbot_config:** 的整个部分，包括 **agbot_config:** 标记和 **|** 字符。
2. 将 **AgreementWorkers** 更改为值 **30**。
3. 将 **ProtocolTimeoutS** 更改为值 **1200**。
4. 在 **spec** 下粘贴此配置块，包含更改。
5. `oc get cm ibm-edge-config -o yaml` 的下一次运行将抽取 **exchange_config:** 的整个部分，包括 **exchange_config:** 标记和 **|** 字符。
6. 在 **cache** 配置中进行添加，并将其粘贴到定制资源。 其应该类似于：
```
spec:
  exchange_config: |
    {
      "api": {
        "cache": {
          "idsTtlSeconds": 4000
        },
        "db": {
          "jdbcUrl": "$EDGE_EXCHANGE_DB_URL",
          "maxConnectionAge": 3600,
          "maxIdleTimeExcessConnections": 0,
          "maxPoolSize": "30",
          "password": "$EDGE_EXCHANGE_DB_PASS",
          "user": "$EDGE_EXCHANGE_DB_USER"
        },
        "logging": {
          "level": "INFO"
        },
        "root": {
          "enabled": "true",
          "password": "$EDGE_EXCHANGE_ROOT_PASS"
        }
      }
    }
```
{: codeblock}

## 大型环境的其他 ORG 级别配置

最后，为支持大于 10,000 个边缘节点的大型环境，请调整边缘节点用于检查更改的脉动信号时间间隔。 

以下命令应该由超级用户发出：
```
hzn exchange org update --heartbeatmin=60 --heartbeatmax=900 --heartbeatadjust=60 <org_name>
```
{: codeblock}

如果使用多个 ORG，那么应该针对支持大量边缘节点的每个 ORG 发出命令。

