# Write a numpy program to create a 4x4 matrix with random values, now create a new array from the
# said array such that it starts with the Last row and goes till the first

import numpy as np 

arr = np.random.randint(10,99,(4,4))
print(arr)

arr = arr[::-1]
print(arr)