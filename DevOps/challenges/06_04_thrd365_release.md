# Release Management Standardization & Deployment Automation in ThinkRD365

In the ThinkRD365 project, I identified a major gap in release tracking and deployment consistency. Although development was progressing smoothly, there was no structured way to track releases across multiple repositories and environments, leading to confusion during deployments.

The system consisted of multiple components:
- Infrastructure (IaC)
- Backend services
- ETL pipelines
- Frontend applications

Each component had deployments across multiple environments:
- Development
- QA
- Pre-production
- Production

---

## Challenges Identified

- No centralized tracking of releases across repositories
- Difficulty in identifying which version was deployed in each environment
- Manual execution of database migration scripts during deployments
- High risk of human error due to running scripts individually
- Lack of versioning consistency across services
- No standardized deployment artifact management

---

## Actions Taken

### Release Tracking Standardization

- Designed a centralized **release tracking sheet** covering:
  - All repositories (IaC, Backend, ETL, Frontend)
  - Pull Requests mapped to environments (Dev → QA → Preprod → Prod)
  - Microservices with their respective deployment environments

- Introduced **version tagging strategy**:
  - Tagged releases (e.g., `v5.0.0`) across repositories
  - Ensured traceability between code, PRs, and deployments

---

### Deployment Automation for Database Scripts

Initially, database scripts (SQL and JS) were executed manually during deployment.

To improve reliability:

- Consolidated all migration scripts into structured release folders
- Created a **shell script (.sh)** to automate execution of:
  - Main database scripts
  - Order (ORD) database scripts
  - Migration scripts in sequence

---

### Artifact Management using Azure Blob Storage

Implemented a centralized artifact distribution mechanism using **Azure Blob Storage**:

#### Upload Process

- Used `azcopy` to upload release scripts from local system to blob storage:

```bash
azcopy copy \
"D:\Repo\Deploy_scripts\Release-v5.0.0" \
"https://<storage-account>.blob.core.windows.net/script-container?<SAS_TOKEN>" \
--recursive