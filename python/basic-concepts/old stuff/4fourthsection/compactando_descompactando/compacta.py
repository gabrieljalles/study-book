from zipfile import ZipFile
import os

#ESCREVENDO E COMPACTANDO .....
caminho =r'C:\Users\Gabriel\Desktop\pythonudemy\udemypython\4fourthsection\compactando_descompactando'
with ZipFile('arquivo.zip', 'w') as zip:
       for arquivo in os.listdir(caminho):
              caminho_completo = os.path.join(caminho, arquivo)
              zip.write(caminho_completo, arquivo) #o primeiro é o  caminho completo e o segundo é como eu quero salvar ele, apenas nomes

#LENDO
with ZipFile('arquivo.zip', 'r') as zip:
       for arquivo in zip.namelist():
              print(arquivo)

#EXTRAINDO TUDO ....
with ZipFile('arquivo.zip', 'r') as zip:
       zip.extractall('descompactado') #extraindo para a pasta descompactado