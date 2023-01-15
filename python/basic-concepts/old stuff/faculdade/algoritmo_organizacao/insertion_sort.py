#insere novos valores  a lista
# semelhante a pedir uma nova carta no baralho e acrescentar na mão

# a lista possui um único valor, sendo ordenada

# parte do principio de que um valor precisa ser inserido na lista,
# ele é comparado a um valor já existente para saber se precisa ser efetuado
# uma troca de posição e assim por diante.
# ele verifica o valor que vai entrar com os demais da lista

def executar_insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
        valor_inserir = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > valor_inserir:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j+1] = valor_inserir

    return print(lista)

lista = [10,9,5,8,11,-1,3]

executar_insertion_sort(lista)




