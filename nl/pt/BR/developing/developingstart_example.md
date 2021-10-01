---

copyright:
years: 2019
lastupdated: "2019-06-24"  

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Criando o seu próprio serviço de borda Hello World
{: #dev_start_ex}

O exemplo a seguir usa um serviço `Hello World` simples para ajudá-lo a aprender mais sobre o desenvolvimento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). Com esse exemplo, você desenvolve um serviço de borda único que suporta três arquiteturas de hardware e usa as ferramentas de desenvolvimento do {{site.data.keyword.horizon}}.
{:shortdesc}

## Antes de Começar
{: #dev_start_ex_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:
```
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procedimento
{: #dev_start_ex_procedure}

Este exemplo faz parte do projeto de software livre do [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga as etapas em [Construindo e publicando seu próprio Serviço de borda de exemplo Hello World](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld/CreateService.md#build-publish-your-hw) e, em seguida, retorne aqui.

## O que fazer em seguida
{: #dev_start_ex_what_next}

* Experiente os outros exemplos de serviço de borda em [Desenvolvendo um serviço de borda para dispositivos](../OH/docs/developing/developing.md).
