1. Changing the name from Platform 2.0 to Thinkrd365

The project was started intially with 3 environment (dev, preprod, prod) with branchs (develop, preprod and main). The project is hosted in azure cloud all the resources are hosted in single directory using Azure intra ID (for internal organisation ). The azure cloud is maintaining by the client side they created an subscription and created a group and gave contributor, Key Vault Administrator and User Access Administrator access. use to raise jira ticket to get the requesting service principle, create Azure ADB2C directories (dev, uat,prod) their DNS records, Add Users to Azure AD Group, Email Accounts Setup.

- mean while team leader proposed an new environment (qa) with branch uat for testing. so created resources in Azure intra ID (for internal organisation ) and Azure ADB2C directories. so totally 4 branchs and 4 environemnts

But the name of project is changed from platform 2.0 to thikrd365 inorder to sale the product the client and the technical officer asked to change the naming convenction also we explained 
Subject: Proposal to Update Domain Name for UAT Environment
Updating the domain name for our UAT environment from "https://platform20-uat.certainti.ai" to "https://thinkrd365-uat.certainti.ai" (Option A) to align with minimize disruption. Below are the details of the proposed approach and a comparison with an alternative option.

Option A: Change Domain Name 
- Action Plan:
  1. Redeploy Terraform code without modifying existing resources to update the domain name.
  2. Obtain an SSL certificate for the new URL on the VM side.
- Benefits:
  - Preserves all existing resources and data.
  - Minimal operational impact with straightforward implementation.

Option B: Full Rename from platform20 to thinkrd365
- Implications:
  - Renaming resources (e.g., from uat-platform20-rg to uat-thinkrd365-rg) will recreate them, leading to data loss.
  - Additional tasks include:
    1. Recreating resources (listed below).
    2. Recreating B2C credentials.
    3. Updating Azure Key Vault.
    4. Obtaining an SSL certificate for the new URL on the VM side.
- Affected Resources in uat-platform20-rg:
  - uat-platform20-api-management
  - uat-platform20-dce
  - uat-platform20-dcr
  - uat-platform20-keyvault
  - uat-platform20-law
  - uat-platform20-psqlserver-centralus-main
  - uat-platform20-psqlserver-centralus-org
  - uat-platform20-staticwebapp
  - uat-platform20-vm-backend
  - uat-platform20-vm-backend_OsDisk_1_2ed5d40c4ccb48d7b3fd199725714d90
  - uat-platform20-vm-etl
  - uat-platform20-vm-etl_OsDisk_1_b715b564cf204ecd8760969389de2e88
  - uat-platform20-vm-nic-backend
  - uat-platform20-vm-nic-etl
  - uat-platform20-vm-nic-redis
  - uat-platform20-vm-pub-ip-backend
  - uat-platform20-vm-pub-ip-etl
  - uat-platform20-vm-pub-ip-redis
  - uat-platform20-vm-redis
  - uat-platform20-vm-redis_OsDisk_1_43cdf78808de492792f5d0a7e631c409
  - uat-platform20-vm-sg-backend
  - uat-platform20-vm-sg-etl
  - uat-platform20-vm-sg-redis
  - uat-platform20-vnet
  - uatplatform20registry
  - uatplatform20stor
- Drawbacks:
  - High risk of data loss and service disruption.
  - Significant effort required for reconfiguration.

Please let me know if you need further details or wish to discuss the implementation plan.
but client has choosen option B

Team leader also proposed during migration he need history of commits
so i proposed 4 branchs and 6 environments
1. develop branch with old environment (dev) and new environment (development)
2. uat branch with old environment (uat) and new environment (qa)
3. prepord branch with old environment preprod
4. main branch with old environment prod

so i creafully created and migrated 
- from dev environment to development environment and
- form uat environment to qa environment

so now i know it is 4 branchs and 4 environement will past commits of dev and uat environments