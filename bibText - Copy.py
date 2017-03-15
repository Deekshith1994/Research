from urllib.request import Request, urlopen
from xlutils.copy import copy
from xlrd import open_workbook
from pybtex.database.input import bibtex
import time

w = copy(open_workbook('DL_Magazine_URLs_Padding0.xls'))
for i in range(0,10): w.get_sheet(0).write(0,i,"")

file = open('ids.txt')
lines = file.readlines()
parser = bibtex.Parser()

for i in range(0, 500):
    address = 'http://dl.acm.org/exportformats.cfm?id='+lines[i].strip()+'&expformat=bibtex'
    req = Request(address, headers={'User-Agent': 'Mozilla'})
    htmlfile = urlopen(req)
    htmltext = htmlfile.read()
    bibdata = parser.parse_bytes(htmltext)
    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        try:
            w.get_sheet(0).write(i+1,0,lines[i])
            w.get_sheet(0).write(i+1, 1, htmltext.decode())
            w.get_sheet(0).write(i+1, 2, b["author"])
            w.get_sheet(0).write(i+1, 3, b["title"])
            w.get_sheet(0).write(i+1, 4, b["journal"])
            w.get_sheet(0).write(i+1, 5, b["issue_date"])
            w.get_sheet(0).write(i+1, 6, b["volume"])
            w.get_sheet(0).write(i+1, 7, b["number"])
            w.get_sheet(0).write(i+1, 8, b["month"])
            w.get_sheet(0).write(i+1, 9, b["year"])
            w.get_sheet(0).write(i+1, 10, b["issn"])
            w.get_sheet(0).write(i+1, 11, b["pages"])
            w.get_sheet(0).write(i+1, 12, b["numpages"])
            w.get_sheet(0).write(i+1, 13, b["url"])
            w.get_sheet(0).write(i+1, 14, b["doi"])
            w.get_sheet(0).write(i+1, 15, b["acmid"])
            w.get_sheet(0).write(i+1, 16, b["publisher"])
            w.get_sheet(0).write(i+1, 17, b["address"])
        except(KeyError):
            print("Error at this ID : "+lines[i])
            continue
    w.save('Updated_DL_Magazine_URLs_Padding0.xls')
    time.sleep(4)
