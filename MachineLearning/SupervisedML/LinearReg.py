import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

insurance_data = pd.read_csv("MachineLearning\DataSet\insurance.csv")
# print(insurance_data)
# print(insurance_data.columns)
# print(insurance_data.dtypes)
# print(insurance_data.isnull().sum())

## Step - 1
# first, we will pre-process this data
# will perform feature engineering (encode the values)(converting data into numerical values)
# Female - 1    Male - 0
# smoker -> yes(1) no(0)
# reigon -> will encode later on
# print(set(insurance_data["sex"].values))
gender_mapping = {
    "male" : 0,
    "female" : 1
}
# print(set(insurance_data["smoker"].values))
smoker_mapping = {
    "yes" : 1,
    "no" : 0
}
insurance_data["sex"] = insurance_data["sex"].map(gender_mapping)
insurance_data["smoker"] = insurance_data["smoker"].map(smoker_mapping)
# print(insurance_data.head())

## Step-2
# Want to look relationship between "bmi" and "charges" values
sns.scatterplot(
    x=insurance_data["bmi"], 
    y=insurance_data["charges"],
    hue=insurance_data["smoker"]
)
# plt.show()

## Step - 3
# Whenever, we prepare our data for Machine Learning Algorithm we divie data into X(input) & Y(output)
X = insurance_data.drop(["charges", "region"], axis=1)
Y = insurance_data["charges"]
# print(X)

## Step=4
# train test split
X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)
# print(Y_test.head())

## Step-5
# Train the Model
model = LinearRegression()
model.fit(X_train, Y_train)

# ## Step-6
# Predicting Values
y_pred = model.predict(X_test)
# print(y_pred[0])
# print(Y_test.iloc[0])

## Step-7
# Evaluting Model
r2 = r2_score(Y_test, y_pred)
print(r2)