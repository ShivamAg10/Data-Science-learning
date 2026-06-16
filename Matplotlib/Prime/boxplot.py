import matplotlib.pyplot as plt 
import numpy as np 

data = [7,8,5,6,9,4,10,12,15]
# plt.boxplot(data)
plt.grid(True)
# plt.show()

## Multiple Datasets on boxPlot
data1 = np.random.normal(50, 10, 100)
data2 = np.random.normal(60, 15, 100)
# print(data2)
# plt.boxplot([data1, data2], labels = ["group1", "group2"])
# plt.show()

## Horizontal Box Plot
# plt.boxplot(data2, vert=False, showmeans=True)
# plt.show()

## Show Mean in a Box Plot
# plt.boxplot(data2, vert=False, showmeans=True)
# plt.show()

## Changing Whisker Length
plt.boxplot(data2, vert=False, showmeans=True, whis = 1)
plt.show()