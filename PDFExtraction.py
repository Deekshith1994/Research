import PyPDF2
pdffileObj = open('test.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdffileObj)
print(pdfReader.numPages)
print('1')
