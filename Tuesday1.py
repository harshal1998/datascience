import pandas as pd
from tabulate import tabulate

# data = pd.DataFrame({"name": ["harshal", "akshay", "inder"], "class": ["fy", "ty", "sy"]})
# print(data)
# print()
#
# data1 = pd.DataFrame([["abc", "ty"], ["xyz", "sy"]], columns=["name", "class"])
# print(data1)
# print()
#
# data2 = pd.DataFrame({"hours": [2, 1, 4, 6], "calories": [200, 300, 400, 500]}, index=["day1", "day2", "day3", "day4"])
# print(data2)
# print()
# print(data2.loc[["day2"]])
#
# data3 = pd.Series([1, 2, 3, 4], index=("d1", "d2", "d3", "d4"))
# print(data3)
# print(data3["d4"])

# df = pd.read_csv('a.csv')
#
# jdf = pd.read_json("a.json")
# l = []
# d = jdf.loc[0]
# l3 = list(d[0].keys())
# for i in range(len(jdf)):
#     d = jdf.loc[i]
#     l2 = list(d[0].values())
#     l.append(l2)
#
# df2 = pd.DataFrame(l, columns=l3)
# print(df2)


# print(data)
# for i in range(8):
#     if i % 2 != 0:
#         print(df.loc[[i]])


data = pd.read_json("Sample Json with 200 Records.json")
r = []
for i in range(len(data)):
    temp = []
    df = data.loc[i]
    d = df[0]
    id = d["id"]
    name = d["name"]
    title = d["title"]
    description = d["description"]
    location = d["location"]
    temp = [id, name, description, title, location]
    r.append(temp)
df1 = pd.DataFrame(r, columns=["id", "name", "description", "title", "location"])

print(tabulate(df1, headers=["id", "name", "description", "title", "location"], tablefmt='fancy_grid'))
