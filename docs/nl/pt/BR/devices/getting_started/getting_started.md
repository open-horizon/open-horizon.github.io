---

copyright:
years: 2019
lastupdated: "2019-08-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Informações Iniciais
{: #getting_started}

Revise os tópicos a seguir, que o ajudarão a começar a usar o {{site.data.keyword.edge_devices_notm}}, incluindo informações sobre como gerenciar o software e os serviços de borda.
{:shortdesc}

Para obter mais informações sobre como instalar o software necessário para os dispositivos {{site.data.keyword.edge_devices_notm}}, consulte os tópicos a seguir:

* [Preparando um dispositivo de borda](../installing/adding_devices.md)
* [Instale o {{site.data.keyword.horizon_agent}} em seu dispositivo de borda e registre-o com o exemplo de Hello World](../installing/registration.md)
* [Exemplos de serviço de borda adicionais](../installing/additional_examples.md)
  * [Exemplo de porcentagem de carregamento da CPU host (cpu2evtstreams)](../installing/cpu_load_example.md)
  * [Hello world](policy.md)
  * [Processamento de borda de rádio definido por software](../installing/software_defined_radio_ex.md)
  * [Assistente de voz off-line (processtext)](../installing/offline_voice_assistant.md)
  * [Conversão de voz para texto do Watson](../installing/watson_speech.md)
* [Explorando o comando hzn](../installing/exploring_hzn.md)

## Visão geral de como o {{site.data.keyword.edge_devices_notm}} funciona
{: #overview}

O {{site.data.keyword.edge_devices_notm}} é projetado especificamente para o gerenciamento de nó de borda visando minimizar os riscos de implementação e gerenciar o ciclo de vida do software de serviço em nós de borda de forma totalmente autônoma.
{:shortdesc}

## Arquitetura do {{site.data.keyword.edge_devices_notm}}
{: #iec4d_arch}

Outras soluções de computação de borda geralmente se concentram em uma das seguintes estratégias de arquitetura:

* Uma autoridade centralizada poderosa para fazer com que a conformidade de software do nó de borda seja cumprida.
* A transmissão da responsabilidade sobre a conformidade de software aos proprietários do nó de borda, que devem monitorar as atualizações de software e fazer manualmente com que a conformidade seja cumprida em seus próprios nós de borda.

A primeira solução concentra a autoridade de forma centralizada, criando um ponto único de falha e um destino que os invasores podem explorar para controlar a frota inteira de nós de borda. A segunda solução pode resultar em uma grande porcentagem de nós de borda sem as atualizações de software mais recentes instaladas. Se os nós de borda não estiverem todos na versão mais recente ou tiverem todas as correções disponíveis, eles poderão ficar vulneráveis a invasores. Ambas as abordagens também dependem, tipicamente, da autoridade central como base para o estabelecimento de confiança.

<p align="center">
<img src="../../images/edge/overview_illustration.svg" width="70%" alt="Ilustração do alcance global da computação de borda.">
</p>

Ao contrário dessas abordagens de solução, o {{site.data.keyword.edge_devices_notm}} é descentralizado. O {{site.data.keyword.edge_devices_notm}} gerencia a conformidade do software de serviço automaticamente nos nós de borda sem nenhuma intervenção manual. Em cada nó de borda, os processos do agente decentralizados e totalmente autônomos são executados controlados pelas políticas especificadas durante o registro da máquina no {{site.data.keyword.edge_devices_notm}}. Os processos descentralizados e totalmente autônomos do agbot (robô de contrato), geralmente são executados em um local central, mas podem ser executados em qualquer lugar, incluindo em nós de borda. Assim como os processos do agente, os agbots são governados por políticas. Os agentes e os agbots manipulam a maior parte do gerenciamento de ciclo de vida do software de serviço
de borda para os nós de borda e fazem com que a conformidade de software seja cumprida nos nós de borda.

Para aumentar a eficiência, o {{site.data.keyword.edge_devices_notm}} inclui dois serviços centralizados, o exchange e o switchboard. Esses serviços não têm autoridade central sobre os processos autônomos do agente e do agbot. Nesse caso, esses serviços fornecem serviços simples de descoberta e de compartilhamento de metadados (o exchange) e um serviço de caixa de correio privada para suportar as comunicações de ponto a ponto (o switchboard). Esses serviços suportam o trabalho totalmente autônomo dos agentes e agbots.

Por último, o console do {{site.data.keyword.edge_devices_notm}} ajuda os administradores a configurar a política e monitorar o status dos nós de borda.

Cada um dos cinco tipos de componentes do {{site.data.keyword.edge_devices_notm}} (agentes, agbots, exchange, switchboard e console) tem uma área restrita de responsabilidade. Cada componente não possui autoridade nem credenciais para agir fora de sua respectiva área de responsabilidade. Ao dividir a responsabilidade e definir o escopo de autoridade e de credenciais, o {{site.data.keyword.edge_devices_notm}} oferece gerenciamento de risco para a implementação de nó de borda.

## Descoberta e negociação
{: #discovery_negotiation}

O {{site.data.keyword.edge_devices_notm}}, que é baseado no projeto [1{{site.data.keyword.horizon_open}} ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/), é principalmente descentralizado e distribuído. Os processos do agente
autônomo e do robô do contrato (agbot) colaboram no gerenciamento
de software de todos os nós de borda registrados.

Um processo do agente autônomo é executado em cada nó de borda do Horizon para cumprir as políticas configuradas pelo proprietário do dispositivo de borda.

Os agbots autônomos monitoram os padrões e políticas de implementação no Exchange e buscam os agentes do nó de borda que ainda não estão em conformidade. Os Agbots propõem contratos aos nós de borda para que fiquem em conformidade. Quando um agbot e o agente chegam a um acordo, eles cooperam para gerenciar o ciclo de vida do software de serviços de borda no nó de borda.

Os agbots e agentes usam os seguintes serviços centralizados
para localizarem-se, estabelecerem a confiança e comunicarem-se com
segurança no {{site.data.keyword.edge_devices_notm}}:

* O {{site.data.keyword.horizon_exchange}}, que
facilita a descoberta.
* O {{site.data.keyword.horizon_switch}}, que permite
comunicações ponto a ponto seguras e privadas entre os agbots e os
agentes.

<img src="../../images/edge/distributed.svg" width="90%" alt="Serviços centralizados e descentralizados">

### {{site.data.keyword.horizon_exchange}}
{: #iec4d_exchange}

O {{site.data.keyword.horizon_exchange}} permite que os proprietários do dispositivo de borda registrem os nós de borda para o gerenciamento de ciclo de vida do software. Ao registrar um nó de borda com o {{site.data.keyword.horizon_exchange}} no {{site.data.keyword.edge_devices_notm}}, você especifica o padrão ou política de implementação para o nó de borda. (Em seu núcleo, um padrão de implementação é simplesmente um conjunto predefinido e nomeado de políticas para gerenciar os nós de borda.) Os padrões e as políticas devem ser projetados, desenvolvidos, testados, assinados e publicados no {{site.data.keyword.horizon_exchange}}.

Cada nó de borda é registrado com um ID exclusivo e token de segurança. Os nós podem ser registrados para usar um padrão ou políticas fornecidos por sua própria organização, ou um padrão que é fornecido por outra organização.

Quando um padrão ou política é publicado no {{site.data.keyword.horizon_exchange}}, os agbots procuram descobrir quaisquer nós de borda que sejam afetados pelo padrão ou política novos ou atualizados. Quando um nó de borda registrado é localizado, um agbot negocia com o agente do nó de borda.

Embora o {{site.data.keyword.horizon_exchange}} permita que os agbots localizem os nós de borda que estão registrados para usar padrões ou políticas, o {{site.data.keyword.horizon_exchange}} não está diretamente envolvido no processo de gerenciamento do software do nó de borda. Os agbots e os agentes manipulam o processo de gerenciamento
de software. O {{site.data.keyword.horizon_exchange}} não tem autoridade sobre o nó de borda e não inicia nenhum contato com os agentes do nó de borda.

### {{site.data.keyword.horizon_switch}}
{: #horizon_switch}

Quando um agbot descobre um nó de borda que é afetado por um padrão ou política novos ou atualizados, o agbot usa o {{site.data.keyword.horizon}} switchboard para enviar uma mensagem privada ao agente nesse nó. Essa mensagem é uma proposta de contrato para colaborar no gerenciamento de ciclo de vida do software do nó de borda. Quando o agente recebe a mensagem do agbot em sua caixa postal privada no {{site.data.keyword.horizon_switch}}, ela decriptografa e avalia a proposta. Se estiver dentro de sua própria política de nó, o nó enviará uma mensagem de aceitação para o agbot. Caso contrário, o nó rejeitará a proposta. Quando o agbot recebe uma aceitação de contrato em sua caixa postal privada no {{site.data.keyword.horizon_switch}}, a negociação é concluída.

Os agentes e agbots postam chaves públicas no {{site.data.keyword.horizon_switch}} para permitir uma comunicação segura e privada que usam o Perfect Forward Secrecy. Com essa criptografia, o
{{site.data.keyword.horizon_switch}} funciona apenas como um
gerenciador de caixa de correio. Ele é incapaz de decriptografar as mensagens.

Nota: como toda a comunicação é intermediada pelo {{site.data.keyword.horizon_switch}}, os endereços IP dos nós de borda não são revelados a nenhum agbot até que o agente em cada nó de borda opte por revelar essas informações. O agente
revela essas informações quando ele e o agbot negociam um contrato
com sucesso.

## Gerenciamento de ciclo de vida do software de borda
{: #edge_lifecycle}

Depois que o agbot e o agente chegam a um acordo para um determinado padrão ou conjunto de políticas, eles colaboram para gerenciar o ciclo de vida do software do padrão ou da política no nó de borda. O agbot monitora o padrão ou a política à medida que evolui ao longo do tempo, e monitora o nó de borda quanto à conformidade. O agente faz download do software localmente no nó de borda, verifica a assinatura do software e, se verificada, executa e monitora o software. Se necessário, o agente atualiza o software e
o interrompe quando apropriado.

O agente obtém as imagens do contêiner do Docker de serviço de borda especificado a partir dos registros apropriados e verifica as assinaturas de imagem do contêiner. Em seguida, o agente inicia os contêineres em ordem de dependência reversa com a configuração que está especificada no padrão ou na política. Quando os contêineres estão em execução, o agente local monitora os contêineres. Se a execução de qualquer contêiner for interrompida inesperadamente, o agente reativará o contêiner para tentar manter o padrão ou a política em conformidade no nó de borda.

O agente possui uma tolerância limitada para falhas. Se um contêiner estiver repetidamente e rapidamente travando, o agente parará de tentar reiniciar os serviços com falha definitivamente e cancelará o contrato.

### Dependências de serviço do {{site.data.keyword.horizon}}
{: #service_dependencies}

Um serviço de borda pode especificar em suas dependências de metadados em outros serviços de borda que ele usa. Quando um serviço de borda é implementado em um nó de borda como resultado de um padrão ou política, o agente também implementará todos os serviços de borda que ele requerer (na ordem de dependência inversa). Qualquer número de níveis de dependências de serviço é suportado.

### Rede do Docker do {{site.data.keyword.horizon}}
{: #docker_networking}

O {{site.data.keyword.horizon}} usa recursos de rede do Docker para isolar contêineres do Docker, de modo que somente os serviços que os requerem possam se conectar a eles. Ao iniciar um contêiner de serviço que depende de outro serviço, o contêiner de serviço será conectado à rede privada do contêiner de serviço dependente. Isso facilita a execução de serviços de borda criados por diferentes organizações porque cada serviço de borda pode acessar outros serviços que são listados apenas em seus metadados.
