import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", 
                index_col="Name")

# print(df.to_string())
# print(df["Name"])
# print(df["Height"])
# print(df.loc["Name"])
# print(df.loc["Venusaur"])
# print(df.loc["Venusaur", ["Type2", "Weight"]])
# print(df.loc["Venusaur" : "Mewtwo" ,["Height", "Weight"]])
# print(df.iloc[0:34:3])
print(df.iloc[0:34:3, 0:3])