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

# Exigences relatives au dimensionnement et au système

Avant d'installer {{site.data.keyword.edge_servers_notm}}, examinez la configuration système requise pour chacun des produits ainsi que l'évaluation de l'encombrement.
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [Dimensionnement pour le noeud final multicluster](#mc_endpoint)
  - [Dimensionnement pour les services du concentrateur de gestion](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [Documentation sur l'installation de {{site.data.keyword.ocp_tm}} ![S'ouvre dans un nouvel onglet](../images/icons/launch-glyph.svg "S'ouvre dans un nouvel onglet")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* Noeuds de calcul ou noeuds worker {{site.data.keyword.open_shift_cp}} : 16 coeurs | 32 Go de RAM

  Remarque : Si vous souhaitez installer {{site.data.keyword.edge_devices_notm}} en plus d'{{site.data.keyword.edge_servers_notm}}, vous devrez ajouter des ressources de noeud supplémentaires, tel qu'expliqué dans la [section sur le dimensionnement](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).
  
* Exigences de stockage :
  - Pour une installation hors ligne, le registre d'images {{site.data.keyword.open_shift_cp}} requiert au moins 100 Go.
  - La base de données MongoDB et la journalisation pour les services de gestion requièrent chacune 20 Go d'espace de la classe de stockage.
  - Vulnerability Advisor requiert 60 Go d'espace dans la classe de stockage, en cas d'activation.

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

Le dimensionnement est disponible pour les encombrements de type minimal et production.

### Topologie de déploiement pour {{site.data.keyword.open_shift}} et {{site.data.keyword.edge_servers_notm}}

| Topologie de déploiement | Description de l'utilisation | Configuration des noeuds {{site.data.keyword.open_shift}} 4.2 |
| :--- | :--- | :--- | :---|
| Minimal | Déploiement d'un petit cluster | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 noeuds maîtres <br> &nbsp; 2 noeuds worker ou plus </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 noeud worker dédié </p> |
| Production | Prend en charge la configuration par défaut <br> d'{{site.data.keyword.edge_servers_notm}}| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 noeuds maîtres (haute disponibilité native) <br>&nbsp; 4 noeuds worker ou plus </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 noeuds worker dédiés|
{: caption="Tableau 1. Configurations des différentes topologies de déploiement pour {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Remarque : Pour les noeuds worker dédiés d'{{site.data.keyword.edge_servers_notm}}, définissez les noeuds master, management et proxy sur un noeud worker {{site.data.keyword.open_shift}} qui est expliqué dans la [documentation d'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) d'{{site.data.keyword.edge_servers_notm}}.

Remarque : Tous les volumes persistants indiqués ci-dessous sont ceux par défaut. Vous devez dimensionner les volumes en fonction de la quantité de données stockées dans le temps.

### Dimensionnement minimal
| Configuration | Nombre de noeuds | Unités centrales virtuelles (vCPU) | Mémoire | Volumes persistants (Go) | Espace disque (Go) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| maître, gestion, proxy	| 1| 16	| 32	| 20  | 100  |
{: caption="Tableau 2. Dimensionnement minimal du noeud {{site.data.keyword.open_shift}} pour {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

### Dimensionnement de production

| Configuration | Nombre de noeuds | Unités centrales virtuelles (vCPU) | Mémoire | Volumes persistants (Go) | Espace disque (Go) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| maître, gestion, proxy	| 3| 48	| 96	| 60  | 300  |
{: caption="Tableau 3. Dimensionnement en production du noeud {{site.data.keyword.open_shift}} pour {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

## Dimensionnement du noeud final multicluster
{: #mc_endpoint}

| Nom du composant                 	| Facultatif 	| Demande d'UC 	| Limite d'UC  	| Demande mémoire  	| Limite de mémoire 	|
|--------------------------------	|----------	|-------------	|------------	|-----------------	|--------------	|
| ApplicationManager             	| True     	| 100 mCore   	| 500 mCore   	| 128 MiB         	| 2 GiB        	|
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
| TopologyWeaveScope(1 par noeud) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="Tableau 4. Instructions relatives au noeud final multicluster" caption-side="top"}

## Dimensionnement pour les services du concentrateur de gestion
{: #management_services}

| Nom du service                 | Facultatif | Demande d'UC | Limite d'UC | Demande mémoire | Limite de mémoire | Volume persistant (capa par défaut) | Autres considérations |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui, Common-web-ui, iam-policy-controller, key-management, mcm-kui, metering, monitoring, multicluster-hub,nginx-ingress, search | Défaut | 9 025 m | 29 289 m | 16 857 Mi | 56 963 Mi | 20 GiB | |
| Journalisation d'audit | Facultatif | 125 m | 500 m | 250 Mi | 700 Mi | | |
| Contrôleur de politiques CIS | Facultatif | 525 m | 1 450 m | 832 Mi | 2 560 Mi | | |
| Image Security Enforcement | Facultatif | 128 m | 256 m | 128 Mi | 256 Mi | | |
| Licence | Facultatif | 200 m | 500 m | 256 Mi | 512 Mi | | |
| Journalisation | Facultatif | 1 500 m | 3 000 m | 9 940 Mi | 10 516 Mi | 20 GiB | |
| Application des quotas de compte de multilocation | Facultatif | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Mutation Advisor | Facultatif | 1 000 m | 3 300 m | 2 052 Mi | 7 084 Mi | 100 GiB | |
| Notary | Facultatif | 600 m | 600 m  | 1 024 Mi | 1 024 Mi | | |
| Contrôleur de politiques de chiffrement des secrets | Facultatif | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| Secure Token Service (STS) | Facultatif | 410 m | 600 m  | 94 Mi  | 314 Mi | | Nécessite Red Hat OpenShift Service Mesh (Istio) |
| Service de diagnostic d'intégrité du système | Facultatif | 75 m | 600 m | 96 Mi | 256 Mi | | |
| Vulnerability Advisor (VA) | Facultatif | 1 940 m | 4 440 m | 8 040 Mi | 27 776 Mi | 10 GiB | Nécessite Red Hat OpenShift logging (Elasticsearch) |
{: caption="Tableau 5. Dimensionnement des services de concentrateur" caption-side="top"}

## Etape suivante

Revenez à la [documentation d'installation](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html) d'{{site.data.keyword.edge_servers_notm}}.
