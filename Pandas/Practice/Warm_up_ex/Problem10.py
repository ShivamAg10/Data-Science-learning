# Find total number of students having marks between 90 to 100(inclusive) using between method

import pandas as pd 

dict ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv','Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,100],
                'Gender':['Male','Female','Female','Male','Male','Female','Female']
}
df=pd.DataFrame(dict)

print(len(df[(df["Marks"] >= 90) & (df["Marks"] <= 100)]))
print(sum(df['Marks'].between(90,100)))