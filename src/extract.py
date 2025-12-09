import requests
import os
import json

RAW_PATH = "data/raw"
os.makedirs(RAW_PATH, exist_ok=True)

def run_extract():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        file_path = os.path.join(RAW_PATH, "covid_countries.json")
        with open(file_path, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Extracted {len(data)} countries to {file_path}")
    else:
        print("Failed to fetch data:", response.status_code)
