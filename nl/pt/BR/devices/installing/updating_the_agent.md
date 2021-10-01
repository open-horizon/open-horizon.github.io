---

copyright:
years: 2020
lastupdated: "2020-2-2"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Atualizando o agente
{: #updating_the_agent}

Se você tiver recebido pacotes de agente do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) atualizados, será possível atualizar facilmente seu dispositivo de borda:

1. Execute as etapas em [Reúna as informações e os arquivos necessários para dispositivos de borda](../../hub/gather_files.md#prereq_horizon) para criar o arquivo **agentInstallFiles-&lt;edge-device-type&gt;.tar.gz** atualizado com os pacotes de agentes mais novos.
  
2. Para cada dispositivo de borda, execute as etapas em [Instalação e registro automatizados do agente](automated_install.md#method_one),
com a exceção de que, ao executar o comando **agent-install.sh**, deve-se especificar o serviço e o
padrão ou a política que você deseja executar no dispositivo de borda.
