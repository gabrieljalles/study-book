"""
Combinations - ordem não importa
permutacao - ordem importa
Ambos não repetem valores únicos
Produto - ordem importa e repete valores únicos
"""

from itertools import combinations, permutations, product

pessoas = ['luiz','Andre','Eduardo','Leticia','Fabricio','Rose']
total = 0
for grupo in combinations(pessoas,3): # eu quero combinações, que não importa a ordem, de 3 pessoas
    print(grupo) # luiz andre eduardo é a mesma coisa que andre luiz eduardo....
    total += 1
print(total)
total = 0

print(f'{"permutations":=^49}')
for grupo in permutations(pessoas,2): # eu quero permutações, que a ordem importa de 2 pessoas
    print(grupo)
    total+=1
print(total)


"""
vamos dizer que eu queira mais detalhado ainda, no caso da permutacao (luiz,luiz) não irá me mostrar.
preciso então do product que me mostra todas as combinacoes possíveis
"""

print(f'{"product":=^49}')
for grupo in product(pessoas, repeat=2):  # eu quero o produto, que a ordem importa de 2 pessoas e valores iguais podem ocupar indices diferentes na mesma junção
    print(grupo)
    total+=1
print(total)
