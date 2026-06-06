import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\w_data.csv")
# print(df)

# print(df.isnull())
# print(df.isnull().sum())
# df.dropna(axis=1)

## filling age 
# mean = df["age"].mean()
# df['age'] = df["age"].fillna(mean)
# print(df)

# ## ffill
# df['age'] = df["age"].ffill()
# print(df)

## bfill
df['age'] = df["age"].bfill()

# df['age'].iloc[7] = 34.67
# print(df)

df['age'] = df['age'].astype('int64')
# print(df)

df2 = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\globalAirQuality.csv")
# print(df2["timestamp"].dtypes)

df2['timestamp'] = pd.to_datetime(df2['timestamp'])
# print(df2["timestamp"].dtypes)
# print(df2)

## Apply method - apply()
df["tax"] = df['income'].apply(lambda x : "20%" if x > 50000 else "10%")
# print(df)

## Map Method - map()
gender_map = {
    "Male" : "M",
    "Female" : "F", 
    "Unknown" : "U"
}
df["gender"] = df['gender'].map(gender_map)
# print(df)

df = df.assign(new_income = df['income'] * 1.1)
print(df)