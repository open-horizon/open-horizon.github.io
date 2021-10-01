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

# Fehlerbehebung bei Knotenfehlern
{: #troubleshooting_node_errors}

{{site.data.keyword.edge_devices_notm}} publiziert eine Untergruppe von Ereignisprotokollen in Exchange, die in der {{site.data.keyword.gui}} angezeigt werden können. Die folgenden Fehler enthalten Links zu Hinweisen für die Fehlerbehebung.
{:shortdesc}

  - [error_image_load](#eil)
  - [error_in_deployment_configuration](#eidc)
  - [error_start_container](#esc)

## error_image_load
{: #eil}

Dieser Fehler tritt auf, wenn das Service-Image, auf das in der Servicedefinition verwiesen wird, nicht im Image-Repository vorhanden ist. Gehen Sie wie folgt vor, um diesen Fehler zu beheben: 

1. Publizieren Sie den Service ohne das Flag **-I** erneut.
    ```
    hzn exchange service publish -f <servicedefinitionsdatei>
    ```
    {: codeblock}

2. Publizieren Sie das Service-Image direkt im Image-Repository.
    ```
    docker push <imagename>
    ```
    {: codeblock} 
    
## error_in_deployment_configuration
{: #eidc}

Dieser Fehler tritt auf, wenn die Bereitstellungskonfigurationen für die Servicedefinitionen eine Bindung an eine Datei angeben, auf die nur der Rootbenutzer Zugriff hat. Gehen Sie wie folgt vor, um diesen Fehler zu beheben: 

1. Binden Sie den Container an eine Datei, auf die nicht nur der Rootbenutzer Zugriff hat. 
2. Ändern Sie die Dateiberechtigungen so, dass Benutzer die Datei lesen und schreiben können. 

## error_start_container
{: #esc}

Dieser Fehler tritt auf, wenn Docker beim Starten des Service-Containers einen Fehler feststellt. Die Fehlernachricht enthält möglicherweise weitere Informationen, die angeben, warum der Start des Containers fehlgeschlagen ist. Die Schritte zur Fehlerbehebung hängen vom Fehler ab. Die folgenden Fehler können auftreten: 

1. Die Einheit verwendet bereits einen publizierten Port, der von den Bereitstellungskonfigurationen angegeben wird. Gehen Sie wie folgt vor, um diesen Fehler zu beheben:  

    - Ordnen Sie dem Service-Container-Port einen anderen Port zu. Die angezeigte Portnummer muss nicht mit der Nummer des Service-Ports übereinstimmen. 
    - Stoppen Sie das Programm, dass denselben Port verwendet. 

2. Ein publizierter Port, der von den Bereitstellungskonfigurationen angegeben wird, hat keine gültige Portnummer. Eine Portnummer muss eine Zahl im Bereich zwischen 1 und 65535 sein. 
3. Ein Datenträgername in den Bereitstellungskonfigurationen ist kein gültiger Dateipfad. Datenträgerpfade müssen mit absoluten (und nicht mit relativen) Pfaden angegeben werden.  

## Zusätzliche Informationen

Weitere Informationen finden Sie in den folgenden Quellen:
  * [Leitfaden zur Fehlerbehebung für {{site.data.keyword.edge_devices_notm}}](../troubleshoot/troubleshooting.md)
