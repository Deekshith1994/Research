import random
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from xlutils.copy import copy
from xlrd import open_workbook
import time
import PyPDF2
from firebase import firebase



def RandomUserAgents():
    uas = ["Mozilla"]
    return random.choice(uas)

ua = RandomUserAgents()

# proxy = {"http": "http://username:p3ssw0rd@10.10.1.10:3128"}

headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

w = copy(open_workbook('DL_Magazine_URLs_Padding0.xls'))

file = open('ids.txt')
lines = file.readlines()

for i in range(0,len(lines)):
    if(lines[i].strip()!= ""):
        print(lines[i].strip());
        try:
            # time.sleep(4)
            # req = Request('http://dl.acm.org/citation.cfm?id=' + lines[i].strip(), headers=headers)#1965725
            # htmlfile = urlopen(req)
            # soup = BeautifulSoup(htmlfile, "html.parser")
            # temp = soup.find('a', {"name": "FullTextPDF"})['href']
            # address = 'http://dl.acm.org/' + temp
            # print(address)
            address = "http://delivery.acm.org/10.1145/1970000/1965725/p5-vardi.pdf?ip=152.15.236.134&id=1965725&acc=OPEN&key=A79D83B43E50B5B8%2E48786266F2419CCD%2E4D4702B0C3E38B35%2E7BDEF374746A56FB&CFID=745020279&CFTOKEN=36770104&__acm__=1490888820_cda4f94c6173722e0411de005b5bf9a7"
            time.sleep(4)
            req = Request(address, headers={'User-Agent': 'chrome'})
            response = urlopen(req)
            file = open("document.pdf", 'wb')
            file.write(response.read())
            file.close()

            pdf_file = open("document.pdf", 'rb')
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            page_content = ""
            for pg in read_pdf.pages:
                page_content += pg.extractText()

            page_content = page_content.replace("\n","")
            # firebaseR = firebase.FirebaseApplication('https://pique-fa32e.firebaseio.com/')
            # result = firebaseR.put('/ResearchPapers_fullText', lines[i].strip(), page_content)
            print(page_content)
        except:
            # address = "http://delivery.acm.org/10.1145/1970000/1965725/p5-vardi.pdf?ip=152.15.236.134&id=1965725&acc=OPEN&key=A79D83B43E50B5B8%2E48786266F2419CCD%2E4D4702B0C3E38B35%2E7BDEF374746A56FB&CFID=745020279&CFTOKEN=36770104&__acm__=1490888820_cda4f94c6173722e0411de005b5bf9a7"
            # time.sleep(4)
            # req = Request(address, headers={'User-Agent': 'chrome'})
            # response = urlopen(req)
            print("Problem with ID :"+lines[i].strip())
    else :
        print(lines[i]);