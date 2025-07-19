import os
import requests 
import json 
from datetime import datetime


def extract_weather(api_key, output_dir='/opt/airflow/data/raw/'):
    print(api_key)
    lat = 21.0285
    lon = 105.8542
    today = datetime.today().strftime('%Y%m%d')
    filename = f"{output_dir}hanoi_weather_{today}.json"

    if os.path.exists(filename):
        print(f"📦 {filename} already exists.")
        return filename  # Return path to existing file

    url = f"https://api.openweathermap.org/data/2.5/weather?q=Hanoi&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    os.makedirs(output_dir, exist_ok=True)
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"✅ Extracted to {filename}")
    return filename
