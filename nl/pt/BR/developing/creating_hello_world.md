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

* Crie um operador do Ansible usando `operator-sdk`
* Use o operador para implementar um serviço em um cluster de borda
* Exponha uma porta em seu cluster de borda que seja possível acessar externamente com o comando `curl`

Consulte [Criando seu próprio serviço de borda do operador)](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service).

Para executar o serviço `hello-operador` publicado, consulte [Usando o serviço de borda de exemplo do operador com política de implementação](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
