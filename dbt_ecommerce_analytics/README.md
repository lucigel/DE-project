# 📊 E-commerce Analytics Warehouse with dbt & PostgreSQL

A personal data modeling project to simulate an analytics warehouse using dbt and PostgreSQL.

## 📌 Project Overview

This project simulates an analytics layer for an e-commerce business:
- Starts from raw transactional data (e.g. orders, customers).
- Transforms into cleaned staging tables.
- Builds star-schema dimensional models for analysis.
- Adds data testing, documentation, and lineage graph using dbt.

## 🛠 Tech Stack

- dbt (Data Build Tool)
- PostgreSQL
- Docker
- Faker (to generate mock data)

## 🧠 What I Did

- Created staging and marts models using SQL in dbt.
- Designed star schema: `fact_orders`, `dim_customers`, `dim_products`.
- Added data tests, documentation, and generated dbt docs with lineage.
- Loaded mock data into PostgreSQL from CSV files.

## 📁 Folder Structure
```yaml
dbt_ecommerce_analytics/
├── dbt_project/
│ ├── models/
│ ├── dbt_project.yml
│ └── profiles.yml
├── data/ # Mock CSV data
└── docker-compose.yml
```

## ✅ What I Learned

- Best practices in warehouse modeling (staging, marts)
- Creating reusable and testable SQL models
- Using dbt for lineage tracking and documentation
- Working with PostgreSQL and Docker in analytics context
