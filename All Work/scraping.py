import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from xlutils.copy import copy    
from xlrd import open_workbook
import time

w = copy(open_workbook('DL_Magazine_URLs_Padding0.xls'))
x = 0
file = open('ids.txt')
lines = file.readlines()
ids_array = []
for line in lines:
    req = Request('http://dl.acm.org/citation.cfm?id=1618591', headers={'User-Agent': 'chrome'})
    htmlfile = urlopen(req)
    soup = BeautifulSoup(htmlfile, "html.parser")
    w.get_sheet(0).write(x, 6, soup.find('td', {"style": "padding-left:10px;"}).text)
    print(soup.find('td', {"style": "padding-left:10px;"}).text)
    w.save('Updated_DL_Magazine_URLs_Padding0.xls')
    x = x + 1
    time.sleep(5)