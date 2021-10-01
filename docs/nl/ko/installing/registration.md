---

copyright:
years: 2020
lastupdated: "2020-02-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 에이전트 설치
{: #registration}

에지 디바이스에 {{site.data.keyword.horizon}} 에이전트 소프트웨어를 설치할 때, 에지 디바이스를 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에 등록하여 디바이스를 에지 컴퓨팅 관리 도메인에 추가하고 에지 서비스를 실행할 수 있습니다. 다음 지시사항은 새 에지 디바이스를 최소 helloworld 예제 에지 서비스에 등록하여 에지 디바이스가 제대로 작동하는지 확인합니다. helloworld 에지 서비스는 자체 에지 서비스를 에지 디바이스에서 실행할 준비가 되면 쉽게 중지할 수 있습니다.
{:shortdesc}

## 시작하기 전에
{: #before_begin}

[에지 디바이스 준비](adding_devices.md)의 단계를 완료해야 합니다.

## 에지 디바이스 설치 및 등록
{: #installing_registering}

에지 디바이스에 에이전트를 설치하고 에지 디바이스를 등록하기 위한 네 가지 방법이 제공되며, 각각 서로 다른 상황에서 유용합니다.

* [자동화된 에이전트 설치 및 등록](automated_install.md) - 최소한의 단계를 사용하여 1개의 에지 디바이스를 설치 및 등록합니다. **최초 사용자는 이 메소드를 사용해야 합니다.**
* [고급 수동 에이전트 설치 및 등록](advanced_man_install.md) - 사용자 스스로 1개의 에지 디바이스를 설치 및 등록하기 위한 각 단계를 수행합니다. 정상에서 벗어난 무엇인가를 수행해야 하고 방법 1에서 사용되는 스크립트가 필요한 유연성을 갖지 않는 경우에 이 방법을 사용하십시오. 또한 에지 디바이스를 설정하기 위해 필요한 사항을 정확하게 이해하기 원하는 경우에도 이 방법을 사용할 수 있습니다.
* [대량 에이전트 설치 및 등록](many_install.md#batch-install) - 한 번에 많은 에지 디바이스를 설치 및 등록합니다.
* [SDO 에이전트 설치 및 등록](sdo.md) - SDO 디바이스로 자동 설치합니다.

## 질문 및 문제점 해결
{: #questions_ts}

이들 단계를 수행하는 데 어려움이 있으면 제공된 문제점 해결 및 자주 묻는 질문(FAQ) 주제를 검토하십시오. 자세한 정보는 다음을 참조하십시오.
  * [문제점 해결](../troubleshoot/troubleshooting.md)
  * [자주 묻는 질문(FAQ)](../getting_started/faq.md)
