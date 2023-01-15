"""
formatando valores com modificadores

:s - Texto
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(numero)f - quantidade de casas decimais (float) :.5f por exemplo
:(CARACTERE) (> ou < ou ^)(quantidade)(tipo -s, d ou f)
> - esquerda
< - direita
^ - centro
"""

num_1 = 1
print(f'{num_1:0>10}')  # nesse caso, eu quero que o valor apresentado tenha  um total de 10 algarismos,
# ele soma 1 da variável com o restante em 0 e que eles ficarão a esquerda > do número. Resposta: 0000000001

num_2 = 512
print(f'{num_2:0<10}') # Resposta : 5120000000

num_3 = 115
print(f'{num_3:0^9}') #Resposta : 000115000

num_4 = 252
print(f'{num_4:.2f}')  #resposta : 252.00

num_5 = 973
print(f'{num_5:0<10.2f}')  #observe que quando eu digo 10 e também coloco o float :.2f ele conta o ponto como digito
  #Resposta : 973.000000

