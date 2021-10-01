---

copyright:
years: 2019
lastupdated: "2020-2-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Conversão de voz para texto do Watson
{: #watson-speech}

Esse serviço recebe a palavra Watson. Quando ela é detectada, o serviço captura um clipe de áudio e envia para uma instância do Speech to Text.  As palavras vazias são removidas (opcionalmente), e o texto transcrito é enviado para {{site.data.keyword.event_streams}}.

## Antes de Começar

Assegure-se de que seu sistema atenda a estes requisitos:

* Deve-se registrar e cancelar registro executando as etapas em [Preparando um dispositivo de borda](adding_devices.md).
* Uma placa de som USB e um microfone devem estar instalados em seu Raspberry Pi. 

Esse serviço requer tanto uma instância do {{site.data.keyword.event_streams}} quanto do IBM Speech to Text para executar corretamente. Para obter instruções sobre como implementar uma instância de fluxos de eventos, consulte [Exemplo de porcentagem de carregamento da CPU do Host (cpu2evtstreams)](../using_edge_services/cpu_load_example.md).  

Assegure-se de que as variáveis de ambiente necessárias do {{site.data.keyword.event_streams}} estejam configuradas:

```
echo "$EVTSTREAMS_API_KEY, $EVTSTREAMS_BROKER_URL"
```
{: codeblock}

Por padrão, o tópico de fluxo do evento que essa amostra usa é `myeventstreams`, mas você pode usar qualquer tópico configurando a seguinte variável de ambiente:

```
export EVTSTREAMS_TOPIC=<your-topic-name>
```
{: codeblock}

## Implementando uma instância do IBM Speech to Text
{: #deploy_watson}

Se uma instância for implementada atualmente, obtenha as informações de acesso e configure as variáveis de ambiente, ou siga estas etapas:

1. Navegue até o IBM Cloud.
2. Clique em **Criar recurso**.
3. Insira `Speech to Text` na caixa de procura.
4. Selecione o azulejo `Speech to Text`.
5. Selecione uma região, selecione um plano de precificação, insira um nome do serviço e clique em **Criar** para provisionar a instância.
6. Após o fornecimento ser concluído, clique na instância e anote a chave de API e a URL das credenciais e exporte-as como a variável de ambiente a seguir:

    ```
    export STT_IAM_APIKEY=<speech-to-text-api-key>     export STT_URL=<speech-to-text-url>
    ```
    {: codeblock}

7. Acesse a seção Introdução para obter instruções de como testar o serviço Speech to Text.

## Registrando seu dispositivo de borda
{: #watson_reg}

Para executar o exemplo de serviço watsons2text em seu nó de borda, deve-se registrar seu nó de borda com o padrão de implementação `IBM/pattern-ibm.watsons2text-arm`. Execute as etapas na seção [Usando o Watson Speech to Text para IBM Event Streams Service with Deployment Pattern](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text#-using-the-ibm-watson-speech-to-text-to-ibm-event-streams-service-with-deployment-pattern) do arquivo leia-me.

## Informações adicionais

O código-fonte do exemplo `processtect` também está disponível no repositório Horizon GitHub como um exemplo para o desenvolvimento do {{site.data.keyword.edge_notm}}. Essa fonte inclui o código para todos os quatro serviços que são executados nos nós de borda para esse exemplo. 

Esses serviços incluem:

* O serviço [hotworddetectar](https://github.com/open-horizon/examples/tree/master/edge/services/hotword_detection) ouve e detecta a palavra-chave Watson e, em seguida, grava um clipe de áudio e publica-o no broker mqtt.
* O serviço [watsons2text](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/watson_speech2text) recebe um clipe de áudio e envia para o serviço IBM Speech to Text e publica o texto decifrado no broker mqtt.
* O serviço [stopwordremoval](https://github.com/open-horizon/examples/tree/master/edge/services/stopword_removal) que é executado como um servidor WSGI obtém um objeto JSON, como  {"text": "how are you today"} e remove as palavras common stop e retorna {"result": "how you today"}.
* O serviço [mqtt2kafka](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt2kafka) publica dados no {{site.data.keyword.event_streams}} quando ele recebe algo no tópico mqtt onde ele está inscrito.
* O [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) é responsável por toda comunicação inter-container.

## O que fazer em seguida

* Para obter instruções sobre a construção e publicação de sua própria versão do Serviço de borda do Assistente de voz off-line, consulte [Serviço de borda do Assistente de voz Off-line](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/watson_speech2text/CreateService.md#-building-and-publishing-your-own-version-of-the-watson-speech-to-text-to-ibm-event-streams-service). Siga as etapas no diretório `watson_speech2text` do repositório de exemplos Open Horizon.

* Consulte [Repositório de exemplos Open Horizon](https://github.com/open-horizon/examples).
