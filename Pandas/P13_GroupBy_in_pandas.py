import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", 
                index_col="Name")

group = df.groupby("Type1")
print(group["Height"].mean())