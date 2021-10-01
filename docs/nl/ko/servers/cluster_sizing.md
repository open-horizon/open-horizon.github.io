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

# 크기 조정 및 시스템 요구사항

{{site.data.keyword.edge_servers_notm}}를 설치하기 전에 각 제품 및 설치 공간 크기 조정에 대한 시스템 요구사항을 검토하십시오.
{:shortdesc}

  - [{{site.data.keyword.ocp_tm}}](#ocp)
  - [{{site.data.keyword.edge_servers_notm}}](#cloud_pak)
  - [멀티클러스터-엔드포인트에 대한 크기 조정](#mc_endpoint)
  - [관리 허브 서비스에 대한 크기 조정](#management_services)

## {{site.data.keyword.ocp_tm}}
{: #ocp}

* [{{site.data.keyword.ocp_tm}} 설치 문서![새 탭에서 열림](../images/icons/launch-glyph.svg "새 탭에서 열림")](https://docs.openshift.com/container-platform/4.2/welcome/index.html)
* {{site.data.keyword.open_shift_cp}} 컴퓨팅 또는 작업자 노드: 16 코어 | 32GB RAM

  참고: {{site.data.keyword.edge_servers_notm}} 및 {{site.data.keyword.edge_devices_notm}} 설치 시 [크기 조정 섹션](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/devices/installing/install.html#size)에서 요약한 대로 추가 노드 리소스를 추가해야 합니다.
  
* 스토리지 요구사항:
  - 오프라인 설치의 경우 {{site.data.keyword.open_shift_cp}} 이미지 레지스트리는 최소한 100GB가 필요합니다.
  - 관리 서비스 MongoDB 및 로깅은 각각 스토리지 클래스를 통해 20GB가 필요합니다.
  - 취약성 어드바이저는 사용 설정된 경우 스토리지 클래스를 통해 60GB가 필요합니다.

## {{site.data.keyword.edge_servers_notm}}
{: #cloud_pak}

최소 및 프로덕션 설치 공간을 위한 크기 조정이 사용 가능합니다.

### {{site.data.keyword.open_shift}} 및 {{site.data.keyword.edge_servers_notm}}를 위한 배치 토폴로지

| 배치 토폴로지 | 사용량 설명 | {{site.data.keyword.open_shift}} 4.2 노드 구성 |
| :--- | :--- | :--- | :---|
| 최소 | 작은 클러스터 배치 | <p>{{site.data.keyword.open_shift}}: <br> &nbsp; 3 마스터 노드 <br> &nbsp; 2 이상의 작업자 노드 </p><p>{{site.data.keyword.edge_servers_notm}}:<br> &nbsp; 1 전용 작업자 노드 </p> |
| 프로덕션 | {{site.data.keyword.edge_servers_notm}}의 <br> 기존 구성 지원| <p> {{site.data.keyword.open_shift}}: <br>&nbsp; 3 마스터 노드(기본 HA) <br>&nbsp; 4 이상의 작업자 노드 </p><p> {{site.data.keyword.edge_servers_notm}}:<br>&nbsp; 3 전용 작업자 노드|
{: caption="표 1. {{site.data.keyword.edge_servers_notm}}에 대한 배치 토폴로지 구성" caption-side="top"}

참고: 전용 {{site.data.keyword.edge_servers_notm}} 작업자 노드의 경우 마스터, 관리, 프록시 노드를 하나의 {{site.data.keyword.open_shift}} 작업자 노드로 설정하십시오. 이는 {{site.data.keyword.edge_servers_notm}} [설치 문서](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)에서 구성됩니다.

참고: 아래에 표시된 모든 지속적 볼륨은 기본값입니다. 시간에 따라 저장되는 데이터의 양을 기반으로 볼륨의 크기를 조정해야 합니다.

### 최소 크기 조정
| 구성 |노드 수 | vCPU 수 |메모리 | 지속적 볼륨(GB) | 디스크 공간(GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| 마스터, 관리, 프록시	|1| 16	| 32	| 20  | 100  |
{: caption="표 2. {{site.data.keyword.edge_servers_notm}}를 위한 최소 {{site.data.keyword.open_shift}} 노드 크기 조정" caption-side="top"}

### 프로덕션 크기 조정

| 구성 |노드 수 | vCPU 수 |메모리 | 지속적 볼륨(GB) | 디스크 공간(GB) |
| :--- | :---: | :---: | :---: | :---: |:---: |
| 마스터, 관리, 프록시	|3| 48	| 96	| 60  | 300  |
{: caption="표 3. {{site.data.keyword.edge_servers_notm}}를 위한 프로덕션 {{site.data.keyword.open_shift}} 노드 크기 조정" caption-side="top"}

## 멀티클러스터-엔드포인트에 대한 크기 조정
{: #mc_endpoint}

| 컴포넌트 이름                 	| 선택사항 	| CPU 요청 	| CPU 한계  	| 메모리 요청  	| 메모리 한계 	|
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
| TopologyWeaveScope(노드당 1) 	| True     	| 50 mCore    	| 250 mCore  	| 64 MiB          	| 256 MiB      	|
| TopologyWeaveApp               	| True     	| 50 mCore    	| 250 mCore  	| 128 MiB         	| 256 MiB      	|
| TopologyCollector              	| True     	| 50 mCore    	| 100 mCore  	| 20 MiB          	| 50 MiB       	|
| MulticlusterEndpointOperator   	| False    	| 100 mCore   	| 500 mCore  	| 100 MiB         	| 500 MiB      	|
{: caption="표 4. 멀티클러스터-엔드포인트 지시사항" caption-side="top"}

## 관리 허브 서비스를 위한 크기 조정
{: #management_services}

| 서비스 이름                 | 선택사항 | CPU 요청 | CPU 한계 | 메모리 요청 | 메모리 한계 | 지속적 볼륨(값이 기본값임) | 추가 고려사항 |
|-------------------------------- |---------- |------------- |------------ |----------------- |-------------- |----------------- |-------------- |
| Catalog-ui, Common-web-ui, iam-policy-controller, key-management, mcm-kui, metering, monitoring, multicluster-hub,nginx-ingress, search | 기본값 | 9,025 m | 29,289 m | 16,857 Mi | 56,963 Mi | 20 GiB | |
| 감사 로깅 | 선택사항 | 125 m | 500 m | 250 Mi | 700 Mi | | |
| CIS 정책 제어기 | 선택사항 | 525 m | 1,450 m | 832 Mi | 2,560 Mi | | |
| 이미지 보안 시행 | 선택사항 | 128 m | 256 m | 128 Mi | 256 Mi | | |
|Licensing | 선택사항 | 200 m | 500 m | 256 Mi | 512 Mi | | |
| 로깅 | 선택사항 | 1,500 m | 3,000 m | 9,940 Mi | 10,516 Mi | 20 GiB | |
| 멀티테넌시 계정 할당 시행 | 선택사항 | 25 m | 100 m | 64 Mi | 64 Mi | | |
| Mutation Advisor | 선택사항 | 1,000 m | 3,300 m | 2,052 Mi | 7,084 Mi | 100 GiB | |
| Notary | 선택사항 | 600 m | 600 m  | 1,024 Mi | 1,024 Mi | | |
| 시크릿 암호화 정책 제어기 | 선택사항 | 50 m | 100 m  | 100 Mi | 200 Mi | 110 GiB | |
| 보안 토큰 서비스(STS) | 선택사항 | 410 m | 600 m  | 94 Mi  | 314 Mi | | Red Hat OpenShift 서비스 메시(Istio) 필요 |
| 시스템 성능 상태 검사 서비스 | 선택사항 | 75 m | 600 m | 96 Mi | 256 Mi | | |
| 취약성 어드바이저(VA) | 선택사항 | 1,940 m | 4,440 m | 8,040 Mi | 27,776 Mi | 10 GiB | Red Hat OpenShift 로깅(Elasticsearch) 필요 |
{: caption="표 5. 허브 서비스 크기 조정" caption-side="top"}

## 다음에 수행할 작업

{{site.data.keyword.edge_servers_notm}} [설치 문서](https://www.ibm.com/support/knowledgecenter/SSFKVV_4.0/servers/install_edge.html)로 돌아가십시오.
