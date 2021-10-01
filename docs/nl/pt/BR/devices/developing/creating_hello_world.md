---

copyright:
  years: 2020
lastupdated: "2020-04-9"

---

{:shortdesc: .shortdesc}
{:new_window: target="_blank"}
{:codeblock: .codeblock}
{:pre: .pre}
{:screen: .screen}
{:tip: .tip}
{:download: .download}

# Criando seu próprio Hello World para clusters
{: #creating_hello_world}

Para implementar um serviço de borda conteinerizado em um cluster de borda, a primeira etapa é construir um Operador Kubernetes que implemente o serviço de borda conteinerizado em um cluster Kubernetes.

Use como exemplo as instruções a seguir: 

* Grave um operador
* Use um operador para implementar um serviço de borda em um cluster (neste caso, `ibm.helloworld`)
* Transmita as variáveis de ambiente do horizonte (e outras variáveis necessárias) para os pods de serviço implementados

Consulte [Criando seu próprio serviço de cluster Hello World ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/operator/CreateService.md).

Para executar o serviço `ibm.operator`, consulte [Exemplo de serviço de borda do operador com a política de implementação ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
