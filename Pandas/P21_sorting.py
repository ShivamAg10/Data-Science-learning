import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")

# print(df.sort_values(by="Name", ascending=False))
print(df.sort_values(by=["Name", "Type1"], ascending=False))