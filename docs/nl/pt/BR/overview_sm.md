---

copyright:
years: 2021
lastupdated: "2021-07-20"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visão geral do Secrets Manager
{: #overviewofsm}

Os serviços implementados na borda geralmente exigem acesso aos serviços em nuvem, o que significa que o serviço precisa de credenciais para se autenticar no serviço em nuvem. O Secrets Manager fornece um mecanismo seguro que permite que as credenciais sejam armazenadas, implantadas e gerenciadas sem expor os detalhes dentro de metadados do {{site.data.keyword.ieam}} (por exemplo, definições e políticas de serviço) ou a outros usuários do sistema que não devem ter acesso ao segredo. O Secrets Manager é um componente plugável de {{site.data.keyword.ieam}}. Atualmente, HashiCorp Vault é o único Secrets Manager suportado.

Um segredo é um ID de usuário/senha, certificado, chave RSA ou qualquer outra credencial que conceda acesso a um recurso protegido de que um aplicativo de borda precisa para executar sua função. Os segredos são armazenados no Secrets Manager. Um segredo tem um nome, que é usado para identificar o segredo, mas que não fornece nenhuma informação sobre os detalhes do próprio segredo. Os segredos são administrados pela CLI do {{site.data.keyword.ieam}} ou por um administrador, usando a IU ou a CLI do Secrets Manager.

Um desenvolvedor de serviços declara a necessidade de um segredo dentro de uma definição de serviço do {{site.data.keyword.ieam}}. O implementador de serviço anexa (ou vincula) um segredo do Secrets Manager à implementação do serviço, associando o serviço a um segredo do Secrets Manager. Por exemplo; suponha que um desenvolvedor precise acessar o serviço de nuvem XYZ por meio de autenticação básica. O desenvolvedor atualiza a definição de serviço do {{site.data.keyword.ieam}} para incluir um segredo chamado myCloudServiceCred. O implementador de serviço vê que o serviço requer um segredo para implementá-lo e está ciente de um segredo no Secrets Manager denominado cloudServiceXYZSecret que contém credenciais de autenticação básicas. O implementador de serviço atualiza a política de implementação (ou padrão) para indicar que o segredo do serviço denominado myCloudServiceCreds deve conter as credenciais do segredo do Secrets Manager denominado cloudServiceXYZSecret. Quando o implementador de serviços publica a política de implementação (ou padrão), o {{site.data.keyword.ieam}} implementará de forma segura os detalhes de cloudServiceXYZSecret para todos os nós de borda compatíveis com a política de implementação (ou padrão).
