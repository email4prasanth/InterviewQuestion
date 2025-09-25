# ⚡ Digital Signage System – DevOps Documentation (Lite)  

## 1. Project Overview  
- [x] Multi-tenant digital signage platform.  
- [x] Admins manage content → backend schedules/queues → TVs fetch/play content via WebSocket + SQS.  
- [x] Frontend: React on S3/CloudFront.  
- [x] Backend: Spring Boot on EC2 (Dev) & ECS (Prod).  
- [x] Reliable delivery via SQS.  

## 2. Environments  
- [x] **Dev** → EC2 (manual deployment via SSH + scripts).  
- [x] **Prod** → ECS + ALB (automated CI/CD with Serverless Framework).  
- [x] Access controlled via IAM roles, Security Groups, VPC isolation.  

## 3. Infrastructure  
- [x] Cloud: AWS (S3, CloudFront, EC2, ECS, ECR, RDS, SQS, VPC).  
- [x] Infra-as-Code: Serverless Framework for ECS tasks + networking.  
- [x] Networking: VPC with Security Groups restricting access.  
- [x] Storage: RDS/Aurora (schedules, playlists, device status).  

## 4. CI/CD Pipelines  
- [x] Frontend: GitHub Actions → Build React → S3 → CloudFront Invalidate.  
- [x] Backend Dev: Manual EC2 deployment (kill ports + start scripts).  
- [x] Backend Prod: GitHub Actions → Build Docker images → Push to ECR → `sls deploy` → ECS Tasks behind ALB.  
- [x] Rollback: Restart services (Dev) / Redeploy ECS task definition (Prod).  

## 5. Monitoring & Logging  
- [ ] Logging: App logs via Spring Boot (no mention of centralization yet).  
- [ ] Metrics: Not specified (could add CloudWatch or Prometheus).  
- [ ] Alerting: Not defined.  

## 6. Security  
- [x] Authentication: IAM + Spring Security (JWT/OAuth).  
- [x] Role-based access: Super Admin (global) / Store Admin (per-store).  
- [x] Network security: VPC, Security Groups, IAM-auth SSH keys.  

## 7. Scalability & Reliability  
- [x] ECS Tasks for backend services (scalable).  
- [x] ALB for load distribution.  
- [x] SQS ensures reliable message delivery (devices offline → queue).  
- [ ] Backup/DR: Not defined.  

## 8. Runbooks  
- [x] **Dev Deployment**: SSH → stop services (8080, 9090, 7070) → run scripts.  
- [x] **Prod Deployment**: CI/CD builds Docker → ECR → ECS → ALB routing.  
- [ ] **Incident Response**: Not defined.  
- [ ] **Recovery Guide**: Not defined.  
