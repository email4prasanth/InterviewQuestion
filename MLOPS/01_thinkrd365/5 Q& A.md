1.  do you mean for 3 different use case employe attrition, tax risk and payroll anamoly are you using single model or 3 different models
- We used three separate ML models because each use case had different business objectives and feature sets. Employee attrition prediction, payroll anomaly detection, and tax validation risk detection were treated as independent ML pipelines with separate training, tracking, evaluation, and deployment processes.

2. Suppose if one model fails does it impact other two microservices, each with its own CI/CD pipeline Or Pipeline job trigger when there is change, and all services share a common dependency/library.
- Each ML use case in ThinkRD365 was deployed as an independent microservice with separate CI/CD pipelines and isolated containers, so failure in one model service typically did not impact the others. However, since some preprocessing and utility libraries were shared across services, dependency management became important. We handled this using versioned common libraries, container isolation, integration testing, and rollback strategies to avoid cross-service impact.
- Scenario 1 — One Model Fails , only specfic micorservice will get impact.
- Scenario 2 — Shared Dependency Problem over come by
    - Versioned Shared Libraries Example: common-ml-utils v1.2, common-ml-utils v1.3
    - Independent CI/CD Validation
    - Backward Compatibility Testing - regression tests executed, compatibility validation done
    - Container Isolation- Each service packaged separately
