secreto = 'python'

secreto_temporario = ''
digitadas = ['t']

for letra_secreta in secreto:
    print(f'iteração para a letra {letra_secreta}')

    if letra_secreta in digitadas:
        print (f'eba, a letra que eu queria {letra_secreta}')
        secreto_temporario += letra_secreta
    else:
        secreto_temporario += "*"


print(secreto_temporario)