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



# Desinstalar
{: #uninstalling_hub}

**Aviso:** si se suprime el recurso personalizado **EamHub**, se empezarán a eliminar inmediatamente los recursos de los que depende el centro de gestión de {{site.data.keyword.ieam}}, incluidos los componentes de IBM Cloud Platform Common Services. Asegúrese de que ésa es su intención antes de continuar.

Consulte la página [copia de seguridad y recuperación](../admin/backup_recovery.md) si esta desinstalación se está realizando para facilitar una restauración a un estado anterior.

* Inicie sesión en el clúster como administrador de clúster con **cloudctl** o **oc login**, en el espacio de nombres donde está instalado el operador de {{site.data.keyword.ieam}}.
* Ejecute lo siguiente para suprimir el recurso personalizado (valor predeterminado **ibm-edge**):
  ```
  oc delete eamhub ibm-edge
  ```
  {: codeblock}
* Asegúrese de que todos los pods del centro de gestión de {{site.data.keyword.ieam}} hayan terminado y que solo los dos pods de operador que se muestran aquí estén en ejecución antes de continuar con el paso siguiente:
  ```
  $ oc get pods   NAME                                           READY   STATUS    RESTARTS   AGE   ibm-common-service-operator-794f868789-gdt2z   1/1     Running   0          20h   ibm-eamhub-operator-7455c95496-nf48z           1/1     Running   0          20h
  ```
* Desinstale el operador del centro de gestión de {{site.data.keyword.ieam}} utilizando la consola del clúster de OpenShift. Seleccione el espacio de nombres donde está instalado el operador de {{site.data.keyword.ieam}} y vaya a **Operadores** > **Operadores instalados** > el icono del menú de desbordamiento de **Centro de gestión de IEAM** > **Desinstalar operador**.
* Siga las instrucciones de **Desinstalación de todos los servicios** en la página [Desinstalación](https://www.ibm.com/docs/en/cpfs?topic=online-uninstalling-foundational-services) de IBM Cloud Platform Common Services, sustituyendo las apariciones del espacio de nombres **common-service** por el espacio de nombres donde está instalado el operador de {{site.data.keyword.ieam}}.
