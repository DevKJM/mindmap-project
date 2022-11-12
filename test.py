import PyPDF2 as pdf


filename = r'C:\Users\K\Desktop\test_3.pdf'
Report = open(filename, 'rb') 
pdfReader = pdf.PdfFileReader(Report)
pageObj = pdfReader.getPage(0)
txt = pageObj.extractText()

object = pdfReader.get_object()
print(object)
decoded_data = pageObj.decode('utf-8')
print(decoded_data)

#replaced_data = replace_text(decoded_data, {"아메":"리카"})

#encoded_data = replaced_data.encode('utf-8')