---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# Requisitos de sistema y dimensionamiento
{: #size}

## Consideraciones sobre el dimensionamiento

El dimensionamiento del clúster incluye muchas consideraciones. Este contenido describe algunas de estas consideraciones y proporciona la mejor guía posible para ayudarle a dimensionar el clúster.

La consideración principal consiste en determinar qué servicios deben ejecutarse en el clúster. Este contenido sólo proporciona orientación para el dimensionamiento de los siguientes servicios:

* {{site.data.keyword.common_services}}
* Centro de gestión de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}})

De forma opcional, puede instalar el [registro de clúster de {{site.data.keyword.open_shift_cp}}](../admin/accessing_logs.md#ocp_logging).

## Consideraciones sobre la base de datos de {{site.data.keyword.ieam}}

Dos configuraciones de base de datos soportadas afectan a las consideraciones de dimensionamiento del centro de gestión de {{site.data.keyword.ieam}}:

* Las bases de datos **locales** se instalan (de forma predeterminada) como recursos de {{site.data.keyword.open_shift}} en el clúster de {{site.data.keyword.open_shift}}.
* Las bases de datos **remotas** son bases de datos que el usuario ha suministrado, que pueden ser ofertas SaaS de proveedor de nube, locales, etc.

### Requisitos de almacenamiento local de {{site.data.keyword.ieam}}

Además del componente SDO (Secure Device Onboarding) siempre instalado, el gestor de bases de datos y secretos **local** requiere almacenamiento persistente. Este almacenamiento utiliza clases de almacenamiento dinámico que están configuradas para el clúster {{site.data.keyword.open_shift}}

Para obtener más información, consulte [Instrucciones de configuración y opciones de almacenamiento de {{site.data.keyword.open_shift}} dinámico soportadas](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html).

Es responsable de habilitar el cifrado en reposo en el momento de la creación del clúster. A menudo se puede incluir como parte de la creación de clústeres en las plataformas en la nube. Para obtener más información, consulte la [siguiente documentación](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html).

Un punto principal a tener en cuenta para el tipo de clase de almacenamiento que se elige es determinar si esa clase de almacenamiento soporta **allowVolumeExpansion**. En caso afirmativo, lo siguiente devuelve **true**:

```
oc get storageclass <clase de almacenamiento deseado> -o json | jq .allowVolumeExpansion
```
{: codeblock}

Si la clase de almacenamiento permite la expansión de volumen, el dimensionamiento puede ajustarse después de la instalación (dado que el espacio de almacenamiento subyacente está disponible para la asignación). Si la clase de almacenamiento no permite la expansión de volumen, debe preasignar almacenamiento para el caso de uso. 

Si es necesario más almacenamiento después de la instalación inicial con una clase de almacenamiento que no permite la expansión de volumen, deberá ejecutar una reinstalación siguiendo los pasos que se describen en la página de [ copia de seguridad y recuperación ](../admin/backup_recovery.md).

Las asignaciones se pueden cambiar antes de la instalación del centro de gestión de {{site.data.keyword.ieam}} modificando los valores de **Almacenamiento** como se describe en la página de [configuración](configuration.md). Las asignaciones se establecen en los siguientes valores predeterminados:

* PostgreSQL Exchange (almacena datos para Exchange y fluctúa de tamaño en función del uso, pero el valor de almacenamiento predeterminado puede soportar hasta el límite anunciado de nodos periféricos)
  * 20 GB
* PostgreSQL AgBot (almacena datos para el AgBot, el valor de almacenamiento predeterminado puede soportar hasta el límite anunciado de nodos periféricos)
  * 20 GB
* MongoDB Cloud Sync Service (almacena contenido para el servicio de gestión de modelos (MMS)). En función del número y el tamaño de los modelos, es posible que desee modificar esta asignación predeterminada.
  * 50 GB
* Volumen persistente de Hashicorp Vault (almacena los secretos utilizados por servicios de dispositivos periféricos)
  * 10 GB (este tamaño de volumen no es configurable)
* Volumen persistente de incorporación de dispositivo seguro (almacena cupones de propiedad de dispositivo, opciones de configuración de dispositivo y el estado de despliegue de cada dispositivo)
  * 1 GB (este tamaño de volumen no es configurable)

* **Notas:**
  * Los volúmenes de {{site.data.keyword.ieam}} se crean con la modalidad de acceso **ReadWriteOnce**.
  * IBM Cloud Platform Common Services tiene requisitos de almacenamiento adicionales para sus servicios. Se crean los siguientes volúmenes en el espacio de nombres **ibm-common-services** al instalar con los valores predeterminados de {{site.data.keyword.ieam}}:
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE     alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h     prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    Puede obtener más información sobre los requisitos de almacenamiento y las opciones de configuración de IBM Cloud Platform Common Services [aquí](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html).

### Consideraciones acerca de las bases de datos remotas de {{site.data.keyword.ieam}}

La utilización de sus propias bases de datos **remotas** reduce la clase de almacenamiento y los requisitos de cálculo para esta instalación, a menos que se suministren en el mismo clúster.

Como mínimo, suministre bases de datos **remotas** con los siguientes recursos y valores:

* 2vCPU
* 2 GB de RAM
* Los tamaños de almacenamiento predeterminados mencionados en la sección anterior
* Para las bases de datos PostgreSQL, 100 **max_connections** (que suele ser el valor predeterminado)

## Tamaño de nodo de trabajador

Los servicios que utilizan recursos de cálculo de [Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) se planifican en los nodos de trabajador disponibles.

### Requisitos mínimos para la configuración de {{site.data.keyword.ieam}} predeterminada
| Número de nodos de trabajador | vCPU por nodo de trabajador | Memoria por nodo de trabajador (GB) | Almacenamiento de disco local por nodo de trabajador (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**Nota:** algunos entornos de cliente podrían necesitar vCPU adicionales por nodo trabajador o nodos de trabajador adicionales, por lo que se puede asignar más capacidad de CPU al componente de Exchange.


&nbsp;
&nbsp;

Después de determinar el dimensionamiento adecuado para el clúster, puede empezar la [instalación](online_installation.md).
