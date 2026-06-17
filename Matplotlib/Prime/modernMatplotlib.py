import matplotlib.pyplot as plt 
import numpy as np 

x = [i for i in range(1,11)]
y1 = [np.sqrt(i) for i in x] # square root
y2 = [i*2 for i in x] # double
y3 = [i*i for i in x] # square
y4 = [i**3 for i in x] # Cube

fig, axes = plt.subplots(2,2)
axes[0][0].plot(x,y1)
axes[0][0].set_title("plot-1 Square Root")

axes[0][1].plot(x,y2)
axes[0][1].set_title("plot-2 Double")

axes[1][0].plot(x,y3)
axes[1][0].set_title("plot-3 Square")

axes[1][1].plot(x,y4)
axes[1][1].set_title("plot-4 Cube")

fig.tight_layout()
plt.show()