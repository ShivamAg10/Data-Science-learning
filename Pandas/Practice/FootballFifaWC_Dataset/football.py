import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Practice\FootballFifaWC_Dataset\wc_tournaments.csv")
# print(df)

# Q.1. Load your wc_tournaments.csv file into a Pandas DataFrame named df. 
# Write a script that extracts the top_scorer_goals column as a high-performance NumPy float64 array and 
# uses a NumPy vector method to find the maximum number of goals scored by an individual player in a single 
# tournament.
max_goals = df["top_scorer_goals"].to_numpy().max()
# print(max_goals)

# Q.2. Convert both the total_matches and total_goals columns simultaneously into a 2D NumPy array named stats_matrix. 
# Write a command using stats_matrix to calculate the overall average of matches and goals across all 
# historical tournaments respectively, ensuring your output contains two distinct values (one for matches, one for goals).
answer2 = df[["total_matches", "total_goals"]].to_numpy().mean(axis=0)
# print(answer2)

# Q.3. Write a Pandas vector-based boolean mask that filters the DataFrame to return only the rows where the 
# tournament's host_nation successfully won the tournament (i.e., where host_nation matches the champion).
answer3 = df[df["host_nation"] == df["champion"]]
# print(answer3)

import random
print(random.randint(1,13))