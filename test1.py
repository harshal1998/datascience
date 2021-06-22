import bs4 as bs
import requests
import urllib
import pandas as pd
import random
import urllib
import re

# url = "https://main.sci.gov.in/case-status"
# a1 = urllib.request.urlopen(url).read()
# a = requests.get(url).text
# sp = bs.BeautifulSoup(a, "lxml")
# sp1 = bs.BeautifulSoup(a1, "lxml")
# # print(a)
# # print(sp1)
# data = sp1.find("p", attrs={"id": "cap"})
# print(data.prettify())


url = "https://citizen.mahapolice.gov.in/Citizen/MH/PublishedFIRs.aspx"
a = requests.get(url).text
# print(a)
sp = bs.BeautifulSoup(a, "lxml")
dfrom = sp.find("input", attrs={"id": "ContentPlaceHolder1_txtDateOfRegistrationFrom"})
dto = sp.find("input", attrs={"id": "ContentPlaceHolder1_txtDateOfRegistrationTo"})
unit = sp.find("select", attrs={"id": "ContentPlaceHolder1_ddlDistrict"})
district = ["THANE CITY", "THANE RURAL", "NAVI MUMBAI", "RAILWAY MUMBAI"]
temp = random.sample(district, 1)
# print(type(temp[0]))
Data = {'ctl00$ContentPlaceHolder1$txtDateOfRegistrationFrom': '01-01-2021',
        'ctl00$ContentPlaceHolder1$txtDateOfRegistrationTo': '24-04-2021',
        'ctl00$ContentPlaceHolder1$ddlDistrict': 'NAVI MUMBAI'}
# print(data)
b = requests.post(url, data=Data).text
# print(b)
sp1 = bs.BeautifulSoup(b, "lxml")
print(sp1.prettify())
xy=(re.findall())
# t = sp.find_all("div", {"class": "margintopgrid"})
# t1=t[2].find("div")
# # print(t1)
# t2=t1.find("table")
# print(t2)
