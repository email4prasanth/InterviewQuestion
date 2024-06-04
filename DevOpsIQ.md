**DevOps Tools -packer, ansible, terraform, jenkins, docker, kubernetes, puppet, promethes, git, gitlab..**
- What is difference between Cloud Engineer and DevOps Engineer
    - Cloud Engineer is require for migrating Onpermises to Cloud platform and key resposibilites are
        - Multi-tier cloud **Architecture Desigin**.
        - **Migration plan** includes data transfer, app deloy and disaster plan setup. 
        - Providing **Security** by controling the access of user, encrypting sensitive information
        - Maintaining infrastructure IaaC (AWS - CloudFromation).
        - **TrobuleShooting**
        - **Monitoring**
        - Skill
            - AWS
            - Cloud services - db, security, storage, networking
            - IaaC - CloudFormation, Terraform.
            - Security - 
            - Monitoring Tools -
    - DevOps Engineer is bridge b/w Developers and Operators to improve the application delivery
   
- **DevOps** is a process of improving the application delivery, it is culture of learning 
```
1. Automation
2. Quality
3. Monitoring
4. Testing
```

- ansible
    - An open-source IT automation tool that focuses on automating IT tasks like provisioning and deployment. Ansible is used for software provisioning, application deployment, configuration management, and troubleshooting deployment.

- 

- jenkins
    - An open-source automation server that helps with continuous integration and delivery (CI/CD). Jenkins is used for building apps, testing builds, and integrating changes quickly.

- Monitoring Tools- https://www.tigera.io/learn/guides/kubernetes-monitoring/kubernetes-monitoring-tools/
    - Kubernetes Dashboard
    - Prometheus
    - cAdvisor
    - Elastic Stack (ELK)

</h1> Interview Questions </h1>

1. Explain your current CI/CD setup 
- Currently we are using Jenkins for continious integration and continious deployment. we use Github as soucre code repository, we configured git hub webhook that will trigger the jenkins pipeline (Orchestrater) for every commit. The source is GITHUB and the target platform is kubernetes. 
  - Continious Integration
    - These pipeline has multiple stages
        1. Checkout stage - In this stage we checkout the code that user has made
        2. Build & UT stage - We use maven(written in java to build backend) for building and Unit Test Framework in the code repository.
        3. Code Scan - we use sonarqube repository to check the security vulnerability that code is free from any security
        4. Image Build - we use Dockerfile in the git repository to build container image.
        5. Image Scan - we check the binaries(.exe), default packages and base image are free from  vulnerabilities 
        6. Image Push - We push the image to AWS ECR.
    - These are multiple stages that are in continious integration, we write declerative jenkins file pipeline (jenkins groovy scripting) in Jenkis for Orchstrating each of them
- Continous Delivery
    - we use jenkins pipeline and update this image in the kubernetes manifest
    - we push this updated image to git hub repository (different from source code repository) to hold these manifest and host  helm chart repo on github using github pages.
    - we use gitops tools argocd (watch for updates) to deploy the image in kubernetes by pushing any changes made.
2. How do you handle secrets
- Currently iam woking on AWS we use AWS Seceret Manager to store the sensitive information 
- In GitHub there is an option called GitHub actions that stores sensitive info like passwords, secrets and tokens at differnt levels like organisation, repository and repository envi.
    - repository - gh secret set SECRET_NAME
    - environment - gh secret set --env ENV_NAME SECRET_NAME
    - organisation - gh secret set --org ORG_NAME SECRET_NAME
3. what is your Deployment strategy
- We use canary deployment strategy using load balancer where traffic is routed form old version to newversion like 10/90 , 30/70, 505/50, 70/30 and 90/10.
4. what do you do if deployment app is faulty?
- We check with 10/90 if it is working properly with bug free we will increase the traffic else we stop deploying in new version.
5. Jenkins setup, Backup and Scalling up
- To setup jenkins using bash script install java and current long term suppourt command
- Jenkin is on AWS we have AutoScalling we employed predective scalling on AWS. Once it scaled up jenkins uses SSH to intract with the newly created onces.
- Jenkins has .backup folder using cronjobs we periodically backup the files.
- Backup

6. what is jenkins controller and jenkins agent [link](https://www.jenkins.io/doc/book/getting-started/)
- An agent is machine a bare-meatal, VM, Container or cloud execute the task directed by the controller.
    - Purpose of Jenkins controller is to adminstrtion connections and tooling for the agents 
    - Any machine that run java can be jenkins agent. For secuity and performance jenkins agent is used to perform jobs, not to do any jobs directly on controller.
7. What are the real time challenges you faced.
- While implementing CI/CD pipeline using jenkis I faced few problems
    1. **Handling Secret Managment** In my previous organisation we had lot of microservice and we need to store more secrets, and we need to reference these secrets in jenkins pipline.
    - we store these secrets using **hashicorp vault** and give reference in jenkins pipeline. In this way handle the secrets and preserve the security. 
    2. **Docker Image** we tried to reduce the size of docker image which is huge and it is concerning w.r.t security.
    - we use **docker multi stage build** and using destory less images we not only reduce the size but also preserved the security by removing the packages that are installed in the images.
    3. **kubernetes pod** My organisation is dealing wiht lot of pods, some pods are consuming more resoure we identified and applied `requests and limits`. When ever I found a pod is consuming more resource I will approch development team and rnquire why it is consuming more and will increase the `limits` as per requirement. 
    4. **kubernetes app**  Deploying applications using kubernetes and ckeck it woking if any of the application goes down or unresponsive and if dont know. **solution** I use to open kubernetes pod and collect logs, if it is java application go to application check the dumps, analize the dumps and approach develop team and solve the issue.
    5. **Terraform** 

    
8. What is your day to day activity?

- Terrafrom, Docker,  DevOps, jenkins, CI/CD, Kubernetes, 
- How do you implement DevOps in you project (5m)
- What is your branching strategy 
- How do you work with developers and merge the code how it is going from development to production
- Write an ansible playbook, doker file, shell script, resource creation using terrafrom.
- Stages in pipeline
- how you are providing dev to prod automatically.
- Is there any Diaster recovery 

