import random
from algoritmos_de_busca import executa_busca_linear

lista = random.sample(range(1000), 50)
print(sorted(lista))

executa_busca_linear(lista, 20)
