# Finding minimum value along the rows

import numpy as np 

myArr = np.random.randint(10,99,(2,4))
print(myArr)

minimumValue = np.min(myArr, axis=0)
print(minimumValue)