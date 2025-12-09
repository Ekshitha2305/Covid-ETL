import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ---------------- 1. Load Data ----------------
conn = sqlite3.connect("database/covid.db")
df = pd.read_sql("SELECT * FROM covid_stats", conn)
conn.close()

# ---------------- 2. Prepare Data ----------------
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(['country', 'date'])

# 7-day rolling averages
df['rolling_7d_cases'] = df.groupby('country')['todayCases'].transform(lambda x: x.rolling(7,1).mean())
df['rolling_7d_deaths'] = df.groupby('country')['todayDeaths'].transform(lambda x: x.rolling(7,1).mean())

# Latest snapshot
latest_df = df[df['date'] == df['date'].max()]

# ---------------- 3. Top 5 Countries Bar Charts ----------------
def plot_top5(column, title):
    top5 = latest_df.sort_values(column, ascending=False).head(5)
    plt.figure(figsize=(10,6))
    sns.barplot(x='country', y=column, data=top5)
    plt.title(title)
    plt.ylabel(column)
    plt.show()

plot_top5('cases', "Top 5 Countries by Total Cases")
plot_top5('deaths', "Top 5 Countries by Total Deaths")
plot_top5('rolling_7d_deaths', "Top 5 Countries by 7-Day Avg Deaths")

# ---------------- 4. Trend Lines for Selected Countries ----------------
selected_countries = ['USA','India','Brazil']  # change as needed
for country in selected_countries:
    c_df = df[df['country'] == country]
    plt.figure(figsize=(12,6))
    sns.lineplot(x='date', y='cases', data=c_df, label='Total Cases')
    sns.lineplot(x='date', y='deaths', data=c_df, label='Total Deaths')
    sns.lineplot(x='date', y='recovered', data=c_df, label='Total Recovered')
    plt.title(f"COVID-19 Trend for {country}")
    plt.xticks(rotation=45)
    plt.ylabel("Count")
    plt.show()

# ---------------- 5. Optional: Interactive Plotly Charts ----------------
for country in selected_countries:
    fig = px.line(df[df['country'] == country], 
                  x='date', y=['cases','deaths','recovered'], 
                  title=f"Interactive COVID-19 Trend for {country}")
    fig.show()
