---

copyright:
years: 2019
lastupdated: "2019-06-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Gerenciamento de software de borda
{: #edge_software_mgmt}

O {{site.data.keyword.edge_devices_notm}} baseia-se em processos independentes distribuídos geograficamente para gerenciar o ciclo de vida do software de todos os nós de borda.
{:shortdesc}

Os processos independentes que manipulam o gerenciamento de software do nó de borda usam os serviços {{site.data.keyword.horizon_exchange}} e {{site.data.keyword.horizon_switch}} para encontrarem-se na Internet, sem revelar seus endereços. Depois que eles se encontram, o processo usa o {{site.data.keyword.horizon_exchange}} e o {{site.data.keyword.horizon_switch}} para negociar os relacionamentos e, em seguida, colaborar para gerenciar o software do nó de borda. Para obter mais informações, consulte [Descoberta e negociação](discovery_negotiation.md).

O software do {{site.data.keyword.horizon}} em qualquer host pode agir como um agente do nó de borda e/ou como um agbot.

## Agbot (robô de contrato)

As instâncias do agbot são criadas de forma central para gerenciar cada padrão de implementação de software do {{site.data.keyword.edge_devices_notm}} que é publicado no {{site.data.keyword.horizon_exchange}}. Você ou um de seus desenvolvedores também pode executar os processos do agbot em qualquer máquina que possa acessar o {{site.data.keyword.horizon_exchange}} e o {{site.data.keyword.horizon_switch}}.

Quando um agbot é iniciado e configurado para gerenciar um padrão de implementação de software específico, o agbot é registrado com o {{site.data.keyword.horizon_exchange}} e começa a pesquisar os nós de borda que estão registrados para executar o mesmo padrão de implementação. Quando um nó de borda é descoberto, o agbot envia uma solicitação ao agente local nesse nó de borda para colaborar com o gerenciamento do software.

Quando um contrato é negociado, o agbot envia as seguintes informações para o agente:

* Os detalhes da política que estão contidos no padrão de implementação.
* A lista de serviços e versões do {{site.data.keyword.horizon}} que estão incluídos no padrão de implementação.
* As dependências entre esses serviços.
* A capacidade de compartilhamento dos serviços. Um serviço pode ser configurado como `exclusive`, `singleton` ou `multiple`.
* Detalhes sobre cada contêiner de cada serviço. Estes detalhes incluem as informações a seguir: 
  * O registro do Docker no qual o contêiner está registrado, como o registro público DockerHub ou um registro privado.
  * As credenciais de registro para registros privados.
  * Os detalhes do ambiente de shell para configuração e customização.
  * Os hashes assinados criptograficamente do contêiner e sua configuração.

O agbot continua a monitorar se há mudanças no padrão de implementação de software no {{site.data.keyword.horizon_exchange}}, como se novas versões de serviços do {{site.data.keyword.horizon}} são publicadas para o padrão. Em caso de detecção de mudanças, o agbot envia solicitações novamente para cada nó de borda registrado no padrão para colaborar no gerenciamento da transição para a nova versão do software.

O agbot também verifica periodicamente cada um dos nós de borda que estão registrados para o padrão de implementação para assegurar que todas políticas do padrão sejam cumpridas. Se uma política não estiver sendo cumprida, o agbot poderá interromper o contrato negociado. Por exemplo, se o nó de borda interromper o envio de dados ou o fornecimento de pulsações por uma duração estendida, o agbot poderá cancelar o contrato.  

### Agente do nó de borda

Um agente do nó de borda é criado quando o pacote de software do {{site.data.keyword.horizon}} é instalado em uma máquina de borda. Para obter mais informações sobre a
instalação do software, consulte [Instalando o software {{site.data.keyword.horizon}}](../installing/adding_devices.md).

Ao registrar o nó de borda posteriormente com o {{site.data.keyword.horizon_exchange}}, você deverá fornecer as seguintes informações:

* A URL do {{site.data.keyword.horizon_exchange}}.
* O nome e o token de acesso do nó de borda.
* O padrão de implementação de software que deve ser executado no nó de borda. É necessário fornecer o nome da organização e do padrão para identificar o padrão.

Para obter mais informações sobre o registro, consulte
[Registrando sua máquina de borda](../installing/registration.md).

Depois que o nó de borda é registrado, o agente local pesquisa o {{site.data.keyword.horizon_switch}} em busca de solicitações de colaboração a partir de processos do agbot remoto. Quando o agente é descoberto por um agbot com seu padrão de implementação configurado, o agbot envia uma solicitação ao agente do nó de borda para negociar a colaboração no gerenciamento de ciclo de vida do software para o nó de borda. Quando um contrato é realizado, o agbot envia informações para o nó de borda.

O agente puxa os contêineres do Docker especificados a partir dos registros apropriados. Em seguida, o agente verifica os hashes do contêiner e as assinaturas criptográficas. Em seguida, o agente inicia os contêineres na ordem de dependência reversa com as configurações de ambiente especificadas. Quando os contêineres estão em execução, o agente local monitora os contêineres. Se a execução de qualquer contêiner for interrompida inesperadamente, o agente reativará o contêiner para tentar manter o padrão de implementação intacto no nóde borda.

### Dependências de serviço do {{site.data.keyword.horizon}}

Embora o agente do {{site.data.keyword.horizon}} funcione para iniciar e gerenciar os contêineres no padrão de implementação designado, as dependências entre os serviços devem ser gerenciadas no código do contêiner de serviço. Mesmo que os contêineres sejam iniciados na ordem de dependência reversa, o {{site.data.keyword.horizon}} não pode assegurar que os provedores de serviços estejam totalmente iniciados e prontos para fornecer o serviço antes que os consumidores do serviço sejam iniciados. Os consumidores devem manipular de forma estratégica a possível lentidão do início dos serviços dos quais dependem. Como os contêineres que fornecem os serviços podem falhar e ser desativados, os consumidores do serviço também devem manipular a ausência dos serviços que consomem. 

O agente local detecta quando um serviço trava, iniciando-o com o mesmo nome de rede, na mesma rede privada do Docker. Ocorre um breve tempo de inatividade durante o processo de reativação. O serviço de consumo também deve manipular o breve tempo de inatividade, caso contrário, ele também poderá falhar.

O agente possui uma tolerância limitada para falhas. Se um contêiner estiver travando repetidamente e rapidamente, o agente poderá desistir de reiniciar os serviços que sempre falham e cancelar o contrato.

### Rede do Docker do {{site.data.keyword.horizon}}

O {{site.data.keyword.horizon}} usa os recursos de rede do Docker para isolar os contêineres do Docker que fornecem serviços. Esse isolamento assegura que apenas os consumidores autorizados possam acessar os contêineres. Cada contêiner é iniciado na ordem de  reversa, ou seja, os produtores primeiro e, em seguida, os consumidores, em uma rede virtual privada do Docker separada. Sempre que um contêiner de consumo de serviço é iniciado, ele é conectado à rede privada do seu contêiner de produtor. Os contêineres de produtor são acessíveis apenas pelos consumidores cujas dependências do produtor são conhecidas pelo {{site.data.keyword.horizon}}. Devido à forma como as redes do Docker são implementadas, todos os contêineres são acessíveis a partir de shells do host. 

Se for necessário obter o endereço IP de algum contêiner, será possível usar o comando `docker inspect <containerID>` para obter o `IPAddress` designado. É possível atingir qualquer contêiner a partir das shells do host.

## Segurança e Privacidade

Embora os agentes do nó de borda e os agbots do padrão de implementação possam descobrir uns aos outros, os componentes mantêm a privacidade completa até que um contrato de colaboração seja negociado formalmente. As identidades do agente e do agbot e todas as comunicações são criptografadas. As colaborações de gerenciamento de software também são criptografadas. Todos os softwares que estão sendo gerenciados são assinados criptograficamente. Para obter mais
informações sobre os aspectos de privacidade e segurança do
{{site.data.keyword.edge_devices_notm}}, consulte
[Segurança e privacidade](../user_management/security_privacy.md).
