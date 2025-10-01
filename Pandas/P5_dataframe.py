import pandas as pd 

data = {
    "Name" : ["Shivam", "Hemant", "Ashok"],
    "Age" : [20, 14, 47]
}

df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, index=["Employee1", "Employee2", "Employee3"])
print(df)

print(df.loc["Employee2"])
print(df.iloc[0])