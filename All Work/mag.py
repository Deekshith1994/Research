from urllib.request import Request, urlopen
from xlutils.copy import copy
from xlrd import open_workbook
from pybtex.database.input import bibtex
import time

w = copy(open_workbook('DL_Proceedings.xls'))
for i in range(0,10): w.get_sheet(0).write(0,i,"")

file = open('ids.txt')
lines = file.readlines()
parser = bibtex.Parser()

for i in range(8686, len(lines)):
    address = 'http://dl.acm.org/exportformats.cfm?id='+lines[i].strip()+'&expformat=bibtex'
    req = Request(address, headers={'User-Agent': 'Mozilla'})
    htmlfile = urlopen(req)
    htmltext = htmlfile.read()
    bibdata = parser.parse_bytes(htmltext)
    for bib_id in bibdata.entries:
        b = bibdata.entries[bib_id].fields
        try : w.get_sheet(0).write(i+1,0,lines[i])
        except(KeyError): continue
        try : w.get_sheet(0).write(i+1, 1, htmltext.decode())
        except(KeyError):
            print("Error at this ID : " + str(i) + ":" + lines[i])
            w.get_sheet(0).write(i + 1, 1, "Not Found")
            continue
        try : w.get_sheet(0).write(i+1, 2, b["author"])
        except(KeyError):w.get_sheet(0).write(i+1, 2, "Not Found")
        try: w.get_sheet(0).write(i+1, 3, b["title"])
        except(KeyError): w.get_sheet(0).write(i+1, 3, "Not Found")
        try: w.get_sheet(0).write(i+1, 4, b["journal"])
        except(KeyError):w.get_sheet(0).write(i+1, 4, "Not Found")
        try: w.get_sheet(0).write(i+1, 5, b["issue_date"])
        except(KeyError):w.get_sheet(0).write(i+1, 5, "Not Found")
        try: w.get_sheet(0).write(i+1, 6, b["volume"])
        except(KeyError):w.get_sheet(0).write(i+1, 6, "Not Found")
        try: w.get_sheet(0).write(i+1, 7, b["number"])
        except(KeyError):w.get_sheet(0).write(i+1, 7, "Not Found")
        try: w.get_sheet(0).write(i+1, 8, b["month"])
        except(KeyError):w.get_sheet(0).write(i+1, 8, "Not Found")
        try: w.get_sheet(0).write(i+1, 9, b["year"])
        except(KeyError):w.get_sheet(0).write(i+1, 9, "Not Found")
        try: w.get_sheet(0).write(i+1, 10, b["issn"])
        except(KeyError):w.get_sheet(0).write(i+1, 10, "Not Found")
        try: w.get_sheet(0).write(i+1, 11, b["pages"])
        except(KeyError):w.get_sheet(0).write(i+1, 11, "Not Found")
        try: w.get_sheet(0).write(i+1, 12, b["numpages"])
        except(KeyError):w.get_sheet(0).write(i+1, 12, "Not Found")
        try: w.get_sheet(0).write(i+1, 13, b["url"])
        except(KeyError):w.get_sheet(0).write(i+1, 13, "Not Found")
        try: w.get_sheet(0).write(i+1, 14, b["doi"])
        except(KeyError):w.get_sheet(0).write(i+1, 14, "Not Found")
        try: w.get_sheet(0).write(i+1, 15, b["acmid"])
        except(KeyError):w.get_sheet(0).write(i+1, 15, "Not Found")
        try: w.get_sheet(0).write(i+1, 16, b["publisher"])
        except(KeyError):w.get_sheet(0).write(i+1, 16, "Not Found")
        try: w.get_sheet(0).write(i+1, 17, b["address"])
        except(KeyError):w.get_sheet(0).write(i+1, 17, "Not Found")
    w.save('DL_Proceedings.xls')
    time.sleep(3)
