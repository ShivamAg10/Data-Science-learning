import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\DataCleaning\etflix1.csv")

# print(df.columns)

# print(df.duplicated().sum())

df["date_added"] = pd.to_datetime(df["date_added"])
# print(df["date_added"])

a = df["country"].unique()
# print(a)

print(df[df["country"] == "Not Given"].values.sum())