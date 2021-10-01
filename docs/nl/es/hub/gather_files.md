---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Recopilar archivos de nodo periférico
{: #prereq_horizon}

Se necesitan varios archivos para instalar el agente {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) en los dispositivos periféricos y los clústeres periféricos y registrarlos en {{site.data.keyword.ieam}}. Este contenido le guía por el proceso de empaquetado de los archivos necesarios para los nodos periféricos. Realice estos pasos en un host de administración que esté conectado al centro de gestión de {{site.data.keyword.ieam}}.

En los pasos siguientes, se presupone que ha instalado los mandatos de [CLI de IBM Cloud Pak (**cloudctl**) y CLI de cliente de OpenShift (**oc**)](../cli/cloudctl_oc_cli.md) y que está ejecutando los pasos desde el directorio de soporte de instalación no desempaquetado **ibm-eam-{{site.data.keyword.semver}}-bundle**. Este script busca los paquetes {{site.data.keyword.horizon}} necesarios en el archivo **agent/edge-packages-{{site.data.keyword.semver}}.tar.gz** y crea los archivos de certificado y configuración de nodo periférico necesarios.

1. Inicie sesión en el clúster de centro de gestión con credenciales de administrador y el espacio de nombres de la instalación de {{site.data.keyword.ieam}}:
   ```bash
   cloudctl login -a &amp;TWBLT;cluster-url&gt; -u &amp;TWBLT;cluster-admin-user&gt; -p &amp;TWBLT;cluster-admin-password&gt; -n &amp;TWBLT;namespace&gt; --skip-ssl-validation
   ```
   {: codeblock}

2. Establezca las variables de entorno siguientes:

   ```bash
   export CLUSTER_URL=https://$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}') oc --insecure-skip-tls-verify=true -n kube-public get secret ibmcloud-cluster-ca-cert -o jsonpath="{.data.ca\.crt}" | base64 --decode &gt; ieam.crt export HZN_MGMT_HUB_CERT_PATH="$PWD/ieam.crt" export HZN_FSS_CSSURL=${CLUSTER_URL}/edge-css
   ```
   {: codeblock}

   Defina las siguientes variables de autenticación de Docker, proporcionando su propia **ENTITLEMENT_KEY**:
   ```
   export REGISTRY_USERNAME=cp export REGISTRY_PASSWORD=<ENTITLEMENT_KEY>
   ```
   {: codeblock}

   **Nota:** Obtenga la clave de titularidad a través de [Mi clave de IBM](https://myibm.ibm.com/products-services/containerlibrary).

3. Vaya al directorio **agent** donde **edge-packages-{{site.data.keyword.semver}}.tar.gz** es:

   ```bash
   cd agent
   ```
   {: codeblock}

4. Hay dos formas preferidas de recopilar los archivos para la instalación de nodos periféricos utilizando el script **edgeNodeFiles.sh**. Elija uno de los métodos siguientes en función de sus necesidades:

   * Ejecute el script **edgeNodeFiles.sh** para recopilar los archivos necesarios y colocarlos en el componente CSS (Cloud Sync Service) del sistema de gestión de modelos (MMS).

     **Nota**: El script **edgeNodeFiles.sh** se ha instalado como parte del paquete horizon-cli y debe estar en la vía de acceso.

     ```bash
     HZN_EXCHANGE_USER_AUTH='' edgeNodeFiles.sh ALL -c -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     En cada nodo periférico, utilice el distintivo **-i 'css:'** de **agent-install.sh** para hacerle obtener los archivos necesarios de CSS.

     **Nota**: Si tiene previsto utilizar los [dispositivos periféricos habilitados para SDO](../installing/sdo.md), debe ejecutar este formato del mandato `edgeNodeFiles.sh`.

   * Como alternativa, utilice **edgeNodeFiles.sh** para empaquetar los archivos en un archivo tar:

     ```bash
     edgeNodeFiles.sh ALL -t -p edge-packages-{{site.data.keyword.semver}} -r cp.icr.io/cp/ieam
     ```
     {: codeblock}

     Copie el archivo tar en cada nodo periférico y utilice el distintivo **-z** de **agent-install.sh** para obtener los archivos necesarios del archivo tar.

     Si todavía no ha instalado el paquete **horizon-cli** en este host, hágalo ahora. Consulte [Configuración posterior a la instalación](post_install.md#postconfig) para ver un ejemplo de este proceso.

     Localice los scripts **agent-install.sh** y **agent-uninstall.sh** que se han instalado como parte del paquete **horizon-cli**.    Estos scripts son necesarios en cada nodo periférico durante la configuración (actualmente **agent-uninstall.sh** sólo soporta clústeres periféricos):
    * Ejemplo de {{site.data.keyword.linux_notm}}:

     ```
     ls /usr/horizon/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

    * Ejemplo de macOS:

     ```
     ls /usr/local/bin/agent-{install,uninstall}.sh
     ```
     {: codeblock}

**Nota**: **edgeNodeFiles.sh** tiene más distintivos para controlar qué archivos se recopilan y dónde deben colocarse. Para ver todos los distintivos disponibles, ejecute: **edgeNodeFiles.sh -h**

## Qué hacer a continuación

Antes de configurar nodos periféricos, el usuario o los técnicos de nodo deben crear una clave de API y recopilar otros valores de variables de entorno. Siga los pasos recogidos en [Creación de la clave de API](prepare_for_edge_nodes.md).
