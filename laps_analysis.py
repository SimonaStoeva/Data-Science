import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt5Agg')
import fastf1
import tkinter as tk

fastf1.Cache.enable_cache('D:\\Me\\python\\F1-data')

session = fastf1.get_session(2023,3, "Q")
session.load()

session.laps #dataframe

pd.set_option('display.max_columns', None)
print(session.laps.head())

session.laps['IsAccurate'] == True
#LapTimeSeconds - moq kolona, Time - kolona ot fastf1
session.laps['LapTimeSeconds'] = session.laps['Time'].dt.total_seconds()

accurate_laps = session.laps[session.laps['IsAccurate'] == True]

fastest_lap = accurate_laps.loc[accurate_laps.groupby('Driver')['LapTimeSeconds'].idxmin()] #индекс на реда с най-малко време

print(fastest_lap[['Driver', 'LapTimeSeconds', 'LapNumber']])

x = fastest_lap['Driver']
y = fastest_lap['LapTimeSeconds']
plt.bar(x, y, color='blue')
plt.xlabel("Driver")
plt.ylabel("Lap Time")
plt.show()