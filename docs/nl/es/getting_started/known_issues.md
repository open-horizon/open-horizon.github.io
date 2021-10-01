---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Limitaciones y problemas conocidos  
{: #knownissues}

A continuación, se recogen los problemas conocidos y limitaciones de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

Para obtener la lista completa de problemas abiertos para la capa de código abierto de {{site.data.keyword.ieam}}, revise los problemas de GitHub en cada uno de los [repositorios de Open Horizon](https://github.com/open-horizon/).

{:shortdesc}

## Problemas conocidos de {{site.data.keyword.ieam}} {{site.data.keyword.version}}

Estos son los problemas conocidos y las limitaciones de {{site.data.keyword.ieam}} {{site.data.keyword.version}}.

* {{site.data.keyword.ieam}} no realiza exploraciones en busca de virus o programas maliciosos en los datos que se cargan en el sistema de gestión de modelos (MMS). Para obtener más información sobre la seguridad de MMS, consulte [Seguridad y privacidad](../OH/docs/user_management/security_privacy.md#malware).

* El distintivo **-f &lt;directory&gt;** de **edgeNodeFiles.sh** no tiene el efecto deseado. En su lugar, los archivos se recopilan en el directorio actual. Para más información, consulte el [problema 2187](https://github.com/open-horizon/anax/issues/2187). La solución alternativa es ejecutar el mandato de la siguiente forma:

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* Como parte de la instalación de {{site.data.keyword.ieam}}, en función de la versión de {{site.data.keyword.common_services}} instalada, es posible que se hayan creado certificados cuya vida útil sea corta, lo que conduciría a su renovación automática. Es posible que surjan los siguientes problemas de certificado ([que se pueden resolver siguiendo estos pasos](cert_refresh.md)):
  * Se ha visualizado una salida JSON inesperada con un mensaje "Request failed with status code 502" al acceder a la consola de gestión de {{site.data.keyword.ieam}}.
  * Los nodos periféricos no se actualizan cuando se renueva un certificado y se deben actualizar manualmente para garantizar una correcta comunicación con {{site.data.keyword.ieam}} Hub.

* Cuando se utiliza {{site.data.keyword.ieam}} con bases de datos locales, si el pod **cssdb** se suprime y se vuelve a crear, ya sea manual o automáticamente mediante el planificador de Kubernetes, se perderán los datos de la base de datos Mongo. Siga la documentación de [copia de seguridad y recuperación](../admin/backup_recovery.md) para poder mitigar la pérdida de datos.

* Cuando se utiliza {{site.data.keyword.ieam}} con bases de datos locales, si se suprimen los recursos de trabajo **create-agbotdb-cluster** o **create-exchangedb-cluster**, el trabajo se volverá a ejecutar y reiniciará la base de datos correspondiente, lo que ocasionará la pérdida de los datos. Siga la documentación de [copia de seguridad y recuperación](../admin/backup_recovery.md) para poder mitigar la pérdida de datos.

* Cuando se utilizan bases de datos locales, puede que una o varias de las bases de datos postgres no respondan. Para resolver este problema, reinicie todos los centinelas y proxies de la base de datos que no responde. Modifique y ejecute los siguientes mandatos con la aplicación afectada y el Recurso personalizado (CR) `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` y `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` (ejemplo de centinela exchange: `oc rollout restart deploy ibm-edge-exchangedb-sentinel`).

* Si ejecuta **hzn service log** en {{site.data.keyword.rhel}} con cualquier arquitectura, el mandato se cuelga. Para más información, consulte el [problema 2826](https://github.com/open-horizon/anax/issues/2826). Para solucionar temporalmente esta condición, obtenga los registros de contenedor (también puede especificar -f para la cola):

   ```
   docker logs &amp;TWBLT;container&gt;
   ```
   {: codeblock}


## Limitaciones de {{site.data.keyword.ieam}}{{site.data.keyword.version}}

* La documentación del producto de {{site.data.keyword.ieam}} se traduce para los geografías participantes, pero la versión en inglés se actualiza continuamente. Las discrepancias entre el inglés y las versiones traducidas pueden aparecer entre los ciclos de traducción. Compruebe la versión en inglés para ver si alguna discrepancia se resolvió después de publicar las versiones traducidas.

* Si modifica los atributos **owner** o **public** de servicios, patrones o políticas de despliegue en Exchange, puede tardar hasta cinco minutos en acceder a estos recursos para ver el cambio. De forma similar, cuando se proporciona un privilegio de administrador de usuario de Exchange, dicho cambio puede tardar hasta cinco minutos en propagarse a todas las instancias de Exchange. La cantidad de tiempo se puede reducir estableciendo `api.cache.resourcesTtlSeconds` en un valor inferior (el valor predeterminado es 300 segundos) en el archivo `config.json` de Exchange, a costa de reducir ligeramente el rendimiento.

* El agente no da soporte al [Sistema de gestión de modelos](../developing/model_management_system.md) (MMS) para los servicios dependientes.

* El enlace secreto no funciona para un servicio sin acuerdo definido en un patrón.
 
* El agente de clúster periférico no da soporte a K3S v1.21.3+k3s1 porque el directorio de volumen montado solo tiene el permiso 0700. Consulte [No se pueden escribir datos en PVC local](https://github.com/k3s-io/k3s/issues/3704) para obtener una solución temporal.
 
* Cada agente de nodo periférico de {{site.data.keyword.ieam}} inicia todas las conexiones de red con el centro de gestión de {{site.data.keyword.ieam}} . El centro de gestión nunca inicia conexiones a sus nodos periféricos. Por lo tanto, un nodo periférico puede estar detrás de un cortafuegos NAT si el cortafuegos tiene conectividad TCP con el centro de gestión. Sin embargo, los nodos periféricos no pueden comunicarse actualmente con el centro de gestión mediante un proxy SOCKS.
  
* La instalación de dispositivos periféricos con Fedora o SuSE sólo la soporta el método [Instalación y registro manuales avanzados del agente](../installing/advanced_man_install.md).
