---

copyright:
years: 2020
lastupdated: "2020-02-03"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalando o agente
{: #registration}

Ao instalar o software do agente {{site.data.keyword.horizon}} em um dispositivo de borda, é possível registrar seu dispositivo de borda no {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) para incluir o dispositivo no domínio de gerenciamento de computação de borda e executar serviços de borda. As instruções a seguir registram o seu novo dispositivo de borda com o serviço de borda de exemplo de helloworld mínimo para confirmar que o dispositivo de borda está funcionando corretamente. O serviço de borda Hello World pode ser facilmente interrompido quando você estiver pronto para executar os seus próprios serviços de borda no dispositivo de borda.
{:shortdesc}

## Antes de Começar
{: #before_begin}

Você deve executar as etapas em [Preparando um dispositivo de borda](adding_devices.md).

## Instalando e registrando dispositivos de borda
{: #installing_registering}

São fornecidos quatro métodos diferentes para instalar o agente e registrar dispositivos de borda e cada um desses métodos é útil para uma circunstância diferente:

* [Instalação e registro automatizados do agente](automated_install.md) - instale e registre um serviço de borda, usando um número mínimo de etapas. **Os usuários de primeira viagem devem usar este método.**
* [Instalação e registro manuais avançados do agente](advanced_man_install.md) - execute você mesmo cada uma das etapas para instalar e registrar um dispositivo de borda. Use este método caso precise executar algo fora do comum e o script que é usado no Método 1 não fornece a flexibilidade necessária. Também é possível usar este método caso queira entender exatamente o que é necessário para configurar um dispositivo de borda.
* [Instalação e registro do agente em massa](many_install.md#batch-install) - instale e registre muitos dispositivos de borda de uma vez.
* [Instalação e registro do agente SDO](sdo.md) - instalação automática com dispositivos SDO

## Perguntas e resolução de problemas
{: #questions_ts}

Em caso de dificuldades com qualquer uma dessas etapas, revise os tópicos sobre resolução de problemas e de perguntas mais frequentes fornecidos. Para obter informações adicionais, consulte
  * [Resolução de problemas](../troubleshoot/troubleshooting.md)
  * [Perguntas mais Frequentes](../getting_started/faq.md)
