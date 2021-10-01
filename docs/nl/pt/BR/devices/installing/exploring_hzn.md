---

copyright:
years: 2019
lastupdated: "2019-11-17"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# Explorando o comando hzn
{: #exploring-hzn}

Nos nós de borda do {{site.data.keyword.horizon}}, o comando `hzn` permite que
você inspecione muitos aspectos do estado do sistema local e do ecossistema maior do
{{site.data.keyword.edge_devices_notm}} fora do nó de borda. O comando `hzn` também
permite que você interaja com o sistema e mude o estado de recursos que possui.

É possível obter ajuda para o comando `hzn`, incluindo mais detalhes sobre qualquer um
dos subcomandos usando a sinalização `--help` (ou `-h`) em qualquer nível
de subcomando. Por exemplo, tente os comandos a seguir:

```
hzn --help
hzn node --help
hzn exchange pattern --help
```
{: codeblock}

É possível usar a sinalização `--verbose` (ou `-v`) no comando `hzn` para fornecer uma saída mais detalhada. Geralmente, os comandos `hzn` são wrappers de conveniência nas APIs de REST fornecidos pelos componentes do {{site.data.keyword.horizon}}, e a sinalização `--verbose` geralmente mostra os detalhes das interações do REST nos bastidores. Por exemplo, tente:

```
hzn node list -v
```  
{: codeblock}

A saída desse comando mostra as duas chamadas de método REST `GET` nas URLs do `localhost` em que o agente do {{site.data.keyword.horizon}} local responde às solicitações REST.
