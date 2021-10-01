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

# Model Management System
{: #model_management_details}

O sistema de gerenciamento de modelo (MMS) alivia a carga de gerenciamento do modelo de Inteligência artificial (IA) para serviços cognitivos executados em nós de borda. O MMS também pode ser usado para a entrega de outros tipos de arquivos de dados para os nós de borda. O MMS facilita o armazenamento, a entrega e a segurança de modelos, dados e outros pacotes de metadados necessários aos serviços de borda. Isso permite que os nós de borda enviem e recebam facilmente modelos e metadados para e a partir da nuvem.

O MMS é executado no hub do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) e em nós de borda. O Cloud Sync Service (CSS) entrega modelos, metadados ou dados para nós ou grupos de nós específicos dentro de uma organização. Depois que os objetos são entregues aos nós de borda, é disponibilizada uma API que permite que o serviço de borda obtenha os modelos ou dados a partir do Cloud Sync Service (ESS).

Os objetos são preenchidos no MMS por desenvolvedores de serviços, administradores de devops e autores de modelos. Os componentes do MMS facilitam a integração entre as ferramentas do modelo de AI e os serviços cognitivos em execução na borda. À medida em que os autores completam os modelos, estes são publicados no MMS, que imediatamente os disponibiliza para os nós de borda. Por padrão, a integridade do modelo é garantida por hash e assinatura do modelo e, em seguida, carregando a assinatura e a chave de verificação antes de publicar o modelo. O MMS usa a assinatura e a chave para verificar se o modelo carregado não foi adulterado. Esse mesmo procedimento também é usado quando o MMS implementa o modelo em nós de borda.

O {{site.data.keyword.ieam}} também fornece uma CLI (**hzn mms**) que permite a manipulação dos objetos modelo e seus metadados.

Os diagramas a seguir mostram o fluxo de trabalho associado ao desenvolvimento e à atualização de modelos de IA usando o MMS

### Desenvolvendo e usando um modelo de IA com o MMS

<img src="../images/edge/02a_Developing_AI_model_using_MMS.svg" style="margin: 3%" alt="Desenvolvendo um serviço de IA usando o MMS"> 

### Atualizando um modelo de IA com o MMS

<img src="../images/edge/02b_Updating_AI_model_using_MMS.svg" style="margin: 3%" alt="Atualizando um serviço de IA usando o MMS"> 

## Conceitos de MMS

O MMS é constituído por vários componentes: CSS, ESS e objetos.

O CSS e o ESS fornecem APIs que os desenvolvedores e administradores usam para interagir com o MMS. Os objetos são os modelos de aprendizado de máquina e outros tipos de arquivos de dados que são implementados em nós de borda.

### CSS

O CSS é implementado no hub de gerenciamento do {{site.data.keyword.ieam}} quando o {{site.data.keyword.ieam}} é instalado. O CSS usa o banco de dados mongoDB para armazenar objetos e manter o status de cada nó de borda.

### ESS

O ESS está integrado no agente {{site.data.keyword.ieam}} que é executado no nó de borda. O ESS pesquisa continuamente o CSS para atualizações de objetos e armazena quaisquer objetos que sejam entregues ao nó em um banco de dados local no nó de borda. As APIs do ESS podem ser usadas por serviços que são implementados no nó de borda para acessar os metadados e os objetos de dados ou modelo.

### Objetos (metadados e dados)

Os metadados descrevem seus modelos de dados. Um objeto é publicado no MMS com metadados e dados, ou apenas com metadados. Nos metadados, os campos **objectType** e **objectID** definem a identidade do objeto dentro de uma determinada organização. Esses campos relacionados ao destino determinam os nós de borda aos quais enviar o objeto:

* **destinationOrgID**
* **destinationType**
* **destinationID**
* **destinationList**
* **destinationPolicy**

Outras informações do objeto, incluindo descrição, versão e assim por diante, podem ser especificadas nos metadados. O valor da versão não tem significado semântico para o serviço de sincronização; portanto, existe apenas uma cópia do objeto no CSS.

Um arquivo de dados é o arquivo que contém a definição de modelo específica do ML que é usada por um serviço cognitivo. Arquivos de modelo de AI, arquivos de configuração e dados binários são exemplos de arquivos de dados.

### Modelo de IA

O modelo de IA (Inteligência Artificial) não é um conceito específico do MMS, mas é um caso de uso principal do MMS. Os modelos de IA são representações matemáticas de um processo do mundo real relacionado à IA. Os serviços cognitivos que imitam as funções cognitivas humanas usam e consomem o modelo de IA. Para gerar um modelo de IA, aplique algoritmos de IA em dados de treinamento. Resumindo, o modelo de IA é distribuído pelo MMS e usado por um serviço cognitivo executado em um nó de borda.

