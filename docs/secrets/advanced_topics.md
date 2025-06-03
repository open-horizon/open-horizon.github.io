---
copyright: Contributors to the Open Horizon project
years: 2021 - 2025
title: Advanced Topics
description: Advanced topics and considerations for secrets management in Open Horizon
lastupdated: 2025-06-03
nav_order: 3
parent: Secrets Management
grand_parent: Developing edge services
---

{:new_window: target="blank"}
{:shortdesc: .shortdesc}
{:screen: .screen}
{:codeblock: .codeblock}
{:pre: .pre}

# Advanced Topics
{: #advanced_topics}

This guide covers advanced topics and considerations for secrets management in Open Horizon.

## Security considerations
{: #security_considerations}

To manage secrets securely, you must consider the storage, access control, and transmission of the secrets.

### Secret storage
- Secrets are stored in OpenBao or HashiCorp Vault using the KV V2 secrets engine.
- All secrets are encrypted at rest.
- Access is controlled through OpenBao or Vault ACLs.
- Secrets are isolated organization.

### Access control
- Organization admins have full control over organization-wide secrets.
- Users can only access their own private secrets.
- The agbot component has read-only access to secrets.
- Exchange root users have no direct access to secrets.

### Secret transmission
- Secrets are transmitted securely between components.
- Secrets are only sent to nodes that need them.
- Secret updates are sent through secure channels.
- All secret operations are logged.

## Performance implications
{: #performance}

Several secrets-related activities may impact application performance.  Here are the three main areas to consider.

### Secret updates
- Secret updates trigger agreement updates.
- Multiple secret updates can be batched.
- Services should handle updates gracefully.
- Consider update frequency and impact.

### Storage considerations
- OpenBao or Vault performance can be affected by:
  - Number of secrets
  - Secret size
  - Update frequency
  - Access patterns

### Network impact
- Secret updates require network communication.
- Consider network bandwidth and latency.
- Plan for offline scenarios.
- Implement proper retry mechanisms.

## Migration strategies
{: #migration}

As an application is migrated to a secrets management solution, consider the following steps during the initial move and during application version upgrades.

### Moving to secrets management
1. **Assessment**
   - Identify current secret storage
   - Map secret usage
   - Plan migration order

2. **Preparation**
   - Set up secrets manager
   - Configure access controls
   - Create backup strategy

3. **Migration**
   - Create new secrets
   - Update service definitions
   - Test in staging
   - Roll out gradually

4. **Verification**
   - Verify secret access
   - Test updates
   - Monitor performance
   - Clean up old storage

### Version upgrades
- Plan for backward compatibility
- Test with new versions
- Have rollback plan
- Update documentation

## Troubleshooting
{: #advanced_troubleshooting}

When tracking down the source of problems, here are some areas to look and some tools to use.

### Common issues
1. **Secret access problems**
   - Check OpenBao or Vault logs
   - Verify ACLs
   - Check network connectivity
   - Verify authentication

2. **Update failures**
   - Check agreement status
   - Verify service configuration
   - Check network connectivity
   - Review service logs

3. **Performance issues**
   - Monitor OpenBao or Vault metrics
   - Check network latency
   - Review access patterns
   - Consider caching

### Debugging tools
```bash
# Check secret status
hzn secretsmanager secret list

# View Vault logs
journalctl -u vault

# Check service logs
hzn service log -f <service>

# Monitor network
tcpdump -i any port 8200
```

## Best practices
{: #advanced_best_practices}

The following are some practices to consider as you use secrets management categorized by role.

### Security
1. **Secret management**
   - Rotate secrets regularly
   - Use strong encryption
   - Implement proper access controls
   - Monitor access patterns

2. **Service design**
   - Minimize secret usage
   - Implement proper error handling
   - Use secure communication
   - Follow principle of least privilege

### Operations
1. **Monitoring**
   - Track secret usage
   - Monitor update frequency
   - Watch for failed updates
   - Track access patterns

2. **Maintenance**
   - Regular backups
   - Performance optimization
   - Clean up unused secrets
   - Update operations documentation for each code change

### Development
1. **Testing**
   - Test all secret operations
   - Verify update handling
   - Check error scenarios
   - Test performance

2. **Documentation**
   - Document purpose and valid values
   - Update procedures
   - Troubleshooting guides
   - Security considerations 