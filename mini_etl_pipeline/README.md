# 🧪 Mini ETL Data Pipeline with Airflow, PostgreSQL & Docker

A personal ETL pipeline project showcasing how to orchestrate data extraction, transformation, and loading using Apache Airflow.

## 📌 Project Overview

This project implements a complete mini ETL workflow:
- Extracts weather or currency exchange data from a public API.
- Stores raw data locally or on S3-like storage.
- Transforms and cleans data using Python.
- Loads cleaned data into a PostgreSQL database.
- All steps are orchestrated via an Airflow DAG.

## 🛠 Tech Stack

- Apache Airflow (via Docker Compose)
- Python (for ETL scripts)
- PostgreSQL
- Docker

## 🧠 What I Did

- Built modular ETL scripts (`extract`, `transform`, `load`) using Python.
- Designed and implemented a DAG using Airflow’s `PythonOperator`.
- Dockerized the entire system for portability and reproducibility.
- Applied logging and error handling to improve observability.
- Managed PostgreSQL as the final data sink.

## 📁 Folder Structure
```yaml
mini_etl_pipeline/
├── dags/ # Airflow DAGs
├── data/ # Raw and processed data
├── scripts/ # ETL scripts
├── docker-compose.yml # Full pipeline infrastructure
└── requirements.txt
```

## ✅ What I Learned

- Hands-on orchestration with Airflow
- Structuring ETL pipelines in modular fashion
- Building reproducible data workflows with Docker
- Integrating external APIs and relational databases
