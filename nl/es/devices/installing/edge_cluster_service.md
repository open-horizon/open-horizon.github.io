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

En general, el desarrollo de un servicio para ejecutarlo en un clúster periférico es similar al desarrollo
de un servicio periférico que se ejecuta en un dispositivo periférico, pero la diferencia está en cómo
se despliega el servicio periférico. Para desplegar un servicio periférico contenerizado en un clúster periférico, un desarrollador debe crear
primero un operador de Kubernetes que despliegue el servicio periférico contenerizado en un clúster
Kubernetes. Después de que el operador se haya escrito y probado, el desarrollador crea y publica el operador
como servicio de IBM Edge Application Manager (IEAM). Este proceso permite a un administrador de IEAM desplegar
el servicio de operador tal como se haría para cualquier servicio IEAM, con políticas o patrones.

Para utilizar el servicio `ibm.operator` que ya se ha publicado en el intercambio
IEAM utilizando la política de despliegue para ejecutar el servicio contenerizado de
`helloworld` en el clúster, consulte
[Horizon Operator Example Edge Service
![Se abre en otro separador](../../images/icons/launch-glyph.svg "Se abre en otro separador")](https://github.com/open-horizon/examples/tree/master/edge/services/operator#horizon-operator-example-edge-service).