## Conceitos de MMS no {{site.data.keyword.ieam}}

Existem relacionamentos específicos entre os conceitos de MMS e outros conceitos no {{site.data.keyword.ieam}}.

O {{site.data.keyword.ieam}} pode registrar um nó com um padrão ou com uma política. Quando você estiver criando os metadados para um objeto, configure o campo **destinationType** nos metadados do objeto para o nome padrão de nós que devem receber este objeto. Todos os nós do {{site.data.keyword.ieam}} que usam o mesmo padrão podem ser considerados como estando no mesmo grupo. Portanto, esse mapeamento permite enviar objetos a todos os nós de um determinado tipo. O campo **destinationID** é igual ao ID do nó de borda do {{site.data.keyword.ieam}}. Caso o campo de metadados **destinationID** não seja configurado, o objeto será transmitido para todos os nós que têm o padrão (**destinationType**).

Ao criar metadados para objetos que devem ser entregues a nós registrados com uma política, deixe **destinationType** e **destinationID** em branco e, em vez disso, configure o campo **destinationPolicy**. Ele contém as informações de destino (propriedade de política, restrição e serviço) que definem quais nós recebem o objeto. Configure os campos **services** para indicar qual serviço processa o objeto. Os campos **properties** e **constraints** são opcionais e são usados para limitar ainda mais a lista de nós que devem receber o objeto.

Em um nó de borda, é possível que haja vários serviços em execução, que podem ter sido desenvolvidos por diferentes entidades. A camada de autenticação e de autorização do agente do {{site.data.keyword.ieam}} controla quais serviços podem acessar um determinado objeto. Os objetos implementados por meio de políticas são visíveis apenas para serviços referenciados na **destinationPolicy**. No entanto, esse nível de isolamento não está disponível para os objetos implementados em nós que executam um padrão. Em um nó que usa um padrão, todos os objetos que são entregues a esse nó são visíveis para todos os serviços no nó.

## Comandos da CLI do MMS

Esta seção descreve um exemplo de MMS e descreve como usar alguns comandos de MMS.

Por exemplo, um usuário opera três câmeras, em que um serviço de aprendizado de máquina (**weaponDetector**) é implementado para identificar pessoas que estão portando armas. Este modelo já está treinado e o serviço está em execução nas câmeras (que atuam como nós).

### Verificar o status do MMS

Antes de publicar o modelo, emita o comando **hzn mms status** para verificar o status do MMS. Verifique **heathStatus** em **general** e **dbStatus** em **dbHealth**. Os valores desses campos devem ser verdes, o que indica que o CSS e o banco de dados estão em execução.

```
$ hzn mms status {   "general": {     "nodeType": "CSS",     "healthStatus": "green",     "upTime": 21896   },   "dbHealth": {     "dbStatus": "green",     "disconnectedFromDB": false,     "dbReadFailures": 0,     "dbWriteFailures": 0   }
}
```
{: codeblock}

### Crie o objeto de MMS

No MMS, o arquivo de modelo de dados não é publicado de forma independente. Para a publicação e distribuição, o MMS requer um arquivo de metadados juntamente com o arquivo de modelo de dados. O arquivo de metadados configura um conjunto de atributos para o modelo de dados. O MMS armazena, distribui e recupera os objetos de modelo com base nos atributos que são definidos em metadados.

O arquivo de metadados é um arquivo json.

1. Visualize um modelo de arquivo de metadados:

   ```
   hzn mms object new
   ```
   {: codeblock}
2. Copie o modelo para um arquivo chamado **my_metadata.json**:

   ```
   hzn mms object new >> my_metadata.json
   ```
   {: codeblock}

   Como alternativa, é possível copiar o modelo do terminal e colá-lo em um arquivo.

É importante entender o significado dos campos de metadados e como eles se relacionam com o exemplo de metadados.

