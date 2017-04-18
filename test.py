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

headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}

file = open('ids.txt')
lines = file.readlines()

for i in range(len(lines)-1,0, -1):
    if(lines[i].strip()!= ""):

        print(lines[i]);
        try:
            time.sleep(4)
            url = 'http://dl.acm.org/citation.cfm?id=' + str(lines[i]).strip()
            print(url)
            req = Request(url, headers=headers)
            htmlfile = urlopen(req)
            soup = BeautifulSoup(htmlfile, "html.parser")
            temp = soup.find('a', {"name": "FullTextPDF"})['href']
            address = 'http://dl.acm.org/' + temp
            print(address)

            time.sleep(4)
            req = Request(address, headers={'User-Agent': 'chrome'})
            response = urlopen(req)
            text = response.read()
            file = open("document.pdf", 'wb')
            file.write(text)
            file.close()
            s = str(lines[i]).strip()+".pdf"
            file1 = open("pdfs/"+s, 'wb')
            file1.write(text)
            file1.close()

            pdf_file = open("document.pdf", 'rb')
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            page_content = ""
            for pg in read_pdf.pages:
                page_content += pg.extractText()

            page_content = page_content.replace("\n","")
            firebaseR = firebase.FirebaseApplication('https://pique-fa32e.firebaseio.com/')
            result = firebaseR.put('/ResearchPapers_FullText', lines[i].strip(), page_content)
            print(page_content)
            with open("Output.txt", "a") as text_file:
                text_file.write("Executed: %s\t" % lines[i].strip())
                text_file.write("i: %s\n" % i)
        except Exception as e:
            print("Problem with ID : "+str(lines[i]) +": "+ str(e))
            print(str(e))
            with open("Errors.txt", "a") as text_file:
                text_file.write("Error: %s" % str(lines[i]))
                text_file.write("i: %s\n" % i)
                text_file.write("Exception: %s\n" % str(e))

    else :
        print(lines[i]);

file.close();