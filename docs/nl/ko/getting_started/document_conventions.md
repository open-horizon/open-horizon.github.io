---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 이 문서에서 사용된 규칙
{: #document_conventions}

이 문서는 특정 의미를 전달하기 위해 컨텐츠 규칙을 사용합니다.  

## 명령 규칙

< >에 표시된 변수 컨텐츠를 사용자의 필요에 따른 값으로 대체하십시오. 명령에 < > 문자를 포함시키지 마십시오.

### 예제

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
   
## 리터럴 문자열

관리 허브 또는 코드에서 표시되는 컨텐츠는 리터럴 문자열입니다. 이 컨텐츠는 **굵은체** 텍스트로 표시됩니다.
   
 ### 예제
   
 `service.sh` 코드를 검사하면 해당 작동을 제어하기 위해 해당 리터럴 문자열 및 기타 구성 변수를 사용함을 알 수 있습니다. **PUBLISH**는 코드가 IBM Event Streams에 메시지를 전송하려고 시도하는지 여부를 제어합니다. **MOCK**는 service.sh가 REST API 및 해당 종속 서비스(cpu 및 gps)에 접속하려고 시도하는지 여부 및 `service.sh`가 허위 데이터를 작성하는지 여부를 제어합니다.
  
