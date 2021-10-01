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

Conclua o procedimento a seguir para fazer download dos pacotes do {{site.data.keyword.ieam}}:

1. Encontre o seu número de peça do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).
2. Acesse a guia IBM Passport Advantage Online em [Passport Advantage](https://www.ibm.com/software/passportadvantage/) e efetue login com o seu IBMid.
2. Procure os seus arquivos usando os números de peça que estão listados em [Pacotes e números de peça do {{site.data.keyword.ieam}}](#part_numbers_table):
3. Faça o download dos arquivos para um diretório no computador.

## Pacotes e números de peça do {{site.data.keyword.ieam}}
{: #part_numbers_table}

|Descrição da peça|Número da peça do Passport Advantage|
|----------------|------------------------------|
|{{site.data.keyword.edge_notm}} Resource Value Unit License + SW Subscription & Support 12 Months|D2840LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANNUAL SW S&S RNWL 12 months|E0R0HLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit ANNUAL SW S&S REINSTATE 12 months|D2841LL|
|{{site.data.keyword.edge_notm}} Resource Value Unit MONTHLY LICENSE|D283ZLL|
|{{site.data.keyword.edge_notm}} Resource Value Unit Committed Term License|D28I1LL|
{: caption="Tabela 1. Pacotes e números de peças do {{site.data.keyword.ieam}}" caption-side="top"}

## Licença
{: #licensing}

Os requisitos de licenciamento são calculados com base no total de nós registrados. Em qualquer sistema, que instalou a CLI **hzn** que foi configurada para autenticar com o seu hub de gerenciamento, determine o seu total de nó registrado:

  ```
  hzn exchange status | jq .numberOfNodes
  ```
  {: codeblock}

A saída será um número inteiro, veja este exemplo de saída:

  ```
  $ hzn exchange status | jq .numberOfNodes   2641
  ```

Use a tabela de conversão a seguir em [Documento de licença do {{site.data.keyword.ieam}}](https://ibm.biz/ieam-43-license) para calcular as licenças necessárias, com a contagem de nós retornada para o seu ambiente a partir do comando anterior:

  ```
  From 1 to 10 Resources, 1.00 UVU per Resource   From 11 to 50 Resources, 10.0 UVUs plus 0.87 UVUs per Resource above 10   From 51 to 100 Resources, 44.8 UVUs plus 0.60 UVUs per Resource above 50   From 101 to 500 Resources, 74.8 UVUs plus 0.25 UVUs per Resource above 100   From 501 to 1,000 Resources, 174.8.0 UVUs plus 0.20 UVUs per Resource above 500   From 1,001 to 10,000 Resources, 274.8 UVUs plus 0.07 UVUs per Resource above 1,000   From 10,001 to 25,000 Resources, 904.8 UVUs plus 0.04 UVUs per Resource above 10,000   From 25,001 to 50,000 Resources, 1,504.8 UVUs plus 0.03 UVUs per Resource above 25,000   From 50,001 to 100,000 Resources, 2,254.8 UVUs plus 0.02 UVUs per Resource above 50,000   For more than 100,000 Resources, 3,254.8 UVUs plus 0.01 UVUs per Resource above 100,000
  ```

O exemplo a seguir percorre o cálculo das licenças necessárias para nós do **2641**, o que exigiria a compra de **pelo menos 390** licenças:

  ```
  274.8 + ( .07 * ( 2641 - 1000 ) )
  274.8 + ( .07 * 1641 )   274.8 + 114.87   389.67
  ```

## Relatório de licença

A utilização do {{site.data.keyword.edge_notm}} é automaticamente calculada e transferida por upload periodicamente para um serviço de licenciamento comum instalado localmente em seu cluster. Para obter mais informações sobre o serviço de licenciamento, incluindo como visualizar o uso atual, gerar relatórios de uso e muito mais, consulte a [documentação do serviço de licenciamento](https://www.ibm.com/docs/en/cpfs?topic=operator-overview).
