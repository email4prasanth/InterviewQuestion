```sh
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         THINKRD365 - LAKEHOUSE ARCHITECTURE                         │
└─────────────────────────────────────────────────────────────────────────────────────┘

    RAW DATA SOURCES                    BRONZE LAYER                    SILVER LAYER
         (S3/Blob)                      (Raw Ingestion)                (Cleaned Data)
              │                               │                              │
    ┌─────────┼─────────┐             ┌───────┼───────┐              ┌────────┼────────┐
    │         │         │             │       │       │              │        │        │
    ▼         ▼         ▼             ▼       ▼       ▼              ▼        ▼        ▼
┌───────┐ ┌───────┐ ┌───────┐    ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
│Payroll│ │Attend-│ │  Tax  │    │ Bronze  │ │ Bronze  │ │ Bronze  │ │ Silver  │ │ Silver  │
│  CSV  │ │ ance  │ │Decla- │───▶│ Payroll │ │Attend-  │ │  Tax    │─▶│ Payroll │ │Employee│
│Files  │ │ CSV   │ │ration │    │  Raw    │ │ ance    │ │  Raw    │ │ Clean   │ │ Master  │
└───────┘ └───────┘ └───────┘    └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
                                              │                              │
                                              │                              │
                                         ┌────┴────┐                    ┌────┴────┐
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