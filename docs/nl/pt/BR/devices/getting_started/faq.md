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

Obtenha respostas para algumas das perguntas mais frequentes (FAQs) sobre o {{site.data.keyword.edge_devices_notm}}.
{:shortdesc}

  * [O {{site.data.keyword.edge_devices_notm}} é um software livre?](#open_sourced)
  * [Como posso desenvolver e implementar serviços de borda usando o {{site.data.keyword.edge_devices_notm}}?](#dev_dep)
  * [Quais plataformas de hardware de nó de borda o {{site.data.keyword.edge_devices_notm}} suporta?](#hw_plat)
  * [Posso executar qualquer distribuição do {{site.data.keyword.linux_notm}} em meus nós de borda com o {{site.data.keyword.edge_devices_notm}}?](#lin_dist)
  * [Quais linguagens de programação e ambientes são suportados pelo {{site.data.keyword.edge_devices_notm}}?](#pro_env)
  * [Existe documentação detalhada para as APIs de REST fornecidas pelos componentes no {{site.data.keyword.edge_devices_notm}}?](#rest_doc)
  * [O {{site.data.keyword.edge_devices_notm}} usa Kubernetes?](#use_kube)
  * [O {{site.data.keyword.edge_devices_notm}} usa MQTT??](#use_mqtt)
  * [Quanto tempo normalmente leva depois de registrar um nó de borda antes que os contratos sejam formados e os contêineres correspondentes iniciem a execução?](#agree_run)
  * [O software {{site.data.keyword.horizon}} e todos os outros softwares ou dados relacionados ao {{site.data.keyword.edge_devices_notm}} podem ser removidos de um host de nó de borda?](#sw_rem)
  * [Há um painel para visualizar os contratos e serviços que estão ativos em um nó de borda?](#db_node)
  * [O que acontece quando um download de imagem de contêiner é interrompido por uma indisponibilidade de rede?](#image_download)
  * [Como o IEAM é protegido?](#ieam_secure)
  * [Como gerenciar a IA no Edge com modelos versus IA no Cloud?](#ai_cloud)

## O software do {{site.data.keyword.edge_devices_notm}} é um software livre?
{: #open_sourced}

{{site.data.keyword.edge_devices_notm}} é um produto IBM. Porém, seus componentes principais usam fortemente o projeto de software livre do [Open Horizon - EdgeX Project ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group). Muitas amostras e programas de exemplo que estão disponíveis no projeto {{site.data.keyword.horizon}} funcionam com o {{site.data.keyword.edge_devices_notm}}. Para obter mais informações sobre o projeto, consulte [Open Horizon - Grupo de projetos EdgeX ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://wiki.edgexfoundry.org/display/FA/Open+Horizon+-+EdgeX+Project+Group).

## Como posso desenvolver e implementar serviços de borda usando o {{site.data.keyword.edge_devices_notm}}?
{: #dev_dep}

Consulte [Usando serviços de borda](../developing/using_edge_services.md).

## Quais plataformas de hardware de nó de borda o {{site.data.keyword.edge_devices_notm}} suporta?
{: #hw_plat}

O {{site.data.keyword.edge_devices_notm}} suporta diferentes arquiteturas de hardware por meio do pacote binário Debian {{site.data.keyword.linux_notm}} para o {{site.data.keyword.horizon}} ou por meio de contêineres do Docker. Para obter mais informações, consulte [Instalando o software {{site.data.keyword.horizon}}](../installing/installing_edge_nodes.md).

## Posso executar qualquer distribuição do {{site.data.keyword.linux_notm}} nos meus nós de borda com o {{site.data.keyword.edge_devices_notm}}?
{: #lin_dist}

Sim e não.

É possível desenvolver um software de borda que use qualquer distribuição do {{site.data.keyword.linux_notm}} como a imagem base dos contêineres do Docker (se ele usar a instrução Dockerfile `FROM` ) se essa base funcionar no kernel do host do {{site.data.keyword.linux_notm}} em suas máquinas de borda. Isso significa que é possível usar qualquer distribuição para seus contêineres que o Docker possa executar em seus hosts de borda.

No entanto, seu sistema operacional de host da máquina de borda deve ser capaz de executar uma versão recente do Docker e ser capaz de executar o software {{site.data.keyword.horizon}}. Atualmente, o software {{site.data.keyword.horizon}} é fornecido apenas como um pacote Debian para máquinas de borda executando o {{site.data.keyword.linux_notm}}. Para máquinas Apple Macintosh, uma versão de contêiner do Docker é fornecida. A equipe de desenvolvimento do {{site.data.keyword.horizon}} usa principalmente as distribuições Apple Macintosh ou Ubuntu ou Raspbian {{site.data.keyword.linux_notm}}.

## Quais linguagens de programação e ambientes são suportados pelo {{site.data.keyword.edge_devices_notm}}?
{: #pro_env}

O {{site.data.keyword.edge_devices_notm}} suporta quase qualquer linguagem de programação e biblioteca de software que possam ser configuradas para execução em um contêiner do Docker apropriado em seus nós de borda.

Se o seu software requer acesso a serviços de hardware ou de sistema operacional específicos, poderá ser necessário fornecer argumentos equivalentes ao `docker run` para suportar esse acesso. É possível especificar argumentos suportados dentro da seção `deployment` de seu arquivo de definição de contêiner do Docker.

## Há uma documentação detalhada para as APIs de REST fornecidas pelos componentes no {{site.data.keyword.edge_devices_notm}}?
{: #rest_doc}

Yes. Para obter mais informações, consulte [{{site.data.keyword.edge_devices_notm}} APIs](../installing/edge_rest_apis.md). 

## O {{site.data.keyword.edge_devices_notm}} usa o Kubernetes?
{: #use_kube}

Yes. O {{site.data.keyword.edge_devices_notm}} usa serviços do Kubernetes do [{{site.data.keyword.open_shift_cp}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://docs.openshift.com/container-platform/4.4/welcome/index.html).

## O {{site.data.keyword.edge_devices_notm}} usa o MQTT?
{: #use_mqtt}

O {{site.data.keyword.edge_devices_notm}} não usa o Message Queuing Telemetry Transport (MQTT) para suportar suas próprias funções internas, no entanto, os programas que você implementar em suas máquinas de borda podem usar o MQTT livremente para seus próprios propósitos. Há programas de exemplo disponíveis que usam MQTT e outras tecnologias (por exemplo, o {{site.data.keyword.message_hub_notm}}, com base no Apache Kafka) para transportar dados para máquinas de borda e a partir delas.

## Quanto tempo normalmente leva depois de registrar um nó de borda antes que os contratos sejam formados e os contêineres correspondentes iniciem a execução?
{: #agree_run}

Geralmente, são necessários apenas alguns segundos após o registro para que o agente e um robô de contrato remoto finalizem um contrato para implementação do software. Após isso ocorrer, o agente {{site.data.keyword.horizon}} faz download (`docker pull`) de seus contêineres para a máquina de borda, verifica suas assinaturas criptográficas com o {{site.data.keyword.horizon_exchange}} e as executa. Dependendo dos tamanhos de seus contêineres e do tempo que eles levam para iniciar e entrar em funcionamento, pode levar mais alguns segundos ou muitos minutos para que a máquina de borda esteja totalmente operacional.

Após registrar uma máquina de borda, é possível executar o comando `hzn node list` para visualizar o estado do {{site.data.keyword.horizon}} em sua máquina de borda. Quando o comando `hzn node list` mostrar que o estado é `configured`, os robôs de contrato do {{site.data.keyword.horizon}} serão capazes de descobrir a máquina de borda e começar a formar contratos.

Para observar as fases do processo de negociação de contrato, é possível usar o comando `hzn agreement list`.

Depois que uma lista de contratos for finalizada, é possível usar o comando `docker ps` para visualizar os contêineres em execução. Também é possível emitir o `docker inspet<container>` para ver informações mais detalhadas sobre a implementação de qualquer `<container>` específico.

## O software {{site.data.keyword.horizon}} e todos os outros softwares ou dados que estão relacionados a {{site.data.keyword.edge_devices_notm}} serão removidos de um host do nó de borda?
{: #sw_rem}

Yes. Se sua máquina de borda estiver registrada, cancele o registro da máquina de borda executando: 
```
hzn unregister -f -r
```
{: codeblock}

Quando a máquina de borda estiver com registro cancelado, remova o software instalado do {{site.data.keyword.horizon}}:
```
sudo apt purge -y bluehorizon horizon horizon-cli
```
{: codeblock}

## Há um painel para visualizar os contratos e serviços que estão ativos em um nó de borda?
{: #db_node}

Também é possível usar a IU da web do {{site.data.keyword.edge_devices_notm}} para observar seus nós e serviços de borda.

Além disso, é possível usar o comando `hzn` para obter informações sobre os contratos e serviços ativos usando a API de REST do agente local no nó de borda. Execute os comandos a seguir para usar a API para recuperar as informações relacionadas:
```
hzn node list
hzn agreement list
docker ps
```
{: codeblock}

## O que acontece quando um download de imagem de contêiner é interrompido por uma indisponibilidade de rede?
{: #image_download}

A API do docker é usada para fazer download de imagens de contêiner. Se a API do docker finalizar o download, ele retornará um erro para o agente. Por sua vez, o agente cancela a tentativa de implementação atual. Quando o Agbot detecta o cancelamento, ele inicia uma nova tentativa de implementação com o agente. Durante a tentativa de implementação subsequente, a API do docker continua o download de onde ele parou. Esse processo continua até que a imagem seja totalmente transferida por download e a implementação possa continuar. A API de ligação do docker é responsável pelo pull de imagem e, no caso de falha, o contrato é cancelado.

## Como o IEAM é protegido?
{: #ieam_secure}

* O {{site.data.keyword.ieam}} automatiza e usa de modo criptográfico a autenticação de chave pública e privada de serviços de borda à medida que ele se comunica com o hub de gerenciamento do {{site.data.keyword.ieam}} durante o fornecimento. A comunicação é iniciada e controlada sempre pelo dispositivo de borda. 
* O sistema possui credenciais de nó e de serviço.
* Verificação e autenticidade de software usando a verificação hash.

Consulte
[Segurança no Edge ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/cloud/blog/security-at-the-edge).

## Como gerenciar a IA no Edge com modelos versus IA no Cloud?
{: #ai_cloud}

Normalmente, a IA na borda permite a execução de inferência de máquina no local com uma subsegunda latência, o que permite uma resposta em tempo real com base no caso de uso e no hardware (por exemplo,RaspberryPi, Intel x86 e Nvidia Jetson nano). O sistema de gerenciamento de modelo do {{site.data.keyword.ieam}} permite a implementação de modelos de IA atualizados sem nenhum tempo de inatividade de serviço.

Consulte
[Modelos implementados no Edge ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://www.ibm.com/cloud/blog/models-deployed-at-the-edge).
