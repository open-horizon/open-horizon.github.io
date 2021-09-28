---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 디바이스용 에지 서비스 개발
{: #developing}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 에지 서비스 개발을 시작하려면 먼저 컨텐츠를 공개하기 위한 인증 정보를 설정해야 합니다. 모든 서비스가 서명되어야 하므로 암호화 서명 키 쌍도 작성해야 합니다. 전제조건 단계, [에지 서비스 작성 준비](service_containers.md)를 완료해야 합니다.

이 다이어그램은 {{site.data.keyword.horizon}} 내 컴포넌트 간의 일반적인 상호작용을 보여줍니다.

<img src="../images/edge/03a_Developing_edge_service_for_device.svg" style="margin: 3%" alt="에지 디바이스"> 

## 예제
{: #edge_devices_ex_examples}

인증 정보 및 서명 키를 사용하여 개발 예제를 완료하십시오. 해당 예제에서는 단순 서비스를 빌드하는 방법을 보여주고 {{site.data.keyword.ieam}} 개발 기초에 대해 알아볼 수 있도록 합니다.

이러한 개발 예제 각각은 에지 서비스 개발의 여러 측면을 보여줍니다. 최적화된 학습 경험을 위해 여기에 나열된 순서대로 예제를 완료하십시오.

* [에지 서비스에 이미지 전송](transform_image.md) - 에지 서비스로 기존 Docker 이미지 배치를 보여줍니다.

* [고유한 hello world 에지 서비스 작성](developingstart_example.md) - 에지 서비스 개발, 테스트, 공개, 배치에 대한 기본을 보여줍니다.

* [CPU 대 {{site.data.keyword.message_hub_notm}} 서비스](cpu_msg_example.md) - 에지 서비스 구성 매개변수를 정의하고 에지 서비스에 기타 에지 서비스가 필요함을 지정하고 클라우드 데이터 수집 서비스에 데이터를 전송하는 방법을 보여줍니다.

* [모델 관리를 사용하는 Hello world](model_management_system.md) - 모델 관리 서비스를 사용하는 에지 서비스를 개발하는 방법을 보여줍니다. 모델 관리 서비스는 예를 들어, 머신 학습 모델이 진화할 때마다 동적으로 업데이트하기 위해 에지 노드의 에지 서비스에 대한 파일 업데이트를 비동기로 제공합니다.

* [시크릿을 사용한 Hello world](developing_secrets.md) - 시크릿을 사용하는 에지 서비스를 개발하는 방법을 보여줍니다. 시크릿은 로그인 신임 정보 또는 개인 키와 같은 민감한 데이터를 보호하는 데 사용됩니다. 시크릿은 에지에서 실행 중인 서비스에 안전하게 배치됩니다.

* [롤백을 사용하여 에지 서비스 업데이트](../using_edge_services/service_rollbacks.md) - 배치 성공을 모니터하고, 에지 노드에서 실패하는 경우 에지 서비스의 이전 버전으로 노드를 다시 되돌리는 방법을 설명합니다.

이러한 예제 서비스의 빌드를 완료한 후 다음 문서에서 {{site.data.keyword.ieam}}용 서비스 개발에 대한 자세한 정보를 검토하십시오.

## 추가 정보
{: #developing_more_info}

{{site.data.keyword.ieam}} 소프트웨어 개발에 대한 중요한 원칙과 우수 사례를 검토하십시오.

* [에지 네이티브 개발 우수 사례](best_practices.md)

{{site.data.keyword.ieam}}에서는 선택적으로 공용 Docker 허브 대신 IBM 사설 보안 컨테이너 레지스트리에 서비스 컨테이너 이미지를 넣을 수 있습니다. 예를 들어 공용 레지스트리에 포함하기에 적합하지 않은 자산을 포함하는 소프트웨어 이미지가 있는 경우.

* [개인 컨테이너 레지스트리 사용](container_registry.md)

{{site.data.keyword.ieam}}을 사용하여 공용 Docker 허브 대신 IBM 사설 보안 컨테이너 레지스트리에 서비스 컨테이너를 넣을 수 있습니다.

* [개발 세부사항](developing_details.md)

{{site.data.keyword.ieam}}을 사용하여 에지 머신에 대해 원하는 서비스 컨테이너를 개발할 수 있습니다.

* [API](../api/edge_rest_apis.md)

{{site.data.keyword.ieam}}은 컴포넌트가 협업하고 조직의 개발자와 사용자가 컴포넌트를 제어할 수 있도록 RESTful API를 제공합니다.
