#para saber se um  objeto é iteravel print(hasattr(objeto,'__iter__'))
lista = [0,1,2,3,4,5]
print(hasattr(lista,'__iter__'))
#para saber se um objeto é um iterador print(hasattr(lista,'__next__')) # TODO ITERADOR É UM ITERAVEL, MAS NEM TODO ITERAVEL ....
print(hasattr(lista,'__next__'))

#você pode  passar um objeto assim objeto  =  iter(objeto)
lista = iter(lista)
print(hasattr(lista,'__next__'))

# se é um objeto iteravel, posso usar o for para exibir os objetos separadamente, com o for ele transforma essa lista em
#um iterador. uma lista não é ITERADOR

import sys #usado para saber o tamanho usado para armazenar no computador
lista = list(range(10))
print(lista)
print(sys.getsizeof(lista))

import time #usado para colocar tempo entre execução de códigos

# def gera():
#     r = []
#     for n in range(100):
#         r.append(n)
#         time.sleep(0.1)
#         return r
#
# g = gera()
#
# for v in g:
#     print(v)

l1 = [x for x in range(1000)] # troque de couchetes por parenteses
g1 = (x for x in range(1000))

#veja que, apesar de ser igual, a lista chama todos os valores ao mesmo tempo, enquanto o gerador não. o gerador espera seu comando.
print(sys.getsizeof(l1))
print(sys.getsizeof(g1))

#para pedir um novo valor no gerador
print(next(g1))
print(next(g1))
print(next(g1))
print(next(g1))

