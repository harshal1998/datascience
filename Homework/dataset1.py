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

df1 = pd.read_csv("datasets/bestsellers with categories.csv")
df1.dropna()

# # Below code is used to convert Genre column values to 0(Non Fiction) & 1(Fiction)
# for i in range(len(df1)):
#     if df1.loc[i, 'Genre'] == "Non Fiction":
#         df1.loc[i, 'Genre'] = 0
#     if df1.loc[i, 'Genre'] == "Fiction":
#         df1.loc[i, 'Genre'] = 1
# df1.to_csv("datasets/bestsellers with categories.csv")

# # now we r going to predict genre using user rating,reviews, price, year

x = df1[['User Rating', 'Reviews', 'Price', 'Year']]
y = df1['Genre']

# # splitting data into two parts train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# print(x,x_test.shape)

mod1 = linear_model.LinearRegression()
mod1.fit(x_train, y_train)
p1 = mod1.predict(x_test)
print("LinearRegression:", mod1.score(x_test, y_test))

mod2 = LogisticRegression()
mod2.fit(x_train, y_train)
p2 = mod2.predict(x_test)
print("LogisticRegression:", mod2.score(x_test, y_test))

mod3 = RandomForestClassifier()
mod3.fit(x_train, y_train)
p3 = mod3.predict(x_test)
print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p3))

mod4 = RandomForestClassifier(criterion="entropy")
mod4.fit(x_train, y_train)
p4 = mod4.predict(x_test)
print("RandomForestClassifier(criterion='entropy'):", mod4.score(x_test, y_test))

mod5 = DecisionTreeClassifier(criterion="gini")
mod5.fit(x_train, y_train)
p5 = mod5.predict(x_test)
print("DecisionTreeClassifier(criterion='gini'):", mod5.score(x_test, y_test))

mod6 = DecisionTreeClassifier(criterion="entropy")
mod6.fit(x_train, y_train)
p6 = mod6.predict(x_test)
print("DecisionTreeClassifier(criterion='entropy'):", mod6.score(x_test, y_test))

mod8 = SVC(kernel="poly")
mod8.fit(x_train, y_train)
p8 = mod8.predict(x_test)
print("SVC(kernel='poly'):", mod8.score(x_test, y_test))

mod9 = SVC(kernel="rbf")
mod9.fit(x_train, y_train)
p9 = mod9.predict(x_test)
print("SVC(kernel='rbf'):", mod9.score(x_test, y_test))

mod11 = KNeighborsClassifier(n_neighbors=5)
mod11.fit(x_train, y_train)
p11 = mod11.predict(x_test)
print("KNeighborsClassifier:", mod11.score(x_test, y_test))

mod12 = KMeans(n_clusters=2)
z = df1.iloc[:, [1, 2, 3, 4]].values
p12 = mod12.fit_predict(z)
print(p12)
