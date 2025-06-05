import numpy as np 

unsorted = np.random.randint(12,56,(10))
print(unsorted)

print("sorted Array: ", np.sort(unsorted))

# Sorting in 2d array
unsorted_2d = np.random.randint(12,56,(3,4))
print(unsorted_2d)

# Column wise sorting
print("Column Sorted 2D Array: ", np.sort(unsorted_2d, axis = 0))

# Row wise sorting
print("Row Sorted 2D Array: ", np.sort(unsorted_2d, axis = 1))