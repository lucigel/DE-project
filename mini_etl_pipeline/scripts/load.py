# load.py 
from airflow.hooks.postgres_hook import PostgresHook

def load_weather(conn_id: str ='pg_weather', **kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='transform_weather_data', key='return_value')
    print(data)
    hook = PostgresHook(postgres_conn_id=conn_id)
    conn = hook.get_conn()
    cur = conn.cursor()

    insert_query = """
    INSERT INTO weather_data (city, timestamp, temperature, humidity, pressure, description, wind_speed, wind_deg)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        data["city"],
        data["timestamp"],
        data["temperature"],
        data["humidity"],
        data["pressure"],
        data["description"],
        data["wind_speed"],
        data["wind_deg"]
    )

    cur.execute(insert_query, values)
    conn.commit()
    cur.close()
    conn.close()
    print("✅ Loaded data to PostgreSQL")