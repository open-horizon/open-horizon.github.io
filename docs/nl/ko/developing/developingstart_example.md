---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 고유한 hello world 에지 서비스 작성
{: #dev_start_ex}

다음 예제는 단순 `Hello World` 서비스를 사용하여 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})의 개발에 대해 자세히 알아봅니다. 이 예제를 통해 세 가지 하드웨어 아키텍처를 지원하고 {{site.data.keyword.horizon}} 개발 도구를 사용하는 단일 에지 서비스를 개발합니다.
{:shortdesc}

## 시작하기 전에
{: #dev_start_ex_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## 프로시저
{: #dev_start_ex_procedure}

이 예제는 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) 오픈 소스 프로젝트의 일부입니다. [고유한 Hello World 예제 에지 서비스 빌드 및 공개](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw)의 단계를 수행한 후 여기로 돌아오십시오.

## 다음에 수행할 작업
{: #dev_start_ex_what_next}

* [디바이스에 대한 에지 서비스 개발}](../OH/docs/developing/developing.md)에서 다른 에지 서비스 예제를 사용해 보십시오.
