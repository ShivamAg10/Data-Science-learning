import numpy as np 

arr = np.arange(12)
print("Original Array: ", arr)

reshaped = arr.reshape((3,4))
print("Reshaped Array: \n", reshaped)

flatten = reshaped.flatten()
print("Flattened Array: ", flatten)

# Return view, instead of copy
raveled = reshaped.ravel()
print("Raveled Array: ", raveled)

transpose = reshaped.T
print("Transposed Array: \n", transpose)