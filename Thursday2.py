import pandas as pd
import matplotlib.pyplot as pt
import numpy as np
from numpy import random
from tabulate import tabulate
from sqlalchemy import create_engine
import mysql.connector as m

# conn = m.connect(user="root", password="root", host="localhost", database="harshal")
# cur = conn.cursor()
# engine = create_engine('mysql://root:root@localhost/harshal')
# df = pd.read_csv("train.csv")
# df.dropna(inplace=True)
#
# for i in df.index:
#     if df.loc[i, "Sex"] == "male":
#         df.loc[i, "Sex"] = 1
#     if df.loc[i, "Sex"] == "female":
#         df.loc[i, "Sex"] = 0
# print(df.to_string())
# df.to_sql('train', con=engine, if_exists='append', index=False)
#
#
# dbdata = pd.read_sql_table("train", engine)
#
# dbdata.to_excel("train.xlsx")

# df1 = df[["Survived", "Sex"]]
# print(df1.to_string())

# sur=np.array(df1["Survived"])
# sex=np.array(df1["Sex"])
#
# pt.subplot(1,2,1)
# pt.title("Survived")
# pt.hist(sur)
# pt.subplot(1,2,2)
# pt.title("Gender")
# pt.hist(sex)
# pt.show()

x = np.array([random.randint(1, 30) for i in range(100)])
y = np.array([random.randint(20, 100) for i in range(100)])
pt.scatter(x, y)
pt.show()

m1 = np.reshape(x, (10, 10))
print("Matrix1:\n", m1, end="\n\n")

m2 = np.reshape(y, (10, 10))
print("Matrix2:\n", m2, end="\n\n")

print("Addition:\n", m1 + m2, end="\n\n")
print("Subtraction:\n", m1 - m2)
