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

# Servicio de clúster periférico
{: #Edge_cluster_service}

En general, el desarrollo de un servicio para ejecutarlo en un clúster periférico es similar al desarrollo de un servicio periférico que se ejecuta en un dispositivo periférico, pero la diferencia está en cómo se despliega el servicio periférico. Para desplegar un servicio periférico contenerizado en un clúster periférico, un desarrollador debe crear primero un operador de Kubernetes que despliegue el servicio periférico contenerizado en un clúster Kubernetes. Una vez que se ha escrito y probado el operador, el desarrollador crea y publica el operador como un servicio de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}). El servicio de operador se puede desplegar en clústeres periféricos con política o patrón como lo haría cualquier servicio de {{site.data.keyword.edge_notm}}.

{{site.data.keyword.ieam}} Exchange contiene un servicio denominado `hello-operator` que le permite exponer un puerto en el clúster periférico al que se puede acceder externamente utilizando el mandato `curl`. Para desplegar este servicio de ejemplo en el clúster periférico, consulte [Servicio periférico de ejemplo de operador de Horizon](https://github.com/open-horizon/examples/tree/v2.27/edge/services/hello-operator#-using-the-operator-example-edge-service-with-deployment-policy).
