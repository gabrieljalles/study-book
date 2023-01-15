# a partir da posição 0, ele procura quem é o menor da lista e troca para ficar na posição 0
# a partir da posição 1, ele procura quem é o menor da lista e troca para ficar na posição 1
# a partir da posição 2, ele procura quem é o menor da lista e troca para ficar na posição 2
#...
#esse tipo de organização é muito lento para listas grandes
#ponto positivo, ele é intuitivo

def selection_sort(lista, valor):
    n = len(lista)

    for i in range(0, n):
        index_menor = i
        for j in range(i+1, n):
            if lista[j] < lista [index_menor]:
                index_menor = j
        lista[i], lista[index_menor] = lista[index_menor], lista[i]
    return lista


