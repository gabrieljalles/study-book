import random
from functools import reduce

possibilidades = list(range(60, 101))  # Cada colaborador pode trabalhar de 6.0 a 10.0horas

tempo_producao = []


def formata_tempo(n):
    return n/10

probabilidade = []
for i in possibilidades:
    if i < 80:
        probabilidade.append(3)
    if i == 80:
        probabilidade.append(20)
    if i > 80:
        probabilidade.append(1)

# visualização da probabilidade funcionando e se a soma é igual a  100
# print(probabilidade)
# print(reduce(lambda ac, i: i + ac, probabilidade, 0))

# Quantas vezes eu quero rodar o aleatorizador
amostragem = 1000000

# cria-se uma lista  com as respostas do aleatorizador
escolhas = list(random.choices(possibilidades, probabilidade, k=amostragem))

# coloco em ordem a lista
escolhas.sort()

# Contando quantas vezes aparece cada número
contador = 0


for i,n in enumerate(escolhas):

    if escolhas[i] == escolhas[i-1]:
        continue
    else:
        print(f'o valor {formata_tempo(n)} apareceu {escolhas.count(n)} vezes e tem {round(escolhas.count(n)/amostragem*100)} % de chance de sair ')



# pensando em uma forma de contar quantas vezes sai as possibilidades

# for index in range(amostragem):
#     for x in escolhas: #para cada x in escolhas
#         if x in escolhas.items:
#
#
#
#
#
#
#
# porcentagem_red = (red / contador) * 100
# porcentagem_black = (black / contador) * 100
# porcentagem_green = (green / contador) * 100
# porcentagem_white = (white / contador) * 100
# total_porcentagem = porcentagem_green + porcentagem_black + porcentagem_red
#
# print(f' o red saiu no total de {red} vezes. sua porcentagem é de {porcentagem_red} %')
# print(f' o green saiu no total de {green} vezes. sua porcentagem é de {porcentagem_green} %')
# print(f' o black saiu no total de {black} vezes. sua porcentagem é de {porcentagem_black} %')
# print(f' o white saiu no total de {white} vezes. sua porcentagem é de {porcentagem_white} %')
#
# print(f' porcentagem total  = {total_porcentagem}')
