
1. Tell me about your self.
    - I have a total of 4+ years of experience in IT industry. I worked as Sr. DevOps Engineer in Adiel Technology. My core competence is AWS, having experience in compute sevice, network service, database servie, Secuity & Complaince. I worked on IAC tool like terraform, configuration managment tool like ansible, containrization tool like docker, CI/CD tool like jenkins, AzureDevOps. I have good knowledge on orchestration tool like kubernetes. I know languages like pyhton, powershell, bash.
    - My daily routine - As part of DevOps Engineer role we use to manage kubernetes cluster for our organisation. we ensure the applications are deployed on the cluster and there is no issues with the application, so we have to setup monitoring on kubernetes cluster,
    - apart from that we use to do lot of maintaince activity as we have 3 masternode and 10 worker nodes like **upgrading versions** using tags and **installing required packages** ensuring that these are free form vulnurabilities.
    - we ensure that when ever bugs on the kubernetes when developer are not able to troubleshoot w.r.t some pod, unable to troubleshoot w.r.t some services or unable to route the traffic inside the kubernetes cluster as subject expertise we comes into picture to solve the issue.
    - apart from this we offer subject expertise on k8s, if anyone in organisation has any issue with kubernetes they create tickets for us, we use to solve the issues.
    - Creating infrastrcuture for all environement DEV, STAG, PROD server
    - Deployment - Developer develops the code, we use to write dockerfile for that code to deploy.
    - Storing - we store the image using dockerhub.
    - Download dependencies -Ansible is used to download and install the multiple denpendencies in the host at a time.
    - CI/CD - jenkins pipeline is used to automate the entire things.
2. How many Projects you have done.
    - In my previous organisation eariler we worked on monolithic service, micro services, terraform, different CI/CD pipelines, IAC terraform and orchestration like kubernetes. For instance in one of my project i automated the for microservice based application using kubernetes which significantly reduced deployment time by 50%.
    - In another project, I set up a scalable infrastructure on AWS using Terraform, which improved the system's reliability and performance. Maintained 99% uptime for critical applications through effective monitoring.Each project has helped me deepen my expertise in different areas of DevOps, from automation to cloud management.
3. what type of challenges you faced how do you over come those challenges.
    - While implementing CI/CD pipeline using jenkis I faced few problems
    1. **Handling Secret Managment** In my previous organisation we had lot of microservice and we need to store more secrets, and we need to reference these secrets in jenkins pipline.
    - we store these secrets using **hashicorp vault** and give reference in jenkins pipeline. In this way handle the secrets and preserve the security. 
    2. **Docker Image** we tried to reduce the size of docker image which is huge and it is concerning w.r.t security.
    - we use **docker multi stage build** and using distroless images we not only reduce the size but also preserved the security by removing the packages that are installed in the images.
    3. **kubernetes pod** My organisation is dealing wiht lot of pods, some pods are consuming more resoure we identified and applied `requests and limits`. When ever I found a pod is consuming more resource I will approch development team and rnquire why it is consuming more and will increase the `limits` as per requirement. 
    4. **kubernetes app**  Deploying applications using kubernetes and ckeck it woking if any of the application goes down or unresponsive and if dont know. **solution** I use to open kubernetes pod and collect logs, if it is java application go to application check the dumps, analize the dumps and approach develop team and solve the issue.
    5. while deploying the code some times we face challanges, the deployment may get failure in that sitution we use to follow branching strategy create a feature branch from the main branch, in my senario the code will work fine at the developers end but not work on production side, there we found the bug and it will fix by developer but we need to provide branch strategy to them
4. Can you tell me two senarios where you struggeled a lot.
    - One among my project we faced a serious issue of application downtime due to heavy traffic, intially we desing setup doesnot conisider the autoscaling. we made deep analysis of traffic bottleneck, includin improper autoscalling and database connections. Due to lack of documentation and risk of down time. I spent a considerable time in optimizing the infra, setting up autoscalling policies, RDS to handle more connection. This eventuallly reduces the download that day i learnt two things 1. planning for scalability in the early stage with documentation, 2. Through testing in UAT stagging before moving to production.
    - During terraform code i faced an issue where i encountered an issue with dependencies and resource which creating a dependency loop in creating VPC, I have taken enough time to check the root cause for circular dependency. later i used `depend_on` and module in the code.
    - We jenkins CI/CD pipline where lot of microservices are running we need to keep the secerets, pipeline failure due to inconsistent behaviour of different environment. The root cause for this is enivorment specific variables and dependency mismatch. Later i used to create different workspace for terraform, we use namespace (virtual isolate ) to run the container which utilizes the same resource. In docker i used to create **docker bridge**, storing sercets in **hashicorp vault** and give reference in jenkins pipeline.
    - In one among my projects handling vulnerabilities in docker images. some critical vulnerabilities are identifing in several docker images due to oudated image or updating image to rectify risk. The challange is identifing such vulnerability images and their dependency and finding the secure alternate with less downtime or no downtime. I setup an automated vunlnerabiltiy scaning, work closly with developers, update the dependecies with improved security. 
