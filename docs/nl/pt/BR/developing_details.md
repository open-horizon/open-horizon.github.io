---

copyright:
years: 2021
lastupdated: "2021-02-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Detalhes do desenvolvimento
{: #developing}

O conteúdo a seguir fornece mais detalhes sobre as práticas de desenvolvimento de software e os conceitos para o desenvolvimento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}).
{:shortdesc}

## Introdução
{: #developing_intro}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.edge_abbr}}) é construído no software de código aberto [Open Horizon](https://www.lfedge.org/projects/openhorizon/).

Com o {{site.data.keyword.ieam}}, é possível desenvolver quaisquer contêineres de serviço que você deseje para suas máquinas de borda. É possível, então, assinar criptograficamente a configuração do contêiner e publicá-lo. Por fim, é possível implementar seus contêineres de serviço usando uma política ou padrão de implementação para controlar instalação de software, monitoramento e atualização. Depois de concluir essas tarefas, é possível visualizar o {{site.data.keyword.horizon_agents}} e o {{site.data.keyword.horizon_agbots}} formando contratos para colaborar no gerenciamento do ciclo de vida do software. Esses componentes gerenciam de forma autônoma os detalhes do ciclo de vida do software em seu {{site.data.keyword.edge_nodes}}. O {{site.data.keyword.ieam}} também pode usar políticas para implementar autonomamente modelos de aprendizado de máquina. Para obter informações sobre a implementação do modelo de aprendizado de máquina, consulte [Sistema de gerenciamento de modelos](model_management_system.md).

O processo interno de desenvolvimento de software do {{site.data.keyword.ieam}} visa manter a segurança e a integridade do sistema, ao mesmo tempo, simplificando bastante o esforço necessário para o gerenciamento ativo de software nos nós de borda. É possível construir procedimentos de publicação do {{site.data.keyword.ieam}} em seu pipeline de integração e implementação contínuas. Quando os agentes autônomos distribuídos descobrem mudanças publicadas no software ou em uma política, como dentro da política de {{site.data.keyword.edge_deploy_pattern}} ou de implementação, os agentes autônomos atuam de forma independente para atualizar o software e fazer cumprir suas políticas em toda a sua frota de máquinas de borda, onde quer que estejam localizados.

## Serviços
{: #services_deploy_patterns}

{{site.data.keyword.edge_services}} são os blocos de construção de soluções de borda. Cada serviço contém um ou mais contêineres do Docker. Cada contêiner do Docker pode, por sua vez, conter um ou mais processos de longa execução. Esses processos podem ser gravados em quase qualquer linguagem de programação e usar quaisquer bibliotecas ou utilitários. No entanto, os processos devem ser desenvolvidos e executados no contexto de um contêiner do Docker. Essa flexibilidade significa que quase não há nenhuma restrição no código que o {{site.data.keyword.ieam}} pode gerenciar para você. Quando um contêiner é executado, o contêiner é restringido em um ambiente de simulação seguro. Esse ambiente de simulação restringe o acesso a dispositivos de hardware, alguns serviços do sistema operacional, o sistema de arquivos do host, as redes da máquina de borda do host e, o mais importante, outros serviços em execução no nó de borda. Para obter informações sobre as restrições do ambiente de simulação, consulte [Ambiente de simulação](#sandbox).

O código de exemplo `cpu2evtstreams` consiste em um contêiner de Docker que usa dois outros serviços de borda. Esses serviços de borda se conectam sobre redes virtuais do Docker privado local usando APIs de REST HTTP. Esses serviços são denominados `cpu` e `gps`. O agente implementa cada serviço em uma rede privada separada juntamente com cada serviço que declarou uma dependência do serviço. Uma rede é criada para `cpu2evtstreams` e `cpu` e outra rede é criada para `cpu2evtstreams` e `gps`. Se houver um quarto serviço nesta implementação que também esteja compartilhando o serviço `cpu`, outra rede privada será criada para apenas a `cpu` e o quarto serviço. No {{site.data.keyword.ieam}}, essa estratégia de rede restringe o acesso apenas aos outros serviços listados em `requiredServices` quando os outros serviços foram publicados. O diagrama a seguir mostra a implementação do `cpu2evtstreams` quando o padrão é executado em um nó de borda:

<img src="../images/edge/07_What_is_an_edge_node.svg" style="margin: 3%" alt="Serviços em um padrão">

Nota: a configuração do IBM Event Streams é necessária apenas para alguns exemplos.

As duas redes virtuais permitem que o contêiner de serviço `cpu2evtstreams` acesse as APIs de REST que são fornecidas pelos contêineres de serviço `cpu` e `gps`. Esses dois contêineres gerenciam o acesso aos serviços do sistema operacional e aos dispositivos de hardware. Embora as APIs de REST sejam usadas, há muitas outras formas possíveis de comunicação que podem ser usadas para permitir que os serviços compartilhem dados e controle.

Geralmente, o padrão de codificação mais efetivo para os nós de borda envolve a implementação de vários serviços pequenos, configuráveis e implementáveis de forma independente. Por exemplo, os padrões de Internet das Coisas geralmente possuem serviços de baixo nível que precisam de acesso ao hardware de nó de borda, como sensores ou atuadores. Esses serviços fornecem acesso compartilhado a esse hardware para outros serviços usarem.

Esse padrão é útil quando o hardware requer acesso exclusivo para fornecer uma função útil. O serviço de baixo nível pode gerenciar esse acesso adequadamente. A princípio, a função dos contêineres de serviço `cpu` e `gps` é semelhante à do software do driver de dispositivo no sistema operacional do host, mas em um nível superior. A segmentação do código em pequenos serviços independentes, alguns especializados em acesso a hardware de baixo nível, permite uma clara separação de interesses. Cada componente é livre para desenvolver-se e ser atualizado em campo de forma independente. Os aplicativos de terceiros também podem ser implementados com segurança juntamente com sua pilha de software integrada tradicional de proprietário, permitindo que eles acessem os hardwares ou outros serviços específicos de forma seletiva.

Por exemplo, uma implementação do responsável pelo tratamento industrial pode ser composta por um serviço de baixo nível para monitoramento de sensores de uso de energia e outros serviços de baixo nível. Esses outros serviços de baixo nível podem ser usados para ativar o controle dos atuadores para ligar os dispositivos monitorados. A implementação também pode ter outro contêiner de serviço de alto nível que consome os serviços do sensor e atuador. Esse serviço de nível superior pode usar os serviços para alertar os operadores ou para desligar automaticamente os dispositivos quando são detectadas leituras anômalas de consumo de energia. Esta implementação também pode incluir um serviço de histórico que registra e arquivou os dados do sensor e do atuador e, possivelmente, completa análise sobre os dados. Outros componentes úteis de tal implementação podem ser um serviço de localização GPS.

Cada contêiner de serviço individual pode ser versionado de forma independente e atualizado com este design. Cada serviço individual também pode ser reconfigurado e composto em outras implementações úteis sem mudanças de código. Se necessário, um serviço de analítica de terceiros pode ser incluído na implementação. Este serviço de terceiros pode ter acesso a apenas um determinado conjunto de APIs somente leitura, o que evita que o serviço interaja com os atuadores na plataforma.

Como alternativa, todas as tarefas neste exemplo do controlador industrial podem ser executadas dentro de um único contêiner de serviço. Normalmente, essa alternativa não é a melhor abordagem, pois uma coleção de serviços menores independentes e interconectados geralmente torna as atualizações de software mais rápidas e mais flexíveis. As coleções de serviços menores também podem ser mais robustas em campo. Para obter mais informações sobre como projetar uma implementação, consulte [Práticas de desenvolvimento nativo da borda](best_practices.md).

## Ambiente de Simulação
{: #sandbox}

O ambiente de simulação em que implementações executam restringe o acesso a APIs que são fornecidas por outros contêineres de serviço. Somente os serviços que declaram dependências explicitamente em seus serviços têm permissão de acesso. Outros processos no host não conseguem acessar esses serviços. Da mesma forma, outros hosts remotos não podem acessar nenhum de seus serviços, a menos que seu serviço publique explicitamente uma porta para a interface de rede externa do host. As restrições de controle de acesso do ambiente de simulação são determinadas pela capacidade de endereçamento da rede, não por uma lista de controle de acesso administrada. Isso é feito criando redes virtuais para cada serviço, e apenas os contêineres de serviço que têm permissão para se comunicar são conectados à mesma rede. Isso alivia a necessidade de configurar o controle de acesso em cada nó de borda.

## Serviços que usam outros serviços
{: #using_services}

Os serviços de borda geralmente usam várias interfaces de API que são fornecidas por outros serviços de borda para adquirir dados deles ou para entregar comandos de controle para eles. Essas interfaces de API são geralmente APIs de REST HTTP, como aquelas fornecidas pelos serviços `cpu` e `gps` de baixo nível no exemplo `cpu2evtstreams`. No entanto, essas interfaces podem ser realmente qualquer coisa desejada, como memória compartilhada, TCP ou UDP, e podem conter criptografia ou não. Como essas comunicações geralmente ocorrem dentro de um único nó de borda, sem que as mensagens saiam desse host, a criptografia é desnecessária.

Como alternativa às APIs de REST, é possível usar uma interface de publicação e assinatura, como a interface que é fornecida pelo MQTT. Quando um serviço fornece dados somente de modo intermitente, geralmente uma interface de publicação e assinatura é uma alternativa mais simples do que pesquisar uma API de REST repetidamente, já que as APIs de REST podem atingir o tempo limite. Por exemplo, considere um serviço que monitora um botão de hardware e fornece uma API a outros serviços para detectar se ocorreu um pressionamento de botão. Se uma API de REST for usada, o responsável pela chamada não poderá simplesmente chamar a API de REST e aguardará uma resposta que seria recebida quando o botão fosse pressionado. Se o botão não fosse pressionado por muito tempo, a API de REST atingiria o tempo limite. Nesse caso, o provedor da API precisaria responder prontamente para evitar um erro. O responsável pela chamada deveria chamar repetidamente e frequentemente a API para ter certeza de não perder um pressionamento rápido de botão. Uma solução melhor seria o responsável pela chamada assinar um tópico apropriado em um serviço e um bloco de publicação e assinatura. Em seguida, o responsável pela chamada poderá esperar que algo seja publicado, o que poderá ocorrer muito depois. O provedor da API pode cuidar do monitoramento do hardware do botão e, em seguida, publicar somente as mudanças de estado nesse tópico, como `button pressed`ou `>button released`.

O MQTT é uma das ferramentas mais populares de publicação e assinatura que pode ser usada. É possível implementar um broker MQTT como um serviço de borda e fazer com que seus serviços de publicador e assinante o exijam. O MQTT também é usado frequentemente como um serviço de nuvem. O IBM Watson IoT Platform, por exemplo, usa o MQTT para comunicar-se com os dispositivos de IoT. Para obter mais informações, consulte [IBM Watson IoT Platform](https://www.ibm.com/cloud/watson-iot-platform). Alguns dos exemplos do projeto {{site.data.keyword.horizon_open}} usam o MQTT. Para obter mais informações, consulte exemplos do [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/examples).

Outra ferramenta popular de publicação e assinatura é o Apache Kafka, que também é usado frequentemente como um serviço de nuvem. O {{site.data.keyword.message_hub_notm}}, que é usado pelo exemplo `cpu2evtstreams` para enviar dados para o {{site.data.keyword.cloud_notm}}, também baseia-se em Kafka. Para obter informações adicionais, consulte [{{site.data.keyword.message_hub_notm}}](https://www.ibm.com/cloud/event-streams).

Qualquer contêiner de serviço de borda pode fornecer ou consumir outros serviços de borda locais no mesmo host e serviços de borda fornecidos em hosts vizinhos na LAN local. Os contêineres podem comunicar-se com sistemas centralizados em um data center corporativo remoto ou do provedor em nuvem. Como autor de serviço, você determina com quem e como seus serviços se comunicam. Ao se comunicar com os serviços do provedor em nuvem, use segredos para conter as credenciais de autenticação conforme descrito em [Desenvolvendo segredos](developing_secrets.md).

Talvez você ache útil revisar o exemplo do `cpu2evtstreams` novamente para ver como o código de exemplo usa os outros dois serviços locais. Por exemplo, como o código de exemplo especifica as dependências dos dois serviços locais, declara e usa variáveis de configuração e comunica-se com o Kafka. Para obter mais informações, consulte [Exemplo do `cpu2evtstreams`](cpu_msg_example.md).

## Serviços de modo privilegiado
{: #priv_services}
Em uma máquina host, algumas tarefas só podem ser executadas por uma conta com acesso raiz. O equivalente para contêineres é o modo privilegiado. Enquanto os contêineres geralmente não precisam de modo privilegiado no host, há alguns casos de uso em que ele é necessário. Em {{site.data.keyword.ieam}} você tem a capacidade de especificar que um serviço deve ser implementado com a execução de processo privilegiado ativada. Por padrão, ele está desativado. Deve-se ativá-lo explicitamente na [configuração de implementação](https://open-horizon.github.io/anax/deployment_string.html) do respectivo arquivo de Definição de Serviço para cada serviço que precisa executar neste modo. E mais adiante, qualquer nó sobre o qual você deseja implentar esse serviço deve também permitir explicitamente contêineres de modo privilegiado. Isso garante que os proprietários de nós tenham algum controle sobre quais serviços estão executando em seus nós de borda. Para obter um exemplo de como ativar a política de modo privilegiado em um nó de borda, consulte [política de nós privilegiados](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Se a definição de serviço ou uma de suas dependências requer o modo privilegiado, a política do nó também deve permitir o modo privilegiado ou então nenhum dos serviços não será implementado ao nó. Para uma discussão aprofundada sobre o modo privilegiado, veja [O que é o modo privilegiado e eu preciso dele?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).


## Definição de Serviços
{: #service_definition}

Nota: consulte [Convenções usadas neste documento](../getting_started/document_conventions.md) para obter mais informações sobre a sintaxe de comando.

Em cada projeto do {{site.data.keyword.ieam}}, há um arquivo `horizon/service.definition.json`. Este arquivo define seu serviço de borda para duas finalidades. Uma dessas finalidades é permitir que você simule a execução de seu serviço usando a ferramenta `hzn dev`. Esta ferramenta simula um ambiente de agente real incluindo o [Ambiente de simulação de rede](#sandbox). Essa simulação é útil para trabalhar em quaisquer instruções de implementação especiais que você possa precisar, como ligações de porta e acesso ao dispositivo de hardware. A simulação também é útil para verificar as comunicações entre os contêineres de serviço nas redes privadas virtuais do Docker que o agente cria para você. A outra razão para este arquivo é permitir que você publique seu serviço para o {{site.data.keyword.horizon_exchange}}. Nos exemplos fornecidos, o arquivo `horizon/service.definition.json` é fornecido dentro do exemplo de repositório GitHub ou é gerado pelo comando `hzn dev service new`.

Abra o arquivo `horizon/service.definition.json` que contém os metadados do {{site.data.keyword.horizon}} de uma das implementações de serviço de exemplo, por exemplo, o [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Todo serviço que é publicado em {{site.data.keyword.horizon}} precisa ter um nome que o identifique exclusivamente dentro de sua organização. O nome é colocado no campo `url` e forma um identificador exclusivo global quando combinado com seu nome de organização e uma `versão` e `arquitetura de hardware` de implementação específica. Para uma descrição completa da definição de serviço consulte [Definição de serviço](https://github.com/open-horizon/anax/blob/master/docs/service_def.md). O exemplo [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json) explora alguns recursos adicionais de uma definição de serviço básica como os serviços necessários e variáveis de serviço.

A seção `requiredServices` do arquivo `horizon/service.definition.json` relaciona quaisquer dependências de serviço que este serviço usa. A ferramenta `hzn dev dependency fetch` permite incluir dependências nesta lista, portanto, não é necessário editar manualmente a lista. Depois que dependências são incluídas, quando o agente executa o contêiner, aqueles outros `requiredServices` são executados automaticamente (por exemplo, quando você usa `hzn dev service start` ou quando você registra um nó ao qual este serviço é implementado). Para obter mais informações sobre os serviços necessários, consulte [Definição de Serviço](https://github.com/open-horizon/anax/blob/master/docs/service_def.md) e [cpu2evtstreams](cpu_msg_example.md).

Na seção `userInput`, você declara as variáveis de serviço que o seu Service pode consumir para configurar a si mesmo para uma determinada implementação. Você declara nomes de variáveis, tipos de dados e valores padrão aqui e você também pode fornecer uma descrição legível para cada um deles. Quando você usa `hzn dev service start` ou quando você registra um nó de borda no qual este serviço é implementado, é necessário configurar essas variáveis de serviço. O exemplo [cpu2evtstreams](cpu_msg_example.md) faz isso fornecendo um arquivo `userinput.json` durante o registro do nó. Também é possível configurar variáveis de serviço remotamente por meio do comando da CLI `hzn exchange node update -f <userinput-settings-file>`. Para obter mais informações sobre variáveis de serviço, consulte [Definição de serviço](https://github.com/open-horizon/anax/blob/master/docs/service_def.md) e [cpu2evtstreams](cpu_msg_example.md).

O arquivo `horizon/service.definition.json` também contém uma seção de `deployment`, em direção ao final do arquivo. Os campos nesta seção nomeia cada contêiner do Docker que implementa o seu Serviço lógico. O nome de cada contêiner na matriz `services` é o nome DNS que outros contêineres usam para identificar o contêiner na rede privada virtual compartilhada. Se esse contêiner fornecer uma API de REST para outros contêineres consumirem, será possível acessar essa API de REST dentro do contêiner de consumo usando `curl http://<name>/<your-rest-api-uri>`. O campo `image` para cada nome fornece uma referência à imagem do contêiner do Docker correspondente, como no DockerHub ou em algum registro de contêiner privado. Outros campos na seção `implementação` podem ser usados para configurar o contêiner com opções de tempo de execução que o Docker usa para executar o contêiner. Para obter mais informações, consulte [Configuração de implementação do {{site.data.keyword.horizon}}](https://github.com/open-horizon/anax/blob/master/docs/deployment_string.md).

## O que fazer em seguida
{: #developing_what_next}

Para obter mais informações sobre como desenvolver o código do nó de borda, revise a documentação a seguir:

* [Práticas de desenvolvimento nativas de borda](best_practices.md)

   Revise os princípios importantes e as melhores práticas para desenvolver serviços de borda para o desenvolvimento de software do {{site.data.keyword.ieam}} .

* [Usando o {{site.data.keyword.cloud_registry}}](container_registry.md)

  Com o {{site.data.keyword.ieam}}, é possível colocar opcionalmente os contêineres de serviço no registro do contêiner seguro e privado da IBM e não no Docker Hub público. Por exemplo, se houver uma imagem de software que inclua ativos cuja inclusão em um registro público não seja apropriada, será possível usar um registro de contêiner do Docker privado, como o {{site.data.keyword.cloud_registry}}.

* [APIs](../api/index.md)

  O {{site.data.keyword.ieam}} fornece APIs RESTful para colaboração e permite que os desenvolvedores e usuários de sua organização controlem os componentes.

* [Atualizando um serviço de borda com retrocesso](../using_edge_services/service_rollbacks.md)

  Revise os detalhes adicionais sobre como apresentar uma nova versão de um serviço de borda existente e as melhores práticas de desenvolvimento de software para atualizar as configurações de retrocesso no padrão ou nas políticas de implementação.
