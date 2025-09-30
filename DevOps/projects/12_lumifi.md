# Lumifi Workflow

## Business

Lumifi Dental is a specialized **electronic health record (EHR) system** designed for dental professionals. It simplifies patient record management, integrates with clinical workflows, and ensures compliance with healthcare data standards. The system leverages a **serverless architecture on AWS** for scalability, reliability, and cost efficiency. Its primary business function is to securely manage dental patient data, appointments, and financials while enabling quick access for practitioners.

---

1. Core Components

## Frontend Layer

* **AWS S3** — Static hosting of the React frontend
* **Amazon CloudFront** — Global CDN for performance, WAF integration, and SSL termination
* **Route 53 (DNS)** — Domain management and certificate provisioning

## Backend Layer

* **AWS Lambda** — Node.js/TypeScript serverless functions
* **Amazon API Gateway** — API gateway with routing, throttling, and security policies
* **Amazon SES** — Transactional and notification email service

## Data Layer

* **Amazon RDS (Postgres)** — Relational database for structured clinical and financial data
* **Amazon S3 (Standard)** — Object storage for files and Terraform state
* **AWS Secrets Manager** — Centralized secrets and credentials storage

## Security & Management

* **AWS WAF** — Web application firewall for exploit prevention
* **Amazon VPC** — Isolated network environment with subnets, endpoints, and security groups
* **IAM** — Role-based access control with MFA-enabled DevOps accounts
* **Terraform (Remote State in S3)** — Infrastructure as Code automation
* **GitHub Actions** — CI/CD pipelines for backend and frontend deployments

---

2. Data Flow

## Technical Data Flow

### 1. Frontend Workflow (React / S3 + CloudFront)

#### Flow:

User → CloudFront (CDN + WAF) → S3 (React App) → API Gateway (for dynamic requests)

### 2. Backend Workflow — Serverless Functions

* Tech Stack:

  * Node.js (TypeScript) with Sequelize ORM
  * PostgreSQL (SSL-enabled)
  * Zod for schema validation
  * SES for communication

#### Flow:

User → API Gateway → AWS Lambda → RDS/Postgres → Response

#### Environments

* **Development/QA**

```sh
Push to develop → GitHub Actions → Deploy to Dev Infra → API Gateway (Dev URL) → RDS Dev DB
```

* **Production**

```sh
Merge to main → GitHub Actions Release → Deploy to Prod Infra → API Gateway (Prod URL) → RDS Prod DB
```

---

3. Key AWS Services Used

## Compute & Hosting

* **AWS Lambda** — Event-driven serverless backend functions
* **Amazon S3** — Static site hosting and state file storage

## Networking & Content Delivery

* **Amazon CloudFront** — CDN with low-latency delivery
* **Amazon API Gateway** — Secure API routing
* **Amazon VPC** — Network isolation and segmentation
* **AWS Route 53** — DNS and certificate validation

## Database & Storage

* **Amazon RDS (Postgres)** — Primary structured data store
* **Amazon S3** — Document storage & Terraform backend

## Security & Identity

* **AWS WAF** — Protection against OWASP top 10 attacks
* **AWS IAM** — Fine-grained access control with MFA
* **AWS Secrets Manager** — Secrets and database credentials management

## Monitoring & Management

* **CloudWatch Logs** — Monitoring and log aggregation
* **Terraform** — Infrastructure as Code
* **GitHub Actions** — CI/CD for automated deployments

## Developer Tools

* **Serverless Framework (v4)** — Deployment of Lambda functions
* **GitHub Actions Secrets** — Secure pipeline configuration
* **TypeScript + Node.js** — Backend implementation
* **React + Redux** — Frontend implementation

---

> This architecture ensures **scalability**, **security**, and **maintainability** by using a fully managed **serverless AWS stack**. It enables rapid development cycles through CI/CD pipelines while enforcing compliance and data protection standards.


## Client Requirements / DNS

* Provide `SERVERLESS_LICENSE_KEY`
* Setup DNS records for `lumifidental.com` (SSL certificate)
* Alternate domains → `app-dev.lumifidental.com`
* Share SES DNS records (CNAME, A)

---

## Key Notes

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
