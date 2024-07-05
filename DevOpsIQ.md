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

- Introduce yourself
```
Hello, my name is Marri Prasanth. With 4 years of IT experience, I have honed my expertise in Build and Release engineering, focusing on the seamless integration and deployment of software.

In my role, I manage GIT repositories, oversee user administration, and handle branching, tagging, and merging activities. I am skilled at configuring web hooks to trigger Jenkins pipelines and proficient in creating and managing these pipelines using shared libraries.

I possess a strong working knowledge of Linux and excel in automating scripts using Python and Bash. My experience extends to leveraging Terraform for providing and maintaining AWS infrastructure as code in an automated manner. Additionally, I have written playbooks in Ansible and effectively managed nodes.

My proficiency with Docker includes creating images, containers, and Docker files for various environments. I have managed Docker container deployment and scaling using Kubernetes orchestration with Helm.

Monitoring and alerting are key components of my skill set, utilizing Prometheus and Grafana to focus on performance metrics. My experience spans working with AWS and Azure DevOps, where I create resource groups and configure app services, storage accounts, containers, and VPCs via Terraform scripts.

I configure build and release pipelines in Azure DevOps to deploy packages across development, QA, UAT, and production environments. Additionally, I handle administrative processes for cloud systems, including installation, backup, security, array management, and software patching to ensure compliance.

My networking skills include VPN configuration and management, and I am proficient in continuous integration and continuous improvement practices, particularly CI/CD pipelines. I am adept in project management and agile methodologies, facilitating effective collaboration and communication within teams.

With strong problem-solving and decision-making skills, I ensure efficient cloud infrastructure and containerization management. My expertise includes automated testing, unit testing, performance testing, and working with APIs. I have a sound knowledge of microservices architecture and Infrastructure as a Service (IaaS).

Committed to continuous learning and improvement in the field of information technology, I am familiar with network protocols and standards such as HTTP, REST, and SSL.

Thank you for taking the time to learn about my background and skills as a DevOps engineer.
```
- Continious Delivery require manual approval before deploying into production. Continous Deployment directly deploys in production.
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
8. What is your branching strategy 

- At my current role, we use GitHub Flow as our branching strategy. GitHub Flow is a simple, yet effective model that is well-suited for continuous delivery and continuous integration environments. Here's an overview of how we implement GitHub Flow and the benefits it provides:

- Main Branch:
    - We have a single main branch that always contains production-ready code.
    - All new features, fixes, and improvements are merged into the main branch through pull requests (PRs).
- Feature Branches:
    - For each new feature or bug fix, we create a dedicated feature branch from the main branch.
    - Feature branches are named descriptively, often including the ticket number and a brief description (e.g., feature/123-add-login-button).
- Pull Requests (PRs):
    - Once a feature or fix is completed, a pull request is opened to merge the feature branch back into he main branch.
    - PRs are reviewed by team members to ensure code quality, functionality, and adherence to coding standards.
    - Continuous integration (CI) pipelines run automated tests on the pull request to catch any potential issues early.
- Code Reviews and Approvals:
    - We have a mandatory code review process where at least one other team member must approve the changes before they are merged.
    - This practice not only improves code quality but also promotes knowledge sharing among team members.
- Continuous Integration and Deployment (CI/CD): 
    - Every commit to the main branch triggers an automated CI pipeline that runs comprehensive tests to ensure stability.
    - Upon successful completion of tests, the changes are automatically deployed to our staging environment for further testing.
    - Once the changes are verified in staging, they are promoted to the production environment, ensuring a smooth and reliable deployment process.
- Benefits of GitHub Flow:
    - Simplicity: GitHub Flow is straightforward, making it easy for the team to adopt and follow.
    - Continuous Delivery: The model supports frequent and reliable releases, which is ideal for agile development practices.
    - Collaboration: The pull request and code review process foster collaboration and improve code quality.
    - Flexibility: It allows us to quickly address hotfixes or critical issues by creating short-lived branches directly from the main branch.
    - By using GitHub Flow, we maintain a streamlined workflow that promotes quick iterations, high code quality, and robust CI/CD practices. This strategy aligns well with our goal of delivering high-quality software efficiently and effectively.


