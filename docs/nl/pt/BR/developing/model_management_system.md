---

copyright:
years: 2020
lastupdated: "2020-02-6"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello World usando o gerenciamento de modelo
{: #model_management_system}

Este exemplo ajuda você a aprender como desenvolver um {{site.data.keyword.edge_service}} ({{site.data.keyword.ieam}}) que usa o sistema de gerenciamento de modelo (MMS). Você pode usar esse sistema para implementar e atualizar os modelos de máquina de aprendizado que são usados por serviços de borda que são executados em seus nós de borda.
{:shortdesc}

## Antes de Começar
{: #mms_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```
{: codeblock}

## Procedimento
{: #mms_procedure}

Este exemplo faz parte do projeto de software livre do [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga as etapas em [Criando seu próprio serviço de borda Hello MMS](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) e, em seguida, retorne aqui.

## O que fazer em seguida
{: #mms_what_next}

* Experimente os outros exemplos de serviços de borda em [Desenvolvendo um serviço borda para dispositivos](../OH/docs/developing/developing.md).

## Leitura Adicional

* [Sistema de gerenciamento de modelo](../OH/docs/developing/model_management_details.md)
