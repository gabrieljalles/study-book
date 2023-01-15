string = '012345678901234567890123456789012345678901234567890123456789'
m = 10
print(string[0:10])
print(string[10:20])

lista = [string[i:i+m] for i in range(0,len(string),m)]
test = [i for i in range(0,len(string),m)]
rang = [(i,i+m) for i in range(0,len(string),m)]

print(test) # mostrando que o range vai de 10 em 10
print(rang) # mostrando na forma de tupla o que é pro comportamento funcionar
print(lista) # uma lista que separa de tanto até tanto

separa_ponto = ".".join(lista)
print(separa_ponto)