from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, expr
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

# 1. Khởi tạo Spark Session với packages
spark = SparkSession.builder \
    .appName("KafkaSparkStreaming") \
    .config("spark.jars", "/opt/bitnami/spark/jars/postgresql-42.6.0.jar") \
    .config("spark.sql.streaming.checkpointLocation", "/tmp/checkpoint") \
    .getOrCreate()

# 2. Định nghĩa schema cho dữ liệu Kafka
schema = StructType([
    StructField("sensor_id", StringType()),
    StructField("value", IntegerType()),
    StructField("timestamp", TimestampType())
])

# 3. Đọc stream từ Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka-1:9094,kafka-2:9094,kafka-3:9094") \
    .option("subscribe", "sensor_topic") \
    .option("startingOffsets", "earliest") \
    .load()

# 4. Parse JSON
parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# 5. Xử lý dữ liệu
processed_df = parsed_df.withColumn(
    "alert", 
    expr("CASE WHEN value > 100 THEN 1 ELSE 0 END")
)

# 6. Ghi vào PostgreSQL
def write_to_postgres(batch_df, batch_id):
    batch_df.write \
        .format("jdbc") \
        .option("url", "jdbc:postgresql://postgres:5432/streaming_db") \
        .option("dbtable", "sensor_alerts") \
        .option("user", "user") \
        .option("password", "password") \
        .mode("append") \
        .save()

query = processed_df.writeStream \
    .foreachBatch(write_to_postgres) \
    .outputMode("update") \
    .start()

query.awaitTermination()