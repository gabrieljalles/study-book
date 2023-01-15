hora_atual = input("Quantas horas ?")

if hora_atual.isnumeric():
    hora_atual = int(hora_atual)
    if hora_atual >=0 and hora_atual<=11:
        print("bom dia")
    elif hora_atual >= 12 and hora_atual<= 17:
        print("boa tarde")
    elif hora_atual >= 18 and hora_atual<= 23:
        print("boa noite")
    else:
        print("precisa digitar um número entre 0 e 23 horas")
else:
    print("digite um número valido")





