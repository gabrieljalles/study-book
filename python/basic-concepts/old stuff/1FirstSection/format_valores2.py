"""
manipulação de strings
"""
#indice positivos  012345678
texto           = 'python s2'
#indice negativo -[987654321]

print(texto[5])  #resposta : n
print(texto[6])  #resposta :     não é visivel pq  o indice 6 corresponde  a espaço.

nova_string = texto[2:6]  #caso eu queira pegar de tanto até tanto , ele é inclusivo no 2 e exclusivo no 6, ou seja,
                          #não pega o espaço, mas pega o THON;
print(nova_string) #resposta : thon

#usando os indices negativos

nova_string2 = texto[-9:-4]
print(nova_string2) #resposta : pytho
# o indice negativo é bom para incluir ou excluir o ultimo caractere do  indice.

#https://docs.python.org/3/library/functions.html
#https://docs.python.org/3/library/stdtypes.html





