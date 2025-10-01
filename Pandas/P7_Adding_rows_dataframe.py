import pandas as pd 

data = {
    "Name" : ["Shivam", "Hemant", "Ashok"],
    "Age" : [20, 14, 47]
}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

new_rows = pd.DataFrame([{"Names" : "Khushi", "Age" : 18},
                        {"Name" : "Anju"}], 
                        index=["Employee 4", "Employee 5"])

df = pd.concat([df, new_rows])
print(df)