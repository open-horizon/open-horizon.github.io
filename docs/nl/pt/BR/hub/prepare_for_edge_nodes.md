---

copyright:
years: 2020
lastupdated: "2020-10-13"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Criando sua chave de API
{: #prepare_for_edge_nodes}

Este conteúdo explica como criar uma chave de API e reunir alguns arquivos e valores da variável de ambiente que são necessários quando você configura nós de borda. Execute estas etapas em um host que pode se conectar ao seu cluster do hub de gerenciamento do {{site.data.keyword.ieam}}.

## Antes de Começar

* Se você ainda não instalou o **cloudctl**, consulte [Instalando o cloudctl, o oc e o kubectl](../cli/cloudctl_oc_cli.md) para fazer isso.
* Entre em contato com o administrador do {{site.data.keyword.ieam}} para obter as informações necessárias para efetuar login no hub de gerenciamento por meio do **cloudctl**.

## Procedimento

Se você tiver configurado uma conexão LDAP, será possível usar as credenciais de usuários adicionados para efetuar login e criar chaves de API, será possível usar as credenciais de administrador iniciais impressas pelo seguinte comando:
```
echo "$(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_username}' | base64 --decode) // $(oc -n ibm-common-services get secret platform-auth-idp-credentials -o jsonpath='{.data.admin_password}' | base64 --decode)"
```
{: codeblock}

1. Use `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}}. Especifique o usuário para o qual você deseja criar uma chave de API:

   ```bash
   cloudctl login -a <cluster-url> -u <user> -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Cada usuário que está configurando nós de borda deve ter uma chave de API. É possível usar a mesma chave de API para configurar todos os seus nós de borda (ela não é salva nos nós de borda). Crie uma chave de API:

   ```bash
   cloudctl iam api-key-create "<choose-an-api-key-name>" -d "<choose-an-api-key-description>"
   ```
   {: codeblock}

   Localize o valor da chave na saída de comando; esta é a linha que começa com **Chave de API**. Salve o valor da chave para uso futuro porque não será possível consultá-lo por meio do sistema posteriormente.

3. Entre em contato com o administrador do {{site.data.keyword.ieam}} para obter ajuda na configuração dessas variáveis de ambiente:

  ```bash
  export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>   export HZN_ORG_ID=<your-exchange-organization>   mgmtHubIngress=$(oc get cm management-ingress-ibmcloud-cluster-info -o jsonpath='{.data.cluster_ca_domain}')   export HZN_FSS_CSSURL=https://$mgmtHubIngress/edge-css/   echo "export HZN_FSS_CSSURL=$HZN_FSS_CSSURL"
  ```
  {: codeblock}

## O que vem depois

Quando você estiver pronto para configurar nós de borda, siga as etapas em [Instalando nós de borda](../installing/installing_edge_nodes.md).

