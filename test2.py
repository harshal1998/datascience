import bs4 as bs
import requests
import urllib
import pandas as pd
import random
import urllib

url = "https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiox6SaoMHwAhXTzzgGHeXpAWkQPAgI/fb"
a = requests.get(url).text
sp = bs.BeautifulSoup(a, "lxml")
# print(sp.prettify())
b = requests.get(url, data={"q": "fb"})
print(b.text)