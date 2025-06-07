import numpy as np 
import matplotlib.pyplot as plt 

sales_data = np.array( [
    [1, 150000, 180000, 220000, 250000],     # Paradise Biryani
    [2, 120000, 140000, 160000, 190000],     # Beijing Bites
    [3, 200000, 230000, 260000, 300000],     # Pizza Hub
    [4, 180000, 210000, 240000, 270000],     # Burger Point
    [5, 160000, 185000, 205000, 230000]     # Chai Point
] )

print("------ Zomato sales analysis ------")
print("Sales Data Shape: ", sales_data.shape)
print("Sample data for 1st 3 restaurant: \n", sales_data[:3])
print("Data without restaurant id's: \n ", sales_data[:, 1:])

print("\n\n----- Total Sales Per Year -----\n", np.sum(sales_data[:, 1:], axis = 0))
print("\n\n----- Yearly Total of each restaurant-----\n", np.sum(sales_data[:, 1:], axis = 1))

print("\n\n----- Minimum sales per restaurant -----\n", np.min(sales_data[:, 1:], axis=1))

print("\n\n----- Minimum sales per Year -----\n", np.max(sales_data[:, 1:], axis=0))

print("\n\n----- Average sales per restaurant -----\n", np.mean(sales_data[:, 1:], axis=1))

print("\n\n----- Cumulative sum per restaurant -----\n", np.cumsum(sales_data[:, 1:], axis=1))

plt.figure(figsize=(10,6))
plt.plot(np.mean((np.cumsum(sales_data[:, 1:], axis=1)), axis=0))
plt.title("Average Cumulative sales across all restaurant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()