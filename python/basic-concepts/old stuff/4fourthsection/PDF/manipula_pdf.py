"""
Documentação do modulo:
    https://pythonhosted.org/PyPDF2/
Blog que mostra exemplos do pdf2:
    https://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/
"""
import PyPDF2
import os

# -----------------------Aprendendo a juntar PDFS----------------------------------------------
# caminho_pdf = r'C:\Users\Gabriel\Desktop\pythonudemy\udemypython\4fourthsection\PDF\pdf'
#
# novo_pdf = PyPDF2.PdfFileMerger() #junta varios pdf em um só
# # alencando os arquivos que estão presente na pasta
# for root, dirs, files in os.walk(caminho_pdf):
#     for file in files:
#        caminho_completo_pdf = os.path.join(root, file) #root = pasta # file = arquivo, junta os dois
#
#        arquivo_pdf = open(caminho_completo_pdf,'rb') # rb = read binary
#        novo_pdf.append(arquivo_pdf)
#
# if not os.path.exists('novo_arquivo.pdf'):
#     with open(f'{caminho_pdf}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
#         novo_pdf.write(meu_novo_pdf)


# -------------------------SEPARANDO PDFS--------------------------------------------------------
# separando em dois arquivos
# pegando o pdf novo_arquivo e colocando em uma nova pasta (novo_pdf_separado)

with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()  # vendo quantas paginas o pdf tem
    for num_pagina in range(num_paginas):  # em pdf a pagina 1 é a 0 como indice
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novo_pdf_separado/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
