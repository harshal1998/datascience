import numpy as np
import random
import pandas as pd
import sklearn as sk
from sklearn import linear_model
from sklearn.model_selection import cross_val_score
import matplotlib.pyplot as pt

df = pd.read_excel("car.xlsx")
# print(df.to_string())
# x = np.array(df['Distance']).reshape(-1, 1)
# y = df['Speed']
# print(x,y,sep="\n")

# mod1 = linear_model.LinearRegression()
# mod1.fit(x, y)
#
# testdata = pd.DataFrame({"dist": [100000, 200, 40000, 10, 1]})
# p = mod1.predict(testdata)
# print(p)
# print(mod1.score(x, y))
# sco = cross_val_score(mod1, x, y, cv=5)
# print(sco)
# print(sco.mean(), sco.std())
# pt.scatter(x, y)
# pt.plot(x, mod1.predict(x))
# pt.show()

# print(type(y))
# x = df['Distance']
# y = df['Speed']
# time=[]
# for i in range(27):
#     a=df.loc[i,'Distance']/df.loc[i,'Speed']
#     time.append(round(a,2))
#     df.loc[i,'time']=round(a,2)
# print(df)
# df.to_excel("car.xlsx")

x = df[['Distance', 'time']]
y = df['Speed']
mod1 = linear_model.LinearRegression()
mod1.fit(x, y)

testdata = [[5000, 2]]
p = mod1.predict(testdata)
print(p)
print(mod1.score(x, y))
sco = cross_val_score(mod1, x, y, cv=5)
print(sco)
print(sco.mean(), sco.std())

# plt.subplot(1, 2, 1)
# plt.plot(x,y)
