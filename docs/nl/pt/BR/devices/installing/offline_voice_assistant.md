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

## Antes de iniciar
{: #before_beginning}

Assegure-se de que seu sistema atenda a estes requisitos:

* Deve-se registrar e cancelar registro executando as etapas em [Preparando um dispositivo de borda](adding_devices.md).
* Uma placa de som USB e um microfone devem estar instalados em seu Raspberry Pi. 

## Registrando seu dispositivo de borda
{: #reg_edge_device}

Para executar o exemplo de serviço `processtext` em seu nó de borda, deve-se registrar o seu nó de borda com o padrão de implementação `IBM/pattern-ibm.processtext`. 

Execute as etapas na seção Usando o serviço de borda de exemplo do assistente de voz off-line com padrão de implantação [Usando o serviço de borda de exemplo do assistente de voz off-line com padrão de implantação![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext#-using-the-offline-voice-assistant-example-edge-service-with-deployment-pattern) do arquivo leia-me.

## Informações adicionais
{: #additional_info}

O código-fonte `processtext` de exemplo também está disponível no repositório GitHub do Horizon, como um exemplo para o desenvolvimento do {{site.data.keyword.edge_devices_notm}}. Essa fonte inclui o código para todos os serviços que são executados nos nós de borda para esse exemplo. 

Esses serviços [Exemplos do Open
Horizon ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) incluem:

* O serviço [voice2audio ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/voice2audio) registra o clipe de áudio de cinco segundos e publica-o no bloker mqtt.
* O serviço [audio2text ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/audio2text) usa o clipe de áudio e converte-o em texto off-line usando pocket sphinx.
* O serviço [processtext ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/processtext) usa o texto e tenta executar o comando registrado.
* O serviço [text2speech ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/text2speech) reproduz a saída do comando por meio de um alto-falante.
* O [mqtt_broker ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/mqtt_broker) gerencia toda comunicação intercontêiner.

## O que fazer a seguir
{: #what_next}

Para obter instruções sobre como construir e publicar sua própria versão de voz para texto do Watson, consulte as etapas do diretório `processtext` no repositório de [Exemplos do Open Horizon ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/blob/master/edge/services/processtext/CreateService.md#-building-and-publishing-your-own-version-of-the-offline-voice-assistant-edge-service). 
