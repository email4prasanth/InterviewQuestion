## Suppose you have 4 microservices, each with its own CI/CD pipeline, and all services share a common dependency/library.

How would you design the pipeline so that:
1. If a change happens in one microservice, only that specific service pipeline runs.
2. If a change happens in the shared dependency, only the impacted services are rebuilt/redeployed.
3. Unnecessary deployments of unaffected microservices are avoided.

Explain the CI/CD strategy, dependency management, and deployment optimization approach you would use.
```text
# Selective CI/CD Triggering in Microservices with Shared Dependency

Suppose we have 4 microservices in a monorepo:

```text
service-a/
service-b/
service-c/
common-lib/
```

All services depend on `common-lib`.

---

#### Scenario 1: Change inside `service-a` only

Only `service-a` pipeline should trigger.

This is done using:
- path-based triggers,
- conditional stages/jobs,
- or Git diff detection.

Example:

```yaml
trigger:
  paths:
    include:
      - service-a/**
```

Or in Jenkins/GitHub Actions/GitLab:
- detect changed folders using `git diff`
- trigger only impacted service pipeline.

---

#### Scenario 2: Change inside `common-lib`

Since all services depend on `common-lib`, all affected services may need:
- rebuild,
- retest,
- redeploy.

But unnecessary deployments should be avoided if compatibility is maintained.

---

# Possible Solutions

#### Option A — Versioned Shared Library (Best Practice)

Convert `common-lib` into:
- separate package,
- artifact,
- or internal library.

Each microservice uses a fixed version:

```text
service-a -> common-lib v1.2
service-b -> common-lib v1.2
```

If `common-lib` changes:
- publish new version,
- only services upgrading to new version rebuild.

This isolates pipelines completely.

---

#### Option B — Dependency Graph Impact Analysis

Use tools like:
- Nx,
- Bazel,
- Gradle dependency graph,
- custom scripts.

Pipeline determines:
- which services are impacted by the changed dependency.

Only impacted services run.

---

#### Option C — Contract Testing / Backward Compatibility

If `common-lib` changes but public contracts remain same:
- only library tests run,
- no redeploy needed.

If there is a breaking change:
- rebuild dependent services.

---

# Key Concepts Expected by Interviewer

The interviewer was likely expecting concepts such as:

- Monorepo pipeline optimization
- Selective deployment
- Dependency graph analysis
- Path-based triggers
- Shared library versioning
- Impacted service detection
- Backward compatibility
- CI/CD orchestration
```
---
- Python code to find the duplicates
- Azure databricks, Aws Sagemaker.
- Github issue faced during production deployment.
- Data drift is identified?
- does the github stores the versions??
- Which is better server or serverless??
- How you troblue shoot the production issues?

