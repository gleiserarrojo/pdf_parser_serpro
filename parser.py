import PyPDF2

# abre o pdf para ler
file = open('Resultado Pratica.PDF', 'rb')

# cria o leitor do pdf
reader = PyPDF2.PdfReader(file)

# extrai o texto da primeira página e divide os nomes
names = reader.pages[0].extract_text().split('/') 

# fecha o arquivo
file.close()

# remove todo o texto antes do primeiro nome e salva só as infos do candidato
names[0] = names[0].split(',')
aux = names[0][-3].split('\n')
names[0] = str(aux[-1] + ',' + names[0][-2] + ',' + names[0][-1])

# remove espacos e quebras de linhas (FIX)
for x in range(len(names)):
    names[x] = names[x].replace(" ", "").replace("\n", "")
    print(names[x])
