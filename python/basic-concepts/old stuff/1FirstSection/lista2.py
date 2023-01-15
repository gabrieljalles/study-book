"""
listas em PYTHON
fatiamento
append, insert, pop ,del, clear, extend
min, max
range
"""

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

print(l1)
print(l2)
print(l3)

#usando extend
#pegue uma lista que já existe
l1.extend(l2)
print(l1) #resposta = [1, 2, 3, 4, 5, 6] outra forma de somar duas listas

#posso também adicionar apenas um valor qualquer
l1.extend('a')
print(l1) #resposta = [1, 2, 3, 4, 5, 6, 'a']  não esqueça que os comandos anteriores já juntaram as 2 listas  e esse comando acrescentou o "a"

#append()
#quando vamos adicionar uma um valor, normalmente usamos append()
# pra não bagunçar tanto, vou criar outra lista
l5 = [1,2,3]
l5.append('asdads')
print(l5)  #resposta = [1, 2, 3, 'asdads']
print("==========================")
#acessando o indice novo , o 3
print(l5[3]) #resposta = asdads

#insert
#podemos usar o insert para acrescentar um valor e forçar ele a ficar em qualquer indice que desejamos.
l5.insert(0,'banana')
print(l5) # nesse caso, eu pedi para que banana ficasse no indice 0 #resposta = ['banana', 1, 2, 3, 'asdads'], ele move os demais pra frente

#pop()
#a utilização do pop, ele tira o último elemento da lista , como o último era asdasa
l5.pop() #resposta = ['banana', 1, 2, 3]
print(l5)


#del
del(l5[0])   # estou pedindo para retirar do indice 0 o elemento  da lista l5
print(l5) #resposta = [1,2,3]

#max min
#quando eu quero saber o maior valor e o menor valor da minha lista
print(max(l5)) #resposta = 3
print(min(l5)) # resposta = 1

"""
a diferença entre extend e append é :
x = [1,2,3]
x.append([4,5])
print (x) [1,2,3[4,5]]
==================
x = [1,2,3]
x.extend([4,5]) 
print (x) [1,2,3,4,5]
O extend adiciona os elementos do iterável, o append o iterável inteiro

"""

