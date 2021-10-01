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

# Multi-Tenant-Funktionalität
{: #multit}

## Tenants in {{site.data.keyword.edge_notm}}
{: #tenants}

{{site.data.keyword.edge_notm}} ({{site.data.keyword.ieam}}) unterstützt das allgemeine IT-Konzept der Multi-Tenant-Funktionalität in Form von Organisationen, wobei jeder Tenant eine eigene Organisation besitzt. Organisationen dienen der Aufteilung von Ressourcen. Benutzer in einer Organisation können daher keine Ressourcen in einer anderen Organisation erstellen oder ändern. Darüber hinaus können Ressourcen in einer Organisation nur von Benutzern in dieser Organisation angezeigt werden, es sei denn, die Ressourcen sind als 'Öffentlich' markiert.

### Allgemeine Anwendungsfälle

Zur Nutzung der Multi-Tenant-Funktionalität in {{site.data.keyword.ieam}} werden zwei gängige Anwendungsfälle verwendet:

* Ein Unternehmen umfasst mehrere Geschäftsbereiche, die jeweils eine separate Organisation in demselben {{site.data.keyword.ieam}}-Management-Hub bilden. Hierbei gibt es rechtliche, geschäftliche oder technische Gründe dafür, dass die einzelnen Geschäftsbereiche jeweils eine separate Organisation mit einer eigenen Gruppe von {{site.data.keyword.ieam}}-Ressourcen darstellen sollen, auf die die anderen Geschäftsbereiche standardmäßig keinen Zugriff haben. Das Unternehmen hat auch bei separaten Organisationen die Möglichkeit, eine gemeinsame Gruppe von Organisationsadministratoren für die Verwaltung aller Organisationen einzusetzen.
* Ein Unternehmen hostet {{site.data.keyword.ieam}} als Service für seine Kunden, wobei es für jeden Kunden im Management-Hub mindestens eine Organisation gibt. In diesem Fall verfügt jeder Kunde über individuelle Organisationsadministratoren.

Der von Ihnen ausgewählte Anwendungsfall bestimmt, wie Sie {{site.data.keyword.ieam}} und Identity and Access Manager ([IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/landing_iam.html)) konfigurieren.

### Typen von {{site.data.keyword.ieam}}-Benutzern
{: #user-types}

{{site.data.keyword.ieam}} unterstützt die folgenden Benutzerrollen:

| **Rolle** | **Zugriff** |
|--------------|-----------------|
| **Hubadministrator** | Verwaltet die Liste der {{site.data.keyword.ieam}}-Organisationen durch das Erstellen, Ändern und Löschen von Organisationen nach Bedarf und durch die Erstellung von Organisationsadministratoren in jeder Organisation. |
| **Organisationsadministrator** | Verwaltet die Ressourcen in einzelnen oder mehreren {{site.data.keyword.ieam}}-Organisationen. Organisationsadministratoren können alle Ressourcen (Benutzer, Knoten, Service, Richtlinie oder Muster) innerhalb der Organisation erstellen, anzeigen oder ändern, auch wenn sie nicht der Eigner der Ressource sind. |
| **Regulärer Benutzer** | Erstellt Knoten, Services, Richtlinien und Muster innerhalb der Organisation und ändert oder löscht die Ressourcen, die er erstellt hat. Zeigt alle Services, Richtlinien und Muster in der Organisation an, die von anderen Benutzern erstellt wurden. |
{: caption="Tabelle 1. {{site.data.keyword.ieam}}-Benutzerrollen" caption-side="top"}

Der Abschnitt [Rollenbasierte Zugriffssteuerung](../user_management/rbac.md) enthält Beschreibungen aller {{site.data.keyword.ieam}}-Rollen.

## Beziehung zwischen IAM und {{site.data.keyword.ieam}}
{: #iam-to-ieam}

Der IAM-Service (IAM - Identity and Access Manager) verwaltet Benutzer für alle Cloud Pak-basierten Produkte, einschließlich {{site.data.keyword.ieam}}. IAM wiederum verwendet LDAP, um die Benutzer zu speichern. Jeder IAM-Benutzer kann Mitglied einzelner oder mehrerer IAM-Teams sein. Da jedes IAM-Team einem IAM-Konto zugeordnet ist, kann ein IAM-Benutzer indirekt Mitglied einzelner oder mehrerer IAM-Konten sein. Weitere Details finden Sie unter [Multi-Tenant-Funktionalität in IAM](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/multitenancy/multitenancy.html).

{{site.data.keyword.ieam}} Exchange stellt Authentifizierungs- und Berechtigungsservices für andere {{site.data.keyword.ieam}}-Komponenten bereit. Exchange delegiert die Authentifizierung von Benutzern an IAM. Dies bedeutet, dass die IAM-Benutzerberechtigungsnachweise an Exchange übergeben werden und dass die Ermittlung ihrer Gültigkeit von IAM durchgeführt wird. Jede Benutzerrolle (Hubadministrator, Organisationsadministrator oder regulärer Benutzer) ist in Exchange definiert. Auf diese Weise werden die Aktionen festgelegt, die Benutzer in {{site.data.keyword.ieam}} ausführen dürfen.

Jede Organisation in {{site.data.keyword.ieam}} Exchange ist einem IAM-Konto zugeordnet. Daher sind IAM-Benutzer in einem IAM-Konto automatisch Mitglieder der entsprechenden {{site.data.keyword.ieam}}-Organisation. Die einzige Ausnahme von dieser Regel besteht darin, dass die Rolle des {{site.data.keyword.ieam}}-Hubadministrators in Bezug auf Organisationen als externe Rolle eingestuft wird. Daher ist es nicht relevant, zu welchem IAM-Konto der IAM-Benutzer mit Hubadministratorberechtigung gehört.

Die Zuordnung zwischen IAM und {{site.data.keyword.ieam}} kann wie folgt zusammengefasst werden:

| **IAM** | **Beziehung** | **{{site.data.keyword.ieam}}** |
|--------------|----------|-----------------|
| IAM-Konto | wird zugeordnet zu | {{site.data.keyword.ieam}}-Organisation |
| IAM-Benutzer | wird zugeordnet zu | {{site.data.keyword.ieam}}-Benutzer |
| Für die Rolle ist keine IAM-Entsprechung vorhanden | Keine | {{site.data.keyword.ieam}}-Rolle |
{: caption="Tabelle 2. Zuordnung zwischen IAM und {{site.data.keyword.ieam}}" caption-side="top"}

Die Berechtigungsnachweise, die für die Anmeldung an der {{site.data.keyword.ieam}}-Konsole verwendet werden, sind der IAM-Benutzer und das zugehörige Kennwort. Als Berechtigungsnachweis für die {{site.data.keyword.ieam}}-Befehlszeilenschnittstelle (`hzn`) wird ein IAM-API-Schlüssel verwendet.

## Ausgangsorganisation
{: #initial-org}

Eine Organisation wurde standardmäßig während der {{site.data.keyword.ieam}}-Installation mit einem von Ihnen vergebenen Namen erstellt. Wenn Sie die Multi-Tenant-Funktionalität von {{site.data.keyword.ieam}} nicht benötigen, reicht diese Ausgangsorganisation für Ihre Verwendung von {{site.data.keyword.ieam}} aus und Sie können den Rest dieser Seite überspringen.

## Benutzer als Hubadministrator erstellen
{: #create-hub-admin}

Der erste Schritt zur Verwendung der Multi-Tenant-Funktionalität von {{site.data.keyword.ieam}} ist die Erstellung mindestens eines Hubadministrators, der die Organisationen erstellen und verwalten kann. Zuvor müssen Sie jedoch ein IAM-Konto und einen Benutzer erstellen oder auswählen, denen die Hubadministratorrolle zugeordnet werden kann.

1. Verwenden Sie die Befehlszeilenschnittstelle `cloudctl`, um sich beim {{site.data.keyword.ieam}}-Management-Hub als Clusteradministrator anzumelden. (Wenn Sie `cloudctl` noch nicht installiert haben, lesen Sie die Anweisungen im Abschnitt ['cloudctl', 'kubectl' und 'oc' installieren](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <kennwort> --skip-ssl-validation
   ```
   {: codeblock}

2. Wenn Sie noch keine Verbindung zwischen einer LDAP-Instanz und IAM hergestellt haben, dann führen Sie diesen Schritt jetzt aus. Befolgen Sie dazu die Anweisungen in [Verbindung zum LDAP-Verzeichnis herstellen](https://www.ibm.com/support/knowledgecenter/SSHKN6/iam/3.x.x/configure_ldap.html).

3. Der Benutzer mit Hubadministratorberechtigung muss sich in einem IAM-Konto befinden. (Dabei spielt es keine Rolle, welches Konto verwendet wird.) Wenn Sie nicht bereits über ein IAM-Konto verfügen, dem Sie den Benutzer mit Hubadministratorberechtigung hinzufügen möchten, erstellen Sie ein entsprechendes Konto:

   ```bash
   IAM_ACCOUNT_NAME='hub admin account'   # or choose another name    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d 'account for the hub admin users'    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

4. Erstellen Sie einen LDAP-Benutzer, dem die Rolle des {{site.data.keyword.ieam}}-Hubadministrators zugeordnet werden soll, oder wählen Sie einen bereits vorhandenen LDAP-Benutzer aus. Verwenden Sie nicht denselben Benutzer als {{site.data.keyword.ieam}}-Hubadministrator und {{site.data.keyword.ieam}}-Organisationsadministrator (oder regulären {{site.data.keyword.ieam}}-Benutzer).

5. Importieren Sie den Benutzer in IAM:

   ```bash
   HUB_ADMIN_USER=<IAM/LDAP-benutzername_des_benutzers_mit_hubadministratorberechtigung>    cloudctl iam user-import -u $HUB_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $HUB_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

6. Weisen Sie dem IAM-Benutzer die Rolle des Hubadministrators zu:

   ```bash
   EXCHANGE_ROOT_PW=<kennwort_für_exchange-rootbenutzer>    export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/root:$EXCHANGE_ROOT_PW    export HZN_EXCHANGE_URL=<url_für_exchange>    hzn exchange user create -H $HUB_ADMIN_USER ""
   ```
   {: codeblock}

7. Überprüfen Sie, ob dem Benutzer die Rolle des Hubadministrators zugeordnet ist. In der Ausgabe des folgenden Befehls muss `"hubAdmin": true` angegeben sein.

   ```bash
   hzn exchange user list $HUB_ADMIN_USER
   ```
   {: codeblock}

### Benutzer mit Hubadministratorberechtigung über {{site.data.keyword.ieam}}-Befehlszeilenschnittstelle verwenden
{: #verify-hub-admin}

Erstellen Sie einen API-Schlüssel für den Benutzer mit Hubadministratorberechtigung und überprüfen Sie, ob er über die Funktionalität für den Hubadministrator verfügt:

1. Verwenden Sie die Befehlszeilenschnittstelle `cloudctl`, um sich beim {{site.data.keyword.ieam}}-Management-Hub als Hubadministrator anzumelden:

   ```bash
   cloudctl login -a <cluster-url> -u $HUB_ADMIN_USER -p <hubadministratorkennwort> -c $IAM_ACCOUNT_ID --skip-ssl-validation
   ```
   {: codeblock}

2. Erstellen Sie für den Benutzer mit Hubadministratorberechtigung einen API-Schlüssel:

   ```bash
   cloudctl iam api-key-create "${HUB_ADMIN_USER}-api-key" -d "API key for $HUB_ADMIN_USER"
   ```
   {: codeblock}

   Suchen Sie den API-Schlüsselwert in der Befehlsausgabezeile, die mit **API Key** beginnt. Speichern Sie den Schlüsselwert zur zukünftigen Verwendung an einem sicheren Ort, da Sie ihn später nicht mehr aus dem System abfragen können. Legen Sie diesen Wert außerdem für nachfolgende Befehle in dieser Variablen fest:

   ```bash
   HUB_ADMIN_API_KEY=<soeben_erstellter_iam-api-schlüssel>
   ```
   {: codeblock}

3. Zeigen Sie alle Organisationen im Management-Hub an. Daraufhin werden die während der Installation erstellte Ausgangsorganisation sowie die Organisationen **root** und **IBM** angezeigt:

   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    hzn exchange org list -o root
   ```
   {: codeblock}

4. Melden Sie sich bei der [{{site.data.keyword.ieam}}-Managementkonsole](../console/accessing_ui.md) als der IAM-Benutzer mit Hubadministratorberechtigung und mit dem zugehörigen Kennwort an. Die Organisationsadministrationskonsole wird angezeigt, da Ihre Berechtigungsnachweise für die Anmeldung über die Hubadministratorrolle verfügen. Verwenden Sie diese Konsole, um Organisationen anzuzeigen, zu verwalten und hinzuzufügen. Sie können Organisationen auch über die Befehlszeilenschnittstelle (CLI) hinzufügen. Weitere Informationen hierzu erhalten Sie im folgenden Abschnitt.

## Organisation über CLI erstellen
{: #create-org}

Alternativ zur Erstellung von Organisationen über die {{site.data.keyword.ieam}}-Organisationsadministrationskonsole können Sie Organisationen auch mithilfe der Befehlszeilenschnittstelle (Command Line Interface; CLI) erstellen. Voraussetzung für die Erstellung einer Organisation ist das Erstellen oder Auswählen eines IAM-Kontos, das der Organisation zugeordnet wird. Des Weiteren müssen Sie einen IAM-Benutzer erstellen oder auswählen, dem die Organisationsadministratorrolle zugewiesen wird.

**Hinweis**: Ein Organisationsname darf keine Unterstriche (_), Kommata (,), Leerzeichen (), einfache Anführungszeichen (') oder Fragezeichen (?) enthalten..

Führen Sie die folgenden Schritte aus:

1. Wenn Sie diesen Schritt noch nicht ausgeführt haben, dann erstellen Sie nun einen Benutzer mit Hubadministratorberechtigung. Führen Sie dazu die im vorherigen Abschnitt beschriebenen Schritte aus. Vergewissern Sie sich, dass der API-Schlüssel für den Hubadministrator in der folgenden Variablen festgelegt ist:

   ```bash
   HUB_ADMIN_API_KEY=<iam-api-schlüssel_des_benutzers_mit_hubadministratorberechtigung>
   ```
   {: codeblock}

2. Verwenden Sie die Befehlszeilenschnittstelle `cloudctl`, um sich beim {{site.data.keyword.ieam}}-Management-Hub als Clusteradministrator anzumelden und ein IAM-Konto zu erstellen, dem die neue {{site.data.keyword.ieam}}-Organisation zugeordnet wird. (Wenn Sie `cloudctl` noch nicht installiert haben, lesen Sie die Informationen im Abschnitt ['cloudctl', 'kubectl' und 'oc' installieren](../cli/cloudctl_oc_cli.md).)

   ```bash
   cloudctl login -a <cluster-url> -u admin -p <kennwort> --skip-ssl-validation    NEW_ORG_ID=<name_der_neuen_organisation>    IAM_ACCOUNT_NAME="$NEW_ORG_ID"    cloudctl iam account-create "$IAM_ACCOUNT_NAME" -d "$IAM_ACCOUNT_NAME account"    IAM_ACCOUNT_ID=$(cloudctl iam account "$IAM_ACCOUNT_NAME" | grep -E '^ID' | awk '{print $2}')
   IAM_TEAM_ID=$(cloudctl iam teams -s | grep -m 1 "$IAM_ACCOUNT_NAME" | awk '{print $1}')
   ```
   {: codeblock}

3. Erstellen Sie einen LDAP-Benutzer, dem die Rolle des Organisationsadministrators zugewiesen werden soll, oder wählen Sie einen bereits vorhandenen LDAP-Benutzer aus. Importieren Sie den LDAP-Benutzer anschließend in IAM. Sie können einen Benutzer mit Hubadministratorberechtigung nicht als Benutzer mit Organisationsadministratorberechtigung verwenden, aber Sie können denselben Benutzer mit Organisationsadministratorberechtigung in mehreren IAM-Konten verwenden. Daher können sie mehrere {{site.data.keyword.ieam}}-Organisationen verwalten.

   ```bash
   ORG_ADMIN_USER=<IAM/LDAP-benutzername_des_benutzers_mit_organisationsadministratorberechtigung>    cloudctl iam user-import -u $ORG_ADMIN_USER    cloudctl iam user-onboard $IAM_ACCOUNT_ID -r PRIMARY_OWNER -u $ORG_ADMIN_USER    IAM_RESOURCE_ID=$(cloudctl iam resources | grep ':n/ibm-edge:')
   cloudctl iam resource-add $IAM_TEAM_ID -r $IAM_RESOURCE_ID
   ```
   {: codeblock}

4. Legen Sie die folgenden Umgebungsvariablen fest, erstellen Sie die {{site.data.keyword.ieam}}-Organisation und vergewissern Sie sich, dass die Organisation vorhanden ist:
   ```bash
   export HZN_ORG_ID=root    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$HUB_ADMIN_API_KEY    export HZN_EXCHANGE_URL=<url_für_exchange>    hzn exchange org create -a IBM/agbot -t "cloud_id=$IAM_ACCOUNT_ID" --description "$NEW_ORG_ID organization" $NEW_ORG_ID    hzn exchange agbot addpattern IBM/agbot IBM '*' $NEW_ORG_ID    hzn exchange org list $NEW_ORG_ID
   ```
   {: codeblock}

5. Weisen Sie dem IAM-Benutzer, den Sie zuvor ausgewählt haben, die Rolle des Benutzers mit Organisationsadministratorberechtigung zu und vergewissern Sie sich, dass der Benutzer  in {{site.data.keyword.ieam}} Exchange mit der Rolle des Organisationsadministrators erstellt wurde:

   ```bash
   hzn exchange user create -o $NEW_ORG_ID -A $ORG_ADMIN_USER "" "<e-mail-adresse>"    hzn exchange user list -o $NEW_ORG_ID $ORG_ADMIN_USER
   ```
   {: codeblock}

   In der für den Benutzer ausgegebenen Auflistung muss Folgendes angezeigt werden: `"admin": true`

<div class="note"><span class="notetitle">Anmerkung:</span> Wenn Sie mehrere Organisationen erstellen und denselben Organisationsadministrator für die Verwaltung aller Organisationen wünschen, verwenden Sie für `ORG_ADMIN_USER` jedes Mal denselben Wert über diesen Abschnitt.</div>

Der Organisationsadministrator kann jetzt die [{{site.data.keyword.ieam}}-Managementkonsole](../console/accessing_ui.md) verwenden, um {{site.data.keyword.ieam}}-Ressourcen in dieser Organisation zu verwalten.

### Organisationsadministrator die Verwendung der CLI ermöglichen

Damit ein Organisationsadministrator den Befehl `hzn exchange` verwenden kann, um {{site.data.keyword.ieam}}-Ressourcen über die Befehlszeilenschnittstelle (CLI) zu verwalten, muss er folgende Aktionen ausführen:

1. Befehlszeilenschnittstelle `cloudctl` zur Anmeldung beim {{site.data.keyword.ieam}}-Management-Hub verwenden und einen API-Schlüssel erstellen:

   ```bash
   cloudctl login -a <cluster-url> -u $ORG_ADMIN_USER -p <hubadministratorkennwort> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${ORG_ADMIN_USER}-api-key" -d "API key for $ORG_ADMIN_USER"
   ```
   {: codeblock}

   Suchen Sie den API-Schlüsselwert in der Befehlsausgabezeile, die mit **API Key** beginnt. Speichern Sie den Schlüsselwert zur zukünftigen Verwendung an einem sicheren Ort, da Sie ihn später nicht mehr aus dem System abfragen können. Legen Sie diesen Wert außerdem für nachfolgende Befehle in dieser Variablen fest:

   ```bash
   ORG_ADMIN_API_KEY=<soeben_erstellter_iam-api-schlüssel>
   ```
   {: codeblock}

   **Tipp:** Wenn Sie diesen Benutzer in Zukunft zu weiteren IAM-Konten hinzufügen wollen, müssen Sie nicht für jedes Konto einen API-Schlüssel erstellen. Derselbe API-Schlüssel funktioniert in allen IAM-Konten, dessen Mitglied dieser Benutzer ist, und somit in allen {{site.data.keyword.ieam}}-Organisationen, zu denen dieser Benutzer gehört.

2. Überprüfen Sie mit dem Befehl `hzn exchange`, ob der API-Schlüssel ordnungsgemäß funktioniert:

   ```bash
   export HZN_ORG_ID=<organisations-id>    export HZN_EXCHANGE_USER_AUTH=root/iamapikey:$ORG_ADMIN_API_KEY    hzn exchange user list
   ```
   {: codeblock}


Die neue Organisation ist nun einsatzbereit. Informationen zum Festlegen einer maximalen Anzahl von Edge-Knoten in dieser Organisation oder zum Anpassen der standardmäßigen Heartbeateinstellungen für Edge-Knoten finden Sie unter [Organisationskonfiguration](#org-config).

## Benutzer ohne Administratorberechtigung in einer Organisation
{: #org-users}

Ein neuer Benutzer kann zu einer Organisation hinzugefügt werden, indem der IAM-Benutzer (als `MEMBER`) in das entsprechende IAM-Konto importiert und über ein Onboarding in dieses IAM-Konto aufgenommen wird. Sie müssen den Benutzer nicht explizit zu {{site.data.keyword.ieam}} Exchange hinzufügen, da dieser Schritt bei Bedarf automatisch ausgeführt wird.

Anschließend kann der Benutzer die [{{site.data.keyword.ieam}}-Managementkonsole](../console/accessing_ui.md) verwenden. Damit der Benutzer die Befehlszeilenschnittstelle `hzn exchange` verwenden kann, muss er folgende Aktionen ausführen:

1. Befehlszeilenschnittstelle `cloudctl` zur Anmeldung beim {{site.data.keyword.ieam}}-Management-Hub verwenden und einen API-Schlüssel erstellen:

   ```bash
   IAM_USER=<iam-benutzer>    cloudctl login -a <cluster-url> -u $IAM_USER -p <hubadministratorkennwort> -c $IAM_ACCOUNT_ID --skip-ssl-validation    cloudctl iam api-key-create "${IAM_USER}-api-key" -d "API key for $IAM_USER"
   ```
   {: codeblock}

   Suchen Sie den API-Schlüsselwert in der Befehlsausgabezeile, die mit **API Key** beginnt. Speichern Sie den Schlüsselwert zur zukünftigen Verwendung an einem sicheren Ort, da Sie ihn später nicht mehr aus dem System abfragen können. Legen Sie diesen Wert außerdem für nachfolgende Befehle in dieser Variablen fest:

   ```bash
   IAM_USER_API_KEY=<soeben_erstellter_iam-api-schlüssel>
   ```
   {: codeblock}

3. Legen Sie die folgenden Umgebungsvariablen fest und überprüfen Sie den Benutzer:

```bash
export HZN_ORG_ID=<organisations-id> export HZN_EXCHANGE_USER_AUTH=iamapikey:$IAM_USER_API_KEY hzn exchange user list
```
{: codeblock}

## IBM Organisation
{: #ibm-org}

Die IBM Organisation ist eine individuelle Organisation, die vordefinierte Services und Muster bereitstellt, die als Technologiebeispiele vorgesehen sind und von jedem Benutzer in jeder Organisation verwendet werden können. Die IBM Organisation wird automatisch erstellt, wenn der {{site.data.keyword.ieam}}-Management-Hub installiert wird.

**Hinweis:** Die Ressourcen in der IBM Organisation sind zwar öffentlich, die IBM Organisation ist jedoch nicht dafür vorgesehen, sämtliche öffentlichen Inhalte im {{site.data.keyword.ieam}}-Management-Hub zu speichern.

## Organisationskonfiguration
{: #org-config}

Für jede {{site.data.keyword.ieam}}-Organisation gelten die folgenden Einstellungen. Die Standardwerte für diese Einstellungen sind oft ausreichend. Wenn Sie bestimmte Einstellungen anpassen möchten, führen Sie den Befehl `hzn exchange org update -h` aus, um die Befehlsflags anzuzeigen, die verwendet werden können.

| **Einstellung** | **Beschreibung** |
|--------------|-----------------|
| `description` | Eine Beschreibung der Organisation. |
| `label` | Der Name der Organisation. Dieser Wert wird verwendet, um den Namen der Organisation in der {{site.data.keyword.ieam}}-Managementkonsole anzuzeigen. |
| `heartbeatIntervals` | Diese Einstellung gibt an, wie oft Edge-Knoten-Agenten in der Organisation den Management-Hub auf Anweisungen abfragen. Weitere Details finden Sie im folgenden Abschnitt. |
| `limits` | Die Grenzwerte für diese Organisation. Momentan ist der einzige Grenzwert `maxNodes`. Er gibt die maximale Anzahl der in dieser Organisation zulässigen Edge-Knoten an. Die Anzahl der Edge-Knoten, die von einem einzelnen {{site.data.keyword.ieam}}-Management-Hub unterstützt werden können, ist in der Praxis begrenzt. Mit dieser Einstellung kann der Benutzer mit Hubadministratorberechtigung die Anzahl der Knoten begrenzen, die von jeder Organisation genutzt werden können, wodurch verhindert wird, dass eine einzige Organisation die gesamte Kapazität belegt. Ein Wert von `0` bedeutet, dass keine Begrenzung besteht. |
{: caption="Tabelle 3. Organisationseinstellungen" caption-side="top"}

### Heartbeatabfrageintervall für Agenten
{: #agent-hb}

Der auf jedem Edge-Knoten installierte {{site.data.keyword.ieam}}-Agent sendet in regelmäßigen Zeitabständen Heartbeats an den Management-Hub, um diesem anzuzeigen, dass er weiterhin aktiv und verbunden ist und Anweisungen empfängt. Sie müssen diese Einstellungen nur bei Umgebungen mit extrem hoher Skalierung ändern.

Das Heartbeatintervall ist die Zeit, die der Agent zwischen Heartbeats an den Management-Hub wartet. Das Intervall wird im Laufe der Zeit automatisch angepasst, um die Reaktionsfähigkeit zu optimieren und die Auslastung des Management-Hubs zu reduzieren. Die Intervallanpassung wird durch drei Einstellungen gesteuert:

| **Einstellung** | **Beschreibung**|
|-------------|----------------|
| `minInterval` | Die in Sekunden angegebene kürzeste Wartezeit des Agenten zwischen Heartbeats an den Management-Hub. Sobald ein Agent registriert wurde, beginnt er mit den Abfragen in diesem Intervall. Das Intervall ist nie kleiner als dieser Wert. Ein Wert von `0` bedeutet, dass der Standardwert verwendet wird. |
| `maxInterval` | Die in Sekunden angegebene längste Wartezeit des Agenten zwischen Heartbeats an den Management-Hub. Ein Wert von `0` bedeutet, dass der Standardwert verwendet wird. |
| `intervalAdjustment` | Dies ist die Anzahl der Sekunden, die zum aktuellen Heartbeatintervall hinzugefügt werden sollen, wenn der Agent feststellt, dass er das Intervall vergrößern kann. Nachdem erfolgreich Heartbeats an den Management-Hub gesendet, jedoch seit einiger Zeit keine Anweisungen empfangen wurden, wird das Heartbeatintervall allmählich erhöht, bis der Wert für das maximale Heartbeatintervall erreicht worden ist. Analog wird nach dem Empfang von Anweisungen das Heartbeatintervall herabgesetzt, um sicherzustellen, dass nachfolgende Anweisungen schnell verarbeitet werden. Ein Wert von `0` bedeutet, dass der Standardwert verwendet wird. |
{: caption="Tabelle 4. Einstellungen für 'heartbeatIntervals'" caption-side="top"}

Die Heartbeatintervalleinstellungen in der Organisation werden auf Knoten angewendet, bei denen das Heartbeatintervall nicht explizit konfiguriert ist. Mit dem Befehl `hzn exchange node list <node id>` können Sie prüfen, ob für einen Knoten die Heartbeatintervalleinstellung explizit festgelegt wurde.

Weitere Informationen zum Konfigurieren von Einstellungen in Umgebungen mit hoher Skalierung finden Sie unter [Skalierungskonfiguration](../hub/configuration.md#scale).
