# transform.py 
import json 
from datetime import datetime


def transform_weather(json_file, **kwargs):
    ti = kwargs['ti']

    with open(json_file, 'r') as f:
        data = json.load(f)

    cleaned = {
        "city": data.get("name"), 
        "timestamp": datetime.fromtimestamp(data["dt"]), 
        "temperature": data["main"]["temp"], 
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"], 
        "description": data["weather"][0]["description"], 
        "wind_speed": data["wind"]["speed"], 
        "wind_deg": data["wind"]["deg"]
    }
    ti.xcom_push(key='data', value=cleaned)

    return cleaned


