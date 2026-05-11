- Kubernetes
- Do you worked on production release
Yes, I worked on production releases in a microservices-based project called “interaction-chatbot” in the THRD365 project.

The data science team prepared and cleaned the data using data wrangling techniques. Based on the use case, we identified it as a regression problem and trained multiple models like Random Forest and Gradient Boosting with hyperparameter tuning in Jupyter notebooks.

Once the model performance was validated, my role as a DevOps engineer was to containerize the application using Docker, manage CI/CD pipelines, push images to ECR, and deploy the application into Kubernetes production environments with proper monitoring and scaling.

- Did you get a chance to work on auto scale
Yes, I have knowledge of Kubernetes autoscaling using HPA (Horizontal Pod Autoscaler) and VPA (Vertical Pod Autoscaler).
We configured minimum and maximum pod replicas based on CPU and memory utilization to handle varying traffic loads.
I was involved in monitoring and understanding the setup, although the primary implementation was handled collaboratively within the team.

- Briefly discribe about the Control and worker node
The Kubernetes Control Plane manages the overall cluster operations. It consists of:
kube-apiserver → handles API requests
etcd → stores cluster state information
kube-scheduler → schedules pods to worker nodes
kube-controller-manager → maintains desired cluster state

Worker nodes are responsible for running application workloads. They consist of:
kubelet → communicates with the control plane
kube-proxy → handles networking and service communication
container runtime → runs containers such as Docker or containerd

- how do you notice the container is not working
First, I check the pod status using **kubectl get pods**.
If the pod is in CrashLoopBackOff, Error, or Restarting state, I inspect logs using **kubectl logs** and **kubectl describe pod**.

I also verify:
    - container health probes
    - resource utilization
    - port mappings
    - environment variables
    - image pull issues
For monitoring and alerting, we use Prometheus and Grafana dashboards to identify application or infrastructure-level problems.

- is the image creation is your responsibility or developers?
Image creation is a collaborative responsibility between developers and DevOps engineers.
Developers usually provide the application requirements, dependencies, and startup commands.
As a DevOps engineer, I review and optimize the Dockerfile by:
selecting secure and lightweight base images
suggesting multi-stage builds
reducing image size
improving security and compatibility
After validation, we build and push the image through the CI/CD pipeline for deployment.

- mlops
- what is the recent project you worked on mlops
Recently, I worked on a microservice called “interaction-chatbot” in the THRD365 project.

The project involved preparing and processing data, training machine learning models, tracking experiments using MLflow, containerizing the application using Docker, and deploying it through CI/CD pipelines into Kubernetes environments.

We evaluated multiple regression models such as Random Forest and Gradient Boosting with hyperparameter tuning before moving the best-performing model into production.

- what is the pyspark where it is used
PySpark is the Python API for Apache Spark.

It is mainly used for distributed data processing and handling large-scale datasets efficiently across clusters.

PySpark is commonly used in:

big data processing
ETL pipelines
machine learning workflows
real-time analytics

Compared to normal Python processing, PySpark is faster for huge datasets because it distributes the workload across multiple nodes.

- what is the contribution did you gave
My contribution was mainly from the DevOps and MLOps side.
I worked on:
Docker image creation and optimization
MLflow integration for experiment tracking, dvc for data version and model registry for model version.
CI/CD pipeline setup using GitHub Actions
Kubernetes deployment
monitoring using Prometheus and Grafana
managing deployments and troubleshooting production issues

I also collaborated with the data science team during model deployment and validation stages.
- how do you move the working model to production
Once the model performance is validated, we package the model along with its dependencies using Docker.

The model artifact is versioned and tracked using MLflow.

Then the CI/CD pipeline automatically:

builds the Docker image
pushes it to the container registry
deploys it into Kubernetes

After deployment, we monitor:

model performance
application logs
latency
resource usage

If everything is stable, the model becomes part of the production environment.
- is mlfow is a open source?
Yes, MLflow is an open-source platform mainly used for:
experiment tracking
model versioning
artifact management
model registry
deployment lifecycle management

- did you tag manually or automatically
We mainly used automatic tagging through the CI/CD pipeline.

For example:

Git commit SHA
build number
release version

- what is data drift how did you noticed it
Data drift happens when the incoming production data distribution changes compared to the training data.

Due to this, model accuracy may reduce over time.

We identified data drift by:

monitoring prediction patterns
comparing training and production datasets
checking sudden drops in model performance metrics
observing abnormal prediction behavior

Monitoring dashboards and validation reports helped us identify such deviations
- you said hyperparameter tunning how do you select?
Hyperparameter tuning is done to improve model performance.

We select parameters based on:

model type
dataset characteristics
evaluation metrics

We experimented with combinations such as:

learning rate
number of estimators
tree depth
batch size

using techniques like Grid Search or Random Search and selected the configuration that produced the best evaluation score with minimal overfitting.
- you said only 32 dolars is optimized cost how did you achieved?
- how do you check the logs?
We check logs at multiple levels.

Kubernetes level:

kubectl logs
kubectl describe pod

Container level:

Docker container logs

Monitoring level:

Prometheus alerts
Grafana dashboards

For centralized logging, logs can also be integrated with tools like CloudWatch depending on the environment.
- you grafana how it is implemented
Grafana is used as a visualization and monitoring dashboard.

Prometheus collects metrics from Kubernetes clusters and applications, and Grafana connects to Prometheus as a data source.

We created dashboards for:

CPU usage
memory usage
pod restarts
application health
response time
request metrics

Alerts were also configured to notify when thresholds exceeded acceptable limits.
- project
- what is the main purpose of kafka
Apache Kafka is mainly used for real-time data streaming and message processing between systems.

Its main purposes are:

asynchronous communication
handling high-throughput data streams
decoupling microservices
real-time event processing

Kafka works using producers, topics, and consumers where messages are published and consumed reliably.
- Github
- Did you created end to end CICD pipeline