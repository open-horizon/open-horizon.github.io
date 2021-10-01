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

# Descoberta e negociação
{: #discovery_negotiation}

O {{site.data.keyword.edge_devices_notm}}, que é
baseado no projeto {{site.data.keyword.horizon_open}}, é
basicamente descentralizado e distribuído. Os processos do agente
autônomo e do robô do contrato (agbot) colaboram no gerenciamento
de software de todos os nós de borda registrados.
{:shortdesc}

Para obter mais informações sobre o projeto
{{site.data.keyword.horizon_open}}, confira [{{site.data.keyword.horizon_open}}](https://github.com/open-horizon/).

Um processo do agente autônomo é executado em cada nó de borda
do Horizon para cumprir as políticas configuradas pelo
proprietário da máquina de borda.

Simultaneamente, os processos do agbot autônomo, que são
designados a cada padrão de implementação de software, usam as
políticas definidas para o padrão designado para buscar os
agentes do nó de borda que estão registrados para o padrão. Independentemente disso, esses agbots e agentes autônomos seguem as
políticas do proprietário da máquina de borda para negociar contratos
formais para a colaboração. Sempre que os agbots e agentes estão em
um contrato, eles cooperam para gerenciar os ciclos de vida de software
dos nós de borda correspondentes.

Os agbots e agentes usam os seguintes serviços centralizados
para localizarem-se, estabelecerem a confiança e comunicarem-se com
segurança no {{site.data.keyword.edge_devices_notm}}:

* O {{site.data.keyword.horizon_switch}}, que permite
comunicações ponto a ponto seguras e privadas entre os agbots e os
agentes.
* O {{site.data.keyword.horizon_exchange}}, que
facilita a descoberta.

<img src="../../images/edge/distributed.svg" width="90%" alt="Serviços
centralizados e descentralizados">

## {{site.data.keyword.horizon_exchange}}

O {{site.data.keyword.horizon_exchange}} permite
que os proprietários da máquina de borda registrem os nós de borda
para o gerenciamento de ciclo de vida do software. Ao registrar um nó
de borda com o {{site.data.keyword.horizon_exchange}} no {{site.data.keyword.edge_devices_notm}}, você especifica o
padrão de implementação para o nó de borda. Um padrão de
implementação é um conjunto de políticas para gerenciar o nó de
borda, um manifesto de software assinado criptograficamente e
quaisquer configurações associadas. O padrão de implementação deve
ser projetado, desenvolvido, testado, assinado e publicado no
{{site.data.keyword.horizon_exchange}}.

Cada nó de borda deve ser registrado com o
{{site.data.keyword.horizon_exchange}} sob a organização do
proprietário da máquina de borda. Cada nó de borda é registrado com
um ID e um token de segurança aplicáveis apenas a esse nó. Os nós
podem ser registrados para executar um padrão de implementação de
software fornecido pela própria organização ou um padrão
fornecido por outra organização, quando o padrão de implementação está
disponível publicamente.

Quando um padrão de implementação é publicado no
{{site.data.keyword.horizon_exchange}}, um ou mais agbots são
designados para gerenciar esse padrão de implementação e quaisquer
políticas associadas. Esses agbots buscam descobrir quaisquer nós de
borda que estejam registrados para o padrão de implementação. Quando
um nó de borda registrado é localizado, os agbots negociam com os
processos do agente local para o nó
de borda.

Embora o {{site.data.keyword.horizon_exchange}} permita
que os agbots localizem os nós de borda correspondentes a um padrão
de implementação registrado, o
{{site.data.keyword.horizon_exchange}} não está envolvido diretamente no processo de gerenciamento de software do nó de
borda. Os agbots e os agentes manipulam o processo de gerenciamento
de software. O {{site.data.keyword.horizon_exchange}} não tem
autoridade sobre o nó de borda e não inicia nenhum contato com
os agentes do nó de borda.

## {{site.data.keyword.horizon_switch}}

Os agbots pesquisam o {{site.data.keyword.horizon_exchange}} periodicamente para localizar todos
os nós de borda registrados para o padrão de implementação deles. Quando um agbot descobre um nó de borda registrado com seu
padrão de implementação, ele usa o
{{site.data.keyword.horizon}} switchboard para enviar uma
mensagem privada ao agente nesse nó. Essa mensagem é uma solicitação
para que o agente colabore no gerenciamento de ciclo de
vida do
software do nó de borda. Enquanto isso, o agente pesquisa sua caixa
de correio privada no {{site.data.keyword.horizon_switch}} em
busca de mensagens do agbot. Quando uma mensagem é recebida, o agente
decriptografa, valida e responde para aceitar a solicitação.

Além de pesquisar no
{{site.data.keyword.horizon_exchange}}, cada agbot também
pesquisa sua caixa de correio privada no
{{site.data.keyword.horizon_switch}}. Quando o agbot recebe uma aceitação de solicitação de
um agente, a negociação é concluída.

Os agentes e agbots compartilham as chaves públicas com o
{{site.data.keyword.horizon_switch}} para ativar a
comunicação segura e privada. Com essa criptografia, o
{{site.data.keyword.horizon_switch}} funciona apenas como um
gerenciador de caixa de correio. Todas as mensagens são
criptografadas pelo remetente antes de serem enviadas para o
{{site.data.keyword.horizon_switch}}. O {{site.data.keyword.horizon_switch}} é
incapaz de decriptografar as mensagens. No entanto, o
destinatário pode
decriptografar qualquer mensagem que seja criptografada com sua chave
pública. O destinatário também usa a chave pública do remetente para
criptografar as respostas do destinatário para o remetente.

**Observação:** Como toda a comunicação é
intermediada por meio do
{{site.data.keyword.horizon_switch}}, os endereços IP dos nós
de borda não são revelados a nenhum agbot até que o agente
em cada nó de borda escolha revelar essas informações. O agente
revela essas informações quando ele e o agbot negociam um contrato
com sucesso.

## Gerenciamento de ciclo de vida do software

Quando um nó de borda é registrado com o
{{site.data.keyword.horizon_exchange}} para um padrão de
implementação específico, um agbot desse padrão de implementação
pode passar a localizar o agente no nó de borda. O agbot do
padrão de implementação usa o
{{site.data.keyword.horizon_exchange}} para localizar o
agente e usa o {{site.data.keyword.horizon_switch}} para
negociar com o agente a colaboração no gerenciamento de software.

O agente do nó de borda recebe a solicitação para
colaboração do agbot e avalia a proposta para assegurar que ela
esteja em conformidade com as políticas definidas pelo
proprietário do nó de borda. O agente verifica as assinaturas
criptográficas usando os arquivos-chave instalados localmente. Se a
proposta for aceitável de acordo com as políticas locais e as
assinaturas forem verificadas, o agente aceitará a proposta e,
juntamente com o agbot, concluirá o contrato. 

Com o contrato em vigor, o agbot e o agente colaboram para
gerenciar o ciclo de vida do software do padrão de implementação no
nó de borda. O agbot fornece detalhes à medida que o padrão de
implementação evolui ao longo do tempo e monitora a conformidade do nó
de
borda. O agente faz o download do software localmente no nó de borda,
verifica a assinatura do software e, se ela for aprovada, executa e
monitora o software. Se necessário, o agente atualiza o software e
o interrompe quando apropriado.

Para obter mais informações sobre o processo de gerenciamento
de software, consulte
[Gerenciamento de software
de borda](edge_software_management.md).
