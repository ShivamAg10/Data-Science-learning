import matplotlib.pyplot as plt 
import numpy as np 

days = ["Mon", "Tue", "Wed", "Thr", "Fri", "Sat", "Sun"]
# Number of customers in different field
direct = np.random.randint(10,100,7)
organic = np.random.randint(10,100,7)
social = np.random.randint(10,100,7)

# plt.boxplot([direct, organic, social])
plt.stackplot(days, direct, organic, social, labels=["direct", "organic", "social"])
plt.title("Marketing Data for the week")
plt.xlabel("Days")
plt.ylabel("# of customers")
plt.legend()
plt.grid(True)
plt.show()