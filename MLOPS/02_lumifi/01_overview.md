# Lumifi Dental – Regression-Based MLOps Implementation

## Business Problem

Lumifi Dental wanted to leverage Machine Learning to predict:

- Treatment cost estimation
- Insurance claim amount prediction
- Appointment duration prediction
- Revenue forecasting

The primary production use case was:

## Treatment Cost Prediction

Predict the estimated treatment cost before treatment begins.

---

# MLOps Architecture

```text
Patient Records
Appointment Data
Treatment History
Insurance Data
      ↓
Feature Engineering
      ↓
Regression Model
      ↓
Predicted Treatment Cost
      ↓
Dentist / Front Desk
```

---

# Regression Use Case

## Treatment Cost Estimation

### Input Features

| Feature | Description |
|----------|------------|
| patient_age | Patient age |
| treatment_type | Root canal, implant, filling, etc. |
| treatment_complexity | Low, Medium, High |
| appointment_duration | Estimated treatment time |
| insurance_coverage_percentage | Insurance coverage |
| previous_treatment_cost | Historical treatment cost |
| dentist_experience | Years of experience |
| number_of_visits | Historical visits |
| medical_history_score | Risk score |
| treatment_material_cost | Material expenses |

---

## Output

```text
Estimated Treatment Cost = $2,350
```

Since the output is numerical, this is a:

### Regression Problem

---

# Feature Engineering

Raw EHR data cannot be directly used by ML models.

## Example

### Raw Data

```text
Treatment Type = Root Canal
```

### Encoded Data

```text
Treatment_Root_Canal = 1
```

---

## Derived Features

### Cost Per Visit

```text
total_previous_cost / number_of_visits
```

---

### Average Treatment Duration

```text
total_treatment_hours / total_visits
```

---

### Insurance Impact Score

```text
treatment_cost × coverage_percentage
```

---

### Patient Loyalty Score

```text
Years with clinic
```

---

# Algorithms Used

## 1. Linear Regression

### Purpose

Used as a baseline model because it is simple and explainable.

### Formula

```text
y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ
```

### Hyperparameters

- fit_intercept
- positive

---

## 2. Random Forest Regressor

### Purpose

Used because healthcare costs often have nonlinear relationships.

### Example

```text
Age + Insurance + Treatment Complexity
```

do not always follow a straight-line relationship.

### Hyperparameters

| Hyperparameter | Value |
|---------------|---------|
| n_estimators | 100 |
| max_depth | 10 |
| min_samples_split | 5 |
| min_samples_leaf | 2 |

---

## 3. XGBoost Regressor

### Purpose

Production model because it provided the highest accuracy.

### Advantages

- Handles complex treatment cost patterns
- Captures insurance effects
- Learns treatment combinations effectively

### Hyperparameters

| Hyperparameter | Value |
|---------------|---------|
| learning_rate | 0.1 |
| max_depth | 6 |
| n_estimators | 200 |
| subsample | 0.8 |
| colsample_bytree | 0.8 |

---

# Performance Metrics

For regression models, we do **not** use:

- Accuracy
- Precision
- Recall
- F1-Score

Instead, we use:

---

## MAE (Mean Absolute Error)

Measures average prediction error.

### Example

```text
Actual Cost = $2000
Predicted Cost = $1900

Error = $100
```

---

## RMSE (Root Mean Squared Error)

Measures prediction error while penalizing larger mistakes more heavily.

---

## R² Score

Measures how much variance is explained by the model.

### Example

```text
R² = 0.90
```

Meaning:

```text
Model explains 90% of data variation
```

---

# MLflow Implementation

Used for:

- Experiment tracking
- Hyperparameter tracking
- Metric logging
- Model versioning
- Artifact management

### Example

```python
mlflow.log_metric("rmse", 125)
mlflow.log_metric("mae", 85)
```

---

# Model Registry Workflow

```text
Training
   ↓
Validation
   ↓
MLflow Registry
   ↓
Staging
   ↓
Production
```

---

# CI/CD for MLOps

```text
GitHub Commit
      ↓
GitHub Actions
      ↓
Unit Tests
      ↓
Model Validation
      ↓
Docker Build
      ↓
Deploy Lambda Prediction Service
```

---

# Data Drift Detection

## Example

### Training Data

```text
Average Treatment Cost = $1500
```

### Current Production Data

```text
Average Treatment Cost = $2800
```

Cost distribution has changed significantly.

### Action

Trigger retraining pipeline.

---

# Model Drift Detection

Monitor:

```text
Predicted Cost
vs
Actual Final Cost
```

If:

- RMSE increases significantly
- MAE exceeds threshold

then:

```text
Retraining Triggered
```

---

# Retraining Pipeline

```text
RDS
 ↓
Feature Engineering
 ↓
Model Training
 ↓
Validation
 ↓
MLflow
 ↓
Model Registry
 ↓
Deployment
```

---

# Production Monitoring

## Monitored Metrics

- RMSE
- MAE
- R² Score
- Prediction latency
- Lambda execution failures
- API response times

## Monitoring Tools

- CloudWatch Logs
- CloudWatch Metrics
- MLflow Dashboard

---

# Security Implementation

- AWS IAM (Least Privilege Access)
- AWS Secrets Manager
- SSL/TLS Everywhere
- VPC Isolation
- WAF Protection
- Audit Logging

---

# Production Challenges

## Data Quality Issues

- Missing insurance information
- Incorrect treatment codes
- Duplicate patient records

### Solution

- Validation rules
- Data cleansing pipelines

---

## Data Drift

- Treatment costs changed over time
- Insurance coverage policies changed

### Solution

- Drift monitoring
- Automated retraining

---

## Deployment Challenges

- Lambda package dependencies
- Environment consistency
- Rollback handling

### Solution

- CI/CD pipelines
- Versioned model deployments
- Registry-based rollbacks

---

# Interview Summary

> Lumifi Dental implemented a regression-based MLOps workflow for treatment cost prediction. We engineered features from patient demographics, treatment history, appointment data, and insurance coverage. We evaluated Linear Regression, Random Forest Regressor, and XGBoost Regressor, with XGBoost providing the best production performance. We used MLflow for experiment tracking, Model Registry for lifecycle management, GitHub Actions for CI/CD, CloudWatch for monitoring, and automated retraining based on drift detection and model performance degradation.