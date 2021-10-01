---

copyright:
years: 2020
lastupdated: "2020-04-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에지 서비스에 이미지 전송
{: #transform_image}

이 예제는 기존 Docker 이미지를 에지 서비스로 공개하고 연관된 배치 패턴을 작성하고 해당 배치 패턴을 실행하기 위해 에지 노드를 등록하는 단계를 안내합니다.
{:shortdesc}

## 시작하기 전에
{: #quickstart_ex_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```
{: codeblock}

## 프로시저
{: #quickstart_ex_procedure}

참고: 명령 구문에 대한 자세한 정보는 [이 문서에서 사용된 규칙](../../getting_started/document_conventions.md)을 참조하십시오.

1. 프로젝트 디렉토리를 작성하십시오.

  1. 배치 호스트에서 기존 Docker 프로젝트 디렉토리로 변경하십시오. **기존 Docker 프로젝트가 없지만 이 예제를 계속하려는 경우** 해당 명령을 사용하여 남은 프로시저와 함께 사용할 수 있는 단순 Dockerfile을 작성하십시오.

    ```bash
    cat << EndOfContent > Dockerfile
    FROM alpine:latest
    CMD while :; do echo "Hello, world."; sleep 3; done
    EndOfContent
    ```
    {: codeblock}

  2. 프로젝트에 대해 에지 서비스 메타데이터를 작성하십시오.

    ```bash
    hzn dev service new -s myservice -V 1.0.0 -i $DOCKER_HUB_ID/myservice --noImageGen
    ```
    {: codeblock}

    이 명령은 **horizon/service.definition.json**을 작성하여 서비스를 설명하고 **horizon/pattern.json**을 작성하여 배치 패턴을 설명합니다. 이러한 파일을 열고 컨텐츠를 찾아볼 수 있습니다.

2. 서비스를 빌드하고 테스트하십시오.

  1. Docker 이미지를 빌드하십시오. 이미지 이름은 **horizon/service.definition.json**에서 참조된 사항과 일치해야 합니다.

    ```bash
    eval $(hzn util configconv -f horizon/hzn.json)
    export ARCH=$(hzn architecture)
    sudo docker build -t "${DOCKER_IMAGE_BASE}_$ARCH:$SERVICE_VERSION" .
    unset DOCKER_IMAGE_BASE SERVICE_NAME SERVICE_VERSION
    ```
    {: codeblock}

  2. {{site.data.keyword.horizon}} 시뮬레이션 에이전트 환경에서 이 서비스 컨테이너 이미지를 실행하십시오.

    ```bash
        hzn dev service start -S
    ```
    {: codeblock}

  3. 서비스 컨테이너가 실행 중인지 확인하십시오.

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  4. 시작 시 컨테이너에 전달된 환경 변수를 보십시오. (이는 전체 에이전트가 서비스 컨테이너로 전달하는 동일한 환경 변수입니다.)

    ```bash
    sudo docker inspect $(sudo docker ps -q --filter name=myservice) | jq '.[0].Config.Env'
    ```
    {: codeblock}

  5. 서비스 컨테이너 로그를 보십시오.

    **{{site.data.keyword.linux_notm}}**의 경우:

    ```bash
    sudo tail -f /var/log/syslog | grep myservice[[]
    ```
    {: codeblock}

    **{{site.data.keyword.macOS_notm}}**의 경우:

    ```bash
sudo docker logs -f $(sudo docker ps -q --filter name=myservice)
    ```
    {: codeblock}

  6. 서비스를 중지하십시오.

    ```bash
        hzn dev service stop
    ```
    {: codeblock}

3. 서비스를 {{site.data.keyword.edge_devices_notm}}에 공개하십시오. 이제 서비스 코드가 시뮬레이션된 에이전트 환경에서 예상대로 실행하는 것을 검증했으므로, 에지 노드에 배치할 수 있도록 서비스를 {{site.data.keyword.horizon_exchange}}에 공개하십시오.

  다음 **publish** 명령은 **horizon/service.definition.json** 파일과 사용자의 키 쌍을 사용하여 서비스를 서명하고 {{site.data.keyword.horizon_exchange}}에 공개합니다. 또한 Docker 허브에 이미지를 푸시합니다.

  ```bash
  hzn exchange service publish -f horizon/service.definition.json
  hzn exchange service list
  ```
  {: codeblock}

4. 서비스의 배치 패턴을 공개하십시오. 에지 노드에서 이 배치 패턴을 사용하여 {{site.data.keyword.edge_devices_notm}}가 서비스를 에지 노드에 배치하도록 할 수 있습니다.

  ```bash
    hzn exchange pattern publish -f horizon/pattern.json
    hzn exchange pattern list
  ```
  {: codeblock}

5. 에지 노드를 등록하여 배치 패턴을 실행하십시오.

  1. 이전에 에지 노드를 **IBM** 조직의 공용 배치 패턴에 등록한 것과 동일한 방식으로 고유한 조직 아래에 공개한 배치 패턴에 에지 노드를 등록하십시오.

    ```bash
    hzn register -p pattern-myservice-$(hzn architecture) -s myservice --serviceorg $HZN_ORG_ID
    ```
    {: codeblock}

  2. 결과적으로 시작된 Docker 컨테이너 에지 서비스를 나열하십시오.

    ```bash
    sudo docker ps
    ```
    {: codeblock}

  3. myservice 에지 서비스 출력을 보십시오.

    ```bash
    sudo hzn service log -f myservice
    ```
    {: codeblock}

6. {{site.data.keyword.edge_devices_notm}} 콘솔에서 작성한 노드, 서비스 및 패턴을 보십시오. 다음과 함께 콘솔 URL을 표시할 수 있습니다.

  ```bash
  echo "$(awk -F '=|edge-exchange' '/^HZN_EXCHANGE_URL/ {print $2}' /etc/default/horizon)edge"
  ```
  {: codeblock}

7. 에지 노드를 등록 취소하고 **myservice** 서비스를 중지하십시오.

  ```bash
        hzn unregister -f
  ```
  {: codeblock}

## 다음에 수행할 작업
{: #quickstart_ex_what_next}

* [{{site.data.keyword.edge_devices_notm}}로 에지 서비스 개발](developing.md)의 다른 에지 서비스 예제를 시도해 보십시오.
