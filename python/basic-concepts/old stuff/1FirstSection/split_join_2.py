string = "O brasil é penta"
lista = string.split(" ") #split me permite separar usando um argumento (" "), nesse caso, o espaço. Cada vez que tem o espaço, ele separa
print(lista)
#resp: ['O', 'brasil', 'é', 'penta']
#agora eu quero juntar todos os elementos da lista usando o caractere ','. veja abaixo:
string2= ','.join(lista)  # o join junta a lista em string
print(string2) #resp: O,brasil,é,penta

print("================================================")

# for v1,v2 in enumerate(lista):  # esse v1 e v2  está desempacotando a lista
                                  # esse enumerate enumera a lista/ retorna tuplas

for indice, valor in enumerate(lista):
    print(indice,valor,lista[indice])  #observe que o valor é igual a lista[indice], O desempacotamento é uma forma de agilizar
#================================================================
#uma lista pode conter outras listas

listanova = [
    [1,2],
    [3,4],
    [5,6],
]
for v in listanova:
    # print(v[0]) # estou pedidondo para mostrar o indice 0 de cada valor da listanova RESP: 1 3 5
    print(v[0],v[1])  #estou pedindo para mostrar o indice 0 e 1. resp: 12   34   56

print('=====================================================================================')
lista= [
    [0,'luiz'], #a função enumerate faz a mesma coisa que eu fiz aqui ele enumera cada valor
    [1,'joao'],
    [2,'maria'], #observe a lista de baixo com essa, veja que a enumerate acrescenta os indices sem ter eles.
]
for indice,nome in lista:
    print(indice, nome)
print("========= veja que são iguais===========")
lista= ['luiz','joao','maria',]

for indice,nome in enumerate(lista):
    print(indice,nome)

lista = ['luiz', 'joao', 'maria']

#veja outro exemplo:
n1,n2,n3 = lista

print(n2) #joao
