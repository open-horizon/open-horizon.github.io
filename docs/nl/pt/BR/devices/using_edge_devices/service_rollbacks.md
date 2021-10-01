---

copyright:
years: 2020
lastupdated: "2020-03-30"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Atualizando um serviço de borda com retrocesso
{: #service_rollback}

Os serviços em nós de borda geralmente executam funções críticas, portanto, quando uma nova versão de um serviço de borda é apresentada para muitos nós de borda, é importante monitorar o sucesso da implementação e, caso ela falhe em qualquer nó de borda, o nó é revertido para a versão anterior do serviço de borda. O {{site.data.keyword.edge_notm}} pode fazer isso automaticamente. Em padrões ou políticas de implementação, é possível definir qual versão ou versões de serviço anterior devem ser usadas quando uma nova versão de serviço falha.

O conteúdo a seguir fornece detalhes adicionais sobre como apresentar uma nova versão de um serviço de borda existente e as melhores práticas de desenvolvimento de software para atualização das configurações de retrocesso no padrão ou nas políticas de implementação.

## Criando uma nova definição de serviço de borda
{: #creating_edge_service_definition}

Conforme explicado nas seções [Desenvolvendo serviços de borda com o {{site.data.keyword.edge_notm}}](../developing/developing.md) e [Detalhes do desenvolvimento](../developing/developing_details.md), as principais etapas para liberar uma nova versão de um serviço de borda são:

- Editar o código de serviço de borda conforme necessário para a nova versão.
- Editar o número da versão de semântica do código na variável de versão de serviço no arquivo de configuração **hzn.json**.
- Reconstrua seus contêineres de serviço.
- Designar e publicar a nova versão de serviço de borda no Horizon Exchange.

## Atualizando configurações de retrocesso no padrão ou na política de implementação
{: #updating_rollback_settings}

Um novo serviço de borda especifica seu número da versão no campo `version` da definição de serviço.  

Os padrões ou as políticas de implementação determinam quais serviços são implementados em quais nós de borda. Para
usar os recursos de retrocesso do serviço de borda, é necessário incluir a referência no seu novo número de versão de serviço na seção **serviceVersions** nos arquivos de configuração do padrão ou da política de implementação.

Quando um serviço de borda é implementado em um nó de borda como resultado de um padrão ou política, o agente implementa a versão de serviço com o valor de prioridade superior.

Por exemplo:

```json
 "serviceVersions": 
[
 {
   "version": "2.3.1",
   "priority": {
    "priority_value": 2,
    "retries": 1,
    "retry_durations": 1800
   }
 },
      {
        "version": "1.0.0",
   "priority": {
    "priority_value": 6,
    "retries": 1,
    "retry_durations": 2400
   }
  },
      {
        "version": "2.3.0",
   "priority": {
    "priority_value": 4,
    "retries": 1,
    "retry_durations": 3600
   }
  }
]
```
{: codeblock}

As variáveis adicionais são fornecidas na seção de prioridade. A propriedade `priority_value` configura a ordem de qual versão de serviço deve ser tentada primeiro; em termos práticos, um número inferior significa maior prioridade. O valor da variável `retries` define o número de vezes que o Horizon tentará iniciar esta versão de serviço dentro do intervalo de tempo que está especificado por `retry_durations` antes de retroceder para a próxima versão de prioridade mais alta. A variável `retry_durations` define o intervalo de tempo específico em segundos. Por exemplo, três falhas de serviço ao longo de um mês podem não garantir o retrocesso do serviço para uma versão anterior, mas três falhas dentro de cinco minutos podem ser uma indicação de que há algo errado com a nova versão de serviço.

Em seguida, publique novamente seu padrão de implementação ou atualize a política de implementação com as mudanças de seção **serviceVersion** no Horizon Exchange.

Observe que também é possível verificar a compatibilidade das atualizações das configurações de política de implementação ou de padrão com o comando `deploycheck` da CLI. Para visualizar mais detalhes, emita: 

```bash
hzn deploycheck -h
```
{: codeblock}

Os agbots do {{site.data.keyword.ieam}} detectam rapidamente as mudanças no padrão de implementação ou na política de implementação. Em seguida, os agbots chegam até cada agente cujo nó de borda está registrado para executar o padrão de implementação ou é compatível com a política de implementação atualizada. O agbot e o agente coordenam o download dos novos contêineres, a interrupção e a remoção dos contêineres antigos e o início dos novos contêineres.

Como resultado, seus nós de borda que estão registrados para executar o padrão de implementação atualizado ou são compatíveis com a política de implementação executarão rapidamente a nova versão de serviço de borda com o valor de prioridade superior, independentemente de onde o nó de borda estiver localizado geograficamente.  

## Visualizando o progresso da nova versão de serviço que está sendo retrocedida
{: #viewing_rollback_progress}

Consulte repetidamente os contratos do dispositivo até que os campos `agreement_finalized_time` e `agreement_execution_start_time` sejam preenchidos em: 

```bash
hzn agreement list
```
{: codeblock}

Observe que o contrato listado mostra a versão que está associada ao serviço e os valores de data e hora aparecem nas variáveis (por exemplo, "agreement_creation_time": "",)

Além disso, o campo de versão é preenchido com a nova versão de serviço (e operacional) com o valor de prioridade superior:

```json
[
  {
    …
    "agreement_creation_time": "2020-04-01 11:55:08 -0600 MDT",
    "agreement_accepted_time": "2020-04-01 11:55:17 -0600 MDT",
    "agreement_finalized_time": "2020-04-01 11:55:18 -0600 MDT",
    "agreement_execution_start_time": "2020-04-01 11:55:20 -0600 MDT",
    "agreement_data_received_time": "",
    "agreement_protocol": "Basic",
    "workload_to_run": {
      "url": "ibm.helloworld",
      "org": "ibm",
      "version": "2.3.1",
      "arch": "amd64"
    }
  }
]
```
{: codeblock}

Para obter detalhes adicionais, é possível inspecionar os logs do evento para o nó atual com o comando da CLI:

```bash
hzn eventlog list
```
{: codeblock}

Por último, também é possível usar o [console de gerenciamento](../getting_started/accessing_ui.md) para modificar as configurações de versões de implementação de retrocesso. É possível fazer isso ao criar uma nova política de implementação ou ao visualizar e editar os detalhes de política existentes incluindo configurações de retrocessos. Observe que o termo "intervalo de tempo" na seção de retrocesso da IU é equivalente a "retry_durations" na CLI.
