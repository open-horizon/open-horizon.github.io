---

copyright:
  years: 2016, 2019
lastupdated: "2019-03-14"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 접근성 기능

접근성 기능은 거동이 불편하거나 시각 장애가 있는 사용자가 정보 기술 컨텐츠를 정상적으로 사용할 수 있도록 지원합니다.
{:shortdesc}

## 개요

{{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에는 다음의 주요 접근성 기능이 포함되어 있습니다.

* 키보드 전용 조작
* 스크린 리더 오퍼레이션
* {{site.data.keyword.ieam}} 클러스터 관리용 명령행 인터페이스(CLI)

{{site.data.keyword.ieam}}은 최신 W3C 표준인 [WAI-ARIA 1.0 ![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘")](http://www.w3.org/TR/wai-aria/){: new_window}을 사용하여 [전자 및 정보 기술에 대한 Section 508 표준 ![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘")](http://www.access-board.gov/guidelines-and-standards/communications-and-it/about-the-section-508-standards/section-508-standards){: new_window} 및 [WCAG(Web Content Accessibility Guidelines) 2.0 ![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘")](http://www.w3.org/TR/WCAG20/){: new_window}의 준수를 보장합니다. 접근성 기능을 이용하려면 {{site.data.keyword.ieam}}에서 지원하는 최신 웹 브라우저와 최신 릴리스의 스크린 리더를 사용하십시오.

IBM 문서의 {{site.data.keyword.ieam}} 온라인 제품 문서에서 내게 필요한 옵션을 사용할 수 있습니다. 일반적인 접근성 정보는 [IBM Accessibility ![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘")](http://www.ibm.com/accessibility/us/en/){: new_window}를 참조하십시오.

## 하이퍼링크

IBM 문서 외부에서 호스팅되는 컨텐츠에 대한 링크인 모든 외부 링크는 새 창에서 열립니다. 또한 이러한 외부 링크는 외부 링크 아이콘(![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘"))으로 플래그 지정됩니다.

## 키보드 탐색

{{site.data.keyword.ieam}}은 표준 탐색 키를 사용합니다.

{{site.data.keyword.ieam}}은 다음의 키보드 단축키를 사용합니다.

|조치|Internet Explorer의 단축키|Firefox의 단축키|
|------|------------------------------|--------------------|
|컨텐츠 보기 프레임으로 이동|Alt+C 이후 Enter 및 Shift+F6 누르기|Shift+Alt+C 및 Shift+F6|
{: caption="표 1. {{site.data.keyword.ieam}}의 키보드 단축키" caption-side="top"}

## 인터페이스 정보

{{site.data.keyword.ieam}}은 최신 버전의 스크린 리더를 사용합니다.

{{site.data.keyword.ieam}} 사용자 인터페이스에는 초당 2 - 55번 깜박이는 컨텐츠가 없습니다.

{{site.data.keyword.ieam}} 웹 사용자 인터페이스는 캐스케이딩 스타일시트에 의존하여 컨텐츠를 적절하게 렌더링하고 유용한 환경을 제공합니다. 이 애플리케이션은 시각 장애가 있는 사용자가 고대비 모드를 포함한 시스템 표시 설정을 사용할 수 있는 동일한 방법을 제공합니다, 사용자는 디바이스 또는 웹 브라우저 설정을 사용하여 글꼴 크기를 제어할 수 있습니다.

{{site.data.keyword.gui}}에 액세스하려면 웹 브라우저를 열고 다음 URL로 이동하십시오.

`https://<Cluster Master Host>:<Cluster Master API Port>/edge`

사용자 이름과 비밀번호는 config.yaml 파일에 정의되어 있습니다.

{{site.data.keyword.gui}}은 컨텐츠를 적절하게 렌더링하고 유용한 환경을 제공하기 위해 캐스케이딩 스타일시트에 의존하지 않습니다. 그러나 IBM Knowledge 문서에서 사용할 수 있는 제품 문서는 캐스케이딩 스타일시트에 의존합니다. {{site.data.keyword.ieam}}은 시각 장애가 있는 사용자가 고대비 모드를 포함한 시스템 표시 설정을 사용할 수 있는 동일한 방법을 제공합니다, 사용자는 디바이스 또는 브라우저 설정을 사용하여 글꼴 크기를 제어할 수 있습니다. 참고로, 제품 문서에는 표준 스크린 리더가 잘못 발음할 수 있는 파일 경로, 환경 변수, 명령 및 기타 컨텐츠가 포함되어 있습니다. 가장 정확한 표현을 위해 모든 구두점을 읽도록 스크린 리더 설정을 구성하십시오.


## 공급업체 소프트웨어

{{site.data.keyword.ieam}}에는 IBM 라이센스 계약에서 언급되지 않는 특정 공급업체 소프트웨어가 포함되어 있습니다. IBM은 이러한 제품의 접근성 기능을 제공하지 않습니다. 해당 제품의 접근성 정보가 필요하면 해당 공급업체에 문의하십시오.

## 관련된 접근성 정보

표준 IBM 헬프 데스크와 지원 웹 사이트 외에도, IBM에는 청각 장애가 있는 고객이 판매 및 지원 서비스에 액세스하기 위해 사용할 수 있는 TTY 전화 서비스가 있습니다.

TTY 서비스  
 800-IBM-3383 (800-426-3383)  
 (북미 지역 내)

접근성과 관련된 IBM의 공약에 대한 자세한 정보는 [IBM Accessibility ![외부 링크 아이콘](../images/icons/launch-glyph.svg "외부 링크 아이콘")](http://www.ibm.com/able){: new_window}를 참조하십시오.
