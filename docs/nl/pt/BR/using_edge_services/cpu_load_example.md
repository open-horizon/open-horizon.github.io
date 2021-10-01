---

copyright:
years: 2020
lastupdated: "2020-02-06"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Uso da CPU para {{site.data.keyword.message_hub_notm}}
{: #cpu_load_ex}

A porcentagem de carga da CPU do host é um exemplo de um padrão de implementação que consome dados de porcentagem de carga da CPU e os disponibiliza por meio do IBM Event Streams.

Esse serviço de borda consulta repetidamente a carga da CPU do dispositivo de borda e envia os dados resultantes para [IBM Event Streams](https://www.ibm.com/cloud/event-streams). Este serviço de borda pode ser executado em qualquer nó de borda, pois ele não requer hardware de sensor especializado.

Antes de realizar esta tarefa, registre-se e cancele o registro executando as etapas em [Instalar o agente Horizon em seu dispositivo de borda](../installing/registration.md)

Para ganhar experiência com um cenário mais realista, este exemplo de cpu2evtstreams ilustra mais aspectos de um serviço de borda típico, incluindo:

* Consultando dados do dispositivo de borda dinâmico
* Análise de dados do dispositivo de borda (por exemplo, o `cpu2evtstreams` calcula uma média de janela da carga da CPU)
* Enviando dados processados para um serviço central de alimentação de dados
* Automatiza a aquisição de credenciais de fluxo do evento para autenticar com segurança a transferência de dados

## Antes de Começar
{: #deploy_instance}

Antes de implementar o serviço de borda cpu2evtstreams você precisa de uma instância do {{site.data.keyword.message_hub_notm}} em execução na nuvem para receber seus dados. Cada membro de sua organização pode compartilhar uma instância do {{site.data.keyword.message_hub_notm}}. Se a instância for implementada, obtenha as informações de acesso e configure as variáveis de ambiente.

### Implementando o  {{site.data.keyword.message_hub_notm}}  no  {{site.data.keyword.cloud_notm}}
{: #deploy_in_cloud}

1. Navegue até o {{site.data.keyword.cloud_notm}}.

2. Clique em **Criar recurso**.

3. Insira `Fluxos do evento` na caixa de procura.

4. Selecione o ladrilho **Fluxos do evento**.

5. Em **Fluxos do evento**, insira um nome do serviço, selecione uma região, selecione um plano de precificação e clique em **Criar** para provisionar a instância.

6. Após a provisão ser concluída, clique na instância.

7. Para criar um tópico, clique no ícone + e, em seguida, nomeie a instância `cpu2evtstreams`.

8. É possível criar credenciais em seu terminal ou obtê-las, caso se elas já tenham sido criadas. Para criar credenciais, clique em **Credenciais de serviço > Nova credencial**. Crie um arquivo chamado `event-streams.cfg` com suas novas credenciais formatadas semelhantes ao codeblock a seguir. Embora essas credenciais precisem ser criadas apenas uma vez, salve este arquivo para uso futuro por você mesmo ou por outros membros da equipe que possam precisar de acesso do {{site.data.keyword.event_streams}}.

   ```
   EVTSTREAMS_API_KEY="<the value of api_key>"    EVTSTREAMS_BROKER_URL="<all kafka_brokers_sasl values in a single string, separated by commas>"
   ```
   {: codeblock}
        
   Por exemplo, na área de janela de credenciais de visualização:

   ```
   EVTSTREAMS_BROKER_URL=broker-4-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-3-  x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-2-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-0-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-1-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093,broker-5-x7ztkttrm44911kc.kafka.svc01.us-south.eventstreams.cloud.ibm.com:9093
   ```
   {: codeblock}

9. Depois de criar o `event-streams.cfg`, configure essas variáveis de ambiente em seu shell:

   ```
   eval export $(cat event-streams.cfg)
   ```
   {: codeblock}

### Testando o {{site.data.keyword.message_hub_notm}} no {{site.data.keyword.cloud_notm}}
{: #testing}

1. Instale o `kafkacat` (https://linuxhostsupport.com/blog/how-to-install-apache-kafka-on-ubuntu-16-04/).

2. Em um terminal, insira o seguinte para inscrever-se no tópico `cpu2evtstreams`:

    ```
    kafkacat -C -q -o end -f "%t/%p/%o/%k: %s\n" -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

3. Em um segundo terminal, publique o conteúdo de teste no tópico `cpu2evtstreams` para exibi-lo no console original. Por exemplo:

    ```
    echo 'hi there' | kafkacat -P -b $EVTSTREAMS_BROKER_URL -X api.version.request=true -X security.protocol=sasl_ssl -X sasl.mechanisms=PLAIN -X sasl.username=token -X sasl.password=$EVTSTREAMS_API_KEY -t cpu2evtstreams
    ```
    {: codeblock}

## Registrando seu dispositivo de borda
{: #reg_device}

Para executar o exemplo de serviço cpu2evtstreams em seu nó de borda, deve-se registrar seu nó de borda com o padrão de implementação do `IBM/pattern-ibm.cpu2evtstreams`. Execute as etapas na seção **primeira** em [Horizon CPU Para {{site.data.keyword.message_hub_notm}}](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/README.md).

## Informações adicionais
{: #add_info}

O código-fonte de exemplo da CPU está disponível no  [{{site.data.keyword.horizon_open}}repositório de exemplos](https://github.com/open-horizon/examples) como um exemplo para o desenvolvimento de serviço de borda do {{site.data.keyword.edge_notm}}. Essa fonte inclui o código para todos os três serviços que são executados no nó de borda para este exemplo:

  * O serviço cpu que fornece dados da porcentagem de carregamento da CPU como um serviço REST em uma rede privada local do Docker. Para obter mais informações, consulte [Horizon CPU Percent Service](https://github.com/open-horizon/examples/tree/master/edge/services/cpu_percent).
  * O serviço de gps que fornece informações de localização a partir de hardware de GPS (se disponível) ou um local que é estimado a partir do endereço IP de nós de borda. Os dados da localização são fornecidos como um serviço REST em uma rede Docker privada local. Para obter mais informações, consulte [Horizon GPS Service)](https://github.com/open-horizon/examples/tree/master/edge/services/gps).
  * O serviço cpu2evtstreams que usa as APIs de REST que são fornecidas pelos outros dois serviços. Esse serviço envia os dados combinados para um broker de {{site.data.keyword.message_hub_notm}} kafka na nuvem. Para obter mais informações sobre o serviço, consulte [{{site.data.keyword.horizon}} CPU To {{site.data.keyword.message_hub_notm}} Service](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/cpu2evtstreams.md).
  * Para obter mais informações sobre o {{site.data.keyword.message_hub_notm}}, consulte [Event Streams - Visão geral](https://www.ibm.com/cloud/event-streams?mhsrc=ibmsearch_a&mhq=event%20streams).

## O que fazer em seguida
{: #cpu_next}

Se você deseja implementar seu próprio software em um nó de borda, deve criar seus próprios serviços de borda e padrão de implementação ou política de implementação associados. Para obter mais informações, consulte [Desenvolvendo um serviço de borda para dispositivos](../OH/docs/developing/developing.md).
