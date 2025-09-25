import numpy as np 

# Create a program to change a string element in a specified numpy array to uppercase, lowercase, capitalize first letter, title-case or swapcase.

str_arr = np.array(["hi", "My", "name", "is", "SHIVAM"])
print(str_arr)

upper = np.char.upper(str_arr)
print(upper)

lower = np.char.lower(str_arr)
print(lower)

capitalize = np.char.capitalize(str_arr)
print(capitalize)

title = np.char.title(str_arr)
print(title)

swapcase = np.char.swapcase(str_arr)
print(swapcase)