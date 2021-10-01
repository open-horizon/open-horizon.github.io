---

copyright:
  years: 2020
lastupdated: "2020-04-27"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Visão geral do serviço de borda para clusters
{: #cluster_deployment}

O recurso de cluster de borda do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho de um cluster de hub para instâncias remotas do OpenShift® Container Platform 4.2 ou outros clusters baseados em Kubernetes. Os clusters de borda são nós de borda do {{site.data.keyword.ieam}} que são implementados como clusters do Kubernetes. Um cluster de borda ativa os casos de uso na borda que requerem colocação de computação com operações de negócios ou que requerem mais capacidade de escalabilidade e de computação do que pode ser suportado por um dispositivo de borda. Além disso, não é incomum que clusters de borda forneçam serviços de aplicativos necessários para suportar serviços em execução em um dispositivo de borda devido à sua estreita proximidade com os dispositivos de borda. O {{site.data.keyword.ieam}} implementa serviços de borda em um cluster de borda por meio de um operador do Kubernetes, ativando os mesmos mecanismos de implementação autônomos usados com dispositivos de borda. O poder total do Kubernetes como uma plataforma de gerenciamento de contêiner está disponível para serviços de borda implementados pelo {{site.data.keyword.ieam}}.

O IBM Cloud Pak for Multicloud Management pode ser usado, opcionalmente, para fornecer um nível mais profundo de gerenciamento específico de clusters de borda do Kubernetes, mesmo para serviços de borda implementados pelo {{site.data.keyword.ieam}}.

Inclua um gráfico mostrando etapas de instalação e configuração de alto nível (e mostrando também dispositivos e clusters) do nó de borda.
