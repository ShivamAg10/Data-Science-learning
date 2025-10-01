import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")

print(df.isnull())
print(df.isnull().sum()) # By default -> columns
print(df.isnull().sum(axis=0)) # Columns
print(df.isnull().sum(axis=1)) # Rows