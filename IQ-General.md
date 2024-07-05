#### Self Introduction
1. Tell me about yourself
2. curretly which project you are woking on  - ecommerce microservices
3. what are the tools - git, jenkins, terrafrom &ansible, docker & kubernetes, prometheus & grafana
4. what kind of technology used in the project - java
5. what are the roles and resposibilitie in the current project
    - Creating infrastrcuture for all environement DEV, STAG, PROD server
    - Deployment - Developer develops the code, we use to write dockerfile for that code to deploy.
    - Storing - we store the image using dockerhub.
    - Download dependencies -Ansible is used to download and install the multiple denpendencies in the host at a time.
    - CI/CD - jenkins pipeline is used to automate the entire things.
6. what are the challanges you have faced in the current project.
    - while deploying the code some times we face challanges, the deployment may get failure in that sitution we use to follow branching strategy create a feature branch from the main branch, in my senario the code will work fine at the developers end but not work on production side, there we found the bug and it will fix by developer but we need to provide branch strategy to them
7. what are branching strategy you are using.
    - current we are using github flow, once the code fixs the bug in the production server in feature branch and the application is working fine, we raise PR to mereg with main branch, this will reviewd by team memebers quality, functionality, need to approve before merging into main brach. Then we raise PR form production to stagging, once it is fixed we raise PR form stagging to Devlopment.
8. Difference between main brach and master branch
    - while create github repo wiht readme file main branch will create, else master branch will create.
#### Linux
- How will give the execution access to root (--root--group--others)
    ```
    mkdir devopspractice
    cd devopspractice
    touch file (will create file)
    chown root file
    ls -al (-rw-rw-r--)
    sudo chmod u+x file
    ls -al (will display -rwxrw-r--)
    ```
- How do you manage and view running  process
```
ps
ps -aux
top (used to check the CPU, Memory of different processor)
free ()
```
- SSH or Secure Shell is secure way to connect the remote linux computer. it is safe through encryption and authentication.
```
ssh username@hostname
ssh -p 2222 username@hostname (connect with port)
ssh -i keyname username@hostname (using pvt key)
```
- cronjob
- cronjob is scheduler in LINUX like OS, It will automate the repetitive task when and how often it should run.
```
crontab -e
select nano
* * * * *
```
- alias command is used save time and reduce type errors.`alias ku='kubectl'`
9. If we forgot the password for git client in local system how do you update
    - For a local system generate guthub token form github
10. Which Linux version you are using in your project.
    - Amazon Linux - use `yum` to install any package
    - Ubuntu - use `apt` to install any package.
    - Both are operating in Linux but the flovour (basic commands) is different
    - Amazon linux will come with default packages like `curl, wget`, but in ubuntu we need to install.
11. Difference between curl and wget
    - wget will downloading files from the internet
    - cure will downloading files and uploading data and suppourts various protocols and check the connection is established.
12. what is awk command in linux.
    - Aho, weinberger and kernighan command, basically used to text file to search the specific pattern in the files performance opertion on the matching lines.
    - Ex: awk '{print $2}' file.text will print second word of each line.
13. How do you check the free space in linux machine.
    - `df -h` or `du -shu path/directory`
14. what are groups in linux
    - Groups is used to add multiple users at a time to access the files.
15. How to check which user belongs to group.
    - id -G -n username -- -G tag retrives all group ids, -n gives name of th group
    - sudo groupadd groupname1
    - sudo useradd username1
    - sudo groupmod -a -U username1 groupnam1
    - sudo groups -- it will list all the groups
#### Sonarqube
16. what is quality profile in sonarqube
    - Sonarqude is used for checking code quality and continious inspection. We can create custom quality profile in tweo ways
        - by selecting the rules which we want to include
        - predefine quality profile is the sonarqube.
    - when a project is analyised, the rule that are defined in the quality profile used to evaluate the code and regenerate the report of code quality.
    - This will helps to find the bugs, security vunlnerabilites.
17. If my code quality get failed what will you do.
  -  we need to check the sonarqude for any bugs, if bug is arised from developer side we need to raise a ticket to fix the bug.
#### Jenkins
18. Master and Slave in Jenkins
    - Mater node is used to manage the slave instance, suppouse 100 builds need to run if it is done in master then it will cause performance issue, the master will distrubute the jobs to slave to perform the tasks. 
19. If Master node is failed what will happen.
    - First we need to check the reason for its failure issues like connectivity, Volume is extended or not. If Master is failed the jobs in slave wont get effected but we lost control/manage over the slave, in order to avoid this we need to keep backup.
20. If Master is down how we can run the jobs
    - we can acces the path /var/lib/jenkins/ and find the jobs and we can take the backup from the existing server, taking the volumes and associate with the new server and can set the jenkins in nwe instance.
21. syntax
    pipeline{
        agent any
        stages{
            stage ('stage1){
                steps{
                    echo "This is stage 1"
                }
            }
            stage (stage2){
                steps {
                    echo "This is stage 2"
                }
            }
        }
    }
