# Updating the agent

If you received updated Open Horizon (Open Horizon) agent packages, you can easily update your edge device:

1. Perform the steps in [Gather the necessary information and files for edge devices](https://open-horizon.github.io/docs/hub/gather_files/#prereq_horizon) to create the updated **agentInstallFiles-<edge-device-type>.tar.gz** file with the newer agent packages.
1. For each edge device, perform the steps in [Automated agent installation and registration](https://open-horizon.github.io/docs/installing/automated_install/#method_one), except that when running the **agent-install.sh** command, specify the service and pattern or policy you want to run on the edge device.
