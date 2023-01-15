from random import randint

while True:
    numero = str(randint(100000000, 999999999))
    #cpf = input("digite um cpf")
    # novo_cpf = cpf[:-2]  #eliminando os dois últimos algarismos
    novo_cpf = numero
    reverso = 10 #variável que decai em cada ciclo
    total = 0 #somatorio após a multiplição


    for index in range(19): #19 porque o programa percorre a criação dos dois digitos
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso


        reverso -= 1
        if reverso < 2:
            reverso = 11
            d= 11 - (total % 11)

            if d >9:
                d=0
            total = 0
            novo_cpf += str(d)

    lista = []
    lista.append(novo_cpf)
    print(lista)



