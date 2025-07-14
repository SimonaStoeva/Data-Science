import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')

df = pd.read_csv('constructor_standings.csv')
df = df.dropna()
df['Year'] = df['Year'].astype(int)


total_points = df.groupby('Team')['PTS'].sum().sort_values(ascending=False)
top10 = total_points[0:10]


x = df['Team']
y = df['PTS']
plt.bar(top10.index, top10.values, color='lavender')
plt.xlabel("Team")
plt.ylabel("Points")
plt.title("Average constructor points")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
