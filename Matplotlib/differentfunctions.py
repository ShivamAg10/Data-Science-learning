import matplotlib.pyplot as plt 

x = ["Mon", "Tue", "Wed", "Thr", "Fri"]
y = [10, 15, 7, 20, 12]
z = [19, 18, 17, 26, 15]

plt.plot(x,y, label="week 1")
plt.plot(x,z, label="week 2")

plt.title("Bakery Sales this week")

plt.xlabel("Day of the week")
plt.ylabel("Sales Per Day")

plt.legend(loc='upper left', shadow=True, fancybox=True, framealpha=0.8, ncol=1, title='Data Series')
# plt.legend()
plt.show()