9. What is your day to day activity?
- As a DevOps engineer, my day-to-day activities encompass a wide range of tasks that ensure smooth and efficient development, deployment, and maintenance of applications. Here is a detailed breakdown of my typical day:
- Daily Standup Meetings:
    - Attend daily standup meetings with the development and operations teams to discuss ongoing projects, blockers, and priorities for the day.
- Monitoring and Incident Response:
    - Continuously monitor system performance, application logs, and infrastructure health using tools like Prometheus, Grafana, and Splunk.
    - Respond to alerts and incidents, troubleshoot issues, and work towards quick resolutions to minimize downtime.
- CI/CD Pipeline Management:
    - Maintain and optimize continuous integration/continuous deployment (CI/CD) pipelines using tools like Jenkins, GitHub Actions, or GitLab CI.
    - Implement new CI/CD pipelines for new projects or enhance existing ones to improve efficiency and reliability.
- Infrastructure as Code (IaC):
    - Manage and provision infrastructure using IaC tools like Terraform, CloudFormation, or Ansible.
    - Ensure infrastructure is version-controlled, reproducible, and scalable.
- Automation and Scripting:
    - Develop and maintain scripts to automate repetitive tasks, such as deployment processes, server maintenance, and data backups.
    - Write and refine automation scripts using languages like Python, Bash, or PowerShell.
- Collaboration and Support:
    - Work closely with development teams to ensure seamless integration and deployment of new features and updates.
    - Provide support and guidance to developers on best practices for using CI/CD tools and infrastructure.
- Security and Compliance:
    - Implement security best practices and compliance requirements in the infrastructure and CI/CD pipelines.
    - Conduct regular security audits, vulnerability assessments, and apply patches or updates as needed.
- Performance Optimization: 
    - Analyze system performance and identify bottlenecks or inefficiencies.
    - Implement performance tuning and scaling strategies to ensure optimal application performance and user experience.
- Documentation and Knowledge Sharing:
    - Document processes, configurations, and troubleshooting steps to maintain a knowledge base.
    - Share knowledge with team members through documentation, training sessions, and code reviews.
- Research and Learning:
    - Stay up-to-date with the latest industry trends, tools, and technologies by reading blogs, attending webinars, and participating in professional development courses.
    - Experiment with new tools and practices that could benefit the team's workflow and improve system reliability and efficiency.
- Backup and Recovery Planning:
    - Ensure that proper backup and recovery mechanisms are in place and regularly tested.
    - Develop and maintain disaster recovery plans to minimize data loss and downtime in case of catastrophic events.
- Environment Management:
    - Manage different environments (development, testing, staging, production) to ensure consistency and reliability across the software development lifecycle.
    - Implement environment provisioning and de-provisioning processes to support dynamic infrastructure needs.
- This diverse set of activities ensures that I contribute to maintaining a robust, efficient, and secure DevOps environment, supporting the overall goal of delivering high-quality software reliably and continuously.

10. how do you resolve merge conflicts
- Resolving merge conflicts is a critical skill for a DevOps engineer, ensuring smooth integration of code changes. Here’s a step-by-step approach to resolving merge conflicts, along with best practices:

- Step-by-Step Approach to Resolving Merge Conflicts
    - Identify the Conflict: When attempting to merge branches (e.g., using git merge or git pull), Git will identify conflicts and notify you about the files that need resolution.
    - Review the Conflicted Files: Open each conflicted file to review the conflicting changes. Git marks conflicts within the file using markers:
    ```
    <<<<<<< HEAD
    Code from the current branch
    =======
    Code from the branch being merged
    >>>>>>> branch-to-merge
    ```
    - Analyze and Decide:  Analyze the differences between the conflicting changes. Decide how to merge the changes. This might involve keeping one version, combining both changes, or reworking the code to integrate both changes harmoniously.
    - Edit the Files:Manually edit the conflicted sections to resolve the conflict. Remove the conflict markers (<<<<<<<, =======, >>>>>>>) after resolving the conflicts.
    - Test the Changes: Ensure that the resolved code compiles and works as expected. Run automated tests to verify that the resolution did not introduce any issues.
    - Add and Commit the Resolved Changes: Once conflicts are resolved and tested, add the resolved files to the staging area `git add <conflicted-file`. Commit the resolved changes `git commit -m "Resolved merge conflict in <conflicted-file>"`.
    - Complete the Merge: 
    ```
    git merge --continue
    git push origin <branch-name>
    ```
