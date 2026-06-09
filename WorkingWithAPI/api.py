import requests
import pandas as pd 

url = "https://stephen-king-api.onrender.com/api/books"
a = requests.get(url)
# print(a)
data = a.json()
# print(data)
df = pd.json_normalize(data["data"])
df.to_csv("books.csv")