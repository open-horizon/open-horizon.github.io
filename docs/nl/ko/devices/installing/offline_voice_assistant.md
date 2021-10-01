---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 오프라인 음성 지원
{: #offline-voice-assistant}

1분 마다, 오프라인 음성 지원은 5초 오디오 클립을 기록하고 오디오 클립을 에지 디바이스의 텍스트로 로컬로 변환하고 호스트 머신이 명령을 실행하고 출력을 표현하도록 지시합니다. 

## 시작하기 전에
{: #before_beginning}

시스템이 해당 요구사항을 충족하는지 확인하십시오.

* [에지 디바이스 준비](adding_devices.md)의 단계를 수행하여 등록 및 등록 취소해야 합니다.
* USB 사운드 카드 및 마이크로폰이 Raspberry Pi에 설치됩니다. 

## 에지 디바이스 등록
{: #reg_edge_device}

에지 노드에서 `processtext` 서비스 예제를 실행하려면 `IBM/pattern-ibm.processtext` 배치 패턴에 에지 노드를 등록해야 합니다. 

readme 파일의 배치 패턴을 사용하여 오프라인 음성 지원 예제 에지 서비스 사용([배치 패턴을 사용하여 오프라인 음성 지원 예제 에지 서비스 사용 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern)) 섹션에 있는 단계를 수행하십시오.

## 추가 정보
{: #additional_info}

`processtext` 예제 소스 코드는 Horizon GitHub 저장소에서 I{{site.data.keyword.edge_devices_notm}} 개발에 대한 예제로 사용할 수도 있습니다. 이 소스에는 이 예제의 에지 노드에서 실행되는 모든 서비스에 대한 코드가 포함되어 있습니다. 

해당 [Open Horizon 예제 ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) 서비스는 다음을 포함합니다.

* [voice2audio ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) 서비스는 5초 오디오 클립을 기록하고 mqtt 브로커에 공개합니다.
* [audio2text ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) 서비스는 오디오 클립을 사용하고 포켓 스핑크스를 통해 텍스트 오프라인으로 변환합니다.
* [processtext ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) 서비스는 텍스트를 사용하고 레코드 명령을 실행하려고 시도합니다.
* [text2speech ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) 서비스는 스피커를 통해 명령 출력을 재생합니다.
* [mqtt_broker ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker)에서는 모든 컨테이너 간 통신을 관리합니다.

## 다음에 수행할 작업
{: #what_next}

Watson 음성-문자 변환의 사용자 고유 버전 빌드 및 공개에 대한 지시사항은 [Open Horizon 예제![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service) 저장소의 `processtext` 디렉토리 단계를 참조하십시오. 
