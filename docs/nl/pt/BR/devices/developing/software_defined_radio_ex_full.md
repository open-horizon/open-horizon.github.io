---

copyright:
years: 2019
lastupdated: "2019-06-26"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Processamento de borda de rádio definido por software
{: #defined_radio_ex}

***NOTA DO AUTOR: Troy fará a mesclagem deste conteúdo com o conteúdo de software_defined_radio_ex.md.***

Este exemplo usa o rádio definido por software (SDR) como um exemplo de processamento de borda. Com o SDR, é possível enviar dados brutos por meio do espectro de rádio completo para um servidor de nuvem para processamento. O nó de borda processa os dados localmente e, em seguida, envia menos volume de dados mais valiosos para um serviço de processamento em nuvem para processamento adicional.
{:shortdesc}

Este diagrama mostra a arquitetura para este exemplo de SDR:

<img src="../../images/edge/08_sdrarch.svg" width="70%" alt="Arquitetura de exemplo">

O processamento de borda SDR é um exemplo cheio de recursos que consome áudio da estação de rádio, extrai discurso e converte o discurso extraído em texto. O exemplo conclui a análise de sentimentos no texto e disponibiliza os dados e os resultados por meio de uma interface com o usuário na qual é possível visualizar os detalhes dos dados de cada nó de borda. Use esse exemplo para saber mais sobre o processamento de borda.

O SDR recebe sinais de rádio usando o circuito digital em uma CPU do computador para manipular o trabalho para requerer um conjunto de circuitos analógicos especializados. Esses circuitos analógicos normalmente são restringidos pela amplitude do espectro de rádio que eles podem receber. Um receptor de rádio analógico construído para receber estações de rádio FM, por exemplo, não pode receber sinais de rádio de qualquer outro lugar no espectro de rádio. O SDR pode acessar grandes partes do espectro. Se você não tiver o hardware SDR, será possível usar dados simulados. Quando você estiver usando dados simulados, o áudio do
fluxo
da Internet será tratado como se fosse transmitido pela FM e recebido
no nó de borda.

Antes de executar esta tarefa, registre e cancele o registro do seu dispositivo de borda executando as etapas em [Instalar o agente Horizon em seu dispositivo de borda e registrá-lo com o exemplo de Hello World](registration.md).

Este código contém esses componentes primários.

|Componente|Descrição|
|---------|-----------|
|[sdr service ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/sdr)|O serviço de nível inferior acessa o hardware no nó de borda|
|[ssdr2evtstreams service ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/sdr2evtstreams)|O serviço de nível superior recebe dados do serviço sdr de nível inferior e conclui a análise local dos dados no nó de borda. O
serviço sdr2evtstreams então envia os dados processados para o software de back-end em nuvem.|
|[Software de back-end de nuvem ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/cloud/sdr)|O software back-end de nuvem recebe dados de nós de borda para análise adicional. Em seguida, a implementação back-end pode apresentar um mapa dos nós de borda e mais informações dentro de uma interface com o usuário baseada na web.|
{: caption="Tabela 1. Rádio definido por software para componentes primários do {{site.data.keyword.message_hub_notm}}" caption-side="top"}

## Registrando seu dispositivo

Embora esse serviço possa ser executado usando dados simulados em qualquer dispositivo de borda, se você estiver usando um dispositivo de borda, como um Raspberry Pi com o hardware SDR, configure um módulo kernel para suportar primeiro o hardware do SDR. Deve-se configurar esse
módulo manualmente. Os contêineres do Docker podem estabelecer uma distribuição diferente do Linux em seus contextos, mas o contêiner não pode instalar módulos do kernel. 

Conclua as etapas a
seguir para configurar esse módulo:

1. Como um usuário raiz, crie um arquivo denominado
`/etc/modprobe.d/rtlsdr.conf`.

   ```
   sudo nano /etc/modprobe.d/rtlsdr.conf
   ```
   {: codeblock}

2. Inclua
as seguintes linhas no arquivo:

   ```
   blacklist rtl2830
     blacklist rtl2832
     blacklist dvb_usb_rtl28xxu
   ```
   {: codeblock}

3. Salve o arquivo e, em seguida, reinicie antes de
continuar:
   ```
   sudo reboot
   ```
   {: codeblock}   

4. Configure a seguinte chave de API do
{{site.data.keyword.message_hub_notm}} no ambiente. Esta chave é criada para uso com este exemplo e é usada para alimentar os dados processados reunidos pelo seu nó de borda para a IU de rádio definido por software IBM.

   ```
   export EVTSTREAMS_API_KEY=X2e8cSjbDAMk-ztJLaoi3uffy8qsQTnZttUjcHCfm7cp
    export EVTSTREAMS_BROKER_URL=broker-3-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-4-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-y420pyyyvhhmttz0.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

5. Para executar o exemplo de serviço sdr2evtstreams em seu nó de borda, deve-se registrar seu nó de borda com o padrão de implementação IBM/pattern-ibm.sdr2evtstreams. Execute as etapas em [Condições prévias para o uso do SDR para o IBM Event Streams Exemplo Edge Service![Abre em uma novaguia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fedge%2Fevtstreams%2Fsdr2evtstreams). 


6. Verifique a UI da Web de exemplo para saber se o nó de borda
está enviando resultados. Para obter mais informações, consulte
[UI
da web de exemplo de rádio definida por software![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://sdr-poc-sdr-poc-app-delightful-leopard.mybluemix.net). Efetue login com essas credenciais:

   * Nome do usuário: guest@ibm.com
   * Senha: guest123

## Implementando na nuvem

Opcionalmente, as IBM Functions, os bancos de dados IBM e o código da IU da web podem ser implementados no IBM Cloud se caso você deseja criar sua própria IU da web de exemplo de rádio definido por software. É possível fazer isso com um único comando depois que você [criar uma conta paga ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://cloud.ibm.com/login).

O código de implementação está localizado no repositório examples/cloud/sdr/deploy/ibm. Para obter mais informações, consulte [Conteúdo do repositório de implementação ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/links?url=https%3A%2F%2Fgithub.com%2Fopen-horizon%2Fexamples%2Ftree%2Fmaster%2Fcloud%2Fsdr%2Fdeploy%2Fibm). 

Este código consiste em um arquivo README.md com instruções detalhadas e em um script deploy.sh que manipula a carga de trabalho. O repositório também contém um Makefile como outra interface no script deploy.sh. Revise as instruções do repositório para saber mais sobre a implementação de seu próprio back-end de nuvem para o exemplo de SDR. 

Nota: este processo de implementação requer serviços pagos que incorrem em encargos em sua conta do {{site.data.keyword.cloud_notm}}.

## O que fazer a seguir

Se você deseja implementar seu próprio software em um nó de borda, deve criar seus próprios serviços de borda e padrão de implementação ou política de implementação associados. Para obter mais informações, consulte [Desenvolvendo serviços de borda com o IBM Edge Application Manager for Devices](../developing/developing.md).
