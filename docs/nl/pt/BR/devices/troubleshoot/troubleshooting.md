---

copyright:
years: 2019
lastupdated: "2019-06-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Resolução de problemas
{: #troubleshooting}

Revise as dicas de resolução de problemas e os problemas comuns que podem ocorrer com o {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para ajudar a resolver quaisquer problemas encontrados.
{:shortdesc}

O Guia de Resolução de Problemas a seguir descreve os principais componentes de um sistema do {{site.data.keyword.ieam}} e como investigar as interfaces incluídas para determinar o estado do sistema.

## Ferramentas de Resolução de Problemas
{: #ts_tools}

Muitas interfaces que são incluídas com o {{site.data.keyword.ieam}} fornecem informações que podem ser usadas para diagnosticar problemas. Essas informações estão disponíveis por meio das APIs de REST da {{site.data.keyword.gui}} e HTTP e de uma ferramenta de shell do {{site.data.keyword.linux_notm}}, `hzn`.

Em uma máquina de borda, pode ser necessário solucionar problemas do host, problemas do software Horizon, problemas do Docker ou problemas em sua configuração ou no código em contêineres de serviço. Os problemas do host da máquina de borda estão além do escopo deste documento. Se você precisar solucionar problemas do Docker, há muitos comandos e interfaces do Docker que podem ser usados. Para obter mais informações, consulte a documentação do Docker.

Se os contêineres de serviço que você está executando usam o {{site.data.keyword.message_hub_notm}} (que é baseado no Kafka) para o sistema de mensagens, é possível se conectar manualmente aos fluxos do Kafka para o {{site.data.keyword.ieam}} para diagnosticar problemas. É possível assinar um tópico de mensagem para observar o que foi recebido pelo {{site.data.keyword.message_hub_notm}} ou é possível publicar em um tópico de mensagem para simular mensagens de outro dispositivo. O comando `kafkacat` {{site.data.keyword.linux_notm}} é uma maneira fácil de publicar ou assinar o {{site.data.keyword.message_hub_notm}}. Use a versão mais recente desta ferramenta. O {{site.data.keyword.message_hub_notm}} também fornece páginas da web gráficas que podem ser usadas para acessar algumas informações.

Em qualquer máquina na qual o {{site.data.keyword.horizon}} está instalado, use o comando `hzn` para depurar problemas com o agente {{site.data.keyword.horizon}} local e com o {{site.data.keyword.horizon_exchange}} remoto. Internamente, o comando `hzn` interage com as APIs de REST HTTP fornecidas. O comando `hzn` simplifica o acesso e fornece uma melhor experiência do usuário do que as próprias APIs de REST. O comando `hzn` geralmente fornece um texto mais descritivo em sua saída e inclui um sistema de ajuda on-line integrado. Use o sistema de ajuda para obter informações e detalhes sobre quais comandos serão usados e detalhes sobre a sintaxe de comando e argumentos. Para visualizar essas informações de ajuda, execute os comandos `hzn --help` ou `hzn \<subcommand\> --help`.

Em nós em que os pacotes do {{site.data.keyword.horizon}} não são suportados ou não estão instalados, é possível interagir diretamente com as APIs de REST HTTP subjacentes. Por exemplo, é possível usar o utilitário `curl` ou outros utilitários da CLI da API de REST. Também é possível escrever um programa em uma linguagem que suporte consultas REST. 

## Dicas de resolução de problemas
{: #ts_tips}

Para ajudar a solucionar problemas específicos, revise as perguntas sobre o estado do seu sistema e quaisquer dicas associadas sobre os tópicos a seguir. Para cada pergunta, é fornecida uma descrição do motivo pelo qual a pergunta é relevante para a resolução de problemas do seu sistema. Para algumas perguntas, dicas ou um guia detalhado é fornecido para aprender como obter as informações relacionadas para seu sistema.

Essas perguntas são baseadas na natureza de problemas de depuração e estão relacionadas a ambientes diferentes. Por exemplo, ao solucionar problemas em um nó de borda, pode ser necessário concluir o acesso ao nó e controlá-lo, o que pode aumentar sua capacidade para coletar e visualizar informações.

* [Dicas de resolução de problemas](troubleshooting_devices.md)

  Revise os problemas comuns que talvez você encontre ao usar o {{site.data.keyword.ieam}}.
