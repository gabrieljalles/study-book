"""
expressões lambda são funções anônimas
"""
a = lambda x,y: x* y
print(a(2,2))

print('==========usabilidade=======')
lista = [
    ['P1',13],
    ['P2',6],
    ['P3',7],
    ['P4',50],
    ['P5',8],
]
#para ordenar essa lista pelo preço do indice 1 de cada item

lista.sort(key=lambda item: item[1], reverse=True)  # o reverse true faz a ordem ficar decrescente
print(lista)

#outra forma de ordenar seria pelo sorted, nele você não modifica a lista, cria uma cópia dela
print(sorted(lista, key=lambda i:i[1]))

