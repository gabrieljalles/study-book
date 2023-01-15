"""
Listas em python
"""
secreto = 'perfume'
digitados = []
chances = 5

print("----Seja bem vindo ao jogo da forca----")


while True :
    if chances < 0:
        print('Você perdeu!!! suas chances acabaram')
        break
    print(f"suas chances atuais são de {chances}")
    letra = input('Digite uma letra:')

    if len(letra) > 1:  # forçar o usuário a digitar uma letra por vez
        print('ahhhhh isso não vale, digite apenas uma letra.')
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f'parabéns a letra "{letra}" tem na palavra secreta')

    else:
        print(f' Quee penaaa !!!! letra "{letra}" não tem na palavra secreta')
        digitados.pop()
        chances -= 1

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'você descobriu a palavra secreta, {secreto_temporario}')
        break
    else:
        print(f'atualmente a palavra secreta está {secreto_temporario}')




