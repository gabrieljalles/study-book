#Escreva de 5 formas diferentes uma frase com as variaveis abaixo.

nome = 'Pe41g'
duracao_filtro = 1
vasao_minuto = 2.000000000000010000

#forma padrao
print(" 1 o filtro eletrolux", nome, "tem a duracao do filtro de",duracao_filtro,"ano e consegue tirar",vasao_minuto,"por minuto")

#forma f'
print(f'2 o filtro eletrolux {nome} tem a duracao do filtro de {duracao_filtro} ano e consegue tirar {vasao_minuto} por minutos')

# forma format
print(' 3o filtro eletrolux{} tem a duracao do filtro de {} ano e consegue tirar {:.2f} por minuto'.format(nome,duracao_filtro,vasao_minuto))

#complementação de format / o numero dentro da chave corresponde a posição lá do final do format, observe:
print(' 4 o filtro eletrolux {0} tem a duracao do filtro de {1} ano e consegue tirar {2:.2f} por minuto'.format(nome,duracao_filtro,vasao_minuto))

#complementacao de format/  pode ser atribuido pequenas variaveis dentro do format.
print(' 5 o filtro eletrolux {n} com o nome de {n} tem duaracao do filtro de {v} ano e consegue tirar {time:.2f}'.format(n=nome,v=duracao_filtro,time=vasao_minuto))
