---

copyright:
years: 2020
lastupdated: "2020-4-8"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Clusters de borda
{: #edge_clusters}

Em construção; conteúdo proveniente de: https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/servers/overview.html

A computação de borda aproxima os aplicativos corporativos dos locais nos quais os dados são criados.
{:shortdesc}

  * [Visão geral](#overview)
  * [Benefícios da computação de borda](#edge_benefits)
  * [Exemplos](#examples)
  * [Arquitetura](#edge_arch)
  * [Conceitos ](#concepts)

## Visão geral
{: #overview}

A computação de borda é um novo paradigma importante que pode expandir o modelo operacional por meio da virtualização da nuvem para além de um data center ou de um centro de computação em nuvem. Ela move as cargas de trabalho de aplicativos de um local centralizado para locais remotos, como fábricas, armazéns, centros de distribuição, lojas de varejo, centros de transporte e outros. Basicamente, a computação de borda oferece a capacidade de mover cargas de trabalho de aplicativos para qualquer lugar em que a computação seja necessária fora de seus data centers e do ambiente de hospedagem de nuvem.

O {{site.data.keyword.edge_servers_notm}} fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho a partir de um cluster de hub para instâncias remotas do {{site.data.keyword.icp_server}} ou outros clusters baseados no Kubernetes.

O {{site.data.keyword.edge_servers_notm}} usa o {{site.data.keyword.mcm_core_notm}} para controlar a implementação de cargas de trabalho conteinerizadas para os servidores de borda, gateways e dispositivos hospedados pelos clusters do {{site.data.keyword.icp_server}} em locais remotos.

O {{site.data.keyword.edge_servers_notm}} também inclui suporte para um {{site.data.keyword.edge_profile}}. Esse perfil suportado pode ajudar a reduzir o uso de recurso do {{site.data.keyword.icp_server}} quando o {{site.data.keyword.icp_server}} é instalado para ser usado na hospedagem de um servidor de borda remoto. Esse perfil coloca nele os serviços mínimos necessários para suportar o gerenciamento remoto robusto desses ambientes de servidor e os aplicativos corporativos críticos que você está hospedando. Com esse perfil, você ainda é capaz de autenticar usuários, coletar dados de log e de evento e implementar cargas de trabalho em um único nó do trabalhador ou em um conjunto de clusters.

## Benefícios da computação de borda
{: #edge_benefits}

* Mudança de valor agregado para a organização: a transferência das cargas de trabalho de aplicativo para os nós de borda para operações de suporte em locais remotos onde os dados são coletados, em vez de enviar os dados para o data center central para processamento.

* Reduza as dependências da equipe de TI: o uso do {{site.data.keyword.edge_servers_notm}} pode ajudá-lo a reduzir as dependências da equipe de TI. Com o {{site.data.keyword.edge_servers_notm}}, é possível implementar e gerenciar cargas de trabalho críticas em servidores de borda com segurança e confiança para centenas de locais remotos a partir de um local central, sem exigir que uma equipe de TI em tempo integral seja implementada em cada um dos locais remotos para gerenciar as cargas de trabalho no local.

## Exemplos
{: #examples}

A computação de borda aproxima os aplicativos corporativos dos locais nos quais os dados são criados. Por exemplo, se você opera uma fábrica, os equipamentos da fábrica podem incluir sensores para registrar qualquer número de pontos de dados que forneçam detalhes sobre como a fábrica está operando. Os sensores podem registrar o número de peças que estão sendo montadas por hora, o tempo necessário para que um empilhador retorne à posição inicial ou a temperatura de operação de uma máquina fabricada. As informações desses pontos de dados podem ser benéficas para ajudá-lo a determinar se você está operando em uma eficiência de pico, identificar os níveis de qualidade que você está alcançando ou prever quando uma máquina provavelmente falhará e exigirá manutenção preventiva.

Em outro exemplo, se houver trabalhadores em locais remotos cuja tarefa possa resultar no trabalho em situações perigosas, como ambientes quentes ou com barulho muito alto, proximidade de gases de escape ou de produção ou máquinas pesadas, poderá ser necessário monitorar as condições do ambiente. É possível coletar informações de várias origens que podem ser usadas em locais remotos. Os dados desse monitoramento podem ser usados pelos supervisores para determinar quando instruir os trabalhadores a fazer pausas, tomar água ou encerrar o equipamento.

Em um outro exemplo, é possível usar câmeras de vídeo para monitorar propriedades, como para identificar o tráfego de pessoas em lojas de varejo, restaurantes ou locais de entretenimento, para funcionar como um monitor de segurança para registrar atos de vandalismo ou outras atividades indesejadas ou para reconhecer condições de emergência. Se você também coletar dados dos vídeos, será possível usar a computação de borda para processar a análise de vídeo localmente para ajudar os trabalhadores a responderem mais rapidamente a oportunidades e incidentes. Os trabalhadores de restaurantes podem estimar melhor a quantidade de comida a ser preparada, os gerentes de varejo podem determinar se devem ser abertos mais balcões de caixa e a equipe de segurança pode responder mais rapidamente a emergências ou alertar os primeiros respondentes.

Em todos esses casos, o envio dos dados registrados para um centro de computação em nuvem ou para um data center pode incluir latência no processamento de dados. Essa perda de tempo pode causar consequências negativas durante a tentativa de responder a situações e oportunidades críticas.

Se os dados registrados forem dados que não exijam nenhum processamento especial ou sensível ao tempo, será possível que sejam gerados custos significativos de rede e de armazenamento para o envio desnecessário desses dados normais.

Como alternativa, se algum dado coletado também for confidencial, como informações pessoais, aumentará o risco de expor esses dados sempre que eles forem movidos para outro local diferente de onde foram criados.

Além disso, se qualquer uma de suas conexões de rede não for confiável, você também correrá o risco de interromper operações críticas.

## Arquitetura
{: #edge_arch}

O objetivo da computação de borda é aproveitar as disciplinas que foram criadas para a computação em nuvem híbrida para suportar operações remotas de instalações de computação de borda. {{site.data.keyword.edge_servers_notm}} O é projetado para esse propósito.

Uma implementação típica do {{site.data.keyword.edge_servers_notm}} inclui uma instância do {{site.data.keyword.icp_server}} que está instalada em seu data center do cluster do hub. Essa instância do {{site.data.keyword.icp_server}} é usada para hospedar um controlador do {{site.data.keyword.mcm_core_notm_novers}} dentro do cluster do hub. O cluster do hub é onde ocorre o gerenciamento de todos os servidores de borda remotos. O {{site.data.keyword.edge_servers_notm}} usa o {{site.data.keyword.mcm_core_notm_novers}} para gerenciar e implementar cargas de trabalho do cluster do hub para os servidores de borda baseados em Kubernetes remotos quando as operações remotas são necessárias.

Esses servidores de borda podem ser instalados em locais remotos no local para tornar as cargas de trabalho do aplicativo locais onde as operações de negócios críticas ocorrem fisicamente, como em suas fábricas, armazéns, lojas de varejo, centros de distribuição e mais. Uma instância do {{site.data.keyword.icp_server}} e uma do {{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}} são necessárias em cada um dos locais remotos em que você deseja hospedar um servidor de borda. O {{site.data.keyword.mcm_core_notm_novers}} {{site.data.keyword.klust}} é usado para gerenciar servidores de borda remotamente.

O diagrama a seguir ilustra a topologia de alto nível de uma configuração de computação de borda típica que usa o {{site.data.keyword.icp_server}} e o {{site.data.keyword.mcm_core_notm_novers}}:

<img src="../images/edge/edge_server_data_center.svg" alt="{{site.data.keyword.edge_servers_notm}} topologia" width="50%">

O diagrama a seguir mostra a arquitetura de alto nível típica de um sistema {{site.data.keyword.edge_servers_notm}}:

<img src="../images/edge/edge_server_manage_hub.svg" alt="{{site.data.keyword.edge_servers_notm}} arquitetura" width="50%">

Os diagramas a seguir mostram a arquitetura de alto nível das implementações típicas dos componentes do {{site.data.keyword.edge_servers_notm}}:

* Cluster do hub

  <img src="../images/edge/multicloud_managed_hub.svg" alt="{{site.data.keyword.edge_servers_notm}} cluster do hub" width="20%">

  O cluster do hub do {{site.data.keyword.mcm_core_notm_novers}} age como um hub de gerenciamento. O cluster do hub é geralmente configurado com todos os componentes do {{site.data.keyword.icp_server}} que são necessários para executar seus negócios. Esses componentes necessários incluem os componentes que são necessários para suportar as operações que são executadas em seus servidores de borda remotos.

* Servidor de borda remoto

  <img src="../images/edge/edge_managed_cluster.svg" alt="{{site.data.keyword.edge_servers_notm}} cluster gerenciado" width="20%">

  Cada servidor de borda remoto é um cluster gerenciado do {{site.data.keyword.mcm_core_notm_novers}} que inclui um instalado {{site.data.keyword.klust}}. Cada servidor de borda remoto pode ser configurado com qualquer um dos serviços hospedados padrão do {{site.data.keyword.icp_server}} que são necessários para o centro de operação remoto e não são restringidos pelos recursos do servidor de borda.

  Se as restrições de recursos forem um fator limitante para um servidor de borda, a configuração mínima do {{site.data.keyword.icp_server}} poderá ser obtida usando o {{site.data.keyword.edge_profile}}. Se a configuração do {{site.data.keyword.edge_profile}} for usada para o servidor de borda, a topologia típica poderá ser semelhante ao diagrama a seguir:

  <img src="../images/edge/multicloud_managed_cluster.svg" alt="{{site.data.keyword.edge_profile}} topologia de cluster gerenciado" width="70%">

  Os componentes dentro dessa topologia funcionam principalmente como um proxy para suas contrapartes dentro do cluster do hub e podem transferir o trabalho para o cluster do hub. Os componentes do servidor de borda também concluem o processamento local enquanto as conexões entre o servidor de borda remoto e o cluster do hub são desconectadas temporariamente, como em uma conectividade de rede não confiável entre os locais.

## Conceitos
{: #concepts}

**computação de borda**: um modelo de cálculo distribuído que aproveita a computação disponível fora dos data centers tradicionais e em nuvem. Um modelo de computação de borda coloca uma carga de trabalho mais próxima de onde os dados associados são criados e onde as ações são executadas em resposta à análise desses dados. A colocação de dados e de cargas de trabalho em dispositivos de borda reduz as latências, diminui as demandas na largura da banda da rede, aumenta a privacidade de informações confidenciais e ativa as operações durante as interrupções da rede.

**dispositivo de borda**: um equipamento, como uma máquina de montagem em uma fábrica, uma ATM, uma câmera inteligente ou um automóvel, com capacidade de computação integrada na qual um trabalho significativo pode ser executado e dados podem ser coletados ou produzidos.

**gateway de borda**: um servidor de borda que possui serviços que executam funções de rede, como conversão de protocolo, terminação de rede, tunelamento, proteção de firewall ou conexões wireless. Um gateway de borda funciona como o ponto de conexão entre o dispositivo de borda ou o servidor de borda e a nuvem ou uma rede maior.

**nó de borda**: qualquer dispositivo de borda, servidor de borda ou gateway de borda em que a computação de borda ocorre.

**servidor de borda**: um computador em uma instalação de operações remotas que executa cargas de trabalho de aplicativo corporativo e serviços compartilhados. Um servidor de borda pode ser usado para conectar-se a um dispositivo de borda, conectar-se a outro servidor de borda ou funcionar como um gateway de borda para conectar-se à nuvem ou a uma rede maior.

**serviço de borda**: um serviço que é projetado especificamente para ser implementado em um servidor de borda, um gateway de borda ou um dispositivo de borda. Reconhecimento visual, insights acústicos e reconhecimento de voz são exemplos de possíveis serviços de borda.

**carga de trabalho de borda**: qualquer serviço, microsserviço ou software que faça um trabalho significativo ao ser executado em um nó de borda.

- [Requisitos e recomendações de hardware](cluster_sizing.md)
- [Instalando componentes compartilhados do {{site.data.keyword.edge_notm}}](install_edge.md)
{: childlinks}
