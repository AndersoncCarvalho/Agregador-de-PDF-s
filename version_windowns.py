import PyPDF2
import os


#cria objeto PFM[PdfFileMerger]
merger = PyPDF2.PdfMerger()

#busca dentro da pasta
  pasta = r"[diretório/pasta dos pdf's]"
arquivos = os.listdir(pasta)

#adiciona arquivos PDF ao objeto PFM
for arquivo in arquivos:
    #verifica se o arquivo é um PDF
    if arquivo.endswith(".pdf"):
        #adiciona o arquivo ao objeto PFM
        merger.append(os.path.join(pasta, arquivo))

#salva documento PDF unidicado
      merger.write("[nome do pdf]")
