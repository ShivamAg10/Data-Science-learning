import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\practiceData\dataset-1\Diwali_Sales_Data.csv", encoding='cp1252')
# print(df.head(10))
# print(len(df["Cust_name"].unique()))
# print(df.info())

# print(df.shape)
# print(df.isnull().sum())
# print(df[df.isnull().any(axis=1)])
df.drop(["Status", "unnamed1"],axis=1, inplace=True)
# print(df.head())
# print(df.isnull().sum())
# print(df.shape)
df.dropna(inplace=True)
# print(df.shape)
# print(df.isnull().sum())
# print(df.duplicated())
# print(df.info())
# print(df.head(6))
df["Amount"] = df["Amount"].astype('int')
# print(df.head(15))
# print(df["Amount"].mode())