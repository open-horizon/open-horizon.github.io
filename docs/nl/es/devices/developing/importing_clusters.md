---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalación de un agente y registro de un clúster periférico
{: #importing_clusters}

Puede instalar agentes en estos clústeres periféricos:

* Kubernetes
* Kuberetes pequeños ligeros (se recomiendan para las pruebas)

## Instalación de agentes en clústeres periféricos Kubernetes
{: #install_kube}

Hay una instalación de agente automatizada disponible ejecutando el script `agent-install.sh`. 

Siga estos pasos en el entorno en el que se ejecutará el script de instalación de agente:

1. Obtenga el archivo `agentInstallFiles-x86_64-Cluster.tar.gz` y una clave de API del administrador. Éstos ya se deben haber creado en [Recopilar la información y los archivos necesarios para los clústeres periféricos](preparing_edge_cluster.md).  

2. Establezca el nombre de archivo en una variable de entorno para los pasos siguientes:

   ```
   export AGENT_TAR_FILE=agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

3. Extraiga los archivos del archivo tar:

   ```
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz
   ```
   {: codeblock}

4. Exporte las credenciales de usuario de Horizon Exchange, que pueden estar en una de estas formas:

   ```
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
   {: codeblock}

   o

   ```
   export HZN_EXCHANGE_USER_AUTH=<nombre_usuario>/<nombre_usuario>:<contraseña>
   ```
   {: codeblock}

5. Ejecute el mandato `agent-install.sh` para instalar y configurar el agente de Horizon y registre el clúster periférico para ejecutar el servicio periférico de ejemplo helloworld:

   ```
   ./agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p
   ```
   {: codeblock}

   Nota: Durante la instalación de agente, es posible que vea esta solicitud: **¿Desea sobrescribir horizon?[y/N]:**. Seleccione **y** y pulse **Intro**; `agent-install.sh` establece la configuración correctamente.

6. (Opcional) Para ver las descripciones de distintivo `agent-install.sh` disponibles: 

   ```
   ./agent-install.sh -h
   ```
   {: codeblock}

7. Liste los recursos de agente que se ejecutan en Kubernetes. Ahora, que el agente está instalado en el clúster periférico y que el clúster periférico está registrado, puede listar los siguientes recursos de clúster periféricos:

   * Espacio de nombres:

   ```
   kubectl get namespace openhorizon-agent
   ```
   {: codeblock}

   * Despliegue:

   ```
   kubectl get deployment -n openhorizon-agent
   ```
   {: codeblock}

   Para listar los detalles del despliegue de agente:

   ```
   kubectl get deployment -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Configmap:

   ```
   kubectl get configmap openhorizon-agent-config -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Secret:
   
   ```
   kubectl get secret openhorizon-agent-secrets -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * PersistentVolumeClaim:
   
   ```
   kubectl get pvc openhorizon-agent-pvc -n openhorizon-agent -o yaml
   ```
   {: codeblock}

   * Pod:

   ```
   kubectl get pod -n openhorizon-agent
   ```
   {: codeblock}

8. Ver registros, obtener el ID de pod y: 

   ```
   kubectl logs <pod-id> -n openhorizon-agent
   ```
   {: codeblock}

9. Ejecute el mandato `hzn` dentro del contenedor de agente:

   ```
   kubectl exec -it <pod-id> -n openhorizon-agent /bin/bash
   hzn --help
   ```
   {: codeblock}

10. Explore los distintivos de mandato `hzn` y el submandato:

   ```
   hzn --help
   ```
   {: codeblock}

## Instalación de agentes en clústeres periféricos pequeños y ligeros de Kubernetes

En este contenido se describe cómo instalar el agente en microk8s, un clúster ligero y pequeño de kubernetes que puede instalar y configurar localmente, incluyendo:

* Instalación y configuración de microk8s
* Instalación de un agente en microk8s

### Instalación y configuración de microk8s

1. Instale microk8s:

   ```
   sudo snap install microk8s --classic --channel=1.14/stable
   ```
   {: codeblock}

2. Establezca un alias para microk8s.kubectl:

   Nota: Asegúrese de que no tiene el mandato `kubectl` si desea realizar pruebas en microk8s. 

  * MicroK8s utiliza un mandato kubectl con espacio de nombres para impedir conflictos con las instalaciones existentes de kubectl. Si no dispone de una instalación existente, es más fácil añadir un alias (`append to ~/.bash_aliases`): 
   
   ```
   alias kubectl='microk8s.kubectl' 
   ```
   {: codeblock}
  
   * A continuación:

   ```
   source ~/.bash_aliases
   ```
   {: codeblock}

3. Habilite el módulo de almacenamiento y dns en microk8s:

   ```
   microk8s.enable dns storage
   ```
   {: codeblock}

4. Cree la clase de almacenamiento en microk8s. El script de instalación de agente utiliza `gp2` como la clase de almacenamiento predeterminada para la reclamación de volumen persistente. Esta clase de almacenamiento se debe crear en el entorno de microk8s antes de instalar el agente. Si el agente de clúster periférico va a utilizar otra clase de almacenamiento, también se debe crear de antemano. 

   A continuación se muestra un ejemplo de creación de `gp2` como clase de almacenamiento:  

   1. Cree un archivo storageClass.yml: 

      ```
      apiVersion: storage.k8s.io/v1
      kind: StorageClass
      metadata:
       name: gp2
      provisioner: microk8s.io/hostpath
      reclaimPolicy: Delete
      volumeBindingMode: Immediate
      ```
      {: codeblock}

   2. Utilice el mandato `kubectl` para crear el objeto storageClass en microk8s:

      ```
      kubectl apply -f storageClass.yml
      ```
      {: codeblock}

### Instalación de un agente en microk8s

Siga estos pasos para instalar un agente en microk8s.

1. Complete los [pasos 1 -3](#install_kube).

2. Ejecute el mandato `agent-install.sh` para instalar y configurar el agente de Horizon y registre el clúster periférico para ejecutar el servicio periférico de ejemplo helloworld:

   ```
   source agent-install.sh -u $HZN_EXCHANGE_USER_AUTH -k agent-install.cfg  -D cluster -p "IBM/pattern-ibm.helloworld"
   ```
   {: codeblock}

   Nota: Durante la instalación de agente, es posible que vea esta solicitud: **¿Desea sobrescribir horizon?[y/N]:**. Seleccione **y** y pulse **Intro**; `agent-install.sh` establece la configuración correctamente.

## Eliminar el agente del clúster ligero de Kubernetes 

Nota: Dado que el script de desinstalación de agente no está completo en este release, la eliminación de agente se realiza suprimiendo el espacio de nombres openhorizon-agent.

1. Suprima el espacio de nombres

   ```
   kubectl delete namespace openhorizon-agent
   ```
   {: codeblock}

      Nota: en ocasiones, la eliminación del espacio de nombres se detiene en el estado "Terminando". En esta situación, consulte [Un espacio de nombres se ha atascado en el estado Terminando ![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para suprimir el espacio de nombres manualmente.

2. Suprima clusterrolebinding: 

   ```
   kubectl delete clusterrolebinding openhorizon-agent-cluster-rule
   ```
   {: codeblock}

<!--If this installation was done as part of a prerequisite for {{site.data.keyword.edge_devices_notm}}, [return to continue that installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html).-->
