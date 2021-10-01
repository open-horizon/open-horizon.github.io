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

* 연산자 작성
* 연산자를 사용하여 클러스터에 에지 서비스 배치(이 경우, `ibm.helloworld`)
* 배치된 서비스 팟(Pod)에 Horizon 환경 변수(및 기타 필요한 환경 변수) 전달

[Hello World 클러스터 서비스 작성 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/operator/CreateService.md)의 내용을 참조하십시오.

공개된 `ibm.operator` 서비스를 실행하려면 [배치 정책을 사용하는 연산자 예제 에지 서비스 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service)를 참조하십시오.
