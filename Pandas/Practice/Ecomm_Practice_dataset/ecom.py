import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Practice\Ecomm_Practice_dataset\Ecomm_dataset.csv")
# print(df.to_string())

# # 1. Highest & Lowest Purchase prices
# print(df["Purchase Price"].max())
# print(df["Purchase Price"].min())

# # 2. Average Purchase Price
# print(df["Purchase Price"].mean())

# # 3. How many people have French "fr" as their language
# print(len(df[df["Language"]=="fr"]))

# # 4. Job title contains Engineer
# print(len(df[df["Job"].str.contains("engineer", case=False)]))

# 5. Find email of the person with the following ip address: 132.207.160.22
# print(df[df["IP Address"]=="132.207.160.22"]["Email"])

# 6. How many People have mastercard as their credit card provider and made a purchase above 50?
# print(len(df[(df["CC Provider"]=="Mastercard") & (df["Purchase Price"] > 50)]))

# 7. Find email of person with credit card number: 4664825258997302
print(df[df["Credit Card"] == 4664825258997302]["Email"])
# print(df["Credit Card"])