|Campo|Descrição|Notas|
|-----|-----------|-----|
|**objectID**|O ID do objeto.|Um identificador exclusivo necessário do objeto dentro da sua organização.|
|**objectType**|O tipo de objeto.|Um campo necessário que é definido pelo usuário; não há tipos de objetos integrados.|
|**destinationOrgID**|A organização de destino.|Um campo necessário usado para distribuir o objeto para nós dentro da mesma organização.|
|**destinationType**|O tipo do destino.|O padrão usado pelos nós que devem receber este objeto.|
|**destinationID**|O ID de destino.|Um campo opcional configurado com o ID do único nó (sem prefixo org) no qual o objeto deve ser colocado. Se omitido, o objeto será enviado a todos os nós com o destinationType.|
|**destinationsList**|A lista de destino.|Um campo opcional configurado com uma matriz de pares pattern:nodeId que devem receber este objeto. Esta é uma alternativa à configuração de **destinationType** e **destinationID**.|
|**destinationPolicy**|A política de destino.|Use ao distribuir o objeto para nós registrados com a política. Nesse caso, não configure **destinationType**, **destinationID** ou **destinationsList**.|
|**expiration**|Um campo opcional.|Indica quando o objeto expirará e será removido do MMS.|
|**activationTime**|Um campo opcional.|A data em que este objeto deve ser ativado automaticamente. Ele não é entregue a nenhum nó até depois do horário de ativação.|
|**version**|Um campo opcional.|Valor de sequência arbitrária. O valor não é interpretado de forma semântica. O sistema de gerenciamento de modelo não mantém várias versões de um objeto.| 
|**description**|Um campo opcional.|Uma descrição arbitrária.|

Nota:

1. Ao usar **destinationPolicy**, remova os campos **destinationType**, **destinationID** e **destinationsList** dos metadados. Os itens **properties**, **constraints** e **services** dentro de **destinationPolicy** determinarão os destinos que receberão este objeto.
2. **version** e **description** podem ser fornecidos como sequências dentro dos metadados. O valor da versão não é interpretado semanticamente. O MMS não mantém várias versões de um objeto.
3. **expiration** e **activationTime** devem ser fornecidos no formato RFC3339.

Preencha os campos em **my_metadata.json** usando uma dessas duas opções:

