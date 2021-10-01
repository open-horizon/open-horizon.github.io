---

copyright:
years: 2020
lastupdated: "2020-03-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Processo de CI-CD para serviços de borda
{: #edge_native_practices}

Um conjunto de serviços de borda em evolução é essencial para o uso efetivo do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) e um robusto processo de Integração Contínua e Implementação Contínua (CI/CD) é um componente crítico. 

Use este conteúdo para organizar os blocos de construção disponíveis para você criar o seu próprio processo CI/CD. Em seguida, saiba mais sobre esse processo no repositório [`open-horizon/exemplos`](https://github.com/open-horizon/examples).

## Variáveis de Configuração
{: #config_variables}

Como um desenvolvedor de serviços de borda, considere o tamanho do contêiner de serviço em desenvolvimento. Com base nessas informações, talvez seja necessário dividir seus recursos de serviço em contêineres separados. Nessa situação, as variáveis de configuração que são usadas para fins de teste podem ajudar a simular dados que são provenientes de um contêiner ainda não desenvolvido. No [arquivo de definição de serviço cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json), é possível ver variáveis de entrada como **PUBLISH** e **MOCK**. Se você examinar o código `service.sh`, verá que ele usa essas variáveis e outras variáveis de configuração para controlar seu comportamento. O **PUBLISH** controla se o código tenta enviar mensagens para o IBM Event Streams. O **MOCK** controla se o service.sh tenta entrar em contato com as APIs de REST e seus serviços dependentes (cpu e gps) ou se o `service.sh` cria dados falsos.

No momento da implementação do serviço, é possível substituir os valores padrão da variável de configuração, especificando-os na definição do nó ou no comando `hzn register`.

## Compilação cruzada
{: #cross_compiling}

É possível usar o Docker para construir um serviço conteinerizado para diversas arquiteturas a partir de uma única máquina amd64. Da mesma forma, é possível desenvolver serviços de borda com linguagens de programação compiladas que suportam a compilação cruzada, como o Go. Por exemplo, se você estiver gravando código em seu Mac (um dispositivo de arquitetura amd64) para um dispositivo de braço (um Raspberry Pi), talvez seja necessário construir um contêiner do Docker que especifique parâmetros, como GOARCH, para o braço de destino. Este conjunto pode evitar erros de implementação. Consulte [open-horizon gps service](https://github.com/open-horizon/examples/tree/master/edge/services/gps).

## Teste
{: #testing}

O teste frequente e automatizado é uma parte importante do processo de desenvolvimento. Para facilitar o teste, é possível usar o comando `hzn dev service start` para executar o seu serviço em um ambiente de agente do Horizon simulado. Essa abordagem também é útil em ambientes DevOps nos quais pode ser problemático instalar e registrar o agente do Horizon completo. Este método automatiza os testes de serviços no repositório `open-horizon examples` com o destino **make test**. Consulte [make test target](https://github.com/open-horizon/examples/blob/305c4f375aafb09733f244ec9a899ce136b6d311/edge/services/helloworld/Makefile#L30).


Execute **make test** para construir e executar o serviço que usa **hzn dev service start**. Depois que estiver em execução, [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) irá monitorar os logs de serviço para localizar os dados que indicam que o serviço está executando corretamente.

## Testando a Implementação
{: #testing_deployment}

Quando você está desenvolvendo uma nova versão de serviço, o acesso a um teste completo do mundo real é ideal. Para isso, é possível implementar o seu serviço em nós de borda; no entanto, como este é um teste, talvez você não queira implementar inicialmente o seu serviço em todos os seus nós de borda.

Para isso, crie uma política de implementação ou padrão que faça referência apenas à sua nova versão de serviço. Em seguida, registre seus nós de testes com esta nova política ou padrão. Se estiver usando uma política, uma opção é configurar uma propriedade em um nó de borda. Por exemplo, "name": "mode", "value": "testing" e inclua essa restrição em sua política de implementação ("mode == testing"). Isso permite que você tenha certeza de que somente os nós que você separou para teste recebam a nova versão do seu serviço. 

**Nota**: também é possível criar um padrão ou uma política de implementação por meio do console de gerenciamento. Consulte [Usando o console de gerenciamento](../console/accessing_ui.md).

## Implementação de Produção
{: #production_deployment}

Depois de mover a nova versão de seu serviço de um ambiente de teste para produção, problemas que não foram encontrados durante o teste podem ocorrer. Suas configurações de retrocesso de política de implementação ou de padrão são úteis na resolução desses problemas. Em uma seção `serviceVersions` de padrão ou de política de implementação, é possível especificar várias versões mais antigas do seu serviço. Dê a cada versão uma prioridade para que o seu nó de borda retroceda se houver um erro com a sua nova versão. Além de designar uma prioridade a cada versão de retrocesso, é possível especificar itens, como o número e a duração de novas tentativas antes de efetuar fallback para uma versão de prioridade inferior do serviço especificado. Para obter a sintaxe específica, consulte [este exemplo de política de implementação](https://github.com/open-horizon/anax/blob/master/cli/samples/business_policy.json).

## Visualizando seus nós de borda
{: #viewing_edge_nodes}

Depois de implementar uma nova versão do seu serviço para nós, é importante que você seja capaz de monitorar o funcionamento de seus nós de borda facilmente. Use o {{site.data.keyword.ieam}} {{site.data.keyword.gui}} para esta tarefa. Por exemplo, quando você está no processo [Teste de implementação](#testing_deployment) ou [Implementação de produção](#production_deployment), é possível procurar rapidamente pelos nós que usam sua política de implementação ou nós com erros.

## Migrando serviços
{: #migrating_services}

Em algum momento, talvez seja necessário mover serviços, padrões ou políticas de uma instância do {{site.data.keyword.ieam}} para outra. Da mesma forma, talvez seja necessário mover serviços de uma organização do Exchange para outra. Isso pode acontecer se você instalou uma nova instância do {{site.data.keyword.ieam}} em um ambiente de host diferente. Como alternativa, poderá ser necessário mover serviços se você tiver duas instâncias do {{site.data.keyword.ieam}}, uma dedicada ao desenvolvimento e outra para produção. Para facilitar esse processo, é possível usar o script [`loadResources`)](https://github.com/open-horizon/examples/blob/master/tools/loadResources) no repositório de exemplos open-horizon.

## Teste de solicitação pull automatizado com o Travis
{: #testing_with_travis}

É possível automatizar testes sempre que uma solicitação pull (PR) for aberta para o seu repositório GitHub usando [Travis CI](https://travis-ci.com). 

Continue lendo este conteúdo para saber como alavancar o Travis e as técnicas no repositório GitHub de exemplos do open-horizon. 

No repositório de exemplos, o Travis CI é usado para construir, testar e publicar amostras. No arquivo [`.travis.yml`](https://github.com/open-horizon/examples/blob/master/.travis.yml), um ambiente virtual é configurado para ser executado como uma máquina Linux amd64 com hzn, Docker e [qemu](https://github.com/multiarch/qemu-user-static) para construção em múltiplas arquiteturas.

Neste cenário, o kafkacat também é instalado para permitir que o cpu2evtstreams envie dados para o IBM Event Streams. Semelhante ao uso da linha de comandos, o Travis pode usar variáveis de ambiente, como `EVTSTREAMS_TOPIC` e `HZN_DEVICE_ID`, para uso com os serviços de borda de amostra. O HZN_EXCHANGE_URL é configurado para apontar para a troca de preparação para publicação de quaisquer serviços modificados. 

O script [travis-localizar](https://github.com/open-horizon/examples/blob/master/tools/travis-find) é então usado para identificar serviços que foram modificados pela solicitação de pull aberto.

Se uma amostra tiver sido modificada, o destino `test-all-arches` no **makefile** desse serviço será executado. Com os contêineres qemu das arquiteturas suportadas em execução, as construções entre arquiteturas são executadas com este destino **makefile** configurando a variável de ambiente `ARCH` imediatamente antes da construção e do teste. 

O comando `hzn dev service start` executa o serviço de borda, e o arquivo [serviceTest.sh](https://github.com/open-horizon/examples/blob/master/tools/serviceTest.sh) monitora os logs de serviço para determinar se o serviço está operando corretamente.

Consulte [helloworld Makefile](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L24) para visualizar o destino dedicado `test-all-arches` Makefile.

O cenário a seguir demonstra um teste de ponta a ponta mais completo. Se uma das amostras modificadas incluir `cpu2evtstreams`, uma instância do IBM Event Streams pode ser monitorada em segundo plano e marcada para HZN_DEVICE_ID. Ela poderá passar no teste e ser incluída em uma lista de todos os serviços de passagem somente se ela localizar o ID do nó **travis-test** nos dados lidos a partir do tópico cpu2evtstreams. Isso requer uma chave de API do IBM Event Streams e uma URL do broker que são configuradas como variáveis de ambiente secreto.

Depois que o PR é mesclado, esse processo é repetido e a lista de serviços de passagem é usada para identificar quais serviços podem ser publicados no Exchage. As variáveis de ambiente secreto Travis que são usadas neste exemplo incluem tudo o que é necessário para enviar por push, assinar e publicar serviços no Exchange. Isso inclui as credenciais do Docker, o HZN_EXCHANGE_USER_AUTH e um par de chaves de assinatura criptográfico que pode ser obtido com o comando `hzn key create`. Para salvar as chaves de assinatura como variáveis de ambiente seguro, elas devem ser codificadas em base64.

A lista de serviços que passaram no teste funcional é usada para identificar quais serviços devem ser publicados com o destino de publicação de `Makefile` de publicação. Consulte [amostra helloworld](https://github.com/open-horizon/examples/blob/afd4a5822aede44616eb5da7cd9dafd4d78f12ec/edge/services/helloworld/Makefile#L45).

Como os serviços foram construídos e testados, este destino publica o serviço, a política de serviço, o padrão e a política de implementação em todas as arquiteturas no Exchange. 

**Nota**: além disso, é possível executar muitas dessas tarefas por meio do console de gerenciamento. Consulte [Usando o console de gerenciamento](../console/accessing_ui.md).

