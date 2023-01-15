from dados import pessoas,lista,produtos
from functools import reduce
"""
essa funcao é uma acumuladora
"""
# normalmente acumulamos dessa maneira
acumula =  0
for item in lista:
    acumula += item
print(acumula)
#=======================================
# reduce recebe funcao e nesse caso, anonima lambda
# ac é o nome que eu dei ao acumulador
# i é o item
# i + ac a somatoria
# lista é os dados que estou passando
# 0 é o valor inicial
soma_lista =  reduce(lambda ac,i:i + ac, lista, 0)
print(soma_lista)

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos/len(produtos))  #média de precos

soma_idades = reduce(lambda ac, i:i['idade'] +ac , pessoas, 0)
print(f'{soma_idades/len(pessoas):.2f}')


