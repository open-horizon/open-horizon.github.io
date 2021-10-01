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


# Aplicativo

## Acessando o Painel do Granafa do {{site.data.keyword.ieam}} 
{: #monitoring_dashboard}

1. Siga as etapas em [Usando o console de gerenciamento](../console/accessing_ui.md) para garantir que seja possível acessar console de gerenciamento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Navegue até `https://<cluster-url>/grafana` para visualizar o painel do Grafana. 
3. No canto inferior esquerdo, há um ícone de perfil. Passe o mouse sobre ele e selecione a opção mudar organização. 
4. Selecione a organização `ibm-edge`. Se você instalou o {{site.data.keyword.ieam}} em um namespace diferente, selecione essa organização em vez disso.
5. Procure por "{{site.data.keyword.ieam}}" de modo que seja possível monitorar a pressão geral da CPU, da memória e da rede de sua instalação do {{site.data.keyword.ieam}}.

   <img src="../images/edge/ieam_monitoring_dashboard.png" style="margin: 3%" alt="IEAM Monitoring Dashboard" width="85%" height="85%" align="center">


# Monitoramento de nós e serviços de borda
{: #monitoring_edge_nodes_and_services}

[Efetue login no console de gerenciamento](../console/accessing_ui.md) para monitorar os nós da borda e serviços do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

* Monitorar os nós de borda:
  * O painel de Nós é a primeira página exibida e inclui um gráfico de rosca que mostra o estado de todos os nós de borda.
  * Para ver todos os nós em um determinado estado, clique nessa cor no gráfico de rosca. Por exemplo, para ver todos os nós de borda com erros (se houver), clique na cor em que a legenda indica que é usada para **Possui erro**.
  * Uma lista dos nós com erros é exibida. Para realizar drill down em um nó para ver o erro específico, clique no nome do nó.
  * Na página de detalhes do nó que é exibida, a seção **Erros do agente de borda** mostra os serviços que possuem erros, a mensagem de erro específica e o registro de data/hora.
* Monitorar os serviços de borda:
  * Na guia **Serviços**, clique no serviço no qual você deseja realizar drill down, que exibe a página de detalhes do serviço de borda.
  * Na seção **Implementação** da página de detalhes, é possível ver as políticas e os padrões que implementam este serviço nos nós de borda.
* Monitorar os serviços de borda em um nó de borda:
  * In the **Nodes**, alterne para a visualização de lista e clique no nó de borda que você deseja realizar drill down.
  * Na página de detalhes do nó, a seção **Serviços** mostra quais serviços de borda estão atualmente em execução naquele nó de borda.
