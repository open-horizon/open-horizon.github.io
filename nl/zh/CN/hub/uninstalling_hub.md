---

copyright:
years: 2020
lastupdated: "2020-10-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# 卸载
{: #uninstalling_hub}

**警告：**删除 **EamHub** 定制资源将立即除去 {{site.data.keyword.ieam}} 管理中心所依赖于的资源，包括 IBM Cloud Platform Common Services 组件。 在继续前，确保这是您的意图。

如果将执行此卸载以促进复原至先前状态，请参阅[备份和恢复](../admin/backup_recovery.md)页面。

* 使用 **cloudctl** 或 **oc login** 以集群管理员身份登录到集群，直至安装 {{site.data.keyword.ieam}} 操作程序的名称空间。
* 运行以下命令以删除定制资源（缺省值为 **ibm-edge**）：
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* 确保所有 {{site.data.keyword.ieam}} 管理中心 pod 已终止，并且仅此处显示的两个操作程序 pod 正在运行，然后再继续下一步：
  ```
  $ oc get pods
  NAME                                           READY   STATUS    RESTARTS   AGE
  ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h
  ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* 使用 OpenShift 集群控制台，卸载 {{site.data.keyword.ieam}} 管理中心操作程序。 选择在其中安装 {{site.data.keyword.ieam}} 操作程序的名称空间，然后浏览至**操作程序** > **已安装的操作程序** > **IEAM 管理中心**的溢出菜单图标 > **卸载操作程序**。
* 遵循 IBM Cloud Platform Common Services [卸载](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/uninstallation.html)页面上的**卸载所有服务**指示信息，将出现的任何 **common-service** 名称空间替换为在其中安装 {{site.data.keyword.ieam}} 操作程序的名称空间。
