---

copyright:
  years: 2020
lastupdated: "2020-02-1"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Requisitos de sistema y dimensionamiento

Antes de instalar {{site.data.keyword.edge_servers_notm}} revise los requisitos del sistema de cada uno de los productos y el dimensionamiento de la ocupación.
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [Dimensionamiento para punto final de varios clústeres](#mc_endpoint)
  - [Dimensionamiento para los servicios del centro de gestión](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [Documentación de instalación de {{site.data.keyword.ocp_tm}} ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* Nodos de cálculo o trabajador de {{site.data.keyword.open_shift_cp}}: 16 núcleos | 32 GB RAM

  Nota: si desea instalar
{{site.data.keyword.edge_devices_notm}} además de {{site.data.keyword.edge_servers_notm}},
necesitará añadir recursos de nodo adicionales como se describe en la
[sección
de dimensionamiento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).
  
* Requisitos de almacenamiento:
  - Para la instalación fuera de línea, el registro de imágenes de {{site.data.keyword.open_shift_cp}} necesita 100 GB como mínimo.
  - Los servicios de gestión MongoDB y registro necesitan cada uno 20 GB a través de la clase de almacenamiento.
  - Si está habilitado, el asesor de vulnerabilidades necesita 60 GB a través de la clase de almacenamiento.

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

El dimensionamiento está disponible para ocupaciones mínimas y de producción.

### Topología de despliegue para {{site.data.keyword.open_shift}} y {{site.data.keyword.edge_servers_notm}}

| Topología de despliegue | Descripción de uso | Configuración de nodos de {{site.data.keyword.open_shift}} 4.2 |
| :--- | :--- | :--- | :---|
| Mínima | Despliegue de clúster pequeño | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 nodos maestros <br> &nbsp; 2 o más nodos de trabajador </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 nodo de trabajador dedicado </p> |
| Producción | Soporta la configuración predeterminada <br> de {{site.data.keyword.edge_servers_notm}}| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 nodos maestros (HA nativa) <br>&nbsp; 4 o más nodos de trabajador </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 nodos de trabajador dedicados|
{: caption="Tabla 1. Configuraciones de topología de despliegue para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Nota: para los nodos de trabajador de {{site.data.keyword.edge_servers_notm}} dedicados,
establezca los nodos maestro, de gestión y proxy en un nodo de trabajador
de {{site.data.keyword.open_shift}}, que se ha configurado en
[Documentación de instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)
de {{site.data.keyword.edge_servers_notm}}.

Nota: todos los volúmenes persistentes indicados a continuación son predeterminados. Debe cambiar el tamaño de los volúmenes según la cantidad de datos que se almacenan a lo largo del tiempo.

### Dimensionamiento mínimo
| Configuración | Número de nodos | vCPU | Memoria | Volúmenes persistentes (GB) | Espacio de disco (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| maestro, gestión, proxy	| 1| 16	| 32	| 20  | 100  |
{: caption="Tabla 2. Dimensionamiento de nodos de {{site.data.keyword.open_shift}} mínimo para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

### Dimensionamiento de producción

| Configuración | Número de nodos | vCPU | Memoria | Volúmenes persistentes (GB) | Espacio de disco (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| maestro, gestión, proxy	| 3| 48	| 96	| 60  | 300  |
{: caption="Tabla 3. Dimensionamiento de nodos de {{site.data.keyword.open_shift}} de producción para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

## Dimensionamiento para punto final de varios clústeres
{: #mc_endpoint}

| Nombre de componente                 	| Opcional 	| Solicit. CPU 	| Límite CPU  	| Solicit. memoria  	| Límite memoria 	|
|--------------------------------	|----------	|-------------	|------------	|-----------------	|--------------	|
| ApplicationManager             	| True     	| 100 mCore   	| 500mCore   	| 128 MiB         	| 2 GiB        	|
| WorkManager                    	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB       |
| ConnectionManager              	| False    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| ComponentOperator              	| False    	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| CertManager                    	| False    	| 100 mCore   	| 300 mCore  	| 100 MiB         	| 300 MiB      	|
| PolicyController               	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| SearchCollector                	| True     	| 25 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| ServiceRegistry                	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 258 MiB      	|
| ServiceRegistryDNS             	| True     	| 100 mCore   	| 500 mCore  	| 70 MiB          	| 170 MiB      	|
| MeteringSender                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringReader                 	| True     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringDataManager            	| True     	| 100 mCore   	| 1000 mCore 	| 256 MiB         	| 2560 MiB     	|
| MeteringMongoDB                	| True     	| -           	| -          	| 500 MiB           | 1 GiB        	|
| Tiller                         	| True     	| -           	| -          	| -               	| -            	|
| TopologyWeaveScope(1 per node) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="Tabla 4. Instrucciones para punto final de varios clústeres" caption-side="top"}

## Dimensionamiento para servicios de centro de gestión
{: #management_services}

| Nombre de servicio                 | Opcional | Solicitud de CPU | Límite de CPU | Solicitud de memoria | Límite de memoria | Volumen persistente (valor predeterminado) | Consideraciones adicionales |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui, Common-web-ui, iam-policy-controller, key-management, mcm-kui, metering, monitoring, multicluster-hub,nginx-ingress, search | Valor predeterminado | 9.025 m | 29.289 m | 16.857 Mi | 56.963 Mi | 20 GiB | |
| Registro de auditoría | Opcional | 125 m | 500 m | 250 Mi | 700 Mi | | |
| Controlador de política de CIS | Opcional | 525 m | 1.450 m | 832 Mi | 2.560 Mi | | |
| Imposición de seguridad de imagen | Opcional | 128 m | 256 m | 128 Mi | 256 Mi | | |
| Licencias | Opcional | 200 m | 500 m | 256 Mi | 512 Mi | | |
| Registro | Opcional | 1.500 m | 3.000 m | 9.940 Mi | 10.516 Mi | 20 GiB | |
| Imposición de cuota de cuenta de multiarrendatario | Opcional | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Asesor de mutaciones | Opcional | 1.000 m | 3.300 m | 2.052 Mi | 7.084 Mi | 100 GiB | |
| Notario | Opcional | 600 m | 600 m  | 1.024 Mi | 1.024 Mi | | |
| Controlador de política de cifrado secreto | Opcional | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| Secure Token Service (STS) | Opcional | 410 m | 600 m  | 94 Mi  | 314 Mi | | Necesita malla de servicios de Red Hat OpenShift (Istio) |
| Servicio de comprobación de estado del sistema | Opcional | 75 m | 600 m | 96 Mi | 256 Mi | | |
| Asesor de vulnerabilidades (VA) | Opcional | 1.940 m | 4.440 m | 8.040 Mi | 27.776 Mi | 10 GiB | Necesita registro de Red Hat OpenShift (Elasticsearch) |
{: caption="Tabla 5. Dimensionamiento de servicios de centro" caption-side="top"}

## Qué hacer a continuación

Vuelva a la [documentación de instalación](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) de {{site.data.keyword.edge_servers_notm}}.
