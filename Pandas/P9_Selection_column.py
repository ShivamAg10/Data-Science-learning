import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")
# print(df)
# print(df.to_string())

# print(df["Name"])

# print(df["names"])

print(df[["Name", "Height", "Weight"]])