"""
count  - itertools
"""

from itertools import count

contador = count(start=0, step=2) # podemos dizer onde queremos que o contador comece, e de que formas ele passa os números
for valor in contador:
    print(round(valor,2)) #quero que ele arredonde com 2 casas
    if valor == 10: # é importante criar uma forma de  parar o contador, caso contrário ele vai ao infinito
        break

