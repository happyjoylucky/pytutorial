import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


# res = requests.get("http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701")
res = requests.get("http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')
df = pd.read_html(str(table))
print(tabulate(df[10],headers='keys',tablefmt='psql'))