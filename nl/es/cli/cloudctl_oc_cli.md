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

Siga estos pasos para instalar las herramientas de línea de mandatos que son necesarias para gestionar aspectos de los clústeres periféricos y del centro de gestión de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}):

## cloudctl

1. Examine la IU web de {{site.data.keyword.ieam}} en: `https://<CLUSTER_URL>/common-nav/cli`

2. Expanda la sección **CLI de IBM Cloud Pak** y seleccione **OS**.

3. Copie el mandato **curl** visualizado y ejecútelo para descargar el binario **cloudctl**.

4. Haga que el archivo sea ejecutable y muévalo a **/usr/local/bin**:
  
   ```bash
   chmod 755 cloudctl-*    sudo mv cloudctl-* /usr/local/bin/cloudctl
   ```
   {: codeblock}

5. Asegúrese de que **/usr/local/bin** está en la PATH y, a continuación, verifique que **cloudctl** está funcionando:
  
   ```bash
   cloudctl --help
   ```
   {: codeblock}

## oc

1. Descargue el archivo tar de CLI de {{site.data.keyword.open_shift_cp}} de la [CLI de cliente de OpenShift (oc)](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest/). Seleccione el archivo **openshift-client-\*-\*.tar.gz** para el sistema operativo.

2. Busque el archivo tar descargado y desempaquételo:
  
   ```bash
   tar -zxvf openshift-client-*-*.tar.gz
   ```
   {: codeblock}

3. Mueva el mandato **oc** a **/usr/local/bin**:
  
   ```bash
   sudo mv oc /usr/local/bin/
   ```
   {: codeblock}

4. Asegúrese de que **/usr/local/bin** está en la PATH y verifique que **oc** está funcionando:
  
   ```bash
   oc --help
   ```
   {: codeblock}

Como alternativa, utilice [homebrew](https://brew.sh/) para instalar **oc** en {{site.data.keyword.macOS_notm}}:
  
   ```bash
   brew install openshift-cli
   ```
   {: codeblock}

## Kubectl

Siga las instrucciones de [Instalar y configurar kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/).
