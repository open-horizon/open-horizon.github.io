---

copyright:
years: 2019, 2020
lastupdated: "2020-02-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Melhores práticas de desenvolvimento de borda nativa
{: #edge_native_practices}

Você criará cargas de trabalho que operarão na borda – em instalações de cálculos externas aos limites normais do data center de TI ou do ambiente de nuvem. Isso significa que será necessário considerar as condições individuais desses ambientes. Isso é referido como o modelo de programação nativa de borda.

## Melhores práticas para desenvolver serviços de borda
{: #best_practices}

As melhores práticas e diretrizes a seguir ajudam a projetar e desenvolver serviços de borda a serem usados com o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

Automatizar a execução de serviços na borda é diferente de automatizar os serviços na nuvem, das seguintes maneiras:

* O número de nós de borda pode ser muito maior.
* As redes para os nós da borda podem ser não confiáveis e muito mais lentas. Os nós de borda estão frequentemente atrás de firewalls, portanto, as conexões geralmente não podem ser iniciadas a partir da nuvem para os nós de extremidade.
* Os nós de borda são restringidos por recursos.
* Um dos pontos fortes por trás da operação de cargas de trabalho na borda é a capacidade de reduzir a latência e otimizar a largura da banda da rede. Isso faz com que o posicionamento da carga de trabalho em relação ao local dos dados seja importante. 
* Geralmente, os nós de borda estão em locais remotos e não são configurados pela equipe de operações. Depois que um nó de borda é configurado, a equipe pode não estar disponível para administrar o nó.
* Geralmente os nós de borda também são ambientes menos confiáveis do que os servidores em nuvem.

Essas diferenças requerem o uso de diferentes técnicas para implementar e gerenciar o software nos nós de borda. O {{site.data.keyword.ieam}} foi projetado para gerenciar nós de borda. Quando estiver criando serviços, siga as orientações abaixo para assegurar que seus serviços sejam projetados para funcionar com nós de borda.

## Diretrizes para o desenvolvimento de serviços
{: #service_guidelines}


* **Modelo de programação nativa em nuvem:** o modelo de programação nativa em nuvem usa muitos princípios da programação nativa em nuvem, incluindo:

  * Divisão das cargas de trabalho em componentes e contêineres – construa o aplicativo centralizado em um conjunto de microsserviços, cada um deles empacotado em grupos logicamente relacionados, mas equilibrando esse agrupamento, de forma a reconhecer onde os diferentes contêineres podem apresentar melhor desempenho em diferentes camadas ou nós de borda.
  * Exposição de APIs aos microsserviços, permitindo que outras partes do aplicativo encontrem os serviços dos quais dependem.
  * Design loose coupling entre microsserviços para permitir que eles operem independentemente um do outro e para evitar suposições stateful que imponham afinidades entre os serviços que, de outra forma, prejudicariam o ajuste de escala elástico, o failover e a recuperação.
  * Exercício de integração contínua e implementação contínua (CI/CD), em conjunto com as práticas de Agile Development dentro de uma estrutura DevOps.
  * Considere os recursos a seguir para obter mais informações sobre as práticas de programação nativas em nuvem:
    * [10 ATRIBUTOS CHAVE DE APLICATIVOS NATIVOS NA NUVEM](https://thenewstack.io/10-key-attributes-of-cloud-native-applications/)
    * [Programação nativa na nuvem](https://researcher.watson.ibm.com/researcher/view_group.php?id=9957)
    *	[Entendendo os aplicativos nativos na nuvem](https://www.redhat.com/en/topics/cloud-native-apps)

* **Disponibilidade de serviço:** se o seu contêiner de serviço requerer e usar outros contêineres de serviço, o seu serviço deverá ser tolerante quando esses serviços estiverem ausentes em algumas situações. Por exemplo, quando os contêineres forem iniciados inicialmente, mesmo quando forem iniciados a partir do final do gráfico de dependência, no sentido de baixo para cima, alguns serviços poderão ser iniciados com uma rapidez maior do que outros. Nessa situação, os contêineres de serviço precisarão tentar novamente enquanto esperam que as dependências fiquem totalmente funcionais. Da mesma forma, se um contêiner de serviço dependente for atualizado automaticamente, ele será reiniciado. É uma melhor prática para seus serviços sempre ser tolerante às interrupções nos serviços dos quais ele depende.
* **Portabilidade:** o mundo da computação de borda abrange várias camadas do sistema – incluindo dispositivos de borda, clusters de borda e locais de borda de rede ou de metro. O local em que a carga de trabalho de borda conteinerizada será eventualmente colocada depende de uma combinação de fatores, incluindo sua dependência de determinados recursos, como dados de sensores e atuadores, requisitos de latência final e a capacidade de cálculo disponível. A carga de trabalho deve ser projetada para tolerar o uso em diferentes camadas do sistema, de acordo com as necessidades do contexto no qual o aplicativo será usado.
* **Orquestração do contêiner:** além do ponto anterior sobre a portabilidade multicamada, os dispositivos de borda normalmente serão operados com tempo de execução do Docker nativo, sem orquestração de contêiner local. Os clusters de borda e as bordas de rede e de metro serão configurados com o Kubernetes para orquestrar a carga de trabalho com relação às demandas de recurso concorrente compartilhado. O contêiner deve ser implementado de forma a evitar qualquer dependência explícita do Docker ou do Kubernetes, permitindo sua portabilidade para diferentes camadas do mundo da computação de borda distribuída. 
* **Exteriorização de parâmetros de configuração:** use o suporte integrado fornecido pelo {{site.data.keyword.ieam}} para exteriorizar todas as variáveis de configuração e dependências de recursos, para que possam ser fornecidas e atualizadas para os valores específicos para o nó no qual o contêiner está implementado.
* **Considerações de tamanho:** os seus contêineres de serviço devem ser os menores possível para que os serviços possam ser implementados em redes com probabilidade de lentidão ou em dispositivos de borda pequenos. Para ajudar a desenvolver contêineres de serviço menores, use as técnicas a seguir:

  * Use linguagens de programação que podem ajudá-lo a construir serviços menores:
    * As melhores: go, rust, c, sh
    * Aceitáveis: c++, python, bash
    * Considere: linguagens baseadas em nodejs, Java e JVM, como scala
  * Use técnicas que podem ajudar a construir imagens menores do Docker:
    * Use a alpine como a imagem base do {{site.data.keyword.linux_notm}}.
    * Para instalar pacotes em uma imagem baseada em alpine, use o comando `apk --no-cache --update add` para evitar o armazenamento do pacote em cache, que não é necessário para o tempo de execução.
    * Exclua os arquivos na mesma camada do Dockerfile (comando) onde os arquivos são incluídos. Se usar uma linha de comandos do Dockerfile separada para excluir os arquivos da imagem, você aumentará o tamanho da imagem do contêiner. Por exemplo, é possível usar `&&` para agrupar os comandos para fazer download, usar e, em seguida, excluir arquivos, tudo dentro de um único comando `RUN` do Dockerfile.
    * Não inclua as ferramentas de construção na imagem do Docker de tempo de execução. Como uma melhor prática, use uma [construção de vários estágios do Docker](https://docs.docker.com/develop/develop-images/multistage-build/) para construir os artefatos de tempo de execução. Em seguida, seletivamente, copie os artefatos de tempo de execução necessários, como os componentes executáveis, em sua imagem do Docker de tempo de execução.
* **Manter os serviços autocontidos:** como um serviço precisa ser enviado por meio de uma rede para nós de borda e iniciados de forma autônoma, o contêiner de serviço precisa incluir tudo aquilo de que o serviço depende. É necessário empacotar esses ativos, como todos os certificados necessários, para o contêiner. Não dependa da disponibilidade de administradores para concluir as tarefas para incluir os ativos necessários no nó de borda para que um serviço seja executado com sucesso.
* **Privacidade de dados:** cada vez que você move dados privados e sensíveis em torno da rede, você aumenta a vulnerabilidade desses dados para ataque e exposição. Como um de seus principais benefícios, a computação de borda permite manter esses dados onde foram criados. Use essa oportunidade em seu contêiner e proteja-o. Idealmente, não se deve transmitir dados para outros serviços. Caso seja absolutamente necessário transmitir dados para outros serviços ou camadas no sistema, tente remover as informações de identificação pessoal (PII), informações pessoais de saúde (PHI) ou informações pessoais financeiras (PFI), usando técnicas de ofuscação e de remoção de identificação ou criptografando-as com uma chave cuja propriedade seja completamente interna ao serviço. 
* **Projetar e configurar para automação:** os nós de borda e os serviços que são executados nos nós precisam ser o mais próximos de zero-ops possível. O {{site.data.keyword.ieam}} automatiza a implementação e o gerenciamento de serviços, mas os serviços devem ser estruturados para permitir que {{site.data.keyword.ieam}} seja capaz de automatizar esses processos sem intervenção humana. Para ajudá-lo a projetar para automação, siga as diretrizes a seguir:
  * Limite o número de variáveis de entrada do usuário de um serviço. Todas as variáveis UserInput sem valores padrão na definição de serviço requerem que os valores sejam especificados para cada nó de borda. Limite o número de variáveis ou evite usar variáveis, sempre que possível.  
  * Se algum serviço requerer muitas definições de configuração, use um arquivo de configuração para definir as variáveis. Inclua uma versão padrão do arquivo de configuração dentro do contêiner de serviço. Em seguida, use o sistema de gerenciamento de modelo {{site.data.keyword.ieam}} para permitir que o administrador forneça seu próprio arquivo de configuração e atualize-o ao longo do tempo.
  * **Uso de serviços de plataforma padrão:** muitos aplicativos podem ser atendidos por serviços de plataforma previamente implementados. Em vez de criar esses recursos no aplicativo do zero, considere usar aquilo que já foi criado e está à sua disposição. Uma origem desses serviços de plataforma incluir o IBM Cloud Pak, que abrange uma ampla gama de capacidades, muitas das quais foram construídas, elas próprias, usando práticas de programação nativas em nuvem, tais como:
    * **Gerenciamento de dados:** considere o IBM Cloud Pak for Data para seus requisitos de banco de dados de armazenamento SQL e não SQL de blocos e de objetos, serviços de aprendizado de máquina e IA e necessidades de data lake. 
    * **Segurança:** considere o IBM CloudPak for Security para as necessidades de criptografia, de varredura de código e de detecção de intrusão.
