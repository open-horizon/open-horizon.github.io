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

# Dimensionamento e requisitos do sistema

Antes de instalar o {{site.data.keyword.edge_servers_notm}}, revise os requisitos do sistema de cada um dos produtos e o dimensionamento da área de cobertura.
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [Dimensionamento para o terminal de vários clusters](#mc_endpoint)
  - [Dimensionamento para os serviços de hub de gerenciamento](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [Documentação de instalação do {{site.data.keyword.ocp_tm}} ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* Nós de cálculo ou de trabalhador do {{site.data.keyword.open_shift_cp}}: 16 Core | 32 GB RAM

  Nota: se você desejar instalar o {{site.data.keyword.edge_devices_notm}} além do {{site.data.keyword.edge_servers_notm}}, será necessário incluir recursos de nó adicionais conforme descrito na [seção de dimensionamento](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size).
  
* Requisitos de armazenamento:
  - Para a instalação off-line, o registro de imagem do {{site.data.keyword.open_shift_cp}} requer pelo menos 100 GB.
  - Os serviços de gerenciamento MongoDB e a criação de log requerem, cada um, 20 GB na classe de armazenamento.
  - Se ativado, o consultor de vulnerabilidade requer 60 GB pela classe de armazenamento.

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

O dimensionamento disponível destina-se a áreas de cobertura mínimas e de produção.

### Topologia de implementação para o {{site.data.keyword.open_shift}} e o {{site.data.keyword.edge_servers_notm}}

| Topologia de implementação | Descrição do uso | Configuração do nó {{site.data.keyword.open_shift}} 4.2 |
| :--- | :--- | :--- | :---|
| Mínimo | Implementação de cluster pequeno | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 nós principais <br> &nbsp; 2 ou mais nós do trabalhador </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 nó do trabalhador dedicado </p> |
| Produção | Suporta a configuração padrão <br> de {{site.data.keyword.edge_servers_notm}}| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 nós principais (HA nativa) <br>&nbsp; 4 ou mais nós do trabalhador </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 nós do trabalhador dedicados|
{: caption="Tabela 1. Configurações de topologia de implementação para o {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Nota: para nós do trabalhador do {{site.data.keyword.edge_servers_notm}} dedicado, configure os nós principais, de gerenciamento e de proxy para um nó do trabalhador do {{site.data.keyword.open_shift}}, que está configurado na {{site.data.keyword.edge_servers_notm}} [Documentação de instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html).

Nota: todos os volumes persistentes indicados abaixo são padrão. Os volumes devem ser dimensionados com base na quantidade de dados que serão armazenados ao longo do tempo.

### Dimensionamento mínimo
| Configuração | Número de nós | vCPUs | Memória | Volumes persistentes (GB) | Espaço em Disco (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| principal, gerenciamento e proxy	| 1| 16	| 32	| 20  | 100  |
{: caption="Tabela 2. Dimensionamento de nó mínimo do {{site.data.keyword.open_shift}} para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

### Dimensionamento de produção

| Configuração | Número de nós | vCPUs | Memória | Volumes persistentes (GB) | Espaço em Disco (GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| principal, gerenciamento e proxy	| 3| 48	| 96	| 60  | 300  |
{: caption="Tabela 3. Dimensionamento de nó de produção do {{site.data.keyword.open_shift}} para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

## Dimensionamento para o terminal de vários clusters
{: #mc_endpoint}

| Nome do componente                 	| Opcional 	| Solicitação de CPU 	| Limite de CPU  	| Solicitação de memória  	| Limite de memória 	|
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
| TopologyWeaveScope(1 por nó) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="Tabela 4. Instruções para terminais de vários clusters" caption-side="top"}

## Dimensionamento para serviços de hub de gerenciamento
{: #management_services}

| Nome do Serviço                 | Opcional | Solicitação de CPU | Limite de CPU | Solicitação de memória | Limite de memória | Volume persistente (valor padrão) | Considerações adicionais |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui, Common-web-ui, iam-policy-controller, key-management, mcm-kui, metering, monitoring, multicluster-hub,nginx-ingress, search | Padrão | 9.025 m | 29.289 m | 16.857 Mi | 56.963 Mi | 20 gigabytes | |
| Criação de log da auditoria | Opcional | 125 m | 500 m | 250 Mi | 700 Mi | | |
| Controlador de Política do CIS | Opcional | 525 m | 1.450 m | 832 Mi | 2.560 Mi | | |
| Cumprimento de segurança da imagem | Opcional | 128 m | 256 m | 128 Mi | 256 Mi | | |
| Licença | Opcional | 200 m | 500 m | 256 Mi | 512 Mi | | |
| Criação de Log | Opcional | 1.500 m | 3.000 m | 9.940 Mi | 10.516 Mi | 20 gigabytes | |
| Cumprimento de cota da conta de ocupação variada | Opcional | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Mutation Advisor | Opcional | 1.000 m | 3.300 m | 2.052 Mi | 7.084 Mi | 100 GiB | |
| Tabelião Público | Opcional | 600 m | 600 m  | 1.024 Mi | 1.024 Mi | | |
| Controlador de política de criptografia secreta | Opcional | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| Serviço de token seguro (STS) | Opcional | 410 m | 600 m  | 94 Mi  | 314 Mi | | Requer o Red Hat OpenShift Service Mesh (Istio) |
| Serviço de verificação de funcionamento do sistema | Opcional | 75 m | 600 m | 96 Mi | 256 Mi | | |
| Vulnerability Advisor (VA) | Opcional | 1.940 m | 4.440 m | 8.040 Mi | 27.776 Mi | 10 GiB | Requer a criação de log do Red Hat OpenShift (Elasticsearch) |
{: caption="Tabela 5. Dimensionamento de serviços de hub" caption-side="top"}

## O que fazer a seguir

Retorne para a {{site.data.keyword.edge_servers_notm}} [documentação de instalação](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html).
