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

O recurso de cluster de borda do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) ajuda a gerenciar e implementar cargas de trabalho a partir de um cluster de hub de gerenciamento em instâncias remotas do OpenShift® Container Platform ou de outros clusters baseados em Kubernetes. Clusters de borda são nós de borda do {{site.data.keyword.ieam}} que são clusters Kubernetes. Um cluster de borda possibilita casos de uso na borda, que requerem a colocação de cálculo com operações de negócios ou que requerem mais escalabilidade, disponibilidade e capacidade de cálculo do que pode ser suportado por um dispositivo de borda. Além disso, não é incomum que clusters de borda forneçam serviços de aplicativos que são necessários para suportar serviços em execução em dispositivos de borda devido à sua estreita proximidade com os dispositivos de borda. O {{site.data.keyword.ieam}} implementa serviços de borda em um cluster de borda por meio de um operador do Kubernetes, ativando os mesmos mecanismos de implementação autônomos usados com dispositivos de borda. O poder total do Kubernetes como uma plataforma de gerenciamento de contêiner está disponível para serviços de borda que são implementados pelo {{site.data.keyword.ieam}}.

<img src="../OH/docs/images/edge/05b_Installing_edge_agent_on_cluster.svg" style="margin: 3%" alt="{{site.data.keyword.horizon_exchange}}, agbots and agents">

As seções a seguir descrevem como instalar um cluster de borda e instalar o agente do {{site.data.keyword.ieam}} nele.

- [Preparando um cluster de borda](preparing_edge_cluster.md)
- [Instalando o Agente](edge_cluster_agent.md)
{: childlinks}
