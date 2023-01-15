l1 = [1,2,3,4,5,6,7,8,9]
ex1 = [valor for valor in l1]
print(ex1)

ex2 = [v * 2 for v in l1] # agora se imprimimos esse exemplo, cada elemento da lista 1 foi multiplicado por 2
print(ex2)

ex3 = [(v,v2) for v in l1 for v2 in range(3)] #para cada valor in l1 vou pegar um valor de range 3 e colocar junto
print(ex3)

l2 = ['luiz','gabriel','brenda']
ex4 = [v.replace('a','@').upper() for v in l2] #estou pedindo para que o reescreva a  e coloque @,deixe tudo maiuscula para cada valor in l2

tupla = (
    ('chave1','valor'),
    ('chave2','valor1'),
)
ex5 = [(y,x) for x,y in tupla] # inverti as tuplas chave por valor
print(ex5)

l3 = list (range(100))
ex6 = [v for v in l3 if v % 2 ==0 if v % 8 == 0]# quero todos os valores que são divisiveis por 2 na lista l3
print(ex6)




































































































