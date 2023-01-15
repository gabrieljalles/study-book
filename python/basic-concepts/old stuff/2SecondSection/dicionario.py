"""
diferença entre listas e dicionários
nas listas o python gera um indice automatico pra você
------
Dicionário você controla o indice ou chave - estrutura de dados que suporta chave e um valor
chaves dentro do dicionário precisam ter valores únicos, o último valor atribuido a uma chave será o verdadeiro

"""
d1 = {'chave1':'valor da chave'}  # DUAS FORMAS DE CRIAR DICIONÁRIO
d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave') # DUAS FORMAS DE CRIAR DICIONÁRIO
print(d1)
print(d2)

d1['nova_chave'] = 'Valor da nova chave' #MANEIRA DE ADICIONAR ou ATUALIZAR

#possibilidades na criação da dicionário

d3 = {
    'str':'valor',
    123: 'outrovalor',
    (1,2,3,4): 'Tupla',
}
print(d3)
d3.update({'nova_chave':'novo_valor'})  #MANEIRA DE ADICIONAR ou ATUALIZAR
print(d3)

  #PARA APAGAR UMA CHAVE E SEU VALOR
del d3['str']
print(d3)

  #como conferir se um valor ou uma chave está dentro de um DICIONÁRIO
print('str' in d3)
print('str' in d3.keys()) # checando a chave
print('valor' in d3.values()) #checando o valor

print(len(d3)) # o len em dicionário mostra quantos PARES  tem dentro do dicionário

d4 ={
    'chave1' : 'valor reginaldo',
    'chave2' : 'Outro valor',
    'chave3' : 'Tupla',
}

for v in d4.values(): # estou acessando os valores do dicionário
    print(v)

for v in d4: # estou acessando apenas as chaves
    print(v)

for k,v in d4.items(): # estou acessando os dois ao mesmo tempo
    print(k,v)
print("=====================================================================")
clientes = {
    'usuario354':{
        'nome' : 'joao',
        'sobrenome' : 'Moreira',
    },
    'usuario154':{
        'nome' : 'Fernando',
        'sobrenome' : 'Azedo',
    },
}


for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}') # a utilização da \t identa os codigos



