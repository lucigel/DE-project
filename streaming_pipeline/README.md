# 🔁 Real-time Data Pipeline with Kafka, Spark & PostgreSQL

A personal project to build a simple real-time data pipeline using Kafka and Spark Structured Streaming.

## 📌 Project Overview

This pipeline simulates real-time data ingestion and processing:
- Kafka producer simulates real-time events (e.g. user clickstream or IoT sensors).
- Spark Streaming consumes Kafka data, processes it, and writes to PostgreSQL.
- Entire system runs via Docker Compose.

## 🛠 Tech Stack

- Apache Kafka
- Apache Spark Structured Streaming
- PostgreSQL
- Docker

## 🧠 What I Did

- Simulated streaming data using a Kafka Python producer.
- Implemented a Spark Structured Streaming job to transform and write to PostgreSQL.
- Used Docker Compose to orchestrate Kafka, Spark, and PostgreSQL services.
- Designed simple transformations and sink schema in PostgreSQL.

## 📁 Folder Structure
```yaml
streaming_pipeline/
├── docker-compose.yml
├── spark_app/ # Spark streaming job
├── kafka_producer/ # Kafka producer simulation
└── README.md
```

## ✅ What I Learned

- Fundamentals of building streaming pipelines
- Integrating multiple distributed systems (Kafka + Spark + PostgreSQL)
- Handling real-time data flows and fault tolerance
- Containerizing stream processing applications
