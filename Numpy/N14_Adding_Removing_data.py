import numpy as np 

# Adding two arrays
arr = np.random.randint(10,99, (2,4))
arr1 = np.random.randint(10,99, (2,4))
print("arr:\n", arr)
print("arr1:\n",arr1)

combined_arr = np.concatenate((arr, arr1))
print("combined arr: \n", combined_arr)

# Array Compatibility
print("Checking array compatibility: \n", arr.shape == arr1.shape)

# vstack() -> adds row in a array
arr2 = np.random.randint(10,99,(4))
print("arr2: \n", arr2)
with_new_row = np.vstack((arr, arr2))
print("After vstack: \n", with_new_row)

# hstack() -> adds column in a array
new_col = np.array([[7,9], [8,6]])
with_new_col = np.hstack((arr, new_col))
print("After hstack:\n", with_new_col)

# Removing data
np_arr = np.random.randint(10,99, 5)
print("np_arr: \n", np_arr)
deleted = np.delete(np_arr, 3)
print("after deleting: \n",deleted)