# Removing rows which contains null alues in a numpy array.

import numpy as np 

arr = np.array([[1,2,3,np.nan,5,6],[7,8,9,0,np.nan,2]])

# arr = arr[np.nan(arr).any(axis=1)]
print(np.nan(arr))