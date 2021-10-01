---

copyright:
  years: 2020
lastupdated: "2020-02-1"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 大小调整和系统需求

在安装 {{site.data.keyword.edge_servers_notm}} 之前，请复查每个产品的系统需求以及资源占用量调整。
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [调整多集群端点的大小](#mc_endpoint)
  - [调整管理中心服务的大小](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [{{site.data.keyword.ocp_tm}} 安装文档 ![在新选项卡中打开](../images/icons/launch-glyph.svg "在新选项卡中打开")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* {{site.data.keyword.open_shift_cp}} 计算或工作程序节点：16 核 | 32 GB RAM

  注：如果要安装 {{site.data.keyword.edge_devices_notm}} 以及 {{site.data.keyword.edge_servers_notm}}，那么需要添加[调整大小部分](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)中概述的其他节点资源。
  
* 存储需求：
  - 对于脱机安装，{{site.data.keyword.open_shift_cp}} 映像注册表至少需要 100 GB。
  - 管理服务 MongoDB 和日志记录都需要 20 GB 存储类。
  - 漏洞顾问程序需要 60 GB 存储类（如果已启用）。

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

大小调整可用于最小和生产占用量。

### {{site.data.keyword.open_shift}} 和 {{site.data.keyword.edge_servers_notm}} 的部署拓扑

| 部署拓扑 | 使用情况描述 | {{site.data.keyword.open_shift}} 4.2 节点配置 |
| :--- | :--- | :--- | :---|
| 最小 | 小型集群部署 | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 个主节点 <br> &nbsp; 2 个或更多工作程序节点 </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 个专用工作程序节点 </p> |
| 生产 | 支持缺省配置 <br> {{site.data.keyword.edge_servers_notm}}| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 个主节点（本机 HA） <br>&nbsp; 4 个或更多工作程序节点 </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 个专用工作程序节点|
{: caption="表 1. {{site.data.keyword.edge_servers_notm}} 的部署拓扑配置" caption-side="top"}

注：对于专用 {{site.data.keyword.edge_servers_notm}} 工作程序节点，将主节点、管理节点和代理节点设置为一个 {{site.data.keyword.open_shift}} 工作程序节点，在{{site.data.keyword.edge_servers_notm}} [安装文档](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)中配置此节点。

注：以下指示的所有持久卷都是缺省值。 必须基于随时间存储的数据量来调整卷的大小。

### 最小大小调整
| 配置 | 节点数 | vCPU | 内存 | 持久卷 (GB) | 磁盘空间 (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| 主、管理、代理	| 1| 16	| 32	| 20  | 100  |
{: caption="表 2. {{site.data.keyword.edge_servers_notm}} 的最小 {{site.data.keyword.open_shift}} 节点大小调整" caption-side="top"}

### 生产大小调整

| 配置 | 节点数 | vCPU | 内存 | 持久卷 (GB) | 磁盘空间 (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| 主、管理、代理	| 3| 48	| 96	| 60  | 300  |
{: caption="表 3. {{site.data.keyword.edge_servers_notm}} 的生产 {{site.data.keyword.open_shift}} 节点大小调整" caption-side="top"}

## 多集群端点大小调整
{: #mc_endpoint}

| 组件名称                 	| 可选 	| CPU 请求 	| CPU 限制  	| 内存请求  	| 内存限制 	|
|--------------------------------	|----------	|-------------	|------------	|-----------------	|--------------	|
| ApplicationManager             	| True     	| 100 mCore   	| 500mCore   	| 128 MiB         	| 2 GiB        	|
| WorkManager                    	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB       |
| ConnectionManager              	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| ComponentOperator              	| False    	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| CertManager                    	| False    	| 100 mCore   	| 300 mCore  	| 100 MiB         	| 300 MiB      	|
| PolicyController               	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| SearchCollector                	| True     	| 25 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| ServiceRegistry                	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 258 MiB      	|
| ServiceRegistryDNS             	| True     	| 100 mCore   	| 500 mCore  	| 70 MiB          	| 170 MiB      	|
| MeteringSender                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringReader                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringDataManager            	| True     	| 100 mCore   	| 1000 mCore 	| 256 MiB         	| 2560 MiB     	|
| MeteringMongoDB                	| True     	| -           	| -          	| 500 MiB           | 1 GiB        	|
| Tiller                         	| True     	| -           	| -          	| -               	| -            	|
| TopologyWeaveScope(1 per node) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="表 4. 多集群端点指示信息" caption-side="top"}

## 管理中心服务大小调整
{: #management_services}

| 服务名称                 | 可选 | CPU 请求 | CPU 限制 | 内存请求 | 内存限制 | 持久卷（缺省值） | 其他注意事项 |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui、Common-web-ui、iam-policy-controller、key-management、mcm-kui、metering、monitoring、multicluster-hub、nginx-ingress、search | 缺省值 | 9,025 m | 29,289 m | 16,857 Mi | 56,963 Mi | 20 GiB | |
| 审计日志记录 | 可选 | 125 m | 500 m | 250 Mi | 700 Mi | | |
| CIS 策略控制器 | 可选 | 525 m | 1,450 m | 832 Mi | 2,560 Mi | | |
| 映像安全性实施 | 可选 | 128 m | 256 m | 128 Mi | 256 Mi | | |
| 许可 | 可选 | 200 m | 500 m | 256 Mi | 512 Mi | | |
| 日志记录 | 可选 | 1,500 m | 3,000 m | 9,940 Mi | 10,516 Mi | 20 GiB | |
| 多租户帐户配额实施 | 可选 | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Mutation Advisor | 可选 | 1,000 m | 3,300 m | 2,052 Mi | 7,084 Mi | 100 GiB | |
| Notary | 可选 | 600 m | 600 m  | 1,024 Mi | 1,024 Mi | | |
| 密钥加密策略控制器 | 可选 | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| 安全令牌服务 (STS) | 可选 | 410 m | 600 m  | 94 Mi  | 314 Mi | | 需要 Red Hat OpenShift 服务网 (Istio) |
| 系统运行状况检查服务 | 可选 | 75 m | 600 m | 96 Mi | 256 Mi | | |
| 漏洞顾问程序 (VA) | 可选 | 1,940 m | 4,440 m | 8,040 Mi | 27,776 Mi | 10 GiB | 需要 Red Hat OpenShift 日志记录 (Elasticsearch) |
{: caption="表 5. 中心服务大小调整" caption-side="top"}

## 后续操作

返回到{{site.data.keyword.edge_servers_notm}}[安装文档](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)。
