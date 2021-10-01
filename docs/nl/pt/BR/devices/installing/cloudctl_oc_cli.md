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

# Instalando o cloudctl, o kubectl e o oc
{: #cloudctl_oc_cli}

As ferramentas da linha de comandos são necessárias para gerenciar aspectos do hub de gerenciamento e dos clusters de borda do {{site.data.keyword.edge_notm}}. Instale-os usando estas etapas:

* **cloudctl and kubectl:** obtenha a CLI do IBM Cloud Pak (**cloudctl**) e a CLI do Kubernetes (**kubeclt**) usando a IU da web do {{site.data.keyword.edge_notm}} em: `https://<CLUSTER_URL>/common-nav/cli`

  * Uma alternativa para a instalação de **kubectl** no {{site.data.keyword.macOS_notm}} é usar o [homebrew ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://brew.sh/):
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc:** obtenha a CLI do {{site.data.keyword.open_shift_cp}} a partir da [CLI do cliente OpenShift (oc) ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/).

  * Uma alternativa para a instalação de **oc** no {{site.data.keyword.macOS_notm}} é usar o [homebrew ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://brew.sh/):
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
