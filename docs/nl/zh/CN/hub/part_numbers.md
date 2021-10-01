---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Passport Advantage
{: #part_numbers}

完成以下过程以下载 {{site.data.keyword.ieam}} 软件包：

1. 查找 {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) 部件号。
2. 转至位于 [Passport Advantage ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/software/passportadvantage/) 的 IBM Passport Advantage Online 选项卡，并使用您的 IBM ID 登录。
2. 使用 [{{site.data.keyword.ieam}} 软件包和部件号](#part_numbers_table)中列出的部件号来搜索文件：
3. 将文件下载到计算机上的目录。

## {{site.data.keyword.ieam}}软件包和部件号
{: #part_numbers_table}

|部件描述|Passport Advantage 部件号|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} 资源价值单元许可证 + 软件预订和支持 12 个月|D2840LL|
|{{site.data.keyword.edge_notm}} 资源价值单元年软件预订和支持 RNWL 12 个月|E0R0HLL|
|{{site.data.keyword.edge_notm}} 资源价值单元年软件预订和支持 REINSTATE 12 个月|D2841LL|
|{{site.data.keyword.edge_notm}} 资源价值单元每月许可证|D283ZLL|
|{{site.data.keyword.edge_notm}} 资源价值单元承诺期限许可证|D28I1LL|
{: caption="表 1. {{site.data.keyword.ieam}}软件包和部件号" caption-side="top"}

## 许可
{: #licensing}

根据已注册的节点总数算出许可需求。 在已安装 **hzn** CLI，且 CLI 已配置为向管理中心进行认证的系统上，确定已注册的节点总数：

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

输出为整数，请参阅以下样本输出：

  ```
  $ hzn exchange status | jq .numberOfNodes
  2641
  ```

使用 [{{site.data.keyword.ieam}} 4.1 许可证信息文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://www.ibm.com/software/sla/sladb.nsf/displayLIs/D4C02F02F4E383AF85258581000B9E30?OpenDocument) 中的以下转换表来计算所需许可证数，并显示通过先前命令返回的适用于环境的节点计数：

  ```
  From 1 to 10 Resources, 1.00 UVU per Resource
  From 11 to 50 Resources, 10.0 UVUs plus 0.87 UVUs per Resource above 10
  From 51 to 100 Resources, 44.8 UVUs plus 0.60 UVUs per Resource above 50
  From 101 to 500 Resources, 74.8 UVUs plus 0.25 UVUs per Resource above 100
  From 501 to 1,000 Resources, 174.8.0 UVUs plus 0.20 UVUs per Resource above 500
  From 1,001 to 10,000 Resources, 274.8 UVUs plus 0.07 UVUs per Resource above 1,000
  From 10,001 to 25,000 Resources, 904.8 UVUs plus 0.04 UVUs per Resource above 10,000
  From 25,001 to 50,000 Resources, 1,504.8 UVUs plus 0.03 UVUs per Resource above 25,000
  From 50,001 to 100,000 Resources, 2,254.8 UVUs plus 0.02 UVUs per Resource above 50,000
  For more than 100,000 Resources, 3,254.8 UVUs plus 0.01 UVUs per Resource above 100,000
  ```

以下示例显示了计算 **2641** 个节点所需的许可证数的过程，结果为需要购买**至少 390** 个许可证：

  ```
  274.8 + ( .07 * ( 2641 - 1000 ) )
  274.8 + ( .07 * 1641 )
  274.8 + 114.87
  389.67
  ```
