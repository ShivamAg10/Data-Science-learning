import numpy as np 

arr = np.random.randint(10,99,(10))
print(arr)

where_result = np.where(arr > 50)
# print(where_result)
# print(arr[where_result])

# we can give more than 1 condition as well
condition_array = np.where(arr > 50, arr * 2, arr)
print(condition_array)

# This Condition-array is working like this: 
## if (arr > 50){
    ## arr * 2
##}
## else{
    ##arr
##}

# We can also understand it like this as well
condition_array = np.where(arr > 50, True, False)
print(condition_array)