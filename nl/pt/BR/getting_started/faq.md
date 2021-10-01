---

copyright:
years: 2020
lastupdated: "2020-04-21"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Perguntas mais frequentes
{: #faqs}

A seguir estão as respostas para algumas perguntas frequentes (FAQs) sobre o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
{:shortdesc}

  * [Existe uma maneira de criar um ambiente autocontido para propósitos de desenvolvimento?](#one_click)
  * [O {{site.data.keyword.ieam}} é um software livre?](#open_sourced)
  * [Como posso usar o {{site.data.keyword.ieam}} para desenvolver e implementar serviços de borda?](#dev_dep)
  * [Quais plataformas de hardware de nó de borda o {{site.data.keyword.ieam}} suporta?](#hw_plat)
  * [Posso executar qualquer distribuição do {{site.data.keyword.linux_notm}} em meus nós de borda com o {{site.data.keyword.ieam}}?](#lin_dist)
  * [Quais linguagens de programação e ambientes são suportados pelo {{site.data.keyword.ieam}}?](#pro_env)
  * [Existe documentação detalhada para as APIs de REST fornecidas pelos componentes no {{site.data.keyword.ieam}}?](#rest_doc)
  * [O {{site.data.keyword.ieam}} usa Kubernetes?](#use_kube)
  * [O {{site.data.keyword.ieam}} usa MQTT?](#use_mqtt)
  * [Quanto tempo normalmente leva depois de registrar um nó de borda antes que os acordos sejam formados e os contêineres correspondentes comecem a funcionar?](#agree_run)
  * [O software {{site.data.keyword.horizon}} e todos os outros softwares ou dados relacionados ao {{site.data.keyword.ieam}} podem ser removidos de um host de nó de borda?](#sw_rem)
  * [Há um painel para visualizar os contratos e serviços que estão ativos em um nó de borda?](#db_node)
  * [O que acontece quando um download de imagem de contêiner é interrompido por uma indisponibilidade de rede?](#image_download)
  * [Como o {{site.data.keyword.ieam}} é seguro?](#ieam_secure)
  * [Como gerenciar a IA no Edge com modelos versus IA no Cloud?](#ai_cloud)

## Existe uma maneira de criar um ambiente autocontido para propósitos de desenvolvimento?
{: #one_click}

É possível instalar o hub de gerenciamento de software livre (sem o console de gerenciamento do {{site.data.keyword.ieam}}) com o instalador “tudo-em-um” para desenvolvedores. O instalador tudo-em-um cria um hub de gerenciamento completo, mas mínimo, não adequado para uso de produção. Ele também configura um nó da borda de exemplo. Esta ferramenta permite que os desenvolvedores de componente de software livre comecem rapidamente, sem precisar esperar o tempo necessário para a configuração de um hub de gerenciamento de produção completo do {{site.data.keyword.ieam}}. Para obter informações sobre o instalador all-in-one, consulte [Open Horizon - DevOps](https://github.com/open-horizon/devops/tree/master/mgmt-hub).

## O software do {{site.data.keyword.ieam}} é um software livre?
{: #open_sourced}

{{site.data.keyword.ieam}} é um produto IBM. Porém, seus componentes principais utilizam fortemente o projeto de software livre [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). Muitas amostras e programas de exemplo que estão disponíveis no projeto {{site.data.keyword.horizon}} funcionam com o {{site.data.keyword.ieam}}. Para obter mais informações sobre o projeto, consulte [Open Horizon - EdgeX Project Group](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## Como posso desenvolver e implementar serviços de borda com o {{site.data.keyword.ieam}}?
{: #dev_dep}

Consulte [Usando serviços de borda](../using_edge_services/using_edge_services.md).

## Quais plataformas de hardware de nó de borda o {{site.data.keyword.ieam}} suporta?
{: #hw_plat}

O {{site.data.keyword.ieam}} suporta diferentes arquiteturas de hardware por meio do pacote binário Debian {{site.data.keyword.linux_notm}} para o {{site.data.keyword.horizon}} ou por meio de contêineres do Docker. Para obter mais informações, consulte [Instalando o software {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## Posso executar qualquer distribuição do {{site.data.keyword.linux_notm}} nos meus nós de borda com o {{site.data.keyword.ieam}}?
{: #lin_dist}

Sim e não.

É possível desenvolver software de borda que usa qualquer distribuição do {{site.data.keyword.linux_notm}} como a imagem base dos contêineres Docker (se usar a instrução Dockerfile `FROM`) se essa base funcionar no kernel {{site.data.keyword.linux_notm}} do host em seus nós de borda. Isso significa que é possível usar qualquer distribuição para seus contêineres que o Docker possa executar em seus hosts de borda.

No entanto, o seu sistema operacional do host do nó de borda deve ser capaz de executar uma versão recente do Docker e ser capaz de executar o software do {{site.data.keyword.horizon}}. Atualmente, o software do {{site.data.keyword.horizon}} é fornecido apenas como pacotes Debian e RPM para nós de borda que executam o {{site.data.keyword.linux_notm}}. Para máquinas Apple Macintosh, uma versão de contêiner do Docker é fornecida. A equipe de desenvolvimento do {{site.data.keyword.horizon}} usa principalmente as distribuições Apple Macintosh ou Ubuntu ou Raspbian {{site.data.keyword.linux_notm}}.

Além disso, a instalação do pacote RPM foi testada em nós de borda configurados com Red Hat Enterprise Linux (RHEL) Versão 8.2.

## Quais linguagens de programação e ambientes são suportados pelo {{site.data.keyword.ieam}}?
{: #pro_env}

O {{site.data.keyword.ieam}} suporta quase qualquer linguagem de programação e biblioteca de software que possam ser configuradas para execução em um contêiner do Docker apropriado em seus nós de borda.

Se o seu software requer acesso a serviços de hardware ou de sistema operacional específicos, poderá ser necessário fornecer argumentos equivalentes ao `docker run` para suportar esse acesso. É possível especificar argumentos suportados dentro da seção `deployment` de seu arquivo de definição de contêiner do Docker.

## Há uma documentação detalhada para as APIs de REST fornecidas pelos componentes no {{site.data.keyword.ieam}}?
{: #rest_doc}

Sim. Para obter mais informações, consulte [{{site.data.keyword.ieam}} APIs](../api/edge_rest_apis.md). 

## O {{site.data.keyword.ieam}} usa o Kubernetes?
{: #use_kube}

Sim. O {{site.data.keyword.ieam}} usa os serviços Kubernetes [{{site.data.keyword.open_shift_cp}})](https://docs.openshift.com/container-platform/4.6/welcome/index.md).

## O {{site.data.keyword.ieam}} usa o MQTT?
{: #use_mqtt}

O {{site.data.keyword.ieam}} não usa o Message Queuing Telemetry Transport (MQTT) para oferecer suporte a suas próprias funções internas; no entanto, os programas que você implementa em seus nós de borda podem usar o MQTT para seus próprios fins. Estão disponíveis programas de exemplo que usam o MQTT e outras tecnologias (por exemplo, {{site.data.keyword.message_hub_notm}}, com base no Apache Kafka) para transportar dados de e para nós de borda.

## Quanto tempo normalmente leva depois de registrar um nó de borda antes que os contratos sejam formados e os contêineres correspondentes iniciem a execução?
{: #agree_run}

Geralmente, são necessários apenas alguns segundos após o registro para que o agente e um robô de contrato remoto finalizem um contrato para implementação do software. Depois que isso ocorre, o agente do {{site.data.keyword.horizon}} faz o download (`docker pull`) seus contêineres para o nó de borda, verifica suas assinaturas criptográficas com o {{site.data.keyword.horizon_exchange}} e os executa. Dependendo dos tamanhos de seus contêineres e do tempo que leva para iniciar e funcionar, pode levar de apenas alguns segundos a mais ou até muitos minutos antes que o nó de borda esteja totalmente operacional.

Depois de registrar um nó de borda, é possível executar o comando `hzn node list` para visualizar o estado de {{site.data.keyword.horizon}} em seu nó de borda. Quando o comando `hzn node list` mostra que o estado é `configured`, os agbots do {{site.data.keyword.horizon}} são capazes de descobrir o nó de borda e começar a firmar acordos.

Para observar as fases do processo de negociação de contrato, é possível usar o comando `hzn agreement list`.

Depois que uma lista de contratos for finalizada, é possível usar o comando `docker ps` para visualizar os contêineres em execução. Também é possível emitir o `docker inspet<container>` para ver informações mais detalhadas sobre a implementação de qualquer `<container>` específico.

## O software {{site.data.keyword.horizon}} e todos os outros softwares ou dados que estão relacionados a {{site.data.keyword.ieam}} serão removidos de um host do nó de borda?
{: #sw_rem}

Sim. Se o seu nó de borda estiver registrado, cancele o registro do nó de borda executando: 
```
hzn unregister -f -r
```
{: codeblock}

Quando o nó de extremidade não está registrado, é possível remover o software do {{site.data.keyword.horizon}} instalado, por exemplo, para execução de sistemas baseados em Debian:
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## Há um painel para visualizar os contratos e serviços que estão ativos em um nó de borda?
{: #db_node}

Também é possível usar a IU da web do {{site.data.keyword.ieam}} para observar seus nós e serviços de borda.

Além disso, é possível usar o comando `hzn` para obter informações sobre os contratos e serviços ativos usando a API de REST do agente do {{site.data.keyword.horizon}} local no nó de borda. Execute os comandos a seguir para usar a API para recuperar as informações relacionadas:

```
hzn node list hzn agreement list docker ps
```
{: codeblock}

## O que acontece quando um download de imagem de contêiner é interrompido por uma indisponibilidade de rede?
{: #image_download}

A API do Docker é usada para fazer download de imagens de contêiner. Se a API do Docker finalizar o download, ele retornará um erro para o agente. Por sua vez, o agente cancela a tentativa de implementação atual. Quando o Agbot detecta o cancelamento, ele inicia uma nova tentativa de implementação com o agente. Durante a tentativa de implementação subsequente, a API do Docker continua o download de onde ele parou. Esse processo continua até que a imagem seja totalmente transferida por download e a implementação possa continuar. A API de ligação do Docker é responsável pela extração da imagem e, em caso de falha, o contrato é cancelado.

## Como o {{site.data.keyword.ieam}} é seguro?
{: #ieam_secure}

* O {{site.data.keyword.ieam}} automatiza e usa de modo criptográfico a autenticação de chave pública e privada de serviços de borda à medida que ele se comunica com o hub de gerenciamento do {{site.data.keyword.ieam}} durante o fornecimento. A comunicação é sempre iniciada e controlada pelo nó de borda.
* O sistema possui credenciais de nó e de serviço.
* Verificação e autenticidade de software usando a verificação hash.

Consulte [Segurança no Edge](https://www.ibm.com/cloud/blog/security-at-the-edge).

## Como gerenciar a IA no Edge com modelos versus IA no Cloud?
{: #ai_cloud}

Normalmente, a IA na extremidade permite que você execute inferência de máquina no local com latência de subsegundo, o que permite resposta em tempo real com base no caso de uso e hardware (por exemplo, RaspberryPi, Intel x86 e Nvidia Jetson nano). O sistema de gerenciamento de modelo do {{site.data.keyword.ieam}} permite a implementação de modelos de IA atualizados sem nenhum tempo de inatividade de serviço.

Consulte [Modelos implementados na borda](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
