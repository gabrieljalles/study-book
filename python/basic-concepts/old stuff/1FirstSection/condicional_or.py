nome = input('Qual o seu nome ?')

if nome:
    print(nome)
else:
    print("você não digitou nada")
#================================================
#deixando o código mais rápido
print(nome or 'Você não digitou nada'or 'Outra coisa')  #assim que tiver  uma opção verdadeira, ele para nela.

#============Outro exemplo =====================================
a = 0
b = None
c = False
d = []  #lista vazia = false
e = {}  #dicionário vazio = false
f = 22
g= 'Luiz'

variavel = a or b or c or d or e or f or g
print(variavel) # como o algoritmo achou primeiro o f22 ele para nele, se tivesse alternado a ordem iria fazer diferença
# isso é uma ótima forma de você encurtar vários elif


