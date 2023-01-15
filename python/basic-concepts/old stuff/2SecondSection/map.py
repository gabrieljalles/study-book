from dados import produtos, pessoas, lista

#suponha que eu queira multiplicar todos os valores da lista por 2
nova_lista = map(lambda x:2*x, lista)
#a funcao map não retorna uma lista pronta, ela retorna um iterador
# se você entendeu list comprenhions, não usará tanto map , pode encontra-la em outros códigos
nova_lista2 = [x*2 for x in lista]
print(lista)
print(list(nova_lista))
print(list(nova_lista2))

precos = map(lambda p:p['preco'], produtos) #estou acessando o dicionario produtos e pegando somente os precos
print(list(precos))

def aumenta_preco(p): # o objetivo era aumentar 5% de cada valor do dicionario
    p['preco'] = round(p['preco'] * 1.05,2)
    return p

novo_precos = map(aumenta_preco,produtos) # a funcao map no primeiro parametro aceita uma funcao (pode ser anonima'lambda) ou normal como aumenta_preco

for produto in novo_precos:
    print(produto)