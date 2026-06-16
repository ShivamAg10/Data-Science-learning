import matplotlib.pyplot as plt 
import numpy as np 

x = [i for i in range(1,11)]
y1 = [np.sqrt(i) for i in x] # square root
y2 = [i*2 for i in x] # double
y3 = [i*i for i in x] # square
y4 = [i**3 for i in x] # Cube

plt.subplot(2,2,1)
plt.plot(x, y1)
plt.title("plot1 - square root")

plt.subplot(2,2,2)
plt.plot(x, y2)
plt.title("plot1 - double value")

plt.subplot(2,2,3)
plt.plot(x, y3)
plt.title("plot3 - square value")

plt.subplot(2,2,4)
plt.plot(x, y4)
plt.title("plot4 - cube value")

plt.tight_layout()
plt.show()