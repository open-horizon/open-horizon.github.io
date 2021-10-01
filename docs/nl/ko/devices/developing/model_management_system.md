---

copyright:
years: 2020
lastupdated: "2020-02-6"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 모델 관리를 사용하는 Hello world
{: #model_management_system}

이 예는 모델 관리 시스템(MMS)를 사용하는 {{site.data.keyword.edge_service}} 개발 방법을 학습하는 데 도움이 됩니다. 이 시스템을 사용하여 에지 노드에서 실행되는 에지 서비스가 사용하는 학습 머신 모델을 배치하고 업데이트할 수 있습니다.
{:shortdesc}

## 시작하기 전에
{: #mms_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 프로시저
{: #mms_procedure}

이 예제는 [{{site.data.keyword.horizon_open}} ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/) 오픈 소스 프로젝트의 일부입니다. [사용자 고유의 Hello MMS 에지 서비스 작성 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md))의 단계를 수행한 후 여기로 되돌아오십시오.

## 다음에 수행할 작업
{: #mms_what_next}

* [디바이스를 위한 에지 서비스 개발](developing.md)에서 다른 에지 서비스 예제를 시도해 보십시오.

## 추가 정보

* [모델 관리 세부사항](../developing/model_management_details.md)
