# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("database/covid.db")
# df = pd.read_sql("SELECT * FROM covid_stats", conn)

# # Aggregate to latest values per country
# df_latest = df.groupby("country").agg({
#     "cases": "max",
#     "deaths": "max",
#     "recovered": "max"
# }).reset_index()

# print(df_latest.sort_values("cases", ascending=False).head(5))

# import sqlite3
# import pandas as pd

# conn = sqlite3.connect("database/covid.db")
# df = pd.read_sql("SELECT * FROM covid_stats", conn)
# conn.close()

# import matplotlib.pyplot as plt
# import seaborn as sns

# latest_df = df[df['date'] == df['date'].max()]

# top_cases = latest_df.sort_values('cases', ascending=False).head(5)

# plt.figure(figsize=(10,6))
# sns.barplot(x='country', y='cases', data=top_cases)
# plt.title("Top 5 Countries by Total COVID Cases")
# plt.ylabel("Total Cases")
# plt.show()



