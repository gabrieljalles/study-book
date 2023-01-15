# outra forma de criar uma lista de maneira mais automatica
"""
poderiamos usar a função range para criar de maneira mais rápida uma lista de 100 elementos, mas ele não retorna uma lista
e sim  um objeto.
"""
l2 = range(1,10)
print(l2) #resposta = range(1, 10)

#para arrumar isso, existe um comando chamado list para transformar todos os objetos em listas. observe.
l2 = list(range(1,10))
print(l2) #resposta = [1, 2, 3, 4, 5, 6, 7, 8, 9]



