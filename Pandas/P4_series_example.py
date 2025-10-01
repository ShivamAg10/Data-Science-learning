import pandas as pd 

calories = {
    "Day1" : 1750,
    "Day2" : 2200.5,
    "Day3" : 1700
}

series = pd.Series(calories)
print(series)