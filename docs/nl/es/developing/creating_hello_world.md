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

# Creación de su propio hello world para clústeres
{: #creating_hello_world}

Para desplegar un servicio periférico contenerizado en un clúster periférico, el primer paso es construir un Operador de Kubernetes que despliegue el servicio periférico contenerizado en un clúster Kubernetes.

Utilice este ejemplo para aprender a:

* Crear un operador de Ansible con `operator-sdk`
* Utilizar el operador desplegar un servicio en un clúster periférico
* Exponer un puerto en el clúster periférico al que pueda acceder externamente con el mandato `curl`

Consulte [Creación de su propio servicio periférico de operador](https://github.com/open-horizon/examples/blob/v2.27/edge/services/hello-operator/CreateService.md#creating-your-own-operator-edge-service).

Para ejecutar el servicio `hello-operator` publicado, consulte [Utilización del servicio periférico de ejemplo de operador con la política de despliegue](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
