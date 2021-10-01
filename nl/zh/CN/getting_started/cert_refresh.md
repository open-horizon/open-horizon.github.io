---

copyright:
  years: 2021
lastupdated: "2021-02-09"

---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}
{:child: .link .ulchildlink}
{:childlinks: .ullinks}

# 证书刷新
{: #certrefresh}

作为 {{site.data.keyword.ieam}} 安装的一部分，在缺省情况下创建并使用证书，有效期为 90 天。 此过程将指导您为 Common Services、{{site.data.keyword.ieam}} 中心和您的 {{site.data.keyword.ieam}} 节点刷新 CA 证书。

您必须为此刷新完成三个任务：
1. 以管理员身份在集群上生成新证书以与您的边缘节点所有者共享。
2. 提供证书，与边缘节点所有者交流以下边缘节点指示信息以警告他们必须将这个新证书应用于每个边缘节点。
3. 以管理员身份在集群上刷新 Kubernetes 资源以将新证书应用于所有必需位置。

**注**：如果到期日期是初始安装后 90 天，那么您的边缘节点将继续运行直至到期日期。 连续执行这三个任务将对边缘节点所有者有益，使其能够预信任新证书，从而在最大程度上减少通信中断。 如果到期日期已过，那么您的边缘节点目前无法与 IEAM 中心通信。 在这种情况下，您可以并行完成**任务 2** 和**任务 3**。

## 任务 1：生成新证书
{: #task1}
1. 以集群管理员身份登录已安装 {{site.data.keyword.ieam}} 中心的集群，并检查现有证书上的到期日期：
   ```
   echo "$(oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode)" | openssl x509 -text -noout | grep -A 2 Validity
   ```
   {: codeblock}


2. 在进行更改前，验证证书管理器 API Webhook 的状态：
   ```
   oc describe apiservice v1beta1.webhook.certmanager.k8s.io
   ```
   {: codeblock}

   ```
   Status:
     Conditions:
       Last Transition Time:  2021-02-08T19:12:06Z
       Message:               all checks passed
       Reason:                Passed
       Status:                True
       Type:                  Available
   ```

   如果状态不匹配，请运行这些命令以刷新密钥证书管理器服务：
   ```
   oc delete apiservice v1beta1.webhook.certmanager.k8s.io;
   oc delete pod -l name=ibm-common-service-operator -n ibm-common-services;
   oc delete pod -l app=ibm-cert-manager-webhook -n ibm-common-services
   ```
   {: codeblock}

   验证证书管理器状态（可能需要花费一分钟进行传播）：
   ```
   oc describe apiservice v1beta1.webhook.certmanager.k8s.io
   ```
   {: codeblock}

3. 更新要应用于下一个证书的到期日期。 此示例将创建有效期 2 年的证书，此有效期在到期日期前 10 天自动更新：
   ```
   oc patch certificate cs-ca-certificate --type=merge --patch '{"spec": {"duration": "17520h","renewBefore": "240h"}}' -n ibm-common-services
   ```
   {: codeblock}

4. 删除当前证书密钥：
   ```
   oc delete secret cs-ca-certificate-secret -n ibm-common-services
   ```
   {: codeblock}

5. 验证新证书上更新的到期日期：
   ```
   oc describe certificate cs-ca-certificate -n ibm-common-services
   ```
   {: codeblock}

6. 将新证书导出到文件：
   ```
   oc get secret cs-ca-certificate-secret -o jsonpath="{.data['ca\.crt']}" -n ibm-common-services | base64 --decode > /tmp/cs-ca.crt
   ```
   {: codeblock}

   将通信发送给拥有边缘节点的任何用户，日期为想要执行**任务 3** 中的指示信息、此证书文件以及[任务 2](cert_refresh.md#task2) 指示信息的直接链接以允许最终用户在应用这个新证书前先预信任的时间。

   **注**：与 `cloudctl` CLI 通信的 API 服务立即应用这个新证书。 虽然在实时集群上执行此更改后似乎没有通信问题，但是在此阶段重新引导此集群的确会导致边缘节点发生认证问题并损坏 `cloudctl login` 功能（`oc login` 保持运行）。 通信将在完成**任务 3** 中的步骤后完全复原。

## 任务 2：将新证书应用于边缘节点
{: #task2}
### 对于边缘设备
1. 登录主机并手动连接位于证书文件末尾的新证书或运行以下命令（将 <DEVICE_HOST> 替换为您的节点主机名或 IP，并将 <CA_CERT_FILE> 替换为您给定的证书文件位置）：
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; echo -e '$(cat <CA_CERT_FILE>)' >> \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

2. 验证证书是否有两个证书条目：
   ```
   ssh root@<DEVICE_HOST> "source /etc/default/horizon; cat \$HZN_MGMT_HUB_CERT_PATH"
   ```
   {: codeblock}

### 对于边缘集群
1. 登录正在运行代理程序 POD 的名称空间，将现有证书添加到您给定的 **cs-ca.crt** 文件（将 <CA_CERT_FILE> 替换为您给定的包含新证书的文件位置）：
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode >> <CA_CERT_FILE>
   ```
   {: codeblock}

2. 验证证书文件是否有两个证书条目：
   ```
   cat <CA_CERT_FILE>
   ```
   {: codeblock}

3. 修补密钥值以从该文件添加新证书（替换 <CA_CERT_FILE>）：
   ```
   oc patch secret openhorizon-agent-secrets --type=merge --patch '{"data": {"agent-install.crt": "'$(cat <CA_CERT_FILE> | base64)'"}}'
   ```
   {: codeblock}

4. 验证密钥是否有两个证书条目：
   ```
   oc get secret openhorizon-agent-secrets -o jsonpath="{.data['agent-install\.crt']}" | base64 --decode
   ```
   {: codeblock}

5. 重新启动 {{site.data.keyword.ieam}} 代理程序 pod：
   ```
   oc delete pod $(oc get pods | grep 'agent-' | awk '{print $1}')
   ```
   {: codeblock}

现在您的边缘节点准备好在启用新证书后对其进行信任。

## 任务 3：刷新 Kubernetes 资源以应用新证书
{: #task3}
如果证书尚未到期，您可以等待执行这些步骤，直到所有期望的边缘节点已添加新证书。 如果证书已到期，请继续执行这些步骤，而不是等待边缘节点所有者。

**注**：可能存在一段短暂的 API 认证停机时间（少于 1 分钟）。 在这段时间内，现有边缘节点工作负载将继续运行，但是利用 API 密钥进行认证的任何 `hzn` CLI 命令将不运行，直到 **auth** pod 已重新启动。

1. 刷新叶证书：
   ```
   mkdir secret_backup;
   cd secret_backup;
   ```
   {: codeblock}

   ```
   oc get certs -o custom-columns=:spec.secretName,:spec.issuerRef.name --no-headers -n ibm-common-services |egrep "cs-ca-clusterissuer|cs-ca-issuer" | while read secretName issuerName
   do
     oc get secret $secretName -o yaml -n ibm-common-services > secret.$secretName.yaml
     oc delete secret $secretName -n ibm-common-services
   done
   ```
   {: codeblock}

2. 刷新认证 pod（此时认证短暂停机）
   ```
   oc delete pod -l app=auth-idp -n ibm-common-services;
   oc delete pod -l app=auth-pap -n ibm-common-services;
   oc delete pod -l app=auth-pdp -n ibm-common-services
   ```
   {: codeblock}

3. 删除以下密钥和路由：
   ```
   oc  delete secret ibmcloud-cluster-ca-cert -n ibm-common-services;
   oc delete route cp-console -n ibm-common-services
   ```
   {: codeblock}

4. 刷新以下 pod 以更新 management-ingress-ibmcloud-cluster-ca-cert 密钥：
   ```
   oc delete pod -l name=operand-deployment-lifecycle-manager -n ibm-common-services
   ```
   {: codeblock}

5. 验证边缘名称空间中的密钥是否已更新（可能需要花费一分钟进行传播）：
   ```
   oc get secret management-ingress-ibmcloud-cluster-ca-cert -o jsonpath="{.data['ca\.crt']}" -n ibm-edge | base64 --decode
   ```
   {: codeblock}

6. 刷新 {{site.data.keyword.ieam}} Exchange 和 SDO pod（这会导致短暂的 {{site.data.keyword.ieam}} 通信停运）：
   ```
   oc delete pod -l app.kubernetes.io/component=exchange -n ibm-edge
   oc delete pod -l app.kubernetes.io/component=sdo -n ibm-edge
   ```
   {: codeblock}

7. 使用新证书刷新 CSS 安装工件；这将确保未来的边缘节点安装信任新证书：
   ```
   echo '{"objectID": "agent-install.crt","objectType": "agent_files","destinationOrgID": "IBM","version": "","public": true}' > /tmp/agent-cert-mms.json
   hzn mms -o IBM object publish -m /tmp/agent-cert-mms.json -f /tmp/cs-ca.crt
   ```
   {: codeblock}
