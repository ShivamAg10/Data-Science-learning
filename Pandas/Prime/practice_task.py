import pandas as pd 

df = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\w_data.csv")

## Shift Id column to last
# new_col_order = [col for col in df.columns if col != "id"] + ["id"]
# df= df[new_col_order]
# # print(df)

# print(df.isnull().sum())
# print(df)

## Handling Null Values in Name
df["name"] = df["name"].fillna("Not Defined")
# print(df)

## Handling Null Values in Age
df["age"] = df["age"].ffill()
# print(df)

## Handling Null Values in Country
df["country"] = df['country'].bfill()
# print(df)

## Handling Null Values in Gender
gender_map = {
    "Male" : "M",
    "Female" : "F",
    "Unknown" : "U"
}
df["gender"] = df['gender'].map(gender_map).fillna("U")
# print(df)

## Handling Null Values in Income
df["income"] = df["income"].fillna(0)
# print(df)

## droping Duplicates
df.drop_duplicates(inplace = True)
# print(df)

## Sorting according to name - A to Z
df = df.sort_values("name")
# print(df)

## Index values
df = df.reset_index(drop = True)
# print(df)

df.to_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\sorted_data.csv")


## Assignment Dataset
iris_flower = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\IRIS.csv")
titanic = pd.read_csv("D:\desktop\Data Science Learning\Data-Science-learning\Pandas\Prime\Titanic-Dataset.csv")

# Iris Flower Dataset Problems

# 1. Display the following information:
# a. First 10 Rows
# print(iris_flower.head(10))
# b. Shape and DataType
# print(iris_flower.shape, iris_flower.dtypes)
# c. Summary Statistics (mean, std, min, max)
# print(iris_flower.info())

# 2. Select those rows where petal_length>4.5 and species="iris-virginica"
# print(iris_flower[(iris_flower["petal_length"] > 4.5) & (iris_flower['species']=='Iris-virginica')])

# 3.Group By species and Compute Avg Sepal_Length, Maximum Patel Width and Standard deviation of sepal_width
answer = iris_flower.groupby('species').agg(
    Avg_Sepal_Length = ("sepal_length", "mean"),
    Max_Petal_Width = ("petal_width", "max"),
    Std_Sepal_Width = ("sepal_width", "std")
)
# print(answer)

# 4. Creating New Column: "petal ratio" = petal_length / petal_width
iris_flower["petal_ratio"] = iris_flower['petal_length']/iris_flower['petal_width']
# print(iris_flower)

# Titanic dataset

# 1. Display only columns - Name, Sex, Age, Fare, Survived
# print(titanic[["Name", "Sex", "Age", "Fare", "Survived" ]])

# 2. Select Passenger whose are Female and Fare > 30
# print(titanic.dtypes)
# print(titanic[(titanic["Sex"] == "female") & (titanic["Fare"] > 30.0)][["Sex", "Fare"]])

# 3. Group By Pclass  and Compute Survival Rate, Average Fare, Average Age
grouping = titanic.groupby("Pclass").agg(
    Survival_Rate = ("Survived", "mean"),
    Avg_Fare = ("Fare", "mean"),
    Avg_Age = ("Age", "mean")
)
print(grouping)
# print(titanic["Pclass"])