---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Convenções usadas neste documento
{: #document_conventions}

Este documento usa convenções de conteúdo para transmitir significado específico.  

## Convenções de comando

Substitua o conteúdo variável que é mostrado em < > por valores específicos às suas necessidades. Não inclua caracteres <> no comando.

### Exemplo

  ```
  hzn key create "<companyname>" "<youremailaddress>"
  ```
  {: codeblock}
   
## Sequências de caracteres literais

O conteúdo que você vê no hub de gerenciamento ou no código é uma sequência de caracteres literal. Este conteúdo é mostrado como texto em **negrito**.
   
 ### Exemplo
   
 Se você examinar o código `service.sh`, verá que ele usa essas variáveis e outras variáveis de configuração para controlar seu comportamento. O **PUBLISH** controla se o código tenta enviar mensagens para o IBM Event Streams. O **MOCK** controla se o service.sh tenta entrar em contato com as APIs de REST e seus serviços dependentes (cpu e gps) ou se o `service.sh` cria dados falsos.
  
