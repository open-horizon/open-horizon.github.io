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

# Instalación de cloudctl, kubectl y oc
{: #cloudctl_oc_cli}

Las herramientas de línea de mandatos son necesarias para gestionar aspectos del centro de gestión y de los clústeres periféricos de {{site.data.keyword.edge_notm}}. Instálelos utilizando estos pasos:

* **cloudctl y kubectl:** Obtenga la CLI de IBM Cloud Pak (**cloudctl**)
y la CLI de kubernetes (**kubeclt**) de la interfaz de usuario web de
{{site.data.keyword.edge_notm}} en: `https://<CLUSTER_URL>/comm/nav/cli`

  * Una alternativa para instalar **kubectl** en {{site.data.keyword.macOS_notm}} es utilizar [homebrew ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://brew.sh/):
  
    ```bash
    brew install kubernetes-cli`
    ```
    {: codeblock}

* **oc:** Obtenga la CLI de {{site.data.keyword.open_shift_cp}} de la [CLI de cliente de OpenShift (oc) ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/).

  * Una alternativa para instalar **oc** en {{site.data.keyword.macOS_notm}} consiste en utilizar [homebrew ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://brew.sh/):
  
    ```bash
    brew install openshift-cli`
    ```
    {: codeblock}
