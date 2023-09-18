import PyPDF2

file = open('Resultado Pratica.PDF', 'rb')

reader = PyPDF2.PdfReader(file)

list = reader.pages[0].extract_text().split('/') 

list[0] = list[0].split(',')

# list[0] = list.split('\n')

print(list[0])

file.close()
