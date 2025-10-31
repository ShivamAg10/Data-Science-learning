import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Practice\San_Francisco_City_Employee_Salary_DataSet\Salaries.csv")
# print(df)

# 1.  Display Top 10 Rows of The Dataset
# print(df.head(10))

# 2. Check Last 10 Rows of The Dataset
# print(df.tail(10))

# 3. Find Shape of Our Dataset (Number of Rows And Number of Columns)
# print(df.shape)

# 4.  Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requiremen
# print(df.info())

# 5. Check Null Values In The Dataset
# print(df.isnull())

# 6. Drop ID, Notes, Agency, and Status Columns
# df = df.drop(columns=["Id", "Notes", "Agency", "Status"])
# print(df.head())

# 7. Get Overall Statistics About The Dataframe
# print(df.describe())

# 8. Find Occurrence of The Employee Names  (Top 5)
print(df["EmployeeName"].head()) # Wrong

# 9. Find The Number of Unique Job Titles
# print(len(df["JobTitle"].unique()))

# 10.Total Number of Job Titles Contain Captain
print(df["JobTitle"])