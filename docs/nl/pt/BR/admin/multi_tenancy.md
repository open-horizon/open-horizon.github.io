---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Ocupação variada
{: #multit}

## Locatários no {{site.data.keyword.edge_notm}}
{: #tenants}

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) suporta o conceito geral de TI de ocupação variada por meio de organizações, onde cada locatário tem sua própria organização. As organizações separam recursos; portanto, os usuários de cada organização não podem criar ou modificar recursos em uma organização diferente. Além disso, os recursos em uma organização podem ser visualizados apenas por usuários nessa organização, a menos que os recursos sejam marcados como públicos.

### Casos de uso comuns

Dois casos de uso amplo são usados para a ocupação variada no {{site.data.keyword.ieam}}:

* Uma empresa tem várias unidades de negócios nas quais cada unidade de negócios é uma organização separada no mesmo hub de gerenciamento do {{site.data.keyword.ieam}}. Considere as razões jurídicas, empresariais ou técnicas pelas quais cada unidade de negócios deve ser uma organização separada, com seu próprio conjunto de recursos do {{site.data.keyword.ieam}} que, por padrão, não são acessíveis para outras unidades de negócios. Mesmo com organizações separadas, a empresa tem a opção de usar um grupo comum de administradores para gerenciar todas as organizações.
* Uma empresa hospeda o {{site.data.keyword.ieam}} como um serviço para seus clientes, que contam individualmente com uma ou mais organizações no hub de gerenciamento. Nesse caso, os administradores da organização são exclusivos para cada cliente.

O caso de uso que você escolher determinará sua configuração do {{site.data.keyword.ieam}} e do Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)).