1. Enviar o objeto de MMS para os nós de borda executados com uma política.

   Neste exemplo, os nós de borda da câmera node1, node2 e node3 são registrados com a política. **weaponDetector** é um dos serviços em execução nos nós e deseja-se que o arquivo de modelo seja usado pelo serviço **weaponDetector** executado nos nós de borda da câmera. Como os nós de destino são registrados com uma política, use apenas **destinationOrgID** e **destinationPolicy**. Configure o campo **ObjectType** como **model**, mas ele poderia ser configurado com qualquer sequência que seja significativa para o serviço que recupera o objeto.

   Nesse cenário, o arquivo de metadados pode ser:

   ```json
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationPolicy": {        "properties": [],        "constraints": [],        "services": [          {            "orgID": "$SERVICE_ORG_ID",            "arch": "$ARCH",            "serviceName": "weaponDetector",            "version": "$VERSION"          }        ]      },      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

2. Enviar o objeto de MMS para os nós de borda executados com um padrão.

   Nesse cenário, são utilizados os mesmos nós, mas agora eles são registrados com o padrão **pattern.weapon-detector**, que possui **weaponDetector** como um dos serviços.

   Para enviar o modelo para os nós com um padrão, altere o arquivo de metadados:

   1. Especifique o padrão do nó no campo **destinationType**.
   2. Remova o campo **destinationPolicy**.

   O arquivo de metadados é semelhante a:

   ```
   {        "objectID": "my_model",      "objectType": "model",      "destinationOrgID": "$HZN_ORG_ID",      "destinationType": "pattern.weapon-detector",      "version": "1.0.0",      "description": "weaponDetector model"    }
   ```
   {: codeblock}

Agora, o arquivo de modelo e o arquivo de metadados estão prontos para publicação.

### Publicar o objeto de MMS

Publicar o objeto com o arquivo de metadados e de dados:

```
hzn mms object publish -m my_metadata.json -f my_model
```
{: codeblock}

### Listar o objeto de MMS

Listar o objeto de MMS com este **objectID** e este **objectType** dentro da organização especificada:

```
hzn mms object list --objectType=model --objectId=my_model
```
{: codeblock}

Este é o resultado do comando, que será semelhante a:

```
Listing objects in org userdev: [   {     "objectID": "my_model",     "objectType": "model"   }
]
```

Para mostrar todos os metadados do objeto de MMS, inclua **-l** no comando:

```
hzn mms object list --objectType=model --objectId=my_model -l
```
{: codeblock}

Para mostrar o status do objeto e os destinos juntamente com o objeto, inclua **-d** no comando. O resultado de destino a seguir indica que o objeto é entregue às câmeras: node1, node2 e node3. 

```
hzn mms object list --objectType=model --objectId=my_model -d
```
{: codeblock}

A saída do comando anterior é semelhante a:

```
[   {     "objectID": "my_model",     "objectType": "model",     "destinations": [       {         "destinationType": "pattern.mask-detector",         "destinationID": "node1",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node2",         "status": "delivered",         "message": ""       },       {         "destinationType": "pattern.mask-detector",         "destinationID": "node3",         "status": "delivered",         "message": ""       },     ],     "objectStatus": "ready"   }
]
```

Há opções de filtragem mais avançadas disponíveis para limitar a lista de objetos de MMS. Para ver uma lista completa de sinalizações:

```
hzn mms object list --help
```
{: codeblock}

### Excluir o objeto de MMS

Excluir o objeto de MMS:

```
hzn mms object delete --type=model --id=my_model
```
{: codeblock}

O objeto é removido do MMS.

### Atualizar o objeto MMS

Os modelos podem mudar ao longo do tempo. Para publicar um modelo atualizado, use **publicar objeto MMS de hzn** com o mesmo arquivo de metadados (o valor da versão **upgrade** é sugerido). Com o MMS, não é necessário atualizar individualmente os modelos para as três câmeras. Use isso para atualizar o objeto **my_model** nos três nós.

```
hzn mms object publish -m my_metadata.json -f my_updated_model
```
{: codeblock}

## Apêndice

Nota: consulte [Convenções usadas neste documento](../getting_started/document_conventions.md) para obter mais informações sobre a sintaxe de comando.

A seguir, é mostrado um exemplo da saída do comando **hzn mms object new** usado para gerar um modelo de metadados do objeto de MMS:

```
{     "objectID": "",            /* Required: A unique identifier of the object. */   "objectType": "",          /* Required: The type of the object. */   "destinationOrgID": "$HZN_ORG_ID", /* Required: The organization ID of the object (an object belongs to exactly one organization). */   "destinationID": "",       /* The node id (without org prefix) where the object should be placed. */                              /* If omitted the object is sent to all nodes with the same destinationType. */                              /* Delete this field when you are using destinationPolicy. */   "destinationType": "",     /* The pattern in use by nodes that should receive this object. */                              /* If omitted (and if destinationsList is omitted too) the object is broadcast to all known nodes. */                              /* Delete this field when you are using policy. */   "destinationsList": null,  /* The list of destinations as an array of pattern:nodeId pairs that should receive this object. */                              /* If provided, destinationType and destinationID must be omitted. */                              /* Delete this field when you are using policy. */   "destinationPolicy": {     /* The policy specification that should be used to distribute this object. */                              /* Delete these fields if the target node is using a pattern. */     "properties": [          /* A list of policy properties that describe the object. */       {         "name": "",         "value": null,         "type": ""           /* Valid types are string, bool, int, float, list of string (comma separated), version. */                              /* Type can be omitted if the type is discernable from the value, e.g. unquoted true is boolean. */       }     ],     "constraints": [         /* A list of constraint expressions of the form <property name> <operator> <property value>, separated by boolean operators AND (&&) or OR (||). */       ""     ],     "services": [            /* The service(s) that will use this object. */       {         "orgID": "",         /* The org of the service. */         "serviceName": "",   /* The name of the service. */         "arch": "",          /* Set to '*' to indcate services of any hardware architecture. */         "version": ""        /* A version range. */       }     ]   },   "expiration": "",          /* A timestamp/date indicating when the object expires (it is automatically deleted). The time stamp should be provided in RFC3339 format.  */   "version": "",             /* Arbitrary string value. O valor não é interpretado de forma semântica. The Model Management System does not keep multiple version of an object. */   "description": "",         /* An arbitrary description. */   "activationTime": ""       /* A timestamp/date as to when this object should automatically be activated. The timestamp should be provided in RFC3339 format. */ }
```
{: codeblock}

## Exemplo
{: #mms}

Este exemplo o ajuda a aprender como desenvolver um {{site.data.keyword.edge_service}} que usa o sistema de gerenciamento de modelo (MMS). Você pode usar esse sistema para implementar e atualizar os modelos de máquina de aprendizado que são usados por serviços de borda que são executados em seus nós de borda.
{:shortdesc}

Para obter um exemplo que usa MMS, consulte [Serviço de borda de exemplo do Horizon Hello Model Management Service (MMS)](https://github.com/open-horizon/examples/tree/master/edge/services/helloMMS).

## Antes de Começar
{: #mms_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Procedimento
{: #mms_procedure}

Este exemplo faz parte do projeto de software livre [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga as etapas em [Criando seu próprio serviço de borda Hello MMS](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) e, em seguida, retorne aqui.

## O que fazer em seguida
{: #mms_what_next}

* Experimente os outros exemplos de serviços de borda em [Desenvolvendo um serviço borda para dispositivos](developing.md).

## Leitura Adicional

* [Hello World usando o gerenciamento de modelo](model_management_system.md)
