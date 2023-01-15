
while True:
    print()
    num_1 = input("digite um número")
    num_2 = input("digite outro número")
#============================================
    if num_1.isnumeric() and num_2.isnumeric():
        num_1 = int(num_1)
        num_2 = int(num_2)
    else:
        print("digite um valor válido.")
        continue
#===========================================

    operador = input ("digite um operador:")
    # +  - / *
    if operador == "+":
        print(num_1 + num_2)
    elif operador == "-":
        print(num_1 - num_2)
    elif operador == "/":
        print(num_1 / num_2)
    elif operador == "*":
        print(num_1 * num_2)
    else:
        print("operador inválido")

    sair = input("deseja sair ? [s]im [n]ão")
    if sair == "n":
        pass
    elif sair == "s":
        break
    else:
        print("digite um valor válido")








