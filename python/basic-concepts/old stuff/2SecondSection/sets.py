"""
a maior diferença entre os sets e as listas é que os sets só suportam elementos ÚNICOS

um set é criado por chaves , cuidado para não confundir com dicionário, observe o padrão :
set não possuem par de chaves e valores, eles possuem apenas valores

fique atento criar um {} vazio, ele não é set, mas sim dicionario
para criar um set em branco s1=set()

sets não respeitam ordem
sets não aceitam elementos duplicados. usados para eliminar elementos duplicados de uma lista
"""
s1 =set()
s1.add('python') #adiciona toda a palavra de uma vez 'python'
s1.update('python') # adiciona tambem, ela recebe um iteravel e itera sobre esse elemento 'p' 'y' 't' ... não tem ordem

print(s1)

#CONVERTENDO PARA SET UMA LISTA
l1 = [1,2,3,4,5,6,6,6,6]
l1 = set(l1) #eliminando a repetição
l1 = list(l1)
print(l1)

s2  = {1,2,3,6,587}
s4 = {1,2,3,6,7,8,9,10}
s3 = s2 & s4  # intersecção {1, 2, 3, 6}
print(s3)
s5 = s2 | s4  #uniao {1, 2, 3, 6, 7, 8, 9, 10,587}
print(s5)
s6 = s2 ^ s4  #os únicos valores que estão em cada um mas não estão no outro {7, 8, 9, 10, 587}
print(s6)
