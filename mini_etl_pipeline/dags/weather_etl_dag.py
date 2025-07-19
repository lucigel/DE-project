import os 
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.extract import extract_weather
from scripts.transform import transform_weather
from scripts.load import load_weather

default_args = {
    'owner': 'duy',
    'retries': 2,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    tags=['etl', 'weather']
) as dag:

    output_dir = '/opt/airflow/data/raw/'
    today = datetime.today().strftime('%Y%m%d')
    json_file = filename = f"{output_dir}hanoi_weather_{today}.json"

    extract_task = PythonOperator(
        task_id='extract_weather_data',
        python_callable=extract_weather,
        op_kwargs={
            'api_key': os.getenv('API_KEY', 'b1d6aba62b74e155c68b24a0ffebd18c'),  
        }
    )

    transform_task = PythonOperator(
        task_id='transform_weather_data',
        python_callable=transform_weather,
        provide_context=True,
        op_kwargs = {
            f"json_file": json_file
        }
    )

    load_task = PythonOperator(
        task_id='load_weather_to_postgres',
        python_callable=load_weather,
        provide_context=True,
    )

    extract_task >> transform_task >> load_task
