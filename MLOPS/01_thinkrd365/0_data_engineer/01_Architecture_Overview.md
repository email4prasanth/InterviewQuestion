```sh
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         THINKRD365 - LAKEHOUSE ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

    RAW DATA SOURCES                    BRONZE LAYER                     SILVER LAYER
         (S3/Blob)                      (Raw Ingestion)                 (Cleaned Data)
              │                               │                               │
    ┌─────────┼─────────┐             ┌───────┼───────┐               ┌────────┼────────┐
    │         │         │             │       │       │               │        │        │
    ▼         ▼         ▼             ▼       ▼       ▼               ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐    ┌─────────┐ ┌─────────┐ ┌─────────┐  ┌─────────┐ ┌─────────┐
│Payroll│ │Attend-│ │  Tax  │    │ Bronze  │ │ Bronze  │ │ Bronze  │  │ Silver  │ │ Silver  │
│  CSV  │ │ ance  │ │Decla- │───▶│ Payroll │ │Attend-  │ │  Tax    │──▶│ Payroll │ │Employee│
│Files  │ │ CSV   │ │ration │    │  Raw    │ │ ance    │ │  Raw    │  │ Clean   │ │ Master  │
└───────┘ └───────┘ └───────┘    └─────────┘ └─────────┘ └─────────┘  └─────────┘ └─────────┘
                                              │                              │
                                              │                              │
                                         ┌────┴───┐                    ┌────┴────┐
                                         │ Change │                    │ Data    │
                                         │ Data   │                    │ Quality │
                                         │ Feed   │                    │ Rules   │
                                         └────────┘                    └─────────┘

    GOLD LAYER                          ML FEATURE LAYER                PREDICTION LAYER
 (Aggregated Data)                        (ML Ready)                      (Outputs)
         │                                     │                                 │
    ┌────┼────┐                          ┌─────┼─────┐                      ┌─────┼─────┐
    │    │    │                          │     │     │                      │     │     │
    ▼    ▼    ▼                          ▼     ▼     ▼                      ▼     ▼     ▼
┌───────┐ ┌───────┐ ┌───────┐      ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
│  Dim  │ │  Dim  │ │  Dim  │      │ Payroll  │ │Attrition │ │   Tax    │ │Anomaly   │ │Attrition │
│Employee│ │  Time  │ │Country│      │Features  │ │Features  │ │Features  │ │Predictions│ │Predictions│
└───────┘ └───────┘ └───────┘      └──────────┘ └──────────┘ └──────────┘ └──────────┘ └──────────┘
    │         │         │                 │            │            │            │            │
    └────┬────┘         │                 └─────┬──────┘            └─────┬──────┘
         │              │                       │                         │
         ▼              ▼                       ▼                         ▼
    ┌────────────────────────────────┐    ┌─────────────┐           ┌─────────────┐
    │     fact_payroll (Fact Table)   │    │   MLflow    │           │   HR Dash   │
    │  (Star Schema - Central Table)  │    │ Experiment  │           │   PowerBI   │
    └────────────────────────────────┘    │   Tracking  │           │   Tableau   │
                                           └─────────────┘           └─────────────┘
```
- Primary Key, Forigen Key, Surrogate Key Explained

┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           fact_payroll (Child Table)                                │
├─────────────────┬─────────────────┬──────────────────┬─────────────┬────────────────┤
│ payroll_sk (PK) │ employee_id     │ employee_sk (FK) │ salary_date │ salary_amount  │
│ (Surrogate Key) │ (Natural ID)    │ (FK to Parent)   │             │                │
├─────────────────┼─────────────────┼──────────────────┼─────────────┼────────────────┤
│ 1001            │ 101             │ 5001             │ 2024-01-31  │ 85,000         │─── Rajesh's payroll
│ 1002            │ 101             │ 5001             │ 2024-02-29  │ 87,000         │─── Rajesh's another payroll
│ 1003            │ 102             │ 5002             │ 2024-01-31  │ 65,000         │─── Priya's payroll
│ 1004            │ 103             │ 5003             │ 2024-01-31  │ 95,000         │─── Amit's payroll
└─────────────────┴─────────────────┴──────────────────┴─────────────┴────────────────┘