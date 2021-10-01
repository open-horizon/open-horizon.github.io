---

copyright:
years: 2019, 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Componentes

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) inclui vários componentes que são empacotados com o produto.
{:shortdesc}

Visualize a tabela a seguir para obter uma descrição dos componentes do {{site.data.keyword.ieam}}:

|Componente|Versão|Descrição|
|---------|-------|----|
|[Serviços Comuns da Plataforma IBM Cloud](https://www.ibm.com/docs/en/cpfs)|3.6.x|Este é um conjunto de componentes base que são instalados automaticamente como parte da instalação do operador do {{site.data.keyword.ieam}}.|
|Agbot|{{site.data.keyword.anax_ver}}|Instâncias de robô de contrato (agbot) que são criadas centralmente e que são responsáveis pela implementação de cargas de trabalho e de modelos de aprendizado de máquina no {{site.data.keyword.ieam}}.|
|MMS |1.5.3-338|O Model Management System (MMS) facilita o armazenamento, a entrega e a segurança de modelos, dados e outros pacotes de metadados necessários aos serviços de borda. Isso permite que os nós de borda enviem e recebam facilmente modelos e metadados para e a partir da nuvem.|
|API Exchange|2.87.0-531|O Exchange fornece a API de REST que contém todas as definições (padrões, políticas, serviços, etc.) usadas por todos os outros componentes no {{site.data.keyword.ieam}}.|
|Console de Gerenciamento|1.5.0-578|A IU da web usada pelos administradores do {{site.data.keyword.ieam}} para visualizar e gerenciar os outros componentes do {{site.data.keyword.ieam}}.|
|Secure Device Onboard|1.11.11-441|O componente SDO habilita a tecnologia que é criada pela Intel para simplificar e assegurar a configuração de dispositivos de borda e associá-los a um hub de gerenciamento de borda.|
|Cluster Agent|{{site.data.keyword.anax_ver}}|Esta é a imagem de contêiner, que é instalada como um agente em clusters de borda para ativar o gerenciamento de carga de trabalho do nó pelo {{site.data.keyword.ieam}}.|
|Agente do Dispositivo|{{site.data.keyword.anax_ver}}|Este componente é instalado em dispositivos de borda para ativar o gerenciamento de carga de trabalho do nó pelo {{site.data.keyword.ieam}}.|
|Gerenciador de segredos|1.0.0-168|O Gerenciador de Segredos é o repositório para segredos implementados em dispositivos de borda, possibilitando que os serviços recebam de forma segura credenciais usadas para autenticar em suas dependências de envio de dados.|
