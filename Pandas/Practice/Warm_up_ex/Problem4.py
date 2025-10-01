# Display information about our dataset like Total no of rows, Total no of columns, DataType of each 
# columns and memory requirement

import pandas as pd 

dict ={'Name':['Priyang','Aadhya','Krisha','Vedant','Parshv','Mittal','Archana'],
                'Marks':[98,89,99,87,90,83,99],
                'Gender':['Male','Female','Female','Male','Male','Female','Female']
}
df=pd.DataFrame(dict)

print("Number of rows:", df.shape[0])
print("Number of columns:", df.shape[1])
print("Datatypes of each columns: \n", df.dtypes)
print("Memory usage: \n", df.memory_usage())
df.info()