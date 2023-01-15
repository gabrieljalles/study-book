# um algoritmo de busca linear percorre por todos os dados de um objeto
# muito custoso computacionalmente.
#todas as posições são inventadas até que se encontre um elemento buscado
def executa_busca_linear(lista, valor):
    for elemento in lista:
        if valor == elemento:
            return print(True)
    print(False)



