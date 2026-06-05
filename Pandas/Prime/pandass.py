## AQI Data Set
import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\globalAirQuality.csv")
# print(df.head())

# print(df['city'])
# print(df[['city', 'aqi']])

# print(df.loc[0])
# print(df.loc[0:3])

# print(df.loc[0, "aqi"])
# print(df.loc[0, ["city", "aqi"]])
print(df.loc[0:2, ["city", "aqi"]])