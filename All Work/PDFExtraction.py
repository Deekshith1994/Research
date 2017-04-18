import PyPDF2
from firebase import firebase
from urllib.request import Request, urlopen
from xlutils.copy import copy
from xlrd import open_workbook
import time

# w = open_workbook('DL_Magazines.xls')
# w.sheet_names()
# sheet = w.sheet_by_index(0)

for i in range(2,5000):
    # address = 'http://' + sheet.cell(i, 19).value
    # id = sheet.cell(i, 2).value
    address = 'http://dl.acm.org/ft_gateway.cfm?id=2980762&ftid=1782564&dwn=1&CFID=736847395&CFTOKEN=16783311'
    print(address)
    req = Request(address, headers={'User-Agent': 'chrome'})
    response = urlopen(req)
    file = open("document.pdf", 'wb')
    file.write(response.read())
    file.close()



    pdf_file = open("document.pdf", 'rb')
    read_pdf = PyPDF2.PdfFileReader(pdf_file)
    page_content = ""
    for pg in read_pdf.pages :
        page_content += pg.extractText()


    print(page_content)

    firebaseR = firebase.FirebaseApplication('https://pique-fa32e.firebaseio.com/')
    result = firebaseR.put('/ResearchPapers_fullText', i, page_content)
    print(result)
    result = firebaseR.get('/ResearchPapers_fullText', None)
    print(result)
    time.sleep(4)


 # w.get_sheet(0).write((int)(i + 1), 20, soup.find('div', {"id": "references"}).text)
            # print("dl.acm.org/"+soup.find('a', {"name": "FullTextPDF"})['href'])
            # w.save('DL_Magazine_URLs_Padding0.xls')

