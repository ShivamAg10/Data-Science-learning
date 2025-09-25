import numpy as np 

# Multiply string elements into a numpy array

arr = np.array(["Shivam", "Agrawal"])
multipling = np.char.multiply(arr,2)
print(multipling)