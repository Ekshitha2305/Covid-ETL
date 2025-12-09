import sqlite3
import os

DB_PATH = "database/covid.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def run_load(df):
    conn = sqlite3.connect(DB_PATH)
    
    # Drop table if exists (so new schema with 'date' column is created)
    conn.execute("DROP TABLE IF EXISTS covid_stats")
    
    # Create table with new data
    df.to_sql("covid_stats", conn, if_exists="replace", index=False)
    
    conn.commit()
    conn.close()
    print(f"Loaded data into {DB_PATH}")
