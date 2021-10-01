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

Intel에 의해 작성된 [SDO](https://software.intel.com/en-us/secure-device-onboard)(Secure Device Onboard)는 에지 디바이스를 쉽고 안전하게 구성하고 에지 관리 허브와 연관시키도록 합니다. 에이전트가 디바이스에 설치되고 자동으로(단순히 디바이스에 전원 공급) {{site.data.keyword.ieam}} 관리 허브에 등록되도록 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}})에서 SDO 사용 디바이스를 지원합니다.

## SDO 개요
{: #sdo-overview}

SDO은 다음 컴포넌트로 구성됩니다.

* 에지 디바이스의 SDO 모듈(일반적으로 디바이스 제조업체에서 설치)
* 소유권 바우처(물리적 디바이스와 함께 디바이스 구매자에게 제공되는 파일)
* SDO 랑데부 서버(처음 시작할 때 SDO 사용 디바이스가 처음으로 접속하는 잘 알려진 서버)
* SDO 소유자 서비스(이 특정한 {{site.data.keyword.ieam}}의 이 특정 인스턴스를 사용하도록 디바이스를 구성하는 {{site.data.keyword.ieam}} 관리 허브로 실행되는 서비스)

**참고**: SDO는 에지 클러스터가 아니라, 에지 디바이스만 지원합니다.

### SDO 플로우

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO installation overview">

## 시작하기 전에
{: #before_begin}

SDO에서는 에이전트 파일이 {{site.data.keyword.ieam}} CSS(Cloud Sync Service)에 저장되어야 합니다. 아직 수행되지 않은 경우 [에지 노드 파일 수집](../hub/gather_files.md)의 설명에 따라 다음 명령 중 하나를 실행하도록 관리자에게 요청하십시오.

  `edgeNodeFiles.sh ALL -c ...`

## SDO 시도
{: #trying-sdo}

SDO 사용 에지 디바이스를 구매하기 전에 SDO 사용 디바이스를 시뮬레이션하는 VM으로 {{site.data.keyword.ieam}}에서 SDO 지원을 테스트할 수 있습니다.

1. API 키가 필요합니다. API 키가 아직 없는 경우 API 키 작성을 위한 지시사항은 [API 키 작성](../hub/prepare_for_edge_nodes.md) 을 참조하십시오.

2. 이러한 환경 변수 값을 가져오려면 {{site.data.keyword.ieam}} 관리자에게 문의하십시오. (다음 단계에서 이 값이 필요합니다.)

   ```bash
   export HZN_ORG_ID=<exchange-org>    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>    export HZN_SDO_SVC_URL=https://<ieam-mgmt-hub-ingress>/edge-sdo-ocs/api    export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>    export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. SDO가 {{site.data.keyword.ieam}} 에이전트를 디바이스에 자동으로 설치하고 {{site.data.keyword.ieam}} 관리 허브에 등록하는지 관찰하려면 [open-horizon/SDO-support 저장소](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md)의 단계를 수행하십시오.

## {{site.data.keyword.ieam}} 도메인에 SDO 기반 디바이스 추가
{: #using-sdo}

SDO 지원 디바이스를 구매했으면 {{site.data.keyword.ieam}} 도메인에 통합하려는 경우:

1. [ {{site.data.keyword.ieam}} 관리 콘솔](../console/accessing_ui.md)에 로그인하십시오.

2. **노드** 탭에서 **노드 추가**를 클릭하십시오. 

   SDO 서비스에서 개인 소유권 키를 작성하고 해당 공개 키를 다운로드하는 데 필요한 정보를 입력하십시오.
   
3. 디바이스를 구매할 때 받은 소유권 바우처를 가져오려면 필수 정보를 입력하십시오.

4. 네트워크에 디바이스를 연결하고 전원을 공급하십시오.

5. 관리 콘솔에서 **노드** 개요 페이지를 보고 설치 이름을 필터링하여 온라인으로 제공되는 디바이스의 진행 상태를 확인하십시오.
