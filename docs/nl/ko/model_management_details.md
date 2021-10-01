---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# 모델 관리 시스템
{: #model_management_details}

모델 관리 시스템(MMS)은 에지 노드에서 실행하는 코그너티브 서비스에 대한 인공 지능(AI) 모델 관리의 부담을 덜어줍니다. 또한 MMS를 사용하여 다른 데이터 파일 유형을 에지 노드에 전달할 수 있습니다. MMS는 에지 서비스에서 필요한 모델, 데이터 및 기타 메타데이터 패키지의 스토리지, 전달 및 보안을 용이하게 합니다. 이것은 에지 노드가 클라우드로 및 클라우드로부터 모델과 메타데이터를 쉽게 전송 및 수신할 수 있게 합니다.

MMS는 {{site.data.keyword.edge_notm}}({{site.data.keyword.ieam}}) 허브 및 에지 노드에서 실행합니다. CSS(Cloud Sync Service)가 조직 내의 특정 노드 또는 노드 그룹에 모델, 메타데이터 또는 데이터를 전달합니다. 오브젝트가 에지 노드로 전달된 후, 에지 서비스가 ESS(Edge Sync Service)로부터 모델이나 데이터를 얻을 수 있게 하는 API를 사용할 수 있습니다.

오브젝트는 서비스 개발자, devops 관리자 및 모델 작성자에 의해 MMS에서 채워집니다. MMS 컴포넌트는 에지에서 실행 중인 AI 모델 도구 및 코그너티브 서비스 사이의 통합을 용이하게 합니다. 작성자가 모델을 완료한 후, 모델이 MMS에 공개되어 에지 노드에 즉시 사용할 수 있게 됩니다. 기본적으로 모델의 무결성은 모델을 해시 및 서명한 다음 모델을 게시하기 전에 서명 및 확인 키를 업로드하여 보장됩니다. MMS는 서명과 키를 사용하여 업로드된 모델이 변조되지 않았는지를 확인합니다. 이러한 동일한 절차는 MMS가 모델을 에지 노드에 배치할 때에도 사용됩니다.

{{site.data.keyword.ieam}}은 또한 모델 오브젝트 및 해당 메타데이터의 조작을 가능하게 하는 CLI(**hzn mms**)를 제공합니다.

다음 다이어그램에서는 MMS를 사용하여 AI 모델을 개발하고 업데이트하는 데 관련된 워크플로우를 보여줍니다.

### MMS에서 AI 모델 개발 및 사용

<img src="../images/edge/02a_Developing_AI_model_using_MMS.svg" style="margin: 3%" alt="MMS를 사용하여 AI 서비스 개발"> 

### MMS에서 AI 모델 업데이트

<img src="../images/edge/02b_Updating_AI_model_using_MMS.svg" style="margin: 3%" alt="MMS를 사용하여 AI 서비스 업데이트"> 

## MMS 개념

여러 가지 컴포넌트, 즉 CSS, ESS 및 오브젝트가 MMS를 구성합니다.

CSS와 ESS는 개발자와 관리자가 MMS와 상호작용하기 위해 사용하는 API를 제공합니다. 오브젝트는 기계 학습 모델 및 에지 노드에 배치되는 다른 유형의 데이터 파일입니다.

### CSS

CSS는 {{site.data.keyword.ieam}}이 설치될 때 {{site.data.keyword.ieam}} 관리 허브에 배치됩니다. CSS는 mongoDB 데이터베이스를 사용하여 오브젝트를 저장하고 각 에지 노드의 상태를 유지보수합니다.

### ESS

ESS는 에지 노드에서 실행하는 {{site.data.keyword.ieam}} 에이전트에 임베드됩니다. ESS는 계속해서 CSS에서 오브젝트 업데이트가 있는지 폴링하고 노드로 전달되는 오브젝트를 에지 노드의 로컬 데이터베이스에 저장합니다. ESS API는 에지 노드에 배치되는 서비스가 메타데이터 및 데이터 또는 모델 오브젝트에 액세스할 때 사용할 수 있습니다.

### 오브젝트(메타데이터 및 데이터)

메타데이터는 데이터 모델을 설명합니다. 오브젝트는 메타데이터와 데이터 또는 메타데이터만을 갖고 MMS에 공개됩니다. 메타데이터에서, **objectType** 및 **objectID** 필드가 주어진 조직 내에서 오브젝트의 ID를 정의합니다. 이런 목적지 관련 필드가 오브젝트를 전송할 에지 노드를 판별합니다.

* **destinationOrgID**
* **destinationType**
* **destinationID**
* **destinationList**
* **destinationPolicy**

기타 오브젝트 정보에는 메타데이터에서 지정할 수 있는 설명, 버전 등이 포함됩니다. 버전 값은 동기화 서비스에 시맨틱 의미가 없습니다. 그러므로 오브젝트의 단 하나의 사본이 CSS에 존재합니다.

데이터 파일은 코그너티브 서비스에서 사용하는 ML 특정 모델 정의가 포함되는 파일입니다. 모든 모델 파일, 구성 파일 및 2진 데이터가 데이터 파일의 예입니다.

### AI 모델

AI(Artificial Intelligence) 모델은 MMS 특정 개념이 아니지만 MMS의 주요 유스 케이스입니다. AI 모델은 AI와 관련된 실세계 프로세스의 수학적 표시입니다. 사람의 코그너티브 기능을 흉내내는 코그너티브 서비스가 AI 모델을 사용하고 소비합니다. AI 모델을 생성하려면 실습용 데이터에 AI 알고리즘을 적용하십시오. 요약하면, AI 모델은 MMS에 의해 분배되고 에지 노드에서 실행하는 코그너티브 서비스에 의해 사용됩니다.

## {{site.data.keyword.ieam}}의 MMS 개념

MMS 개념과 {{site.data.keyword.ieam}}의 기타 개념 사이에 특정한 관계가 존재합니다.

{{site.data.keyword.ieam}}은 패턴 또는 정책으로 노드를 등록할 수 있습니다. 오브젝트의 메타데이터를 작성하는 경우, 오브젝트 메타데이터의 **destinationType** 필드를 이 오브젝트를 반드시 수신해야 하는 패턴 이름으로 설정하십시오. 동일한 패턴을 사용하는 모든 {{site.data.keyword.ieam}} 노드는 동일한 그룹에 있는 것으로 생각될 수 있습니다. 그러므로, 이 맵핑은 주어진 유형의 모든 노드에 대한 대상 오브젝트로 만들 수 있습니다. **destinationID** 필드는 {{site.data.keyword.ieam}} 에지 노드 노드 ID와 동일합니다. **destinationID** 메타데이터 필드를 설정하지 않는 경우 오브젝트는 패턴(**destinationType**)을 갖는 모든 노드에 브로드캐스트됩니다.

정책에 등록된 노드로 전달되어야 하는 오브젝트에 대한 메타데이터를 작성할 때 **destinationType** 및 **destinationID**를 공백으로 두고 대신 **destinationPolicy** 필드를 설정하십시오. 이 필드는 오브젝트를 수신하는 노드를 정의하는 목적지 정보(정책 특성, 제한조건 및 서비스)를 보유합니다. 오브젝트를 처리하는 서비스를 표시하도록 **services** 필드를 설정하십시오. **properties** 및 **constraints** 필드는 선택사항이며 오브젝트를 수신하는 노드를 추가로 좁히는 데 사용됩니다.

에지 노드는 해당 노드에서 실행하는 여러 서비스를 가질 수 있는데, 이들은 서로 다른 엔티티에 의해 개발되었을 수 있습니다. {{site.data.keyword.ieam}} 에이전트 인증 및 권한 부여 계층이 주어진 오브젝트에 액세스할 수 있는 서비스를 제어합니다. 정책을 통해 배치된 오브젝트는 **destinationPolicy**에서 참조되는 서비스에만 보입니다. 그러나, 패턴을 실행하는 노드에 배치된 오브젝트는 이 수준의 격리를 사용할 수 없습니다. 패턴을 사용하는 노드에서 해당 노드에 전달되는 모든 오브젝트는 노드의 모든 서비스에 표시됩니다.

## MMS CLI 명령

이 절은 MMS 예제를 설명하고 일부 MMS 명령 사용 방법을 설명합니다.

예를 들어 사용자는 기계 학습 서비스(**weaponDetector**)가 배치된 세 개의 카메라를 작동시켜 무기를 운반하는 사용자를 식별합니다. 이 모델은 이미 훈련되었고, 서비스가 카메라(노드로 작용)에서 실행 중입니다.

### MMS 상태 검사

모델을 공개하기 전에, **hzn mms status** 명령을 실행하여 MMS 상태를 검사하십시오. **general** 아래의 **heathStatus** 및 **dbHealth** 아래의 **dbStatus**를 검사하십시오. 이들 필드의 값은 CSS 및 데이터베이스가 실행 중임을 나타내는 초록색이어야 합니다.

```
$ hzn mms status {   "general": {     "nodeType": "CSS",     "healthStatus": "green",     "upTime": 21896   },   "dbHealth": {     "dbStatus": "green",     "disconnectedFromDB": false,     "dbReadFailures": 0,     "dbWriteFailures": 0   }
}
```
{: codeblock}

### MMS 오브젝트 작성

MMS에서 데이터 모델 파일은 독립적으로 공개되지 않습니다. MMS는 공개 및 배포를 위해 데이터 모델 파일과 함께 메타데이터 파일을 필요로 합니다. 메타데이터 파일은 데이터 모델에 대한 속성 세트를 구성합니다. MMS는 메타데이터에 정의되는 속성을 기반으로 모델 오브젝트를 저장, 분배 및 검색합니다.

메타데이터 파일은 json 파일입니다.

1. 메타데이터 파일의 템플리트 보기:

   ```
   hzn mms object new
   ```
   {: codeblock}
2. **my_metadata.json**이라는 파일에 템플리트 복사:

   ```
   hzn mms object new >> my_metadata.json
   ```
   {: codeblock}

   다른 방법으로는, 터미널에서 템플리트를 복사하고 이를 파일에 붙여넣을 수 있습니다.

메타데이터 필드의 의미와 이들이 메타데이터 예제와 관련되는 방법을 이해하는 것이 중요합니다.

|필드|설명|참고|
|-----|-----------|-----|
|**objectID**|오브젝트 ID.|조직 내에서 오브젝트의 필수 고유 ID입니다.|
|**objectType**|오브젝트 유형.|사용자가 정의하는 필수 필드로서, 기본 제공 오브젝트 유형이 아닙니다.|
|**destinationOrgID**|목적지 조직.|동일한 조직 내에서 오브젝트를 노드에 분배하는 데 사용되는 필수 필드입니다.|
|**destinationType**|목적지 유형.|이 오브젝트를 수신해야 하는 노드가 사용하는 패턴입니다.|
|**destinationID**|목적지 ID.|오브젝트가 배치되어야 하는 단일 노드 ID(org 접두부 없음)로 설정되는 선택적 필드입니다. 생략되는 경우 오브젝트는 destinationType 내의 모든 노드로 전송됩니다.|
|**destinationsList**|목적지 목록.|이 오브젝트를 수신할 pattern:nodeId 쌍의 배열로서 설정되는 대상 선택적 필드입니다. 이것은 **destinationType** 및 **destinationID** 설정의 대안입니다.|
|**destinationPolicy**|목적지 정책.|오브젝트를 정책으로 등록된 노드에 분배할 때 사용하십시오. 이 경우에는 **destinationType**, **destinationID** 또는 **destinationsList**를 설정하지 마십시오.|
|**expiration**|선택적 필드.|오브젝트가 만기하고 MMS에서 제거될 시간을 표시합니다.|
|**activationTime**|선택적 필드.|이 오브젝트가 자동으로 활성화할 날짜입니다. 활성화 시간 이후까지 어떤 노드로도 전달되지 않습니다.|
|**버전**|선택적 필드.|임의의 문자열 값입니다. The value is not semantically interpreted. 모델 관리 시스템은 오브젝트의 여러 버전을 보관하지 않습니다.| 
|**설명**|선택적 필드.|임의의 설명입니다.|

참고:

1. **destinationPolicy**를 사용하는 경우 메타데이터에서 **destinationType**, **destinationID** 및 **destinationsList** 필드를 제거하십시오. **destinationPolicy** 내부의 **특성**, **제한조건** 및 **서비스**는 이 오브젝트를 수신할 대상을 판별합니다.
2. **version** 및 **description**은 메타데이터 내에서 문자열로서 주어질 수 있습니다. 버전의 값이 시맨틱적으로 해석되지 않습니다. MMS는 한 오브젝트의 다중 버전을 보존하지 않습니다.
3. **expiration** 및 **activationTime**은 RFC3339 형식으로 제공되어야 합니다.

다음 두 옵션 중 하나를 사용하여 **my_metadata.json**의 필드를 채우십시오.

1. 정책과 함께 실행하는 에지 노드로 MMS 오브젝트를 전송하십시오.

   이 예제에서 카메라 에지 노드 node1, node2 및 node3은 정책에 등록됩니다. **weaponDetector**는 노드에서 실행 중인 서비스 중 하나이며, 사용자의 모델 파일이 카메라 에지 노드에서 실행 중인 **weaponDetector** 서비스에 의해 사용되기 원합니다. 대상 노드가 정책으로 등록되기 때문에, **destinationOrgID** 및 **destinationPolicy**만 사용하십시오. **ObjectType** 필드를 **model**로 설정하십시오. 그러나 오브젝트를 검색하는 서비스에 의미가 있는 임의의 문자열로 설정될 수 있습니다.

   이 시나리오에서 메타데이터 파일은 다음과 같을 수 있습니다.

   ```json
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationPolicy": {        "properties": [],        "constraints": [],        "services": [          {            "orgID": "$SERVICE_ORG_ID",            "arch": "$ARCH",            "serviceName": "weaponDetector",            "version": "$VERSION"          }        ]      },      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

2. 패턴과 함께 실행하는 에지 노드로 MMS 오브젝트를 전송하십시오.

   이 시나리오에서는 동일한 노드가 사용되지만, 이제 이들은 패턴 **pattern.weapon-detector**으로 등록되며 **weaponDetector**를 서비스 중 하나로 갖습니다.

   패턴을 갖는 노드로 모델을 전송하려면 메타데이터 파일을 변경하십시오.

   1. **destinationType** 필드에서 노드 패턴을 지정하십시오.
   2. **destinationPolicy** 필드를 제거하십시오.

   메타데이터 파일은 다음과 비슷합니다.

   ```
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationType": "pattern.weapon-detector",      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

이제, 모델 파일과 메타데이터 파일을 공개할 준비가 되었습니다.

### MMS 오브젝트 공개

메타데이터 및 데이터 파일 모두와 함께 오브젝트를 공개하십시오.

```
hzn mms object publish -m my_metadata.json -f my_model
```
{: codeblock}

### MMS 오브젝트 나열

주어진 조직 내에서 이 **objectID** 및 **objectType**을 갖는 MMS 오브젝트를 나열하십시오.

```
hzn mms object list --objectType=model --objectId=my_model
```
{: codeblock}

다음은 명령의 결과와 비슷합니다.

```
Listing objects in org userdev: [   {     "objectID": "my_model",     "objectType": "model"   }
]
```

모든 MMS 오브젝트 메타데이터를 표시하려면 명령에 **-l**을 추가하십시오.

```
hzn mms object list --objectType=model --objectId=my_model -l
```
{: codeblock}

오브젝트와 함께 오브젝트 상태 및 목적지를 표시하려면 명령에 **-d**를 추가하십시오. 다음 목적지 결과는 오브젝트가 카메라 node1, node2 및 node3으로 전달됨을 표시합니다.

```
hzn mms object list --objectType=model --objectId=my_model -d
```
{: codeblock}

이전 명령의 출력은 다음과 유사합니다.

```
[   {     "objectID": "my_model",     "objectType": "model",     "destinations": [       {         "destinationType": "pattern.mask-detector",         "destinationID": "node1",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node2",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node3",         "status": "delivered",         "message": ""       },     ],     "objectStatus": "ready"   }
]
```

고급 필터링 옵션을 추가로 사용하여 MMS 오브젝트 목록을 좁힐 수 있습니다. 플래그의 전체 목록을 보려면 다음을 수행하십시오.

```
hzn mms object list --help
```
{: codeblock}

### MMS 오브젝트 삭제

MMS 오브젝트를 삭제하십시오.

```
hzn mms object delete --type=model --id=my_model
```
{: codeblock}

오브젝트가 MMS에서 제거됩니다.

### MMS 오브젝트 업데이트

모델은 시간에 따라 변할 수 있습니다. 업데이트된 모델을 공개하려면 **hzn mms object publish**를 동일한 메타데이터 파일과 함께 사용하십시오(버전 값 **upgrade**가 권장됨). MMS에서 세 개의 카메라 모두에 대해 모델을 하나씩 업데이트할 필요는 없습니다. 세 노드 모두에서 **my_model** 오브젝트를 업데이트하려면 다음을 사용하십시오.

```
hzn mms object publish -m my_metadata.json -f my_updated_model
```
{: codeblock}

## 부록

참고: 명령 구문에 대한 자세한 정보는 [이 문서에서 사용된 규칙](../getting_started/document_conventions.md)을 참조하십시오.

다음은 MMS 오브젝트 메타데이터의 템플리트를 생성하는 데 사용되는 **hzn mms object new** 명령의 출력 예입니다.

```
{     "objectID": "",            /* Required: A unique identifier of the object. */   "objectType": "",          /* Required: The type of the object. */   "destinationOrgID": "$HZN_ORG_ID", /* Required: The organization ID of the object (an object belongs to exactly one organization). */   "destinationID": "",       /* The node id (without org prefix) where the object should be placed. */                              /* If omitted the object is sent to all nodes with the same destinationType. */                              /* Delete this field when you are using destinationPolicy. */   "destinationType": "",     /* The pattern in use by nodes that should receive this object. */                              /* If omitted (and if destinationsList is omitted too) the object is broadcast to all known nodes. */                              /* Delete this field when you are using policy. */   "destinationsList": null,  /* The list of destinations as an array of pattern:nodeId pairs that should receive this object. */                              /* If provided, destinationType and destinationID must be omitted. */                              /* Delete this field when you are using policy. */   "destinationPolicy": {     /* The policy specification that should be used to distribute this object. */                              /* Delete these fields if the target node is using a pattern. */     "properties": [          /* A list of policy properties that describe the object. */       {         "name": "",         "value": null,         "type": ""           /* Valid types are string, bool, int, float, list of string (comma separated), version. */                              /* Type can be omitted if the type is discernable from the value, e.g. unquoted true is boolean. */       }     ],     "constraints": [         /* A list of constraint expressions of the form <property name> <operator> <property value>, separated by boolean operators AND (&&) or OR (||). */       ""     ],     "services": [            /* The service(s) that will use this object. */       {         "orgID": "",         /* The org of the service. */         "serviceName": "",   /* The name of the service. */         "arch": "",          /* Set to '*' to indcate services of any hardware architecture. */         "version": ""        /* A version range. */       }     ]   },   "expiration": "",          /* A timestamp/date indicating when the object expires (it is automatically deleted). The time stamp should be provided in RFC3339 format.  */   "version": "",             /* Arbitrary string value. The value is not semantically interpreted. The Model Management System does not keep multiple version of an object. */   "description": "",         /* An arbitrary description. */   "activationTime": ""       /* A timestamp/date as to when this object should automatically be activated. The timestamp should be provided in RFC3339 format. */ }
```
{: codeblock}

## 예제
{: #mms}

이 예는 모델 관리 시스템(MMS)를 사용하는 {{site.data.keyword.edge_service}} 개발 방법을 학습하는 데 도움이 됩니다. 이 시스템을 사용하여 에지 노드에서 실행되는 에지 서비스가 사용하는 학습 머신 모델을 배치하고 업데이트할 수 있습니다.
{:shortdesc}

MMS를 사용하는 예제는 [Horizon Hello 모델 관리 서비스(MMS) 예제 에지 서비스](https://github.com/open-horizon/examples/tree/master/edge/services/helloMMS)를 참조하십시오.

## 시작하기 전에
{: #mms_begin}

[에지 서비스 작성 준비](service_containers.md)의 전제조건 단계를 완료하십시오. 결과적으로 해당 환경 변수를 설정해야 하고 해당 명령을 설치해야 하며 해당 파일이 있어야 합니다.

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## 프로시저
{: #mms_procedure}

이 예제는 [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) 오픈 소스 프로젝트의 일부입니다. [고유한 Hello MMS 에지 서비스 작성](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)의 단계를 수행한 후 여기로 돌아오십시오.

## 다음에 수행할 작업
{: #mms_what_next}

* [디바이스를 위한 에지 서비스 개발](developing.md)에서 다른 에지 서비스 예제를 시도해 보십시오.

## 추가 정보

* [모델 관리를 사용하는 Hello world](model_management_system.md)
