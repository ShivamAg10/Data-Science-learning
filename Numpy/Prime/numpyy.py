import numpy as np 
import time

lst = list(range(10))
# start = time.time()
# sq_lst = [i**2 for i in lst]
# end = time.time()
# print(end-start)

arr = np.array(lst)
# start = time.time()
# sq_arr = arr ** 2
# end = time.time()
# print(end-start)

print(arr[10])