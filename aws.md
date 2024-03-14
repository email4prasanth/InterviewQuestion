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
- **What services can be used to create a centralized logging solution?**
    - The essential services that you can use are Amazon CloudWatch Logs, store them in Amazon S3, and then use Amazon Elastic Search to visualize them. You can use Amazon Kinesis Firehose to move the data from Amazon S3 to Amazon ElasticSearch.
- **How do you set up a system to monitor website metrics in real-time in AWS?**
- Amazon CloudWatch helps you to monitor the application status of various AWS services and custom events. It helps you to monitor:
    - State changes in Amazon EC2
    - Auto-scaling lifecycle events
    - Scheduled events
    - AWS API calls
    - Console sign-in events


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

#### senario based
