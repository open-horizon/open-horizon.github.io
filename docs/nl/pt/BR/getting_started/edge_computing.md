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

# Visão geral da computação de borda
{: #overviewofedge}

## Recursos do {{site.data.keyword.edge_notm}}
{: #capabilities}

O {{site.data.keyword.edge_notm}} (IEAM) abrange diversas camadas e segmentos de mercado que são otimizados com tecnologias abertas e padrões estabelecidos, como Docker e Kubernetes. Isso inclui plataformas computacionais, ambientes de nuvem privada e corporativos, espaços de computação de rede e gateways locais, controladores e servidores, além de dispositivos inteligentes.

<img src="../images/edge/01_IEAM_overview.svg" width="100%" alt="Visão geral do IEAM">

Centralmente, nuvens públicas de hiperescala, nuvens híbridas, data centers gerenciados com alocação e data centers corporativos tradicionais continuam a agir como pontos de agregação para dados, análises e processamento de dados de back-end.

Redes públicas, privadas e de entrega de conteúdo estão passando por um processo de transformação
de canais simples para ambientes de hospedagem de valor superior para aplicativos na forma de nuvem de rede de borda. Os casos de uso típico para o {{site.data.keyword.ieam}} incluem:

* Computação em nuvem híbrida
* Rede 5G 
* Implementação do servidor de borda
* Capacidade de operações de computação de servidores de borda
* Suporte e otimização de dispositivos ioT

O IBM Multicloud Management Core 1.2 unifica as plataformas de nuvem de vários fornecedores em um único painel consistente, de local para a borda. O {{site.data.keyword.ieam}} é
uma extensão natural que permite a distribuição e o gerenciamento de cargas de trabalho além da rede de
borda para gateways e dispositivos de borda. Além disso, o IBM Multicloud Management Core 1.2 reconhece cargas de trabalho de aplicativos corporativos com componentes de borda, ambientes de nuvem privada ou híbrida e de nuvem pública; nessa situação, o IBM Edge Computing Manager fornece um novo ambiente de execução para IA distribuída, visando atingir origens de dados críticas.

Além disso, o IBM Multicloud Manager-CE fornece ferramentas de IA que aceleram os recursos de deep learning, de reconhecimento visual e de fala e de análise de vídeo e acústica, o que permite deduzir dados em todas as resoluções e na maioria dos formatos de serviços de vídeo, áudio e descoberta.

## Riscos e resolução do {{site.data.keyword.edge_notm}}
{: #risks}

Embora o {{site.data.keyword.ieam}} crie oportunidades exclusivas, ele também apresenta
desafios. Por exemplo, ele transcende os limites físicos do data center em nuvem, o que pode expor problemas de segurança, endereçabilidade, gerenciamento, propriedade e conformidade. E o mais importante, ele multiplica os
problemas de ajuste de escala de técnicas de gerenciamento baseadas em nuvem.

As redes de borda aumentam o número de nós de computação por uma ordem de magnitude. Os gateways de
borda aumentam isso em outra ordem de grandeza. Os dispositivos de borda aumentam esse número em 3 a 4
ordens de magnitude. Se o DevOps (entrega e implementação contínuas) for fundamental para gerenciar
uma infraestrutura de nuvem de hiperescala, então zero-ops (operações sem intervenção humana) serão
fundamentais para gerenciar na escala maciça que o {{site.data.keyword.ieam}} representa.

É fundamental implementar, atualizar, monitorar e recuperar o espaço de computação de borda sem
intervenção humana. Todas essas atividades e processos devem:

* Ser totalmente automatizados
* Poder tomar decisões independentes sobre a alocação de trabalho
* Ser capazes de reconhecer e recuperar-se das mudanças de condições sem a necessidade de intervenção. 

Todas essas atividades devem ser seguras, rastreáveis e defensáveis.

<!--{{site.data.keyword.edge_devices_notm}} delivers edge node management that minimizes deployment risks and manages the service software lifecycle on edge nodes fully autonomously. This function creates the capacity to achieve meaningful insights more rapidly from data that is captured closer to its source. {{site.data.keyword.edge_notm}} is available for infrastructure or servers, including distributed devices.
{:shortdesc}

Intelligent devices are being integrated into the tools that are used to conduct business at an ever-increasing rate. Device compute capacity is creating new opportunities for data analysis where data originates and actions are taken. {{site.data.keyword.edge_notm}} innovations fuel improved quality, enhance performance, and drive deeper, more meaningful user interactions. 

{{site.data.keyword.edge_notm}} can:

* Solve new business problems by using Artificial Intelligence (AI)
* Increase capacity and resiliency
* Improve security and privacy protections
* Leverage 5G networks to reduce latency

{{site.data.keyword.edge_notm}} can capture the potential of untapped data that is created by the unprecedented growth of connected devices, which opens new business opportunities, increases operational efficiency, and improves customer experiences. {{site.data.keyword.edge_notm}} brings Enterprise applications closer to where data is created and actions need to be taken, and it allows Enterprises to leverage AI and analyze data in near-real time.

## {{site.data.keyword.edge_notm}} benefits
{: #benefits}

{{site.data.keyword.edge_notm}} helps solve speed and scale challenges by using the computational capacity of edge devices, gateways, and networks. This function retains the principles of dynamic allocation of resources and continuous delivery that are inherent to cloud computing. With {{site.data.keyword.edge_notm}}, businesses have the potential to virtualize the cloud beyond data centers. Workloads that are created in the cloud can be migrated towards the edge, and where appropriate, data that is generated at the edge can be cleansed and optimized and brought back to the cloud.

{{site.data.keyword.edge_devices_notm}} spans industries and multiple tiers that are optimized with open technologies and prevailing standards like Docker and Kubernetes. This includes computing platform, both private cloud and Enterprise environments, network compute spaces and on-premises gateways, controllers and servers, and intelligent devices.

Centrally, the hyper-scale public clouds, hybrid clouds, colocated managed data centers and traditional Enterprise data centers continue to serve as aggregation points for data, analytics, and back-end data processing.

Public, private, and content-delivery networks are transforming from simple pipes to higher-value hosting environments for applications in the form of the edge network cloud.

{{site.data.keyword.edge_devices_notm}} offers: 

* Integrated offerings that provide faster insights and actions, secure and continuous operations.
* The industry's first policy-based, autonomous edge computing platform
that intelligently manages workload life cycles in a secure and flexible way.
* Open technology and ecosystems compatibility to provide robust support and innovation for industry-wide ecosystems and partners.
* Scalable solutions for wide-ranging deployment on edge devices, servers, gateways, and network elements.

## {{site.data.keyword.edge_notm}} capabilities
{: #capabilities}

* Hybrid cloud computing
* 5G networking 
* Edge server deployment
* Edge servers compute operations capacity
* IoT devices support and optimization

## {{site.data.keyword.edge_notm}} risks and resolution
{: #risks}

Although {{site.data.keyword.edge_notm}} creates unique opportunities, it also presents challenges. For example, it transcends cloud data center's physical boundaries, which can expose security, addressability, management, ownership, and compliance issues. More importantly, it multiplies the scaling issues of cloud-based management techniques.

Edge networks increase the number of compute nodes by an order of magnitude. Edge gateways increase that by another order of magnitude. Edge devices increase that number by 3 to 4 orders of magnitude. If DevOps (continuous delivery and continuous deployment) is critical to managing a hyper-scale cloud infrastructure, then zero-ops (operations with no human intervention) is critical to managing at the massive scale that {{site.data.keyword.edge_notm}} represents.

It is critical to deploy, update, monitor, and recover the edge compute space without human intervention. All of these activities and processes must be fully automated, capable of making decisions independently about work allocation, and able to recognize and recover from changing conditions without intervention. All of these activities must be secure, traceable, and defensible.

## Extending multi-cloud deployments to the edge
{: #extend_deploy}

{{site.data.keyword.mcm_core_notm}} unifies cloud platforms from multiple vendors into a consistent dashboard from on-premises to the edge. {{site.data.keyword.edge_devices_notm}} is a natural extension that enables the distribution and management of workloads beyond the edge network to edge gateways and edge devices.

{{site.data.keyword.mcm_core_notm}} recognizes workloads from Enterprise applications with edge components, private and hybrid cloud environments, and public cloud; where {{site.data.keyword.edge_notm}} provides a new execution environment for distributed AI to reach critical data sources.

{{site.data.keyword.mcm_ce_notm}} delivers AI tools for accelerated deep learning, visual and speech recognition, and video and acoustic analytics, which enables inferencing on all resolutions and most formats of video and audio conversation services and discovery.

## {{site.data.keyword.edge_devices_notm}} architecture
{: #iec4d_arch}

Other edge computing solutions typically focus on one of the following architectural strategies:

* A powerful centralized authority for enforcing edge node software compliance.
* Passing the software compliance responsibility down to the edge node owners, who are required to monitor for software updates, and manually bring their own edge nodes into compliance.

The former focuses authority centrally, creating a single point of failure, and a target that attackers can exploit to control the entire fleet of edge nodes. The latter solution can result in large percentages of the edge nodes not having the latest software updates installed. If edge nodes are not all on the latest version or have all of the available fixes, the edge nodes can be vulnerable to attackers. Both approaches also typically rely upon the central authority as a basis for the establishment of trust.

<p align="center">
<img src="../images/edge/overview_illustration.svg" width="70%" alt="Illustration of the global reach of edge computing.">
</p>

In contrast to those solution approaches, {{site.data.keyword.edge_devices_notm}} is decentralized. {{site.data.keyword.edge_devices_notm}} manages service software compliance automatically on edge nodes without any manual intervention. On each edge node, decentralized and fully autonomous agent processes run governed by the policies that are specified during the machine registration with {{site.data.keyword.edge_devices_notm}}. Decentralized and fully autonomous agbot (agreement bot) processes typically run in a central location, but can run anywhere, including on edge nodes. Like the agent processes, the agbots are governed by policies. The agents and agbots handle most of the edge service software lifecycle management for the edge nodes and enforce software compliance on the edge nodes.

For efficiency, {{site.data.keyword.edge_devices_notm}} includes two centralized services, the exchange and the switchboard. These services have no central authority over the autonomous agent and agbot processes. Instead, these services provide simple discovery and metadata sharing services (the exchange) and a private mailbox service to support peer-to-peer communications (the switchboard). These services support the fully autonomous work of the agents and agbots.

Lastly, the {{site.data.keyword.edge_devices_notm}} console helps administrators set policy and monitor the status of the edge nodes.

Each of the five {{site.data.keyword.edge_devices_notm}} component types (agents, agbots, exchange, switchboard, and console) has a constrained area of responsibility. Each component has no authority or credentials to act outside their respective area of responsibility. By dividing responsibility and scoping authority and credentials, {{site.data.keyword.edge_devices_notm}} offers risk management for edge node deployment.

WRITER NOTE: content from https://www-03preprod.ibm.com/support/knowledgecenter/SSFKVV_4.1/hub/offline_installation.html

Merge the content in this section with the above content.

## {{site.data.keyword.edge_devices_notm}}
{: #edge_devices}

{{site.data.keyword.edge_devices_notm}} provides you with a new architecture for edge node management. It is designed specifically to minimize the risks that are inherent in the deployment of either a global or local fleet of edge nodes. You can also use {{site.data.keyword.edge_devices_notm}} to manage the service software lifecycle on edge nodes fully autonomously.
{:shortdesc}

{{site.data.keyword.edge_devices_notm}} is built on the {{site.data.keyword.horizon_open}} project. For more information about the project, see [{{site.data.keyword.horizon_open}} ![Opens in a new tab](../../images/icons/launch-glyph.svg "Opens in a new tab")](https://github.com/open-horizon).-->

Para obter mais informações sobre como usar o {{site.data.keyword.edge_notm}} e desenvolver serviços de borda, revise os tópicos e grupos de tópicos a seguir:

* [Instalando o hub de gerenciamento](../hub/offline_installation.md) Saiba como instalar e configurar a infraestrutura do {{site.data.keyword.edge_devices_notm}} e reunir os arquivos necessários para a inclusão de dispositivos de borda.

* [Instalando nós de borda](../devices/installing/installing_edge_nodes.md) Saiba como instalar e configurar a infraestrutura do {{site.data.keyword.edge_devices_notm}} e reunir os arquivos necessários para a inclusão de dispositivos de borda.
  
* [Usando serviços de borda](../devices/developing/using_edge_services.md) Saiba mais sobre como usar serviços de borda do {{site.data.keyword.edge_notm}}.

* [Desenvolvendo serviços de borda](../devices/developing/developing_edge_services.md) Saiba mais sobre como usar serviços de borda do {{site.data.keyword.edge_notm}}.

* [Administrando o ](../devices/administering_edge_devices/administering.md)
  Saiba mais sobre como administrar os serviços de borda do {{site.data.keyword.edge_notm}}. 
  
* [Segurança](../devices/user_management/security.md)
  Aprenda mais sobre como o {{site.data.keyword.edge_notm}} mantém a segurança contra ataques e protege a privacidade dos participantes.

* [Usando o console de gerenciamento](../devices/getting_started/accessing_ui.md) Revise as perguntas mais frequentes para obter rapidamente informações chave sobre o {{site.data.keyword.edge_notm}}.

* [Usando a CLI](../devices/getting_started/using_cli.md) Revise as perguntas mais frequentes para obter rapidamente informações chave sobre o {{site.data.keyword.edge_notm}}.

* [APIs](../devices/installing/edge_rest_apis.md)  Revise as perguntas mais frequentes para obter rapidamente informações chave sobre o {{site.data.keyword.edge_notm}}.

* [Resolução de problemas do ](../devices/troubleshoot/troubleshooting.md) Ao encontrar problemas com a configuração ou o uso do {{site.data.keyword.edge_devices_notm}}, revise os problemas comuns que podem ocorrer e as dicas que podem ajudar a resolver os problemas.
