# Challenge-1 
## DevOps Challenge: Azure Project Migration & Renaming

## Resume / LinkedIn Version (Concise, Impact-Focused)
- Led the **full renaming and migration** of a complex Azure-based project from **Platform 2.0 → Thinkrd365**, coordinating 4 branches and 6 environments while preserving Git commit history.  
- Managed **high-risk resource renames** across VMs, Key Vaults, SQL servers, APIs, and Azure AD B2C directories, ensuring **minimal service disruption**.  
- Designed and implemented a **migration strategy** that balanced **client requirements for branding** and **team needs for commit traceability**.  
- Coordinated SSL, DNS, and Key Vault updates across multiple environments, demonstrating strong **DevOps planning and execution skills**.  

## Narrative / Case Study Version (Interview Style)
> “One of the most challenging projects I handled involved migrating and renaming an Azure-hosted platform from **Platform 2.0 to Thinkrd365**. The client required a full rename (including VMs, Key Vaults, SQL servers, APIs, and Azure AD B2C directories) while the team leader requested that we **preserve Git commit history**.  
> 
> I designed a **migration plan covering 4 branches and 6 environments**, allowing us to map old environments (dev, uat) to new ones (development, QA) without losing historical commits. I coordinated SSL certificate updates, DNS records, and Azure Key Vault configuration, ensuring a smooth transition.  
> 
> The project was completed successfully, meeting both **client branding objectives** and **internal traceability requirements**, while minimizing downtime and operational risk. This experience reinforced my ability to handle **complex, multi-stakeholder DevOps projects** with precision and foresight.”

# Branches and Environment Migration: Platform 2.0 → Thinkrd365

## Branch & Environment Mapping

```text
       Old Project: Platform 2.0                 New Project: Thinkrd365
--------------------------------------------------------------------------------
Branch: develop                                Branch: develop
  - Environment: dev      ------>              - Environment: development
      (old dev env)                            (new dev env)

Branch: uat                                    Branch: uat
  - Environment: uat      ------>              - Environment: QA
      (old UAT env)                            (new QA env)

Branch: preprod                                Branch: preprod
  - Environment: preprod  ------>              - Environment: preprod
      (unchanged)

Branch: main                                   Branch: main
  - Environment: prod      ------>              - Environment: prod
      (unchanged)

