# Display top 3 rows of the data set

import pandas as pd 

dict ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv','Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male','Female','Female']
}
df=pd.DataFrame(dict)

print(df[0:3])
print(df.head(3))