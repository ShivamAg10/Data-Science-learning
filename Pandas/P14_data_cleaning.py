import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")

# 1. Drop irrelevant data
# df = df.drop(columns=["Legendary", "Type2"])
# print(df)

# 2. Handling missing data
# df = df.dropna(subset=["Type2"])
# df = df.fillna({"Type2" : "None"})
# print(df.to_string())

# 3. Fixing inconsistent values
# df["Type1"] = df["Type1"].replace({"Grass":"GRASS", "Water" : "H2O"})
# print(df.to_string())

# 4. Standardize text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

# 5. Fix Data Type
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df)

# 6. Remove Duplicates
# print(df)
# df = df.drop_duplicates()
# print(df.to_string())
df = df.duplicated()
print(df)