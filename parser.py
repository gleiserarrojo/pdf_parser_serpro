import PyPDF2

file = open('Resultado Pratica.PDF', 'rb')

reader = PyPDF2.PdfReader(file)

list = reader.pages[0].extract_text().split('/') 

list[0] = list[0].split(',')

# print(list[0])

print(list[0][-3].split('\n'))


file.close()
