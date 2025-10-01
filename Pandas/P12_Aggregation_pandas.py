import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", 
                index_col="Name")

# Mean 
# print(df.mean(numeric_only=True))
print(df["Height"].mean())

# sum 
# print(df.sum(numeric_only=True))

# min 
# print(df.min(numeric_only=True))

# max 
# print(df.max(numeric_only=True))

# count 
# print(df.count())