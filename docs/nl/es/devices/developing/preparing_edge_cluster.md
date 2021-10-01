---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparación de un clúster periférico
{: #preparing_edge_cluster}

## Antes de empezar

Tenga en cuenta lo siguiente antes de empezar a trabajar con clústeres periféricos:

* [Requisitos previos](#preparing_clusters)
* [Recopile la información y los archivos necesarios para los clústeres periféricos](#gather_info)

## Requisitos previos
{: #preparing_clusters}

Antes de instalar un agente en un clúster periférico:

1. Instale Kubectl en el entorno en el que se ejecuta el script de instalación de agente.
2. Instale la CLI de cliente de {{site.data.keyword.open_shift}} (oc) en el entorno en el que
se ejecuta el script de instalación de agente.
3. Obtenga el acceso de administrador de clúster, que es necesario para crear los recursos de clúster pertinentes.
4. Disponga de un registro de clúster periférico para alojar la imagen de Docker de agente.
5. Instale los mandatos **cloudctl** y **kubectl**
y extraiga **ibm-edge-computing-4.1-x86_64.tar.gz**. Consulte
[Proceso de instalación](../installing/install.md#process).

## Recopilar la información y los archivos necesarios para clústeres periféricos
{: #gather_info}

Necesita varios archivos para instalar y registrar los clústeres periféricos
con {{site.data.keyword.edge_notm}}. Esta sección le guiará durante la recopilación de esos archivos
en un archivo tar, que a continuación puede utilizar en cada uno de los clústeres periféricos.

1. Establezca las variables de entorno **CLUSTER_URL**:

    ```
    export CLUSTER_URL=<URL-de-clúster>
   export USER=<su-usuario-administrador-de-ICP>
   export PW=<su-contraseña-de-administrador-de-ICP>
    ```
    {: codeblock}

    De forma alternativa, después de conectar con el clúster con **oc login**, puede ejecutar:

    ```
    export CLUSTER_URL=https://$(oc get routes icp-console -o jsonpath='{.spec.host}')
    ```
    {: codeblock}
    
2. Utilice los privilegios de administrador de clúster para conectar con el clúster y, a continuación,
seleccione **kube-system** como espacio de nombres y rellene la contraseña que ha definido en
config.yaml durante el proceso de instalación de {{site.data.keyword.mgmt_hub}}[](../installing/install.md#process):

    ```
    cloudctl login -a $CLUSTER_URL -u admin -p <su-contraseña-de-adminisrador-de-icp> -n kube-system --skip-ssl-validation
    ```
    {: codeblock}    

3. Establezca el nombre de usuario, la contraseña y el nombre de imagen completa de registro de
clúster periférico en el registro de clúster periférico de las variables de entorno. El valor de
IMAGE_ON_EDGE_CLUSTER_REGISTRY se especifica en este formato:

    ```
    <nombre-registro>/<nombre-repo>/<nombre-imagen>.
    ```
    {: codeblock} 

    Si utiliza el hub de Docker como registro, especifique el valor en este formato:
    
    ```
    <nombre-repo-docker>/<nombre-imagen>
    ```
    {: codeblock}
    
    Por ejemplo:
    
    ```
    export EDGE_CLUSTER_REGISTRY_USER=<su-nombre-usuario-registro-clúster-periférico>
    export EDGE_CLUSTER_REGISTRY_PW=<su-contraseña-registro-clúster-periférico>
    export IMAGE_ON_EDGE_CLUSTER_REGISTRY=<nombre-imagen-completa-en-su-registro-clúster-periférico>
    ```
    {: codeblock}
    
4. Descargue la versión más reciente de **edgeDeviceFiles.sh**:

   ```
   curl -O https://raw.githubusercontent.com/open-horizon/examples/master/tools/edgeDeviceFiles.sh chmod +x edgeDeviceFiles.sh
   ```
   {: codeblock}

5. Ejecute el script **edgeDeviceFiles.sh** para recopilar los archivos necesarios:

   ```
   ./edgeDeviceFiles.sh x86_64-Cluster -t -r -o <id-org-hzn> -n <id-nodo> <otros distintivos>
   ```
   {: codeblock}
    
   Esto crea un archivo denominado agentInstallFiles-x86_64-Cluster .. tar.gz. 
    
**Argumentos de mandato**
   
Nota: Especifique x86_64-Clúster para instalar el agente en un clúster periférico.
   
|Argumentos de mandato|Resultado|
|-----------------|------|
|t                |Cree un archivo **agentInstallFiles-&lt;tipo-dispositivo-periférico&gt;.tar.gz** que contenga todos los archivos recopilados. Si este distintivo no se ha establecido, los archivos recopilados se colocan en el directorio actual.|
|f                |Especifique un directorio al que mover los archivos recopilados. Si el directorio no existe, se creará. El directorio actual es el valor predeterminado|
|r                |Es necesario establecer **EDGE_CLUSTER_REGISTRY_USER**, **EDGE_CLUSTER_REGISTRY_PW** y **IMAGE_ON_EDGE_CLUSTER_REGISTRY** en la variable de entorno (paso 1) si se utiliza este distintivo. En 4.1, es un distintivo necesario.|
|o                |Especifique **HZN_ORG_ID**. Este valor se utiliza para el registro de clúster periférico.|
|n                |Especifique **NODE_ID**, que debe ser el valor del nombre de clúster periférico. Este valor se utiliza para el registro de clúster periférico.|
|s                |Especifique la clase de almacenamiento de clúster que la reclamación de volumen persistente deberá utilizar. La clase de almacenamiento predeterminada es "gp2".|
|i                |La versión de imagen de agente que se debe desplegar en el clúster periférico|


Cuando esté listo para instalar el agente en el clúster periférico, consulte
[Instalación de un agente y registro de un clúster periférico](importing_clusters.md).

<!--DELETE DOWN TO    
   The following flags are only supported for x86_64-Cluster:

    * **-r**: specify edge cluster registry if edge cluster is not using Openshift image registry. "EDGE_CLUSTER_REGISTRY_USER", "EDGE_CLUSTER_REGISTRY_PW" and "EDGE_CLUSTER_REGISTRY_REPONAME" need to be set in environment variable (step 1) if using this flag.
    * **-s**: specify cluster storage class to be used by persistent volume claim. Default storage class is "gp2".
    * **-i**: agent image version to be deployed on edge cluster
    * **-o**: specify HZN_ORG_ID. This value is used for edge cluster registration.
    * **-n**: specify NODE_ID. NODE_ID should be the value of your edge cluster name. This value is used for edge cluster registration. 

4. The command in the previous step creates a file that is called **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz**. If you have other types of edge devices (different architectures), repeat the previous step for each type.

5. Take note of the API key that was created and displayed by the **edgeDeviceFiles.sh** command.

6. Now that you are logged in via **cloudctl**, if you need to create additional API keys for users to use with the {{site.data.keyword.horizon}} **hzn** command:

   ```
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   In the output of the command look for the key value in the line that starts with **API Key** and save the key value for future use.

7. When you are ready to set up edge devices, follow [Getting started using {{site.data.keyword.edge_devices_notm}}](../getting_started/getting_started.md).

Lily - is the pointer in step 7 above still correct?-->

## Qué hacer a continuación

* [Instalación de un agente y registro de un clúster periférico](importing_clusters.md)

## Información relacionada

* [Clústeres periféricos](edge_clusters.md)
* [Cómo empezar a utilizar {{site.data.keyword.edge_notm}}](../getting_started/getting_started.md)
* [Proceso de instalación](../installing/install.md#process)
