"""
listas em PYTHON
fatiamento
append, insert, pop ,del, clear, extend
min, max
range
"""

# indice          0   1   2         3          4     5
lista =         ['A','B','C','dadodolabela','10.5','E']
#indice negativo -6   5   4         3          2    1
# uma lista suporta vários valores e valores de tipos diferentes

#apesar desse tipo de modificação não ser tão usual,
#pode reatribuir esse valor pra cada indice:
lista[5] = "qualquer outra coisa"  # O "E" passou a ser !qualquer outra coisa!

print(lista)

print(lista[-5]) #resposta = B

# se eu quero imprimir os 3 primeiros elementos da minha lista :
print(lista[0:3]) # Resposta = ['A', 'B', 'C']  # o número que para não é incluído, não esqueça;

# Caso eu queira mostrar  pulando informações da minha lista
print(lista[::2]) #resposta = ['A', 'C', '10.5'] omito o início, o fim, então digo que é até acabar e depois falo para pular de 2 em dois

# Caso eu queira inverter a ordem  da minha lista
print(lista[::-1]) #resposta = ['qualquer outra coisa', '10.5', 'dadodolabela', 'C', 'B', 'A']

