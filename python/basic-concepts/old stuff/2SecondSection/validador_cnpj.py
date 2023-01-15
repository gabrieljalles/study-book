"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""

# '04.252.011/0001-10'

from random import randint

reverso = 5
total = 0
contador = 0

def tratador_cnpj(valor):
    valor_semponto = valor.replace('.','')
    valor_sembarra = valor_semponto.replace('/','')
    valor_limpo = valor_sembarra.replace('-','')
    return str(valor_limpo)

def cnpj_semdigito(valor):
    cnpj_semdigito = valor[:-2]
    return cnpj_semdigito

def validador_cnpj(cnpj):
    global contador
    global reverso
    global total

    novo_cnpj = (cnpj_semdigito(tratador_cnpj(cnpj)))
    cnpj_test = tratador_cnpj(cnpj)

    for i in range(25):
        if i > 11:
            i -= 12

        total += int(novo_cnpj[i]) * reverso

        reverso -= 1
        if reverso < 2 and contador == 0:
            reverso = 9
            contador += 1
        elif reverso < 2 and contador == 1:
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            novo_cnpj += str(d)
            reverso = 6
            total = 0
            contador += 1
        elif reverso < 2 and contador == 2:
            reverso = 9
            contador += 1
        elif reverso < 2 and contador == 3:
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            novo_cnpj += str(d)

    if novo_cnpj == cnpj_test:
        return cnpj_original
    else:
        return False

cnpj_original = input('digite o cnpj para verificar:')
teste = validador_cnpj(cnpj_original)

if teste:
    print(f'esse cnpj {cnpj_original} é valido')
else:
    print(f'esse cnpj {cnpj_original} NÃO é valido')


