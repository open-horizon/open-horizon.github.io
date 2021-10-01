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

# モデル管理システム
{: #model_management_details}

モデル管理システム (MMS) は、エッジ・ノード上で実行されるコグニティブ・サービス用の人工知能 (AI) モデル管理の負担を軽減します。 MMS は、他のデータ・ファイル・タイプをエッジ・ノードに送信するためにも使用できます。 MMS は、エッジ・サービスが必要とする、モデル、データ、およびその他のメタデータ・パッケージの保管、送信、およびセキュリティーを容易にします。 これにより、エッジ・ノードはクラウドとの間でモデルおよびメタデータの送受信を簡単に行えるようになります。

MMS は {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ハブおよびエッジ・ノード上で実行されます。 クラウド同期サービス (CSS) は、組織内の特定のノードまたはノード・グループに、モデル、メタデータ、またはデータを配信します。 オブジェクトがエッジ・ノードに送信された後、エッジ・サービスがエッジ同期サービス (ESS) からモデルやデータを取得することを可能にする API が使用可能になります。

オブジェクトは、サービス開発者、DevOps 管理者、およびモデル作成者によって、MMS に取り込まれます。 MMS のコンポーネントは、AI モデル・ツールとエッジ上で実行されるコグニティブ・サービスとの間の連携を促進します。 作成者がモデルを完成させると、モデルは MMS に公開され、それらは即時にエッジ・ノードで使用できるようになります。デフォルトでは、モデルの公開前に、モデルをハッシュして署名し、署名と検証鍵をアップロードすることでモデルの保全性が保証されます。MMS は署名と鍵を使用して、アップロードされたモデルが改ざんされていないことを確認します。MMS がモデルをエッジ・ノードにデプロイする際にも、これと同じ手順が使用されます。

{{site.data.keyword.ieam}} には、モデル・オブジェクトおよびそのメタデータを操作できる CLI (**hzn mms**) もあります。

以下の図は、MMSを使用した AI モデルの開発および更新に関連するワークフローを示しています。

### MMS を使用した AI モデルの開発および使用

<img src="../images/edge/02a_Developing_AI_model_using_MMS.svg" style="margin: 3%" alt="MMS を使用した AI サービスの開発"> 

### MMS を使用した AI モデルの更新

<img src="../images/edge/02b_Updating_AI_model_using_MMS.svg" style="margin: 3%" alt="MMS を使用した AI サービスの更新"> 

## MMS の概念

MMS の構成要素は、CSS、ESS、およびオブジェクトです。

CSS および ESS には、開発者および管理者が MMS と対話するために使用する API があります。 オブジェクトは、機械学習モデルと、エッジ・ノードにデプロイされたその他のタイプのデータ・ファイルです。

### CSS

CSS は、{{site.data.keyword.ieam}} がインストールされるときに {{site.data.keyword.ieam}} 管理ハブにデプロイされます。 CSS は、mongoDB データベースを使用して、オブジェクトを保管し、各エッジ・ノードの状況を保守します。

### ESS

ESS は、エッジ・ノードで実行される {{site.data.keyword.ieam}} エージェントに組み込まれています。 ESS は、オブジェクト更新がないか確認するために CSS を継続的にポーリングし、ノードに送信されたすべてのオブジェクトをエッジ・ノード上のローカル・データベースに保管します。 エッジ・ノードにデプロイされたサービスは、ESS API を使用して、メタデータおよびデータ、またはモデル・オブジェクトにアクセスできます。

### オブジェクト (メタデータおよびデータ)

メタデータは、データ・モデルを記述します。 オブジェクトは、メタデータおよびデータと共に、または、メタデータのみと共に、MMS に公開されます。 メタデータ内の **objectType** フィールドおよび **objectID** フィールドは、特定の組織内のオブジェクトの ID を定義します。 宛先に関する以下のフィールドは、どのエッジ・ノードにオブジェクトを送信するのかを決定します。

* **destinationOrgID**
* **destinationType**
* **destinationID**
* **destinationList**
* **destinationPolicy**

その他のオブジェクト情報 (description、version など) をメタデータ内に指定できます。 version の値には同期サービス向けの意味はなく、CSS に存在するオブジェクトは 1 部のみです。

データ・ファイルは、コグニティブ・サービスによって使用される ML 固有のモデル定義を含むファイルです。 AI モデル・ファイル、構成ファイル、およびバイナリー・データは、データ・ファイルの例です。

### AI モデル

AI (人工知能) モデルは、MMS 固有の概念ではありませんが、MMS の主要なユース・ケースです。 AI モデルは、AI に関連する現実のプロセスを数学的に表現したものです。 人間の認知機能を模倣するコグニティブ・サービスは AI モデルを使用およびコンシュームします。 AI モデルを生成するには、トレーニング・データに AI アルゴリズムを適用します。 要約すると、AI モデルは MMS によって配布され、エッジ・ノードで実行されているコグニティブ・サービスによって使用されます。

## {{site.data.keyword.ieam}} における MMS の概念

{{site.data.keyword.ieam}} において、MMS の概念およびその他の概念の間には特定の関係があります。

{{site.data.keyword.ieam}} は、パターンまたはポリシーを使用してノードを登録できます。 オブジェクトのメタデータを作成するときに、オブジェクトのメタデータ内の **destinationType** フィールドを、このオブジェクトを受信するべきノードのパターン名に設定します。 同じパターンを使用するすべての {{site.data.keyword.ieam}} ノードは、同じグループ内にあると考えることができます。 したがって、このマッピングにより、特定のタイプのすべてのノードをオブジェクトのターゲットにすることができます。 **destinationID** フィールドは、{{site.data.keyword.ieam}} エッジ・ノードのノード ID と同じです。 **destinationID** メタデータ・フィールドが設定されていない場合、オブジェクトはパターン (**destinationType**) を持つすべてのノードに送信されます。

あるポリシーを使用して登録されたすべてのノードに送信される必要のあるオブジェクトのメタデータを作成する場合、**destinationType** と **destinationID** をブランクにし、代わりに、**destinationPolicy** フィールドを設定します。 ここには、オブジェクトをどのノードが受信するのかを定義する宛先情報 (ポリシー・プロパティー、制約、およびサービス) が入れられます。 **services** の各フィールドを設定して、どのサービスがオブジェクトを処理するのかを指示します。 **properties** フィールドおよび **constraints** フィールドはオプションであり、オブジェクトを受信するノードをさらに絞り込むために使用されます。

1 つのエッジ・ノードで複数のサービスを実行することができ、それらのサービスは異なるエンティティーで開発されたものであってもかまいません。 {{site.data.keyword.ieam}} エージェントの認証および許可の層が、どのサービスが特定のオブジェクトにアクセスできるのかを制御します。 ポリシーを介してデプロイされたオブジェクトは、**destinationPolicy** で参照されているサービスにのみ可視になります。 しかし、パターンが実行されているノードにデプロイされたオブジェクトには、このレベルの分離は使用可能ではありません。 パターンを使用しているノードでは、そのノードに送信されるすべてのオブジェクトはそのノード上のすべてのサービスに可視になります。

## MMS CLI コマンド

このセクションでは、MMS の例を示し、いくつかの MMS コマンドの使用方法を説明します。

例えば、武器を携帯している人を識別するための機械学習サービス (**weaponDetector**) がデプロイされた 3 つのカメラをユーザーが運用します。 このモデルは既にトレーニングされていて、サービスはカメラで実行されています (カメラがノードとして機能します)。

### MMS 状況の確認

モデルを公開する前に、**hzn mms status** コマンドを実行して MMS 状況を確認します。 **general** の下の **heathStatus** と、**dbHealth** の下の **dbStatus** を確認してください。 これらのフィールドの値は、CSS およびデータベースが実行中であることを示す「green」でなければなりません。

```
$ hzn mms status
{
  "general": {
    "nodeType": "CSS",
    "healthStatus": "green",
    "upTime": 21896
  },
  "dbHealth": {
    "dbStatus": "green",
    "disconnectedFromDB": false,
    "dbReadFailures": 0,
    "dbWriteFailures": 0
  }
}
```
{: codeblock}

### MMS オブジェクトの作成

MMS では、データ・モデル・ファイルは独立して公開されるのではありません。 MMS では、公開および配布のために、データ・モデル・ファイルと共にメタデータ・ファイルが必要です。 メタデータ・ファイルは、データ・モデルの属性のセットを構成します。 MMS は、メタデータ内に定義された属性に基づいて、モデル・オブジェクトの保管、配布、および取得を行います。

メタデータ・ファイルは json ファイルです。

1. メタデータ・ファイルのテンプレートを表示します。

   ```
   hzn mms object new
   ```
   {: codeblock}
2. テンプレートを **my_metadata.json** という名前のファイルにコピーします。

   ```
   hzn mms object new >> my_metadata.json
   ```
   {: codeblock}

   あるいは、テンプレートを端末からコピーし、ファイルに貼り付けることもできます。

メタデータのフィールドの意味、およびメタデータ例との関係を理解することは重要です。

|フィールド|説明|注記|
|-----|-----------|-----|
|**objectID**|オブジェクト ID。|組織内のオブジェクトの固有 ID を示す必須フィールド。|
|**objectType**|オブジェクト・タイプ。|ユーザーによって定義される必須フィールド。組み込みオブジェクト・タイプはありません。|
|**destinationOrgID**|宛先組織。|同じ組織内のノードにオブジェクトを配布するために使用される必須フィールド。|
|**destinationType**|宛先タイプ。|このオブジェクトを受信するべきノードによって使用されているパターン。|
|**destinationID**|宛先 ID。|オブジェクトが配置されるべき単一ノード ID (組織接頭部なし) に設定されるオプション・フィールド。 省略された場合、オブジェクトは destinationType のすべてのノードに送信されます。|
|**destinationsList**|宛先リスト。|このオブジェクトを受信するべき pattern:nodeId ペアの配列に設定されるオプション・フィールド。 これは、**destinationType** および **destinationID** の設定に代わるものです。|
|**destinationPolicy**|宛先ポリシー。|ポリシーを使用して登録されたノードにオブジェクトを配布するときに使用します。 この場合は、**destinationType**、**destinationID**、**destinationsList** を設定しないでください。|
|**expiration**|オプションのフィールド。|いつオブジェクトの有効期限が切れて MMS から削除されるのかを示します。|
|**activationTime**|オプションのフィールド。|このオブジェクトを自動的にアクティブにする日付。 このアクティブ化期限まではどのノードにも送信されません。|
|**version**|オプションのフィールド。|任意のストリング値。 値が意味を持って解釈されることはありません。 モデル管理システムは、オブジェクトの複数バージョンを保持しません。| 
|** description **|オプションのフィールド。|任意の説明。|

注:

1. **destinationPolicy** を使用する場合、**destinationType** フィールド、**destinationID** フィールド、および **destinationsList** フィールドをメタデータから削除してください。 **destinationPolicy** 内の **properties**、**constraints**、および **services** がこのオブジェクトを受信する宛先を決定します。
2. **version** および **description** をメタデータ内にストリングとして指定できます。 version の値が意味を持って解釈されることはありません。 MMS は、オブジェクトの複数のバージョンを保持しません。
3. **expiration** および **activationTime** は RFC3339 フォーマットで指定する必要があります。

以下の 2 つのオプションのいずれかを使用して、**my_metadata.json** 内のフィールドを設定します。

1. ポリシーを使用して実行されているエッジ・ノードに MMS オブジェクトを送信します。

   この例では、カメラ・エッジ・ノード node1、node2、および node3 がポリシーを使用して登録されています。 **weaponDetector** は、これらのノードで実行されているサービスの 1 つであり、これらのカメラ・エッジ・ノードで実行されている **weaponDetector** サービスによってモデル・ファイルが使用されるようにする必要があります。 ターゲット・ノードはポリシーを使用して登録されているので、**destinationOrgID** および **destinationPolicy** のみを使用します。 **ObjectType** フィールドを **model** に設定しますが、これはオブジェクトを取得するサービスにとって意味のある任意のストリングに設定することができます。

   このシナリオでは、メタデータ・ファイルは次のようになります。

   ```json
   {
     "objectID": "my_model",
     "objectType": "model",
     "destinationOrgID": "$HZN_ORG_ID",
     "destinationPolicy": {
       "properties": [],
       "constraints": [],
       "services": [
         {
           "orgID": "$SERVICE_ORG_ID",
           "arch": "$ARCH",
           "serviceName": "weaponDetector",
           "version": "$VERSION"
         }
       ]
     },
     "version": "1.0.0",
     "description": "weaponDetector model"
   }
   ```
   {: codeblock}

2. パターンを使用して実行されているエッジ・ノードに MMS オブジェクトを送信します。

   このシナリオでは、使用されるノードは同じですが、サービスの 1 つとして **weaponDetector** を含んでいるパターン **pattern.weapon-detector** を使用して登録されています。

   パターンを使用しているノードにこのモデルを送信するため、メタデータ・ファイルを次のように変更します。

   1. **destinationType** フィールドにノード・パターンを指定します。
   2. **destinationPolicy** フィールドを削除します。

   メタデータ・ファイルは次のようになります。

   ```
   {
     "objectID": "my_model",
     "objectType": "model",
     "destinationOrgID": "$HZN_ORG_ID",
     "destinationType": "pattern.weapon-detector",
     "version": "1.0.0",
     "description": "weaponDetector model"
   }
   ```
   {: codeblock}

これで、モデル・ファイルおよびメタデータ・ファイルは公開の準備ができました。

### MMS オブジェクトの公開

メタデータおよびデータ・ファイルの両方と共にオブジェクトを公開します。

```
hzn mms object publish -m my_metadata.json -f my_model
```
{: codeblock}

### MMS オブジェクトのリスト

特定の組織内で以下の **objectID** および **objectType** を持つ MMS オブジェクトをリストします。

```
hzn mms object list --objectType=model --objectId=my_model
```
{: codeblock}

コマンドの結果は以下のようになります。

```
Listing objects in org userdev:
[
  {
    "objectID": "my_model",
    "objectType": "model"
  }
]
```

すべての MMS オブジェクト・メタデータを表示するには、コマンドに **-l** を追加します。

```
hzn mms object list --objectType=model --objectId=my_model -l
```
{: codeblock}

オブジェクトと一緒にオブジェクト状況および宛先を表示するには、コマンドに **-d** を追加します。 以下の宛先結果は、オブジェクトがカメラ node1、node2、および node3 に送信されることを示しています。 

```
hzn mms object list --objectType=model --objectId=my_model -d
```
{: codeblock}

上のコマンドの出力は次のようになります。

```
[
  {
    "objectID": "my_model",
    "objectType": "model",
    "destinations": [
      {
        "destinationType": "pattern.mask-detector",
        "destinationID": "node1",
        "status": "delivered",
        "message": ""
      },
      {
        "destinationType": "pattern.mask-detector",
        "destinationID": "node2",
        "status": "delivered",
        "message": ""
      },
      {
        "destinationType": "pattern.mask-detector",
        "destinationID": "node3",
        "status": "delivered",
        "message": ""
      },
    ],
    "objectStatus": "ready"
  }
]
```

MMS オブジェクト・リストを絞り込むために使用できる拡張フィルタリング・オプションがあります。 フラグの完全なリストを表示するには、以下のようにします。

```
hzn mms object list --help
```
{: codeblock}

### MMS オブジェクトの削除

MMS オブジェクトを削除します。

```
hzn mms object delete --type=model --id=my_model
```
{: codeblock}

MMS からオブジェクトが削除されます。

### MMS オブジェクトの更新

時間の経過とともにモデルの変更がある場合があります。 更新されたモデルを公開するには、同じメタデータ・ファイル (version 値 **upgrade** が推奨されます) と共に **hzn mms object publish** を使用します。 MMS では、3 つのすべてのカメラの 1 つずつについてモデルを更新する必要はありません。 以下を使用して、3 つすべてのノードの **my_model** オブジェクトを更新します。

```
hzn mms object publish -m my_metadata.json -f my_updated_model
```
{: codeblock}

## 付録

注: コマンド構文について詳しくは、[本書の規則](../getting_started/document_conventions.md)を参照してください。

MMS オブジェクト・メタデータのテンプレートを生成するために使用される **hzn mms object new** コマンドの出力例を以下に示します。

```
{
  "objectID": "",            /* Required: A unique identifier of the object. */
  "objectType": "",          /* Required: The type of the object. */
  "destinationOrgID": "$HZN_ORG_ID", /* Required: The organization ID of the object (an object belongs to exactly one organization). */
  "destinationID": "",       /* The node id (without org prefix) where the object should be placed. */
                             /* If omitted the object is sent to all nodes with the same destinationType. */
                             /* Delete this field when you are using destinationPolicy. */
  "destinationType": "",     /* The pattern in use by nodes that should receive this object. */
                             /* If omitted (and if destinationsList is omitted too) the object is broadcast to all known nodes. */
                             /* Delete this field when you are using policy. */
  "destinationsList": null,  /* The list of destinations as an array of pattern:nodeId pairs that should receive this object. */
                             /* If provided, destinationType and destinationID must be omitted. */
                             /* Delete this field when you are using policy. */
  "destinationPolicy": {     /* The policy specification that should be used to distribute this object. */
                             /* Delete these fields if the target node is using a pattern. */
    "properties": [          /* A list of policy properties that describe the object. */
      {
        "name": "",
        "value": null,
        "type": ""           /* Valid types are string, bool, int, float, list of string (comma separated), version. */
                             /* Type can be omitted if the type is discernable from the value, e.g. unquoted true is boolean. */
      }
    ],
    "constraints": [         /* A list of constraint expressions of the form <property name> <operator> <property value>, separated by boolean operators AND (&&) or OR (||). */
      ""
    ],
    "services": [            /* The service(s) that will use this object. */
      {
        "orgID": "",         /* The org of the service. */
        "serviceName": "",   /* The name of the service. */
        "arch": "",          /* Set to '*' to indcate services of any hardware architecture. */
        "version": ""        /* A version range. */
      }
    ]
  },
  "expiration": "",          /* A timestamp/date indicating when the object expires (it is automatically deleted). The time stamp should be provided in RFC3339 format.  */
  "version": "",             /* Arbitrary string value. The value is not semantically interpreted. The Model Management System does not keep multiple version of an object. */
  "description": "",         /* An arbitrary description. */
  "activationTime": ""       /* A timestamp/date as to when this object should automatically be activated. The timestamp should be provided in RFC3339 format. */
}
```
{: codeblock}

## 例
{: #mms}

このサンプルは、モデル管理システム (MMS) を使用する {{site.data.keyword.edge_service}} を開発する方法を理解するのに役立ちます。 このシステムを使用して、エッジ・ノードで実行されるエッジ・サービスによって使用される機械学習モデルをデプロイしたり、更新したりすることができます。
{:shortdesc}

MMS を使用する例については、[Horizon Hello Model Management Service (MMS) Example Edge Service](https://github.com/open-horizon/examples/tree/master/edge/services/helloMMS) を参照してください。

## 始める前に
{: #mms_begin}

[エッジ・サービス作成の準備](service_containers.md)の前提条件ステップを実行してください。 その結果、以下の環境変数が設定され、以下のコマンドがインストールされ、以下のファイルが存在していなければなりません。

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## 手順
{: #mms_procedure}

このサンプルは、[{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/) オープン・ソース・プロジェクトの一部です。 [Creating Your Own Hello MMS Edge Service](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md) の手順に従った後、ここに戻ってください。

## 次の作業
{: #mms_what_next}

* [デバイス用のエッジ・サービスの開発](developing.md)にある他のエッジ・サービスのサンプルを試してください。

## 参考文献

* [モデル管理を使用する Hello World](model_management_system.md)
