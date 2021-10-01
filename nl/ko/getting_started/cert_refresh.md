---

copyright:
  years: 2021
lastupdated: "2021-02-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 인증서 새로 고치기
{: #certrefresh}

{{site.data.keyword.ieam}} 설치의 일부로 설치된 {{site.data.keyword.common_services}} 버전에 따라 인증서가 자동 갱신으로 이어지는 짧은 수명으로 작성되었을 수 있습니다.

{{site.data.keyword.ieam}} 설치 클러스터에 로그인하고 다음을 실행하여 {{site.data.keyword.common_services}}의 현재 버전을 유효성 검증하십시오.
```
$ oc get csv -A | grep -E 'ibm-common-service-operator|NAME' NAMESPACE NAME DISPLAY VERSION REPLACES PHASE ibm-common-services ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-Common-service-operator.v3.6.3 Succeeded ibm-edge ibm-common-service-operator.v3.6.4 IBM Cloud Platform Common Services 3.6.4 ibm-common-service-operator.v3.6.3 Succeeded
```

동일한 연산자의 두 인스턴스(최소한)가 표시되어야 합니다. `ibm-common-services` 네임스페이스의 인스턴스 및 {{site.data.keyword.ieam}} 설치 네임스페이스의 인스턴스입니다. 두 버전이 일치하고 버전이 `3.6.4` 이상인지 확인하십시오. 버전이 일치하지 않거나 이전 버전인 경우 수동으로 등록 업데이트를 설정한 경우 {{site.data.keyword.open_shift}} 콘솔을 참조하거나 이전 업그레이드 시도로 인해 존재할 수 있는 기본 문제를 판별하십시오.

인증서가 자동으로 갱신된 경우 {{site.data.keyword.ieam}}에서 새 인증서를 적절하게 사용하는지 확인하려면 수동 조치가 필요합니다.
1. 새 인증서를 가져오고 {{site.data.keyword.ieam}} 리소스를 새로 고치십시오.
2. 인증서를 제공하고 아래의 에지 노드 지시사항을 에지 노드 소유자와 통신하여 이 새 인증서를 각 에지 노드에 적용해야 함을 알리십시오.

## 태스크 1: 새 인증서를 가져오고 {{site.data.keyword.ieam}} 리소스를 새로 고치십시오.
{: #task1}
1. 클러스터 관리자로 {{site.data.keyword.ieam}} 허브가 설치된 클러스터에 로그인하십시오. 기존 인증서에 대한 작성 및 만료 날짜를 유효성 검증하십시오.
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}

   **참고**: 작성 날짜가 통신 문제가 시작된 시간과 일치하지 않는 경우 문제점은 인증서 갱신 때문이 아닐 수 있으므로 이 프로세스의 나머지 부분을 진행하지 않아야 합니다.

2. 새 인증서를 파일로 내보내십시오.
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

3. {{site.data.keyword.ieam}} Exchange 및 SDO 팟(Pod)을 새로 고치십시오(이로 인해 잠시 동안 {{site.data.keyword.ieam}} 통신이 중단됨).
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge    oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

4. CSS 설치 **agent_files**를 새 인증서로 새로 고치십시오. 그러면 향후 에지 노드 설치가 새 인증서를 신뢰합니다.
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json    hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}

   모든 에지 노드 소유자에게 알리십시오. 일반 사용자가 새 인증서로 해당 노드를 구성할 수 있도록 하려면 이 인증서 파일의 사본과 [태스크 2](cert_refresh.md#task2) 지시사항에 대한 직접 링크를 포함시키십시오.

## 태스크 2: 새 인증서를 에지 노드에 적용
{: #task2}
### 에지 디바이스의 경우
1. 호스트에 로그인하여 새 인증서 파일을 수동으로 대체하거나 다음 명령을 실행하십시오(&amp;TWBLT;DEVICE_HOST&gt;를 노드 호스트 이름 또는 IP로 대체하고 &amp;TWBLT;CA_CERT_FILE&gt;을 지정된 인증서 파일의 위치로 대체).
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' > \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. 이전 인증서가 대체되었는지 유효성 검증하십시오.
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### 에지 클러스터의 경우
1. 에이전트 POD가 실행 중인 네임스페이스에 로그인하여 기존의 만료된 인증서를 대체하십시오(&amp;TWBLT;CA_CERT_FILE&gt;을 새 인증서를 포함하고 있는 지정된 파일의 위치로 대체).
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat &amp;TWBLT;CA_CERT_FILE&gt; | base64 | tr -d '\n')'"}}'
   ```
   {: codeblock}

2. 시크릿이 업데이트되었는지 유효성 검증하십시오.
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

3. {{site.data.keyword.ieam}} 에이전트 팟(Pod)을 다시 시작하십시오.
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}
