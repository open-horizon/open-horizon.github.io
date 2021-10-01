---

copyright:
  years: 2020
lastupdated: "2020-05-9"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Serviço de cluster de borda
{: #Edge_cluster_service}

Em geral, o desenvolvimento de um serviço que será executado em um cluster de borda é semelhante ao desenvolvimento de um serviço de borda que é executado em um dispositivo de borda, com a diferença no modo como o serviço de borda é implementado. Para implementar um serviço de borda conteinerizado em um cluster de borda, um desenvolvedor deve primeiro construir um operador do Kubernetes que implementa o serviço de borda conteinerizado em um cluster do Kubernetes. Depois que o operador é gravado e testado, o desenvolvedor cria e publica o operador como um serviço {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). O serviço do operador pode ser implementado em clusters de borda com política ou padrão como qualquer serviço do {{site.data.keyword.edge_notm}} seria.

O {{site.data.keyword.ieam}} Exchange contém um serviço chamado `hello-operator`, que permite expor uma porta em um cluster de borda que pode ser acessada externamente, usando o comando `curl`. Para implementar esse serviço de exemplo em seu cluster de borda, consulte [Serviço de borda de exemplo do Horizon Operator](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
