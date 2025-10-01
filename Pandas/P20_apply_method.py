import pandas as pd 

def half_weight(x):
    return x/2

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")

print(df["Weight"].apply(half_weight))
print(df["Name"].apply(len))