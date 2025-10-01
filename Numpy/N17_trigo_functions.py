import numpy as np 

# In radian
myArr = np.array([30,45,60,90])
print(myArr)

myArr = np.sin(myArr)
print(myArr)

# In degree
myArr = np.array([30,45,60,90])
print(myArr)

myArr = myArr * np.pi / 180
myArr = np.sin(myArr)
print(myArr)