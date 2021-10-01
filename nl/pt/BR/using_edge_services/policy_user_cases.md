---

copyright:
  years: 2020
lastupdated: "2020-04-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Casos de uso de políticas de implementação
{: #developing_edge_services}

Esta seção destaca um cenário real, em que são descritos tipos de políticas.

<img src="../OH/docs/images/edge/04_Defining_an_edge_policy.svg" style="margin: 3%" alt="Defining an edge policy">

Suponha que um cliente tenha instalado câmeras em caixas eletrônicos para detectar roubos (o cliente também tem outros tipos de nós de borda). O cliente usa uma combinação de caixas eletrônicos convencionais (estáticos) e drive-through (movimento). Nesse caso, há dois serviços de terceiros disponíveis. Cada serviço pode detectar atividades suspeitas nos caixas eletrônicos, mas o teste do cliente determinou que o serviço atm1 detecta de forma mais confiável a atividade suspeita em caixas eletrônicos automáticos (estáticos) e o serviço atm2 detecta de forma mais confiável a atividade suspeita em caixas eletrônicos drive-through (movimento).

Para obter a implementação de serviço e de modelo desejada, a política é expressa assim:

* Configure as propriedades na política do nó em todos os caixas eletrônicos convencionais: propriedades: `camera-type: still`, `atm-type: walk-up`
* Configure as propriedades na política do nó em todos os caixas eletrônicos drive-through: propriedades: `camera-type: motion`, `atm-type: drive-thru`
* Opcionalmente, configure as restrições na política de serviço pelos desenvolvedores de terceiros do atm1 e atm2: restrições: `(Optional)`
* Configure as restrições na política de implementação definida pelo cliente para o serviço atm1: restrições: `camera-type == still`
* Configure as restrições na política de implementação definida pelo cliente para o serviço atm2: restrições: `camera-type == motion`

Nota: o comando `hzn` às vezes usa o termo política de negócios ao se referir à política de implementação.

A política de nó (definida pelo técnico que configura os caixas eletrônicos) informa fatos sobre cada nó; por exemplo, se o caixa eletrônico possui uma câmera e o tipo de local em que o caixa eletrônico está. Essas informações podem ser determinadas e especificadas com facilidade pelo técnico.

A política de serviço é uma instrução sobre o que o serviço requer para operar corretamente (neste caso, uma câmera). O desenvolvedor de serviços de terceiros conhece essas informações, embora não saiba qual cliente as está utilizando. Caso o cliente tenha outros caixas eletrônicos que não possuem câmeras, esses serviços não serão implementados neles, devido a essa restrição.

A política de implementação é definida pelo CIO do cliente (ou por quem estiver gerenciando sua malha de borda). Isso define a implementação geral do serviço para o negócio. Nesse caso, o CIO expressa o resultado esperado para a implementação do serviço, em que atm1 deve ser usado para caixas eletrônicos convencionais e atm2 deve ser usado para caixas eletrônicos em drive-through.

## Política de nó
{: #node_policy}

A política pode ser conectada a um nó. O proprietário do nó pode fornecê-la no horário de registro e ela pode ser mudada a qualquer momento diretamente no nó ou centralmente por um administrador do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Quando a política do nó é alterada de maneira central, isso é refletido para o nó na próxima vez em que este enviar pulsações para o hub de gerenciamento. Quando a política do nó é mudada diretamente no nó, as mudanças são imediatamente refletidas para o hub de gerenciamento, para que a implementação do serviço e do modelo possa ser prontamente reavaliada. Por padrão, um nó possui algumas [propriedades integradas](#node_builtins) que refletem a memória, a arquitetura e o número de CPUs. Opcionalmente, ele pode conter propriedades arbitrárias; por exemplo, o modelo do produto, dispositivos conectados, a configuração de software ou qualquer outra informação considerada relevante pelo proprietário do nó. É possível usar restrições de política para restringir os serviços que têm permissão de execução nesse nó. Cada nó possui apenas uma política que contém todas as propriedades e restrições que são designadas a esse nó.

## Política de Serviço
{: #service_policy}

Nota: a política de serviço é uma função opcional.

Como os nós, os serviços podem expressar políticas e ter também algumas [propriedades integradas](#service_builtins). Essa política é aplicada a um serviço publicado no Exchange e é criada pelo desenvolvedor de serviços. As propriedades da política de serviço poderiam indicar características do código de serviço que os autores de políticas do nó possam considerem relevantes. As restrições de políticas de serviço podem ser usadas para restringir onde e em qual tipo de dispositivo esse serviço pode ser executado. Por exemplo, o desenvolvedor de serviços pode afirmar que esse serviço requer uma determinada configuração de hardware, como restrições de CPU/GPU, restrições de memória, sensores específicos, autuadores e outros dispositivos periféricos. Geralmente, as propriedades e restrições permanecem estáticas por toda a duração do serviço, porque descrevem aspectos da implementação do serviço. Nos cenários de uso esperados, uma mudança em um desses aspectos geralmente coincide com mudanças de código que necessitam de uma nova versão de serviço. As políticas de implementação são usadas para capturar os aspectos mais dinâmicos da implementação de serviço, originários das necessidades de negócios.

## Política de implementação
{: #deployment_policy}

A política de implementação orienta a implementação do serviço. Como ocorre com outros tipos de política, ela contém um conjunto de propriedades e restrições, mas também contém outros itens. Por exemplo, ela identifica explicitamente um serviço a ser implementado e pode, opcionalmente, conter valores de variáveis de configuração, versões de retrocesso de serviço e informações de configuração de funcionamento do nó. A abordagem de política de Implementação para valores de configuração é útil porque essa operação pode ser executada centralmente, sem que seja necessário se conectar diretamente ao nó.

Os administradores podem criar uma política de implementação e o {{site.data.keyword.ieam}} usa essa política para localizar todos os dispositivos correspondentes às restrições definidas e implementa o serviço especificado nesses dispositivos, usando as variáveis de serviço configuradas na política. As versões de retrocesso de serviço instruem o {{site.data.keyword.ieam}} quanto às versões de serviço que devem ser implementadas em caso de falha na implementação de uma versão superior do serviço. A configuração de funcionamento do nó indica como o {{site.data.keyword.ieam}} deve medir o funcionamento (comunicação entre pulsações e o hub de gerenciamento) de um nó antes de determinar se o nó está fora da política.

Como as políticas de implementação capturam as propriedades e restrições de serviço mais dinâmicas e comerciais, espera-se que elas sofram mudanças mais frequentes do que uma política de serviço. O ciclo de vida delas é independente do serviço ao qual fazem referência, o que permite que o administrador da política verifique uma versão de serviço específica ou um intervalo de versão. Depois disso, o {{site.data.keyword.ieam}} mescla a política de serviço e a política de implementação e, em seguida, tenta localizar nós cuja política seja compatível a esses dados.

## Política de modelo
{: #model_policy}

Os dispositivos baseados em aprendizado de máquina (ML) requerem tipos de modelo específicos para operar corretamente e os clientes do {{site.data.keyword.ieam}} devem ser capazes de colocar modelos específicos nos mesmos nós ou em um subconjunto dos nós nos quais esses serviços foram colocados. A finalidade de uma política de modelo é limitar ainda mais o conjunto de nós no qual um determinado serviço é implementado, o que permite que um subconjunto desses nós receba um objeto de modelo específico, aplicando [Hello World usando o gerenciamento de modelo](../developing/model_management_system.md).

## Caso de uso da política estendida
{: #extended_policy_use_case}

No exemplo de caixas eletrônicos, o cliente opera caixas eletrônicos convencionais em áreas rurais pouco utilizadas. O cliente não deseja que os caixas eletrônicos rurais fiquem em execução continuamente e não deseja ativar o caixa eletrônico sempre que perceber que há um objeto próximo. Assim, o desenvolvedor de serviços inclui um modelo de ML no serviço atm1, que ativa o caixa eletrônico caso identifique uma pessoa se aproximando. Para implementar especificamente o modelo de ML nesses caixas eletrônicos rurais, configura-se a política:

* Política do nó nos caixas eletrônicos convencionais rurais: propriedades: `camera-type: still`, `atm-type: walk-up`, `location:  rural`
* Opcionalmente, as restrições da política de serviço definidas por desenvolvedores de terceiros para atm1 permanecem as mesmas: restrições: `(Optional)`
* A política de implementação definida pelo cliente para o serviço atm1 também permanece a mesma: restrições: `camera-type == still
* As restrições de política do modelo são configuradas por desenvolvedores de terceiros no objeto de MMS para o serviço atm1:

```
"destinationPolicy": {
  "constraints": [ "location == rural"  ],   "services": [        { "orgID": "$HZN_ORG_ID",          "serviceName": "atm1",          "arch": "$ARCH",            "version": "$VERSION"        }
  ]
}
```
{: codeblock}

Dentro do objeto de MMS, apolítica de modelo declara um serviço (ou uma lista de serviços) que pode acessar o objeto (nesse caso, atm1) e declara as propriedades e restrições que permitem que o {{site.data.keyword.ieam}} limite ainda mais o posicionamento correto do objeto nos caixas eletrônicos nas localidades rurais. Outros serviços executados no caixa eletrônico não poderão acessar o objeto.

## Propriedades
{: #properties}

Essencialmente, as propriedades são instruções de fatos, que são expressos como pares de name=value. As propriedades também são digitadas, o que permite a construção de expressões poderosas. As tabelas a seguir mostram os tipos de valores de propriedades que são suportados pelo {{site.data.keyword.ieam}} e as propriedades de políticas de nó e de serviço integradas. Os proprietários de nós, desenvolvedores de serviços e administradores de políticas de implementação podem definir propriedades individuais para atender às suas necessidades. Não é necessário definir as propriedades em um armazenador central; elas são configuradas e referenciadas (em expressões de restrições) conforme necessário.

|Tipos de valores de propriedades aceitos|
|-----------------------------|
|version - expressão decimal com pontos, que suporta uma, duas ou três partes; por exemplo, 1.2, 2.0.12, etc|
|string *|
|list of strings (sequências separadas por vírgulas)|
|integer|
|boolean|
|float|
{: caption="Tabela 1. Tipos de valores de propriedades aceitos"}

*Os valores de sequência que contêm espaços devem ser colocados entre aspas.

As propriedades integradas fornecem nomes bem definidos para propriedades comuns, para que todas as restrições possam se referir a elas da mesma maneira. Por exemplo, se um serviço precisar de `x` CPUs para ser executado corretamente ou de maneira eficiente, ele pode usar a propriedade `openhorizon.cpu` em sua restrição. A maioria dessas propriedades não pode ser configurada, mas, em vez disso, são lidas a partir do sistema subjacente e ignoram quaisquer valores configurados por um usuário.

### Propriedades integradas do nó
{: #node_builtins}

|Nome|Tipo|Descrição|Tipo de Política|
|----|----|-----------|-----------|
|openhorizon.cpu|Número Inteiro|O número de CPUs|Nó|
|openhorizon.memory|Número Inteiro|A quantidade de memória em MBs|Nó|
|openhorizon.arch|Sequência|A arquitetura de hardware do nó (por exemplo, amd64, armv6 e assim por diante)|Nó|
|openhorizon.hardwareId|Sequência|O número de série do hardware do nó, se disponível por meio da API do Linux; caso contrário, é um número aleatório com segurança de criptografia que não é alterado por toda a duração de um registro de nó|Nó|
|openhorizon.allowPrivileged|Booleano|Permite que os contêineres usem recursos privilegiados, como a execução privilegiada ou a conexão da rede do host ao contêiner.|Nó|
{: caption="Tabela 2. Propriedades integradas do nó"}

### Propriedades integradas do serviço
{: #service_builtins}

|Nome|Tipo|Descrição|Tipo de Política|
|----|----|-----------|-----------|
|openhorizon.service.url|Sequência|O nome exclusivo do serviço|Serviço|
|openhorizon.service.org|Sequência|A organização multilocatários na qual o serviço é definido*|Serviço|
|openhorizon.service.version|Versão|A versão de um serviço, usando a mesma sintaxe de versão semântica (por exemplo 1.0.0)|Serviço|
{: caption="Tabela 3. Propriedades integradas do serviço"}

*Em uma restrição, caso service.url seja especificado, mas service.org seja omitido, a organização é padronizada para a da política de nó ou de implementação que define a restrição.

## Restrições
{: #constraints}

No {{site.data.keyword.ieam}}, as políticas de nó, de serviço e de implementação podem definir restrições. As restrições são expressas como um predicado em um formato de texto simples e fazem referência a propriedades e seus valores ou a um intervalo de seus valores possíveis. As restrições também podem conter operadores booleanos, como AND (&&), OR (||) entre as expressões de propriedades e valores para a composição de cláusulas mais longas. Por exemplo, `openhorizon.arch == amd64 && OS == Mojave`. Além disso, é possível usar parênteses para criar uma precedência de avaliação dentro de uma única expressão.

|Tipo de valor de propriedade|Operadores Suportados|
|-------------------|-------------------|
|integer|==, <, >, <=, >=, =, !=|
|string *|==, !=, =|
|Lista de sequência de caracteres|em|
|Booleano|==, =|
|versão|==, =, in**|
{: caption="Tabela 4. Restrições"}

*Para os tipos de sequência, uma sequência de caracteres entre aspas, dentro da qual há uma lista de sequências separadas por vírgulas, fornece uma lista de valores aceitáveis; por exemplo, `hello == "beautiful, world"` será true se hello for "beautiful" ou "world".

**Para um intervalo de versão, use `in` em vez de `==`.

## Caso de uso de política ainda mais estendido
{: #extended_policy_use_case_more}

Para ilustrar todo o potencial da natureza bidirecional de uma política, considere o exemplo real nesta seção e inclua algumas restrições para o nó. Em nosso exemplo, suponhamos que alguns dos caixas eletrônicos convencionais nas áreas rurais estejam em locais próximos a leitos d'água, criando uma claridade que o serviço atm1 existente usado pelos demais caixas eletrônicos convencionais não consegue regular. Isso requer um terceiro serviço, que regule melhor a claridade para esses poucos caixas eletrônicos e a política é configurada da seguinte forma:

* Política de nó nos caixas eletrônicos convencionais à beira-mar: propriedades: `camera-type: still`, `atm-type: walk-up`; restrições: `feature == glare-correction`
* Opcionalmente, a política de serviço configurada pelos desenvolvedores de terceiros para atm3: restrições: `(Opcional)`
* Política de implementação definida pelo cliente para o serviço atm3: restrições: `camera-type == still`; propriedades: `feature: glare-correction`  

Novamente, a política do nó informa os fatos sobre o nó; no entanto, nesse caso, o técnico que configurou os caixas eletrônicos próximos a leitos d'água especificou uma restrição de que o serviço a ser implementado nesse nó deve ter o recurso de correção de claridade.

A política de serviço para atm3 possui a mesma restrição que as demais, que exige uma câmera no caixa eletrônico.

Como o cliente sabe que o serviço atm3 regula melhor a claridade, o cliente configura essa restrição na política de implementação associada ao atm3, que satisfaz o conjunto de propriedades no nó e resulta neste serviço que está sendo implementado nos ATMs frontais.

## Comandos de política
{: #policy_commands}

|Command|Descrição|
|-------|-----------|
|`hzn policy list`|A política deste nó de borda.|
|`hzn policy new`|Um modelo de política de nó vazio que pode ser preenchido.|
|`hzn policy update --input-file=INPUT-FILE`|Atualizar a política do nó. As propriedades integradas do nó são automaticamente incluídas caso não estejam contidas na política de entrada.|
|`hzn policy remove [<flags>]`|Remover a política do nó.|
|`hzn exchange node listpolicy [<flags>] <node>`|Exibir a política de nó do Horizon Exchange.|
|`hzn exchange node addpolicy --json-file=JSON-FILE [<flags>] <node>`|Incluir ou substituir a política de nó no Horizon Exchange.|
|`hzn exchange node updatepolicy --json-file=JSON-FILE [<flags>] <node>`|Atualizar um atributo da política para este nó no Horizon Exchange.|
|`hzn exchange node removepolicy [<flags>] <node>`|Remover a política de nó do Horizon Exchange.|
|`hzn exchange service listpolicy [<flags>] <service>`|Exibir a política de serviço do Horizon Exchange.|
|`hzn exchange service newpolicy`|Exibir um modelo de política de serviço vazio que possa ser preenchido.|
|`hzn exchange service addpolicy --json-file=JSON-FILE [<flags>] <service>`|Incluir ou substituir a política de serviço no Horizon Exchange.|
|`hzn exchange service removepolicy [<flags>] <service>`|Remover a política de serviço do Horizon Exchange.|
|`hzn exchange deployment listpolicy [<flags>] [<policy>]`|Exibir as políticas de negócios a partir do Horizon Exchange.|
|`hzn exchange deployment new`|Exibir um modelo de política de implementação vazio que possa ser preenchido.|
|`hzn exchange deployment addpolicy --json-file=JSON-FILE [<flags>] <policy>`|Incluir ou substituir uma política de implementação no Horizon Exchange. Use `hzn exchange deployment new` para um modelo de política de implementação vazio.|
|`hzn exchange deployment updatepolicy --json-file=JSON-FILE [<flags>] <policy>`|Atualizar um atributo de uma política de implementação existente no Horizon Exchange. Os atributos suportados são os atributos de nível superior na definição de política, conforme mostrado pelo comando `hzn exchange deployment new`.|
|`hzn exchange deployment removepolicy [<flags>] <policy>`|Remover a política de implementação no Horizon Exchange.|
|`hzn dev service new [<flags>]`|Criar um novo projeto de serviço. Esse comando gerará todos os arquivos de metadados de serviços do IEC, incluindo o modelo de política de serviço.|
|`hzn deploycheck policy [<flags>]`|Verificar a compatibilidade de política entre uma política de nó, de serviço e de implementação. Além disso, é possível usar `hzn deploycheck all` para verificar as configurações corretas de variável de serviço.|
{: caption="Tabela 5. Ferramentas de desenvolvimento de política"}

Consulte [Explorando o comando hzn](../cli/exploring_hzn.md) para obter mais informações sobre como usar o comando `hzn`.
