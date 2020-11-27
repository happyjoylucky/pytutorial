import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
import time

code = ['A005930','A000660', 'A207940','A035420','A068270']

# res = requests.get("http://comp.fnguide.com/SVO2/ASP/SVD_Finance.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=&NewMenuID=103&stkGb=701")
# res = requests.get("http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A005930&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701")
for code in code:
    url = "http://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode="+code+"&cID=&MenuYn=Y&ReportGB=D&NewMenuID=Y&stkGb=701"
    res = requests.get(url)
    # soup = BeautifulSoup(res.content,'lxml')
    # table = soup.find_all('table')
    # df = pd.read_html(str(table))
    df = pd.read_html(res.text)
    print(tabulate(df[10],headers='keys',tablefmt='psql'))