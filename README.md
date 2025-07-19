# 🧰 Data Engineering Project Portfolio

Welcome to my personal Data Engineering project portfolio!  
This repository contains 3 hands-on mini projects that demonstrate my understanding of core data engineering concepts, tools, and workflows.

Each project focuses on a different aspect of the data engineering lifecycle — from batch ETL pipelines to data modeling and real-time data processing.

---

## 📦 Project List

### 1. 🧪 Mini ETL Pipeline with Airflow + PostgreSQL + Docker

**Goal**: Build a modular batch ETL pipeline from API to database using Airflow.

- Extracts weather or currency data from a public API.
- Saves raw data to local storage (or S3).
- Transforms and cleans the data using Python.
- Loads final data into PostgreSQL.
- Fully orchestrated using Airflow DAG with Dockerized infrastructure.

🔗 [View Project](./mini_etl_pipeline)

---

### 2. 📊 Data Modeling & Analytics with dbt + PostgreSQL

**Goal**: Design and build an analytics warehouse using dbt on top of PostgreSQL.

- Simulates e-commerce datasets (orders, customers, products).
- Implements staging and star-schema marts models with dbt.
- Adds schema testing, documentation, and lineage graph.
- Demonstrates warehouse modeling best practices.

🔗 [View Project](./dbt_ecommerce_analytics)

---

### 3. 🔁 Real-time Streaming Pipeline with Kafka + Spark + PostgreSQL

**Goal**: Build a simple real-time pipeline to simulate ingesting and processing live data streams.

- Kafka producer simulates streaming data (sensor or user logs).
- Spark Structured Streaming reads data from Kafka and transforms it.
- Outputs processed data to PostgreSQL.
- All components run via Docker Compose.

🔗 [View Project](./streaming_pipeline)

---

## 🧠 What I Learned

Through these projects, I practiced key Data Engineering skills:

- 🔧 Building and orchestrating batch ETL pipelines with Airflow
- 🏗 Designing layered data models and star schemas with dbt
- 🚀 Working with real-time streaming tools like Kafka and Spark
- 🐳 Containerizing components using Docker & Docker Compose
- 📄 Writing clean, modular Python & SQL code for data processing
- 🧪 Testing, documenting, and visualizing data workflows

---

## 🚀 How to Run

Each subfolder contains its own `README.md` with setup instructions.  
You can clone this repo and explore each project individually.

```bash
git clone https://github.com/your-username/DE-project.git
cd DE-project
