# COVID-19 ETL Project

## Project Overview
This project is an **end-to-end ETL pipeline** that extracts live COVID-19 data from the [disease.sh API](https://disease.sh/), transforms it, loads it into a SQLite database, and generates insightful dashboards.

---

## ETL Pipeline Steps

1. **Extract**
   - Pulls live COVID-19 data for 231 countries.
   - Saves raw JSON files in `data/raw/`.

2. **Transform**
   - Flattens nested JSON data.
   - Handles missing values (e.g., recovered cases).
   - Adds derived metrics such as per-million statistics and rolling averages.

3. **Load**
   - Loads the cleaned data into SQLite database `database/covid.db`.
   - Stores data in the `covid_stats` table.

4. **Insights / Dashboard**
   - SQL queries to analyze top countries by cases, deaths, and recovered.
   - Python dashboards using Matplotlib/Seaborn and optional Plotly:
     - Top 5 countries by total cases
     - Top 5 countries by total deaths
     - Top 5 countries by 7-day average deaths
     - Trend lines for selected countries over time

---

## Project Structure

covid_etl/
│
├─ data/
│ ├─ raw/ # Raw JSON from API
│ └─ processed/ # Optional processed CSV/JSON
│
├─ database/
│ └─ covid.db # SQLite database
│
├─ src/
│ ├─ extract.py
│ ├─ transform.py
│ ├─ load.py
│ ├─ pipeline.py
│ └─ queries.py
│
└─ dashboard.py # Generates all dashboards


## How to Run

1. Clone the repository:
```bash
git clone https://github.com/Ekshitha2305/Covid-ETL.git
cd Covid-ETL

2.Create a virtual environment and install dependencies:

python -m venv sparkenv
sparkenv\Scripts\activate
pip install pandas matplotlib seaborn plotly requests

3.Run the ETL pipeline:

python src/pipeline.py

4.Run the dashboards:

python dashboard.py

Notes:

.gitignore excludes raw data, database, and virtual environment files.

You can customize selected countries in dashboard.py for trend charts.

Optional: Use Plotly for interactive dashboards.