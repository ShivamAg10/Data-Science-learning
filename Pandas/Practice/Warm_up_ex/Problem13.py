# Display name and marks of female students

import pandas as pd 

dict ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv','Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male','Female','Female']
}
df=pd.DataFrame(dict)

print(df[df["Gender"]=="Female"][["Name", "Marks"]])
print(df[df["Gender"].isin(["Female"])][["Name", "Marks"]])