22. Different stage in jenkins pipeline
    - checkoutstage - get code form the source repo
    - Build and UT
    - code scan
    - build image
    - image scan
    - image push
    - deploy in preproduction server
    - test the code
    - deploy to production server
23. What if i give same build name for the different stages
    - Build will fail and throw an error stage alreafy exists
24. Suppose the first stage get failed what happen to other stages
    - Depends on the configuration, based on `post build actions`
        - success -
        - failure - if any stage got failure it wont execute the other stages.
        - always - even a stage got failed the other stages will execute.
25. what plugins that you are used in jenkins
    - Thinbackup - for backups
    - Deploy to container - to deploy to tomcat web servers
    - Roll based authenication - to give authentication for users.
    - nexus - to store arifacts.
    - publish over ssh
26. How to tigger one job to other job
    - UI option - In jenkins dashboard choose `Build after other job is build`.
    - we can use when option to trigger particular stage
    when{
        expression{
            "${env.variable}" = "YES"
        }
    }
#### Ansible
27. ansible script
```
---
- name: Ansible Syntax for reference
  hosts: dev
  user: ansible
  become: yes
  connection: ssh
  tasks:
    - name: install git in remote repo
      apt: >
      name=git
      state=present
```
- What is become: yes
    - It will act as root user, here we are using user ansible which is non root user we need `sudo` to install the command to avoid this we use become: yes.

28. In your project where you use ansible can you expalin an senario.
 - Consider an Environmet DEV or UAT there are 100`s of servers are available if devleoper wants to clone the source code from the git, manually installing is not possible all the servers, we can configure the system by writing an ansible playbook, If i write and execute the playbook in my local system it will automatically installed in host machines (DEV) environment.
29. How can i copy the files from one server to another servers
    - write a playbook or inventories
    - In ansible configuration file we need to ucomment the inventory
    - In the server we need to add the user `ansible` and provide `password`
    - we need to generate a key from the master server using `ssh-keygen` and copy the key from master server to any other slave servers.
#### Docker
30. Docker is containerization tool to create containers, it is virtual machine that doesnot have any operating system, used to create and run the applications.In VM above the Hypervisor we can have different guest OS for different application, but in container above Hypervisor, guest os and container engine (continerd). 
31. Explain about dockerfile
    - It is text file with set of instructions to buld the image t
    - Docker file contian componets like RUN, WORKDIR, LABEL, ARG, COPY, RUN, EXPOSE, ENV, CMD.
    - RUN command is used to buid the image, CMD is used to execute the commands while we run the image
#### Kubernets
32. what is a pod
 - It is smallest unit in kubernets application that can deploy and managed the containers. It represents single instance of running processor of a cluster. Pod is a basic building block of kubernetes cluster. A single pod contains one or more number of containers. kuberenets can manage the lifecyle of pods and thier components.
 33. write a pod manifest
 `kubectl create deployment app1 --image sreeharshav/fastapi:v1 --replicas 6 --dry-run -o yml > deployment.yml` and `kubectl apply -f deployment.yml`.
 - `kubectl expose app1 --port -80 --type Nodeport --dryrun -o -yml > service.yml` and `kubectl apply -f service.yml`
 34. How do you create pods in the project.
 - Using command deploy the n node cluster, intally the cluster dont have pods `kubectl get pods` if you run `kubectl run testpod1 --image nginx:latest` we can see pods that deployed, this pods has unique network identity and communicate with another pod also.
 35. what is statefullset in kubernetes.
 - Each pod in kubernetes satefullset is assigned with stable network identity(hostname) based on `ordinal index` EX: stateful name `mysql` than hostname is `mysql0, mysql1`. 
 - It will follow order while deploying whenever a failure occurs and recreation takes place.
 - This will suppourt persistant volumes (PV) and Persistant volume claims(PVC) to provide stable and persistance storge.
#### AWS
36. If i lost the pem file of ec2 can i connect to that
- Multiple ways to connect using `ssh-keygen` we can generate `id_rsa` and `id_rsa.pub` and
- we can generate a new pem file and paste the key. 
37. L4 and L7 loadbalancer
    - L4 is network load balancer simple and effective TCP & UDP non http and https traffic
    - L7 is an application load balancer 80-http, 443-https that suppouts redirection that suppourt advance traffic managments
38. NAT Gateway
    - IGW is used to connect the public server where as NAT gateway with Elastic IP is used to connect the private subnet server.
39. Can we connect one vpc to another vpc
    - It is possible by using `vpc peetring`
40. what is NACL and SG?
    - SG are statefull firewall it doesnot require seperate ports to open response traffic Ex: EC2, LAMBDA
    - NACL Network Access Control Lists is applicable to subnets only, they are stateless firewall Inbound(Ingress) and outbound(egress) should open.
    - Inbound is connected in one port, Eformal port in NACL the outbould should connect in another port.
41. 
4. expalin the architecture you recently work on