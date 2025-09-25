# Multiplying 2 numpy array

import numpy as np 

arr = np.random.randint(1,9, (2,2))
arr1 = np.random.randint(1,9,(2,2))
print(arr)
print(arr1)

print(arr*arr1)
## will multiply each element(of same index) of both array

print(np.dot(arr,arr1))
## dot product of an array is equal to the multiplication of an array