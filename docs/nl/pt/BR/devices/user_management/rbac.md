---

copyright:
years: 2019
lastupdated: "2019-09-27"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Controle de acesso baseado na função
{: #rbac}

O {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} suporta várias funções. Sua função determina as ações que podem ser executadas.
{:shortdesc}

## Organizações
{: #orgs}

As organizações dentro do {{site.data.keyword.ieam}} são usadas para separar o
acesso aos recursos. Os recursos para uma organização podem ser visualizados apenas pelas organizações, a menos
que os recursos sejam marcados explicitamente como públicos. Os recursos que estão marcados como públicos são os únicos
recursos que podem ser visualizados entre as organizações.

A organização IBM é usada para fornecer serviços e padrões predefinidos.

Dentro do {{site.data.keyword.ieam}}, seu nome da organização é o nome de seu cluster.

## Identidades
{: #ids}

Há três tipos de identidades dentro do {{site.data.keyword.ieam}}:

* Há dois tipos de canais. Os usuários podem acessar o console do {{site.data.keyword.ieam}} e o Exchange.
  * Usuários do Identity and Access Management (IAM). Os usuários do IAM são reconhecidos pelo {{site.data.keyword.ieam}} Exchange.
    * O IAM fornece o plug-in LDAP, de modo que os usuários LDAP conectados ao IAM se comportam como usuários IAM
    * As chaves da API do IAM (usadas com o comando **hzn**) se comportam como usuários do IAM
  * Usuários locais do Exchange: o usuário raiz do Exchange é um exemplo disso. Geralmente não é necessário criar outros usuários locais do Exchange.
* Nós (dispositivos de borda ou clusters de borda)
* AgBots

### RBAC (Role-Based Access Control)
{: #rbac_roles}

O {{site.data.keyword.ieam}} inclui as funções a seguir:

| **Função**    | **Acesso**    |  
|---------------|--------------------|
| Usuário raiz do Exchange |Tem privilégios ilimitados no Exchange. Esse usuário é definido no arquivo de configuração do Exchange. Ele pode ser desativado, se desejado. |
|Usuário administrativo ou chave de API |Tem privilégios ilimitados dentro da organização. |
|Usuário não administrativo ou chave de API | Pode criar recursos do Exchange (nós, serviços, padrões, políticas) na organização. Pode atualizar ou excluir recursos de propriedade desse usuário. Pode ler todos os serviços, padrões e políticas na organização e serviços e padrões públicos em outras organizações. |
| Nós | Pode ler seu próprio nó no Exchange e ler todos os serviços, padrões e políticas na organização e serviço e padrões públicos em outras organizações. |
| Agbots | Os robôs de contrato na organização IBM podem ler todos os nós, serviços, padrões e políticas em todas as organizações. |
{: caption="Tabela 1. Funções do RBAC" caption-side="top"}
