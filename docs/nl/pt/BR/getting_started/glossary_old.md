{:shortdesc: .shortdesc}
{:new_window: target="_blank"}

# Glossário
*Última atualização: 12 de março de 2020*

Este glossário fornece termos e definições para o {{site.data.keyword.edge}}.
{:shortdesc}

As referências cruzadas a seguir são utilizadas neste glossário:

- *Consulte* o encaminha de um termo não preferencial para um termo preferencial ou de uma abreviação para a sua forma por extenso.
- *Consulte também* o encaminha para um termo relacionado ou contrastante.

<!--If you do not want letter links at the top of your glossary, delete the text between these comment tags.-->

[A](#glossa)
[B](#glossb)
[C](#glossc)
[D](#glossd)
[E](#glosse)
[F](#glossf)
[G](#glossg)
[H](#glossh)
[I](#glossi)
[K](#glossk)
[L](#glossl)
[M](#glossm)
[N](#glossn)
[O](#glosso)
[P](#glossp)
[R](#glossr)
[S](#glosss)
[T](#glosst)
[V](#glossv)
[W](#glossw)

<!--end letter link tags-->

## A
{: #glossa}

### Chave API
{: #x8051010}

Um código exclusivo que é transmitido para uma API para identificar o aplicativo de chamada ou o usuário. Uma chave de API é usada para rastrear e controlar como a API está sendo usada, por exemplo, para evitar o uso malicioso ou abuso da API.

### aplicativo
{: #x2000166}

Um ou mais programas de computador ou componentes de software que
fornecem funcionalidade no suporte direto de um processo ou processos
de negócios específicos.

### zona de disponibilidade
{: #x7018171}

Um segmento de infraestrutura de rede designado pelo operador, funcionalmente independente.

## B
{: #glossb}

### nó de inicialização
{: #x9520233}

Um nó que é usado para executar instalação, configuração, ajuste de escala do nó e atualizações de cluster.

## C
{: #glossc}

### catálogo
{: #x2000504}

Um local centralizado que pode ser usado para procurar e instalar pacotes em um cluster.

### cluster
{: #x2017080}

Um conjunto de recursos, nós do trabalhador, redes e dispositivos de armazenamento que mantêm os aplicativos altamente disponíveis e prontos para implementação em contêineres.

### Container
{: #x2010901}

Uma construção do sistema que permite aos usuários executar instâncias do sistema operacional lógico separadas simultaneamente. Os contêineres usam camadas de sistemas de arquivos para minimizar os tamanhos de imagem e promover a reutilização. Veja também [imagem](#x2024928), [camada](#x2028320), [registro](#x2064940).

### Imagem de contêiner
{: #x8941555}

No Docker, software independente, executável, incluindo ferramentas de código e do sistema, que pode ser usado para executar um aplicativo.

### orquestração de contêiner
{: #x9773849}

O processo de gerenciamento do ciclo de vida de contêineres, incluindo fornecimento, implementação e
disponibilidade.

## D
{: #glossd}

### implementação
{: #x2104544}

Um processo que recupera pacotes ou imagens e os instala em um local definido para que ele possa ser testado ou executado.

### DevOps
{: #x5784896}

Uma metodologia de software que integra desenvolvimento de aplicativo e operações de TI para que as
equipes possam entregar código mais rápido para produção e iterar continuamente com base no feedback do
mercado.

### Docker
{: #x7764788}

Uma plataforma aberta que os desenvolvedores e administradores de sistema podem usar para construir, enviar e executar aplicativos distribuídos.

## E
{: #glosse}

### computação de borda
{: #x9794155}

Um modelo de computação distribuída que aproveita a computação
disponível fora dos datacenters tradicionais e em nuvem. Um modelo de computação de borda coloca uma carga de trabalho mais próxima de onde os dados associados são criados e onde as ações são executadas em resposta à análise desses dados. A colocação de dados e de cargas de trabalho em
dispositivos de borda reduz as latências, diminui as demandas na
largura da banda da rede, aumenta a privacidade de informações
confidenciais e ativa as operações durante as interrupções da rede.

### dispositivo de borda
{: #x2026439}

Um equipamento, como uma máquina de montagem em uma fábrica, uma ATM, uma câmera inteligente ou um automóvel, com
capacidade de computação integrada na qual um trabalho
significativo pode ser executado e dados podem ser coletados ou
produzidos.

### gateway de borda
{: #x9794163}

Um cluster de borda que possui serviços que executam funções de rede, como conversão de protocolo, terminação de rede, tunelamento, proteção de firewall ou conexões sem fio. Um gateway de borda serve como o ponto de conexão entre um dispositivo de borda ou cluster de borda e a nuvem ou uma rede maior.

### nó de borda
{: #x8317015}

Qualquer dispositivo de borda, cluster de borda ou gateway de borda onde a computação de borda ocorre.

### cluster de borda
{: #x2763197}

Um computador em um recurso de operações remotas que executa
cargas de trabalho do aplicativo corporativo e serviços
compartilhados. Um cluster de borda pode ser usado para conectar-se a um dispositivo de borda, conectar-se a outro cluster de borda ou servir como um gateway de borda para conectar-se à nuvem ou a uma rede maior.

### serviço de borda
{: #x9794170}

Um serviço que é projetado especificamente para ser implementado em um cluster de borda, gateway de borda ou dispositivo de borda. Reconhecimento visual, insights acústicos e reconhecimento de voz são exemplos de possíveis serviços de borda.

### carga de trabalho de borda
{: #x9794175}

Qualquer serviço, microsserviço ou parte de software que
executa um trabalho significativo quando executado em um nó de borda.

### terminal
{: #x2026820}

Um endereço de destino de rede que é exposto pelos recursos do Kubernetes, como serviços e ingressos.

## F
{: #glossf}

## G
{: #glossg}

### Grafana
{: #x9773864}

Uma plataforma de análise de dados e de visualização de software livre para
monitorar, procurar, analisar e visualizar métricas.

## H
{: #glossh}

### HA
{: #x2404289}

Veja [alta disponibilidade](#x2284708).

### Gráfico do Helm
{: #x9652777}

Um pacote do Helm que contém informações para instalar um conjunto de recursos do Kubernetes em um cluster do Kubernetes.

### Liberação do Helm
{: #x9756384}

Uma instância de um gráfico do Helm que é executado em um cluster do Kubernetes.

### Repositório do Helm
{: #x9756389}

Uma coleção de gráficos.

### alta disponibilidade (HA)
{: #x2284708}

A habilidade de serviços de TI para suportar todas as indisponibilidades e continuar a fornecer recursos de processamento, de acordo com algum nível de serviço predefinido. As interrupções cobertas incluem eventos planejados, como manutenção e backups, e
eventos não planejados, como falhas de software, falhas de hardware, quedas de energia e
desastres. Veja também [tolerância a falhas](#x2847028).

## I
{: #glossi}

### IBM Cloud Pak
{: #x9773840}

Um pacote de uma ou mais ofertas do IBM Certified Container, comerciais, seguras e gerenciadas pelo ciclo de vida, que são empacotadas juntas e integradas no ambiente do IBM Cloud.

### imagem
{: #x2024928}

Um sistema de arquivos e seus parâmetros de execução usados dentro de um tempo de execução do contêiner para criar um contêiner. O sistema de arquivos consiste em uma série de camadas, combinadas no tempo de execução, que são criadas à medida que a imagem é construída por atualizações sucessivas. A imagem não retém o estado à medida que o contêiner é executado. Consulte também [contêiner](#x2010901), [camada](#x2028320), [registro](#x2064940).

### registro de imagem
{: #x3735328}

Um local centralizado para gerenciamento de imagens.

### ingresso
{: #x7907732}

Uma coleção de regras para permitir conexões de entrada com os serviços de cluster do Kubernetes.

### isolamento
{: #x2196809}

O processo de confinamento de implementações de carga de trabalho para recursos virtuais e físicos dedicados para obter suporte de ocupação variada.

## K
{: #glossk}

### Klusterlet
{: #x9773879}

No IBM Multicloud Manager, o agente que é responsável por um único cluster do Kubernetes.

### Kubernetes
{: #x9581829}

Uma ferramenta de orquestração de software livre para contêineres.

## L
{: #glossl}

### camada
{: #x2028320}

Uma versão mudada de uma imagem pai. As imagens consistem em camadas, em que a versão é disposta em camadas na parte superior da imagem pai para criar a nova imagem. Consulte também [contêiner](#x2010901), [imagem](#x2024928).

### equilibrador de carga
{: #x2788902}

Um software ou hardware que distribui a carga de trabalho em um conjunto de servidores para garantir que estes não sejam sobrecarregados. O balanceador de carga também direciona os usuários a outro servidor se o servidor inicial falhar.

## M
{: #glossm}

### console de gerenciamento
{: #x2398932}

A interface gráfica com o usuário para o {{site.data.keyword.edge_notm}}.

### hub de gerenciamento
{: #x3954437}

O cluster que hospeda os componentes centrais do {{site.data.keyword.edge_notm}}.

### marketplace
{: #x2118141}

Uma lista de serviços ativados a partir dos quais os usuários podem provisionar recursos.

### nó mestre
{: #x4790131}

Um nó que fornece serviços de gerenciamento e controla os nós do trabalhador em um cluster. Os nós principais hospedam processos que são responsáveis pela alocação de recursos, manutenção do estado, planejamento e monitoramento.

### microsserviço
{: #x8379238}

Um conjunto de componentes arquitetônicos pequeno e independente,
cada um com um único propósito, que comunica-se por uma API leve
comum.

### multicloud
{: #x9581814}

Um modelo de computação em nuvem no qual uma empresa usa uma combinação de arquitetura local, de nuvem privada e de nuvem pública.

## N
{: #glossn}

### namespace
{: #x2031005}

Um cluster virtual dentro de um cluster do Kubernetes que pode ser usado para organizar e dividir
recursos entre múltiplos usuários.

### Network File System (NFS)
{: #x2031282}

Um protocolo que permite que um computador acesse arquivos por meio de uma rede
como se eles estivessem em seus discos locais.

### NFS
{: #x2031508}

Consulte  [ Network File System ](#x2031282).

## O
{: #glosso}

### org
{: #x7470494}

Consulte [organização](#x2032585).

### organização (org)
{: #x2032585}

O metaobjeto mais importante na infraestrutura do {{site.data.keyword.edge_notm}}, que representa os objetos de um cliente.

## P
{: #glossp}

### volume persistente
{: #x9532496}

Armazenamento de rede em um cluster que é provisionado por um administrador.

### solicitação de volume persistente
{: #x9520297}

Uma solicitação para armazenamento em cluster.

### política de implementação
{: #x7244520}

Uma política que define onde os serviços de borda devem ser executados.

### conjunto
{: #x8461823}

Um grupo de contêineres que estão em execução em um cluster do Kubernetes. Um pod é uma unidade de
trabalho executável, que pode ser um aplicativo independente ou um microsserviço.

### política de segurança do pod
{: #x9520302}

Uma política que é usada para configurar o controle de nível de cluster sobre o que um pod pode fazer ou o que ele pode acessar.

### Prometheus
{: #x9773892}

Um kit de ferramentas de monitoramento e alerta de sistemas de software livre.

### nó do proxy
{: #x6230938}

Um nó que transmite solicitações externas para os serviços que são criados dentro de um cluster.

## R
{: #glossr}

### RBAC
{: #x5488132}

Consulte [Controle de Acesso Baseado na Função](#x2403611).

### registro
{: #x2064940}

Um serviço de armazenamento e distribuição de imagem de contêiner público ou privado. Consulte também [contêiner](#x2010901), [imagem](#x2024928).

### repo
{: #x7639721}

Consulte [repositório](#x2036865).

### repositório (repo)
{: #x2036865}

Uma área de armazenamento persistente para dados e outros recursos de aplicativos.

### recurso
{: #x2004267}

Um componente físico ou lógico que pode ser fornecido ou reservado para um aplicativo ou instância de serviço. Exemplos de recursos incluem banco de dados, contas e processador, memória e limites de armazenamento.

### controle de acesso baseado na função (RBAC)
{: #x2403611}

O processo de restringir os componentes integrais de um sistema baseado na autenticação
do usuário, funções e permissões.

## S
{: #glosss}

### broker de serviço
{: #x7636561}

Um componente de um serviço que implementa um ampère de ofertas e planos de serviços, e interpreta chamadas para provisionamento e desprovisionamento, vinculação e desvinculação.

### nó de armazenamento
{: #x3579301}

Um nó que é usado para fornecer o armazenamento de backend e o sistema de arquivos para armazenar os dados em um sistema.

### syslog
{: #x3585117}

Consulte [log do sistema](#x2178419).

### log do sistema (syslog)
{: #x2178419}

Um log que é produzido por componentes do Cloud Foundry.

## T
{: #glosst}

### equipe
{: #x3135729}

Uma entidade que agrupa usuários e recursos.

## V
{: #glossv}

### VSAN
{: #x4592600}

Consulte [rede da área de armazenamento virtual](#x4592596).

## W
{: #glossw}

### nó do trabalhador
{: #x5503637}

Em um cluster, uma máquina física ou virtual que contém as implementações e serviços que formam um aplicativo.

### carga de trabalho
{: #x2012537}

Uma coleção de servidores virtuais que são executados com um propósito coletivo definido pelo cliente. Uma carga de trabalho geralmente pode ser visualizada como um aplicativo com multicamadas. Cada carga de trabalho é associada a um conjunto de políticas que definem os objetivos de desempenho e de consumo de energia.
