"""
split - divide uma string #str
join - juntar uma lista #str
Enumerate - Enumerar elementos da lista # list / FEITO para objetos iteraveis,
-------
Até o momento aprendemos que lista e string são iteráveis
"""
#split - pode dividir uma string e criar uma lista dela
string ="O brasil é o país do futubol, o Brasil é penta."
lista_1 = string.split(' ')  #estou criando uma lista por meio da string anterior e separando ela pelo espaço split(" ") , 11 valores
lista_2 = string.split(',')  #estou criando uma lista por meio da string anteior e separando ela por split(" " , 2 valores
print(lista_1)
print(lista_2)

for valor in lista_1:
    print(f'A palavra {valor} apareceu {lista_1.count(valor)}x na frase.')  # estou contando quantas vezes aparece cada valor da lista

print("-------------------------------------------------------------------")
  # CRIANDO UMA lógica para descobrir qual a  palavra que apareceu mais vezes
palavra = ''
contagem = 0
for valor in lista_1:
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'a palavra que apareceu mais vezes foi {palavra} com {contagem}')
