# checking null values in data set

import pandas as pd 

dict ={'Name':['Priyang','Aadhya','Krisha',None,'Parshv','Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male','Female','Female']
}
df=pd.DataFrame(dict)

print(df.isnull())
print(df.isnull().sum()) # By default -> Columns
print(df.isnull().sum(axis=0)) # Columns
print(df.isnull().sum(axis=1)) # Rows