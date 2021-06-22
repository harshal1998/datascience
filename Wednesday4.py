import pandas as pd
import sklearn
from sklearn import linear_model
import numpy as np

# df = pd.read_csv("insurance.csv")
# # print(len(df))
# for i in range(len(df)):
#     if df.loc[i, "sex"] == "male":
#         df.loc[i, "sex"] = 0
#     if df.loc[i, "sex"] == "female":
#         df.loc[i, "sex"] = 1
# print(df.to_string())
# df1=df[["age","sex","bmi","children","smoker","charges"]]
# # print(df1.to_string())
# df1.to_csv("insurance1.csv")
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# df = pd.read_csv("insurance1.csv")
# # for i in range(len(df)):
# #     if df.loc[i, "smoker"] == "yes":
# #         df.loc[i, "smoker"] = 1
# #     if df.loc[i, "smoker"] == "no":
# #         df.loc[i, "smoker"] = 0
# # print(df.to_string())
# # df.to_csv("insurance1.csv",index=False)
#
# x = df[["age", "sex", "bmi", "children", "smoker"]]
# # print(type(x))
# y = df["charges"]
# mod1 = linear_model.LinearRegression()
# mod1.fit(x, y)
# p = mod1.predict(x)
# # print(mod1.score(x,y))
# sco = cross_val_score(mod1, x, y, cv=5)
# # print(sco)
# # print(sco.mean(), sco.std())


# df=pd.read_excel("addm.xlsx")
# df.dropna()
# # print(df.to_string())
# x=np.array(df['percentage']).reshape(-1,1)
# # print(x)
# y=df['addmision']
# mod2 = LogisticRegression()
# mod2.fit(x,y)
# p=mod2.predict(x)
# print(mod2.score(x,y))

# df=pd.read_csv("insurance1.csv")
# x=df[["age","sex","bmi"]]
# y=df['smoker']
# mod=LogisticRegression()
# mod.fit(x,y)
# p=mod.predict(x)
# print(mod.score(x,y))

# df = pd.read_excel("train.xlsx")
# # print(df.to_string())
# x = df[["Pclass", "Sex", "Age"]]
# y = df["Survived"]
# mod = LogisticRegression()
# mod.fit(x, y)
# p = mod.predict(x)
# print(mod.score(x, y))
# # for i in p:
# #     print(i)
# sco = cross_val_score(mod, x, y, cv=10)
# print(sco)
# print(sco.mean(), sco.std())
