---

copyright:
years: 2021
lastupdated: "2021-08-16"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Desenvolver um serviço usando segredos
{: #using secrets}

<img src="../images/edge/10_Secrets.svg" style="margin: 3%" alt="Developing a service using secrets"> 

# Detalhes do Secrets Manager
{: #secrets_details}

O Secrets Manager fornece armazenamento seguro para informações sensíveis como credenciais de autenticação ou chaves de criptografia. Esses segredos são implementados de forma segura por {{site.data.keyword.ieam}} para que apenas os serviços configurados para receber um segredo tenham acesso a ele. O [exemplo de segredo do Hello World](https://github.com/open-horizon/examples/blob/master/edge/services/helloSecretWorld/CreateService.md) fornece uma visão geral de como explorar segredos em um serviço de borda.

O {{site.data.keyword.ieam}} suporta o uso de [Hashicorp Vault](https://www.vaultproject.io/) como o Secrets Manager. Segredos criados usando a CLI hzn são mapeados para segredos de Vault usando o [KV V2 Secrets Engine](https://www.vaultproject.io/docs/secrets/kv/kv-v2). Isso significa que os detalhes de cada segredo do {{site.data.keyword.ieam}} são compostos de uma chave e um valor. Ambos são armazenados como parte dos detalhes do segredo, e ambos podem ser configurados para qualquer valor de sequência. Um uso comum deste recurso é fornecer o tipo de segredo sobre as informações chave e sensíveis como o valor. Por exemplo, configure a chave como "basicauth" e configure o valor como "user:password". Ao fazer isso, o desenvolvedor de serviços pode interrogar o tipo de segredo, possibilitando que o código de serviço manipule o valor corretamente.

Os nomes de segredos no Secrets Manager nunca são conhecidos por uma implementação de serviço. Não é possível transmitir informações da área segura para uma implementação de serviço usando o nome de um segredo.

Os segredos são armazenados no KV V2 Secrets Engine prefixando o nome do segredo com openhorizon e a organização do usuário. Isso garante que segredos criados por usuários do {{site.data.keyword.ieam}} sejam isolados de outros usos do Vault por outras integrações, e ele garante que o isolamento de vários locatários seja mantido.

Os nomes secretos são gerenciados por administradores da organização {{site.data.keyword.ieam}} (ou usuários ao usar segredos particulares do usuário). As Vault Access Control Lists (ACLs) controlam quais segredos um usuário {{site.data.keyword.ieam}} é capaz de gerenciar. Isso é realizado por meio de um plugin de autenticação de Vault que delega autenticação de usuário para a troca do {{site.data.keyword.ieam}}. Ao autenticar com sucesso um usuário, o plugin de autenticação no Vault criará um conjunto de políticas de ACL específicas para este usuário. Um usuário com privilégios de administrador na troca pode:
- Incluir, remover, ler e listar todos os segredos de organização.
- Incluir, remover, ler e listar todos os segredos privados nesse usuário.
- Remova e liste os segredos privados do usuário de outros usuários na organização, mas não é possível incluir ou ler esses segredos.

Um usuário sem privilégios do administrador pode:
- Liste todos os segredos de organização, mas não é possível incluir, remover ou lê-los.
- Incluir, remover, ler e listar todos os segredos privados nesse usuário.

O robô de contrato do {{site.data.keyword.ieam}} também tem acesso a segredos a fim de ser capaz de implementá-los em nós de borda. O robô de contrato mantém um login renovável no Vault e recebe políticas de ACL específicas para seus propósitos. Um robô de contrato pode:
- Leia segredos amplos da organização e qualquer segredo privado do usuário em qualquer organização, mas não é possível incluir, remover ou listar quaisquer segredos.

O usuário raiz do Exchange e os administradores do hub do Exchange não têm permissões no Vault. Veja [Controle de acesso baseado em função](../user_management/rbac.html) para obter mais informações sobre essas funções.
