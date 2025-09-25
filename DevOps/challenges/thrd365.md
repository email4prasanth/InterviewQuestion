# Project Migration and Rename from Platform 2.0 to Thinkrd365

## 1. Context and Challenge
The project was originally named **Platform 2.0**, with 3 environments (dev, preprod, prod) and 3 branches. During the project lifecycle, we faced two major challenges simultaneously:

- Expanding the testing environment (**QA**).  
- Full renaming of the project to **Thinkrd365** to align with client’s commercial strategy.

Both tasks had **high operational risk** and required careful planning to **preserve commit history** and avoid **data loss**.

---
## 2. Technical Complexity
The complexity of the task included:
-  The project is hosted in azure cloud all the resources are hosted in single directory using Azure intra ID (for internal organisation ). The azure cloud is maintaining by the client side they created an subscription and created a group and gave contributor, Key Vault Administrator and User Access Administrator access. Use to raise jira ticket to get the requesting service principle, create Azure ADB2C directories (dev, uat,prod) their DNS records, Add Users to Azure AD Group, Email Accounts Setup.
- **Full rename of Azure resources** (VMs, Key Vaults, SQL servers, APIs, Static Web Apps, VNet, etc.), which carried high risk for **data loss and service disruption**.  
- **Migration while preserving Git commit history** across multiple branches:  
  - dev → development  
  - uat → QA  
- Integration with **Azure AD B2C directories** for new environments.  
- Managing **SSL certificates, DNS updates, and Key Vault reconfigurations** for each renamed resource.

---
## 3. Client and Team Requirements
- Followed **client directive** to use full rename despite higher operational risk. 
- Drawbacks:
  - High risk of data loss and service disruption.
  - Significant effort required for reconfiguration 
- Addressed **team leader requirement** to preserve commit history.  
- Ensured **minimal disruption** to other environments (preprod, prod).

## 4. Solution Approach
- **Created a migration plan** with 4 branches and 6 environments to align old and new resources.
1. develop branch with old environment (dev) and new environment (development)
2. uat branch with old environment (uat) and new environment (qa)
3. prepord branch with old environment preprod
4. main branch with old environment prod  
- **Stepwise migration**:  
  - dev → development  
  - uat → QA  
- **Terraform redeployment** to apply renaming without losing existing resources wherever possible.  
- **Coordinated with client** for Azure AD B2C, SSL, and DNS updates.  
- **Verified commit history** to maintain code traceability.

---
## 5. Outcome / Result
- Successfully migrated all environments with **full rename completed**.  
- **Preserved commit history** for dev and uat branches.  
- Met **both client and team leader requirements** with minimal disruption.  
- Demonstrated ability to **handle complex, multi-stakeholder DevOps projects**.

---

so now i know it is 4 branchs and 4 environement will past commits of dev and uat environments

---
concise, resume-friendly Markdown version highlighting your DevOps
### DevOps Engineer | Project: Platform 2.0 → Thinkrd365

- Led **full Azure resource rename and migration** from Platform 2.0 to Thinkrd365, including VMs, Key Vaults, SQL servers, APIs, Static Web Apps, and VNets.  
- Designed and executed **branch/environment strategy** to preserve Git commit history while creating new environments (development, QA) alongside existing ones (preprod, prod).  
- Coordinated with client and internal teams for **Azure AD B2C integration, DNS updates, SSL certificates, and Key Vault reconfigurations**.  
- Implemented migration using **Terraform** to minimize operational risk and avoid data loss.  
- Successfully balanced **client requirements and team objectives**, ensuring minimal disruption to production systems.  
- Demonstrated ability to handle **complex, multi-stakeholder DevOps projects** with strategic planning and risk mitigation.
