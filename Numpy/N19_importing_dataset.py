import numpy as np
import pandas as pd

data = np.genfromtxt("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", delimiter=",")
print(data)
## Not able to access String data type and it is showing "nan" 

data = np.genfromtxt("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv", delimiter=",", dtype="str")
print(data)
## All data is converted into string

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\csv_file.csv")
print(df)
arr =df.to_numpy()
print(arr)