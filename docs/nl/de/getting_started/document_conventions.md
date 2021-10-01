---

copyright:
years: 2020
lastupdated: "2020-04-01"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# In diesem Dokument verwendete Konventionen
{: #document_conventions}

Zur Vermittlung bestimmter Bedeutungen werden im vorliegenden Dokument Konventionen für den Inhalt verwendet.  

## Konventionen für Befehle

Ersetzen Sie den Variableninhalt, der zwischen den spitzen Klammern (< >) angezeigt wird, durch spezielle Werte für Ihre Anforderungen. Beziehen Sie die Zeichen < > nicht in den Befehl ein.

### Beispiel

  ```
  hzn key create "<unternehmensname>" "<ihre_e-mail-adresse>"
  ```
  {: codeblock}
   
## Literalzeichenfolgen

Bei dem im Management-Hub oder in Code angezeigten Inhalt handelt es sich um eine Literalzeichenfolge. Dieser Inhalt ist als  **Text in Fettdruck** dargestellt.
   
 ### Beispiel
   
 Bei einer Untersuchung des Codes von `service.sh` können Sie feststellen, dass das Script diese und weitere Konfigurationsvariablen einsetzt, um sein Verhalten zu steuern. Die Variable **PUBLISH** steuert, ob der Code versucht, Nachrichten an IBM Event Streams zu senden. Die Variable **MOCK** steuert, ob das Script 'service.sh' versucht, Kontakt zu den REST-APIs und ihren abhängigen Services ('cpu' und 'gps') aufzunehmen, oder ob das Script `service.sh` Pseudodaten erzeugt.
  
