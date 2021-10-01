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

# Dispositivos de borda
{: #edge_devices}

Um dispositivo de borda fornece um ponto de entrada para redes principais corporativas ou de provedor de serviços. Os
exemplos incluem smartphones, câmeras de segurança ou até mesmo um forno microondas conectado à Internet.

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) está disponível para hubs ou servidores de gerenciamento, incluindo dispositivos distribuídos. Consulte as seções a seguir para obter detalhes sobre como instalar o agente leve do {{site.data.keyword.ieam}} nos dispositivos de borda:

* [Preparando um dispositivo de borda](../installing/adding_devices.md)
* [Instalando o Agente](../installing/registration.md)
* [Atualizando o agente](../installing/updating_the_agent.md)

Todos os dispositivos de borda (nós de borda) requerem que o software {{site.data.keyword.horizon_agent}} seja instalado. O {{site.data.keyword.horizon_agent}} também depende do software [Docker ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.docker.com/). 

Focando no dispositivo de borda, o diagrama a seguir mostra o fluxo das etapas que você executa para configurar o dispositivo de borda e o que o agente faz depois que ele é iniciado.

<img src="../../images/edge/05a_Installing_edge_agent_on_device.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, agbots e agentes">
