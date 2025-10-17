# AWS Cost Optimization – RDS & VPC Redesign

## **Problem Statement**
The AWS monthly cost increased significantly, with:  
- **RDS costs up by 172%** due to deploying a new **Multi-AZ db.t4g.medium** instance in production (~$48.48/month).  
- **VPC costs up by 53%** driven by higher **VPC Endpoint usage** and maintaining **separate VPCs for development and production**, leading to redundant networking resources and additional IPv4 charges.  

Overall, the total monthly AWS expenditure rose by **~83%**, primarily due to inefficient **infrastructure design** and **unoptimized RDS scaling**.

---

## **Approach**
As a **DevOps Engineer**, I analyzed the cost breakdown and implemented an **infrastructure optimization plan** following **AWS Well-Architected Framework** best practices:

### **1. VPC Consolidation**
- Proposed and implemented a **single VPC architecture** to eliminate duplicate networking resources.  
- Designed:
  - **Two public subnets** to host the **public (development) RDS**.  
  - **Two private subnets** to host the **private (production) RDS**.  
- Improved network efficiency while maintaining environment isolation using subnet-level segregation and IAM-based access controls.

### **2. RDS Optimization**
- Gradually scaled RDS from **t3.micro → t3.small → t4g.medium** to balance performance and cost.  
- Configured:
  - **Development RDS** as public for developer access via **pgAdmin4** and **Lambda APIs**.  
  - **Production RDS** in private subnets, accessible only through:
    - **Lambda functions** for API-based data access.  
    - A dedicated **EC2 bastion host** for administrative operations and **psql data transfers** between environments.  

### **3. Access Control & Security**
- Enforced **least privilege access**, allowing only authorized users to modify production data through the EC2 instance.  
- Ensured **secure data migration** using **psql dumps** from the development RDS to the production RDS.  

---

## **Achievements**
- 💰 **Reduced AWS monthly cost by ~$57**, achieving:
  - **$34 savings** through **VPC consolidation**.  
  - **$23 savings** through **gradual RDS scaling**.  
- 🚀 **Improved infrastructure efficiency** by consolidating VPCs and optimizing RDS usage.  
- 🔒 **Enhanced security posture** with private subnet isolation and restricted RDS access.  
- 🌐 **Optimized network design** aligned with AWS **Cost Optimization** and **Operational Excellence** pillars.  
- 📉 **Reduced total monthly expenditure** to approximately **$80**, ensuring scalability, maintainability, and cost-effectiveness.

---

### **Tools & Technologies**
- **AWS Services:** VPC, RDS (PostgreSQL), EC2, Lambda, IAM, CloudWatch  
- **Tech Stack:** Terraform, pgAdmin4, psql  
- **Best Practices Followed:** AWS Well-Architected Framework, Least Privilege Access, Cost Optimization