5. What type of bugs or errors you feel difficult.
    - Dependency conflicts - In micro service architecture services are depends on different libraries and version, even with same library with different versions. Resolving this conflicts requrire deeper understanding of software. Using containerization and regular updates can handle this.
    - CI/CD Pipeline Failures - Errors may occur any where in the CI/CD pipeline. To resolve, especially when it is complex build project, this may include environmental variables, secrets managment or scripts. Code scaning, image scanning tools will help to solve this issues.
    - My approach is dividing the complex problem in systematic smaller parts, analyse one component at a time by using appropriate method.
    - Team collaboration and Doumentation the step what the issue is and how i resolved it.
6. can you tell me a senario where you helped you collegeus.
    - Some time the application works fine in stagging environment and fails in production after the deployment of newer version. Docker container is crashing which caused a cascaded failure of service dependencies.
        - I quickly joined the war room with developers, QA and prod team and discuss about the seriousness with minimum downtime.
        - I used to collect the logs form the kukbernetes cluster using central logs, the application was failing due to "database connection timeout" but not clear.
        - I used to check the network related issues in aws sg, inbound and outbound rules and everything is fine.
        - Container debugging by creating same environment in the local system wiht enviromnet variables, and the container is unable to connect with database.
        - After inspect the new docker image build from base image and version, libraries. This dispencary was not shown in production.
        - I communicated the same with team and rollback to previous image, this was done by using jenkins.
        - Once the application is online, we team members update the docker file with correct libraries and test the image.
    - Outcomes:
        - The prod environment was restored in 30 min.
        - Downtime was minimized and application was back online during peak times.
        - I improved CI/CD process in order to prevent the same issuee in future.
    
7. Have you involved to solve any colleague problems who are facing from the long time.
    - I had gone through a situation where the build is getting failure some times it work fine and some time it will pass. The root cause was unclear, making it diffcult to find whether it is dependecy issue or network issue.
    - I gateherd the information from my colleagues about the errors they are facing and build logs. I noticed the errors at different stages like installation, dependency, versions.
    - I examined the CI/CD pipeline where need some improvement by removing outdated plugins, and retries (timeouts), i noticed the CI/CD is working in shared limited resource.
    - I noted the build failure is due to dependency conflicts, i suggested dependency managment tool like `pipenv` for python.
    - I used autoscalling in kubernetes in order to utilize the resource optimally.
    - I implemented better monitoring and alerting for the CI/CD pipeline using tools like Prometheus and Grafana. 
    - Because of this we achived bulid failure rate reduced to 80% with faster release cylce.
    - This experience showed the importance of taking a holistic approach to problem-solving in DevOps.
8. If i gave you three tier application (web, app, db) which important accepts you are put in, so that application will be secure.
    -  Network Security - use VPC, SG traffic and apply LB on top of it add WAF to aviod DDoS and SSL/TLS between client and web applicaiton, Use VPN to avoid unauthourised access.
    - Infrastructure Security - use RBAC for managing permission, MFA for accessing any managment interface (SSL and RDP) and implementing real time monitoring tools like prometheus and grafana.
    - Application Security- use Authentication and Authorization methods, use secure API calls like https.
    - Database Security - allowing only the application to access data base with dedicated user with minimum permision. Perform regular backups of the database and encrypt the backups and storing.
    - Secure Secrets Management Store sensitive information, such as API keys, passwords, and certificates, in a secure secrets management system like AWS Secrets Manager, HashiCorp Vault.
    - Encrypt sensitive data both in transit (using TLS) and at rest (using AES-256 encryption or stronger).

1. what is your previous experience means 
    - what type of projects you have done 
    - Technical skills and 
    - Domain knowledge
    - Time managment skills you have
- Behavourial 
- Attitude
- Time managmet 