---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Passport Advantage
{: #part_numbers}

{{site.data.keyword.ieam}} 패키지를 다운로드하려면 다음 프로시저를 완료하십시오.

1. {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 부품 번호를 찾으십시오.
2. [Passport Advantage](https://www.ibm.com/software/passportadvantage/)의 IBM Passport Advantage 온라인 탭으로 이동하여 IBM ID로 로그인하십시오.
2. [{{site.data.keyword.ieam}} 패키지 및 부품 번호](#part_numbers_table)에 나열된 부품 번호를 사용하여 파일을 검색하십시오.
3. 컴퓨터의 디렉토리로 파일을 다운로드하십시오.

## {{site.data.keyword.ieam}} 패키지 및 부품 번호
{: #part_numbers_table}

|부품 설명|Passport Advantage 부품 번호|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} Resource Value Unit 라이센스 + SW 구독 & 지원 12개월|D2840LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit 연간 SW S&S 갱신 12개월|E0R0HLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit 연간 SW S&S 복원 12개월|D2841LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit 월간 라이센스|D283ZLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit 약정 기간 라이센스|D28I1LL|
{: caption="표 1. {{site.data.keyword.ieam}} 패키지 및 부품 번호" caption-side="top"}

## Licensing
{: #licensing}

라이센싱 요구사항은 등록된 노드 총계를 기반으로 계산됩니다. 관리 허브로 인증하도록 구성된 **hzn** CLI를 설치한 시스템에서 등록된 노드 총계를 판별하십시오.

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

출력은 정수입니다. 다음 샘플 출력을 참조하십시오.

  ```
  $ hzn exchange status | jq .numberOfNodes   2641
  ```

[{{site.data.keyword.ieam}} 라이센스 문서](https://ibm.biz/ieam-43-license)에서 다음 변환 테이블을 사용하여 이전 명령에서 사용자 환경에 대해 리턴된 노드 수를 사용하여 필수 라이센스를 계산하십시오.

  ```
  From 1 to 10 Resources, 1.00 UVU per Resource   From 11 to 50 Resources, 10.0 UVUs plus 0.87 UVUs per Resource above 10   From 51 to 100 Resources, 44.8 UVUs plus 0.60 UVUs per Resource above 50   From 101 to 500 Resources, 74.8 UVUs plus 0.25 UVUs per Resource above 100   From 501 to 1,000 Resources, 174.8.0 UVUs plus 0.20 UVUs per Resource above 500   From 1,001 to 10,000 Resources, 274.8 UVUs plus 0.07 UVUs per Resource above 1,000   From 10,001 to 25,000 Resources, 904.8 UVUs plus 0.04 UVUs per Resource above 10,000   From 25,001 to 50,000 Resources, 1,504.8 UVUs plus 0.03 UVUs per Resource above 25,000   From 50,001 to 100,000 Resources, 2,254.8 UVUs plus 0.02 UVUs per Resource above 50,000   For more than 100,000 Resources, 3,254.8 UVUs plus 0.01 UVUs per Resource above 100,000
  ```

다음 예에서는 **2641**개의 노드에 필요한 라이센스를 계산하는 과정을 안내합니다. 이 경우 **최소 390개**의 라이센스를 구매해야 합니다.

  ```
  274.8 + ( .07 * ( 2641 - 1000 ) )
  274.8 + ( .07 * 1641 )   274.8 + 114.87   389.67
  ```

## 라이센스 보고

{{site.data.keyword.edge_notm}} 사용률은 자동으로 계산되고 클러스터에 로컬로 설치된 공통 라이센싱 서비스에 주기적으로 업로드됩니다. 현재 사용량을 보는 방법을 포함하여 라이센싱 서비스에 대한 자세한 정보를 보려면 사용량 보고서를 생성하고 [라이센싱 서비스 문서](https://www.ibm.com/docs/en/cpfs?topic=operator-overview)를 참조하십시오.