### Tipos de Usuários do {{site.data.keyword.ieam}}
{: #user-types}

O {{site.data.keyword.ieam}} suporta essas funções de usuário:

| **Função** | **Acesso** |
|--------------|-----------------|
| **Administrador de hub** | Gerencia a lista de organizações do {{site.data.keyword.ieam}} criando, modificando e excluindo organizações conforme necessário e criando administradores da organização dentro de cada organização. |
| **Administrador da organização** | Gerencia os recursos em uma ou mais organizações do {{site.data.keyword.ieam}}. Os administradores da organização podem criar, visualizar ou modificar qualquer recurso (usuário, nó, serviço, política ou padrão) dentro da organização, mesmo quando não são proprietários dele. |
| **Usuário regular** | Cria nós, serviços, políticas e padrões dentro da organização e modifica ou exclui os recursos que eles criaram. Visualiza todos os serviços, políticas e padrões na organização que outros usuários criaram. |
{: caption="Tabela 1. Funções de usuário do {{site.data.keyword.ieam}}" caption-side="top"}

Consulte [Controle de acesso baseado na função](../user_management/rbac.md) para obter uma descrição de todas as funções do {{site.data.keyword.ieam}}.

## O relacionamento entre o IAM e o {{site.data.keyword.ieam}}
{: #iam-to-ieam}

O serviço IAM (Identity and Access Manager) gerencia usuários para todos os produtos baseados em Cloud Pak, incluindo o {{site.data.keyword.ieam}}. O IAM, por sua vez, usa o LDAP para armazenar os usuários. Cada usuário do IAM pode ser um membro de uma ou mais equipes do IAM. Como cada equipe do IAM está associada a uma conta do IAM, um usuário do IAM poderá indiretamente ser um membro de uma ou mais contas do IAM. Consulte [Ocupação variada do IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html) para obter detalhes.

A troca do {{site.data.keyword.ieam}} fornece serviços de autenticação e autorização para os outros componentes do {{site.data.keyword.ieam}}. A troca delega a autenticação de usuários para o IAM, o que significa que credenciais do usuário do IAM são passadas para a troca e ela conta com o IAM para determinar se elas são válidas. Cada função de usuário (administrador de hub, administrador da organização ou usuário regular) é definida na troca e isso determina as ações que os usuários têm permissão para executar no {{site.data.keyword.ieam}}.

Cada organização na troca do {{site.data.keyword.ieam}} está associada a uma conta do IAM. Portanto, automaticamente, os usuários do IAM em uma conta do IAM são membros da organização {{site.data.keyword.ieam}} correspondente. A única exceção a esta regra é que a função de administrador de hub do {{site.data.keyword.ieam}} é considerada externa a qualquer organização específica; portanto, não importa a conta do IAM na qual o administrador de hub está.

Para resumir o mapeamento entre o IAM e o {{site.data.keyword.ieam}}:

| **IAM** | **Relacionamento** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| Conta do IAM | mapeia para | Organização do {{site.data.keyword.ieam}} |
| Usuário do IAM | mapeia para | Usuário do {{site.data.keyword.ieam}} |
| Não há nenhuma contraparte do IAM para a função | nenhum | Função do {{site.data.keyword.ieam}} |
{: caption="Tabela 2. IAM - Mapeamento do {{site.data.keyword.ieam}}" caption-side="top"}

As credenciais usadas para efetuar login no console do {{site.data.keyword.ieam}} são o usuário e a senha do IAM. As credenciais usadas para a CLI do {{site.data.keyword.ieam}} (`hzn`) são uma chave de API do IAM.

## A organização inicial
{: #initial-org}

Por padrão, uma organização foi criada durante a instalação do {{site.data.keyword.ieam}} com um nome que você forneceu. Se os recursos de ocupação variada do {{site.data.keyword.ieam}} não forem necessários, esta organização inicial será suficiente para o seu uso do {{site.data.keyword.ieam}} e será possível ignorar o restante desta página.

## Criação de um usuário administrativo do hub
{: #create-hub-admin}

A primeira etapa de uso de ocupação variada do {{site.data.keyword.ieam}} é criar um ou mais administradores de hub que possam criar e gerenciar as organizações. Para isso, deve-se criar ou escolher uma conta e um usuário do IAM que terão a função de administrador de hub designada a eles.

1. Use `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}} como o administrador de cluster. (Se você ainda não tiver instalado o `cloudctl`, consulte [Instalando cloudctl, kubectl e oc](../cli/cloudctl_oc_cli.md) para obter instruções.)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation
   ```
   {: codeblock}

2. Se você ainda não tiver conectado uma instância LDAP ao IAM, faça isso agora seguindo [Conectando-se ao seu diretório LDAP](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

3. O usuário administrativo do hub deve estar em uma conta do IAM. (Não importa qual conta.) Se você ainda não tiver uma conta do IAM na qual deseja que o usuário administrativo do hub esteja, crie uma:

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. Crie ou escolha um usuário LDAP dedicado à função administrativa de hub do {{site.data.keyword.ieam}}. Não use o mesmo usuário que um administrador de hub do {{site.data.keyword.ieam}} e um administrador de organização do {{site.data.keyword.ieam}} (ou usuário regular do {{site.data.keyword.ieam}}).

5. Importe o usuário para o IAM:

   ```bash
   HUB_ADMIN_USER=<the IAM/LDAP user name of the hub admin user>    cloudctl iam user-import -u $HUB_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. Designe a função administrativa de hub para o usuário do IAM:

   ```bash
   EXCHANGE_ROOT_PW=<password for the exchange root user>    export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW    export HZN_EXCHANGE_URL=<the URL of your exchange>    hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. Verifique se o usuário tem a função de usuário do administrador de hub. Na saída do comando a seguir, você deve ver `"hubAdmin": true`.

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### Use o usuário administrativo do hub com a CLI do {{site.data.keyword.ieam}}
{: #verify-hub-admin}

Crie uma chave de API para o usuário administrativo do hub e verifique se ele tem os recursos de administrador do hub:

1. Use `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}} como o administrador de hub:

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. Crie uma chave de API o usuário administrativo do hub:

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   Localize o valor da chave de API na linha de saída de comando que inicia com **Chave de API**. Salve o valor da chave em um local seguro para uso futuro porque não será possível consultá-lo por meio do sistema posteriormente. Além disso, configure-o nesta variável para os comandos subsequentes:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Exibir todas as organizações no hub de gerenciamento. Você deve ver a organização inicial que é criada durante a instalação, bem como as organizações **raiz** e **IBM**:

   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    hzn exchange org list -o root
   ```
   {: codeblock}

4. Efetue login no console de gerenciamento do [{{site.data.keyword.ieam}}](../console/accessing_ui.md) com o usuário e a senha do IAM do seu administrador de hub. O console de administração da organização é exibido porque suas credenciais de login têm a função administrativa de hub. Use este console para visualizar, gerenciar e incluir organizações. Ou é possível incluir organizações usando a CLI na seção a seguir.

## Criando uma organização usando a CLI
{: #create-org}

As organizações podem ser criadas usando a CLI em vez de o console de administração da organização do {{site.data.keyword.ieam}}. Um pré-requisito para criar uma organização é criar ou escolher uma conta do IAM que será associada à organização. Outro pré-requisito é criar ou escolher um usuário do IAM que será designado com a função administrativa da organização.

**Nota**: Um nome de organização não pode conter sublinhados (_), vírgulas (,), espaços em branco ( ), aspas simples (') ou pontos de interrogação (?).

Desempenhe estas etapas:

1. Se você ainda não tiver criado um usuário administrativo de hub, faça isso executando as etapas da seção anterior. Assegure-se de que a chave de API do administrador de hub esteja configurada na variável a seguir:

   ```bash
   HUB_ADMIN_API_KEY=<IAM API key of the hub admin user>
   ```
   {: codeblock}

2. Use `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}} como o administrador de cluster e crie uma conta do IAM com a qual a nova organização do {{site.data.keyword.ieam}} será associada. (Se você ainda não tiver instalado `cloudctl`, consulte [Instalando cloudctl, kubectl e oc](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <password> --skip-ssl-validation    NEW_ORG_ID=<new organization name>    IAM_ACCOUNT_NAME="$NEW_ORG_ID"    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. Crie ou escolha um usuário LDAP que será designado com a função administrativa da organização e importe-a para o IAM. Não é possível usar um usuário administrativo de hub como um usuário administrativo de organização, mas é possível usar o mesmo usuário administrativo de organização em mais de uma conta do IAM. Portanto, isso permite que eles gerenciem mais de uma organização do {{site.data.keyword.ieam}}.

   ```bash
   ORG_ADMIN_USER=<the IAM/LDAP user name of the organization admin user>    cloudctl iam user-import -u $ORG_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. Configure essas variáveis de ambiente, crie a organização do {{site.data.keyword.ieam}} e verifique se ela existe:
   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    export HZN_EXCHANGE_URL=<URL of your exchange>    hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID    hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID    hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. Designe a função de usuário administrativo da organização para o usuário do IAM que você escolheu anteriormente e verifique se o usuário foi criado na troca do {{site.data.keyword.ieam}} com a função administrativa da organização:

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<email-address>"    hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   Na listagem do usuário, você deve ver: `"admin": true`

<div class="note"><span class="notetitle">Nota:</span> se você criar várias organizações e quiser que o mesmo administrador de organização gerencie todas elas, use o mesmo valor para `ORG_ADMIN_USER` todas as vezes que estiver nesta seção.</div>

O administrador da organização agora pode usar o console de gerenciamento do [{{site.data.keyword.ieam}}](../console/accessing_ui.md) para gerenciar recursos do {{site.data.keyword.ieam}} dentro desta organização.

### Permitindo que o administrador da organização use a CLI

Para que um administrador de organização use o comando `hzn exchange` para gerenciar recursos do {{site.data.keyword.ieam}} usando a CLI, ele deve:

1. Usar `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}} e criar uma chave de API:

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   Localize o valor da chave de API na linha de saída de comando que inicia com **Chave de API**. Salve o valor da chave em um local seguro para uso futuro porque não será possível consultá-lo por meio do sistema posteriormente. Além disso, configure-o nesta variável para os comandos subsequentes:

   ```bash
   ORG_ADMIN_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

   **Dica:** se você incluir esse usuário em contas adicionais do IAM no futuro, não será necessário criar uma chave de API para cada uma delas. A mesma chave de API funcionará em todas as contas do IAM das quais este usuário é um membro e, portanto, em todas as organizações do {{site.data.keyword.ieam}} das quais este usuário é um membro.

2. Verifique se a chave de API funciona com o comando `hzn exchange`:

   ```bash
   export HZN_ORG_ID=<organization id>    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY    hzn exchange user list
   ```
   {: codeblock}


A nova organização está pronta para uso. Para configurar um número máximo de nós de borda nesta organização ou customizar as configurações de pulsação do nó de borda padrão, consulte [Configuração da organização](#org-config).

## Usuários não administrativos dentro de uma organização
{: #org-users}

Um novo usuário pode ser incluído em uma organização importando e migrando o usuário do IAM (como um `MEMBER`) para a conta do IAM correspondente. Não é preciso incluir explicitamente o usuário na troca do {{site.data.keyword.ieam}}, pois isso ocorre automaticamente quando necessário.

Em seguida, o usuário pode usar o console de gerenciamento do [{{site.data.keyword.ieam}}](../console/accessing_ui.md). Para usar a CLI `hzn exchange`, o usuário deve:

1. Usar `cloudctl` para efetuar login no hub de gerenciamento do {{site.data.keyword.ieam}} e criar uma chave de API:

   ```bash
   IAM_USER=<iam user>    cloudctl login -a <cluster-url> -u $IAM_USER -p <hub-admin-password> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   Localize o valor da chave de API na linha de saída de comando que inicia com **Chave de API**. Salve o valor da chave em um local seguro para uso futuro porque não será possível consultá-lo por meio do sistema posteriormente. Além disso, configure-o nesta variável para os comandos subsequentes:

   ```bash
   IAM_USER_API_KEY=<IAM API key you just created>
   ```
   {: codeblock}

3. Configure essas variáveis de ambiente e verifique o usuário:

```bash
export HZN_ORG_ID=<organization-id> export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY hzn exchange user list
```
{: codeblock}

## A organização IBM
{: #ibm-org}

A organização IBM é uma organização exclusiva que fornece serviços e padrões predefinidos que se destinam a ser exemplos de tecnologia que são utilizáveis por qualquer usuário em qualquer organização. A organização IBM é criada automaticamente quando o hub de gerenciamento do {{site.data.keyword.ieam}} é instalado.

**Nota**: embora os recursos na organização IBM sejam públicos, ela não deve manter todo o conteúdo público no hub de gerenciamento do {{site.data.keyword.ieam}}.

## Configuração da Organização
{: #org-config}

Cada organização do {{site.data.keyword.ieam}} tem as configurações a seguir. Os valores padrão para essas configurações são frequentemente suficientes. Se você escolher customizar qualquer uma das configurações, execute o comando `hzn exchange org update -h` para ver as sinalizações de comando que podem ser usadas.

| **Configuração** | **Descrição** |
|--------------|-----------------|
| `description` | Uma descrição da organização. |
| `label` | O nome da organização. Este valor é usado para exibir o nome da organização no console de gerenciamento do {{site.data.keyword.ieam}}. |
| `heartbeatIntervals` | A frequência com que os agentes de nó de borda na organização pesquisam o hub de gerenciamento para obter instruções. Consulte a seção a seguir para obter detalhes. |
| `limits` | Limites para esta organização. Atualmente, o único limite é `maxNodes`, que é o número máximo de nós de borda permitido nessa organização. Há um limite prático para o número total de nós de borda que um único hub de gerenciamento do {{site.data.keyword.ieam}} pode suportar. Essa configuração possibilita que o usuário administrativo do hub limite o número de nós que cada organização pode ter, o que evita que uma organização use toda a capacidade. Um valor de `0` significa sem limite. |
{: caption="Tabela 3. Configurações da organização" caption-side="top"}

### Intervalo de pesquisa de pulsação do agente
{: #agent-hb}

O agente do {{site.data.keyword.ieam}} que é instalado em cada nó de borda periodicamente faz pulsações no hub de gerenciamento para permitir que ele saiba que ainda está em execução e conectado, bem como para receber instruções. É necessário mudar apenas essas configurações para os ambientes de escala extremamente alta.

O intervalo de pulsação é a quantia de tempo que o agente espera entre as pulsações para o hub de gerenciamento. O intervalo é ajustado automaticamente ao longo do tempo para otimizar a responsividade e reduzir a carga no hub de gerenciamento. O ajuste de intervalo é controlado por três configurações:

| **Configuração** | **Descrição**|
|-------------|----------------|
| `minInterval` | A quantia de tempo mais curta (em segundos) que o agente deve aguardar entre pulsações para o hub de gerenciamento. Quando um agente é registrado, ele começa a pesquisar neste intervalo. O intervalo nunca será menor do que este valor. Um valor de `0` significa usar o valor padrão. |
| `maxInterval` | A quantia de tempo mais longa (em segundos) que o agente deve aguardar entre pulsações para o hub de gerenciamento. Um valor de `0` significa usar o valor padrão. |
| `intervalAdjustment` | O número de segundos a incluir ao intervalo de pulsação atual quando o agente detecta que pode aumentar o intervalo. Após fazer a pulsação para o hub de gerenciamento com sucesso, mas não receber nenhuma instrução por algum tempo, o intervalo de pulsação será gradualmente aumentado até atingir o intervalo máximo de pulsação. Da mesma forma, quando as instruções são recebidas, o intervalo de pulsação é diminuído para garantir que as instruções subsequentes sejam processadas rapidamente. Um valor de `0` significa usar o valor padrão. |
{: caption="Tabela 4. Configurações de heartbeatIntervals" caption-side="top"}

As configurações de intervalo de pesquisa de pulsação na organização são aplicadas a nós que não configuraram explicitamente o intervalo de pulsação. Para verificar se um nó definiu explicitamente a configuração do intervalo de pulsação, use `hzn exchange node list <node id>`.

Para obter mais informações sobre como definir as configurações em ambientes de alta escala, consulte [Configuração de ajuste de escala](../hub/configuration.md#scale).
