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

# Visão geral do hub de gerenciamento
{: #hub_install_overview}
 
Deve-se instalar e configurar um hub de gerenciamento antes de mover para as tarefas do nó do IBM Edge Application Manager (IEAM).

O IEAM fornece recursos de computação de borda para ajudá-lo a gerenciar e implementar cargas de trabalho a partir de um cluster de hub para instâncias remotas do OpenShift® Container Platform 4.3 ou outros clusters baseados em Kubernetes.

O IEAM usa o IBM Multicloud Management Core 1.2 para controlar a implementação de cargas de trabalho conteinerizadas nos servidores de borda, gateways e dispositivos que são hospedados por clusters do OpenShift® Container Platform 4.3 em locais remotos.

Além disso, o IEAM inclui suporte para um perfil do gerenciador de computação de borda. Este perfil suportado pode ajudá-lo a reduzir o uso de recursos do OpenShift® Container Platform 4.3 quando o OpenShift® Container Platform 4.3 é instalado para uso na hospedagem de um servidor de borda remoto. Esse perfil coloca nele os serviços mínimos necessários para suportar o gerenciamento remoto robusto desses ambientes de servidor e os aplicativos corporativos críticos que você está hospedando. Com esse perfil, você ainda é capaz de autenticar usuários, coletar dados de log e de evento e implementar cargas de trabalho em um único nó do trabalhador ou em um conjunto de clusters.

Inclua um gráfico mostrando a instalação de hub de alto nível e etapas de configuração. 

## Próximos passos

Consulte [Instalando o hub de gerenciamento](install.md) para obter instruções de instalação do hub de gerenciamento.

## Informações relacionadas

* [Instalando nós de borda](installing_edge_nodes.md)
* [Clusters de borda](../developing/edge_clusters.md)
* [Dispositivos de borda](../developing/edge_devices.md)
