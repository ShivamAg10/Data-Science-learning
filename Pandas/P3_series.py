import pandas as pd

data = [100,101,102]
series = pd.Series(data)
print(series)

data = [100.1,101.1,102.1]
series = pd.Series(data)
print(series)

data = ["100","101","102"]
series = pd.Series(data)
print(series)

data = [True,True,False]
series = pd.Series(data)
print(series)

data = [100,101,102]
series = pd.Series(data, index=["i", 'ii', "iv"])
print(series)
print(series.loc["i"])
print(series.iloc[2])

print(series[series >= 101])