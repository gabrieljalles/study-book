from dados import pessoas,lista, produtos

"""
serve para filtrar coisas
"""
#quero numeros maiores que 5
# funcao filter recebe uma funcao, lambda  = anonima, nesse caso;
# a funcao filter retorna ou verdadeiro ou falso para a expressão que você passar
#se retornar falso ele tira da lista principal, se voltar verdadeiro ele deixa
#filter retorna objeto iteravel


nova_lista = filter(lambda x: x>5,lista)
print(list(nova_lista))

#fazendo pelo list comprehension
nova_lista = [x for x in lista if x>5]
print(nova_lista)

# quero o preco de produto e que ele seja maior que 10

nova_lista = filter(lambda k: k['preco'] > 10, produtos)

for produto in nova_lista:
    print(produto)

print("==================================================")
def filtra(produto):
    if produto['preco'] > 50:
        produto['e_caro'] = True # criando uma nova chave
        return True
# a vantagem de trabalhar com funções é que você pode reutilizar essa função em outro local
# como dito anteroriormente, VOCÊ agora pode substituir lambda pela própria funcao.

nova_lista_3 = filter(filtra,produtos)

for produto in nova_lista_3:
    print(produto)

# outro exemplo com pessoas:

def filtra_pessoa(pessoa):
    if pessoa['idade'] < 18:
        pessoa['menor_idade'] = True
        return True

novo_test  = filter(filtra_pessoa,pessoas)

for pessoa in novo_test:
    print(pessoa)



