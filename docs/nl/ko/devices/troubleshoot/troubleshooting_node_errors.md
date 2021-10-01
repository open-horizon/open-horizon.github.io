---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 노드 오류 문제점 해결
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}}에서는 {{site.data.keyword.gui}}에서 볼 수 있는 exchange에 이벤트 로그 서브세트를 공개합니다. 이 오류는 문제점 해결 안내에 링크됩니다.
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

이 오류는 서비스 정의에서 참조하는 서비스 이미지가 이미지 저장소에 없는 경우 발생합니다. 이 오류를 해결하려면 다음을 수행하십시오.

1. **-I** 플래그 없이 서비스를 다시 공개하십시오.
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. 서비스 이미지를 이미지 저장소에 직접 푸시하십시오. 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

이 오류는 서비스 정의 배치 구성이 루트로 보호된 파일에 대한 바인드를 지정하는 경우에 발생합니다. 이 오류를 해결하려면 다음을 수행하십시오.

1. 루트로 보호되지 않은 파일에 컨테이너를 바인드하십시오.
2. 사용자의 파일에 대한 읽기 및 쓰기를 허용하도록 파일 권한을 변경하십시오.

## error_start_container
{: #esc}

이 오류는 서비스 컨테이너를 시작한 경우 Docker에서 오류가 발생하면 나타납니다. 오류 메시지는 컨테이너 시작이 실패한 이유를 나타내는 세부사항을 포함할 수 있습니다. 오류 해결 단계는 오류에 따라 다릅니다. 다음 오류가 발생할 수 있습니다.

1. 디바이스는 배치 구성에서 지정한 공개된 포트를 이미 사용하고 있습니다. 오류를 해결하려면 다음을 수행하십시오. 

    - 다른 포트를 서비스 컨테이너 포트에 맵핑하십시오. 표시되는 포트 번호가 서비스 포트 번호와 일치할 필요는 없습니다.
    - 동일한 포트를 사용하는 프로그램을 중지하십시오.

2. 배치 구성에서 지정한 공개된 포트가 유효한 포트 번호가 아닙니다. 포트 번호는 1 - 65535 범위의 숫자여야 합니다.
3. 배치 구성에서 볼륨 이름은 유효한 파일 경로가 아닙니다. 볼륨 경로는 절대 경로(상대 경로가 아님)로 지정해야 합니다. 

## 추가 정보

자세한 정보는 다음을 참조하십시오.
  * [{{site.data.keyword.edge_devices_notm}} 문제점 해결 안내서](../troubleshoot/troubleshooting.md)
