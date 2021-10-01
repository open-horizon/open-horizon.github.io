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

**Visualização de tecnologia**: neste momento, o suporte do SDO deve ser usado apenas para testar o processo do SDO e para familiarizar-se com ele, a fim de planejar seu uso no futuro. Em uma liberação futura, o suporte do SDO estará disponível para uso em produção.

[O SDO ![Abre em uma novaguia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://software.intel.com/en-us/secure-device-onboard) (Secure Device Onboard) é uma tecnologia criada pela Intel para facilitar e proteger a configuração de dispositivos de borda e para associá-los a um hub de gerenciamento de borda. O {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) inclui suporte para dispositivos ativados para SDO para que o agente seja instalado no dispositivo e registrado no hub de gerenciamento {{site.data.keyword.ieam}} sem nenhum contato (apenas ativando o dispositivo).


## Visão geral do SDO
{: #sdo-overview}

O SDO consiste em quatro componentes:

1. O módulo SDO no dispositivo de borda (geralmente instalado pelo fabricante do dispositivo)
2. Um voucher de propriedade (um arquivo que é fornecido para o comprador de dispositivo juntamente com o dispositivo físico)
3. O servidor rendezvous SDO (o primeiro servidor bem conhecido com o qual um dispositivo ativado para SDO faz contato quando ele inicializa na primeira vez). 
4. Serviços do proprietário SDO (serviços executados com o hub de gerenciamento do
{{site.data.keyword.ieam}} que conectam o dispositivo à esta instância específica do
{{site.data.keyword.ieam}})

### Diferenças na Visualização de tecnologia
{: #sdo-tech-preview-differences}

- **Dispositivo ativado para SDO:** para teste de SDO, um script é fornecido para incluir o módulo SDO em uma VM, para que ele se comporte da mesma maneira que um dispositivo ativado para SDO durante a inicialização. Isso permite testar a integração do SDO com o {{site.data.keyword.ieam}} sem a
necessidade de comprar um dispositivo ativado para SDO.
- **Voucher de propriedade:** normalmente você recebe um voucher de propriedade de um fabricante do dispositivo. Se você usar o script que é mencionado no marcador anterior para incluir o módulo SDO em uma VM, ele também criará o voucher de propriedade na VM. A cópia desse voucher a partir da VM representa o "recebimento do voucher de propriedade de um fabricante do dispositivo".
- **Servidor rendezvous:** na produção, o dispositivo de inicialização faz contato com o servidor rendezvous SDO global da Intel. Para desenvolvimento e teste desta visualização de tecnologia, você usará um servidor rendezvous de desenvolvimento que é empacotado com os serviços do proprietário do SDO.
- **Serviços do proprietário do SDO:** nesta visualização de tecnologia, os serviços do proprietário do SDO não serão instalados automaticamente no hub de gerenciamento do {{site.data.keyword.ieam}}. Em vez disso, é fornecido um script de conveniência para iniciar os serviços do proprietário do SDO em qualquer servidor que tenha acesso à rede ao hub de gerenciamento do {{site.data.keyword.ieam}} e que os dispositivos SDO possam acessar pela rede.

## Usando o SDO
{: #using-sdo}

Para testar o SDO e ver se ele instala automaticamente o agente {{site.data.keyword.ieam}} e o registra com seu hub de gerenciamento do {{site.data.keyword.ieam}}, siga as etapas no repositório [open-horizon/SDO-support ![Abre em uma nova guia](../../images/icons/launch-glyph.svg "Abre em uma nova guia")](https://github.com/open-horizon/SDO-support/blob/master/README.md).
