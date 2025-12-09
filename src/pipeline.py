from extract import run_extract
from transform import run_transform
from load import run_load
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def run_pipeline():
    # 1. Extract
    run_extract()
    
    # 2. Transform
    df = run_transform()
    
    # 3. Load
    run_load(df)
    
    # 4. Insights & Rolling Averages
    print("\n--- Sample Insights ---")
    conn = sqlite3.connect("database/covid.db")
    
    df_db = pd.read_sql("SELECT * FROM covid_stats", conn)
    conn.close()
    
    # Rolling 7-day average for today cases
    df_db['date'] = pd.to_datetime(df_db['date'])
    df_db.sort_values(['country','date'], inplace=True)
    df_db['rolling_7d_cases'] = df_db.groupby('country')['todayCases'].transform(lambda x: x.rolling(7,1).mean())
    df_db['rolling_7d_deaths'] = df_db.groupby('country')['todayDeaths'].transform(lambda x: x.rolling(7,1).mean())
    
    # Top countries by total cases
    top_cases = df_db.groupby('country')['cases'].max().sort_values(ascending=False).head(5)
    print("\nTop 5 Countries by Total Cases:")
    print(top_cases)
    
    # Top countries by 7-day rolling avg deaths (latest date)
    latest_date = df_db['date'].max()
    latest_df = df_db[df_db['date']==latest_date]
    top_rolling_deaths = latest_df.sort_values('rolling_7d_deaths', ascending=False).head(5)
    print("\nTop 5 Countries by 7-day Avg Deaths:")
    print(top_rolling_deaths[['country','rolling_7d_deaths']])
    
    # ---------------- Visualization ----------------
    # Example: trend of total cases for top 5 countries
    plt.figure(figsize=(10,6))
    for country in top_cases.index:
        country_df = df_db[df_db['country']==country]
        plt.plot(country_df['date'], country_df['cases'], label=country)
    plt.title("Total COVID-19 Cases Trend for Top 5 Countries")
    plt.xlabel("Date")
    plt.ylabel("Total Cases")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    run_pipeline()
