from itertools import groupby
# é muito importante que você reordene os  dados antes de usar groupby
alunos  = [
    {'nome' :'luiz', 'Nota':'A'},
    {'nome' :'Letícia', 'Nota':'B'},
    {'nome' :'Fabricio', 'Nota':'C'},
    {'nome' :'Rosemary', 'Nota':'D'},
    {'nome' :'Rebeca', 'Nota':'E'},
    {'nome' :'Bartolomeu', 'Nota':'A'},
    {'nome' :'Andre', 'Nota':'A'},
    {'nome' :'Anderson', 'Nota':'B'},
    {'nome' :'Fernando', 'Nota':'C'},
    {'nome' :'Jose', 'Nota':'B'},
]

"""
A função groupby precisa que o dicionário esteja ordenado
"""

# alunos.sort(key=lambda item: item['Nota'])
# alunos_agrupados = groupby(alunos, lambda item: item['Nota'])
"""
como o código está repedito, podemos isolar a repetição veja :
"""
ordena = lambda item:item['Nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos,ordena)

# for agrupados in alunos_agrupados:
#     print(agrupados)
#resp :
# ('A', <itertools._grouper object at 0x000002859AEFEAF0>)
# ('B', <itertools._grouper object at 0x000002859AEFEAC0>)
# ('C', <itertools._grouper object at 0x000002859AEFEAF0>)
# ('D', <itertools._grouper object at 0x000002859AEFEAC0>)
# ('E', <itertools._grouper object at 0x000002859AEFEAF0>)

#para corrigir isso, estou extraindo os valores acrescentando um novo valor no for
for agrupamento, valores_agrupados in alunos_agrupados:
        print(f'Agrupamentos:{agrupamento}')
        quantidade = 0
        for aluno in valores_agrupados:
            print(f'\t {aluno}')
            quantidade += 1
        print(quantidade)
