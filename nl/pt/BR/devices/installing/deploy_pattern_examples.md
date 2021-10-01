---

copyright:
years: 2019
lastupdated: "2019-07-04"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Exemplos de padrão de implementação
{: #deploy_pattern_ex}

Para ajudá-lo a saber mais sobre a introdução de padrões de implementação do {{site.data.keyword.edge_devices_notm}}, implementação, os programas de exemplo podem ser carregados como padrões de implementação.
{:shortdesc}

Tente registrar cada um desses padrões de implementação de exemplo pré-construídos para aprender mais sobre o uso dos padrões de implementação.

Para registrar um nó de borda para qualquer um dos exemplos de padrão de implementação a seguir, deve-se primeiro remover qualquer registro de padrão de implementação existente do nó da borda. Execute os comandos a seguir no nó da borda para remover qualquer registro de padrão de implementação:
```
 hzn unregister
 hzn node list | jq .configstate.state
```
{: codeblock}

Saída do exemplo:
```
"unconfigured"
```
{: codeblock}

Se a saída de comando exibir `"unconfiguring"` em vez de `"unconfigured"`, aguarde alguns minutos e execute o comando novamente. Geralmente o comando demora apenas alguns segundos para ser concluído. Tente o comando novamente até que a saída exiba `"unconfigured"`.

## Exemplos
{: #pattern_examples}

* [Hello, world ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/blob/master/edge/services/helloworld) Um exemplo mínimo de `"Hello, world."` para apresentar os padrões de implementação do {{site.data.keyword.edge_devices_notm}}.

* [Porcentagem de carregamento da CPU do host](cpu_load_example.md) Um padrão de implementação de exemplo que consome dados de porcentagem de carregamento da CPU e disponibiliza-os por meio do {{site.data.keyword.message_hub_notm}}.

* [Rádio definida por software](software_defined_radio_ex.md) Um exemplo completo que consome áudio de estação de rádio, extrai a fala e converte a fala extraída em texto. O exemplo conclui a análise de sentimentos no texto e disponibiliza os dados e os resultados por meio de uma interface com o usuário na qual é possível visualizar os detalhes dos dados de cada nó de borda. Use esse exemplo para saber mais sobre o processamento de borda.
