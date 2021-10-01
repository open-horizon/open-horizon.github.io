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

# Dimensionierung und Systemvoraussetzungen

Vor der Installation von {{site.data.keyword.edge_servers_notm}} prüfen Sie die Systemvoraussetzungen für jedes Produkt und ermitteln Sie seinen Speicherbedarf.
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [Dimensionierung für Multicluster-Endpunkt](#mc_endpoint)
  - [Dimensionierung für die Management-Hub-Services](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [{{site.data.keyword.ocp_tm}} - Installationsdokumentation ![Wird in einer neuen Registerkarte geöffnet](../images/icons/launch-glyph.svg "Wird in einer neuen Registerkarte geöffnet")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* {{site.data.keyword.open_shift_cp}}-Rechen- oder Workerknoten: 16 Cores | 32 GB RAM

  Hinweis: Wenn Sie {{site.data.keyword.edge_devices_notm}} zusätzlich zu {{site.data.keyword.edge_servers_notm}} installieren möchten, müssen Sie weitere Knotenressourcen hinzufügen, wie im Abschnitt [Dimensionierung](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size) beschrieben.
  
* Speicherbedarf:
  - Für die Offlineinstallation erfordert die {{site.data.keyword.open_shift_cp}} Image-Registry mindestens 100 GB.
  - Die Management-Services MongoDB und die Protokollierung erfordern jeweils 20 GB über die Speicherklasse.
  - Für den Vulnerability Advisor sind 60 GB über die Speicherklasse erforderlich.

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

Die Dimensionierung ist für den minimalen und den Produktionsspeicherbedarf verfügbar.

### Bereitstellungstopologie für {{site.data.keyword.open_shift}} und {{site.data.keyword.edge_servers_notm}}

| Bereitstellungstopologie | Nutzungsbeschreibung | Knotenkonfiguration für {{site.data.keyword.open_shift}} 4.2 |
| :--- | :--- | :--- | :---|
| Minimum | Kleine Clusterbereitstellung | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 Masterknoten <br> &nbsp; mindestens 2 Workerknoten </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 dedizierter Workerknoten </p> |
| Produktion | Unterstützt die Standardkonfiguration <br> von {{site.data.keyword.edge_servers_notm}}| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 Masterknoten (native Hochverfügbarkeit) <br>&nbsp; mindestens 4 Workerknoten </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 dedizierte Workerknoten |
{: caption="Tabelle 1. Konfigurationen der Bereitstellungstopologie für {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Hinweis: Für dedizierte {{site.data.keyword.edge_servers_notm}}-Workerknoten setzen Sie Master-, Management- und Proxy-Knoten auf einen {{site.data.keyword.open_shift}}-Workerknoten, dessen Konfiguration in der [Installationsdokumentation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) zu {{site.data.keyword.edge_servers_notm}} beschrieben ist.

Hinweis: Alle nachstehend aufgeführten persistenten Datenträger sind Standarddatenträger. Sie müssen die Größe der Datenträger basierend auf der Datenmenge, die im Zeitverlauf gespeichert wird, anpassen.

### Minimaldimensionierung
|Konfiguration| Anzahl der Knoten | vCPUs | Arbeitsspeicher | Persistente Datenträger (GB) | Plattenspeicher (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| Master, Management, Proxy | 1 | 16	| 32	| 20  | 100  |
{: caption="Tabelle 2. Minimaldimensionierung von {{site.data.keyword.open_shift}}-Knoten für {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

### Dimensionierung für die Produktion

|Konfiguration| Anzahl der Knoten | vCPUs | Arbeitsspeicher | Persistente Datenträger (GB) | Plattenspeicher (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| Master, Management, Proxy | 3| 48	| 96	| 60  | 300  |
{: caption="Tabelle 3. Dimensionierung von {{site.data.keyword.open_shift}}-Produktionsknoten für {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

## Dimensionierung für Multicluster-Endpunkt
{: #mc_endpoint}

| Komponentenname                 	| Optional 	| CPU-Anforderung 	| CPU-Limit  	| Arbeitsspeicheranforderung  	| Speicherbegrenzung 	|
|--------------------------------	|----------	|-------------	|------------	|-----------------	|--------------	|
| ApplicationManager             	| Ja     	| 100 mCore   	| 500 mCore   	| 128 MiB         	| 2 GiB        	|
| WorkManager                    	| Nein    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB       |
| ConnectionManager              	| Nein    	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| ComponentOperator              	| Nein    	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| CertManager                    	| Nein    	| 100 mCore   	| 300 mCore  	| 100 MiB         	| 300 MiB      	|
| PolicyController               	| Ja     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 256 MiB      	|
| SearchCollector                	| Ja     	| 25 mCore    	| 250 mCore  	| 128 MiB         	| 512 MiB      	|
| ServiceRegistry                	| Ja     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 258 MiB      	|
| ServiceRegistryDNS             	| Ja     	| 100 mCore   	| 500 mCore  	| 70 MiB          	| 170 MiB      	|
| MeteringSender                 	| Ja     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringReader                 	| Ja     	| 100 mCore   	| 500 mCore  	| 128 MiB         	| 512 MiB      	|
| MeteringDataManager            	| Ja     	| 100 mCore   	| 1000 mCore 	| 256 MiB         	| 2560 MiB     	|
| MeteringMongoDB                	| Ja     	| -           	| -          	| 500 MiB           | 1 GiB        	|
| Tiller                         	| Ja     	| -           	| -          	| -               	| -            	|
| TopologyWeaveScope (1 pro Knoten) 	| Ja     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| Ja     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| Ja     	| 50 mCore    	| 100 mCore   	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| Nein    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="Tabelle 4. Anweisungen für Multicluster-Endpunkt" caption-side="top"}

## Dimensionierung für Management-Hub-Services
{: #management_services}

| Servicename                 | Optional 	| CPU-Anforderung | CPU-Limit | Arbeitsspeicheranforderung | Speicherbegrenzung | Persistente Datenträger (Wert ist Standardwert) |Weitere Aspekte |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Katalog-UI, allgemeine Web-UI, IAM-Richtliniencontroller, Schlüsselmanagement, 'mcm-kui', 'metering', Überwachung, Multicluster-Hub, nginx-Ingress, Suche | Standardwert | 9,025 m | 29,289 m | 16,857 Mi | 56,963 Mi | 20 GiB | |
| Auditprotokollierung | Optional | 125 m | 500 m | 250 Mi | 700 Mi | | |
| CIS-Richtliniencontroller | Optional | 525 m | 1,450 m | 832 Mi | 2,560 Mi | | |
| Image-Sicherheitsdurchsetzung | Optional | 128 m | 256 m | 128 Mi | 256 Mi | | |
|Lizenzierung| Optional | 200 m | 500 m | 256 Mi | 512 Mi | | |
| Protokollierung | Optional | 1,500 m | 3,000 m | 9,940 Mi | 10,516 Mi | 20 GiB | |
| Durchsetzung von Multi-Tenant-Kontenkontingenten | Optional | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Mutation Advisor | Optional | 1,000 m | 3,300 m | 2,052 Mi | 7,084 Mi | 100 GiB | |
| Notary | Optional | 600 m | 600 m  | 1,024 Mi | 1,024 Mi | | |
| Controller für Richtlinien zur Verschlüsselung geheimer Schlüssel | Optional | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| Secure Token Service (STS) | Optional | 410 m | 600 m  | 94 Mi  | 314 Mi | | Erfordert Red Hat OpenShift-Servicenetz (Istio) |
| Service für Systemstatusprüfung | Optional | 75 m | 600 m | 96 Mi | 256 Mi | | |
| Vulnerability Advisor (VA) | Optional | 1,940 m | 4,440 m | 8,040 Mi | 27,776 Mi | 10 GiB | Erfordert Red Hat OpenShift-Protokollierung (Elasticsearch) |
{: caption="Tabelle 5. Dimensionierung von Hub-Services" caption-side="top"}

## Nächste Schritte

Kehren Sie zur {{site.data.keyword.edge_servers_notm}} [Installationsdokumentation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) zurück.
