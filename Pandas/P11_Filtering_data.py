import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", 
                index_col="Name")

tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

heavy_pokemon = df[df["Weight"] >= 100]
# print(heavy_pokemon)

# tall_heavy_pokemon = df[(df["Height"] >= 1 ) and (df["Weight"] >= 100)] -> wrong method
tall_heavy_pokemon = df[(df["Height"] >= 1 ) & (df["Weight"] >= 100)]
print(tall_heavy_pokemon)