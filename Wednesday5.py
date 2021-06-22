import pandas as pd
import sklearn
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# df = pd.read_csv("diabetes.csv")
# # print(df.to_string())
# df.dropna()
# x = df[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']]
# # print(x)
# y = df['Outcome']
# # print(x.shape, y.shape)
# x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.1, random_state=10)
# # print(x_tr.shape, x_ts.shape)
# # print(y_tr.shape, y_ts.shape)
#
# mod1 = DecisionTreeClassifier(criterion="entropy")
# mod2 = DecisionTreeClassifier()
# mod1.fit(x_tr, y_tr)
# mod2.fit(x_tr, y_tr)
# p1 = mod1.predict(x_ts)
# p2 = mod2.predict(x_ts)
# print(p1)
# print(p2)
# print(metrics.accuracy_score(y_ts, p1))
# print(metrics.accuracy_score(y_ts, p2))


# df1 = pd.read_excel("animal.xlsx")
# # print(df1.to_string())
# x = df1[['animal_height', 'animal_width', 'face_skill ']]
# # print(x.to_string())
# y = df1['animal_type']
# x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.5, random_state=10)
# mod1 = DecisionTreeClassifier(criterion="entropy")
# mod2 = DecisionTreeClassifier()
# mod1.fit(x_tr, y_tr)
# mod2.fit(x_tr, y_tr)
# # p1 = mod1.predict(x_ts)
# p2 = mod2.predict(x_ts)
# # print(p1)
# print(x_ts)
# print(p2)
# df2 = {"x_ts": x_ts, "p2": p2}
# print(df2.to_string())
# # print(metrics.accuracy_score(y_ts, p1))
# print(metrics.accuracy_score(y_ts, p2))


# df1 = pd.read_excel("animal.xlsx")
# # print(df1.to_string())
# x = df1[['animal_height', 'animal_width', 'face_skill ']]
# # print(x.to_string())
# y = df1['animal_type']
# x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.5, random_state=10)
# mod1 = RandomForestClassifier()
# mod2 = RandomForestClassifier(criterion="entropy")
# mod1.fit(x_tr, y_tr)
# mod2.fit(x_tr, y_tr)
# p1 = mod1.predict(x_ts)
# p2 = mod2.predict(x_ts)
# print(p1)
# print(p2)
# print(metrics.accuracy_score(y_ts, p1))
# print(metrics.accuracy_score(y_ts, p2))


df1 = pd.read_excel("Animal.xlsx")
x = df1[['animal_height', 'animal_width', 'face_skill ']]
y = df1['animal_type']
x_tr, x_ts, y_tr, y_ts = train_test_split(x, y, test_size=0.5, random_state=10)
mod1 = RandomForestClassifier()
mod2 = RandomForestClassifier(criterion="entropy")
mod3 = DecisionTreeClassifier(criterion="gini")
mod4 = DecisionTreeClassifier(criterion="entropy")
mod5 = SVC(kernel="linear")
mod6 = SVC(kernel="poly")
mod7 = SVC(kernel="rbf")
mod1.fit(x_tr, y_tr)
mod2.fit(x_tr, y_tr)
mod3.fit(x_tr, y_tr)
mod4.fit(x_tr, y_tr)
mod5.fit(x_tr, y_tr)
mod6.fit(x_tr, y_tr)
mod7.fit(x_tr, y_tr)
p1 = mod1.predict(x_ts)
p2 = mod2.predict(x_ts)
p3 = mod3.predict(x_ts)
p4 = mod4.predict(x_ts)
p5 = mod5.predict(x_ts)
p6 = mod6.predict(x_ts)
p7 = mod7.predict(x_ts)
print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_ts, p1))
print("RandomForestClassifier(criterion='entropy'):", metrics.accuracy_score(y_ts, p2))
print("DecisionTreeClassifier(criterion='gini'):", metrics.accuracy_score(y_ts, p3))
print("DecisionTreeClassifier(criterion='entropy'):", metrics.accuracy_score(y_ts, p4))
print("SVC(kernel='linear):", metrics.accuracy_score(y_ts, p5))
print("SVC(kernel='poly'):", metrics.accuracy_score(y_ts, p6))
print("SVC(kernel='rbf'):", metrics.accuracy_score(y_ts, p7))

import  from ṣ