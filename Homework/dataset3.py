from sklearn import metrics
import pandas as pd
from sklearn import linear_model
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df3 = pd.read_csv("datasets/vgsales.csv")
df3.dropna()

x = df3[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
y = df3['Global_Sales']

# # splitting data into two parts train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01)
# print(x.shape,x_test.shape)

mod1 = linear_model.LinearRegression()
mod1.fit(x_train, y_train)
p1 = mod1.predict(x_test)
print("LinearRegression:", mod1.score(x_test, y_test))

mod11 = KNeighborsClassifier(n_neighbors=3)
mod11.fit(x_train, y_train)
p11 = mod11.predict(y_test)
print("KNeighborsClassifier:", mod11.score(x_test, y_test))

# mod12 = KMeans(n_clusters=2)
# mod12.fit(x_train, y_train)
# p12 = mod12.predict(x_test)
# print("KMeans:", mod12.score(x_test, y_test))
