
#arquivos .py que podemos  importar para ajudar na programacao
#veja todos os modulos padrao do python em:
#https://docs.python.org/3/py-modindex.html

from sys import platform as apelido_para_reduzir  # esse as " ", na verdade estou renomeando o import
print(apelido_para_reduzir)

#se eu quero importar o modulo inteiro
import random

for i in range(100):
    print(random.randint(0,10)) #é inclusivo para randint observe que tenho que usar o random."....."
#quando eu importo o modulo inteiro, preciso colocar o random."....."
# se eu tivesse importado from random import randint, só precisaria colcoar o randint()



