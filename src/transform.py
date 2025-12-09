import os
import json
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

RAW_PATH = "data/raw"

def run_transform():
    file_path = os.path.join(RAW_PATH, "covid_countries.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    
    records = []

    # --------------- Simulate 30 days of historical data ----------------
    for day_offset in range(30, 0, -1):
        today = datetime.utcnow().date() - timedelta(days=day_offset)
        
        for c in data:
            # Optionally simulate small variations for todayCases and todayDeaths
            # todayCases = max(0, c["todayCases"] + int(pd.np.random.randint(-5, 6)))
            # todayDeaths = max(0, c["todayDeaths"] + int(pd.np.random.randint(-2, 3)))
            todayCases = max(0, c["todayCases"] + int(np.random.randint(-5, 6)))
            todayDeaths = max(0, c["todayDeaths"] + int(np.random.randint(-2, 3)))


            # Handle missing recovered
            recovered = c["recovered"]
            if recovered in [0, None]:
                recovered = c["cases"] - c["deaths"] - c["active"]

            records.append({
                "date": today,
                "country": c["country"],
                "cases": c["cases"],
                "todayCases": todayCases,
                "deaths": c["deaths"],
                "todayDeaths": todayDeaths,
                "recovered": recovered,
                "todayRecovered": c["todayRecovered"],
                "active": c["active"],
                "critical": c["critical"],
                "casesPerOneMillion": c.get("casesPerOneMillion", None),
                "deathsPerOneMillion": c.get("deathsPerOneMillion", None),
                "population": c.get("population", None)
            })
    
    # Create DataFrame
    df = pd.DataFrame(records)
    
    # ---------------- Derived Columns ----------------
    df["activePerMillion"] = (df["active"] / df["population"]) * 1_000_000
    df["casesPerMillion"] = (df["cases"] / df["population"]) * 1_000_000
    df["deathsPerMillion"] = (df["deaths"] / df["population"]) * 1_000_000
    
    return df
