---

copyright:
  years: 2019
lastupdated: "2019-06-12"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Preparando para Instalar o {{site.data.keyword.edge_servers_notm}}
{: #edge_planning}

Antes de instalar o {{site.data.keyword.icp_server}}, ative o {{site.data.keyword.mgmt_hub}}, configure o {{site.data.keyword.edge_servers_notm}} e assegure-se de que o sistema atenda aos requisitos a seguir. Esses requisitos identificam os componentes e configurações mínimos necessários para os servidores de borda planejados.
{:shortdesc}

Esses requisitos também identificam as definições de configuração mínimas para o cluster do {{site.data.keyword.mgmt_hub}} que você planeja usar para gerenciar os servidores de borda.

Use estas informações para ajudá-lo a planejar os requisitos de recurso para a topologia de computação de borda e a configuração geral do {{site.data.keyword.icp_server}} e do {{site.data.keyword.mgmt_hub}}.

   * [Requisitos de hardware](#prereq_hard)
   * [IaaS Suportado](#prereq_iaas)
   * [Ambientes Suportados](#prereq_env)
   * [ Portas necessárias ](#prereq_ports)
   * [Considerações sobre dimensionamento do cluster](#cluster)

## Requisitos de hardware
{: #prereq_hard}

Quando você estiver dimensionando o nó de gerenciamento da topologia de computação de borda, use as diretrizes de dimensionamento do {{site.data.keyword.icp_server}} para uma implementação de um único nó ou de vários nós para ajudá-lo a dimensionar o cluster. Para obter mais informações, consulte [Dimensionando seu cluster do {{site.data.keyword.icp_server}} ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Os requisitos do servidor de borda a seguir se aplicam apenas às instâncias do {{site.data.keyword.icp_server}} que são implementadas em centros de operações remotos usando o {{site.data.keyword.edge_profile}}.

| Requisito | Nós (inicialização, mestre, gerenciamento) | Nós do trabalhador |
|-----------------|-----------------------------|--------------|
| Número de hosts | 1 | 1 |
| Núcleos | 4 ou mais | 4 ou mais |
| CPU | >= 2,4 GHz | >= 2,4 GHz |
| RAM | 8 GB ou mais | 8 GB ou mais |
| Espaço livre em disco para a instalação | 150 GB ou mais | |
{: caption="Tabela 1. Requisitos mínimos de hardware do cluster do servidor de borda." caption-side="top"}

Nota: 150 GB de armazenamento permite até três dias de retenção de dados de log e de eventos quando há desconexão de rede com o data center central.

## IaaS Suportado
{: #prereq_iaas}

A tabela a seguir identifica a Infraestrutura como Serviço (IaaS) suportada que pode ser usada para os serviços de borda.

| IaaS | Versões |
|------|---------|
|Nutanix NX-3000 Series para uso nos locais do servidor de borda | NX-3155G-G6 |
|IBM Hyperconverged Systems que são desenvolvidos com o Nutanix para uso em servidores de borda | CS821 e CS822|
{: caption="Tabela 2. IaaS Suportados para {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Para obter mais informações, consulte o [IBM Hyperconverged Systems desenvolvido com o Nutanix ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Ambientes Suportados
{: #prereq_env}

As tabelas a seguir identificam os sistemas configurados adicionais do Nutanix que podem ser usados com os servidores de borda.

| Tipo de site LOE | Tipo de Nó | Tamanho do cluster | Núcleos por nó (total) | Processadores lógicos por nó (total)	| Memória (GB) por nó (total) | Tamanho do disco do cache por grupo de disco (GB) |	Quantidade de disco do cache por nó	| Tamanho do disco do cache por nó (GB)	| Tamanho do conjunto de cluster total do armazenamento (todos flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Pequeno	| NX-3155G-G6	| 3 nós	| 24 (72)	| 48 (144)	| 256 (768)	| N/A	| N/A	| N/A	| 8 TB |
| Médio | NX-3155G-G6 | 3 nós | 24 (72)	| 48 (144)	| 512 (1.536)	| N/A	| N/A	| N/A	| 45 TB |
| Grande	| NX-3155G-G6	| 4 nós	| 24 (96)	| 48 (192)	| 512 (2.048)	| N/A	| N/A	| N/A	| 60 TB |
{: caption="Tabela 3. Configurações suportadas do Nutanix NX-3000 Series" caption-side="top"}

| Tipo de site LOE	| Tipo de Nó	| Tamanho do cluster |	Núcleos por nó (total) | Processadores lógicos por nó (total)	| Memória (GB) por nó (total)	| Tamanho do disco do cache por grupo de disco (GB) | Quantidade de disco do cache por nó	| Tamanho do disco do cache por nó (GB)	| Tamanho do conjunto de cluster total do armazenamento (todos flash) (TB) |
|---|---|---|---|---|---|---|---|---|---|
| Pequeno	| CS821 (2 soquetes, 1U) | 3 nós | 20 (60)	| 80 (240) | 256 (768) | N/A	| N/A	| N/A	| 8 TB |
| Médio | CS822 (2 soquetes, 2U) | 3 nós	| 22 (66)	| 88 (264) | 512 (1.536) | N/A | N/A | N/A | 45 TB |
| Grande	| CS822 (2 soquetes, 2U) | 4 nós | 22 (88) | 88 (352) | 512 (2.048) | N/A | N/A | N/A | 60 TB |
{: caption="Tabela 4. IBM Hyperconverged Systems que são desenvolvidos com o Nutanix" caption-side="top"}

Para obter mais informações, consulte [IBM Hyperconverged Systems que são desenvolvidos com o Nutanix ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/downloads/cas/BZP46MAV).

## Portas Obrigatórias
{: #prereq_ports}

Se você estiver planejando implementar um servidor de borda remoto com uma configuração de cluster padrão, os requisitos de porta para os nós serão os mesmos que os requisitos de porta para a implementação do {{site.data.keyword.icp_server}}. Para obter mais informações sobre esses requisitos, consulte [Portas necessárias ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/supported_system_config/required_ports.html). Para saber quais são as portas necessárias para o cluster do hub, consulte a seção _Portas necessárias para o {{site.data.keyword.mcm_core_notm}}_.

Se você planeja configurar os servidores de borda usando o {{site.data.keyword.edge_profile}}, ative as portas a seguir:

| Porta | Protocolo | Requisito |
|------|----------|-------------|
| NA | IPv4 | Calico com IP em IP (calico_ipip_mode: Sempre) |
| 179 | TCP	| Sempre para o Calico (network_type:calico) |
| 500 | TCP e UDP	| IPSec (ipsec.enabled: verdadeiro, calico_ipip_mode: Sempre) |
| 2380 | TCP | Sempre se o etcd estiver ativado |
| 4001 | TCP | Sempre se o etcd estiver ativado |
| 4500 | UDP | IPSec (ipsec.enabled: verdadeiro) |
| 9091 | TCP | Calico (network_type: calico) |
| 9099 | TCP | Calico (network_type: calico) |
| 10248:10252 | TCP	| Sempre para Kubernetes |
| 30000:32767 | TCP e UDP | Sempre para Kubernetes |
{: caption="Tabela 5. Portas necessárias para o {{site.data.keyword.edge_servers_notm}}" caption-side="top"}

Nota: as portas 30000:32767 possuem acesso externo. Essas portas devem ser abertas somente se você configurar o tipo de serviço do Kubernetes para NodePort.

## Considerações sobre o dimensionamento do cluster
{: #cluster}

Para o {{site.data.keyword.edge_servers_notm}}, o cluster do hub é geralmente um ambiente hospedado padrão do {{site.data.keyword.icp_server}}. É possível usar esse ambiente para também hospedar outras cargas de trabalho de computação necessárias ou desejadas, para ser atendido a partir de um local central. O ambiente de cluster de hub deve ser dimensionado para que tenha recursos suficientes para hospedar o cluster do {{site.data.keyword.mcm_core_notm}} e quaisquer cargas de trabalho adicionais que se planeje hospedar no ambiente. Para obter mais informações sobre o dimensionamento de um ambiente hospedado padrão do {{site.data.keyword.icp_server}}, consulte [Dimensionando seu cluster do {{site.data.keyword.icp_server}} ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html).

Se necessário, é possível operar um servidor de borda remoto dentro de um ambiente com restrição de recurso. Se for necessário operar um servidor de borda dentro de um ambiente com restrição de recurso, considere o uso do {{site.data.keyword.edge_profile}}. Esse perfil configura apenas os componentes mínimos necessários para um ambiente de servidor de borda. Se você usar esse perfil, ainda deverá alocar recursos suficientes para o conjunto de componentes necessários para uma arquitetura do {{site.data.keyword.edge_servers_notm}} e para fornecer os recursos necessários para quaisquer outras cargas de trabalho do aplicativo hospedadas nos ambientes de servidor de borda. Para obter mais informações sobre a arquitetura do {{site.data.keyword.edge_servers_notm}}, consulte [{{site.data.keyword.edge_servers_notm}}](overview.md#edge_arch).

Embora as configurações do {{site.data.keyword.edge_profile}} possam economizar recursos de memória e de armazenamento, as configurações resultam em um baixo nível de resiliência. Um servidor de borda que é baseado nesse perfil pode operar desconectado do data center central no qual o cluster do hub está localizado. Essa operação desconectada geralmente pode durar até três dias. Se o servidor de borda falhar, ele deixará de fornecer suporte operacional para o centro de operações remoto.

As configurações do {{site.data.keyword.edge_profile}} também são limitadas a suportar apenas a tecnologia e os processos a seguir:
  * Plataformas {{site.data.keyword.linux_notm}} de 64 bits
  * Topologia de implementação que não é de alta disponibilidade (HA)
  * Adição e remoção de nós do trabalhador como operações de dia 2
  * Acesso da CLI ao cluster e controle do cluster
  * Redes Calico

Se você precisar de mais resiliência ou se qualquer uma das limitações anteriores for muito restrita, será possível usar um dos outros perfis de configuração de implementação padrão do {{site.data.keyword.icp_server}} que fornecem suporte maior a failover.

### Distribuições de Amostra

* Ambiente do servidor de borda com base no {{site.data.keyword.edge_profile}} (resiliência baixa)

| Tipo de Nó | Número de nós | CPU | Memória (GB) | Disco (GB) |
|------------|:-----------:|:---:|:-----------:|:---:|
| Inicialização       | 1           | 1   | 2           | 8   |
| Principal     | 1           | 2   | 4           | 16  |
| Gerenciamento | 1           | 1   | 2           | 8   |
| Trabalhador     | 1           | 4   | 8           | 32  |
{: caption="Tabela 6. Valores de perfil de borda para um ambiente de servidor de borda de resiliência baixa" caption-side="top"}

* Ambientes do servidor de borda com base em outros perfis do {{site.data.keyword.icp_server}} (resiliência média a alta)

  Use os requisitos de implementação de amostra pequenos, médios e grandes quando precisar usar uma configuração que não seja a {{site.data.keyword.edge_profile}} para o ambiente do servidor de borda. Para obter mais informações, consulte [Dimensionando suas
implementações de amostra de cluster do {{site.data.keyword.icp_server}} ![Abre em uma nova guia](../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.2.0/installing/plan_capacity.html#samples).
