---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Visão geral da política
{: #policy_overview}

Inclua um gráfico mostrando as partes envolvidas na política (por exemplo, nó, serviço e política de negócios, restrições, propriedades). 

Esta seção discute os conceitos de política. 

Para obter uma visão geral mais abrangente de vários componentes do sistema, consulte [Visão geral de como funciona o IBM Edge Application Manager for Devices](../getting_started/overview.md). Para obter um exemplo prático de política, consulte, [Hello world](../getting_started/policy.md).

Um administrador não consegue gerenciar milhares de nós de borda ao mesmo tempo e a existência de dezenas de milhares de nós de borda ou mais cria uma situação impossível. Para atingir esse nível de abrangência, o {{site.data.keyword.edge_devices_notm}} usa políticas para determinar onde e quando implementar serviços e modelos de aprendizado de máquina de maneira autônoma. As políticas são uma alternativa aos padrões de implementação.

Uma política é expressa por meio de um idioma de política flexível, aplicado a modelos, nós, serviços e políticas de implementação. O idioma de política define os atributos (chamados `properties`) e declara requisitos específicos (chamados `constraints`). Isso permite que cada parte do sistema forneça entradas para o mecanismo de implementação do {{site.data.keyword.edge_devices_notm}}. Antes da implementação dos serviços, as restrições das políticas de modelos, de nós, de serviços e de implementação são verificadas, para assegurar que todos os requisitos sejam atendidos.

Devido ao fato de que os nós (nos quais os serviços são implementados) podem expressar requisitos, a política do {{site.data.keyword.edge_devices_notm}} é descrita como um sistema de política bidirecional. Os nós não são escravos no sistema de implementação de políticas do {{site.data.keyword.edge_devices_notm}}. Como resultado, as políticas permitem melhor controle sobre a implementação do serviço e do modelo do que os padrões. Quando a política está em uso, o {{site.data.keyword.edge_devices_notm}} procura por nós nos quais é possível implementar um determinado serviço e analisa os nós existentes para assegurar que permaneçam em conformidade (na política). Um nó está na política quando as políticas de nó, de serviço e de implementação que originalmente implementaram o serviço permanecem em vigor ou quando as mudanças em uma dessas políticas não afetam a compatibilidade da política. Por meio do uso de políticas, é possível separar melhor os assuntos, permitindo que os proprietários de nós de borda, desenvolvedores de serviços e proprietários de negócios articulem suas próprias políticas de forma independente.

Há quatro tipos de política:

* Nó
* Serviço
* Implementação
* Gabarito
