import numpy as np
import matplotlib.pyplot as plt 

days = ["Mon", "Tue", "Wed", "Thr", "Fri"]
cities = ["New York", "London", "Delhi", "Tokyo"]
temperatures = [
    [22,23,21,24,25], # New York
    [18,19,17,20,21], # London
    [30,32,31,33,34], # Delhi
    [25,26,24,27,28] # Tokyo
]

fig, ax = plt.subplots(2,2)

# count = 0
# for row in range(2):
#     for col in range(2):
#         ax[row][col].plot(days, temperatures[count])
#         ax[row][col].set_title(f"{cities[count]}")
#         count += 1

ax = ax.flatten()
for i, a in enumerate(ax):
    a.plot(days, temperatures[i])
    a.set_title(cities[i])

fig.suptitle("Temperature in cities over a week")
fig.supxlabel("Temperature")
fig.supylabel("Days")
fig.tight_layout()
plt.show()