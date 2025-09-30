# Lumifi Deployment Guide

Lumifi Dental is a serverless Electronic Health Record (EHR) system for the dental industry. The application is fully deployed on **AWS** with a **serverless-first architecture** using Lambda, API Gateway, and CloudFront. Infrastructure is managed with **Terraform**, and CI/CD is handled using **GitHub Actions**.

---
## High-Level Architecture
```sh
[Users]  --> CloudFront (WAF) --> S3 (Frontend static hosting) 
                          \
                           --> API Gateway (HTTP API) --> Lambda functions 
                                                           |-> RDS (Postgres)
                                                           |-> S3 (export/backup)
                                                           |-> SES / Stripe / Secrets Manag
```
## 1. AWS Services Used

| Service             | Purpose                                            |
| ------------------- | -------------------------------------------------- |
| **S3 Standard**     | Object storage (frontend hosting, Terraform state) |
| **CloudFront**      | CDN for frontend with low-latency global delivery  |
| **API Gateway**     | Entry point for backend APIs (path-based routing)  |
| **Lambda**          | Serverless compute (Node.js functions)             |
| **SES**             | Transactional and marketing emails                 |
| **RDS (Postgres)**  | Relational database                                |
| **WAF**             | Web Application Firewall                           |
| **VPC**             | Isolated networking for backend resources          |
| **Secrets Manager** | Securely stores sensitive keys and DB credentials  |

---

## 2. CI/CD with GitHub Actions

* Each repo (`lumifi-backend`, `lumifi-frontend`) contains workflows under `.github/workflows/`.
* Environments:

  * **Feature** → `feature/*` branches
  * **Dev** → `develop` branch
  * **Prod** → `main` + `release/**` branches
* **Secrets**:

  * Short-lived credentials from AWS Secrets Manager during deployments
  * GitHub Secrets for pipeline tokens (e.g., `SERVERLESS_LICENSE_KEY`, `AWS_ACCESS_KEY_ID`)

---

## 3. Repositories

* **Backend** → [`Kazisu/lumifi-backend`](#backend-deployment)

  * Terraform infra + Node.js (TypeScript) Lambda functions
* **Frontend** → [`Kazisu/lumifi-frontend`](#frontend-deployment)

  * Terraform infra + ReactJS frontend

---

## 4. Backend Deployment

### Steps

1. **IAM Setup**

   * Create IAM user `prasanth_devops` with MFA enabled
   * Attach inline policy with least-privilege permissions

2. **Terraform State**

   * Create S3 bucket `lumifi-tfstate-file` for Terraform state storage

3. **Terraform Modules**

   * Resources: `iam`, `rds`, `s3`, `secrets`, `security_groups`, `ses`, `vpc_subnet`, `vpc_endpoints`
   * Version: Terraform `~5.0`
   * Vars defined in `locals.tf`

4. **Serverless Configuration**

   * Framework: `serverless >= 4.0.0`
   * Runtime: `nodejs18.x`
   * Functions:

     ```yaml
     practiceHandlerFunction:
       timeout: 30
       handler: dist/handler.practiceHandler
       events:
         - httpApi:
             path: /${self:custom.env.API_ROOT_PATH}/practice/software
     ```
   * IAM permissions for `logs:*`, `rds-db:connect`, `sts:AssumeRole`

5. **CI/CD Workflow**

   * `dev-backend.yml`

     * `aws-resources-deploy`: Terraform infra
     * `deploy-serverless`: Deploy Lambda with `.env`

6. **Database Setup**

   * Insert initial data into `dev-lumifi-db`
   * Ensure SSL in `pg.connection.ts`:

     ```ts
     dialectOptions: {
       ssl: { require: true, rejectUnauthorized: false },
     }
     ```

7. **Validation**

   * Test API:
     `https://<api-id>.execute-api.us-east-1.amazonaws.com/api/v1/*`
   * Check **CORS** (must allow FE CloudFront distribution domain)

### Folder Structure

```
lumifi-backend/
├── backend-infra/
│   ├── backend.tf
│   ├── iam.tf
│   ├── locals.tf
│   ├── rds.tf
│   ├── s3.tf
│   ├── secrets.tf
│   ├── security_groups.tf
│   ├── ses.tf
│   ├── vpc_endpoints.tf
│   └── vpc_subnet.tf
├── src/
│   ├── lib/            # DB & shared logic
│   ├── middlewares/    # Middlewares
│   ├── models/         # Sequelize models
│   ├── schemas/        # Zod schemas
│   ├── services/       # Business logic
│   ├── handler/        # Route handlers
│   └── test/           # Unit tests
├── serverless.yml
├── package.json
└── tsconfig.json
```

---

## 5. Frontend Deployment

### Steps

1. **Terraform Modules**

   * Resources: `s3`, `cloudfront`, `waf`
   * Version: Terraform `~5.0`
   * Vars in `locals.tf`

2. **S3**

   * Enable CORS, required permissions, public access for static hosting

3. **CloudFront**

   * Origin: S3 website URL
   * Behaviours: check caching, error pages
   * WAF enabled for protection

4. **Validation**

   * Verify CloudFront distribution works with alternate domain (`app-dev.lumifidental.com`)
   * SSL certs provisioned via DNS validation

### Folder Structure

```
lumifi-frontend/
├── frontend-infra/
│   ├── backend.tf
│   ├── cloudfront.tf
│   ├── locals.tf
│   ├── outputs.tf
│   ├── providers.tf
│   ├── s3.tf
│   └── waf.tf
├── public/
├── src/
│   ├── assets/
│   ├── config/
│   ├── lib/
│   ├── lumifi/
│   ├── store/
│   ├── App.tsx
│   ├── index.css
│   └── main.tsx
├── package.json
└── README.md
```

---

## 6. Client Requirements / DNS

* Provide `SERVERLESS_LICENSE_KEY`
* Setup DNS records for `lumifidental.com` (SSL certificate)
* Alternate domains → `app-dev.lumifidental.com`
* Share SES DNS records (CNAME, A)

---

## 7. Key Notes

* Ensure **least-privilege IAM policies**
* Use **AWS Secrets Manager** for DB creds instead of plain GitHub Secrets
* Enable **SSL/TLS everywhere** (RDS, API Gateway, CloudFront)
* Regularly validate **CORS + WAF rules**
* Enforce **branching strategy** for safe deployments

---
### Resume highlight
Implemented and automated deployment of Lumifi Dental, a serverless EHR platform on AWS using Lambda, API Gateway, S3, CloudFront, RDS, and WAF. Designed CI/CD pipelines with GitHub Actions, managed infrastructure with Terraform, enforced IAM security, Secrets Manager, SSL, and DNS. Optimized Dev/Prod workflows ensuring scalable, secure, and resilient operations.

###  One line
Automated AWS serverless deployments for Lumifi Dental using Terraform and GitHub Actions, ensuring secure, scalable CI/CD with Lambda, API Gateway, and RDS.
