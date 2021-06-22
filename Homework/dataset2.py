from sklearn import metrics
import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import matplotlib.pyplot as pt

df2 = pd.read_csv("datasets/StudentsPerformance.csv")
df2.dropna()

# Below code is used to convert Genre column values to 0(male) & 1(feamle)
# for i in range(len(df2)):
#     if df2.loc[i, 'gender'] == "female":
#         df2.loc[i, 'gender'] = 1
#     if df2.loc[i, 'gender'] == "male":
#         df2.loc[i, 'gender'] = 0
# df2.to_csv("datasets/StudentsPerformance.csv", index=False)

x = df2[['math score', 'reading score', 'writing score']]
y = df2['gender']

# # splitting data into two parts train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
# print(x.shape,x_test.shape)

mod1 = linear_model.LinearRegression()
mod1.fit(x_train, y_train)
p1 = mod1.predict(x_test)
print("LinearRegression:", mod1.score(x_test, y_test))

mod2 = LogisticRegression()
mod2.fit(x_train, y_train)
p2 = mod2.predict(x_test)

mod3 = RandomForestClassifier()
mod3.fit(x_train, y_train)
p3 = mod3.predict(x_test)
print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p3))

mod4 = RandomForestClassifier(criterion="entropy")
mod4.fit(x_train, y_train)
p4 = mod4.predict(x_test)
print("RandomForestClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p4))

mod5 = DecisionTreeClassifier(criterion="gini")
mod5.fit(x_train, y_train)
p5 = mod5.predict(x_test)
print("DecisionTreeClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p5))

mod6 = DecisionTreeClassifier(criterion="entropy")
mod6.fit(x_train, y_train)
p6 = mod6.predict(x_test)
print("DecisionTreeClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p6))

mod8 = SVC(kernel="poly")
mod8.fit(x_train, y_train)
p8 = mod8.predict(x_test)
print("SVC(kernel='poly'):", metrics.accuracy_score(y_test, p8))

mod9 = SVC(kernel="rbf")
mod9.fit(x_train, y_train)
p9 = mod9.predict(x_test)
print("SVC(kernel='rbf'):", metrics.accuracy_score(y_test, p9))

mod10 = SVC(kernel="linear")
mod10.fit(x_train, y_train)
p10 = mod10.predict(x_test)
print("SVC(kernel='linear'):", metrics.accuracy_score(y_test, p10))

mod11 = KNeighborsClassifier(n_neighbors=5)
mod11.fit(x_train, y_train)
p11 = mod11.predict(x_test)
print("KNeighborsClassifier:", mod11.score(x_test, y_test))

mod12 = KMeans(n_clusters=2)
mod12.fit(x_train, y_train)
p12 = mod12.predict(x_test)
print("KMeans:", mod12.score(x_test, y_test))
pt.scatter(p11,y_test,cmap='rainbow')
pt.show()
