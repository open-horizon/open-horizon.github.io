# Configuring a storage class

## StorageClass attribute

A PersistentVolumeClaim will be created during the agent install process. It will be used by agent to store data for agent and cronjob. The storageclass must satisfy the following requirements:

- Supports both read and write
- Can be made available immediately
