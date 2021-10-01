---

copyright:
years: 2019
lastupdated: "2019-07-05"

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

O conteúdo a seguir fornece mais detalhes sobre as práticas de desenvolvimento de software e os conceitos para o desenvolvimento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

## Introdução
{: #developing_intro}

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) é construído no software livre [Open Horizon - Grupo de projetos EdgeX ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

Com o {{site.data.keyword.ieam}}, é possível desenvolver quaisquer contêineres de serviço que você deseje para suas máquinas de borda. Em seguida, é possível assinar criptograficamente e publicar seu código. Por fim, é possível especificar políticas dentro de um {{site.data.keyword.edge_deploy_pattern}} para controlar as açõpes de instalação, monitoramento e atualização de software. Depois de concluir essas tarefas, é possível visualizar o {{site.data.keyword.horizon_agents}} e o {{site.data.keyword.horizon_agbots}} formando contratos para colaborar no gerenciamento do ciclo de vida do software. Esses componentes passam então a gerenciar os detalhes do ciclo de vida do software em seus {{site.data.keyword.edge_nodes}} de forma totalmente independente, com base no padrão de implementação registrado para cada nó de borda. O {{site.data.keyword.ieam}} também pode usar políticas para determinar onde e quando implementar serviços e modelos de aprendizado de máquina de maneira autônima. As políticas são uma alternativa aos padrões de implementação.

O processo interno de desenvolvimento de software do {{site.data.keyword.ieam}} visa manter a segurança e a integridade do sistema, ao mesmo tempo, simplificando bastante o esforço necessário para o gerenciamento ativo de software nos nós de borda. O {{site.data.keyword.ieam}} também pode usar políticas para determinar onde e quando implementar serviços e modelos de aprendizado de máquina de maneira autônima. As políticas são uma alternativa aos padrões de implementação. É possível construir procedimentos de publicação do {{site.data.keyword.ieam}} em seu pipeline de integração e implementação contínuas. Ao descobrirem mudanças que foram publicadas no software ou em uma política, como dentro do {{site.data.keyword.edge_deploy_pattern}} ou da política de implementação, os agentes autônomos distribuídos atuam de forma independente para atualizar o software ou aplicar suas políticas em todo o conjunto de máquinas de borda, independentemente de onde estejam localizadas.

## Serviços e padrões de implementação
{: #services_deploy_patterns}

Os {{site.data.keyword.edge_services}} são os blocos de construção dos padrões de implementação. Cada serviço pode conter um ou mais contêineres do Docker. Cada contêiner do Docker pode, por sua vez, conter um ou mais processos de longa execução. Esses processos podem ser gravados em quase qualquer linguagem de programação e usar quaisquer bibliotecas ou utilitários. No entanto, os processos devem ser desenvolvidos e executados no contexto de um contêiner do Docker. Essa flexibilidade significa que quase não há nenhuma restrição no código que o {{site.data.keyword.ieam}} pode gerenciar para você. Quando um contêiner é executado, o contêiner é restringido em um ambiente de simulação seguro. Esse ambiente de simulação restringe o acesso aos dispositivos de hardware, alguns serviços do sistema operacional, o sistema de arquivos do host e as redes da máquina de borda do host. Para obter informações sobre as restrições do ambiente de simulação, consulte [Ambiente de simulação](#sandbox).

O código de exemplo `cpu2evtstreams` consiste em um contêiner do Docker que usa dois outros serviços de borda locais. Esses serviços de borda locais conectam-se por meio de redes virtuais do Docker privadas e locais usando APIs de REST HTTP. Esses serviços são denominados `cpu` e `gps`. O agente implementa cada serviço em uma rede privada separada juntamente com cada serviço que declarou uma dependência do serviço. Uma rede é criada para `cpu2evtstreams` e `cpu` e outra rede é criada para `cpu2evtstreams` e `gps`. Se houver um quarto serviço neste padrão de implementação que também esteja compartilhando o serviço `cpu`, outra rede privada será criada apenas para o `cpu` e o quarto serviço. No {{site.data.keyword.ieam}}, essa estratégia de rede restringe o acesso apenas aos outros serviços listados em `requiredServices` quando os outros serviços foram publicados. O diagrama a seguir mostra o padrão de implementação `cpu2evtstreams` quando o padrão é executado em um nó de borda:

<img src="../../images/edge/07_What_is_an_edge_node.svg" width="70%" alt="Serviços em um padrão">

Nota: a configuração do IBM Event Streams é necessária apenas para alguns exemplos.

As duas redes virtuais permitem que o contêiner de serviço `cpu2evtstreams` acesse as APIs de REST que são fornecidas pelos contêineres de serviço `cpu` e `gps`. Esses dois contêineres gerenciam o acesso aos serviços do sistema operacional e aos dispositivos de hardware. Embora as APIs de REST sejam usadas, há muitas outras formas possíveis de comunicação que podem ser usadas para permitir que os serviços compartilhem dados e controle.

Geralmente, o padrão de codificação mais efetivo para os nós de borda envolve a implementação de vários serviços pequenos, configuráveis e implementáveis de forma independente. Por exemplo, os padrões de Internet das Coisas geralmente possuem serviços de baixo nível que precisam de acesso ao hardware de nó de borda, como sensores ou atuadores. Esses serviços fornecem acesso compartilhado a esse hardware para outros serviços usarem.

Esse padrão é útil quando o hardware requer acesso exclusivo para fornecer uma função útil. O serviço de baixo nível pode gerenciar esse acesso adequadamente. A princípio, a função dos contêineres de serviço `cpu` e `gps` é semelhante à do software do driver de dispositivo no sistema operacional do host, mas em um nível superior. A segmentação do código em pequenos serviços independentes, alguns especializados em acesso a hardware de baixo nível, permite uma clara separação de interesses. Cada componente é livre para desenvolver-se e ser atualizado em campo de forma independente. Os aplicativos de terceiros também podem ser implementados com segurança juntamente com sua pilha de software integrada tradicional de proprietário, permitindo que eles acessem os hardwares ou outros serviços específicos de forma seletiva.

Por exemplo, um padrão de implementação de controlador industrial pode ser composto por um serviço de baixo nível para monitorar os sensores de uso de energia e outros serviços de baixo nível. Esses outros serviços de baixo nível podem ser usados para ativar o controle dos atuadores para ligar os dispositivos monitorados. O padrão de implementação também pode ter outro contêiner de serviço de nível superior que consuma os serviços do sensor e do atuador. Esse serviço de nível superior pode usar os serviços para alertar os operadores ou para desligar automaticamente os dispositivos quando são detectadas leituras anômalas de consumo de energia. Esse padrão de implementação também pode incluir um serviço de histórico que registra e arquiva os dados do sensor e do atuador e, possivelmente, a análise completa dos dados. Outros componentes úteis desse tipo de padrão de implementação podem ser um serviço de localização de GPS.

Cada contêiner de serviço individual pode ser atualizado independentemente com esse design. Cada serviço individual também pode ser reconfigurado e composto em outros padrões de implementação úteis sem quaisquer mudanças de código. Se necessário, um serviço de analítica de terceiros pode ser incluído no padrão. Esse serviço de terceiros pode receber acesso apenas a um determinado conjunto de APIs de somente leitura, que restringe a interação do serviço com os atuadores na plataforma.

Como alternativa, todas as tarefas neste exemplo do controlador industrial podem ser executadas dentro de um único contêiner de serviço. Normalmente, essa alternativa não é a melhor abordagem, pois uma coleção de serviços menores independentes e interconectados geralmente torna as atualizações de software mais rápidas e mais flexíveis. As coleções de serviços menores também podem ser mais robustas em campo. Para obter mais informações sobre como projetar padrões de implementação, consulte [Práticas de desenvolvimento nativas de borda](best_practices.md).

## Ambiente de Simulação
{: #sandbox}

O ambiente de simulação no qual os padrões de implementação são executados restringe o acesso às APIs que são fornecidas por seus contêineres de serviço. Somente os outros serviços que declaram explicitamente que dependem dos seus serviços têm permissão de acesso. Outros processos no host normalmente não acessam esses serviços. De forma semelhante, normalmente os outros hosts remotos não têm acesso a nenhum desses serviços, a menos que o serviço publique explicitamente uma porta para a interface de rede externa do host.

## Serviços que usam outros serviços
{: #using_services}

Os serviços de borda geralmente usam várias interfaces de API que são fornecidas por outros serviços de borda para adquirir dados deles ou para entregar comandos de controle para eles. Essas interfaces de API são geralmente APIs de REST HTTP, como aquelas fornecidas pelos serviços
`cpu` e `gps` de baixo nível no exemplo `cpu2evtstreams`. No entanto, essas interfaces podem ser realmente qualquer coisa desejada, como memória compartilhada, TCP ou UDP, e podem conter criptografia ou não. Como essas comunicações geralmente ocorrem dentro de um único nó de borda, sem que as mensagens saiam desse host, a criptografia é desnecessária.

Como alternativa às APIs de REST, é possível usar uma interface de publicação e assinatura, como a interface que é fornecida pelo MQTT. Quando um serviço fornece dados de forma intermitente apenas, uma interface de publicação e assinatura geralmente é mais simples do que a pesquisa repetida de uma API de REST, uma vez que as APIs de REST podem atingir o tempo limite. Por exemplo, considere um serviço que monitora um botão de hardware e fornece uma API a outros serviços para detectar se ocorreu um pressionamento de botão. Se uma API de REST for usada,
o responsável pela chamada não poderá chamar a API de REST e aguardará por uma resposta que viria quando o botão fosse pressionado. Se
o botão permanecesse não pressionado por muito tempo, a API de REST atingiria o tempo limite. Nesse caso, o provedor da API precisaria responder prontamente para evitar um erro. O responsável pela chamada deveria chamar repetidamente e frequentemente a API para ter certeza de não perder um pressionamento rápido de botão. Uma solução melhor seria o responsável pela chamada assinar um tópico apropriado em um serviço e um bloco de publicação e assinatura. Em seguida, o responsável pela chamada poderá esperar que algo seja publicado, o que poderá ocorrer muito depois. O provedor da API pode cuidar do monitoramento do hardware do botão e, em seguida, publicar somente as mudanças de estado nesse tópico, como `button pressed`ou `>button released`.

O MQTT é uma das ferramentas mais populares de publicação e assinatura que pode ser usada. É possível implementar um broker MQTT como um serviço de borda e fazer com que seus serviços de publicador e assinante o exijam. O MQTT também é usado frequentemente como um serviço de nuvem. O IBM Watson IoT Platform, por exemplo, usa o MQTT para comunicar-se com os dispositivos de IoT. Para obter mais informações, consulte [IBM Watson IoT Platform ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/cloud/watson-iot-platform). Alguns dos exemplos do projeto {{site.data.keyword.horizon_open}} usam o MQTT. Para obter mais informações, consulte exemplos do [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/examples).

Outra ferramenta popular de publicação e assinatura é o Apache Kafka, que também é usado frequentemente como um serviço de nuvem. O {{site.data.keyword.message_hub_notm}}, que é usado pelo exemplo `cpu2evtstreams` para enviar dados para o {{site.data.keyword.cloud_notm}}, também baseia-se em Kafka. Para obter mais informações, consulte [{{site.data.keyword.message_hub_notm}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/cloud/event-streams).

Qualquer contêiner de serviço de borda pode fornecer ou consumir outros serviços de borda locais no mesmo host e serviços de borda fornecidos em hosts vizinhos na LAN local. Os contêineres podem comunicar-se com sistemas centralizados em um data center corporativo remoto ou do provedor em nuvem. Como autor de serviço, você determina com quem e como seus serviços se comunicam.

Talvez você ache útil revisar o exemplo do `cpu2evtstreams` novamente para ver como o código de exemplo usa os outros dois serviços locais. Por exemplo, como o código de exemplo especifica as dependências dos dois serviços locais, declara e usa variáveis de configuração e comunica-se com o Kafka. Para obter mais informações, consulte [Exemplo do `cpu2evtstreams`](cpu_msg_example.md).

## Definição de Serviços
{: #service_definition}

Nota: consulte [Convenções usadas neste documento](../../getting_started/document_conventions.md) para obter mais informações sobre a sintaxe de comando.

Em cada projeto do {{site.data.keyword.ieam}}, há um arquivo `horizon/service.definition.json`. Esse arquivo define seu serviço de borda por dois motivos. Um desses motivos é permitir que você simule a execução de seu serviço pela ferramenta `hzn dev`, semelhante a como ele é executado no {{site.data.keyword.horizon_agent}}. Essa simulação é útil para trabalhar em quaisquer instruções de implementação especiais que você possa precisar, como ligações de porta e acesso ao dispositivo de hardware. A simulação também é útil para verificar as comunicações entre os contêineres de serviço nas redes privadas virtuais do Docker que o agente cria para você. O outro motivo desse arquivo é permitir que você publique seu serviço no {{site.data.keyword.horizon_exchange}}. Nos exemplos fornecidos, o arquivo `horizon/service.definition.json` é fornecido dentro do exemplo de repositório GitHub ou é gerado pelo comando `hzn dev service new`.

Abra o arquivo `horizon/service.definition.json` que contém os metadados do {{site.data.keyword.horizon}} de uma das implementações de serviço de exemplo, por exemplo, o [cpu2evtstreams](https://github.com/open-horizon/examples/blob/master/edge/evtstreams/cpu2evtstreams/horizon/service.definition.json).

Cada serviço que é publicado no {{site.data.keyword.horizon}} precisa ter uma `url` que o identifique exclusivamente dentro da organização. Este campo não é uma URL. Em vez disso, o campo `url` forma um identificador globalmente exclusivo, quando
combinado com seu nome de organização e os campos de implementação específicos `version` e `arch`. É possível editar o arquivo `horizon/service.definition.json` para fornecer valores apropriados para `url` e `version`. Para o valor de `version`, use um valor de estilo de versão semântica. Use os novos valores ao enviar por push, assinar e publicar seus contêineres de serviço. Como alternativa, é possível editar o arquivo `horizon/hzn.json` e as ferramentas substituirão os valores de variáveis que forem encontrados lá, no lugar de quaisquer referências de variáveis usadas no arquivo `horizon/service.definition.json`.

A seção `requiredServices` do arquivo `horizon/service.definition.json` detalha em itens quaisquer dependências de serviço, como outros serviços de borda que esse contêiner use. A ferramenta `hzn dev dependency fetch` faz com que você inclua dependências nesta lista, de modo que não é necessário editar manualmente a lista. Depois
que as dependências são incluídas, quando o agente executa o contêiner, aqueles outros `requiredServices` também são executados automaticamente (por exemplo, quando você usa `hzn dev service start` ou quando você registra um nó com um padrão de implementação que contém este serviço). Para obter mais informações sobre os serviços necessários, consulte [cpu2evtstreams](cpu_msg_example.md).

Na seção `userInput`, você declara as variáveis de configuração que seu serviço pode consumir para configurar-se para uma implementação específica. Aqui você fornece os nomes de variáveis, os tipos de dados e os valores padrão e também pode fornecer uma descrição legível por pessoas para cada item. Quando você usa o `hzn dev service start` ou quando registra um nó de borda com um padrão de implementação contendo esse serviço, é necessário fornecer um arquivo `userinput.json` para definir valores para as variáveis que não têm valores padrão. Para obter mais informações sobre as variáveis de configuração do `userInput` e os arquivos `userinput.json`, consulte [cpu2evtstreams](cpu_msg_example.md).

O arquivo `horizon/service.definition.json` também contém uma seção de `deployment`, em direção ao final do arquivo. Os campos nessa seção nomeiam cada imagem de contêiner do Docker que implementa o serviço lógico. O nome de cada registro que é usado aqui na matriz de `services` é o nome que os outros contêineres usam para identificar o contêiner na rede privada virtual compartilhada. Se esse contêiner fornecer uma API de REST para outros contêineres consumirem, será possível acessar essa API de REST dentro do contêiner de consumo usando `curl http://<name>/<your-rest-api-uri>`. O campo `image` para cada nome fornece uma referência à imagem do contêiner do Docker correspondente, como no DockerHub ou em algum registro de contêiner privado. Os outros campos na seção `deployment` podem ser usados para alterar a maneira que o agente indica que o Docker deve executar o contêiner. Para obter mais informações, consulte [Sequências de implementação do {{site.data.keyword.horizon}}![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/anax/blob/master/doc/deployment_string.md).

## Interagindo com o {{site.data.keyword.horizon_exchange}}
{: #horizon_exchange}

Ao construir e publicar os programas de exemplo, você interage com o {{site.data.keyword.horizon_exchange}} para publicar serviços, políticas e padrões de implementação. Você também usa o {{site.data.keyword.horizon_exchange}} para registrar os nós de borda para executar um determinado padrão de implementação. O {{site.data.keyword.horizon_exchange}} age como um repositório de informações compartilhadas, que permite a comunicação indireta com os outros componentes do {{site.data.keyword.ieam}}. Como desenvolvedor, é necessário entender como trabalhar com o {{site.data.keyword.horizon_exchange}}.

Esse diagrama mostra os agentes que devem estar em execução dentro de cada nó de borda, e os agbots que devem ser configurados para cada padrão de implementação, geralmente na nuvem ou em um data center corporativo centralizado.

Os desenvolvedores do {{site.data.keyword.ieam}} geralmente usam o comando `hzn` para interagir com o {{site.data.keyword.horizon_exchange}}. Especificamente, o comando `hzn exchange` é usado para todas as interações com o {{site.data.keyword.horizon_exchange}}. É possível digitar `hzn exchange --help` para ver todos os subcomandos que podem seguir o `hzn exchange` na linha de comandos. Em seguida, é possível usar o `hzn exchange <subcommand> --help` para obter mais detalhes sobre o `<subcommand>` da sua escolha.

Os comandos a seguir são úteis para interrogar o {{site.data.keyword.horizon_exchange}}:

* Verificar as credenciais do usuário funcionam no {{site.data.keyword.horizon_exchange}}: `hzn exchange user list`
* Verificar a versão do software do {{site.data.keyword.horizon_exchange}}: `hzn exchange version`
* Verificar o status atual do {{site.data.keyword.horizon_exchange}}: `hzn exchange status`
* Listar todos os nós de borda que são criados sob sua organização: `hzn exchange node list`
* Recuperar os detalhes de um nó de borda específico: `hzn exchange node list <node-id>` Substitua o `<node-id>` pelo valor de ID do nó de borda.
* Listar todos os serviços publicados sob sua organização: `hzn exchange service list`
* Listar todos os serviços públicos publicados sob qualquer organização: `hzn exchange service list '<org>/*'`
* Recuperar os detalhes de um serviço publicado específico: `hzn exchange service list <org/service>`
* Listar todos os padrões de implementação publicados sob sua organização: `hzn exchange pattern list`
* Listar todos os padrões de implementação públicos publicados em qualquer organização: `hzn exchange pattern list '<org>/*'`
* Listar todos os detalhes de um determinado serviço publicado: `hzn exchange pattern list <org/pattern>`

## Agentes e agbots
{: #agents_agbots}

É importante compreender as funções dos agentes e dos agbots e exatamente como eles se comunicam. Esse conhecimento pode ser útil para diagnosticar e corrigir problemas quando algo dá errado.

Os agentes e agbots nunca se comunicam diretamente entre si. O agente de cada nó de borda deve estabelecer uma caixa de correio para si no {{site.data.keyword.horizon_switch}} e criar um recurso de nó no {{site.data.keyword.horizon_exchange}}. Em seguida, quando ele desejar executar um determinado padrão de implementação, ele se registrará para este padrão no {{site.data.keyword.horizon_exchange}}.

Os robôs de contrato monitoram os padrões e procuram continuamente o {{site.data.keyword.horizon_exchange}} para localizar nós de borda que se registram para o padrão. Quando um novo nó de borda é registrado para usar um padrão, um robô de contrato atinge o agente local naquele nó de borda correspondente. O agbot acessa por meio do {{site.data.keyword.horizon_switch}}. Agora, tudo o que o robô de contrato pode saber sobre o agente é a sua chave pública. O agbot não sabe o endereço IP do nó de borda nem qualquer outra informação sobre o nó de borda que não seja o fato de que ele está registrado para o padrão de implementação específico. O robô de contrato se comunica com o agente, por meio do {{site.data.keyword.horizon_switch}}, para propor que eles colaborem para gerenciar o ciclo de vida de software desse padrão de implementação nesse nó de borda.

O agente para cada nó de borda monitora o {{site.data.keyword.horizon_switch}} para ver se há alguma mensagem em sua caixa de e-mail. Quando o agente recebe uma proposta de um robô de contrato, ele avalia essa proposta com base nas políticas que o proprietário do nó de borda definiu quando o nó de borda foi configurado e decide se aceitará ou rejeitará a proposta.

Quando uma proposta de padrão de implementação é aceita, o agente continua a puxar os contêineres de serviço apropriados do registro do Docker apropriado, verificar as assinaturas do serviço, configurar o serviço e executar o serviço.

Todas as comunicações entre os agentes e agbots que passam pelo {{site.data.keyword.horizon_switch}} são criptografadas pelos dois participantes. Mesmo que essas mensagens sejam armazenadas no {{site.data.keyword.horizon_switch}} central, o {{site.data.keyword.horizon_switch}} não será capaz de decriptografar e espionar o tráfego de rede dessas conversas.

## Implementando atualizações de software de serviço
{: #deploy_edge_updates}

Depois de implementar o software na frota de nós de borda, será possível atualizar o código. As atualizações de software podem ser realizadas com o {{site.data.keyword.ieam}}. Normalmente, não é necessário fazer nada nos nós de borda para atualizar o software que é executado neles. Assim que você assina e publica uma atualização, os agbots e os agentes executados em cada nó de borda coordenam a implementação da versão mais recente do seu padrão de implementação em cada nó de borda que está registrado para o padrão de implementação atualizado. Um dos principais benefícios do {{site.data.keyword.ieam}} é a simplicidade com a qual ele facilita um pipeline de atualização de software durante todo o processo até chegar nos nós de borda.

Para liberar uma nova versão do software, conclua as etapas a seguir: 

* Edite o código de serviço como você deseja para essa atualização.
* Edite o número da versão semântica do código.
* Reconstrua seus contêineres de serviço.
* Envie os contêineres de serviço atualizados por push para o registro do Docker apropriado.
* Assine e publique novamente os serviços atualizados no {{site.data.keyword.horizon_exchange}}.
* Publique novamente o padrão de implementação no {{site.data.keyword.horizon_exchange}}. Use o mesmo nome e referencie os novos números de versão do serviço.

Os agbots do {{site.data.keyword.horizon}} detectam rapidamente as mudanças no padrão de implementação. Em seguida, os robôs de contrato atingem cada agente cujo nó de borda está registrado para executar o padrão de implementação. O agbot e o agente coordenam o download dos novos contêineres, a interrupção e a remoção dos contêineres antigos e o início dos novos contêineres.

Esse processo faz com que cada um dos nós de borda registrados execute o padrão de implementação atualizado rapidamente para executar a nova versão do contêiner de serviço, independentemente de onde o nó de borda está localizado geograficamente.

## O que fazer a seguir
{: #developing_what_next}

Para obter mais informações sobre como desenvolver o código do nó de borda, revise a documentação a seguir:

[Práticas de desenvolvimento nativas de borda](best_practices.md)

Revise os princípios importantes e as melhores práticas para desenvolver serviços de borda para o desenvolvimento de software do {{site.data.keyword.ieam}} .

[Usando o {{site.data.keyword.cloud_registry}}](container_registry.md)

Com o {{site.data.keyword.ieam}}, é possível colocar opcionalmente os contêineres de serviço no registro do contêiner seguro e privado da IBM e não no Docker Hub público. Por exemplo, se houver uma imagem de software que inclua ativos cuja inclusão em um registro público não seja apropriada, será possível usar um registro de contêiner do Docker privado, como o {{site.data.keyword.cloud_registry}}.

[APIs](../installing/edge_rest_apis.md)

O {{site.data.keyword.ieam}} fornece APIs RESTful para permitir que os componentes colaborarem e que os desenvolvedores e usuários da organização controlem os componentes.
