# file: kafka_producer/mock_producer.py

from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(
    bootstrap_servers='localhost:19092',  # dùng cổng public Kafka-1
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = {
        "sensor_id": random.randint(1, 5),
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "timestamp": time.time()
    }
    print(f"Sending: {data}")
    producer.send('sensor_data', value=data)
    time.sleep(1)
