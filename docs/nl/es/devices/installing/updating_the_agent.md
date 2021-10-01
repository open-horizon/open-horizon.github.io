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

# Actualización del agente
{: #updating_the_agent}

Si ha recibido paquetes de agente de
{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) actualizados,
puede actualizar fácilmente el dispositivo periférico:

1. Siga los pasos indicados en [Recopilar la información y los archivos necesarios para dispositivos periféricos](../../hub/gather_files.md#prereq_horizon) para crear el archivo **agentInstallFiles-&lt;tipo-de-dispositivo-periférico&gt;.tar.gz** actualizado con los paquetes de agente más recientes.
  
2. Para cada dispositivo periférico, realice los pasos de
[Instalación y registro automatizados de agente](automated_install.md#method_one), excepto cuando
ejecute el mandato **agent-install.sh**, donde debe especificar el servicio y el patrón o la política
que desea ejecutar en el dispositivo periférico.
