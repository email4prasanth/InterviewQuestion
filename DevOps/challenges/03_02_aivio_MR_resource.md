# Multi-Region Architecture Optimization & Database Migration in Serverless Environment

In the Aivio project, I identified a critical architectural issue where application components were distributed across multiple AWS regions, leading to latency, increased costs, and operational complexity.

The setup included:
- AWS Lambda functions deployed in Singapore Region (ap-southeast-1)
- MySQL database hosted on EC2 in Mumbai Region (ap-south-1)
- Parameter Store configurations stored in US East (N. Virginia) (us-east-1)

This multi-region architecture caused cross-region communication between services, resulting in higher latency, increased data transfer costs, and potential reliability risks.

---

## Challenges Identified

- High Latency: Lambda functions communicating with a database in another region
- Increased Costs: Cross-region data transfer charges between services
- Operational Complexity: Managing resources across multiple regions
- Slower Configuration Access: Parameter Store calls across regions impacting performance

---

## Actions Taken

### Architecture Optimization

Proposed consolidating all resources into a single region (Singapore) to improve performance, reduce cost, and simplify operations.

---

### Database Migration Strategy (Zero-Downtime Approach)

To safely migrate the MySQL database from Mumbai to Singapore, I implemented a phased migration:

- Created a new EC2 instance with MySQL in Singapore
- Used Amazon S3 for daily database backups and synchronization
- Established VPC peering between regions for secure data transfer
- Maintained parallel data synchronization for ~2 weeks to ensure consistency
- Performed final cutover after validating data integrity

---

### Configuration Optimization

- Migrated Parameter Store values to Singapore region
- Ensured Lambda functions accessed configurations locally to reduce latency

---

## Outcome

- Reduced latency by eliminating cross-region communication
- Lowered AWS costs by avoiding inter-region data transfer charges
- Improved reliability with a simplified single-region architecture
- Achieved zero-downtime migration using phased sync and validation approach
- Enhanced system performance and maintainability

---

## Resume

Optimized multi-region AWS architecture by consolidating services into a single region, executing zero-downtime MySQL migration via S3 sync and VPC peering, reducing latency, cost, and operational complexity while improving system reliability