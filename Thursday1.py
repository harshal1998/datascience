import pandas as pd
from tabulate import tabulate

df = pd.read_excel("a.xls")
# df.dropna(inplace=True)
# df1=df.dropna()
# print(df1)
# df['roll no'].fillna(4,inplace=True)
# df['name'].fillna('akshay',inplace=True)
# df['class'].fillna('fy',inplace=True)
# df.dropna(subset=['class'],inplace=True)
# df.loc[8,'class']="ty"
# df.drop_duplicates(subset=["name"],inplace=True)
# print(df)

df1 = pd.read_csv("heart.csv")
df2 = df1[["age", "sex", "trestbps", "chol", "thalach", "oldpeak"]]
# print(tabulate(df2, headers=["age", "sex", "trestbps", "chol", "thalach", "oldpeak"], tablefmt="simple"))

for i in df2.index:
    if df2.loc[i, "age"] >= 55 and df2.loc[i, "age"] <= 60:
        df2.drop(i, inplace=True)
df2.to_excel("test1.xlsx")
print(tabulate(df2, headers=["age", "sex", "trestbps", "chol", "thalach", "oldpeak"], tablefmt="fancy_grid"))
