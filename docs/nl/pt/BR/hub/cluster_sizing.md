---

copyright:
years: 2020
lastupdated: "2020-10-28"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}


# Dimensionamento e requisitos do sistema
{: #size}

## Considerações sobre Dimensionamento

O dimensionamento de um cluster envolve muitas considerações. Este conteúdo descreve algumas dessas considerações e fornece um guia com diretrizes para auxiliá-lo na tarefa de definição do tamanho do cluster.

O primeiro item a ser levado em conta são os serviços que precisam ser executados no cluster. Este conteúdo oferece orientações sobre dimensionamento apenas para estes serviços:

* {{site.data.keyword.common_services}}
* Hub de gerenciamento do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}})

Opcionalmente, é possível instalar a [criação de log de cluster do {{site.data.keyword.open_shift_cp}}](../admin/accessing_logs.md#ocp_logging).

## Considerações sobre o banco de dados do {{site.data.keyword.ieam}}

Existem duas configurações de banco de dados suportadas que afetam os cálculos de dimensionamento do hub de gerenciamento do {{site.data.keyword.ieam}}:

* Os bancos de dados **locais** são instalados (por padrão) como recursos do {{site.data.keyword.open_shift}} no cluster do {{site.data.keyword.open_shift}}.
* Os bancos de dados **remotos** são bancos de dados fornecidos pelo usuário e podem ser locais, ofertas SaaS de provedores em nuvem e assim por diante.

### Requisitos de armazenamento local do {{site.data.keyword.ieam}}

Além do sempre instalado componente Secure Device Onboarding (SDO), os bancos de dados **locais** e o gerenciador de segredos requerem armazenamento persistente. Este armazenamento utiliza classes de armazenamento dinâmicas configuradas para o seu cluster do {{site.data.keyword.open_shift}}.

Para obter mais informações, consulte [Opções de armazenamento e instruções de configuração do {{site.data.keyword.open_shift}} dinâmico](https://docs.openshift.com/container-platform/4.6/storage/understanding-persistent-storage.html).

Você é responsável por ativar a criptografia em repouso no momento da criação do cluster. Pode muitas vezes ser incluído como parte da criação de clusters em plataformas de nuvem. Para obter mais informações, consulte a [documentação a seguir](https://docs.openshift.com/container-platform/4.6/installing/installing-fips.html).

Um dos aspectos mais importantes quanto ao tipo de classe de armazenamento escolhido é se a classe de armazenamento suporta ou não **allowVolumeExpansion**. Se houver suporte, o comando a seguir retornará **true**:

```
oc get storageclass <desired storage class> -o json | jq .allowVolumeExpansion
```
{: codeblock}

Se a classe de armazenamento permitir a expansão do volume, o tamanho pode ser ajustado após a instalação (dado que o espaço de armazenamento subjacente está disponível para alocação). Caso a classe de armazenamento não permita a expansão de volumes, deve-se pré-alocar o armazenamento de acordo com o caso de uso. 

Se você precisar de mais armazenamento após a instalação inicial com uma classe de armazenamento que não permite expansão de volume, será necessário executar por meio de uma reinstalação usando as etapas descritas na página de [backup e restauração](../admin/backup_recovery.md).

É possível alterar as alocações antes da instalação do Hub de gerenciamento do {{site.data.keyword.ieam}}, modificando os valores de **Armazenamento**, conforme descrito na página [Configuração](configuration.md). As alocações são configuradas para os valores padrão a seguir:

* PostgreSQL Exchange (Armazena dados para o Exchange e tem oscilações de tamanho, dependendo do uso, mas a configuração de armazenamento padrão pode suportar até o limite anunciado de nós de borda)
  * 20 GB
* PostgreSQL AgBot (Armazena dados para o AgBot e a configuração de armazenamento padrão pode suportar até o limite anunciado de nós de borda)
  * 20 GB
* MongoDB Cloud Sync Service (Armazena conteúdo para o Model Management Service (MMS)). Dependendo do número e do tamanho de seus modelos, você pode desejar modificar essa alocação padrão
  * 50 GB
* Volume persistente do Hashicorp Vault (armazena segredos utilizados pelos serviços de dispositivos de borda)
  * 10 GB (Este tamanho de volume não é configurável)
* Volume persistente do Secure Device Onboarding (armazena vouchers de propriedade do dispositivo, opções de configuração do dispositivo e o status de implementação de cada dispositivo)
  * 1 GB (este tamanho de volume não é configurável)

* ** Notas: **
  * Os volumes {{site.data.keyword.ieam}} são criados com o modo de acesso **ReadWriteOnce**.
  * Os Serviços Comuns do IBM Cloud Platform possuem requisitos de armazenamento adicionais para seus serviços. Os volumes  a seguir são criados no namespace **ibm-common-services** quando são instalados com os padrões {{site.data.keyword.ieam}}:
    ```
    NAME                                                                                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE     alertmanager-ibm-monitoring-alertmanager-db-alertmanager-ibm-monitoring-alertmanager-0   Bound    pvc-3979805f-8e3b-44d6-a039-cd438a3dbb25   10Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-0                                                                 Bound    pvc-e21604a7-14e4-4049-824e-a5a9feb472c8   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-1                                                                 Bound    pvc-eaecfa29-5c6a-45c2-9d26-58a393103791   20Gi       RWO            csi-cephfs     20h     mongodbdir-icp-mongodb-2                                                                 Bound    pvc-42282c2b-bde8-4adf-86ad-006d2f07df91   20Gi       RWO            csi-cephfs     19h     prometheus-ibm-monitoring-prometheus-db-prometheus-ibm-monitoring-prometheus-0           Bound    pvc-90237949-6f13-481b-8afa-7d86883b8a4f   10Gi       RWO            csi-cephfs     20h
    ```

    É possível aprender mais sobre os requisitos de armazenamento do IBM Cloud Platform Common Services e sobre opções de configuração [aqui](https://www.ibm.com/support/knowledgecenter/SSHKN6/installer/3.x.x/custom_resource.html).

### Considerações sobre o banco de dados remoto do {{site.data.keyword.ieam}}

A utilização de seus próprios bancos de dados **remotos** reduz as classes de armazenamentos e os requisitos de cálculos para esta instalação, a menos que eles sejam fornecidos no mesmo cluster.

Os bancos de dados **remotos** devem fornecer, pelo menos, os seguintes recursos e configurações:

* 2 vCPUs
* 2 GB de RAM
* Os tamanhos de armazenamento padrão mencionados na seção anterior
* Para bancos de dados PostgreSQL, 100 **max_connections** (que é normalmente o padrão)

## Dimensionamento de nó do trabalhador

Os serviços que usam [recursos de cálculo do Kubernetes](https://kubernetes.io/docs/concepts/configuration/manage-compute-resources-container) são planejados por meio de nós do trabalhador disponíveis.

### Requisitos mínimos para a configuração padrão do {{site.data.keyword.ieam}}
| Número de nós do trabalhador | vCPUs por nó do trabalhador | Memória por nó do trabalhador (GB) | Armazenamento em disco local por nó do trabalhador (GB) |
| :---: | :---: | :---: | :---: |
| 3	| 8	| 32	| 100 	|

**Nota:** Alguns ambientes de clientes podem exigir vCPUs adicionais por nó do trabalhador ou por nós do trabalhador adicionais, portanto, mais capacidade de CPU pode ser alocada para o componente do Exchange.


&nbsp;
&nbsp;

Depois de determinar o dimensionamento adequado para seu cluster, é possível começar a [instalação](online_installation.md).
