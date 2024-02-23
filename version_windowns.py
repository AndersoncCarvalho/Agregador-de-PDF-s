import PyPDF2
import os

# Cria a lista com os nomes dos arquivos PDF na ordem desejada
arquivos_ordenados = ["Adicione aqui a ordem dos arquvios desejados"]

#cria objeto PFM[PdfFileMerger]
merger = PyPDF2.PdfMerger()

#busca dentro da pasta
pasta = r"C:\User\...(coloque o caminho da pasta aqui)"
arquivos = os.listdir(pasta)

#adiciona arquivos PDF ao objeto PFM
for arquivo in arquivos_ordenados:
    #verifica se o arquivo é um PDF
    if arquivo.endswith(".pdf"):
        #adiciona o arquivo ao objeto PFM
        merger.append(os.path.join(pasta, arquivo))

#salva documento PDF unidicado
merger.write('Escreva o nome final do novo PDF unificado aqui')




