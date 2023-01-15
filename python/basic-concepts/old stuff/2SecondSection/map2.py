from dados import produtos, pessoas, lista

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.8)
    return p

nomes = map(aumenta_idade,pessoas)
for pessoa in nomes:
    print(pessoa)



# nomes = map(lambda p: p['idade'] * 1.2,pessoas)
# for pessoa in nomes:
#     print(pessoa)


