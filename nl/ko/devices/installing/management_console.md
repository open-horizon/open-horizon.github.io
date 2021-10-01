---

copyright:
years: 2020
lastupdated: "2020-1-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# {{site.data.keyword.edge_notm}} 콘솔 사용
{: #accessing_ui}

콘솔을 사용하여 에지 컴퓨팅 관리 기능을 수행하십시오. 
 
## {{site.data.keyword.edge_notm}} 콘솔 탐색

1. `https://<cluster-url>/edge`를 브라우징하여 {{site.data.keyword.edge_notm}} 콘솔로 이동하십시오. 여기서 `<cluster-url>`은 클러스터의 외부 유입입니다.
2. 사용자 인증 정보를 입력하십시오. {{site.data.keyword.mcm}} 로그인 페이지가 표시됩니다.
3. 브라우저 주소 표시줄에서, URL의 끝에서 `/multicloud/welcome`을 제거하고 `/edge`를 추가한 후 **Enter**를 누르십시오. {{site.data.keyword.edge_notm}} 페이지가 표시됩니다.

## 지원되는 브라우저

{{site.data.keyword.edge_notm}}는 다음 브라우저로 성공적으로 테스트되었습니다.

|플랫폼|지원되는 브라우저|
|--------|------------------|
|Microsoft Windows™|<ul><li>Mozilla Firefox - Windows용 최신 버전</li><li>Google Chrome - Windows용 최신 버전</li></ul>|
|{{site.data.keyword.macOS_notm}}|<ul><li>Mozilla Firefox - Mac용 최신 버전</li><li>Google Chrome - Mac용 최신 버전</li></ul>|
{: caption="표 1. {{site.data.keyword.edge_notm}}에서 지원되는 브라우저" caption-side="top"}


## {{site.data.keyword.edge_notm}} 콘솔 탐색
{: #exploring-management-console}

{{site.data.keyword.edge_notm}} 콘솔 기능에는 다음이 포함됩니다.

* 강력한 지원을 위한 주변 사이트 링크를 사용한 사용자 친화적인 온보딩
* 광범위한 가시성 및 관리 기능:
  * 노드 상태, 아키텍처 및 오류 정보를 포함하는 광범위한 차트 보기
  * 해결 정보를 위힌 링크를 포함한 오류 세부사항
  * 다음에 대한 정보를 포함하는 위치 및 필터링 컨텐츠: 
    * 소유자
    * 아키텍처 
    * 하트비트(예: 지난 10분, 오늘 등)
    * 노드 상태(활성, 비활성, 오류 등)
    * 배치 유형(정책 또는 패턴)
  * 다음을 포함한 exchange 에지 노드에 관한 유용한 세부사항:
    * 특성
    * 제한조건 
    * 배치
    * 활성 서비스

* 강력한 보기 기능

  * 다음을 기준으로 빠르게 찾고 필터링할 수 있음: 
    * 소유자
    * 아키텍처
    * 버전
    * 공용(true 또는 false)
  * 카드 서비스 보기 또는 나열
  * 이름을 공유하는 그룹화 그룹
  * 다음을 포함하는 Exchange의 각 서비스에 대한 세부사항: 
    * 특성
    * 제한조건
    * 배치
    * 서비스 변수
    * 서비스 종속 항목
  
* 배치 정책 관리

  * 다음을 기준으로 빠르게 찾고 필터링할 수 있음:
    * 정책 ID
    * 소유자
    * 레이블
  * exchange에서 모든 서비스 배치
  * 배치 정책에 특성 추가
  * 표현식 빌드를 위한 제한조건 빌더 
  * 제한조건을 JSON으로 직접 작성하기 위한 고급 모드
  * 롤백 배치 버전 및 노드 성능 상태 설정을 조정하는 기능
  * 다음을 포함하는 정책 세부사항 보기 및 편집:
    * 서비스 및 배치 특성
    * 제한조건
    * 롤백
    * 노드 상태 설정
  
