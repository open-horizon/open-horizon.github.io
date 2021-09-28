---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 시크릿을 사용하는 Hello world
{: #secrets}

이 예제에서는 시크릿을 사용하는 {{site.data.keyword.edge_service}}을(를) 개발하는 방법을 알려 줍니다. 시크릿은 로그인 신임 정보 및 기타 민감한 정보가 안전하게 유지되는지 확인합니다.
{:shortdesc}

## 시작하기 전에
{: #secrets_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## 프로시저
{: #secrets_procedure}

이 예제는 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) 오픈 소스 프로젝트의 일부입니다. [고유한 Hello 시크릿 서비스 작성](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)의 단계를 수행한 후 여기로 돌아오십시오.

## 다음에 수행할 작업
{: #secrets_what_next}

* [디바이스를 위한 에지 서비스 개발](developing.md)에서 다른 에지 서비스 예제를 시도해 보십시오.

## 추가 정보

* [시크릿 사용](../developing/secrets_details.md)
