
# 🛠️ RDS Migration Challenge – Public to Private Subnet Architecture
- AMLY is an internal project for ogranisation employee purpose like time off, goals , leaves, benifits... even if it public they ignored since there is a trade off between cost and security.
- It is developed from 2 years with full potential, Higher authority proposed to convert it into business for sale, so they consider security is high priority they assigned the task to me, as joined recently, because the other devops engineer relocated to another organisation.
## 📌 Context
- Project: **amly** (AWS-hosted, deployed via Bitbucket CI/CD & CloudFormation).
- Backend: **Lambda**, Frontend: **CloudFront**, Database: **RDS** (initially public).
- Initially, RDS was in **public subnets**, accessible over the internet with credentials.
- This was acceptable for internal use, but when the product was proposed for **commercialization**, **security became critical**.
- Requirement: **Eliminate public DB exposure**, ensure secure access, and **optimize costs**.

---

## ⚡ Challenges
- Migrate RDS to **private subnets** with **minimal downtime**.
- Ensure **Lambdas and API Gateway** can still communicate with RDS securely.
- Provide **secure DB access** for developers/admins.
- Balance **security vs cost** (trade-off between VPC Endpoints and NAT Gateway).
- Implement everything as **Infrastructure-as-Code** (CloudFormation, serverless.yml).

---

## 🔧 Solution
1. **Migrated RDS to Private Subnets**
   - Created private subnet group (`amly-prod-pvt-sg`) inside VPC.
   - Restored snapshot of public DB into private subnet group.
   - Restricted security groups → only Lambdas can access port 3306.

2. **VPC Endpoints for AWS Services**
   - **S3 Gateway Endpoint** → backups, file access.
   - **SES Interface Endpoint** → email sending.
   - Allowed AWS service access **without public internet/NAT**.

3. **Lambda & API Gateway Integration**
   - Lambdas deployed in private subnets alongside RDS.
   - API Gateway → Lambda (IAM auth) → RDS (secure comms).

```sh
User → API Gateway → Lambda (private subnet) → RDS (private subnet)
│
├── S3 (via Gateway Endpoint)
└── SES (via Interface Endpoint)
```

4. **Bastion Host for Admin Access**
- Deployed EC2 in public subnet as a **jump server**.
- Configured SSH via `.pem` key.
- Installed MySQL client to securely connect to private RDS.

5. **Cost Optimization**
- Heavy AWS traffic routed via **VPC Endpoints (~$30/mo)**.
- External traffic via **NAT Gateway (~$32/mo + transfer)**.
- Reduced NAT usage → optimized costs.

6. **Infrastructure-as-Code**
- Automated setup using **CloudFormation & serverless.yml**.
- Deployment via **Bitbucket CI/CD**.

---

## ✅ Outcomes
- 🚫 **Public RDS exposure eliminated**.  
- 🔐 **Secure Lambda → RDS integration** with controlled access.  
- 🔑 **Developer/admin access via Bastion Host**.  
- 💰 **Optimized costs** by offloading AWS service traffic to VPC Endpoints.  
- ⚙️ **Fully automated, production-ready, scalable architecture**.  

---

## 📄 Resume Highlight
- Led migration of RDS from **public to private subnets**, eliminating public exposure and strengthening security posture for a product transitioning to commercialization.  
- Designed secure VPC architecture with **Lambda–API Gateway–RDS integration**, **Bastion Host for admin access**, and **VPC Endpoints for S3/SES**, reducing NAT traffic costs by ~40%.  
- Automated infrastructure using **CloudFormation & Bitbucket CI/CD pipelines**, ensuring repeatability and zero-downtime migration.  

---

## 🎤 Interview Story (STAR Method)
- **Situation**: RDS was publicly exposed due to cost trade-offs; commercialization required hardened security.  
- **Task**: Migrate DB into private subnets, ensure secure access, minimize downtime, optimize costs.  
- **Action**: Designed new VPC architecture, introduced Bastion Host, VPC Endpoints, optimized NAT usage, automated via IaC.  
- **Result**: Removed public exposure, achieved secure & scalable architecture, reduced costs, and delivered production-ready setup.
## Related links
- https://github.com/email4prasanth/Access_Service/blob/master/Database/rds_pvt.md





