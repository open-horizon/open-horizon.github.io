---

copyright:
  years: 2019, 2020
lastupdated: "2021-08-31"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Problemas e Limitações Conhecidos  
{: #knownissues}

São problemas e limitações conhecidos do {{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}).

Para obter uma lista completa de problemas em aberto para a camada do {{site.data.keyword.ieam}} OpenSource, revise os problemas do GitHub em cada um dos [repositórios do Open Horizon](https://github.com/open-horizon/).

{:shortdesc}

## Problemas conhecidos do {{site.data.keyword.ieam}} {{site.data.keyword.version}}

Estes são problemas e limitações conhecidos do {{site.data.keyword.ieam}} {{site.data.keyword.version}}.

* O {{site.data.keyword.ieam}} não executa um malware ou varredura de vírus em dados que são carregados para o Model Management Service (MMS). Para obter mais informações sobre a segurança do MMS, consulte [Segurança e privacidade](../OH/docs/user_management/security_privacy.md#malware).

* A sinalização **-f &lt;directory&gt;** de **edgeNodeFiles.sh** não tem o efeito desejado. Em vez disso, os arquivos são coletados no diretório atual. Para obter mais informações, consulte o [problema 2187](https://github.com/open-horizon/anax/issues/2187). A solução alternativa é executar o comando da seguinte forma:

   ```bash
   (cd <dir> && edgeNodeFiles.sh ... )
   ```
   {: codeblock}



* Como parte da instalação do {{site.data.keyword.ieam}}, dependendo da versão do {{site.data.keyword.common_services}} instalado, certificados podem ter sido criados com uma curta expectativa de vida levando à sua renovação automática. É possível encontrar os problemas de certificado a seguir ([que podem ser resolvidos com estas etapas](cert_refresh.md)):
  * Saída JSON inesperada com uma mensagem "Falha na solicitação com o código de status 502" exibida ao acessar o console de gerenciamento do {{site.data.keyword.ieam}}.
  * Os nós de borda não são atualizados quando um certificado é renovado e devem ser atualizados manualmente para assegurar uma comunicação bem-sucedida com o Hub do {{site.data.keyword.ieam}}.

* Ao utilizar o {{site.data.keyword.ieam}} com bancos de dados locais, se o pod **cssdb** for excluído e recriado, manual ou automaticamente por meio através do planejador de Kubernetes, isso resultará em perda de dados para o banco de dados Mongo. Siga a documentação de [backup e recuperação](../admin/backup_recovery.md) para minimizar a perda de dados.

* Ao usar o {{site.data.keyword.ieam}} com bancos de dados locais, se os recursos de tarefas **create-agbotdb-cluster** ou **create-exchangedb-cluster** forem excluídos, a tarefa irá executar novamente e reinicializar o respectivo banco de dados, o que resulta em perda de dados. Siga a documentação de [backup e recuperação](../admin/backup_recovery.md) para minimizar a perda de dados.

* Com o uso de bancos de dados locais, um ou ambos os bancos de dados Postgres podem se tornar não responsivos. Para resolver isso, reinicie todas as sentinelas e proxies para o banco de dados não responsivo. Modifique e execute os comandos a seguir com o aplicativo impactado e seu Recurso Customizado (CR) `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-sentinel` e `oc rollout restart deploy <CR_NAME>-<agbot|exchange>db-proxy` (exemplo de sentinela de troca: `oc rollout restart deploy ibm-edge-exchangedb-sentinel`).

* Se você executar **hzn service log** no {{site.data.keyword.rhel}} com qualquer arquitetura, o comando trava. Para obter mais informações, consulte [problema 2826](https://github.com/open-horizon/anax/issues/2826). Como uma solução alternativa para esta condição, obtenha os logs de contêiner (é possível também especificar -f para cauda):

   ```
   docker logs &amp;TWBLT;container&gt;
   ```
   {: codeblock}


## Limitações do {{site.data.keyword.ieam}} {{site.data.keyword.version}}

* A documentação do produto {{site.data.keyword.ieam}} é traduzida para as geografias participantes, mas a versão em inglês é atualizada continuamente. As discrepâncias entre o inglês e as versões traduzidas podem aparecer entre os ciclos de tradução. Verifique a versão em inglês para ver se alguma discrepância foi resolvida depois que as versões traduzidas foram publicadas.

* Ao mudar os atributos **proprietários** ou **públicos** de serviços, padrões ou políticas de implementação na troca, pode levar até cinco minutos para acessar esses recursos para visualizar a mudança. Da mesma forma, ao fornecer a um usuário de troca o privilégio de administrador, pode levar até cinco minutos para que essa mudança se propague para todas as instâncias de troca. O período de tempo pode ser reduzido configurando `api.cache.resourcesTtlSeconds` para um valor menor (o padrão é 300 segundos) no arquivo `config.json` do Exchange, com um custo de desempenho um pouco menor.

* O agente não oferece suporte ao [Model Management System](../developing/model_management_system.md) (MMS) para serviços dependentes.

* A ligação secreta não funciona para um serviço sem contrato definido em um padrão.
 
* O agente de cluster de borda não suporta K3S v1.21.3+k3s1 porque o diretório de volume montado só tem permissão 0700. Consulte [Não é possível gravar dados em PVC local](https://github.com/k3s-io/k3s/issues/3704) para uma solução temporária.
 
* Cada agente de nó de borda do {{site.data.keyword.ieam}} inicia todas as conexões de rede com o hub de gerenciamento do {{site.data.keyword.ieam}}. O hub de gerenciamento nunca inicia conexões com seus nós de borda. Portanto, um nó de borda pode estar por trás de um firewall NAT se o firewall tiver conectividade TCP com o hub de gerenciamento. No entanto, nós de borda não podem atualmente se comunicar com o hub de gerenciamento por meio de um proxy SOCKS.
  
* A instalação de dispositivos de borda com Fedora ou SuSE é suportada apenas pelo método de [Registro e instalação manual avançada do agente](../installing/advanced_man_install.md).
