---

copyright:
years: 2019, 2020
lastupdated: "2020-01-22"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Implementando serviços de borda
{: #detailed_deployment_policy}

É possível implementar políticas do {{site.data.keyword.edge_notm}} {{site.data.keyword.ieam}} usando políticas ou padrões. Para obter uma visão geral mais abrangente de vários componentes do sistema, consulte [Visão geral do{{site.data.keyword.edge}}](../../getting_started/overview_ieam.md) e [Casos de uso da Política de implementação](policy_user_cases.md). Para obter um exemplo prático de política, consulte [Processo de CI-CD para serviços de borda](../developing/cicd_process.md).

Nota: também é possível criar políticas ou padrões de implementação a partir do console de gerenciamento. Consulte [Usando o console de gerenciamento](../getting_started/accessing_ui.md).

Esta seção discute os conceitos de política e de padrões e inclui um cenário de caso de uso.

Um administrador não consegue gerenciar milhares de nós de borda ao mesmo tempo e a existência de dezenas de milhares de nós de borda ou mais cria uma situação impossível. Para atingir esse nível de abrangência, o {{site.data.keyword.edge_devices_notm}} usa políticas para determinar onde e quando implementar serviços e modelos de aprendizado de máquina de maneira autônoma. 

Uma política é expressa por meio de um idioma de política flexível, aplicado a modelos, nós, serviços e políticas de implementação. O idioma de política define os atributos (chamados `properties`) e declara requisitos específicos (chamados `constraints`). Isso permite que cada parte do sistema forneça entradas para o mecanismo de implementação do {{site.data.keyword.edge_devices_notm}}. Antes da implementação dos serviços, as restrições das políticas de modelos, de nós, de serviços e de implementação são verificadas, para assegurar que todos os requisitos sejam atendidos.

Devido ao fato de que os nós (nos quais os serviços são implementados) podem expressar requisitos, a política do {{site.data.keyword.edge_devices_notm}} é descrita como um sistema de política bidirecional. Os nós não são escravos no sistema de implementação de políticas do {{site.data.keyword.edge_devices_notm}}. Como resultado, as políticas permitem melhor controle sobre a implementação do serviço e do modelo do que os padrões. Quando a política está em uso, o {{site.data.keyword.edge_devices_notm}} procura por nós nos quais é possível implementar um determinado serviço e analisa os nós existentes para assegurar que permaneçam em conformidade (na política). Um nó está na política quando as políticas de nó, de serviço e de implementação que originalmente implementaram o serviço permanecem em vigor ou quando as mudanças em uma dessas políticas não afetam a compatibilidade da política. Por meio do uso de políticas, é possível separar melhor os assuntos, permitindo que os proprietários de nós de borda, desenvolvedores de serviços e proprietários de negócios articulem suas próprias políticas de forma independente.

As políticas são uma alternativa aos padrões de implementação. É possível publicar padrões no hub do {{site.data.keyword.ieam}} depois que um desenvolvedor publicou um serviço de borda no Horizon Exchange. A CLI do hzn oferece recursos para listar e gerenciar padrões no Horizon Exchange, incluindo comandos para listar, publicar, verificar, atualizar e remover padrões de implementação de serviço. Por meio dela, também é possível listar e remover chaves criptográficas que estão associadas a um padrão de implementação específico.

* [Casos de uso da política de implementação](policy_user_cases.md)
* [Usando Padrões](using_patterns.md)
