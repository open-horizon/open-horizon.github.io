---

copyright:
years: 2019, 2020
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# CPU para o serviço {{site.data.keyword.message_hub_notm}}
{: #cpu_msg_ex}

Este exemplo coleta informações de porcentagem de carregamento da CPU para enviar para o {{site.data.keyword.message_hub_notm}}. Use esse exemplo para ajudar a desenvolver seus próprios aplicativos de borda que enviam dados para serviços de nuvem.
{:shortdesc}

## Antes de iniciar
{: #cpu_msg_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedimento
{: #cpu_msg_procedure}

Este exemplo faz parte do projeto de software livre [{{site.data.keyword.horizon_open}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/). Siga as etapas em [Construindo e publicando a sua própria versão da CPU para o Serviço de borda do IBM Event Streams ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/CreateService.md#-building-and-publishing-your-own-version-of-the-cpu-to-ibm-event-streams-edge-service) e, em seguida, retorne aqui.

## O que você aprendeu neste exemplo

### Serviços necessários

O serviço de borda cpu2evtstreams é um exemplo de um serviço que depende de dois outros serviços de borda (**cpu** e **gps**) para realizar sua tarefa. É possível ver os detalhes dessas dependências na seção **requiredServices** do arquivo **horizon/service.definition.json**:

```json
    "requiredServices": [
        {
            "url": "ibm.cpu",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        },
        {
            "url": "ibm.gps",
            "org": "IBM",
            "versionRange": "[0.0.0,INFINITY)",
            "arch": "$ARCH"
        }
    ],
```

### Variáveis de configuração
{: #cpu_msg_config_var}

O serviço **cpu2evtstreams** requer alguma configuração para poder executar. Os serviços de borda podem declarar variáveis de configuração, indicando o tipo delas e fornecendo valores padrão. É possível ver essas variáveis de configuração em **horizon/service.definition.json**, na seção **userInput**:

```json  
    "userInput": [
        {
            "name": "EVTSTREAMS_API_KEY",
            "label": "A chave de API a ser usada ao enviar mensagens à instância do IBM Event Streams",
            "type": "sequência de caracteres",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_BROKER_URL",
            "label": "A lista separada por vírgula de URLs a serem usadas ao enviar mensagens à instância do IBM Event Streams",
            "type": "sequência de caracteres",
            "defaultValue": ""
        },
        {
            "name": "EVTSTREAMS_CERT_ENCODED",
            "label": "O certificado autoassinado codificado em base64 a ser usado ao enviar mensagens à instância do IBM Event Streams. Não é necessário para o IBM Cloud Event Streams.",
            "type": "sequência de caracteres",
            "defaultValue": "-"
        },
        {
            "name": "EVTSTREAMS_TOPIC",
            "label": "O tópico a ser usado ao enviar mensagens à instância do IBM Event Streams",
            "type": "sequência de caracteres",
            "defaultValue": "cpu2evtstreams"
        },
        {
            "name": "SAMPLE_SIZE",
            "label": "o número de amostras a serem lidas antes do cálculo da média", "type": "número inteiro",
            "defaultValue": "5"
        },
        {
            "name": "SAMPLE_INTERVAL",
            "label": "o número de segundos entre as amostras",
"type": "número inteiro",
"defaultValue": "2"
        },
        {
            "name": "MOCK",
            "label": "simular a amostragem de CPU",
            "type": "booleano",
            "defaultValue": "false"
        },
        {
            "name": "PUBLISH",
            "label": "publicar as amostras de CPU no IBM Event Streams", "type": "booleano",
            "defaultValue": "true"
        },
        {
            "name": "VERBOSE",
            "label": "registrar em log tudo o que acontece",
"type": "sequência de caracteres",
"defaultValue": "1"
        }
    ],
```

As variáveis de configuração de entrada do usuário como essas são necessárias para que haja valores quando o serviço de borda for iniciado no nó de borda. Os valores podem vir de qualquer uma destas fontes (nesta ordem de precedência):

1. Um arquivo de entrada do usuário especificado com a sinalização **hzn register -f**
2. A seção **userInput** do recurso de nó de borda no Exchange
3. A seção **userInput** do recurso padrão ou de política de implementação no Exchange
4. O valor padrão especificado no recurso de definição de serviço no Exchange

Ao registrar o dispositivo de borda para esse serviço, você forneceu um arquivo **userinput.json**, que especificava algumas das variáveis de configuração que não possuíam valores padrão.

### Dicas de desenvolvimento
{: #cpu_msg_dev_tips}

Pode ser útil incorporar variáveis de configuração no serviço, pois podem ajudá-lo a testar e depurar o serviço. Por exemplo, os metadados (**service.definition.json**) e o código (**service.sh**) desse serviço usam estas variáveis de configuração:

* **VERBOSE** aumenta a quantidade de informações registradas durante a execução
* **PUBLISH** controla se o código tenta enviar mensagens para o {{site.data.keyword.message_hub_notm}}
* **MOCK** controla se o **service.sh** tenta chamar as APIs REST de suas dependências (os serviços **cpu** e **gps**) ou, em vez disso, criar os próprios dados simulados.

A capacidade de simular os serviços dos quais você depende é opcional, mas pode ser útil para desenvolver e testar componentes de forma isolada dos serviços necessários. Essa abordagem também pode permitir o desenvolvimento de um serviço em um tipo de dispositivo no qual não há sensores de hardware ou atuadores.

A capacidade de desativar a interação com os serviços de nuvem pode ser conveniente durante a fase de desenvolvimento e teste, evitando encargos desnecessários e facilitando o teste em um ambiente devops sintético.

## O que fazer a seguir
{: #cpu_msg_what_next}

* Tente outros exemplos de serviço de borda em [Desenvolvendo serviços de borda com {{site.data.keyword.edge_devices_notm}}](developing.md).
