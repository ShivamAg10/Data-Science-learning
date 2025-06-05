import numpy as np 

arr = np.random.randint(10,99, (3,4))
print(arr)

indices_row_wise = [0,2]
print(arr[indices_row_wise])