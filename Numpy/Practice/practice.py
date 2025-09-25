import numpy as np

arr = np.random.randint(3,90,(2,8))
print(arr)
print()
print()

for i in arr:
    for j in i:
        print(j, end="  ")