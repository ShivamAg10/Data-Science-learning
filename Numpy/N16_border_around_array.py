import numpy as np 

arr = np.random.randint(10,99,(3,3))
print(arr)

arr = np.pad(arr, pad_width=1,mode="constant", constant_values=0)
print(arr)

arr = np.pad(arr, pad_width=1,mode="constant", constant_values=[2,3])
print(arr)