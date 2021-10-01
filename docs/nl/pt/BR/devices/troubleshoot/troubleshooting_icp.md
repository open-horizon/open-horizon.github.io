---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Dicas de resolução de problemas específicos para o ambiente {{site.data.keyword.icp_notm}}
{: #troubleshooting_icp}

Revise este conteúdo para ajudá-lo a solucionar problemas comuns com
ambientes do {{site.data.keyword.icp_notm}} relacionados ao
{{site.data.keyword.edge_devices_notm}}. Essas dicas podem ajudá-lo a resolver problemas comuns e obter informações para identificar causas raiz.
{:shortdesc}

## Suas credenciais do {{site.data.keyword.edge_devices_notm}} estão configuradas corretamente
para uso no ambiente do {{site.data.keyword.icp_notm}}?
{: #setup_correct}

É necessária uma conta do usuário do {{site.data.keyword.icp_notm}} para concluir qualquer
ação dentro do {{site.data.keyword.edge_devices_notm}} neste ambiente. Também é necessária uma chave
de API criada a partir dessa conta.

Para verificar suas credenciais do {{site.data.keyword.edge_devices_notm}} neste ambiente,
execute este comando:

   ```
   hzn exchange user list
   ```
   {: codeblock}

Se uma entrada formatada por JSON for retornada a partir do Exchange mostrando um ou mais usuários, as
credenciais do {{site.data.keyword.edge_devices_notm}} estão configuradas corretamente.

Se uma resposta de erro for retornada, é possível executar as etapas para solucionar problemas de
configuração de credenciais.

Se a mensagem de erro indicar uma chave de API incorreta, é possível criar uma nova chave de API que use
os comandos a seguir.

Consulte [Reunir as informações e os arquivos necessários](../developing/software_defined_radio_ex_full.md#prereq-horizon).
