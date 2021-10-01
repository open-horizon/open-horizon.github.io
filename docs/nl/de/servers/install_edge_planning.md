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

# Installation von {{site.data.keyword.edge_servers_notm}} vorbereiten
{: #edge_planning}

Vor der Installation von {{site.data.keyword.icp_server}} aktivieren Sie den {{site.data.keyword.mgmt_hub}} und konfigurieren Sie {{site.data.keyword.edge_servers_notm}}. Stellen Sie sicher, dass Ihr System die folgenden Anforderungen erfüllt. Diese Anforderungen definieren die mindestens erforderlichen Komponenten und Konfigurationen Ihrer geplanten Edge-Server.
{:shortdesc}

Diese Anforderungen geben außerdem die Einstellungen für die Mindestkonfiguration des {{site.data.keyword.mgmt_hub}}-Clusters an, den Sie zur Verwaltung Ihrer Edge-Server einsetzen wollen.

Verwenden Sie diese Informationen, um die Planung des Ressourcenbedarfs für Ihre Edge-Computing-Topologie und insgesamt für Ihre {{site.data.keyword.icp_server}}- und {{site.data.keyword.mgmt_hub}}-Installation zu erleichtern.

   * [Hardwarevoraussetzungen](#prereq_hard)
   * [Unterstützte IaaS](#prereq_iaas)
   * [Unterstützte Umgebungen](#prereq_env)
   * [Erforderliche Ports](#prereq_ports)
   * [Hinweise zur Clusterdimensionierung](#cluster)

## Hardwarevoraussetzungen
{: #prereq_hard}

Wenn Sie die Größe Ihres Managementknotens für die Edge-Computing-Topologie definieren, dann orientieren Sie sich an den Richtlinien zur Dimensionierung von {{site.data.keyword.icp_server}} für eine Einzel- oder Mehrknotenbereitstellung, um die Dimensionierung Ihres Clusters zu vereinfachen. Weitere Informationen finden Sie unter [Dimensionierung Ihres {{site.data.keyword.icp_server}}-Clusters ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Die folgenden Edge-Server-Anforderungen gelten nur für {{site.data.keyword.icp_server}}-Instanzen, die in fernen Betriebszentren mit dem {{site.data.keyword.edge_profile}} bereitgestellt werden.

| Anforderung | Knoten (Boot, Master, Management) |Workerknoten|
|-----------------|-----------------------------|--------------|
| Anzahl der Hosts | 1 | 1 |
|Cores (Kerne) | 4 oder mehr | 4 oder mehr |
| CPU | >= 2,4 GHz | >= 2,4 GHz |
| Arbeitsspeicher (RAM) | 8 GB oder mehr | 8 GB oder mehr |
| Freier Plattenspeicherplatz für Installation | 150 GB oder mehr | |
{: caption="Tabelle 1. Mindestanforderungen für Cluster-Hardware des Edge-Servers." caption-side="top"}

Hinweis: 150 GB Speicherplatz ermöglicht die Aufbewahrung des Volumens an Protokoll- und Ereignisdaten für drei Tage, wenn keine Netzverbindung zum zentralen Rechenzentrum besteht.

## Unterstützte IaaS
{: #prereq_iaas}

In der folgenden Tabelle werden die unterstützten IaaS-Komponenten (IaaS = Infrastructure as a Service) angegeben, die Sie für Ihre Edge-Services verwenden können.

| IaaS | Versionen |
|------|---------|
|Nutanix NX-3000 Series zur Verwendung an Edge-Server-Standorten | NX-3155G-G6 |
|IBM Hyperconverged Systems powered by Nutanix zur Verwendung in Edge-Servern | CS821 und CS822|
{: caption="Tabelle 2. Unterstützte IaaS für {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Weitere Informationen finden Sie unter [IBM Hyperconverged Systems powered by Nutanix PDF ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/downloads/cas/BZP46MAV). 

## Unterstützte Umgebungen
{: #prereq_env}

In den folgenden Tabellen sind die zusätzlich konfigurierten Nutanix-Systeme angegeben, die Sie für Ihre Edge-Server verwenden können.

| Typ der LOE-Site     | Knotentyp | Clustergröße | Cores pro Knoten (gesamt) | Logische Prozessoren pro Knoten (gesamt) | Speicherplatz (GB) pro Knoten (gesamt) | Größe des Cachedatenträgers pro Plattengruppe (GB) |	Anzahl der Cachedatenträger pro Knoten | Größe der Cachedatenträger pro Knoten (GB)	| Gesamtspeichergröße des Cluster-Pools (nur Flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Klein	| NX-3155G-G6	| 3 Knoten | 24 (72)	| 48 (144)	| 256 (768)	| Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 8 TB |
| Mittel | NX-3155G-G6 | 3 Knoten | 24 (72)	| 48 (144)	| 512 (1.536)	| Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 45 TB |
| Groß 	| NX-3155G-G6	| 4 Knoten | 24 (96)	| 48 (192)	| 512 (2.048)	| Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 60 TB |
{: caption="Tabelle 3. Nutanix NX-3000 Series - Unterstützte Konfigurationen" caption-side="top"}

| Typ der LOE-Site | Knotentyp | Clustergröße |	Cores pro Knoten (gesamt) | Logische Prozessoren pro Knoten (gesamt) | Speicherplatz (GB) pro Knoten (gesamt) | Größe des Cachedatenträgers pro Plattengruppe (GB) | Anzahl der Cachedatenträger pro Knoten | Größe der Cachedatenträger pro Knoten (GB)	| Gesamtspeichergröße des Cluster-Pools (nur Flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Klein	| CS821 (2 Sockets, 1U) | 3 Knoten | 20 (60)	| 80 (240) | 256 (768) | Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 8 TB |
| Mittel | CS822 (2 Sockets, 2U) | 3 Knoten | 22 (66)	| 88 (264) | 512 (1.536)	| Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 45 TB |
| Groß 	| CS822 (2 Sockets, 2U) | 4 Knoten | 22 (88) | 88 (352) | 512 (2.048)	| Nicht zutreffend | Nicht zutreffend | Nicht zutreffend | 60 TB |
{: caption="Tabelle 4. IBM Hyperconverged Systems powered by Nutanix" caption-side="top"}

Weitere Informationen finden Sie unter [IBM Hyperconverged Systems powered by Nutanix ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Erforderliche Ports
{: #prereq_ports}

Wenn Sie die Bereitstellung eines fernen Edge-Servers mit einer Standardclusterkonfiguration planen, dann sind die Portanforderungen für die Knoten identisch mit den Portanforderungen zur Bereitstellung von {{site.data.keyword.icp_server}}. Weitere Einzelheiten zu diesen Voraussetzungen finden Sie unter [Erforderliche Ports ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html). Informationen zu den erforderlichen Ports für den Hub-Cluster finden Sie im Abschnitt _Erforderliche Ports für {{site.data.keyword.mcm_core_notm}}_. 

Wenn Sie die Konfiguration Ihrer Edge-Server mit dem {{site.data.keyword.edge_profile}} planen, dann aktivieren Sie die folgenden Ports:

| Port | Protokoll | Voraussetzung |
|------|----------|-------------|
| NA | IPv4 | Calico mit IP-in-IP (calico_ipip_mode: Always) |
| 179 |TCP	        | Always für Calico (network_type: calico)|
| 500 | TCP und UDP | IPSec (ipsec.enabled: true, calico_ipip_mode: Always) |
|2380 | TCP | Always, wenn etcd aktiviert ist |
|4001 | TCP | Always, wenn etcd aktiviert ist |
| 4500 | UDP | IPSec (ipsec.enabled: true) |
| 9091 | TCP | Calico (network_type:calico) |
| 9099 | TCP | Calico (network_type:calico) |
| 10248:10252 | TCP	| Always für Kubernetes |
| 30000:32767 | TCP und UDP | Always für Kubernetes |
{: caption="Tabelle 5. Erforderliche Ports für {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Hinweis: Die Ports 30000:32767 verfügen über externen Zugriff. Diese Ports müssen nur geöffnet sein, wenn Sie den Kubernetes Service-Typ auf NodePort setzen.

## Hinweise zur Clsterdimensionierung
{: #cluster}

Für {{site.data.keyword.edge_servers_notm}} wird als Hub-Cluster normalerweise eine gehostete {{site.data.keyword.icp_server}}-Standardumgebung verwendet. Sie können diese Umgebung benutzen, um auch andere Verarbeitungsworkloads zu hosten, die Sie über einen zentralen Standort bedienen müssen oder wollen. Die Hub-Cluster-Umgebung muss so dimensioniert werden, dass genügend Ressourcen zum Hosten des {{site.data.keyword.mcm_core_notm}}-Clusters und aller zusätzlichen Workloads bereitgestellt werden können, die Sie in der Umgebung hosten wollen. Weitere Einzelheiten zur Dimensionierung einer gehosteten {{site.data.keyword.icp_server}}-Standardumgebung finden Sie unter [Dimensionierung Ihres {{site.data.keyword.icp_server}}-Clusters ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Bei Bedarf können Sie in einer Umgebung, in der Ressourcenbeschränkungen gelten, einen fernen Edge-Server betreiben. Wenn Sie einen Edge-Server in einer Umgebung mit Ressourcenbeschränkungen betreiben müssen, sollten Sie die Verwendung des {{site.data.keyword.edge_profile}}s in Betracht ziehen. Mit diesem Profil werden nur die für eine Edge-Server-Umgebung mindestens erforderlichen Komponenten konfiguriert. Wenn Sie mit diesem Profil arbeiten, müssen Sie dennoch genügend Ressourcen für die Komponentengruppe zuordnen, die für eine {{site.data.keyword.edge_servers_notm}}-Architektur und zur Bereitstellung der Ressourcen benötigt wird, die für andere Anwendungsworkloads benötigt werden, die in Ihren Edge-Server-Umgebungen gehostet werden. Weitere Informationen zur Architektur von {{site.data.keyword.edge_servers_notm}} finden Sie unter [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch). 

Durch Verwendung der Konfigurationen mit dem {{site.data.keyword.edge_profile}} können zwar Einsparungen beim Speicherplatz- und Speicherressourcenbedarf erzielt werden, andererseits führen diese Konfigurationen aber zu einer reduzierten Ausfallsicherheit. Ein Edge-Server, der auf diesem Profil basiert, kann ohne Verbindung zum zentralen Rechenzentrum arbeiten, in dem sich der Hub-Cluster befindet. Dieser Offlinebetrieb kann normalerweise bis zu drei Tage aufrechterhalten werden. Fällt der Edge-Server aus, dann kann dieser Server für Ihr fernes Betriebszentrum jedoch keine weitere Betriebsunterstützung mehr bieten.

Die Konfigurationen mit dem {{site.data.keyword.edge_profile}} sind auch auf die Unterstützung der folgenden Technologien und Prozesse beschränkt:
  * {{site.data.keyword.linux_notm}}-64-Bit-Plattformen
  * Nicht HA-fähige Bereitstellungstopologie (HA = High Availability; Hochverfügbarkeit)
  * Hinzufügung und Entfernung von Workerknoten als Operationen am zweiten Tag (day-2)
  * CLI-Zugriff auf den Cluster und Kontrolle des Clusters
  * Calico-Netze

Wenn Sie ein höheres Maß an Ausfallsicherheit benötigen oder wenn eine der vorgenannten Einschränkungen für Sie nicht akzeptabel ist, dann können Sie sich stattdessen für die Verwendung eines der anderen standardmäßigen Konfigurationsprofile für die Bereitstellung für {{site.data.keyword.icp_server}} entscheiden, die eine bessere Failover-Unterstützung bieten.

### Beispielbereitstellungen

* Edge-Server-Umgebung auf Basis von {{site.data.keyword.edge_profile}} (niedrige Ausfallsicherheit)

| Knotentyp | Anzahl der Knoten | CPU | Hauptspeicher (GB) | Platte (GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
| Boot      |1 | 1   |2 |8 |
| Master    |1 | 2   |4 | 16 |
| Management |1 | 1   |2 |8 |
| Worker    |1 | 4   |8 |32|
{: caption="Tabelle 6. Werte des Edge-Profils für Edge-Server-Umgebungen mit niedriger Ausfallsicherheit" caption-side="top"}

* Edge-Server-Umgebungen auf Basis anderer {{site.data.keyword.icp_server}}-Profile (mittlere bis hohe Ausfallsicherheit)

  Verwenden Sie die Anforderungen für kleine, mittlere und große Beispielbereitstellungen, wenn Sie eine andere Konfiguration als im {{site.data.keyword.edge_profile}} vorgesehen für Ihre Edge-Server-Umgebung verwenden müssen. Weitere Informationen finden Sie unter [{{site.data.keyword.icp_server}}-Cluster dimensionieren: Beispielbereitstellungen ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples).
