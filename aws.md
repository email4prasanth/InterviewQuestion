- **What are the six pillars of cloud __RSSCOP__**
    - Reliability-applications are highly available, robust & capable of recovering from faults.
    - Security -protection
    - Sustainability- best practices and improvement to meet targets
    - Cost optimization - 
    - Operational expenses- support dev and run work efficiently
    - Performance efficiency- decision-making process

- **What are the tools and techniques that you can use in AWS to identify if you are paying more than you should be, and how to correct it?**
    - Cost Managment Console -show top 5 services used
    - cost explore - gives past 13 months usage and forecast next 3 months
    - AWS Budget - Gives currnet plan will meet the budget 

- **Define and explain the three basic types of cloud services and the AWS products that are built based on them?**
    - Network- VPC, Amazon cloud front, Route53
    - Computing-EC2, Elastic Beanstalk, lambda, Auto-Scaling 
    - Storage - S3, Glacier, Elastic file system, Elastic Block storage

- **Name some of the AWS services that are not region-specific (global)**
    - IAM
    - Route 53
    - Web Application Firewall 
    - CloudFront

#### EC2
- Using VPC a specified IP address can an EC2 instance can launch.

- **Define Amazon EC2 regions and availability zones?**
    - AR conatins one or mor AZ (geographical location), failure in one zone wont effect the on EC2 instances
- **Explain Amazon EC2 root device volume?**
    - Using AMI a new EC2 instance can launch, Image is used to boot an EC2 instance is stored on the root device drive. This device volume is suppourted by EBS or instance store, this will not effected by the lifespan of EC2 instance.

#### AutoScaling
- **What is auto-scaling?**
Based on demand automatically increasing or decreasing of resource (new instance)

#### CloudFront
- **What is geo-targeting in CloudFront?**
- showing personalized content to their audiance based on geographical location

#### CloudFormation
- **What are the steps involved in a CloudFormation Solution?**
    - create or use existing cloud formation template using JSON or YAML
    - store the cloud formation solution in local or s3 bucket
    - using this cloud formation to create stack on your template
    - AWS Cloud formation is used to construct and configure stack resource on your template.
- **Is there any other alternative tool to log into the cloud environment other than console\portal?**
    - Putty
    - windows power shell
    - aws cli linux
    - aws cli windows
    - aws cdk
    - eclipse


#### Amazon CloudWatch
- **What is CloudWatch?**
- The Amazon CloudWatch has the following features:

    - Depending on multiple metrics, it participates in triggering alarms.
    - Helps in monitoring the AWS environments like CPU utilization, EC2, Amazon RDS instances, Amazon SQS, S3, Load Balancer, SNS, etc.
- **What services can be used to create a centralized logging solution?**
    - The essential services that you can use are Amazon CloudWatch Logs, store them in Amazon S3, and then use Amazon Elastic Search to visualize them. You can use Amazon Kinesis Firehose to move the data from Amazon S3 to Amazon ElasticSearch.
- **How do you set up a system to monitor website metrics in real-time in AWS?**
- Amazon CloudWatch helps you to monitor the application status of various AWS services and custom events. It helps you to monitor:
    - State changes in Amazon EC2
    - Auto-scaling lifecycle events
    - Scheduled events
    - AWS API calls
    - Console sign-in events

#### RDS
- **Will your standby RDS be launched in the same availability zone as your primary?**
    - NO, stanby instance lauch in different AZ. If the primary instance fails, the back up instance will assits in recovering all the data.

#### Security
- **What are the native AWS Security logging capabilities?**
- Most of the AWS services have their logging options. Also, some of them have an account level logging, like in AWS CloudTrail, AWS Config, and others. When a new logs are deliverd Simple Notification Service (SNS) it will send Notification.
    - AWS CloudTrail -  Provides a history of the AWS API calls for every account. It lets you perform security analysis, resource change tracking, and compliance auditing of your AWS environment as well.
    - AWS Config  - Understand the configuration changes that happen in your environment. This service provides an AWS inventory that includes configuration history, configuration change notification, and relationships between AWS resources.
- **What is a DDoS attack, and what services can minimize them?**
- It is a cyber attack creates multiple session so that other legitimate user cannot access the service. The following Native Tools will Help to Deny DDoS
    - AWS Sheld
    - AWS WAF
    - Amazon Route53
    - Amazon CloudFront
    - ELB
    - VPC

#### Media Services
- **What is an Elastic Transcoder?**
    - To support multiple devices with various resolutions like laptops, tablets, and smartphones, we need to change the resolution and format of the video. This can be done easily by an AWS Service tool called the Elastic Transcoder

#### RDS - Relational Database Service
#### Snapshots
- **Define Snapshots in Amazon Lightsail?**
    - Resource can be restored using snapshots. Snapshots is backups of EC2 instances, block storage drives, databases done manually or automatically. 

#### Senario Based Questions
- **What is the difference between a Spot Instance, an On-demand Instance, and a Reserved Instance?**
    - Spot Instance - unused instance that user can use at reduced cost
    - Ondemand Instance - pay for computing resource without making longterm obligations.
    - Reserved Instance - allow you to specify attribute (AZ, AR, Instance type, platform, tenancy).
- **On an EC2 instance, an application of yours is active. Once the CPU usage on your instance hits 80%, you must reduce the load on it. What strategy do you use to complete the task?**
    - AutoScaling group is used to deploy additional instance when ever the desired upper threshold hits,
- **Multiple Linux Amazon EC2 instances running a web application for a firm are being used, and data is being stored on Amazon EBS volumes. The business is searching for a way to provide storage that complies with atomicity, consistency, isolation, and durability while also increasing the application's resilience in the event of a breakdown (ACID). What steps should a solutions architect take to fulfill these demands?**
    - AWS Auto Scaling groups can create an application load balancer that spans many availability zones. Mount a target on each instance and save data on Amazon EFS (Amazon Elastic File System).
- **Your business prefers to use its email address and domain to send and receive compliance emails. What service do you recommend to implement it easily and budget-friendly?**
    - Amazon Simple Email Service (Amazon SES), a cloud-based email-sending service, which allows you to send bulk emails to customers swiftly at a minimal cost.
- what is Burstable and non burstable instance.
    - The base price of burstable instance is 15% cheaper than non-burstable, with burstable instance cpu utilization limits:30% for t3.large 
