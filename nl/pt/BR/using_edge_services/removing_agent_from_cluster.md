---

copyright:
years: 2020
lastupdated: "2020-8-25"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Removendo o agente do cluster de borda
{: #remove_agent}

Para cancelar o registro de um cluster de borda e remover o agente {{site.data.keyword.ieam}} do cluster, execute estas etapas:

1. Extraia o script **agent-uninstall.sh** a partir do arquivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exporte suas credenciais de usuário do Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>
   ```
   {: codeblock}

3. Remova o agente:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Nota: ocasionalmente, a exclusão do namespace fica paralisada no estado "Terminating". Nessa situação, consulte [Um namespace está preso no estado Terminando](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para excluir manualmente o namespace.
