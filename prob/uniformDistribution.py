# Uniform Distribution
import numpy as np
import matplotlib.pyplot as plt

# values from 0 to 10
values = np.random.uniform(0, 10, 10_00_0000)
print(values)

# plotting a histogram - becomes more uniform with more values
plt.hist(values, bins=100, density=True, alpha=0.3)

plt.title("Continuous Uniform Distribution between 0 and 10")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.grid(True)

plt.show()