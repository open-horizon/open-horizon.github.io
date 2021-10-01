---

copyright:
years: 2020
lastupdated: "2020-4-24"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Instalação e registro automatizados do SDO
{: #sdo}

Com o [SDO](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard), criado pela Intel, é fácil e seguro configurar dispositivos de borda e associá-los a um hub de gerenciamento de borda. O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) suporta dispositivos ativados por SDO para que o agente seja instalado nos dispositivos e registrado no hub de gerenciamento do {{site.data.keyword.ieam}} com zero toque (simplesmente ligando os dispositivos).

## Visão geral do SDO
{: #sdo-overview}

O SDO consiste nestes componentes:

* O módulo SDO no dispositivo de borda (geralmente instalado pelo fabricante do dispositivo)
* Um voucher de propriedade (um arquivo que é fornecido para o comprador de dispositivo juntamente com o dispositivo físico)
* O servidor rendezvous SDO (o servidor conhecido que é contatado primeiro por um dispositivo ativado por SDO quando ele é iniciado pela primeira vez)
* Serviços de proprietário do SDO (serviços executados no hub de gerenciamento do {{site.data.keyword.ieam}} que configuram o dispositivo para usar esta instância específica do {{site.data.keyword.ieam}})

**Nota**: o SDO suporta apenas dispositivos de borda, não clusters de borda.

### Fluxo do SDO

<img src="../OH/docs/images/edge/09_SDO_device_provisioning.svg" style="margin: 3%" alt="SDO installation overview">

## Antes de Começar
{: #before_begin}

O SDO requer que os arquivos do agente sejam armazenados no {{site.data.keyword.ieam}} Cloud Sync Service (CSS). Se isso não foi feito, peça ao administrador para executar um dos seguintes comandos, conforme descrito em [Reunir arquivos de nó de borda](../hub/gather_files.md):

  `edgeNodeFiles.sh ALL -c ...`

## Experimentando o SDO
{: #trying-sdo}

Antes de adquirir dispositivos de borda ativados para SDO, é possível testar o suporte SDO em {{site.data.keyword.ieam}} com uma MV que simula um dispositivo ativado para SDO:

1. Você precisa de uma chave de API. Consulte [Criando sua chave de API](../hub/prepare_for_edge_nodes.md) para obter instruções para criar uma chave de API, caso você ainda não tenha uma.

2. Entre em contato com o administrador do {{site.data.keyword.ieam}} para obter os valores dessas variáveis de ambiente. (Você precisará deles na próxima etapa.)

   ```bash
   export HZN_ORG_ID=<exchange-org>    export HZN_EXCHANGE_USER_AUTH=iamapikey:<api-key>    export HZN_SDO_SVC_URL=https://<ieam-mgmt-hub-ingress>/edge-sdo-ocs/api    export HZN_MGMT_HUB_CERT_PATH=<path-to-mgmt-hub-self-signed-cert>    export CURL_CA_BUNDLE=$HZN_MGMT_HUB_CERT_PATH
   ```

3. Siga as etapas no [repositório de suporte do Open Horizon/SDO](https://github.com/open-horizon/SDO-support/blob/master/README-1.10.md) para observar se o SDO instala automaticamente o agente {{site.data.keyword.ieam}} em um dispositivo e o registra com o seu hub de gerenciamento do {{site.data.keyword.ieam}}.

## Incluindo dispositivos habilitados para SDO em seu domínio do {{site.data.keyword.ieam}}
{: #using-sdo}

Se você comprou dispositivos habilitados para SDO e deseja incorporá-los ao seu domínio do {{site.data.keyword.ieam}}:

1. [Faça login no console de gerenciamento do {{site.data.keyword.ieam}}](../console/accessing_ui.md).

2. Na guia **Nós**, clique em **Incluir nó**. 

   Insira as informações necessárias para criar uma chave de propriedade privada no serviço SDO e faça download da chave pública correspondente.
   
3. Preencha as informações necessárias para importar os vouchers de propriedade que você recebeu ao comprar os dispositivos.

4. Conecte os dispositivos à rede e ligue-os.

5. De volta ao console de gerenciamento, assista ao progresso dos dispositivos à medida que eles ficam on-line ao visualizar a página de visão geral do **Nó** e filtrar no nome da instalação.
