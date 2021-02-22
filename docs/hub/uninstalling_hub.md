---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}



# Uninstall
{: #uninstalling_hub}

**Warning:** Deleting the **EamHub** custom resource immediately removes the resources that the {{site.data.keyword.ieam}} management hub depends on including IBM Cloud Platform Common Services components. Ensure that is your intent before proceeding.

See the [backup and recovery](../admin/backup_recovery.md) page if this uninstallation is being performed to facilitate a restoration to a previous state.

* Log in to the cluster as a cluster administrator by using **cloudctl** or **oc login**, to the namespace where your {{site.data.keyword.ieam}} operator is installed.
* Run the following to delete the custom resource (default **ibm-edge**):
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* Ensure that all {{site.data.keyword.ieam}} management hub pods have terminated, and only the two operator pods that are shown here are running before proceeding to the next step:
  ```
  $ oc get pods
  NAME                                           READY   STATUS    RESTARTS   AGE
  ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h
  ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* Uninstall the {{site.data.keyword.ieam}} management hub operator using the OpenShift cluster console. Select the namespace where your {{site.data.keyword.ieam}} operator is installed, and navigate to **Operators** > **Installed Operators** > the overflow menu icon of **IEAM Management Hub** > **Uninstall Operator**.
* Follow the **Uninstalling all services** instructions on the IBM Cloud Platform Common Services [Uninstallation](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/uninstallation.html) page, replacing any occurrences of the **common-service** namespace with the namespace where your {{site.data.keyword.ieam}} operator is installed.
