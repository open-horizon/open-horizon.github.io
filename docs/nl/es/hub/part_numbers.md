---

copyright:
years: 2020
lastupdated: "2020-02-10"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Passport Advantage
{: #part_numbers}

Complete el procedimiento siguiente para descargar los paquetes de {{site.data.keyword.ieam}}:

1. Busque el número de pieza de {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Vaya al separador IBM Passport Advantage Online en [Passport Advantage](https://www.ibm.com/software/passportadvantage/) e inicie la sesión con su ID de IBM.
2. Busque los archivos utilizando los números de pieza que se muestran en [Paquetes y números de pieza de {{site.data.keyword.ieam}}](#part_numbers_table):
3. Descargue los archivos en un directorio de su sistema.

## Paquetes de {{site.data.keyword.ieam}} y números de pieza
{: #part_numbers_table}

|Descripción de componente|Número de pieza de Passport Advantage|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} Licencia de Resource Value Unit + suscripción SW & soporte 12 meses|D2840LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANUAL SW S&S RENOVACIÓN 12 meses|E0R0HLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANUAL SW S&S RESTABLECER 12 meses|D2841LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit LICENCIA MENSUAL|D283ZLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit Licencia temporal confirmada|D28I1LL|
{: caption="Tabla 1. Paquetes de {{site.data.keyword.ieam}} y números de pieza" caption-side="top"}

## Licencias
{: #licensing}

Los requisitos de licencia se calculan basándose en el total de nodos registrados. En cualquier sistema que tenga la CLI **hzn** instalada que se ha configurado para autenticarse en el centro de gestión, determine el total de nodos registrados:

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

La salida será un entero; vea esta salida de ejemplo:

  ```
  $ hzn exchange status | jq .numberOfNodes   2641
  ```

Utilice la tabla de conversión siguiente en [Documento de licencia de {{site.data.keyword.ieam}}](https://ibm.biz/ieam-43-license) para calcular las licencias necesarias, con el recuento de nodos devuelto para el entorno desde el mandato anterior:

  ```
  De 1 a 10 recursos, 1,00 UVU por recurso   De 11 a 50 recursos, 10,0 UVU más 0,87 UVU por recurso por encima de 10   De 51 a 100 recursos, 44,8 UVU más 0,60 UVU por recurso por encima de 50   De 101 a 500 recursos, 74,8 UVU más 0,25 UVU por recurso por encima de 100   De 501 a 1.000 recursos, 174,8 UVU más 0,20 UVU por recurso por encima de 500   De 1.001 a 10.000 recursos, 274,8 UVU más 0,07 UVU por recurso por encima de 1.000   De 10.001 a 25.000 recursos, 904,8 UVU más 0,04 UVU por recurso por encima de 10.000   De 25.001 a 50.000 recursos, 1.504,8 UVU más 0,03 UVU por recurso por encima de 25.000   De 50.001 a 100.000 recursos, 2.254,8 UVU más 0,02 UVU por recurso por encima de 50.000   Para más de 100.000 recursos, 3.254,8 UVU más 0,01 UVU por recurso por encima de 100.000
  ```

El ejemplo siguiente le guía a lo largo del cálculo de licencias necesarias para **2641** nodos, lo que hará que sea necesario comprar **al menos 390** licencias:

  ```
  274,8 + (0,07 * ( 2641 - 1000 ) )
  274,8 + (0,07 * 1641 )   274,8 + 114,87   389,67
  ```

## Informes sobre licencias

La utilización de {{site.data.keyword.edge_notm}} se calcula automáticamente y se carga de forma periódica a un servicio de licencia común instalado localmente en el clúster. Para obtener más información sobre el servicio de licencias, incluyendo cómo ver el uso actual, generar informes de uso y más, consulte la [documentación del servicio de licencias](https://www.ibm.com/docs/en/cpfs?topic=operator-overview).
