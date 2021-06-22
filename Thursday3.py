import urllib

import requests
import bs4 as bs
import pandas as pd
import xlsxwriter

# url = requests.get("https://www.tiobe.com/tiobe-index/").text
# data = bs.BeautifulSoup(url, "lxml")
# # print(data.prettify())
# # table = data.find_all('table')
# # table = data.find('table')
# table1 = data.find("table", attrs={"id": "top20"})
# table2 = data.find("table", attrs={"id": "otherPL"})
# table3 = data.find("table", attrs={"id": "VLTH"})
# table4 = data.find("table", attrs={"id": "PLHoF"})
#
# a = []
# tddata1 = []
# tddata2 = []
# tddata3 = []
# tddata4 = []
# for i in [table1, table2, table3, table4]:
#     tr = i.find_all('tr')
#     for j in tr:
#         td = j.find_all('td')
#         temp = [i.text for i in td]
#         if i == table1:
#             tddata1.append(temp)
#         if i == table2:
#             tddata2.append(temp)
#         if i == table3:
#             tddata3.append(temp)
#         if i == table4:
#             tddata4.append(temp)
#
# del tddata1[0]
# del tddata2[0]
# del tddata3[0]
# del tddata4[0]
# # print(tddata1)
#
# writer = pd.ExcelWriter('scrap1.xlsx', engine='xlsxwriter')
#
# df1 = pd.DataFrame(tddata1,columns=["May 2021","May 2020","Change","Programming Language","Ratings","Change"])
# df1.to_excel(writer, sheet_name='Sheet1', index=False)
#
# df2 = pd.DataFrame(tddata2,columns=["Position","Programming Language","Ratings"])
# df2.to_excel(writer, sheet_name='Sheet2',index=False)
#
# df3 = pd.DataFrame(tddata3,columns=["Programming Language","2021","2016","2011","2006","2001","1996","1991","1986"])
# df3.to_excel(writer, sheet_name='Sheet3',index=False)
#
# df4 = pd.DataFrame(tddata4,columns=["Year","Winner"])
# df4.to_excel(writer, sheet_name='Sheet4',index=False)
#
# writer.save()

# url = requests.get("http://100photos.time.com").text
# data = bs.BeautifulSoup(url, "lxml")
# # print(data.prettify())
# idata=data.find_all('img')
# # print(idata)
# a=[]
# b=[]
# for i in idata:
#     # print(i)
#     src=i['src']
#     nm=i['alt']
#     # print(src,nm)
#     a.append(src)
#     b.append(nm)
# # print(a)
# c={"Name":b,"Src":a}
#
# df=pd.DataFrame(c)
#
# df.to_excel("scrap3.xlsx",index=False)
# x=pd.read_excel("scrap3.xlsx")


# url = requests.get("https://www.forbes.com/billionaires/").text
# data = bs.BeautifulSoup(url, "lxml")
# print(data.prettify())


# url1 = urllib.request.urlopen("https://www.forbes.com/billionaires/").read()
# sp = bs.BeautifulSoup(url1, "lxml")
# print(sp)


# heading = []
# description = []
# for i in range(10):
#     url = "https://www.indiatoday.in/latest-headlines"+"?page="+str(i)
#     print(url)
#     d = requests.get(url).text
#     sp = bs.BeautifulSoup(d, "lxml")
#     # print(sp.prettify())
#     data = sp.find('section', attrs={"id": "content"})
#     # print(data.prettify())
#     h = data.find_all("h2")
#     d = data.find_all("p")
#     # print(d)
#
#     h.pop()
#     for i in h:
#         news = i['title']
#         heading.append(news)
#
#     for i in d:
#         desc = i.text
#         description.append(desc)
#
# r = {"Headlines": heading, "Description": description}
# df = pd.DataFrame(r)
# # print(df.to_string())
# df.to_csv("scrap.csv", index=False)

url="https://main.sci.gov.in/case-status"
a=requests.get(url).text
sp=bs.BeautifulSoup(a,"lxml")
# print(sp.prettify())
data=sp.find('p',attrs={"id":"cap"})
print(data)

