import numpy as np 

arr = np.arange(12)

#Basic Slicing
basic_slicing = arr[2:7]
print(basic_slicing)

# With steps
with_steps = arr[1:8:3]
print(with_steps)

#Negative Indexing
neg_index = arr[-3]
print(neg_index)

## Applying slicing and indexing in 2d array

arr_2d = np.array([[1,2,3],
                                [4,5,6],
                                [7,8,9]])

#Specific Element
spec_ele = arr_2d[1,2]
print(spec_ele)

#Entire Row
print("Entire Row: ", arr_2d[1])

#Entire Column
print("Entire Column: ", arr_2d[:, 1])

# 2D Slicing
print("2D Slicing: ", arr_2d[0:2, 1:3])