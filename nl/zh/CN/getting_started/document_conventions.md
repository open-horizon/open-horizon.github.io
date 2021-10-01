---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 此文档中使用的约定
{: #document_conventions}

此文档使用内容约定来表达特定含义。  

## 命令约定

将 < > 中显示的变量内容替换为特定于您的需求的值。 请不要在命令中包含 < > 字符。

### 示例

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
   
## 文字串

您在管理中心上或在代码中看到内容为文字串。 此内容显示**粗体**文本。
   
 ### 示例
   
 如果检查 `service.sh` 代码，您会发现它使用这些配置变量和其他配置变量来控制其行为。 **PUBLISH** 控制代码是否尝试将消息发送到 IBM Event Streams。 **MOCK** 控制 service.sh 是否尝试联系 REST API 及其相依服务（cpu 和 gps）或 `service.sh` 是否创建假数据。
  
