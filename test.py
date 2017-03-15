import random
import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from xlutils.copy import copy
from xlrd import open_workbook
import time


def RandomUserAgents():
    uas = ["Mozilla"]
    return random.choice(uas)

# load the user agents, in random order
ua = RandomUserAgents()

proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}

headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

w = copy(open_workbook('DL_Magazine_URLs_Padding0.xls'))

file = open('ids.txt')
lines = file.readlines()
c = 0
for i in range(116,len(lines),2):
    try:
        req = Request('http://dl.acm.org/citation.cfm?id=' + lines[i].strip(), headers=headers)
        htmlfile = urlopen(req)
        soup = BeautifulSoup(htmlfile, "html.parser")
        try:
            w.get_sheet(0).write((int)((i+c) / 2 + 1), 19, "dl.acm.org/" + soup.find('a', {"name": "FullTextPDF"})['href'])
        except(TypeError):
            w.get_sheet(0).write((int)((i+c) / 2 + 1), 19, "PDF Not Found")
        w.get_sheet(0).write((int)((i+c) / 2 + 1), 20, soup.find('div', {"id": "references"}).text)
        # print("dl.acm.org/"+soup.find('a', {"name": "FullTextPDF"})['href'])
        w.save('DL_Magazine_URLs_Padding0.xls')
        time.sleep(4)
    except(urllib.error.HTTPError):
        print("Problem with ID :"+lines[i].strip())
        i = i + 2

