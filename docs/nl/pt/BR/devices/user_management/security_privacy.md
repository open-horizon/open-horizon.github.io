---

copyright:
years: 2019
lastupdated: "2019-06-24"
 
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

O {{site.data.keyword.edge_devices_notm}}, com base no
{{site.data.keyword.horizon}}, oferece o máximo de
segurança possível contra ataques e protege a privacidade do
participante. O {{site.data.keyword.edge_devices_notm}}
baseia-se nos processos autônomos e distribuídos geograficamente do
agente e do robô de contrato (agbot) para o gerenciamento de
software de
borda e para manter o anonimato.
{:shortdesc}

Para manter o anonimato, os processos do agente e do agbot
compartilham apenas suas chaves públicas em todo o processo de
descoberta e de negociação do
{{site.data.keyword.edge_devices_notm}}. Todas as partes dentro do
{{site.data.keyword.edge_devices_notm}} tratam cada outra
parte como uma entidade não confiável por padrão. As partes
compartilham informações e colaboram apenas quando a confiança é
estabelecida, as negociações entre as partes são concluídas e um
contrato formal é estabelecido.

## Plano de controle distribuído
{: #dc_pane}

Ao contrário das plataformas de Internet das Coisas (IoT)
centralizadas típicas e dos sistemas de controle baseados em nuvem, o plano de controle do
{{site.data.keyword.edge_devices_notm}} é bastante descentralizado. Cada função dentro do
sistema tem um escopo limitado de autoridade para que tenha apenas o nível mínimo de autoridade necessário para concluir as
tarefas associadas. Nenhuma autoridade única pode declarar o
controle sobre o sistema inteiro. Um usuário ou uma função não pode
obter acesso a todos os nós no sistema comprometendo um único host ou
componente de software.

O plano de controle é implementado por três entidades de software diferentes:
* Agentes do {{site.data.keyword.horizon}}
* Agbots do {{site.data.keyword.horizon}}
* {{site.data.keyword.horizon_exchange}}

Os agentes e agbots do {{site.data.keyword.horizon}} são
as entidades primárias e agem de forma autônoma para gerenciar os nós
de
borda. O {{site.data.keyword.horizon_exchange}} facilita a descoberta e a negociação, além de proteger as comunicações entre os agentes e agbots.

### Agentes
{: #agents}

Os agentes do {{site.data.keyword.horizon}} são mais numerosos do que todos os outros agentes no
{{site.data.keyword.edge_devices_notm}}. Um agente é executado em cada um dos nós de borda
gerenciados. Cada agente tem autoridade para gerenciar apenas aquele
único nó de borda. O agente anuncia sua chave pública no
{{site.data.keyword.horizon_exchange}} e negocia com
os processos remotos do agbot para gerenciar o software do nó local. O agente apenas espera receber comunicações dos agbots que são
responsáveis pelos padrões de implementação dentro da organização do
agente.

Um agente comprometido não tem nenhuma autoridade para afetar
nenhum outro nó de borda ou componente do sistema. Se o sistema
operacional do host ou o processo do agente em um nó de borda for
hackeado ou comprometido de outra forma, somente esse nó de
borda será comprometido. As outras partes do sistema
do {{site.data.keyword.edge_devices_notm}} não são afetadas.

Embora possa ser o componente mais poderoso de um nó de borda, o agente do nó de borda é o componente que apresenta menos risco de comprometimento da segurança do sistema geral do {{site.data.keyword.edge_devices_notm}}. O agente é responsável por fazer o download do
software em um nó de borda, verificar o software e, em seguida,
executar e vincular o software a outro software e hardware no nó
de borda. No entanto, dentro da segurança geral do sistema do
{{site.data.keyword.edge_devices_notm}}, o agente não tem
autoridade além do nó de borda no qual está em execução.

### Agbots
{: #agbots}

Os processos do agbot do {{site.data.keyword.horizon}} podem ser executados em qualquer lugar. Por padrão, os processos são executados automaticamente. As
instâncias do agbot são os segundos agentes mais comuns no
{{site.data.keyword.horizon}}. Cada agbot é responsável apenas pelos padrões de
implementação que são designados a esse agbot. Os padrões de
implementação consistem principalmente em políticas e em um manifesto
do serviço de software. Uma única instância do agbot pode gerenciar
vários padrões de implementação para uma organização.

Os padrões de implementação são publicados por desenvolvedores
no contexto de uma organização do usuário do
{{site.data.keyword.edge_devices_notm}}. Os padrões de implementação são fornecidos pelos agbots
aos agentes do {{site.data.keyword.horizon}}. Quando um nó de borda é registrado com
o {{site.data.keyword.horizon_exchange}}, um padrão de
implementação da organização é designado ao nó de borda. O agente
nesse nó de borda aceita ofertas somente de agbots que apresentam
esse padrão de implementação específico dessa organização específica. O agbot é um veículo de entrega de padrões de implementação, mas o
próprio padrão de implementação deve ser aceitável para as políticas
configuradas no nó de borda pelo proprietário do nó de
borda. O padrão de implementação deve ser aprovado na validação de
assinatura para que seja aceito pelo agente.

Um agbot comprometido pode tentar propor contratos maliciosos
com os nós de borda e tentar implementar um padrão de implementação
malicioso nos nós de borda. No entanto, os agentes do nó de borda
aceitam contratos apenas para os padrões de implementação que eles solicitaram por meio do registro e que são aceitáveis para as
políticas configuradas no nó de borda. O agente também usa sua chave
pública para validar a assinatura criptográfica do padrão antes de
aceitá-lo.

Mesmo que os processos do agbot orquestrem a instalação do
software e as
atualizações de manutenção, o agbot não tem autoridade para forçar
nenhum nó de borda ou agente a aceitar o software que ele está oferecendo. O agente em cada nó de borda individual decide qual software
deve ser aceito ou rejeitado. O agente toma essa decisão com base nas
chaves públicas que instalou e nas políticas que são configuradas
pelo proprietário do nó de borda quando o proprietário
registrou o nó de borda com o
{{site.data.keyword.horizon_exchange}}.

## {{site.data.keyword.horizon_exchange}}
{: #exchange}

O {{site.data.keyword.horizon_exchange}} é um serviço centralizado, mas geograficamente replicado e de carga balanceada, que permite que agentes distribuídos e agbots sigam e negociem contratos. Para obter mais informações, consulte [Visão geral do {{site.data.keyword.edge}}](../../getting_started/overview_ieam.md).

O {{site.data.keyword.horizon_exchange}} também
funciona como um banco de dados de metadados compartilhado para
usuários, organizações, nós de borda e todos os serviços, as
políticas e os padrões de implementação publicados.

Os desenvolvedores publicam metadados JSON sobre as implementações, as políticas e os padrões de implementação do serviço de software criados no {{site.data.keyword.horizon_exchange}}. Essas informações são transformadas em hash e
assinadas criptograficamente
pelo desenvolvedor. Os proprietários do nó de borda precisam instalar
as chaves públicas para o software durante o registro do nó de borda
para que o agente local possa usar as chaves para validar as
assinaturas.

Um {{site.data.keyword.horizon_exchange}} comprometido
pode oferecer maliciosamente informações falsas para os processos do
agente e do agbot, mas o impacto é mínimo devido aos
mecanismos de verificação integrados ao sistema. O
{{site.data.keyword.horizon_exchange}} não possui as
credenciais que são necessárias para assinar maliciosamente os
metadados. Um {{site.data.keyword.horizon_exchange}}
comprometido não pode realizar spoof maliciosamente em nenhum usuário
ou organização. O {{site.data.keyword.horizon_exchange}} atua como um armazém para os artefatos que são publicados por desenvolvedores e por proprietários de nós de borda e que serão usados para a ativação de agbots durante os processos de descoberta e de negociação.

O {{site.data.keyword.horizon_exchange}} também media e protege todas as comunicações entre os agentes e agbots. Ele implementa um mecanismo de caixa de correio, no qual os participantes podem deixar mensagens endereçadas a outros participantes. Para receber as mensagens, os participantes devem verificar o painel de comando do Horizon, para ver se há mensagens em suas caixas de correio.

Além disso, agentes e agbots compartilham suas chaves públicas com o {{site.data.keyword.horizon_exchange}}, para ativar as comunicações seguras e privadas. Quando qualquer participante precisa
comunicar-se com outro, esse remetente usa a chave pública do
destinatário-alvo para identificar o destinatário. O remetente usa
essa chave pública para criptografar uma mensagem para o
destinatário. Em seguida, o destinatário pode criptografar sua
resposta usando a chave pública do remetente.

Essa abordagem assegura que o Horizon Exchange seja incapaz de espionar o tráfego de rede das mensagens, porque não dispõe das chaves compartilhadas necessárias para decriptografar as mensagens. Somente os
destinatários-alvo podem decriptografar as mensagens. Um Horizon Exchange corrompido não tem visibilidade das comunicações de nenhum participante e é incapaz de inserir comunicações maliciosas em qualquer conversa entre participantess

## Ataque de negação de serviço 
{: #denial}

O {{site.data.keyword.horizon}} utiliza serviços centralizados. Em sistemas típicos de Internet das Coisas, os serviços centralizados geralmente são vulneráveis a ataques de negação de serviço. Para o {{site.data.keyword.edge_devices_notm}}, esses serviços centralizados são usados apenas para tarefas de descoberta, negociação e atualização. Os processos distribuídos e
autônomos do agente e do agbot usam os serviços centralizados
apenas quando devem concluir as tarefas de descoberta,
negociação e atualização. Caso contrário, quando os contratos forem
formados, o sistema poderá continuar a funcionar normalmente mesmo
quando esses serviços centralizados estiverem off-line. Esse
comportamento assegura que o
{{site.data.keyword.edge_devices_notm}} permaneça ativo se
houver ataques nos serviços centralizados.

## Criptografia assimétrica
{: #asym_crypt}

A maior parte da criptografia no
{{site.data.keyword.edge_devices_notm}} é baseada na
criptografia de chave assimétrica. Com essa forma de criptografia, o cliente e seus desenvolvedores devem gerar um par de chaves usando comandos `hzn key` e usar a chave privada para assinar criptograficamente qualquer software ou serviço que desejem publicar. Deve-se instalar a chave
pública nos nós de borda em que o software ou o serviço precisa
ser executado para que a assinatura criptográfica do software ou do
serviço possa ser verificada.

Os agentes e agbots assinam criptograficamente suas mensagens
entre si usando suas chaves privadas e usam a chave pública da
contraparte para verificar as mensagens que recebem. Os agentes e os
agbots também criptografam as mensagens com a chave pública da outra
parte para assegurar que apenas o destinatário-alvo possa
decriptografar a mensagem.

Se a chave privada e as credenciais de um agente, agbot ou
usuário estiverem comprometidas, somente os artefatos sob o controle
dessa entidade serão expostos. 

## Sumário
{: #summary}

Usando os hashes, as assinaturas criptográficas e a
criptografia, o {{site.data.keyword.edge_devices_notm}}
protege a maior parte da plataforma contra o acesso
indesejado. Por ser predominantemente descentralizado, o
{{site.data.keyword.edge_devices_notm}} evita a exposição à
maioria dos ataques que normalmente são encontrados nas plataformas
de Internet das Coisas mais tradicionais. Ao restringir o escopo da
autoridade e a influência das funções do participante, o
{{site.data.keyword.edge_devices_notm}} impede os possíveis
danos de um host comprometido ou do componente de software
comprometido para essa parte do sistema. Até mesmo os ataques externos
em grande escala nos serviços centralizados dos serviços do
{{site.data.keyword.horizon}} que são usados no
{{site.data.keyword.edge_devices_notm}} têm um impacto mínimo
nos participantes que já possuem um contrato. Os participantes que
estão sob um contrato ativo continuam a operar normalmente
durante qualquer interrupção.
