---

copyright:
years: 2021
lastupdated: "2021-02-20"
 
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Segurança e privacidade
{: #security_privacy}

O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}), com base em [Open Horizon](https://github.com/open-horizon), usa várias tecnologias de segurança diferentes para assegurar que é seguro contra ataques e protege a privacidade. O {{site.data.keyword.ieam}} depende de processos de agente autônomo geograficamente distribuídos para gerenciamento de software de ponta. Como resultado, o hub de gerenciamento do {{site.data.keyword.ieam}} e os agentes representam alvos potenciais para violações de segurança. Este documento explica como o {{site.data.keyword.ieam}} minimiza ou elimina as ameaças.
{:shortdesc}

## Hub de gerenciamento
O hub de gerenciamento do {{site.data.keyword.ieam}} é implementado em uma plataforma OpenShift Container; assim, ele herda todos os benefícios inerentes do mecanismo de segurança. Todo o tráfego de rede do hub de gerenciamento do {{site.data.keyword.ieam}} atravessa um ponto de entrada protegido por TLS. A comunicação de rede do hub de gerenciamento entre os componentes do hub de gerenciamento do {{site.data.keyword.ieam}} é realizada sem TLS.

## Plano de controle seguro
{: #dc_pane}

O hub de gerenciamento do {{site.data.keyword.ieam}} e os agentes distribuídos se comunicam no plano de controle para implementar cargas de trabalho e modelos em nós de borda. Em contraste com as plataformas centralizadas de Internet of Things (IoT) típicas e sistemas de controle baseados em nuvem, o plano de controle de {{site.data.keyword.ieam}} é principalmente descentralizado. Cada agente dentro do sistema tem um escopo limitado de autoridade, de modo que cada agente tem apenas o nível mínimo de autoridade necessário para completar suas tarefas. Nenhum agente pode exercer o controle de todo o sistema. Além disso, um único agente não pode obter acesso a todos os nós de borda no sistema, comprometendo qualquer nó de borda único, host ou componente de software.

O plano de controle é implementado por três entidades de software diferentes:
* Abra os agentes do {{site.data.keyword.horizon}}
* Abra os robôs de contrato do {{site.data.keyword.horizon}}
* Abra {{site.data.keyword.horizon_exchange}}

Os agentes e os robôs de contrato abertos do {{site.data.keyword.horizon}} são os agentes principais dentro do plano de controle. O {{site.data.keyword.horizon_exchange}} facilita a descoberta e comunicação segura entre os agentes e os robôs de contrato. Juntos, eles fornecem proteção no nível da mensagem usando um algoritmo chamado Perfect Forward Secrecy.

Por padrão, os agentes e robôs de contrato se comunicam com a central via TLS 1.3. Mas o próprio TLS não oferece segurança suficiente. O {{site.data.keyword.ieam}} criptografa cada mensagem de controle que flui entre agentes e robôs de contrato antes de ser enviada pela rede. Cada agente e robô de contrato gera um par de chaves RSA de 2048 bits e publica sua chave pública na troca. A chave privada é armazenada no armazenamento protegido por raiz de cada agente. Outros agentes no sistema usam a chave pública do receptor da mensagem para criptografar uma chave simétrica que é usada para criptografar mensagens do plano de controle. Isso garante que apenas o receptor pretendido possa descriptografar a chave simétrica; portanto, a própria mensagem. O uso do Perfect Forward Secrecy no plano de controle fornece segurança extra, como prevenção de ataques man-in-the-middle, que o TLS não impede.

### Agentes
{: #agents}

Os agentes do {{site.data.keyword.horizon_open}} são mais numerosos do que todos os outros agentes no {{site.data.keyword.ieam}}. Um agente é executado em cada um dos nós de borda gerenciados. Cada agente tem autoridade para gerenciar apenas esse nó de borda. Um agente comprometido não tem autoridade para afetar nenhum outro nó de borda ou qualquer outro componente do sistema. Cada nó possui credenciais exclusivas que são armazenadas em seu próprio armazenamento protegido por raiz. O {{site.data.keyword.horizon_exchange}} assegura que um nó só pode acessar seus próprios recursos. Quando um nó for registrado com o comando `hzn register`, será possível fornecer um token de autenticação. No entanto, é melhor prática permitir que o agente gere o seu próprio token para que nenhuma pessoa esteja ciente das credenciais de nó, o que reduz o potencial para comprometer o nó da borda.

O agente está protegido contra ataques à rede porque não possui portas de escuta na rede do host. Toda a comunicação entre o agente e o hub de gerenciamento é realizada pelo agente pesquisando o hub de gerenciamento. Além disso, os usuários são altamente encorajados a proteger os nós de borda com um firewall de rede que evita a intrusão no host do nó. Apesar dessas proteções, se o sistema operacional do host do agente ou o próprio processo do agente for hackeado ou comprometido de outra forma, apenas esse nó de borda será comprometido. As outras partes do sistema do {{site.data.keyword.ieam}} não são afetadas.

O agente é responsável por fazer download e iniciar cargas de trabalho conteinerizadas. Para assegurar que a imagem de contêiner transferida por download e a sua configuração não sejam comprometidas, o agente verifica a assinatura digital da imagem de contêiner e a assinatura digital de configuração de implementação. Quando um contêiner é armazenado em um registro de contêiner, o registro fornece uma assinatura digital para a imagem (por exemplo, um hash SHA256). O registro do contêiner gerencia as chaves usadas para criar a assinatura. Quando um serviço do {{site.data.keyword.ieam}} é publicado usando o comando `hzn exchange service publish`, ele obtém a assinatura de imagem e a armazena com o serviço publicado no {{site.data.keyword.horizon_exchange}}. A assinatura digital da imagem é passada ao agente por meio do plano de controle seguro, que permite ao agente verificar a assinatura da imagem do contêiner em relação à imagem transferida por download. Se a assinatura da imagem não corresponder à imagem, o agente não iniciará o contêiner. O processo é semelhante para a configuração do contêiner, com uma exceção. O comando `hzn exchange service publish` assina a configuração do contêiner e armazena a assinatura no {{site.data.keyword.horizon_exchange}}. Nesse caso, o usuário (publicando o serviço) deve fornecer o par de chaves RSA usado para criar a assinatura. Se o usuário ainda não tiver nenhuma chave, o comando `hzn key create` poderá ser usado a fim de gerá-las para este propósito. A chave pública é armazenada na troca com a assinatura da configuração do contêiner e transmitida ao agente sobre o plano de controle seguro. O agente pode então usar a chave pública para verificar a configuração do contêiner. Se você preferir usar um par de chaves diferente para cada configuração do contêiner, a chave privada usada para assinar esta configuração do contêiner poderá ser descartada agora, já que não é mais necessária. Consulte [Desenvolvendo serviços de borda](../developing/developing_edge_services.md) para obter mais detalhes sobre a publicação de uma carga de trabalho.

Quando um modelo é implementado em um nó de terminal, o agente baixa o modelo e verifica a assinatura do modelo para garantir que não foi adulterado em trânsito. A assinatura e a chave de verificação são criadas quando o modelo é publicado no hub de gerenciamento. O agente armazena o modelo em armazenamento protegido por raiz no host. Uma credencial é fornecida para cada serviço quando ele é iniciado pelo agente. O serviço usa essa credencial para se identificar e permitir o acesso aos modelos que o serviço tem permissão para acessar. Cada objeto de modelo no {{site.data.keyword.ieam}} indica a lista de serviços que podem acessar o modelo. Cada serviço obtém uma nova credencial cada vez que é reiniciado pelo {{site.data.keyword.ieam}}. O objeto modelo não é criptografado pelo {{site.data.keyword.ieam}}. Como o objeto modelo é tratado como um pacote de bit pelo {{site.data.keyword.ieam}}, uma implementação de serviço é gratuita para criptografar o modelo, se necessário. Para obter mais informações sobre como usar o MMS, consulte [Detalhes de gerenciamento de modelo](../developing/model_management_details.md).

### Robôs de contrato
{: #agbots}

O hub de gerenciamento do {{site.data.keyword.ieam}} contém várias instâncias de um robô de contrato, que são responsáveis por iniciar a implantação de cargas de trabalho para todos os nós de borda registrados no hub de gerenciamento. Os robôs de contrato examinam periodicamente todas as políticas e padrões de implementação que foram publicados no Exchange, assegurando que os serviços nesses padrões e políticas sejam implementados em todos os nós de bordas corretos. Quando um robô de contrato inicia uma solicitação de implementação, ele envia a solicitação pelo plano de controle seguro. A solicitação de implementação contém tudo que o agente precisa para verificar a carga de trabalho e sua configuração, caso o agente decida aceitar a solicitação. Consulte [Agentes](security_privacy.md#agents) para obter detalhes de segurança sobre o que o agente faz. O robô de contrato também direciona o MMS para onde e quando implementar os modelos. Consulte [Agentes](security_privacy.md#agents) para obter detalhes de segurança sobre como os modelos são gerenciados.

Um robô de contrato comprometido pode tentar propor implementações de carga de trabalho maliciosas, mas a implementação proposta deve atender aos requisitos de segurança que são declarados na seção do agente. Mesmo que o robô de contrato inicie a implementação da carga de trabalho, ele não tem autoridade para criar cargas de trabalho e configurações de contêiner e, portanto, não pode propor suas próprias cargas de trabalho maliciosas.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

O {{site.data.keyword.horizon_exchange}} é um servidor de API de REST centralizado, replicado e com balanceamento de carga. Ele funciona como um banco de dados compartilhado de metadados para usuários, organizações, nós de borda, serviços publicados, políticas e padrões. Ele também permite que os agentes distribuídos e robôs de contrato implementem cargas de trabalho conteinerizadas, fornecendo o armazenamento para o plano de controle seguro, até que as mensagens possam ser recuperadas. O {{site.data.keyword.horizon_exchange}} não consegue ler as mensagens de controle porque não possui a chave RSA privada para descriptografar a mensagem. Assim, um {{site.data.keyword.horizon_exchange}} comprometido é incapaz de espionar o tráfego do plano de controle. Para obter mais informações sobre a função do Exchange, consulte [Visão geral do {{site.data.keyword.edge}}](../getting_started/overview_ieam.md).

## Serviços de modo privilegiado
{: #priv_services}
Em uma máquina host, algumas tarefas só podem ser executadas por uma conta com acesso raiz. O equivalente para contêineres é o modo privilegiado. Enquanto os contêineres geralmente não precisam de modo privilegiado no host, há alguns casos de uso em que ele é necessário. No {{site.data.keyword.ieam}}, você tem a capacidade de especificar que um serviço de aplicativos deve ser implementado com a execução de processo privilegiado ativada. Por padrão, ele está desativado. Deve-se ativá-lo explicitamente na [configuração de implementação](https://open-horizon.github.io/anax/deployment_string.html) do respectivo arquivo de Definição de serviço para cada serviço que precisa executar neste modo. E mais adiante, qualquer nó sobre o qual você deseja implentar esse serviço deve também permitir explicitamente contêineres de modo privilegiado. Isso garante que os proprietários de nós tenham algum controle sobre quais serviços estão executando em seus nós de borda. Para um exemplo de como ativar a política de modo privilegiado em um nó de borda, consulte [política de nós privilegiados](https://github.com/open-horizon/anax/blob/master/cli/samples/privileged_node_policy.json). Se a definição de serviço ou uma de suas dependências requer o modo privilegiado, a política do nó também deve permitir o modo privilegiado ou então nenhum dos serviços não será implementado ao nó. Para uma discussão aprofundada sobre o modo privilegiado, veja [O que é o modo privilegiado e eu preciso dele?](https://wiki.lfedge.org/pages/viewpage.action?pageId=44171856).

## Ataque de negação de serviço 
{: #denial}

O hub de gerenciamento do {{site.data.keyword.ieam}} é um serviço centralizado. Os serviços centralizados em ambientes baseados em nuvem típicos são geralmente vulneráveis a ataques de negação de serviço. O agente requer uma conexão apenas quando é registrado pela primeira vez no hub ou quando está negociando a implementação de uma carga de trabalho. Em todos os outros momentos, o agente continua a operar normalmente, mesmo quando desconectado do hub de gerenciamento do {{site.data.keyword.ieam}}.  Isso assegura que o agente do {{site.data.keyword.ieam}} permaneça ativo no nó de borda mesmo quando o hub de gerenciamento está sob ataque.

## Model Management System
{: #malware}

O {{site.data.keyword.ieam}} não executa uma varredura de vírus ou malware nos dados que são transferidos por upload para o MMS. Assegure-se de que quaisquer dados transferidos por upload tenham sido varridos antes de seu upload para o MMS.

## Dados em REST
{: #drest}

O {{site.data.keyword.ieam}} não criptografa dados em repouso. A criptografia de dados em repouso deve ser implementada com um utilitário apropriado para o sistema operacional do host no qual o hub ou agente de gerenciamento do {{site.data.keyword.ieam}} está em execução.

## Padrões de Segurança
{: #standards}

Os padrões de segurança a seguir são usados no {{site.data.keyword.ieam}}:
* O TLS 1.2 (HTTPS) é usado para criptografar dados em trânsito de e para o hub de gerenciamento.
* A criptografia AES de 256 bits é usada para dados em trânsito, especificamente as mensagens que fluem sobre o plano de controle seguro.
* Os pares de chaves RSA de 2048 bits são usados para dados em trânsito, especificamente a chave simétrica AES 256 que flui sobre o plano de controle seguro.
* Chaves RSA fornecidas por um usuário para assinar configurações de implantação de contêiner ao usar o comando **hzn exchange service publish**.
* Par de chaves RSA conforme gerado pelo comando **hzn key create**, se o usuário optar por usar este comando. O tamanho de bit desta chave é 4096 por padrão, mas pode ser mudado pelo usuário.

## Resumo
{: #summary}

O {{site.data.keyword.edge_notm}} usa hashes, assinaturas criptográficas e criptografia para garantir a segurança contra acesso indesejado. Por ser basicamente descentralizado, o {{site.data.keyword.ieam}} evita a exposição à maioria dos ataques que são normalmente encontrados em ambientes de computação de borda. Ao restringir o escopo de autoridade das funções dos participantes, o {{site.data.keyword.ieam}} contém o dano potencial de um host comprometido ou componente de software comprometido a essa parte do sistema. Mesmo ataques externos em grande escala nos serviços centralizados dos serviços do {{site.data.keyword.horizon}} que são usados no {{site.data.keyword.ieam}} têm impacto mínimo na execução de cargas de trabalho na borda.
