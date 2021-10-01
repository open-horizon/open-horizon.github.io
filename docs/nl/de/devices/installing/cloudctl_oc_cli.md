---

copyright:
  years: 2020
lastupdated: "2020-5-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 'cloudctl', 'kubectl' und 'oc' installieren
{: #cloudctl_oc_cli}

Die Befehlszeilentools sind erforderlich, um Aspekte der {{site.data.keyword.edge_notm}}-Management-Hub-Cluster und -Edge-Cluster zu verwalten. Installieren Sie sie mit folgenden Schritten:

* **cloudctl und kubectl:** Rufen Sie die IBM Cloud Pak-CLI (**cloudctl**) und die Kubernetes-CLI (**kubeclt**) über Ihre {{site.data.keyword.edge_notm}}-Webbenutzerschnittstelle unter `https://<CLUSTER_URL>/common-nav/cli` ab.

  * Eine Alternative für die Installation von **kubectl** unter {{site.data.keyword.macOS_notm}} ist die Verwendung von [homebrew ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://brew.sh/):
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc:** Rufen Sie die {{site.data.keyword.open_shift_cp}}-CLI unter [OpenShift-Client-CLI (oc) ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/) ab.

  * Eine Alternative für die Installation von **oc** unter {{site.data.keyword.macOS_notm}} ist die Verwendung von [homebrew ![Wird auf einer neuen Registerkarte geöffnet](../../images/icons/launch-glyph.svg "Wird auf einer neuen Registerkarte geöffnet")](https://brew.sh/):
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
