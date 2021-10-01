---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 컴포넌트

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에는 제품에 번들된 여러 컴포넌트가 포함되어 있습니다.
{:shortdesc}

{{site.data.keyword.ieam}} 컴포넌트의 설명에 대해 다음 표를 참조하십시오.

|컴포넌트|버전|설명|
|---------|-------|----|
|[IBM Cloud Platform Common Services](https://www.ibm.com/docs/en/cpfs)|3.6.x|{{site.data.keyword.ieam}} 운영자 설치의 일부로 자동 설치되는 기본 컴포넌트 세트입니다.|
|Agbot|{{site.data.keyword.anax_ver}}|계약 봇(agbot) 인스턴스는 중앙에서 작성되며, {{site.data.keyword.ieam}}에 워크로드 및 기계 학습 모델을 배치하는 데 책임을 집니다.|
|MMS |1.5.3-338|모델 관리 시스템(MMS)은 에지 서비스에서 필요한 모델, 데이터 및 기타 메타데이터 패키지의 스토리지, 전달 및 보안을 용이하게 합니다. 이것은 에지 노드가 클라우드로 및 클라우드로부터 모델과 메타데이터를 쉽게 전송 및 수신할 수 있게 합니다.|
|Exchange API|2.87.0-531|Exchange는 {{site.data.keyword.ieam}}에 있는 다른 모든 컴포넌트가 사용하는 모든 정의(패턴, 정책, 서비스 등)를 보유하는 REST API를 제공합니다.|
|관리 콘솔|1.5.0-578|{{site.data.keyword.ieam}} 관리자가 {{site.data.keyword.ieam}}의 기타 컴포넌트를 보고 관리하기 위해 사용하는 UI입니다.|
|SDO(Secure Device Onboard)|1.11.11-441|SDO 컴포넌트는 쉽고 안전하게 에지 디바이스를 구성한 후 에지 관리 허브와 연관시키기 위해 Intel에서 작성한 기술을 사용할 수 있도록 해줍니다.|
|클러스터 에이전트|{{site.data.keyword.anax_ver}}|이 컴포넌트는 {{site.data.keyword.ieam}}에서 노드 워크로드 관리를 사용할 수 있도록 에지 클러스터에 에이전트로 설치되는 컨테이너 이미지입니다.|
|디바이스 에이전트|{{site.data.keyword.anax_ver}}|이 컴포넌트는 {{site.data.keyword.ieam}}에서 노드 워크로드 관리를 사용으로 설정하기 위해 에지 디바이스에 설치됩니다.|
|Secrets Manager|1.0.0-168|Secrets Manager는 에지 디바이스에 배치된 시크릿의 저장소이며, 서비스를 사용하여 업스트림 종속성에 대해 인증하는 데 사용되는 인증 정보를 안전하게 수신할 수 있습니다.|
