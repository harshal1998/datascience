import urllib.request
import requests
import bs4 as bs
import pandas as pd

# url1 = urllib.request.urlopen("https://www.w3schools.com/").read()
# sp = bs.BeautifulSoup(url1, "lxml")
# print(sp)

# url = "https://www.w3schools.com/html/html_tables.asp"
# text = requests.get(url).text
# # print(text)
# data = bs.BeautifulSoup(text, "lxml")
# # print(bs.prettify())
# tbdata = []
# tb = data.find('table')
# # print(tb.prettify())
# tr = tb.find_all('tr')
# data1 = []
# for i in tr:
#     th = i.find_all('th')
#     thdata = [i.text for i in th]
#
# for i in tr:
#     td = i.find_all('td')
#     tddata = [i.text for i in td]
#     data1.append(tddata)
# # print(data1)
# df = pd.DataFrame(data1,columns=["company","contact","country"])
# print(df)

url = requests.get("https://pythonprogramming.net/parsememcparseface/").text
data = bs.BeautifulSoup(url, "lxml")
# print(data.prettify())
table = data.find('table')
# print(table.prettify())
tr = table.find_all('tr')
# print(tr)
data1 = []

for i in tr:
    td = i.find_all('td')
    tddata = [i.text for i in td]
    data1.append(tddata)
del data1[0]

df = pd.DataFrame(data1, columns=["Program Name", "Internet Points", "Kittens?"])
print(df)
df.to_excel("scrap.xlsx")
