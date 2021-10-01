---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# 클러스터에 대한 고유한 Hello World 작성
{: #creating_hello_world}

에지 클러스터에 컨테이너화된 에지 서비스를 배치하려면 첫 번째 단계는 Kubernetes 클러스터에 컨테이너화된 에지 서비스를 배치하는 Kubernetes 연산자를 빌드하는 것입니다.

이 예제를 사용하여 다음 방법을 알아볼 수 있습니다.

* `operator-sdk`를 사용하여 Ansible 운영자 작성하기
* 연산자를 사용하여 서비스를 에지 클러스터에 배치하기
* 에지 클러스터에 `curl` 명령으로 외부에서 액세스할 수 있는 포트 공개하기

[고유 운영자 에지 서비스 작성](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service)을 참조하십시오.

공개된 `hello-operator` 서비스를 실행하려면 [배치 정책과 함께 운영자 예제 에지 서비스 사용](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy)을 참조하십시오.
