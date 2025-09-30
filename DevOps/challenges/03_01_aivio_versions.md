# AWS Lambda Version Management & Cost Optimization in Serverless Projects
As a DevOps engineer, I identified an issue in our serverless projects where Lambda versions were accumulating unnecessarily. The original Serverless framework setup included the **serverless-prune-plugin**, but during development some teams missed enabling it. This led to unpruned Lambda versions, which consumed storage beyond the default **75GB code storage limit**, eventually extending usage to **300GB** and increasing costs.

### Actions Taken

#### Temporary Fix

To control storage bloat, I implemented cleanup scripts that:

* Retrieved all Lambda functions.
* Listed available versions per function.
* Performed a **dry run** to identify deletable versions while keeping the last 4 versions.
* Executed cleanup to delete older versions across functions.

This ensured immediate cost savings and storage recovery.

#### Permanent Fix

I identified the missing **serverless-prune-plugin** in the deployment workflow and reintroduced it into the Serverless YAML configuration. This ensures only a limited number of old versions are retained automatically during deployments, preventing future cost spikes.

Additionally, I created a monitoring script to:

* Print function names with more than 4 versions.
* Help the team track functions where pruning isn’t working as expected.

### Outcome

* Reduced Lambda storage usage by cleaning up stale versions.
* Automated pruning process with **serverless-prune-plugin** for sustainable cost management.
* Provided visibility into version counts for proactive monitoring.

This approach delivered both an immediate fix and a long-term solution, ensuring efficient Lambda lifecycle management and cost optimization.

### Resume
Optimized AWS Lambda costs by cleaning stale versions with automation scripts and enforcing serverless-prune-plugin, reducing storage bloat and ensuring sustainable serverless lifecycle management
