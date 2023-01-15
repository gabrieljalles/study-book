# existe um erro que a funcao sobrescreve as variaveis criadas ('clientes')
#para consertar é necessário usar o lista = None no parametro e colocar um if para que se estiver vazio crie a lista

def lista_de_clientes(clientes_iteravel,lista=None):
    if lista is None: # sea lista estiver vazia, crie uma nova
        lista = []
    lista.extend(clientes_iteravel)
    return lista


lista_de_clientes_1 = ['fabricio']
clientes1 = lista_de_clientes(['joao','maria','eduardo'])
clientes2 = lista_de_clientes(['Marcos','jarbas'])

print(clientes1)
print(clientes2)
print(lista_de_clientes_1)
