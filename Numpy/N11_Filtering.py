import numpy as np 

arr = np.random.randint(10,99, (3,4))
print(arr)

# print(arr%2)

print(arr%2 == 0.0)

# print(arr[True])
# print(arr[False])

c = arr%2==0.0
# print(c)

even_num = arr[arr % 3 == 0.0]
# print(even_num)

# Filtering with mask
mask = arr > 50
print(mask)
print(arr[mask])