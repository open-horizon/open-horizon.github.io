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

# Eliminación de agente de clúster periférico
{: #remove_agent}

Para anular el registro de un clúster periférico y eliminar el agente de {{site.data.keyword.ieam}} de ese clúster, realice estos pasos:

1. Extraiga el script **agent-uninstall.sh** del archivo tar:

   ```bash
   tar -zxvf agentInstallFiles-x86_64-Cluster.tar.gz agent-uninstall.sh
   ```
   {: codeblock}

2. Exporte las credenciales de usuario de Horizon Exchange:

   ```bash
   export HZN_EXCHANGE_USER_AUTH=iamapikey:<clave-de-API>
   ```
   {: codeblock}

3. Elimine el agente:

   ```bash
   ./agent-uninstall.sh -u $HZN_EXCHANGE_USER_AUTH -d
   ```
   {: codeblock}

Nota: en ocasiones, la supresión del espacio de nombres se detiene en el estado "Terminando". En esta situación, consulte [Un espacio de nombres se ha atascado en el estado Terminando](https://www.ibm.com/support/knowledgecenter/SSBS6K_3.1.1/troubleshoot/ns_terminating.html) para suprimir el espacio de nombres de forma manual.
