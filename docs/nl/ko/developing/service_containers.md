---

copyright:
years: 2019,2020
lastupdated: "2020-01-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 서비스 작성 준비
{: #service_containers}

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})를 사용하여 에지 디바이스의 {{site.data.keyword.docker}} 컨테이너 내에서 서비스를 개발하십시오. 적절한 {{site.data.keyword.linux_notm}} 베이스, 프로그래밍 언어, 라이브러리 또는 유틸리티를 사용하여 에지 서비스를 작성할 수 있습니다.
{:shortdesc}

서비스를 푸시, 서명, 공개한 후 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})가 에지 디바이스에서 완전 자율 에이전트를 사용하여 서비스를 다운로드, 유효성 검증, 구성, 설치, 모니터합니다. 

에지 서비스는 클라우드 수집 서비스를 사용하여 에지 분석 결과를 저장하고 추가 처리합니다. 이 프로세스는 에지 및 클라우드 코드의 개발 워크플로우를 포함합니다.

{{site.data.keyword.ieam}}의 경우 오픈 소스 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) 프로젝트를 기반으로 하며 `hzn` {{site.data.keyword.horizon}} {{site.data.keyword.linux_notm}} 명령을 사용하여 일부 프로세스를 실행합니다.

## 시작하기 전에
{: #service_containers_begin}

1. 호스트에서 {{site.data.keyword.horizon}} 에이전트를 설치하여 {{site.data.keyword.ieam}}에 사용하도록 개발 호스트를 구성하고 {{site.data.keyword.horizon_exchange}}에 호스트를 등록하십시오. [에지 디바이스에 {{site.data.keyword.horizon}} 에이전트를 설치하고 Hello world 예에 등록](../installing/registration.md)을 참조하십시오.

2. [Docker 허브](https://hub.docker.com/) ID를 작성하십시오. 이는 이 절의 지시사항에 Docker 허브에 서비스 컨테이너 이미지 공개가 포함되므로 필요합니다.

## 프로시저
{: #service_containers_procedure}

**참고**: 명령 구문에 대한 자세한 정보는 [이 문서에서 사용되는 규칙](../getting_started/document_conventions.md)을 참조하십시오.

1. [에지 디바이스에 {{site.data.keyword.horizon}} 에이전트 설치 및 Hello world 예에 등록](../installing/registration.md)의 단계를 수행했을 때 Exchange 인증 정보를 설정하십시오. 이 명령이 오류를 표시하지 않음을 확인하여 인증 정보가 올바르게 설정됨을 확인하십시오.

  ```
  hzn exchange user list
  ```
  {: codeblock}

2. 개발 호스트로 {{site.data.keyword.macOS_notm}} 사용 시 Docker 허브 레지스트리 신임 정보를 `~/.docker/plaintext-passwords.json`에 넣으십시오.

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "{ \"auths\": { \"https://index.docker.io/v1/\": { \"auth\": \"$(printf "${DOCKER_HUB_ID:?}:${DOCKER_HUB_PW:?}" | base64)\" } } }" &gt; ~/.docker/plaintext-passwords.json

  ```
  {: codeblock}

3. 이전에 작성한 Docker 허브 ID로 Docker 허브에 로그인하십시오.

  ```
  export DOCKER_HUB_ID="&amp;TWBLT;yourdockerhubid&gt;" export DOCKER_HUB_PW="&amp;TWBLT;yourdockerhubpassword&gt;" echo "$DOCKER_HUB_PW" | docker login -u $DOCKER_HUB_ID --password-stdin
  ```
  {: codeblock}

  출력 예:
  ```
  WARNING! Your password will be stored unencrypted in ~userName/.docker/config.json.
  Configure a credential helper to remove this warning. See https://docs.docker.com/engine/reference/commandline/login/#credentials-store

  Login Succeeded
  ```

4. 암호화 서명 키 쌍을 작성하십시오. 그러면 exchange에 공개할 때 서비스를 서명할 수 있습니다. 

   **참고**: 이 단계는 한 번만 수행하면 됩니다.

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
  
  여기서 `companyname`은 x509 조직으로 사용되며 `youremailaddress`는 x509 CN으로 사용됩니다.

5. 몇 개의 개발 도구를 설치하십시오.

  **{{site.data.keyword.linux_notm}}**(Ubuntu/Debian 배포판):

  ```
  sudo apt install -y git jq make
  ```
  {: codeblock}

  **{{site.data.keyword.macOS_notm}}**의 경우:

  ```
  brew install git jq make
  ```
  {: codeblock}
  
  **참고**: 필요한 경우 brew를 설치하는 방법에 대한 세부사항은 [homebrew](https://brew.sh/)를 참조하십시오.

## 다음에 수행할 작업
{: #service_containers_what_next}

* 인증 정보 및 서명 키를 사용하여 [개발 예제](../OH/docs/developing/developing.md)를 완료하십시오. 해당 예제에서는 단순 에지 서비스를 빌드하는 방법을 보여주고 {{site.data.keyword.edge_notm}}의 개발을 위한 기초를 알아봅니다.
* {{site.data.keyword.edge_notm}}에서 에지 노드에 배치할 Docker 이미지가 이미 있는 경우 [이미지를 에지 서비스로 변환](transform_image.md)을 참조하십시오.
