# Let's check which is faster, either array or list

import numpy as np 
import time

start = time.time()
# print(start)
py_list = [i*2 for i in range(10000000)]
print("\n List Operation Time: ", time.time() - start)

start = time.time()
np_arr = np.arange(10000000)
print("\n Array Operation Time: ", time.time() - start)

# Hence, Numpy Array is faster than a list