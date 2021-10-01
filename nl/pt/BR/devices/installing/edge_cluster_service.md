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

Em geral, o desenvolvimento de um serviço que será executado em um cluster de borda é semelhante ao desenvolvimento de um serviço de borda que é executado em um dispositivo de borda, com a diferença no modo como o serviço de borda é implementado. Para implementar um serviço de borda conteinerizado em um cluster de borda, um desenvolvedor deve primeiro construir um operador do Kubernetes que implementa o serviço de borda conteinerizado em um cluster do Kubernetes. Depois que o operador é gravado e testado, o desenvolvedor cria e publica o operador como um serviço do IBM Edge Application Manager (IEAM). Este processo permite que um administrador do IEAM implemente o serviço do operador tal como faria para qualquer serviço do IEAM, com política ou padrões. 

Para usar o serviço `ibm.operator` que já está publicado em seu IEAM Exchange usando a Política de implementação para executar o serviço conteinerizado `helloworld` em seu cluster, consulte [Serviço de borda de exemplo do operador Horizon ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma novaguia")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).