11. Best Practices for Resolving Merge Conflicts
- Communicate with the Team:
    - Communicate with the team members involved to understand the context of their changes.
    - Collaboration can lead to better resolutions and prevent conflicts in the future.
- Frequent Merges and Rebases:
    - Regularly merge changes from the main branch into your feature branch to minimize the divergence and reduce the likelihood of conflicts.
    - Use rebase carefully to keep your branch up-to-date with the main branch without unnecessary merge commits.
- Use Visual Merge Tools:
- Utilize visual merge tools like kdiff3, meld, or integrated tools in IDEs like Visual Studio Code to help visualize and resolve conflicts more intuitively.
- Automate Tests:
    - Rely on automated testing to quickly identify any issues introduced during the conflict resolution process.
    - Ensure that comprehensive test coverage is in place to validate the changes.
- Documentation and Code Comments:
    - Document complex resolution decisions in the commit messages or code comments for future reference.
    - Clear documentation helps in understanding the reasoning behind the resolution.
- Review and Code Quality:
    - After resolving conflicts, consider having another team member review the changes to ensure quality and correctness.
    - Peer reviews can catch issues that might have been overlooked during the conflict resolution.

12. How do you work with developers and merge the code how it is going from development to production

- As a DevOps engineer, facilitating smooth collaboration between developers and ensuring seamless code integration from development to production involves a series of well-defined steps and practices. Here’s how I typically handle this process:

- Workflow for Working with Developers and Merging Code
- Collaboration and Communication: 
    - Daily Standups: Participate in daily standup meetings to sync with developers on the current status, upcoming tasks, and any blockers.
    - Communication Tools: Use collaboration tools like Slack, Microsoft Teams, or Jira to maintain constant communication and track progress.
- Branching Strategy:
    - Feature Branches: Developers work on feature branches created from the main branch. Each feature, bug fix, or improvement has its own branch.
    - Naming Conventions: Use clear and consistent naming conventions for branches, e.g., feature/login-button, bugfix/issue-123.
- Code Reviews and Pull Requests:
    - Pull Requests (PRs): Developers submit pull requests to merge their feature branches into the main branch. This is a key step where code is reviewed.
    - Code Reviews: Conduct thorough code reviews to ensure code quality, consistency, and adherence to coding standards. Use tools like GitHub, GitLab, or Bitbucket for PR management.
- Continuous Integration (CI):
    - Automated Tests: Ensure that each PR triggers automated tests (unit, integration, and end-to-end tests) through CI pipelines using tools like Jenkins, GitHub Actions, or GitLab CI.
    - Build Verification: Verify that the code builds correctly and passes all tests before it can be merged.
- Merge Conflicts:
    - Conflict Resolution: If a merge conflict occurs, work with the developer to resolve it. Review the conflicting changes, test the resolution, and ensure it integrates smoothly.
    - Best Practices: Encourage frequent merging of the main branch into feature branches to minimize conflicts.
- From Development to Production
- Staging Environment: 
    - Deploy to Staging: Once code is merged into the main branch, it is automatically deployed to the staging environment. This environment mimics production and is used for final testing.
    - Acceptance Testing: Conduct thorough testing in staging, including user acceptance testing (UAT), performance testing, and security testing.
- Continuous Deployment (CD):
    - Deployment Pipeline: Set up a deployment pipeline that automates the process of deploying code to staging and, eventually, production. Use tools like Jenkins, GitLab CI/CD, or AWS CodePipeline.
    - Approval Gates: Implement approval gates in the deployment pipeline where necessary. For example, manual approval might be required before deploying to production.
- Monitoring and Logging:
    - Monitor Staging: Use monitoring tools like Prometheus, Grafana, or ELK Stack (Elasticsearch, Logstash, Kibana) to monitor the staging environment for issues.
    - Log Analysis: Analyze logs to identify and fix any issues before they reach production.
- Production Deployment:
    - Scheduled Deployments: Plan production deployments during low-traffic periods to minimize user impact.
    - Zero Downtime: Use strategies like blue-green deployments or canary releases to achieve zero downtime during deployment.
- Post-Deployment:
    - Monitoring: Continuously monitor the production environment to ensure the deployment is successful and there are no performance or security issues.
    - Rollback Plan: Have a rollback plan in case something goes wrong. Ensure that you can quickly revert to a previous stable state if necessary.
