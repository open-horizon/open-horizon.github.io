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

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) suporta várias funções. Sua função determina as ações que podem ser executadas.
{:shortdesc}

## Organizações
{: #orgs}

O {{site.data.keyword.ieam}} suporta o conceito geral de ocupação variada  por meio de organizações, em que cada locatário tem a sua própria organização. As organizações separam recursos; portanto, os usuários de cada organização não podem criar ou modificar recursos em uma organização diferente. Além disso, os recursos em uma organização podem ser visualizados apenas por usuários dessa organização (a menos que os recursos sejam marcados como públicos). Os recursos marcados como públicos são os únicos recursos que podem ser visualizados por outras organizações.

A organização IBM fornece serviços e padrões predefinidos. Embora os recursos dessa organização sejam públicos, ela não se destina a conter todo o conteúdo público no hub de gerenciamento do {{site.data.keyword.ieam}}.

Por padrão, uma organização é criada durante a instalação do {{site.data.keyword.ieam}} com um nome de sua escolha. É possível criar organizações adicionais conforme necessário. Para obter mais informações sobre como adicionar organizações ao hub de gerenciamento, consulte [Ocupação variada](../admin/multi_tenancy.md).

## Identidades
{: #ids}

Existem quatro tipos de identidades dentro do {{site.data.keyword.ieam}}:

* Usuários do Identity and Access Management (IAM). Os usuários IAM são reconhecidos por todos os componentes  {{site.data.keyword.ieam}}: IU, Exchange, CLI **hzn**, CLI **cloudctl**, CLI **oc** e CLI **kubectl**.
  * O IAM fornece o plug-in LDAP, de modo que os usuários LDAP conectados ao IAM se comportam como usuários IAM
  * As chaves da API do IAM (usadas com o comando **hzn**) se comportam como usuários do IAM
* Usuários apenas do Exchange: o usuário raiz do Exchange é um exemplo disso. Normalmente, você não precisa criar outros usuários locais do Exchange. Como prática recomendada, gerencie usuários no IAM e use essas credenciais de usuário (ou chaves de API associadas a esses usuários) para fazer a autenticação no {{site.data.keyword.ieam}}.
* Nós do Exchange (dispositivos de borda ou clusters de borda)
* Robôs de contrato do Exchange

### RBAC (Role-Based Access Control)
{: #rbac_roles}

O {{site.data.keyword.ieam}} inclui as funções a seguir:

| **Função**    | **Acesso**    |  
|---------------|--------------------|
| Usuário do IAM | Por meio do IAM, podem receber estas funções de hub de gerenciamento: o administrador de Cluster, o administrador, o operador, o editor e o visualizador. Uma função do IAM é atribuída a usuários ou grupos de usuários quando você os adiciona a uma equipe do IAM. O acesso da equipe aos recursos pode ser controlado pelo namespace do Kubernetes. Os usuários do IAM também podem receber qualquer uma das funções do Exchange abaixo usando a CLI **hzn exchange**. |
| Usuário raiz do Exchange | Tem privilégios ilimitados no Exchange. Esse usuário é definido no arquivo de configuração do Exchange. Ele pode ser desativado, se desejado. |
| Usuário administrador do hub do Exchange | Pode visualizar a lista de organizações, visualizar os usuários em uma organização e criar ou excluir organizações. |
| Usuário administrador da organização do Exchange | Tem privilégio ilimitado do Exchange dentro da organização. |
| Usuário do exchange | Pode criar recursos do Exchange (nós, serviços, padrões, políticas) na organização. Pode atualizar ou excluir recursos de propriedade desse usuário. Pode ler todos os serviços, padrões e políticas na organização e serviços e padrões públicos em outras organizações. Pode ler os nós pertencentes a este usuário. |
| Nós do Exchange | Pode ler seu próprio nó no Exchange e ler todos os serviços, padrões e políticas na organização e serviço e padrões públicos em outras organizações. Essas são as únicas credenciais que devem ser salvas no nó de borda, porque elas têm o privilégio mínimo necessário para operar o nó de borda.|
| Robôs de contrato do Exchange | Os robôs de contrato na organização IBM podem ler todos os nós, serviços, padrões e políticas em todas as organizações. |
{: caption="Tabela 1. Funções do RBAC" caption-side="top"}
