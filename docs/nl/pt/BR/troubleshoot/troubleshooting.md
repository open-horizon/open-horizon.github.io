---

copyright:
years: 2020
lastupdated: "2020-10-15"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Dicas de resolução de problemas e perguntas mais frequentes
{: #troubleshooting}

Revise as dicas de resolução de problemas e as perguntas mais frequentes para ajudá-lo a solucionar os problemas que você pode encontrar.
{:shortdesc}

* [Dicas de resolução de problemas](troubleshooting_devices.md)
* [Perguntas mais Frequentes](../getting_started/faq.md)

O conteúdo de resolução de problemas a seguir descreve os principais componentes do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) e como investigar as interfaces incluídas para determinar o estado do sistema.

## Ferramentas de Resolução de Problemas
{: #ts_tools}

Muitas interfaces que são incluídas com o {{site.data.keyword.ieam}} fornecem informações que podem ser usadas para diagnosticar problemas. Essas informações estão disponíveis por meio das APIs de REST da {{site.data.keyword.gui}} e HTTP e de uma ferramenta de shell do {{site.data.keyword.linux_notm}}, `hzn`.

Em um nó de borda, você pode precisar solucionar problemas de host, problemas de software do Horizon, problemas de Docker ou problemas em sua configuração ou o código em contêineres de serviço. Os problemas de host de nó de borda estão além do escopo deste documento. Se você precisar solucionar problemas do Docker, é possível usar muitos comandos e interfaces do Docker. Para obter mais informações, consulte a documentação do Docker.

Se os contêineres de serviço que você está executando usam o {{site.data.keyword.message_hub_notm}} (que é baseado no Kafka) para o sistema de mensagens, é possível se conectar manualmente aos fluxos do Kafka para o {{site.data.keyword.ieam}} para diagnosticar problemas. É possível assinar um tópico de mensagem para observar o que foi recebido pelo {{site.data.keyword.message_hub_notm}} ou é possível publicar em um tópico de mensagem para simular mensagens de outro dispositivo. O comando `kafkacat` {{site.data.keyword.linux_notm}} é uma forma de publicar ou assinar o {{site.data.keyword.message_hub_notm}}. Use a versão mais recente desta ferramenta. O {{site.data.keyword.message_hub_notm}} também fornece páginas da web gráficas que podem ser usadas para acessar algumas informações.

Em qualquer nó de borda em que o {{site.data.keyword.horizon}} esteja instalado, use o comando `hzn` para depurar problemas com o agente do {{site.data.keyword.horizon}} local e o {{site.data.keyword.horizon_exchange}} remoto. Internamente, o comando `hzn` interage com as APIs de REST HTTP fornecidas. O comando `hzn` simplifica o acesso e fornece uma melhor experiência do usuário do que as próprias APIs de REST. O comando `hzn` geralmente fornece um texto mais descritivo em sua saída e inclui um sistema de ajuda on-line integrado. Use o sistema de ajuda para obter informações e detalhes sobre quais comandos serão usados e detalhes sobre a sintaxe de comando e argumentos. Para visualizar essas informações de ajuda, execute os comandos  `hzn --help` ou `hzn <subcommand> --help`.

Em nós de borda em que os pacotes do {{site.data.keyword.horizon}} não são suportados ou instalados, é possível interagir diretamente com as APIs de REST HTTP subjacentes. Por exemplo, é possível usar o utilitário `curl` ou outros utilitários da CLI da API de REST. Também é possível escrever um programa em uma linguagem que suporte consultas REST.

Por exemplo, execute o utilitário `curl` para verificar o status do seu nó de borda:
```
curl localhost:8510/status
```
{: codeblock}

## Dicas de resolução de problemas
{: #ts_tips}

Para ajudar a solucionar problemas específicos, revise as perguntas sobre o estado do seu sistema e quaisquer dicas associadas sobre os tópicos a seguir. Para cada pergunta, é fornecida uma descrição de por que a pergunta é relevante para a resolução de problemas do sistema. Para algumas perguntas, dicas ou um guia detalhado é fornecido para aprender como obter as informações relacionadas para seu sistema.

Essas perguntas são baseadas na natureza de problemas de depuração e estão relacionadas a ambientes diferentes. Por exemplo, ao solucionar problemas em um nó de borda, você pode precisar de acesso completo e controle do nó, o que pode aumentar a sua capacidade de coletar e visualizar informações.

* [Dicas de resolução de problemas](troubleshooting_devices.md)

  Revise os problemas comuns que talvez você encontre ao usar o {{site.data.keyword.ieam}}.
  
## Riscos e resolução do {{site.data.keyword.ieam}}
{: #risks}

Embora o {{site.data.keyword.ieam}} crie oportunidades exclusivas, ele também apresenta desafios. Por exemplo, ele transcende os limites físicos do data center em nuvem, o que pode expor problemas de segurança, endereçabilidade, gerenciamento, propriedade e conformidade. E o mais importante, ele multiplica os problemas de ajuste de escala de técnicas de gerenciamento baseadas em nuvem.

As redes de borda aumentam o número de nós de computação por uma ordem de magnitude. Os gateways de borda aumentam isso em outra ordem de grandeza. Os dispositivos de borda aumentam esse número em 3 a 4 ordens de magnitude. Se os DevOps (entrega contínua e implementação contínua) são essenciais para o gerenciamento de uma infraestrutura de nuvem em hiperescala, então o zero-ops (operações sem intervenção humana) é crítico para o gerenciamento em grande escala que o {{site.data.keyword.ieam}} representa.

É fundamental implementar, atualizar, monitorar e recuperar o espaço de computação de borda sem intervenção humana. Todas essas atividades e processos devem:

* Ser totalmente automatizadas
* Ser capaz de tomar decisões independentes sobre a alocação de trabalho
* Ser capazes de reconhecer e recuperar-se das mudanças de condições sem a necessidade de intervenção.

Todas essas atividades devem ser seguras, rastreáveis e defensáveis.
