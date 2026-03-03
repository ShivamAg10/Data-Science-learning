import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\DataCleaning\etflix1.csv")
# print(df.head())

# print(df.info())
'''
## Data Type Problems-
### date_added column -> object to date
### duration column -> given in mins and seasons -> need to be change

## Director column -> not given (value) to Null
'''

# print(df.describe())

# print(df.isnull().sum())

# print(df[df.duplicated()].shape)
# print(df[df.duplicated()])

# print(df['show_id'].value_counts())

# print(df.columns)
# for col in df.columns:
#     print(df[col].value_counts())
#     print("-"*50)

# print(df[df['title'] == "15-Aug"])

### Handling Missing Values

print(df['duration'].unique())