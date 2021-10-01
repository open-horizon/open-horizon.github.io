---

copyright:
  years: 2020
lastupdated: "2020-05-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Usando Padrões
{: #using_patterns}

Geralmente, os padrões de implementação de serviço podem ser publicados no hub do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) depois que um desenvolvedor publica um serviço de borda no Horizon Exchange.

A CLI do hzn fornece recursos que permitem listar e gerenciar padrões no {{site.data.keyword.horizon_exchange}}, incluindo comandos para listar, publicar, verificar, atualizar e remover padrões de implementação de serviço. Por meio dela, também é possível listar e remover chaves criptográficas que estão associadas a um padrão de implementação específico.

Para obter uma lista completa de comandos da CLI, além de outros detalhes:

```
hzn exchange pattern -h
```
{: codeblock}

## Exemplo

Assine e crie (ou atualize) um recurso de padrão no {{site.data.keyword.horizon_exchange}}:

```
hzn exchange pattern publish --json-file=JSON-FILE [<flags>]
```
{: codeblock}

## Usando padrões de implementação

Usar um padrão de implementação é uma maneira direta e simples de implementar um serviço em seu nó de borda. O usuário especifica os serviços de nível superior a serem implementados no nó de borda e o {{site.data.keyword.ieam}} se encarrega do restante, incluindo a implementação de quaisquer serviços dependentes que os serviços de nível superior possam ter.

Depois de criar e incluir um serviço no {{site.data.keyword.ieam}} Exchange, é necessário criar um arquivo `pattern.json`, semelhante a:

```
{
  "name": "pattern-ibm.cpu2evtstreams-arm",
  "label": "Edge ibm.cpu2evtstreams Service Pattern for arm",
  "description": "Pattern for ibm.cpu2evtstreams for arm",
  "public": true,
  "services": [
    {
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceOrgid": "IBM",
      "serviceArch": "arm",
      "serviceVersions": [
        {
          "version": "1.4.3",
          "priority": {
            "priority_value": 1,
            "retries": 1,
            "retry_durations": 1800,
            "verified_durations": 45
          }
        },
        {
          "version": "1.4.2",
          "priority": {
            "priority_value": 2,
            "retries": 1,
            "retry_durations": 3600
          }
        }
      ]
    }
  ],
  "userInput": [
    {
      "serviceOrgid": "IBM",
      "serviceUrl": "ibm.cpu2evtstreams",
      "serviceVersionRange": "[0.0.0,INFINITY)",
      "inputs": [
        {
          "name": "EVTSTREAMS_API_KEY",
          "value": "$EVTSTREAMS_API_KEY"
        },
        {
          "name": "EVTSTREAMS_BROKER_URL",
          "value": "$EVTSTREAMS_BROKER_URL"
        },
        {
          "name": "EVTSTREAMS_CERT_ENCODED",
          "value": "$EVTSTREAMS_CERT_ENCODED"
        }
      ]
    }
  ]
}
```
{: codeblock}

Este código é um exemplo de um arquivo `pattern.json` para o serviço `ibm.cpu2evtstreams` para dispositivos `arm`. Conforme mostrado aqui, não é necessário especificar `cpu_percentual` e `gps` (serviços dependentes de `cpu2evtstreams`). Essa tarefa é executada pelo arquivo `service_definition.json`, portanto, um nó de borda que foi executado com êxito executa essas cargas de trabalho automaticamente.

O arquivo `pattern.json` permite customizar as configurações de retrocesso na seção `serviceVersions`. É possível especificar várias versões mais antigas do serviço e fornecer uma prioridade diferente para cada uma delas; essas prioridades são usadas pelo nó de borda se for necessário retroceder, caso a nova versão apresente erro. Além de designar uma prioridade a cada versão de retrocesso, é possível especificar itens, como o número e a duração de novas tentativas antes de efetuar fallback para uma versão de prioridade inferior do serviço especificado. 

Também é possível usar a seção `userInput`, próxima à parte inferior, para definir quaisquer variáveis de configuração de que o serviço possa precisar para que o funcionamento central seja correto ao implementar o padrão. Ao ser publicado, o serviço `ibm.cpu2evtstreams` transmite consigo as credenciais necessárias para a publicação de dados no IBM Event Streams, o que pode ser feito usando:

```
hzn exchange pattern publish -f pattern.json
```
{: codeblock}

Após a publicação do padrão, é possível, então, registrar nele um dispositivo arm:

```
hzn register -p pattern-ibm.cpu2evtstreams-arm
```
{: codeblock}

Este comando implementa `ibm.cpu2evtstreams` e quaisquer serviços dependentes no nó.

Nota: nenhum arquivo `userInput.json` é transmitido no comando `hzn register` acima, como aconteceria caso fossem seguidas as etapas nos exemplos de repositório [Usando a CPU para o IBM Event Streams Edge Service com exemplo de repositório ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/evtstreams/cpu2evtstreams#-using-the-cpu-to-ibm-event-streams-edge-service-with-deployment-pattern) do Padrão de implementação. Como as entradas do usuário são transmitidas com o próprio padrão, qualquer nó de borda que se registre automaticamente terá acesso a essas variáveis de ambiente.

Para interromper todas as cargas de trabalho de `ibm.cpu2evtstreams`, é possível cancelar o registro de:

```
hzn unregister -fD
```
{: codeblock}
