---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Hello World com um segredo
{: #secrets}

Este exemplo ensina como desenvolver um {{site.data.keyword.edge_service}} que usa segredos. Os segredos garantem que as credenciais de login e outras informações sensíveis sejam mantidas seguras.
{:shortdesc}

## Antes de Começar
{: #secrets_begin}

Conclua as etapas de pré-requisito em [Preparando para criar um serviço de borda](service_containers.md). Como resultado, estas variáveis de ambiente devem ser configuradas, estes comandos devem ser instalados e estes arquivos devem existir:

```bash
echo "HZN_ORG_ID=$HZN_ORG_ID, HZN_EXCHANGE_USER_AUTH=$HZN_EXCHANGE_USER_AUTH, DOCKER_HUB_ID=$DOCKER_HUB_ID" which git jq make ls ~/.hzn/keys/service.private.key ~/.hzn/keys/service.public.pem cat /etc/default/horizon
```

## Procedimento
{: #secrets_procedure}

Este exemplo faz parte do projeto de software livre do [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/). Siga as etapas em [Criando seu próprio serviço secreto do Hello](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md)) e em seguida, retorne aqui.

## O que fazer em seguida
{: #secrets_what_next}

* Experimente os outros exemplos de serviços de borda em [Desenvolvendo um serviço borda para dispositivos](developing.md).

## Leitura Adicional

* [Usando segredos](../developing/secrets_details.md)
