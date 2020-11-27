from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# def getName(url):
#     try:
#         html = urlopen(url)
#     except HTTPError as e:
#         return None
#     try:
#         bsObj = BeautifulSoup(html,"html.parser")
#         bsObj.findAll("span",{"class":"green"})
#     except AttributeError as e:
#         return None

# nameList = getName("http://www.pythonscraping.com/pages/warandpeace.html")

# if nameList == None:
#     print("Name could not be found.")
# else:
#     for name in nameList:
#         print(name.get_text())

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,"html.parser")
nameList = bsObj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
