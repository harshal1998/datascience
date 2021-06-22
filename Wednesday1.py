import pandas as pd
import mysql.connector as m
import random
import string
from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost/harshal')

conn = m.connect(user="root", password="root", host="localhost", database="harshal")
cur = conn.cursor()

# q = "select * from emp"
# cur.execute(q)
# r = cur.fetchall()
# df = pd.DataFrame(r)
# print(df)

# data=pd.read_csv("https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv")
# df=pd.DataFrame(data)
# print(df)

# How to get 1st 5 data
# data = pd.read_json("Sample Json with 200 Records.json")
# r = []
# for i in range(len(data)):
#     temp = []
#     df = data.loc[i]
#     d = df[0]
#     id = d["id"]
#     name = d["name"]
#     temp = [id, name]
#     r.append(temp)
# df1 = pd.DataFrame(r, columns=["id", "name"])
# print(df1.head(10))

# find size
# print(df1.shape)

# dataframe information
# print(df1.info())

# description about statical form data or dataframe int column
# print(df1.describe())
#
# data = pd.read_excel("a.xlsx")
# print(data)

data1 = {"id": [i for i in range(1, 101)],
         "name": [''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 12))) for i in range(1, 101)],
         "salary": [random.randint(30000, 50000) for j in range(1, 101)]}
df = pd.DataFrame(data1)
df.to_sql('emp1', con=engine, if_exists='append', index=False)

conn.commit()
# print(df)

# df.to_csv("test.csv",index=False)
# df.to_excel("test.xls",index=False)
# df.to_excel("test.xlsx", index=False)
# df.to_json("test.json")