- Feedback Loop:
    - Developer Feedback: Provide feedback to developers about any issues encountered in staging or production. This helps improve code quality and deployment practices.
    - Retrospectives: Conduct regular retrospectives to discuss what went well and what can be improved in the development and deployment process.
- Tools and Technologies
    - Version Control: Git, GitHub
    - CI/CD: Jenkins, AzureDevops
    - Infrastructure as Code (IaC): Terraform, AWS CloudFormation, Ansible
    - Containerization: Docker, Kubernetes
    - Monitoring and Logging: Prometheus, Grafana
    - Collaboration: Microsoft Teams, Jira
- By following these structured processes and using the appropriate tools, I ensure that code moves smoothly from development to production, maintaining high quality and reliability throughout the lifecycle.

- Terrafrom, Docker,  DevOps, jenkins, CI/CD, Kubernetes, 
- How do you implement DevOps in you project (5m)
- Write an ansible playbook, doker file, shell script, resource creation using terrafrom.
- Stages in pipeline
- how you are providing dev to prod automatically.
13. Is there any Diaster recovery 
Yes, disaster recovery (DR) is a critical aspect of our DevOps strategy to ensure business continuity and minimize downtime in case of unexpected failures. Our disaster recovery plan includes several key components and practices:
1. Data Backups:
 - Regular Backups: We perform regular backups of critical data, including databases and application configurations. These backups are automated and scheduled to run daily.
 - Offsite Storage: Backups are stored in multiple locations, including offsite storage and cloud storage solutions like AWS S3 or Azure Blob Storage, to protect against site-specific failures.
2. Infrastructure as Code (IaC):
 - Terraform Scripts: Our entire infrastructure is defined using Terraform scripts. This allows us to quickly recreate the infrastructure in a different region or environment if needed.
 - Version Control: All IaC scripts are version-controlled using Git, ensuring we have a history of changes and can roll back to a previous stable state if required.
3. Automated Recovery:
 - Continuous Integration/Continuous Deployment (CI/CD): Our CI/CD pipelines are designed to automatically deploy applications and configurations to any environment. In case of a disaster, we can rapidly redeploy our applications to a new environment using these pipelines.
 - Infrastructure Automation: Tools like Ansible and Kubernetes are used to automate the provisioning and management of infrastructure, further speeding up the recovery process.
4. Failover and Redundancy:
- High Availability: We design our systems for high availability with redundant components and failover mechanisms. For instance, we use load balancers to distribute traffic across multiple servers and databases are configured with replication.
- Multi-Region Deployment: Critical services are deployed across multiple regions to ensure availability even if one region goes down.
5. Disaster Recovery Drills:
 - Regular Testing: We conduct regular disaster recovery drills to test our DR plan. This includes simulating different disaster scenarios and measuring the time it takes to recover.
 - Continuous Improvement: Based on the results of these drills, we continuously improve our DR strategies and processes to ensure they are effective and up-to-date.
6. Monitoring and Alerts:
 - Proactive Monitoring: We use monitoring tools like New Relic, Prometheus, and Grafana to continuously monitor the health of our systems. This helps us identify potential issues before they escalate into disasters.
 - Automated Alerts: Automated alerts are configured to notify the team of any critical issues, enabling prompt action to mitigate potential disasters.
7. Documentation and Training:
 - Comprehensive Documentation: Detailed documentation of our DR plan, including steps to recover data, redeploy infrastructure, and restore services, is maintained and regularly updated.
 - Team Training: The team is regularly trained on DR procedures to ensure everyone knows their role and responsibilities in the event of a disaster.
- Summary
Our disaster recovery plan is designed to provide a robust framework for handling unexpected failures and ensuring business continuity. By leveraging automated backups, infrastructure as code, high availability architectures, regular testing, and comprehensive monitoring, we can quickly and efficiently recover from disasters with minimal impact on our operations.

#### Monolithic and Microservice
- Monolithic Architecture, the all components of application is tightly bounded and all the component code should write in same language if any component require updation we need to deploy the entire application. Ex: Finacial service like Banking
- Microservice Architecture, the component of applications are autonomous, each component can code with different language, any update in a component can achieve by deploying the service alone not the entire application. Ex: Swiggy