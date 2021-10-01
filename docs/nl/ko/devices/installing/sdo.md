---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# SDO 에이전트 설치 및 등록
{: #sdo}

**기술 미리보기**: 현재 SDO 지원은 SDO 프로세스를 테스트하고
향후 사용을 계획하기 위해 익히는 용도로만 사용해야 합니다. 향후 릴리스에서는 SDO 지원을
프로덕션 용도로 사용할 수 있습니다.

[SDO ![새 탭에서열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://software.intel.com/en-us/secure-device-onboard)(Secure Device Onboard)는 쉽고 안전하게 에지 디바이스를 구성하고 에지 관리 허브와

연관시키기 위해 Intel에서 작성한 기술입니다. 디바이스에 에이전트를 설치하고 자동으로(단순히 디바이스에
전원 공급) {{site.data.keyword.ieam}} 관리 허브에 등록하도록 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서
SDO 사용 디바이스 지원을 추가했습니다.

## SDO 개요
{: #sdo-overview}

SDO은 다음 네 개의 컴포넌트로 구성됩니다.

1. 에지 디바이스의 SDO 모듈(일반적으로 디바이스 제조업체에서 설치)
2. 소유권 바우처(물리적 디바이스와 함께 디바이스 구매자에게 제공되는 파일)
3. SDO 랑데부 서버(처음 부팅할 때 SDO 사용 디바이스가 처음으로 접속하는 잘 알려진 서버)
4. SDO 소유자 서비스(이 특정한 {{site.data.keyword.ieam}} 서비스에 디바이스를 연결하는
{{site.data.keyword.ieam}} 관리 허브로 실행되는 서비스)

### 기술 미리보기의 차이점
{: #sdo-tech-preview-differences}

- **SDO 사용 디바이스:** SDO 테스트용으로 VM에 SDO 모듈을 추가하도록
스크립트가 제공되므로, 부팅 시 SDO 사용 디바이스와 동일한 방식으로 작동합니다. 따라서 SDO 사용 디바이스를 구매하지 않아도 {{site.data.keyword.ieam}}과의 SDO 통합을 테스트할 수 있습니다.
- **소유권 바우처:** 일반적으로 디바이스 제조업체로부터 소유권 바우처를 받습니다. 이전 글머리 기호에서 언급된 스크립트를 사용하여 VM에 SDO 모듈을 추가하는 경우 VM에도 소유권 바우처를
작성합니다. VM에서 이 바우처를 복사하면 "디바이스 제조업체로부터 소유권 바우처를 받는 것"입니다.
- **랑데부 서버:** 프로덕션에서 부팅 디바이스가 Intel의 글로벌 SDO 랑데부 서버에 접속합니다. 이 기술 미리보기의 개발 및 테스트용으로 SDO 소유자 서비스에 번들되어 있는 개발 랑데부 서버를 사용합니다.
- **SDO 소유자 서비스:** 이 기술 미리보기에서 SDO 소유자 서비스는 {{site.data.keyword.ieam}} 관리 허브에 자동으로
설치되지 않습니다. 대신 {{site.data.keyword.ieam}} 관리 허브에 대한 네트워크 액세스 권한이 있으며 SDO 디바이스가
네트워크를 통해 연결할 수 있는 서버에서 SDO 소유자 서비스를 시작하는 편리한 스크립트를 제공합니다.

## SDO 사용
{: #using-sdo}

SDO를 사용해 보고 {{site.data.keyword.ieam}} 에이전트를 자동으로 설치하여 {{site.data.keyword.ieam}} 관리 허브에 등록하는지 보려면
[open-horizon/SDO-support repository ![새 탭에서 열림](../../images/icons/launch-glyph.svg "새 탭에서 열림")](https://github.com/open-horizon/SDO-support/blob/master/README.md)의 단계를 따르십시오.
