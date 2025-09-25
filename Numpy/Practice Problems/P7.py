# Filling diagonal values with a number of a numpy array

import numpy as np 

myArr = np.random.randint(10,99,(3,3))
print(myArr)

for i in range(len(myArr)):
    for j in range(len(myArr)):
        if i == j:
            myArr[i][j] = 7
print(myArr)