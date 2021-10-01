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

# CLI 'hzn' erkunden
{: #exploring-hzn}

Verwenden Sie den Befehl `hzn` auf {{site.data.keyword.horizon}}-Edge-Knoten, um  zahlreiche Aspekte zum Status des lokalen Systems und des weiterreichenden direkten Umfeldes von {{site.data.keyword.edge_notm}} außerhalb des eigenen Edge-Knotens zu untersuchen. Mit dem Befehl `hzn` können Sie mit dem System interagieren und Änderungen am Status der eigenen Ressourcen durchführen.

Die Hilfe zum Befehl `hzn` einschließlich der Details zu den Unterbefehlen können Sie abrufen, indem Sie das Flag `--help` (oder `-h`) auf jeder Unterbefehlsebene angeben. Führen Sie beispielsweise die folgenden Befehle aus:

```
hzn --help   hzn node --help   hzn exchange pattern --help
```
{: codeblock}

Mit dem Flag `--verbose` (oder `-v`) im Befehl `hzn` können Sie das System zur Ausgabe detaillierterer Ausgabedaten anweisen. Häufig werden die `hzn`-Befehle als Oberflächen zur Verbesserung der Benutzerfreundlichkeit der REST-APIs verwendet, die von den {{site.data.keyword.horizon}}-Komponenten bereitgestellt werden. Mit dem Flag `--verbose` können Sie normalerweise die Details der REST-Interaktionen anzeigen, die im Hintergrund ablaufen. Führen Sie z. B. den folgenden Befehl aus:

```
hzn node list -v
```  
{: codeblock}

In der Ausgabe dieses Befehls werden die beiden REST-Methodenaufrufe für `GET` für die URLs des lokalen Hosts (`localhost`) angezeigt, wobei der lokale {{site.data.keyword.horizon}}-Agent auf die REST-Anforderungen reagiert.

Beispiel:

```
[verbose] GET http://localhost:8510/node [verbose] HTTP code: 200 ...
[verbose] GET http://localhost:8510/status [verbose] HTTP code: 200
```  
{: codeblock}
