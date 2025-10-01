import pandas as pd 

data = {
    "Name" : ["Shivam", "Hemant", "Ashok"],
    "Age" : [20, 14, 47]
}

df = pd.DataFrame(data)
df["Job"] = ["B Tech", "Student", "Businessman"]
print(df)