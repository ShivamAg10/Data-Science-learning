import matplotlib.pyplot as plt 

x  = [1,2,3,4]
y = [5,6,7,8]
# plt.plot(x,y)
# plt.show()

oscar_movies = [
    "The Dark Knight",
    "The Hurt Locker",
    "The King's Speech",
    "The Artist",
    "Argo"
]
years = [2008, 2009, 2010, 2011, 2012]
oscar_revenue = [1005, 170, 427, 133, 232]  # in $M
non_oscar_movies = [
    "Slumdog Millionaire",
    "Avatar", 
    "Inception",
    "hugo",
    "Lincoln"
]
non_oscar_revenue = [378, 2788, 829, 185, 275]
plt.plot(years, oscar_revenue, "o--r",label = "Oscar Movies")
plt.plot(years, non_oscar_revenue, "<:y", label = "Non Oscar Movies")
plt.title("Oscar Movie Revenue v/s Non Oscar Movie Revenue")
plt.xlabel("Years")
plt.ylabel("Revenue in $M")
plt.legend()
plt.show()