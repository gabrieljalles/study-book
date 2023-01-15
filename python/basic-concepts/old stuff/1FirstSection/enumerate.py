lista = ['edu','joao','luiz'] # uma lista é um conjunto de elementos

lista =[
       #0     #1     #2
    ['Edu','Joao','Luiz'],       #0
    ['Maria','Aline','Joana'],   #1
    ['Helena','Ed','lu']         #2
]

print(lista[2]) #resp: ['Helena', 'Ed', 'lu']
print(lista[1][2]) #resp: joana

#enumerada = enumerate(lista)
#print(enumerada)  # o objeto foi feito para você iterar sobre ele  resp: <enumerate object at 0x000001AB86AFAC80> e o local da memória

# como enumerada vem no tipo objeto iteravel com memória alocada, precisamos converter para lista
#print(list(enumerada))
""" 
veja que cada elemento da lista possui um indice, graças ao enumerate:
[(0, ['Edu', 'Joao', 'Luiz']), (1, ['Maria', 'Aline', 'Joana']), (2, ['Helena', 'Ed', 'lu'])]
Observe que uma lista comum é possível mudar ou adicionar valores, nesse caso, veja que tem (), ou seja uma tupla
ele não pode ser alterado ou adicionado.
"""
#com o objetivo de deixar mais dinâmico
enumerada = list(enumerate((lista)))
print(enumerada)
"""
<-------------- Enumerate
[    #0          #1
    (0, ['Edu', 'Joao', 'Luiz']),
    (1, ['Maria', 'Aline', 'Joana']), 
    (2, ['Helena', 'Ed', 'lu'])
]
"""
print(enumerada[1][0]) #resp = 1 /no indice um temos os elementos (1, ['Maria', 'Aline', 'Joana']) e o indice zero dentro desse elemento é : 1

print(enumerada[1][1]) #resp = 'Maria', 'Aline', 'Joana'

print(enumerada[1][1][1])





