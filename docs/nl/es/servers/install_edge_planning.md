---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparación de la instalación de {{site.data.keyword.edge_servers_notm}}
{: #edge_planning}

Antes de instalar {{site.data.keyword.icp_server}}, habilite {{site.data.keyword.mgmt_hub}} y configure {{site.data.keyword.edge_servers_notm}} y asegúrese de que el sistema cumple los requisitos siguientes. Estos requisitos identifican los componentes y las configuraciones mínimos necesarios de los servidores periféricos planificados.
{:shortdesc}

Estos requisitos también identifican los valores de configuración mínimos para el clúster de {{site.data.keyword.mgmt_hub}} que va a utilizar para gestionar los servidores periféricos.

Utilice esta información como ayuda para planificar los requisitos de recursos para la topología de Edge Computing y la configuración global de {{site.data.keyword.icp_server}} y {{site.data.keyword.mgmt_hub}} .

   * [Requisitos de hardware](#prereq_hard)
   * [IaaS soportado](#prereq_iaas)
   * [Entornos soportados](#prereq_env)
   * [Puertos necesarios](#prereq_ports)
   * [Consideraciones acerca del dimensionamiento del clúster](#cluster)

## Requisitos de hardware
{: #prereq_hard}

Cuando esté dimensionando el nodo de gestión para la topología de Edge Computing, utilice las directrices de dimensionamiento de {{site.data.keyword.icp_server}} para un despliegue de un solo nodo o de varios nodos para ayudarle a dimensionar el clúster. Para obtener más información, consulte [Dimensionamiento del clúster de {{site.data.keyword.icp_server}} ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Los requisitos del servidor periférico siguiente solo se aplican a las instancias de {{site.data.keyword.icp_server}} que están desplegadas en centros de operaciones remotas mediante el {{site.data.keyword.edge_profile}}.

| Requisito | Nodos (arranque, maestro, gestión) | Nodos de trabajador |
|-----------------|-----------------------------|--------------|
| Número de hosts | 1 | 1 |
| Núcleos | 4 o más | 4 o más |
| CPU | >= 2,4 GHz | >= 2,4 GHz |
| RAM | 8 GB o más | 8 GB o más |
| Espacio libre de disco para la instalación | 150 GB o más | |
{: caption="Tabla 1. Requisitos mínimos de hardware de clúster de servidor periférico." caption-side="top"}

Nota: 150 GB de almacenamiento permiten un máximo de tres días de retención de datos de registro y de sucesos
si hay desconexión de red con el centro de datos central.

## IaaS soportado
{: #prereq_iaas}

En la tala siguiente se identifica la Infrastructure as a Service (IaaS) que puede utilizar para los servicios periféricos.

| IaaS | Versiones |
|------|---------|
|Nutanix NX-3000 Series para el uso en ubicaciones de servidor periférico | NX-3155G-G6 |
|IBM Hyperconverged Systems basados en Nutanix para el uso en servidores periféricos | CS821 y CS822|
{: caption="Tabla 2. IaaS soportados para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Para obtener más información, consulte [IBM Hyperconverged Systems powered by Nutanix PDF ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Entornos soportados
{: #prereq_env}

En las tablas siguiente se identifican los sistemas configurados Nutanix adicionales que puede utilizar con los servidores periféricos.

| Tipo de sitio LOE | Tipo de nodo | Tamaño del clúster | Núcleos por nodo (total) | Procesadores lógicos por nodo (total)	| Memoria (GB) por nodo (total) | Tamaño de disco de memoria caché por grupo de disco (GB) |	Cantidad de disco de memoria caché por nodo	| Tamaño de disco de memoria caché por nodo (GB)	| Tamaño total de agrupación de clúster de almacenamiento (toda la memoria flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Pequeño	| NX-3155G-G6	| 3 nodos	| 24 (72)	| 48 (144)	| 256 (768)	| N/D	| N/D	| N/D	| 8 TB |
| Medio | NX-3155G-G6 | 3 nodos | 24 (72)	| 48 (144)	| 512 (1.536)	| N/D	| N/D	| N/D	| 45 TB |
| Grande	| NX-3155G-G6	| 4 nodes	| 24 (96)	| 48 (192)	| 512 (2.048)	| N/D	| N/D	| N/D	| 60 TB |
{: caption="Tabla 3. Configuraciones soportadas de Nutanix NX-3000 Series" caption-side="top"}

| Tipo de sitio LOE	| Tipo de nodo	| Tamaño del clúster |	Núcleos por nodo (total) | Procesadores lógicos por nodo (total)	| Memoria (GB) por nodo (total)	| Tamaño de disco de memoria caché por grupo de disco (GB) | Cantidad de disco de memoria caché por nodo	| Tamaño de disco de memoria caché por nodo (GB)	| Tamaño total de agrupación de clúster de almacenamiento (toda la memoria flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Pequeño	| CS821 (2 sockets, 1U) | 3 nodos | 20 (60)	| 80 (240) | 256 (768) | N/D	| N/D	| N/D	| 8 TB |
| Medio | CS822 (2 sockets, 2U) | 3 nodos	| 22 (66)	| 88 (264) | 512 (1.536) | N/D | N/D | N/D | 45 TB |
| Grande	| CS822 (2 sockets, 2U) | 4 nodos | 22 (88) | 88 (352) | 512 (2.048) | N/D | N/D | N/D | 60 TB |
{: caption="Tabla 4. IBM Hyperconverged Systems basados en Nutanix" caption-side="top"}

Para obtener más información, consulte [IBM Hyperconverged Systems that are powered by Nutanix ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Puertos necesarios
{: #prereq_ports}

Si tiene previsto desplegar un servidor periférico remoto con una configuración de clúster estándar, los requisitos de puerto para los nodos son los mismos que los requisitos de puerto para el despliegue de {{site.data.keyword.icp_server}}. Para obtener más información acerca de estos requisitos, consulte [Puertos necesarios ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html). Para los puertos necesarios para el clúster de hub, consulte la sección _Puertos necesarios para {{site.data.keyword.mcm_core_notm}}_.

Si tiene previsto configurar los servidores periféricos mediante el {{site.data.keyword.edge_profile}}, habilite los puertos siguientes:

| Puerto | Protocolo | Requisitos |
|------|----------|-------------|
| NA | IPv4 | Calico con IP-in-IP (calico_ipip_mode: Always) |
| 179 | TCP	| Always for Calico (network_type:calico) |
| 500 | TCP y UDP	| IPSec (ipsec.enabled: true, calico_ipip_mode: Always) |
| 2380 | TCP | Always if etcd is enabled |
| 4001 | TCP | Always if etcd is enabled |
| 4500 | UDP | IPSec (ipsec.enabled: true) |
| 9091 | TCP | Calico (network_type:calico) |
| 9099 | TCP | Calico (network_type:calico) |
| 10248:10252 | TCP	| Always for Kubernetes |
| 30000:32767 | TCP y UDP | Always for Kubernetes |
{: caption="Tabla 5. Puertos necesarios para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Nota: Los puertos 30000:32767 tienen acceso externo. Estos puertos solo deben abrirse si establece el tipo de servicio Kubernetes en NodePort.

## Consideraciones acerca del dimensionamiento del clúster
{: #cluster}

Para {{site.data.keyword.edge_servers_notm}}, el clúster de hub suele ser un entorno alojado en {{site.data.keyword.icp_server}} estándar. Puede utilizar este entorno para alojar también otras cargas de trabajo de cálculo que necesite, o desee, que se sirvan desde una ubicación central. El entorno de clúster de hub debe dimensionarse de forma que tenga recursos suficientes para alojar el clúster de {{site.data.keyword.mcm_core_notm}} y cualquier carga de trabajo adicional que tenga previsto alojar en el entorno. Para obtener más información acerca del dimensionamiento de un entorno alojado en {{site.data.keyword.icp_server}} estándar, consulte [Dimensionamiento del clúster de {{site.data.keyword.icp_server}} ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Si es necesario, puede operar un servidor periférico remoto dentro de un entorno de recursos restringidos. Si necesita operar un servidor periférico dentro de un entorno de recursos restringidos, tenga en cuenta la posibilidad de utilizar el {{site.data.keyword.edge_profile}}. Este perfil solo configura los componentes mínimos que son necesarios para un entorno de servidor periférico. Si utiliza este perfil, debe seguir asignando recursos suficientes para el conjunto de componentes necesarios para una arquitectura de {{site.data.keyword.edge_servers_notm}} y para proporcionar los recursos que son necesarios para cualesquiera otras carga de trabajo de aplicaciones alojadas en los entornos de servidor periférico. Para obtener más información sobre la arquitectura de {{site.data.keyword.edge_servers_notm}}, consulte [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch).

Mientras que las configuraciones del {{site.data.keyword.edge_profile}} pueden ahorrar memoria y recursos de almacenamiento, las configuraciones dan como resultado un bajo nivel de resistencia. Un servidor periférico basado en este perfil puede funcionar desconectado del centro de datos en el que está ubicado el clúster de hub. Este funcionamiento en desconexión puede durar normalmente hasta tres días. Si el servidor periférico falla, el servidor deja de proporcionar soporte operativo para el centro de operaciones remoto.

Las configuraciones de {{site.data.keyword.edge_profile}} también están limitadas a soportar solo la tecnología y los procesos siguientes:
  * Plataformas {{site.data.keyword.linux_notm}} de 64 bits
  * Topología de despliegue no de alta disponibilidad (HA)
  * Adición y eliminación de nodos de trabajador como operaciones de 2 días
  * Acceso al clúster y control del mismo por interfaz de línea de mandatos
  * Redes Calico

Si necesita más resistencia o si alguna de las limitaciones anteriores es demasiado restrictiva, en su lugar puede seleccionar la utilización de uno de los otros perfiles de configuración de despliegue estándar para {{site.data.keyword.icp_server}} que proporcionan un mayor soporte de migración tras error.

### Despliegues de ejemplo

* Entorno de servidor periférico basado en el {{site.data.keyword.edge_profile}} (resistencia baja)

| Tipo de nodo | Número de nodos | CPU | Memoria (GB) | Disco (GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
| Arranque       | 1           | 1   | 2           | 8   |
| Maestro     | 1           | 2   | 4           | 16  |
| Gestión | 1           | 1   | 2           | 8   |
| Trabajador     | 1           | 4   | 8           | 32  |
{: caption="Tabla 6. Valores de perfil periférico para un entorno de servidor periférico de resistencia baja" caption-side="top"}

* Entornos de servidor periférico basados en otros perfiles de {{site.data.keyword.icp_server}} (soporte de resistencia medio a alto)

  Utilice los requisitos de despliegue de ejemplo pequeños, medianos y grandes cuando necesite utilizar una configuración que no sea el {{site.data.keyword.edge_profile}} para el entorno del servidor periférico. Para obtener más información, consulte [Dimensionamiento de los despliegues de ejemplo de clúster de {{site.data.keyword.icp_server}} ![Se abre en otro separador](../images/icons/launch-glyph.svg "Se abre en otro separador")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples).
