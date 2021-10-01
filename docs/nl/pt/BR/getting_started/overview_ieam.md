---

copyright:
years: 2020
lastupdated: "2020-05-11"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visão Geral do {{site.data.keyword.edge_notm}}
{: #overviewofedge}

Esta seção fornece uma visão geral do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

## Recursos do {{site.data.keyword.ieam}}
{: #capabilities}

O {{site.data.keyword.ieam}} fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho de um cluster de hub de gerenciamento para dispositivos de borda e instâncias remotas do OpenShift Container Platform ou outros clusters baseados em Kubernetes.

## Arquitetura

O objetivo da computação de borda é aproveitar as disciplinas que foram criadas para a computação em nuvem híbrida para suportar operações remotas de instalações de computação de borda. {{site.data.keyword.ieam}} O é projetado para esse propósito.

A implementação do {{site.data.keyword.ieam}} inclui o hub de gerenciamento que é executado em uma instância do OpenShift Container Platform instalado em seu data center. O hub de gerenciamento é onde ocorre o gerenciamento de todos os nós de borda remotos (dispositivos de borda e clusters de borda).

Esses nós de extremidade podem ser instalados em locais remotos para tornar as cargas de trabalho de seus aplicativos locais em que suas operações críticas de negócios ocorrem fisicamente, como em suas fábricas, armazéns, pontos de venda, centros de distribuição e muito mais.

O diagrama a seguir ilustra a topologia de alto nível de uma configuração de computação de borda típica:

<img src="../OH/docs/images/edge/01_OH_overview.svg" style="margin: 3%" alt="IEAM overview">

O hub de gerenciamento do {{site.data.keyword.ieam}} é projetado especificamente para o gerenciamento de nós de borda para minimizar os riscos de implementação e para gerenciar o ciclo de vida do software de serviço em nós de borda de forma totalmente autônoma. Um instalador do Cloud instala e gerencia os componentes do hub de gerenciamento do {{site.data.keyword.ieam}}. Os desenvolvedores de software desenvolvem e publicam serviços de borda no hub de gerenciamento. Os administradores definem as políticas de implementação que controlam onde os serviços de borda são implementados. O {{site.data.keyword.ieam}} trata de todo o resto.

# Componentes
{: #components}

Para obter mais informações sobre componentes que são empacotados com o {{site.data.keyword.ieam}}, consulte [Componentes](components.md).

## O que vem depois

Para obter mais informações sobre como usar o {{site.data.keyword.ieam}} e desenvolver serviços de borda, revise os tópicos que estão listados na [Página de boas-vindas](../kc_welcome_containers.html) do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
