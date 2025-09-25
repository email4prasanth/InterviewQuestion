# Digital Signage Application Workflow
## Business
# Digital Signage System  
It’s a multi-tenant digital signage platform where admins manage content → backend schedules and queues → TVs fetch/play content via WebSocket + SQS.
Frontend is React on S3/CloudFront, backend is Spring Boot on EC2 (dev) and ECS (prod), with SQS handling reliable delivery.

## 1. Core Components  

### **Admins**  
- **Super Admin**: Manages all stores/devices.  
- **Store Admin**: Manages only their store’s devices. 

### **Content & Scheduling**  
- Upload playlists (**images/videos**).  
- Schedule display times (**one-time/recurring**).  
- Group devices for **synchronized content**.  

### **Device Management**  
- Register, group, and monitor **devices (online/offline)**.  

### **Delivery System**  
- **SQS**: Queues content for delivery.  
- **DB**: Stores **schedules, playlists, and device status**.  

---

## 2. Data Flow  

1️⃣ **Admin Input** → Playlist + Schedule stored in **DB**.  
2️⃣ **Device Pings Server** → Checks for **pending schedules**.  
3️⃣ **SQS Delivers Content** → When **device is online** (immediate or scheduled).  
4️⃣ **Group Sync** → Devices in same group **display content simultaneously**.  

## Technical
## 1. Frontend Workflow (Node.js/React)

### Development
- Code is pushed to the repository (e.g., GitHub).
- CI/CD pipeline (e.g., GitHub Actions) triggers:
  - Build the React app: `npm run build:develop`.
  - Upload static files to AWS S3: `aws s3 sync`.
  - Invalidate CloudFront cache to ensure the latest content is served.

### User Access
- Users interact with the React app hosted on S3 + CloudFront.
- CloudFront serves cached content for performance.

## 2. Backend Workflow (Java/Spring Boot)

### Development Environment (EC2)

#### Deployment
- Code is checked out from the repository (`signage-backend dev` branch).
- SSH into EC2 using IAM-authenticated keys.
- Stop existing services:
  ```bash
  lsof -t -i:8080  # Auth service
  lsof -t -i:9090  # Backend service
  lsof -t -i:7070  # WebSocket service
  ```
- Run deployment scripts:
  ```bash
  ./authstart.sh    # Starts Auth service on port 8080
  ./backendstart.sh # Starts Main API on port 9090
  ./websocket.sh    # Starts WebSocket service on port 7070
  ```

#### Runtime
- EC2 runs all three services simultaneously.
- Security Groups/VPC restrict access to authorized IPs.

### Production Environment (ECS/Serverless)

#### CI/CD Pipeline
- Code changes trigger GitHub Actions.
- Build Docker images for each service (auth, backend, websocket).
- Push images to ECR (`prod-signage-main-*`).

#### Serverless Deployment
- `sls deploy` (Serverless Framework) provisions:
  - ECS Tasks (containerized services).
  - ALB (routes traffic to ECS: `/auth`, `/api`, `/ws`).
  - API Gateway (if Lambda is used).
  - VPC/Security Groups (isolate ECS, ALB, RDS).

#### Runtime
- ALB directs traffic to ECS tasks.
- RDS/Aurora serves as the database (accessed via Spring Boot).

## 3. WebSocket Service

### Role
- Tracks active TVs and manages real-time communication.

### Workflow
1. TV registers as "active" via WebSocket (port 7070).
2. Backend sends schedules/playlists via SQS (queues messages if TV is offline).
3. WebSocket pushes updates (e.g., new content) to connected TVs.

## 4. Playlist & Content Management

### Super Admin/Store Admin
1. Logs into the web app (React frontend).
2. Creates/modifies playlists (images, videos, messages) using a canvas editor.
3. Schedules content for specific TVs/times.

### TV Workflow
1. On activation, TV fetches schedule via backend API.
2. SQS ensures delivery even if TV was offline.

## 5. User Types & Access

- **Super Admin**: Full access (manage all stores, users, content).
- **Store Admin**: Manages content for assigned stores.
- **Authentication**: IAM + Spring Security (JWT/OAuth).

## Sequence Diagram (High-Level)

```
1. Frontend Deploy:
   Code → Build → S3 → CloudFront (Invalidate) → User

2. Backend Dev:
   Code → EC2 (SSH) → Kill Ports → Deploy Scripts → Services (8080, 9090, 7070)

3. Backend Prod:
   Code → ECR → Serverless (ECS + ALB) → RDS

4. TV Workflow:
   TV → WebSocket (Active) → Backend → SQS → Playlist → TV
```

## Key AWS Services Used

| Component            | AWS Services                        |
|----------------------|-----------------------------------|
| **Frontend Hosting** | S3, CloudFront                    |
| **Backend (Dev)**    | EC2, IAM, Security Groups        |
| **Backend (Prod)**   | ECS, ECR, ALB, Serverless, RDS, VPC |
| **Real-Time**        | WebSocket (Spring), SQS          |
| **Auth**            | IAM, Spring Security             |


