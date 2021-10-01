---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visão geral do serviço de borda para clusters
{: #edge_clusters_overview}

O recurso de cluster de borda do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho de um cluster de hub para instâncias remotas do OpenShift® Container Platform 4.2 ou outros clusters baseados em Kubernetes. Os clusters de borda são nós de borda do {{site.data.keyword.ieam}} que são implementados como clusters do Kubernetes. Um cluster de borda ativa os casos de uso na borda que requerem colocação de computação com operações de negócios ou que requerem mais capacidade de escalabilidade e de computação do que pode ser suportado por um dispositivo de borda. Além disso, não é incomum que clusters de borda forneçam serviços de aplicativos necessários para suportar serviços em execução em um dispositivo de borda devido à sua estreita proximidade com os dispositivos de borda. O IEAM implementa serviços de borda em um cluster de borda por meio de um operador do Kubernetes, ativando os mesmos mecanismos de implementação autônomos usados com dispositivos de borda. O poder total do Kubernetes como uma plataforma de gerenciamento de contêiner está disponível para serviços de borda implementados pelo {{site.data.keyword.ieam}}.

O IBM Cloud Pak for Multicloud Management pode ser usado, opcionalmente, para fornecer um nível mais profundo de gerenciamento específico de clusters de borda do Kubernetes, mesmo para serviços de borda implementados pelo IEAM.

Inclua um gráfico mostrando as etapas de instalação e configuração de alto nível do cluster de borda. 

## Próximos passos

Consulte [Clusters de borda](../developing/edge_clusters.md) para obter informações de instalação do cluster de borda.

## Informações relacionadas

* [Instalando nós de borda](installing_edge_nodes.md)
* [Dispositivos de borda](../developing/edge_devices.md)
* [Clusters de borda](../developing/edge_clusters.md)
