---

copyright:
years: 2019
lastupdated: "2019-09-18"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Resolução de problemas de erros do nó
{: #troubleshooting_node_errors}

O {{site.data.keyword.edge_devices_notm}} publica um subconjunto de logs de eventos no Exchange que é visualizável na {{site.data.keyword.gui}}. Esses erros se vinculam à orientação de resolução de problemas.
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

Este erro ocorre quando a imagem de serviço que é referenciada na definição de serviço não existe no repositório de imagem. Para resolver esse erro:

1. Publique novamente o serviço sem a sinalização **-I**.
    ```
    hzn exchange service publish -f <service-definition-file>
    ```
    {: codeblock}

2. Envie por push a imagem de serviço diretamente para o repositório de imagem. 
    ```
    docker push <image name>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

Este erro ocorre quando as configurações de implementação de definições de serviço especificam uma ligação a um arquivo protegido por raiz. Para resolver esse erro:

1. Ligue o contêiner a um arquivo que não esteja protegido por raiz.
2. Mude as permissões de arquivo para permitir que os usuários leiam e gravem no arquivo.

## error_start_container
{: #esc}

Este erro ocorre quando o docker encontra um erro quando ele inicia o contêiner de serviço. Esta mensagem de erro pode conter detalhes que indicam o motivo pelo qual o contêiner iniciou com falha. As etapas de resolução de erro dependem do erro. Os seguintes erros podem ocorrer:

1. O dispositivo já está usando uma porta publicada que é especificada pelas configurações de implementação. Para resolver o erro: 

    - Mapeie uma porta diferente para a porta do contêiner de serviço. O número da porta exibido não precisa corresponder ao número da porta de serviço.
    - Pare o programa que está usando a mesma porta.

2. Uma porta publicada que é especificada pelas configurações de implementação não é um número de porta válido. Os números de porta devem ser um número no intervalo de 1 a 65535.
3. Um nome de volume nas configurações de implementação não é um caminho de arquivo válido. Os caminhos de volume devem ser especificados pelos seus caminhos absolutos (não relativos). 

## Informações adicionais

Para obter informações adicionais, consulte
  * [Guia de Resolução de Problemas do {{site.data.keyword.edge_devices_notm}}](../troubleshoot/troubleshooting.md)
