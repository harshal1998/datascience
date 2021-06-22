from sklearn import metrics
import pandas as pd
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, cross_val_score
import numpy as np
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# df1 = pd.read_csv("datasets/bestsellers with categories.csv")
# df1.dropna()
# #
# # # Below code is used to convert Genre column values to 0(Non Fiction) & 1(Fiction)
# for i in range(len(df1)):
#     if df1.loc[i,'Genre']=="Non Fiction":
#         df1.loc[i,'Genre']=0
#     if df1.loc[i,'Genre']=="Fiction":
#         df1.loc[i,'Genre']=1
# df1.to_csv("datasets/bestsellers with categories.csv")
#
# now we r going to predict genre using user rating,reviews, price, year
#
# x = df1[['User Rating', 'Reviews', 'Price', 'Year']]
# y = df1['Genre']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
# # print(x_test.shape)
#
# mod1 = linear_model.LinearRegression()
# mod1.fit(x_train, y_train)
# p1 = mod1.predict(x_test)
# print("LinearRegression:",mod1.score(x_test,y_test))
#
# mod2 = LogisticRegression()
# mod2.fit(x_train, y_train)
# p2 = mod2.predict(x_test)
#
# mod3 = RandomForestClassifier()
# mod3.fit(x_train, y_train)
# p3 = mod3.predict(x_test)
# print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p3))
#
# mod4 = RandomForestClassifier(criterion="entropy")
# mod4.fit(x_train, y_train)
# p4 = mod4.predict(x_test)
# print("RandomForestClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p4))
#
# mod5 = DecisionTreeClassifier(criterion="gini")
# mod5.fit(x_train, y_train)
# p5 = mod5.predict(x_test)
# print("DecisionTreeClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p5))
#
# mod6 = DecisionTreeClassifier(criterion="entropy")
# mod6.fit(x_train, y_train)
# p6 = mod6.predict(x_test)
# print("DecisionTreeClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p6))
#
# mod8 = SVC(kernel="poly")
# mod8.fit(x_train, y_train)
# p8 = mod8.predict(x_test)
# print("SVC(kernel='poly'):", metrics.accuracy_score(y_test, p8))
#
# mod9 = SVC(kernel="rbf")
# mod9.fit(x_train, y_train)
# p9 = mod9.predict(x_test)
# print("SVC(kernel='rbf'):", metrics.accuracy_score(y_test, p9))
#
# mod10 = SVC(kernel="linear")
# mod10.fit(x_train, y_train)
# p10 = mod10.predict(x_test)
# print("SVC(kernel='linear'):", metrics.accuracy_score(y_test, p10))
#
# # for these df1 dataset RandomForestClassifier(gini) gives best results.


# df2 = pd.read_csv("datasets/StudentsPerformance.csv")
# df2.dropna()
#
# # Below code is used to convert Genre column values to 0(male) & 1(feamle)
# # for i in range(len(df2)):
# #     if df2.loc[i, 'gender'] == "female":
# #         df2.loc[i, 'gender'] = 1
# #     if df2.loc[i, 'gender'] == "male":
# #         df2.loc[i, 'gender'] = 0
# # df2.to_csv("datasets/StudentsPerformance.csv", index=False)
#
# x = df2[['math score', 'reading score', 'writing score']]
# y = df2['gender']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
#
# mod1 = linear_model.LinearRegression()
# mod1.fit(x_train, y_train)
# p1 = mod1.predict(x_test)
# print("LinearRegression:",mod1.score(x_test,y_test))
#
# mod2 = LogisticRegression()
# mod2.fit(x_train, y_train)
# p2 = mod2.predict(x_test)
#
# mod3 = RandomForestClassifier()
# mod3.fit(x_train, y_train)
# p3 = mod3.predict(x_test)
# print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p3))
#
# mod4 = RandomForestClassifier(criterion="entropy")
# mod4.fit(x_train, y_train)
# p4 = mod4.predict(x_test)
# print("RandomForestClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p4))
#
# mod5 = DecisionTreeClassifier(criterion="gini")
# mod5.fit(x_train, y_train)
# p5 = mod5.predict(x_test)
# print("DecisionTreeClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p5))
#
# mod6 = DecisionTreeClassifier(criterion="entropy")
# mod6.fit(x_train, y_train)
# p6 = mod6.predict(x_test)
# print("DecisionTreeClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p6))
#
# mod8 = SVC(kernel="poly")
# mod8.fit(x_train, y_train)
# p8 = mod8.predict(x_test)
# print("SVC(kernel='poly'):", metrics.accuracy_score(y_test, p8))
#
# mod9 = SVC(kernel="rbf")
# mod9.fit(x_train, y_train)
# p9 = mod9.predict(x_test)
# print("SVC(kernel='rbf'):", metrics.accuracy_score(y_test, p9))
#
# mod10 = SVC(kernel="linear")
# mod10.fit(x_train, y_train)
# p10 = mod10.predict(x_test)
# print("SVC(kernel='linear'):", metrics.accuracy_score(y_test, p10))
#
# # for df2 excluding LinearRegression every other model is giving good results

# df3 = pd.read_csv("datasets/vgsales.csv")
# df3.dropna()
#
# x = df3[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']]
# y = df3['Global_Sales']
#
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.01)
#
# mod1 = linear_model.LinearRegression()
# mod1.fit(x_train, y_train)
# p1 = mod1.predict(x_test)
# print("LinearRegression:", mod1.score(x_test, y_test))

# df4 = pd.read_csv("datasets/winequality-red.csv")
# df4.dropna()
#
# x=df4[['citric acid','residual sugar','chlorides','alcohol']]
# y=df4['quality']
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
#
# mod1 = linear_model.LinearRegression()
# mod1.fit(x_train, y_train)
# p1 = mod1.predict(x_test)
# print("linearregression:", mod1.score(x_test,y_test))
#
# mod3 = RandomForestClassifier()
# mod3.fit(x_train, y_train)
# p3 = mod3.predict(x_test)
# print("RandomForestClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p3))
#
# mod4 = RandomForestClassifier(criterion="entropy")
# mod4.fit(x_train, y_train)
# p4 = mod4.predict(x_test)
# print("RandomForestClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p4))
#
# mod5 = DecisionTreeClassifier(criterion="gini")
# mod5.fit(x_train, y_train)
# p5 = mod5.predict(x_test)
# print("DecisionTreeClassifier(criterion='gini'):", metrics.accuracy_score(y_test, p5))
#
# mod6 = DecisionTreeClassifier(criterion="entropy")
# mod6.fit(x_train, y_train)
# p6 = mod6.predict(x_test)
# print("DecisionTreeClassifier(criterion='entropy'):", metrics.accuracy_score(y_test, p6))
#
# mod8 = SVC(kernel="poly")
# mod8.fit(x_train, y_train)
# p8 = mod8.predict(x_test)
# print("SVC(kernel='poly'):", metrics.accuracy_score(y_test, p8))
#
# mod9 = SVC(kernel="rbf")
# mod9.fit(x_train, y_train)
# p9 = mod9.predict(x_test)
# print("SVC(kernel='rbf'):", metrics.accuracy_score(y_test, p9))
#
# mod10 = SVC(kernel="linear")
# mod10.fit(x_train, y_train)
# p10 = mod10.predict(x_test)
# print("SVC(kernel='linear'):", metrics.accuracy_score(y_test, p10))


