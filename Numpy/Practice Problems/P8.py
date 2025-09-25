# Checking if a certain number present in array and fill the negative values with 8

import numpy as np 

myArr = np.random.randint(-3,2,(3,3))
print(myArr)

# for i in range(len(myArr)):
#     for j in range(len(myArr)):
#         if myArr[i][j]==1:
#             print(i, j)
#         if myArr[i][j]<0:
#             myArr[i][j] = 8
# print(myArr)

isin_method = np.isin(myArr, 1)
print(isin_method)

myArr[myArr<0] = 8
print(myArr)