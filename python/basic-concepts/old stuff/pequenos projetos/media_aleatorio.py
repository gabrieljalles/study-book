import random

possibilidades = ['preto', 'verde', 'vermelho']
k = 1000
escolhas = random.choices(possibilidades, [7, 7, 1], k=k)

contador = 0
contagem_fila = []
soma = 0

for item in escolhas:
    if not item == 'preto':
        contador += 1
    else:
        contagem_fila.append(str(contador))
        contador = 0

for item in contagem_fila:
    soma += int(item)
    media = round(soma / len(contagem_fila), 2)

set_contagem = set(contagem_fila)


print("..............Representando simplificado...............")
contador_possibilidades1 = [(x, contagem_fila.count(x))for x in set_contagem]
print(contador_possibilidades1)


print("..............Representando em texto...................")
for i in set_contagem:
    contador_possibilidades = 0
    for x in contagem_fila:
        if i == x:
            contador_possibilidades += 1
    print(f'o número {i} saiu um total de {contador_possibilidades} vezes')

print(f' A cada {media} possibilidades em média, sai o preto')
print(f'para jogar {k} vezes é necessário {30*k/86400} dias')


