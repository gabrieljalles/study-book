"""
 a funcao zip junta  dois objetos iteraveis como duas listas por exemplo :
 o zip uni até a menor lista, caso tenha 2  listas  a menor é  até onde  ele unirá
 para corrigir esse problema, usamos o zip_longest. a partir de agora, ele inclui a maior lista mas preenche os valores
 vazios com NONE
 o  count é um gerador, não tem fim, nesse caso, é melhor usar o zip do que o zip_longest quando usar o count
"""
from itertools import zip_longest, count

cidades = ['São Paulo','Belo Horizonte','Salvador','Monte carmelo']
estados = ['SP','MG','BA']

indice = count()
# cidades_estados = zip_longest(cidades, estados) # por padrão é none, mas pode fazer um preencher com : fillvalue
cidades_estados = zip(indice, cidades, estados)

print(cidades_estados) #não consigo ver nada, preciso do for ou a conversao de lista /<zip object at 0x000002EBC7124800>

for indice,estado, cidade in cidades_estados:
    print(indice,cidade,estado)





