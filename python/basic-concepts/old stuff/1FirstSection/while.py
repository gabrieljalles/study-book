"""
utilizado para realizar ações enquanto uma condição for verdadeira
"""
x = 0
while x <= 100:
    print(x)
    x= x+1

print('acabou!')

#quando o while encontra a palavra continue, ele pula o passo atual e vai pro próximo laço
#observe o exemplo
y = 0
while y < 10:
    if y == 3:  # estou dizendo que  quando x for igual a 3, não execute os códigos do while e passe para o próximo laço
        y = y+1  # para que o programa não fique para sempre no y = 3, precisamos somar o y dentro da condição.
    print(y)  # com isso, quando o programa chega em 3, ele não digita o valor 3 , pula ele.
    y = y + 1

print('Acabou !')



