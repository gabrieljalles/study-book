import random

possibilidades = ['red', 'black', 'green', 'white']  # set # ferramentas usadas
escolhas = random.choices(possibilidades, [50, 29, 20, 1], k=10000000)

red = 0
black = 0
green = 0
white = 0
contador = 0

for x in escolhas:

    contador += 1
    if x == 'red':
        red += 1
    if x == 'green':
        green += 1
    if x == 'black':
        black += 1
    if x == 'white':
        white += 1

porcentagem_red = (red / contador) * 100
porcentagem_black = (black / contador) * 100
porcentagem_green = (green / contador) * 100
porcentagem_white = (white / contador) * 100
total_porcentagem = porcentagem_green + porcentagem_black + porcentagem_red

print(f' o red saiu no total de {red} vezes. sua porcentagem é de {porcentagem_red} %')
print(f' o green saiu no total de {green} vezes. sua porcentagem é de {porcentagem_green} %')
print(f' o black saiu no total de {black} vezes. sua porcentagem é de {porcentagem_black} %')
print(f' o white saiu no total de {white} vezes. sua porcentagem é de {porcentagem_white} %')

print(f' porcentagem total  = {total_porcentagem}')
