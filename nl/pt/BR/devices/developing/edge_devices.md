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

# Antes de iniciar

Entenda esses pré-requisitos para trabalhar com dispositivos de borda:

* [Preparando um dispositivo de borda](#adding-devices)
* [Arquiteturas e sistemas operacionais suportados](#suparch-horizon)
* [Dimensionando](#size)

Nota: os dispositivos de borda também são referidos como agentes. Consulte NOTA DO ESCRITOR para obter uma descrição dos dispositivos de borda e clusters.

## Preparando um dispositivo de borda
{: #adding-devices}

O {{site.data.keyword.edge_devices_notm}} usa o software de produto [{{site.data.keyword.horizon_open}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/). O {{site.data.keyword.horizon_agents}} em seus dispositivos de borda se comunicam com outros componentes do {{site.data.keyword.horizon}} para orquestrar de forma segura o gerenciamento de ciclo de vida de software em seus dispositivos.
{:shortdesc}

O diagrama a seguir mostra as interações típicas entre os componentes no {{site.data.keyword.horizon}}.

<img src="../../images/edge/installers.svg" width="90%" alt="Interações entre os componentes no {{site.data.keyword.horizon}}">

Todos os dispositivos de borda (nós de borda) requerem que o software {{site.data.keyword.horizon_agent}} seja instalado. O {{site.data.keyword.horizon_agent}} também depende do software [Docker ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.docker.com/). 

Focando no dispositivo de borda, o diagrama a seguir mostra o fluxo das etapas que você executa para configurar o dispositivo de borda e o que o agente faz depois que ele é iniciado.

<img src="../../images/edge/registration.svg" width="80%" alt="{{site.data.keyword.horizon_exchange}}, robôs de contrato e agentes">

As instruções a seguir guiam você no processo de instalação do software necessário em seu dispositivo de borda e do registro dele com o {{site.data.keyword.edge_devices_notm}}.

## Arquiteturas e sistemas operacionais suportados
{: #suparch-horizon}

O {{site.data.keyword.edge_devices_notm}} suporta sistemas com as seguintes arquiteturas de hardware:

* Dispositivos ou máquinas virtuais {{site.data.keyword.linux_bit_notm}} que executam Ubuntu 18.x (bionic), Ubuntu 16.x (xenial), Debian 10 (buster) ou Debian 9 (stretch)
* {{site.data.keyword.linux_notm}} no ARM (32 bits), por exemplo, Raspberry Pi, que executa o Raspbian buster ou stretch
* {{site.data.keyword.linux_notm}} no ARM (64 bits), por exemplo NVIDIA Jetson Nano, TX1 ou TX2, que executam o Ubuntu 18.x (biônico)
* {{site.data.keyword.macOS_notm}}

## Dimensionando
{: #size}

O agente requer:

1. 100 MB de RAM (incluindo docker). A RAM aumenta acima desse valor em aproximadamente 100 K por contrato, além de qualquer memória adicional necessária por cargas de trabalho que são executadas no nó.
2. 400 MB de disco (incluindo docker). O disco aumenta acima dessa quantia com base no tamanho das imagens do contêiner que são usadas por cargas de trabalho e no tamanho dos objetos do modelo (vezes 2) que são implementados no nó.

## O que vem a seguir

[Instalando o Agente](installing_the_agent.md)
