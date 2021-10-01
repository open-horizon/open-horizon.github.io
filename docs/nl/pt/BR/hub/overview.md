---

copyright:
years: 2020
lastupdated: "2020-05-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visão geral
{: #Overview}

A computação de borda aproxima os aplicativos corporativos dos locais nos quais os dados são criados.
{:shortdesc}

* [Benefícios da computação de borda](#edge_benefits)
* [Exemplos](#examples)
* [Conceitos ](#concepts)
  
A computação de borda é um novo paradigma importante que pode expandir o modelo operacional por meio da virtualização da nuvem para além de um data center ou de um centro de computação em nuvem. Ela move as cargas de trabalho de aplicativos de um local centralizado para locais remotos, como fábricas, armazéns, centros de distribuição, lojas de varejo, centros de transporte e outros. Essencialmente, a computação de borda fornece a capacidade de mover cargas de trabalho do aplicativo para qualquer lugar no qual a computação é necessária fora de seus data centers e do ambiente de hospedagem de nuvem.

O {{site.data.keyword.ieam}} fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho a partir de um cluster de hub para instâncias remotas do {{site.data.keyword.open_shift_cp}} ou outros clusters baseados no Kubernetes.

O {{site.data.keyword.ieam}} também inclui suporte para um {{site.data.keyword.edge_profile}}. Esse perfil suportado pode ajudar a reduzir o uso de recurso do {{site.data.keyword.open_shift_cp}} quando o {{site.data.keyword.open_shift_cp}} é instalado para ser usado na hospedagem de um cluster de borda remoto. Esse perfil coloca nele os serviços mínimos necessários para suportar o gerenciamento remoto robusto desses ambientes de servidor e os aplicativos corporativos críticos que você está hospedando. Com esse perfil, você ainda é capaz de autenticar usuários, coletar dados de log e de evento e implementar cargas de trabalho em um único nó do trabalhador ou em um conjunto de clusters.

## Benefícios da computação de borda
{: #edge_benefits}

* Mudança de valor agregado para a organização: a transferência das cargas de trabalho de aplicativo para os nós de borda para operações de suporte em locais remotos onde os dados são coletados, em vez de enviar os dados para o data center central para processamento.

* Reduza as dependências da equipe de TI: o uso do {{site.data.keyword.ieam}} pode ajudá-lo a reduzir as dependências da equipe de TI. Use o {{site.data.keyword.ieam}} para implementar e gerenciar cargas de trabalho críticas em clusters de borda de forma segura e confiável em centenas de locais remotos por meio de um local central. Este recurso elimina a necessidade da equipe de TI em tempo integral em cada local remoto para gerenciar as cargas de trabalho no local.

## Exemplos
{: #examples}

A computação de borda aproxima os aplicativos corporativos dos locais nos quais os dados são criados. Por exemplo, se você opera uma fábrica, os equipamentos da fábrica podem incluir sensores para registrar qualquer número de pontos de dados que forneçam detalhes sobre como a fábrica está operando. Os sensores podem registrar o número de peças que estão sendo montadas por hora, o tempo necessário para que um empilhador retorne à posição inicial ou a temperatura de operação de uma máquina fabricada. As informações desses pontos de dados podem ser benéficas para ajudá-lo a determinar se você está operando em uma eficiência de pico, identificar os níveis de qualidade que você está alcançando ou prever quando uma máquina provavelmente falhará e exigirá manutenção preventiva.

Em outro exemplo, se houver trabalhadores em locais remotos cuja tarefa possa resultar no trabalho em situações perigosas, como ambientes quentes ou com barulho muito alto, proximidade de gases de escape ou de produção ou máquinas pesadas, poderá ser necessário monitorar as condições do ambiente. É possível coletar informações de várias origens que podem ser usadas em locais remotos. Os dados desse monitoramento podem ser usados pelos supervisores para determinar quando instruir os trabalhadores a fazer pausas, tomar água ou encerrar o equipamento.

Em um outro exemplo, é possível usar câmeras de vídeo para monitorar propriedades, como para identificar o tráfego de pessoas em lojas de varejo, restaurantes ou locais de entretenimento, para funcionar como um monitor de segurança para registrar atos de vandalismo ou outras atividades indesejadas ou para reconhecer condições de emergência. Se você também coletar dados dos vídeos, será possível usar a computação de borda para processar a análise de vídeo localmente para ajudar os trabalhadores a responderem mais rapidamente a oportunidades e incidentes. Os trabalhadores de restaurantes podem estimar melhor a quantidade de comida a ser preparada, os gerentes de varejo podem determinar se devem ser abertos mais balcões de caixa e a equipe de segurança pode responder mais rapidamente a emergências ou alertar os primeiros respondentes.

Em todos esses casos, o envio dos dados registrados para um centro de computação em nuvem ou para um data center pode incluir latência no processamento de dados. Essa perda de tempo pode causar consequências negativas durante a tentativa de responder a situações e oportunidades críticas.

Se os dados registrados forem dados que não exijam nenhum processamento especial ou sensível ao tempo, será possível que sejam gerados custos significativos de rede e de armazenamento para o envio desnecessário desses dados normais.

Como alternativa, se algum dado coletado também for confidencial, como informações pessoais, aumentará o risco de expor esses dados sempre que eles forem movidos para outro local diferente de onde foram criados.

Além disso, se qualquer uma de suas conexões de rede não for confiável, você também correrá o risco de interromper operações críticas.

## Conceitos
{: #concepts}

**dispositivo de borda**: um equipamento, como uma máquina de montagem em uma fábrica, um caixa eletrônico, uma câmera inteligente ou um automóvel, com capacidade de computação integrada na qual um trabalho significativo pode ser executado e dados podem ser coletados ou produzidos.

**gateway de borda**: um cluster de borda que possui serviços que executam funções de rede, como conversão de protocolo, terminação de rede, tunelamento, proteção de firewall ou conexões wireless. Um gateway de borda serve como o ponto de conexão entre um dispositivo de borda ou cluster de borda e a nuvem ou uma rede maior.

**nó de borda**: qualquer dispositivo de borda, cluster de borda ou gateway de borda em que a computação de borda ocorre.

**cluster de borda**: um computador em uma instalação de operações remotas que executa cargas de trabalho e serviços compartilhados de aplicativo corporativo. Um cluster de borda pode ser usado para conectar-se a um dispositivo de borda, conectar-se a outro cluster de borda ou servir como um gateway de borda para conectar-se à nuvem ou a uma rede maior.

**serviço de borda**: um serviço que é projetado especificamente para ser implementado em um cluster de borda, um gateway de borda ou um dispositivo de borda. Reconhecimento visual, insights acústicos e reconhecimento de voz são exemplos de possíveis serviços de borda.

**carga de trabalho de borda**: qualquer serviço, microsserviço ou software que faça um trabalho significativo ao ser executado em um nó de borda.

Redes públicas, privadas e de entrega de conteúdo estão passando por um processo de transformação de canais simples para ambientes de hospedagem de valor superior para aplicativos na forma de nuvem de rede de borda. Os casos de uso típico para o {{site.data.keyword.ieam}} incluem:

* Implementação de nós de borda
* Capacidade de operações de computação de nós de borda
* Suporte e otimização de nós de borda

O {{site.data.keyword.ieam}} unifica plataformas em nuvem a partir de múltiplos fornecedores em um painel consistente do local para a borda. O {{site.data.keyword.ieam}} é uma extensão natural que permite a distribuição e o gerenciamento de cargas de trabalho além da rede de borda para gateways e dispositivos de borda. O {{site.data.keyword.ieam}} também reconhece cargas de trabalho a partir de aplicativos corporativos com componentes de borda, ambientes de nuvem híbridos e privados e nuvem pública, em que o {{site.data.keyword.ieam}} fornece um novo ambiente de execução para IA distribuída para atingir origens de dados críticos.

Além disso, o {{site.data.keyword.ieam}} entrega ferramentas de IA para reconhecimentos de deep learning, visual e de voz e de análise acústica e de vídeo acelerados, que permite fazer inferências sobre todas as resoluções e sobre a maioria dos formatos de áudio e vídeo, serviços de conversas e descoberta.

## O que vem depois

- [Dimensionamento e requisitos do sistema](cluster_sizing.md)
- [Instalando o hub de gerenciamento](hub.md)
