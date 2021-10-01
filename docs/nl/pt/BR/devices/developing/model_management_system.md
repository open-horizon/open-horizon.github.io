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

Este exemplo o ajuda a aprender como desenvolver um {{site.data.keyword.edge_service}} que usa o sistema de gerenciamento de modelo (MMS). Você pode usar esse sistema para implementar e atualizar os modelos de máquina de aprendizado que são usados por serviços de borda que são executados em seus nós de borda.
{:shortdesc}

## Antes de iniciar
{: #mms_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID"
which git jq make
ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem
cat /etc/default/horizon
```

## Procedimento
{: #mms_procedure}

Este exemplo faz parte do projeto de software livre [{{site.data.keyword.horizon_open}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/). Siga as etapas em [Criando seu próprio serviço de borda de MMS Hello ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/blob/master/edge/services/helloMMS/CreateService.md)) e, em seguida, retorne aqui.

## O que fazer a seguir
{: #mms_what_next}

* Experimente os outros exemplos de serviços de borda em [Desenvolvendo um serviço borda para dispositivos](developing.md).

## Leitura Adicional

* [Detalhes de gerenciamento de modelo](../developing/model_management_details.md)
