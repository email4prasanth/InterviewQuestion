# Thinkrd365 Workflow
## Business
Thinkrd 365 is a global HR and payroll management system under R&D that handles multinational employee data, including salaries, financials, and HR records. It supports real-time operations such as adding, updating, and deleting employees, while retaining historical and current records to ensure auditability and compliance. Its primary business function is to accurately prepare employee tax details for government reporting.

1. Core Components

## Frontend Layer
- **Azure Static Web App** — React/Node.js application  
- **Azure Front Door** — Global CDN, WAF, and load balancing  
- **Azure API Management** — API gateway with security policies  

## Backend Layer
- **Azure Virtual Machines (Backend VM)** — Java/Spring Boot microservices  
- **Azure Virtual Machines (ETL VM)** — Data processing services  
- **Azure Virtual Machines (Redis VM)** — Caching layer  

## Data Layer
- **Azure PostgreSQL Flexible Server (Main)** — `thinkrd365_main` database  
- **Azure PostgreSQL Flexible Server (Org)** — `thinkrd365_org` database  
- **Azure Blob Storage** — File/document storage  

## Security & Management
- **Azure Key Vault** — Secrets management  
- **Azure Active Directory** — Authentication & authorization  
- **Azure Monitor** — Logging and monitoring  
- **Network Security Groups** — Network security  

2. Data Flow

## Technical Data Flow

### 1. Frontend Workflow (React / Static Web App)
#### Flow:
Static Web App → Front Door → API Management → Backend Services
### 2. Backend Workflow — Backend for ThinkRD 365
- Tech Stack:
    - Node.js with TypeScript & GraphQL
    - Database: PostgreSQL (Sequelize)
    - ETL: Python
    - Frontend: React.js
#### Flow:
Backend VM → Key Vault (credentials) → PostgreSQL → Response chain
#### Environments
- Development/QA Environment
```sh
User → API Management → Virtual Machines (Direct) → PostgreSQL
```
- Preprod/Prod Environment
```sh
User → Front Door → API Management → Application Gateway → Virtual Machines (Direct) → VPN Peering → PostgreSQL
```

3. Key Azure Services Used

## Compute & Hosting
- **Azure Virtual Machines** — Backend, ETL, Redis services  
- **Azure Static Web Apps** — Frontend hosting  
- **Azure Container Registry** — Docker image storage  

## Networking & Content Delivery
- **Azure Front Door** — Global load balancing, CDN, WAF  
- **Azure Application Gateway** — Layer 7 load balancing, SSL termination  
- **Azure Virtual Network** — Network isolation and segmentation  
- **Azure Public IP** — Public endpoints  

## Database & Storage
- **Azure PostgreSQL Flexible Server** — Primary data storage *(main + org)*  
- **Azure Blob Storage** — File and document storage  
- **Azure Redis Cache** — In-memory data caching  

## Security & Identity
- **Azure Active Directory** — Authentication and groups  
- **Azure Key Vault** — Secrets and certificate management  
- **Azure Network Security Groups** — Network security rules  
- **Web Application Firewall** — Threat protection  

## Monitoring & Management
- **Azure Monitor** — Comprehensive monitoring  
- **Azure Log Analytics** — Centralized logging  
- **Data Collection Rules** — Unified data collection  
- **Azure Resource Groups** — Resource organization  

## Developer Tools
- **Azure API Management** — API gateway, policies, versioning  
- **Azure Terraform Backend** — Infrastructure as Code state management  
- **Azure RBAC** — Role-based access control  

---

> This architecture provides a **scalable**, **secure**, and **maintainable** cloud infrastructure that follows **microservices principles** while leveraging **Azure’s managed services** for reliability and reduced operational overhead.
