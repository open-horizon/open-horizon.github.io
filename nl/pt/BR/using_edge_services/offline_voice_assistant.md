---

copyright:
years: 2019
lastupdated: "2019-11-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Assistente de voz off-line
{: #offline-voice-assistant}

A cada minuto, o assistente de voz off-line registra um clipe de áudio de cinco segundos, converte o clipe de áudio em texto localmente no dispositivo de borda e direciona a máquina host para executar o comando e falar a saída. 

## Antes de Começar
{: #before_beginning}

Assegure-se de que seu sistema atenda a estes requisitos:

* Deve-se registrar e cancelar registro executando as etapas em [Preparando um dispositivo de borda](../installing/adding_devices.md).
* Uma placa de som USB e um microfone devem estar instalados em seu Raspberry Pi. 

## Registrando seu dispositivo de borda
{: #reg_edge_device}

Para executar o exemplo de serviço `processtext` em seu nó de borda, deve-se registrar o seu nó de borda com o padrão de implementação `IBM/pattern-ibm.processtext`. 

Execute as etapas na seção Usando o Serviço de borda de exemplo do Assistente de voz off-line com padrão de implementação [Usando o Serviço de borda de exemplo do Assistente de voz off-line com padrão de implementação](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) do arquivo readme.

## Informações adicionais
{: #additional_info}

O código-fonte `processtext` de exemplo também está disponível no repositório GitHub do Horizon, como um exemplo para o desenvolvimento do {{site.data.keyword.edge_notm}}. Essa fonte inclui o código para todos os serviços que são executados nos nós de borda para esse exemplo. 

Esses serviços [Open Horizon Exemplos](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) incluem:

* O serviço [voice2audio](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) registra o clipe de áudio de cinco segundos e o publica no broker mqtt.
* O serviço [audio2text](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) usa o clipe de áudio e o converte em texto off-line usando o Pocketsphinx.
* O serviço [processtext](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) usa o texto e tenta executar o comando gravado.
* O serviço [text2speech](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) reproduz a saída do comando por meio de um alto-falante.
* O [mqtt_broker](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) gerencia toda a comunicação inter-container.

## O que fazer em seguida
{: #what_next}

Para obter instruções para construir e publicar sua própria versão do Watson Speeh to Text, consulte as etapas do diretório `processtext` no repositório [Open Horizon examples.](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service) 
